"""Opt-in, bounded observations of two fixed source-backed seeds. Standard library only."""
import argparse
import csv
import datetime as dt
import hashlib
import html
import http.client
import ipaddress
import json
import multiprocessing as mp
import pathlib
import queue
import re
import socket
import ssl
import time

MAX_BODY = 16384
TIMEOUT = 10.0
SEEDS = [
    {"seed_id": "CSAI-TLS-2083", "scheme": "https", "host": "media.fastcdn.bar", "port": 2083,
     "source_urls": ["https://tria.ge/261027-qmb8eaes6q/behavioral1", "https://securelist.com/tr/cyberstrikeai-attacks/121715/"],
     "source_basis": "Exact domain/port from public sandbox task, matched to vendor-reported sample/domain."},
    {"seed_id": "CSAI-ELF-HTTP-8443", "scheme": "http", "host": "23.254.195.48", "port": 8443,
     "source_urls": ["https://datalake.abuse.ch/malware-bazaar/daily/2026-11-06.zip"],
     "source_basis": "Previously locally verified static CyberStrikeAI ELF configuration; source record CS-0FFC40CB2339 and provenance/new-candidate-evidence.json. Archive URL is acquisition provenance, not proof of campaign targeting."},
]


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def title_from_prefix(body):
    m = re.search(r"<title\b[^>]*>(.*?)</title\s*>", body.decode("utf-8", "replace"), re.I | re.S)
    if not m:
        return None
    value = " ".join(html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).split())[:160]
    return re.sub(r"(?i)(token|password|secret|api[_ -]?key)\s*[:=]\s*\S+", r"\1=[REDACTED]", value)


def cert_time(value):
    return dt.datetime.fromtimestamp(ssl.cert_time_to_seconds(value), dt.timezone.utc).isoformat().replace("+00:00", "Z") if value else None


def worker(seed, channel, raw_dir):
    started = time.monotonic()
    r = {"seed_id": seed["seed_id"], "endpoint": f'{seed["scheme"]}://{seed["host"]}:{seed["port"]}/',
         "origin": "analyst_first_party_bounded_network_observation", "publication_category": "first-party-observations",
         "observation_started_at_utc": utc(), "source_urls": seed["source_urls"], "source_basis": seed["source_basis"],
         "india_targeting_established": False, "actor_activity_established": False, "current_c2_success_established": False,
         "origin_server_identified": False, "global_novelty_claimed": False, "http_requests_sent": 0,
         "redirects_followed": 0, "body_capture_limit_bytes": MAX_BODY,
         "dns": {"performed": False, "resolver_scope": "No DNS: seed is an IP literal."}, "tls": {"attempted": False},
         "http": None, "status": "started"}

    def update():
        channel.put(dict(r))

    sock = None
    try:
        try:
            literal = ipaddress.ip_address(seed["host"])
            if not literal.is_global:
                raise ValueError("non_global_seed")
            family = socket.AF_INET6 if literal.version == 6 else socket.AF_INET
            address = seed["host"]
        except ValueError:
            if seed["host"] != "media.fastcdn.bar":
                r["status"] = "non_global_seed_refused"; update(); return
            r["dns"] = {"performed": True, "resolver_scope": "OS-configured system resolver via getaddrinfo; results may be cached; recursive resolver identity not established.", "queried_name": seed["host"], "observed_at_utc": utc()}
            infos = socket.getaddrinfo(seed["host"], seed["port"], type=socket.SOCK_STREAM)
            values = sorted({x[4][0] for x in infos})
            r["dns"]["answers"] = values
            safe = [x for x in infos if ipaddress.ip_address(x[4][0]).is_global]
            safe.sort(key=lambda x: x[0] != socket.AF_INET)
            if not safe:
                r["status"] = "no_global_dns_answer"; update(); return
            family, _, _, _, peer = safe[0]
            address = peer[0]
        r["connected_address_candidate"] = address
        r["status"] = "connecting"; update()
        sock = socket.socket(family, socket.SOCK_STREAM)
        sock.settimeout(max(0.1, TIMEOUT - (time.monotonic() - started)))
        sock.connect((address, seed["port"]))
        r["connected_peer_ip"] = sock.getpeername()[0]
        if seed["scheme"] == "https":
            r["tls"] = {"attempted": True, "server_name": seed["host"], "validation_policy": "Default system trust and hostname verification; failures not bypassed."}
            r["status"] = "tls_handshake"; update()
            sock = ssl.create_default_context().wrap_socket(sock, server_hostname=seed["host"])
            der = sock.getpeercert(binary_form=True)
            cert = sock.getpeercert()
            r["tls"].update({"validated": True, "leaf_der_sha256": hashlib.sha256(der).hexdigest(),
                             "subject_alt_names": [{"type": k, "value": v} for k, v in cert.get("subjectAltName", [])],
                             "not_before_utc": cert_time(cert.get("notBefore")), "not_after_utc": cert_time(cert.get("notAfter")),
                             "observed_at_utc": utc(), "scope_note": "Certificate identifies the presented TLS endpoint; a CDN/shared certificate does not establish origin IP, operator ownership or maliciousness."})
            if raw_dir:
                pathlib.Path(raw_dir).mkdir(parents=True, exist_ok=True)
                (pathlib.Path(raw_dir) / (seed["seed_id"] + "-leaf.der")).write_bytes(der)
            update()
        sock.settimeout(max(0.1, TIMEOUT - (time.monotonic() - started)))
        host_header = f'{seed["host"]}:{seed["port"]}'
        request = f"GET / HTTP/1.1\r\nHost: {host_header}\r\nUser-Agent: bounded-seed-observer/1.0\r\nAccept: */*\r\nConnection: close\r\n\r\n".encode("ascii")
        r["http_requests_sent"] = 1
        r["status"] = "http_request_attempted"
        update()
        sock.sendall(request)
        response = http.client.HTTPResponse(sock)
        response.begin()
        r["http"] = {"status_code": response.status, "observed_at_utc": utc()}
        r["status"] = "http_headers_received"; update()
        body = response.read(MAX_BODY)
        r["http"].update({"title": title_from_prefix(body), "captured_body_bytes": len(body),
                           "captured_body_sha256": hashlib.sha256(body).hexdigest(),
                           "body_hash_scope": "Only the first up to 16384 body bytes; not necessarily the full response.",
                           "body_limit_reached": len(body) == MAX_BODY})
        r["status"] = "http_response_observed"
    except ssl.SSLCertVerificationError as e:
        r["status"] = "tls_validation_failed"
        r["tls"].update({"validated": False, "verify_code": e.verify_code})
    except (socket.timeout, TimeoutError):
        r["status"] = "timeout"
    except socket.gaierror:
        r["status"] = "dns_failed"
    except (OSError, http.client.HTTPException, ValueError) as e:
        r["status"] = "connection_or_protocol_failed"
        r["error_type"] = type(e).__name__
        r["error_errno"] = getattr(e, "errno", None)
    finally:
        if sock:
            try: sock.close()
            except OSError: pass
        r["observation_finished_at_utc"] = utc()
        r["elapsed_seconds"] = round(time.monotonic() - started, 3)
        update()


def observe(seed, raw_dir=None):
    context = mp.get_context("spawn")
    channel = context.Queue()
    child = context.Process(target=worker, args=(seed, channel, raw_dir), daemon=True)
    child.start()
    deadline = time.monotonic() + TIMEOUT
    result = None
    while time.monotonic() < deadline:
        try:
            result = channel.get(timeout=min(0.1, max(0.001, deadline-time.monotonic())))
            if "observation_finished_at_utc" in result:
                break
        except queue.Empty:
            if not child.is_alive():
                break
    if child.is_alive():
        child.terminate()
        child.join(timeout=1)
    else:
        child.join(timeout=1)
    if result is None:
        result = {"seed_id": seed["seed_id"], "endpoint": f'{seed["scheme"]}://{seed["host"]}:{seed["port"]}/',
                  "origin": "analyst_first_party_bounded_network_observation", "publication_category": "first-party-observations", "http_requests_sent": 0}
    if "observation_finished_at_utc" not in result:
        result.update({"status": "bounded_timeout", "observation_finished_at_utc": utc(), "elapsed_seconds": TIMEOUT,
                       "limit_note": "Worker stopped at total endpoint time budget, including DNS/handshake/read; no retry."})
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--observe", action="store_true", help="Explicitly authorize the two fixed standard network observations.")
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--raw-cert-dir", help="Optional local-only certificate DER directory; never publish it.")
    args = ap.parse_args()
    if not args.observe:
        ap.error("No network requests made. Pass --observe to opt in.")
    rows = [observe(seed, args.raw_cert_dir) for seed in SEEDS]
    doc = {"schema_version": "1.0", "generated_at_utc": utc(), "observation_count": len(rows),
           "scope": "Two fixed source-backed seeds; one GET / maximum per endpoint; no retries, redirects, credentials or exploitation.",
           "limitations": "Point-in-time endpoint responses/DNS/certificates are not proof of C2 activity, actor identity, origin ownership or India targeting. Negative results are observations, not new IOCs.",
           "observations": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(doc, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "results": [{"seed_id": r["seed_id"], "status": r["status"], "http_requests_sent": r.get("http_requests_sent", 0)} for r in rows]}))


if __name__ == "__main__":
    main()

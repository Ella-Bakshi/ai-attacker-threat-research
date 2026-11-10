# First-party bounded seed observations

On 2026-11-10 at about 18:41 UTC, we performed two independent, ordinary endpoint reads against previously source-backed seeds. These are our own point-in-time measurements, separate from provider observations and from claims about malicious activity.

| Seed | Observation | Scope |
|---|---|---|
| `https://media.fastcdn.bar:2083/` | Normal TLS validation passed; HTTP 521 | Presented certificate and DNS/CDN endpoint context. Does not establish the origin server or a functioning C2. |
| `http://23.254.195.48:8443/` | HTTP 404 | The root path answered at that moment; no registration, agent, command or administration paths were requested. |

The domain seed came from [public sandbox evidence](https://tria.ge/261027-qmb8eaes6q/behavioral1) matched to [vendor reporting](https://securelist.com/tr/cyberstrikeai-attacks/121715/). The IP/port came from the previously verified local ELF configuration, catalog record `CS-0FFC40CB2339`; its [MalwareBazaar daily archive](https://datalake.abuse.ch/malware-bazaar/daily/2026-11-06.zip) is acquisition provenance. These existing seeds were not newly discovered by the HTTP requests.

The TLS leaf DER SHA256 was `e162a97e2912879e1117c777a002dd35a00e317eb3dd2a021310798360e07e1a`, with SANs `fastcdn.bar` and `*.fastcdn.bar`, valid from 2026-11-01 to 2027-01-30. The local system resolver returned `104.21.48.8` and `172.67.175.42`; the first address was contacted. These DNS addresses are shared CDN context, not newly attributed origin/C2 IPs or standalone blocklist entries.

The collector sends at most one `GET /` per seed, follows no redirects, performs no authentication/POST/admin/exploit requests, uses normal TLS trust/hostname validation and allows at most ten seconds per endpoint including DNS. It captures at most 16 KiB of response body in memory. The sanitized export includes status, a sanitized title if present, and the hash/length of only the captured prefix. It contains no response body, response headers, credentials or cookies. A certificate proves what was presented by the TLS endpoint, not ownership, maliciousness or an origin address.

Run only when another measurement of these same seeds is intended:

```powershell
python -B scripts/observe_two_seeds.py --observe --output first-party-observations-new.json
```

Without `--observe`, no network action occurs. The optional `--raw-cert-dir` stores a leaf DER certificate locally; keep that directory outside publication. No additional scan, retry, redirect, TLS bypass, successful C2 exchange, attacker activity, India targeting or global novelty is claimed. A negative/error response remains an observation, not a new IOC.

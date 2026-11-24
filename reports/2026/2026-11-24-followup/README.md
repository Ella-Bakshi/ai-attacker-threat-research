# 24 November 2026 follow-up

This follow-up adds **six evidence records**, all new to the catalog, and **one historical IP** to the map. The record IDs and locators are published with the original source roles. [Records](records.json) · [CSV](records.csv) · [Counts](summary.json)

## NVISO incident response

NVISO reported ARTEX deploying the ZQAgent backdoor in a Belgian incident. Its publication gives a configured C2 IP and domain, three ZQAgent SHA-256s, and the initial path it observed on disk. Those are six separately scoped records. The IP entered the map. The configured domain remains a domain record. Exact event dates and current operation are unknown. The first-party evidence belongs to NVISO. This review rechecked the publisher's literals and added zero independently derived malicious IOCs. [NVISO original investigation](https://blog.nviso.eu/2026/11/23/artex-fog0003-zqagent-backdoor/)

Previdian's existing HTTP honeypot evidence was rechecked. Its published marked traffic describes attempts and simulated responses. The source cannot determine the tool or operator solely from a request string. Existing records retain those limits. [Previdian telemetry](https://blog.previdian.com/artex-traffic-previdian-threat-intelligence-report-november-2026/)

## Pilot sensor selection

The best initial fit is a static HTTP decoy on a dedicated owned host, using NGINX for allowlisted local access logs. It is a low-interaction sensor. It records UTC time, measured peer address, event ID, method, sanitized path, User-Agent and response status. Ingress observations support the role of request source. Confirming software or C2 requires additional evidence. [NGINX logging](https://nginx.org/en/docs/http/ngx_http_log_module.html) · [Trusted peer handling](https://nginx.org/en/docs/http/ngx_http_realip_module.html)

Beelzebub is a packaged alternative for richer HTTP responses. Raw events can contain sensitive fields, so validate local data minimization before pilot use. Cowrie is complementary if SSH traffic becomes a research priority. OpenCanary's stock HTTP login handler records submitted credentials. DShield's stock setup submits logs for community research. T-Pot's multi-protocol deployment has higher system requirements. [Beelzebub observability](https://docs.beelzebub.ai/operations/observability/) · [Cowrie events](https://docs.cowrie.org/en/stable/OUTPUT.html) · [OpenCanary HTTP source](https://github.com/thinkst/opencanary/blob/master/opencanary/modules/http.py) · [DShield](https://isc.sans.edu/tools/honeypot/) · [T-Pot requirements](https://github.com/telekom-security/tpotce#system-requirements)

The sensor is a proposed build. The 35 unresolved catalog relationships and 25 private leads remain separate. No candidate endpoint was contacted for this review.

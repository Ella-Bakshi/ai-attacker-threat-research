# Deep Huntio

Report date: 2026-11-04. Collection reviewed: 2026-11-10. Source: [deep_huntio](https://hunt.io/blog/artex-south-korea-bank-infrastructure). This folder contains 39 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `u6ud2s[.]dnslog[.]cn` | domain | DNS callback hostname referenced by the staged exploitation artifact | Low | campaign-context |
| `23[.]248[.]226[.]250` | ipv4 | Hong Kong jump host with exposed directories and supporting tooling | Medium | campaign-context |
| `38[.]244[.]50[.]120` | ipv4 | ARTEX console host and SSH tunnel destination referenced in recovered configuration | Medium | campaign-context |
| `23[.]248[.]226[.]250:18099` | network_endpoint | Exposed directory containing 42 files across two subdirectories | Medium | campaign-context |
| `23[.]248[.]226[.]250:8001` | network_endpoint | Directory hosting the JNDI/LDAP exploitation setup | Medium | campaign-context |
| `38[.]244[.]50[.]120:8000` | network_endpoint | Exposed directory containing scripts and supporting files | Medium | campaign-context |
| `ARTEX - Autonomous security assessment console` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX - Bảng điều khiển kiểm thử xâm nhập tự động` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX - Console de Teste de Penetração Autônomo` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX - консоль автономного пентеста` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX - 自主渗透测试控制台` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX - 自律型ペネトレーションテスト管理画面` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX - 자율  침투  테스트  콘솔` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `ARTEX: Autonomous Penetration Testing Console` | html_title | Localized ARTEX console title | Low | software-fingerprints |
| `c7a884afcd7f91408921890d9617bef6bfac3dae992bc25bb9c48c0395a60842` | tls_certificate_sha256 | TLS certificate associated with 38.244.50[.]120, with issuer organization ARTEX | Medium | software-fingerprints |
| `Exp2588` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `Poc2588` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `agt.py` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `agt4.py` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `aio_uaf.c` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `cloudphone-oversea.key` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `cve3493-static` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `cve5054-static` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `exp2588_44` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `ios26_probe.c` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `les.sh` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `payload-dumper-go.exe` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `poc65343_probe.c` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `recv.py` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `relay.py` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `server.py` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `shells.log` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `stub.c` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `stub65343.c` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `tg.conf` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `tg.py` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `wxapkg-watchdog.sh.__rev2` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `x.js` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |
| `x.sh` | filename | Exposed supporting-tool/artifact filename | Low | supporting-tools |

[Evidence methodology](../../../docs/methodology.md).

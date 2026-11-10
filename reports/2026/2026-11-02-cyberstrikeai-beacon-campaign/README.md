# Cyberstrikeai Beacon Campaign

Report date: 2026-11-02. Collection reviewed: 2026-11-10. Source: [securelist](https://securelist.com/tr/cyberstrikeai-attacks/121715/). This folder contains 24 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `d3.b64` | filename | Script-fragment staging filename observed in described intrusion | Low | campaign-context |
| `C:\ProgramData\dsn_line.txt` | path | DSN/DPAPI credential-related staging path described by Kaspersky | Low | campaign-context |
| `fastcdn[.]bar` | domain | C2 for Windows Beacon | Medium | main-iocs |
| `media[.]fastcdn[.]bar` | domain | C2 for Linux Beacon | Medium | main-iocs |
| `104[.]234[.]26[.]163` | ipv4 | C2 for Payload Delivery + Linux Beacon | Medium | main-iocs |
| `185[.]186[.]245[.]144` | ipv4 | C2 for Windows Beacon | Medium | main-iocs |
| `09e1da2afa1216ecc55648ec8e122d2a` | md5 | CyberStrikeAI Linux Beacon | High | main-iocs |
| `2770562d104391b92b42671c270079bb` | md5 | CyberStrikeAI Windows Beacon / c:\windows\temp\svcmon32.exe c:\programdata\svcmon32.exe | High | main-iocs |
| `805b9e4ae74c903787416800999b8418` | md5 | CyberStrikeAI Linux Beacon | High | main-iocs |
| `d726a8b4886c636f76ca6d30ef6a6ff4` | md5 | CyberStrikeAI Windows Beacon / c:\windows\temp\svchosts.exe | High | main-iocs |
| `c:\programdata\svcmon32.exe` | path | Observed CyberStrikeAI Windows Beacon | Low | software-fingerprints |
| `c:\windows\temp\svchosts.exe` | path | Observed CyberStrikeAI Windows Beacon | Low | software-fingerprints |
| `c:\windows\temp\svcmon32.exe` | path | Observed CyberStrikeAI Windows Beacon | Low | software-fingerprints |
| `(nohup <path_to_beacon> &>/dev/null &)` | persistence_pattern | Linux shell-startup pattern described from implementation | Low | software-fingerprints |
| `@reboot <path_to_beacon> &` | persistence_pattern | Linux crontab startup pattern described from implementation | Low | software-fingerprints |
| `SystemUpdate` | registry_value_name | Alternative source-implementation Run-value name | Low | software-fingerprints |
| `Backdoor.CyberStrikeAI.HTTP.C&C` | vendor_detection_name | Kaspersky NDR verdict for characteristic CyberStrikeAI communications | Medium | software-fingerprints |
| `0bbd08af95f877f1d568b03de2eb76b4` | md5 | Tools & Scripts / c:\ProgramData\p1.ps1 (reverse shell PS script) | High | supporting-tools |
| `29efd64dd3c7fe1e2b022b7ad73a1ba5` | md5 | Tools & Scripts / C:\Windows\Temp\wdiag2.exe (mimikatz) | High | supporting-tools |
| `74f57b3e897a4960dcdd5b7e8a54f9df` | md5 | Tools & Scripts / c:\rwx\RogueWinRM.exe | High | supporting-tools |
| `185[.]186[.]245[.]144:5501` | network_endpoint | Reverse-shell PS payload callback endpoint | Low | supporting-tools |
| `C:\Windows\Temp\wdiag2.exe` | path | Observed Tools & Scripts | Low | supporting-tools |
| `c:\ProgramData\p1.ps1` | path | Observed Tools & Scripts | Low | supporting-tools |
| `c:\rwx\RogueWinRM.exe` | path | Observed Tools & Scripts | Low | supporting-tools |

[Evidence methodology](../../../docs/methodology.md).

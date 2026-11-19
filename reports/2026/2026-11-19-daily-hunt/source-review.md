# Primary reporting review: 19 November 2026

The source lane prepared: **212 memberships**, **206 values new to the baseline master**, and six existing-value corroborations. The combined report applies deduplication across these and the separate native-analysis memberships.

| Source and publication | Records | Scope |
|---|---:|---|
| Darktrace, 18 November | 12 | Five historical incident memberships, five shared-service contexts and two qualified appendix filename references |
| huntback, 17 November | 7 | Two workspace exposure leads and five artifact references; authorization and compromise unestablished |
| ReversingLabs, 18 November | 193 | 184 operator-binary SHA256 references and nine console favicon hashes, all software fingerprints |

## Historical network roles

[Darktrace's original investigation](https://www.darktrace.com/fr/blog/agentic-attacks-in-the-wild-inside-three-artex-investigations) supplies two existing BLOODALCHEMY C2 values with a 23 October–2 November communication window. The report's broader ARTEX association is separate from the malware C2 role. It newly describes `213[.]111[.]150[.]145:8099` delivering wisp-agent on 5 November, and `43[.]98[.]196[.]73` as the source of 20 October Azure intrusion activity with **no observed C2**. Attempts to an existing address on 1–2 November remain attempt evidence. Shared paste/file/tunnel services are nonindicative context at score 0.

[huntback's original workspace review](https://huntback.io/blog/inside-cyberstrikeai-221-tool-executions-disabled-approval-gate) identifies `38[.]76[.]169[.]207` and TCP 8010 as the source of exposed session artifacts. Its two hashes identify a database and log, not malware. The source expressly leaves operator identity, authorization and victim compromise unresolved; agent claims are not successful-intrusion evidence. The normalized endpoint joins adjacent host/service rows, with that derivation recorded. No database, retained credentials or target data were downloaded by this lane.

## Software references

[ReversingLabs' original notebook](https://www.reversinglabs.com/blog/threat-researchers-notebook-detection-strategies-for-artex-and-related-forks) provides 184 controller/operator hashes and nine favicon hashes. These are dual-use software identities at score 20. The binary list does not map each entry to a particular fork, platform, version or operator. Two favicon references belong to AntiFox; icon sizes/brand labels are not release versions. Two binary hashes and the original ARTEX favicon were already catalogued. A separately known trojanized hash remains malicious only through its separate existing source membership.

The linked public host CSV returned HTTP 403 to a normal GET. No rows were acquired or reconstructed, and no 3,096-host substitute is proposed. The article itself warns against treating its infrastructure map as a perimeter block list. Its disproved tracking-pixel theory was not promoted to a detection.

## Other news reviewed

Qualys' visible article is updated 18 November; its metadata distinguishes original publication on 16 November from the later modification. CERT-EU's original ARTEX advisory is dated 5 November. Neither supplies a new literal IOC set in the reviewed text. Microsoft’s 29 October North Korea AI-tradecraft article supplies broader adoption context without an IOC table. The newer GTIG report was handed to root for separate review. Third-party reports and ARTEX.sh were discovery aids, not independent corroborating publishers.

All evidence uses original-publication/retrieval dates with their stated precision. No active host requests, DNS resolution, malware execution, scans, submissions, paid-provider calls or commercial exports were used.

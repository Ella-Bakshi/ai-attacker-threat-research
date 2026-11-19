# Historical DNS context from a public Censys figure

On 19 November 2026 we independently transcribed one historical DNS association from a [figure in Censys's 12 November article](https://censys.com/blog/artex-and-ai-attack-tools-why-threat-intelligence-must-originate-from-first-party-data). A second reviewer separately confirmed the same literal and dates.

The [original public image](https://censys.com/wp-content/uploads/image-340.png) displays `tongcanghuanqiu.com` in the Associated Domains table for `43[.]255[.]159[.]10`. Its displayed DNS first/last times are **22 October 2026, 11:19 and 17:01 UTC**, to minute precision. The host's separate historical as-of time is **9 November, 16:23 UTC**.

This is **one new nonindicative context value**, with score **0**. The image does not establish that the domain ran ARTEX, belonged to an attacker, delivered malware or acted as C2. We did not resolve the domain or contact the address. The host's ARTEX badge and vendor reputation assessment remain separate observations; the provider's score 93 is not our evidence score.

[Structured evidence](public-figure-evidence.json) preserves the image identity, exact visual locator, date meanings and limits. [Observation JSON](observations.json) and [CSV](observations.csv) contain the scoped record. This is public-artifact analysis, not a first-party sensor discovery or independently acquired DNS telemetry. No global-first claim is made. Raw image copies remain private.

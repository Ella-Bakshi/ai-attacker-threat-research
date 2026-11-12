# ARTEX source and fork review

Reviewed **12 November 2026**, following [Andrea Palmieri's 8 November article](https://andpalmier.com/posts/artex-source-behind-iocs/). [Machine-readable annotations and fork markers](artex-source-review.json).

## Our pinned-source check

At BaaRai revision `81eab87d166dddfc0d8be2707eadec788b61be0d`, all 379 tracked Go files were inspected for `ProbeSite` and `ResolveDomain`. Only declarations, definitions and comments were found. Worker wiring stores the engine; construction and function presence do not establish invocation. This independently corroborates the article's concern in **our existing source revision**, rather than generalizing from its different upstream release.

Records `AR-F701725362AE` and `AR-3EF7E3FFA9FC` retain valid static evidence. They do **not** demonstrate target egress or an effective traffic rule. No binary was executed or native runtime call graph established. The JSON pins the interface, setter, worker and enrichment definitions; historical records remain intact.

## Historical realm and meaningful forks

The Unit 42 realm observation, `AR-1D971BC82C43`, remains valid historical evidence. [RuoJi6's 3 November commit](https://github.com/RuoJi6/ARTEX/commit/520317636467fe9a45052b7f1ebdcf8f0805924f) replaced the optional ARTEX realm with generic `Restricted` and removed service/version from public health output. A [subsequent commit](https://github.com/RuoJi6/ARTEX/commit/f053931a1df57916d5132a42f8920adf2f9aa842) gated health behind the optional authentication layer. These are fork/configuration/version facts. Chronology does not establish motive. `Restricted` is not a replacement ARTEX IOC; absence of the older marker is inconclusive.

Three article-linked fork UAs were independently checked against immutable header-assignment sites:

| Fork | Source-present User-Agent | Scope |
|---|---|---|
| [panda0x123/artex-ymh](https://github.com/panda0x123/artex-ymh/blob/48adc7f1d8f62cbc47e658c9a2b47d6f63ca6cb1/session/http_shell.go#L257) | `Mozilla/5.0 (ARTEX)` | HTTP-shell path |
| [200210xsb/artex-full](https://github.com/200210xsb/artex-full/blob/97d4960495421abc557060251eddcf761f3001c9/server/nuclei.go#L1402) | `Mozilla/5.0 (compatible; ARTEX-Nuclei-Fingerprint/1.0)` | HTTP fingerprinting helper |
| [luojiaping/ARTEX](https://github.com/luojiaping/ARTEX/blob/7baca5dda545bee3df3601453a99c8002af97722/credhunt/probe.go#L460) | `ARTEX-CredHunter/2.0` | Requests to model providers; not generic victim traffic |

These software references remain outside admitted IOC totals. Exact source presence is verified; runtime execution, deployment, specificity and malicious use are unestablished. They were previously published by the article's author, not first discovered by us.

## Lab evidence limits

The article's lab used a component harness, fake LLM and owned listener. Its TLS and timing results depend on versions and recording/proxy settings. We did not reproduce those experiments. No lab JA4 values were promoted to standalone IOCs. This review adds no malicious infrastructure, map points or India-targeting evidence.

rule RND_CyberStrikeAI_Fork_Egress_Gateway
{
    meta:
        description = "Identify the public RuoJi6 fork egress gateway; not a malware verdict"
        reference = "https://github.com/RuoJi6/CyberStrikeAI/tree/db4a8be2b66805ecfef077286f334b3b94307c6c"
        date = "2026-11-10"
    strings:
        $module = "cyberstrike-ai/internal/egress" ascii
        $blocked = "X-CyberStrikeAI-Blocked" ascii
        $reason = "X-CyberStrikeAI-Block-Reason" ascii
        $realm = "CyberStrike network provenance" ascii
    condition:
        uint32(0) == 0x464c457f and filesize < 32MB and all of them
}

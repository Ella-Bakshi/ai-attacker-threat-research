/* Research fingerprints, 2026-11-10. Matches identify framework code/assets,
   including legitimate installations. They do not establish malicious intent. */

rule RND_ARTEX_Go_Controller
{
    meta:
        author = "Local IOC research"
        date = "2026-11-10"
        purpose = "ARTEX Go executable identification; not a malware verdict"
        reference = "https://github.com/BaaRai/ARTEX/releases/tag/v0.5.1"
    strings:
        $module = "github.com/Autumn-27/artex" ascii
        $ua = "artex-enrich/1.0" ascii
        $auth = "/api/auth/status" ascii
    condition:
        filesize < 128MB and
        (uint16(0) == 0x5a4d or uint32(0) == 0x464c457f) and
        all of them
}

rule RND_ARTEX_Web_API_Client
{
    meta:
        author = "Local IOC research"
        date = "2026-11-10"
        purpose = "Identify current ARTEX web API source/bundle; title-independent"
        reference = "https://github.com/BaaRai/ARTEX/blob/81eab87d166dddfc0d8be2707eadec788b61be0d/web/src/lib/api.ts"
    strings:
        $token = "artex_token" ascii
        $status = "/auth/status" ascii
        $init = "/auth/init" ascii
        $sessions = "/exploration/main-sessions" ascii
    condition:
        filesize < 128MB and all of them
}

rule RND_CyberStrikeAI_Console_HTML_Structure
{
    meta:
        author = "Local IOC research"
        date = "2026-11-10"
        purpose = "Title-independent current console DOM identification"
        reference = "https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/web/templates/index.html"
    strings:
        $id_c2 = "id=\"submenu-c2\"" ascii
        $id_mcp = "class=\"mcp-exec-stats-root\"" ascii
        $id_webshell = "id=\"webshell-batch-probe-btn\"" ascii
    condition:
        filesize < 128MB and all of them
}

rule RND_CyberStrikeAI_C2_Transport_Implementation
{
    meta:
        author = "Local IOC research"
        date = "2026-11-10"
        purpose = "Transport source/implementation identification, including embedded templates"
        reference = "https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/internal/c2/payload_templates/beacon.go.tmpl"
        limitation = "May match controller binaries that embed the payload template; not implant-only"
    strings:
        $magic = "CSB1" ascii
        $implant = "X-Implant-Token" ascii
        $session = "X-Session-Token" ascii
        $jitter = "jitter_percent" ascii
        $process = "process_name" ascii
    condition:
        filesize < 128MB and all of them
}

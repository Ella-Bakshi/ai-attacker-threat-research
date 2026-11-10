rule RND_ARTEX_Traffic_Recorder_Schema_Lineage {
 meta:
  description = "ARTEX traffic-recorder code/schema combination; software identity only"
  source = "https://github.com/BaaRai/ARTEX/tree/81eab87d166dddfc0d8be2707eadec788b61be0d"
  limitation = "Reference artifacts only; no campaign attribution or broad false-positive claim"
 strings:
  $module = "github.com/Autumn-27/artex" ascii
  $body = "CREATE TABLE IF NOT EXISTS exchange_bodies" ascii
  $blob = "CREATE TABLE IF NOT EXISTS blob_refs" ascii
  $fts = "CREATE VIRTUAL TABLE IF NOT EXISTS ex_fts" ascii
 condition:
  filesize <128MB and (uint16(0)==0x5a4d or uint32(0)==0x464c457f) and all of them
}

rule RND_CyberStrikeAI_C2_Database_Schema_Lineage {
 meta:
  description = "CyberStrikeAI controller embedded C2-schema code lineage; not implant-only"
  source = "https://github.com/AIPentest/CyberStrikeAI/tree/b43bdb991c3bee4f433cd1a0a370a90c4e24241e"
  limitation = "Only a local official-source build positive; not a distributed/campaign controller"
 strings:
  $module = "cyberstrike-ai/internal/database" ascii
  $auth = "CREATE TABLE c2_http_session_auth" ascii
  $artifact = "CREATE TABLE c2_payload_artifacts" ascii
  $profiles = "CREATE TABLE c2_profiles" ascii
  $db = "data/conversations.db" ascii
 condition:
  filesize <128MB and (uint16(0)==0x5a4d or uint32(0)==0x464c457f) and all of them
}

rule RND_CyberStrikeAI_Generated_HTTP_Beacon_Lineage {
 meta:
  description = "Native-confirmed CyberStrikeAI generated Linux HTTP beacon lineage; not campaign attribution"
  observed_sample_sha256 = "cbf1045bb2d4de52142b68d825d265588e1c94ec7d4132284deea8fef67fe4d4"
  limitations = "One acquired sample positive; source paths/symbols may change or be removed; no global false-positive claim"
 strings:
  $build = "cyberstrike-ai/tmp/c2/payloads/build-" ascii
  $fetch = "main.fetchC2FileByID" ascii
  $report = "main.buildTaskReport" ascii
  $implant = "X-Implant-Token" ascii
  $session = "X-Session-Token" ascii
  $cwd = "__CSAI_CWD_%x__" ascii
 condition:
  uint32(0)==0x464c457f and filesize<20MB and all of them
}

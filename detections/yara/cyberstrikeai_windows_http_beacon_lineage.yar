rule RND_CyberStrikeAI_Generated_Windows_HTTP_Beacon_Lineage {
 meta:
  description = "Exact-byte backed generated Windows HTTP beacon software lineage; not a malicious-use verdict"
  author = "Anmol Bakshi"
  date = "2026-11-15"
  observed_sample_sha256 = "1b95c2783b667ad5ffbd5b66afc367a92c314f507ba43789ec0bcda5a623a877"
  limitations = "One exact Windows reference positive; finite controls only, no production false-positive estimate; paths and symbols can change"
 strings:
  $build = "cyberstrike-ai/tmp/c2/payloads/build-" ascii
  $tcp = "main.tcpFetchEncryptedFile" ascii
  $fetch = "main.fetchC2FileByID" ascii
  $report = "main.buildTaskReport" ascii
  $persist = "main.persistWindows" ascii
  $implant = "X-Implant-Token" ascii
  $session = "X-Session-Token" ascii
 condition:
  uint16(0)==0x5a4d and uint32(uint32(0x3c))==0x00004550 and filesize<20MB and all of them
}

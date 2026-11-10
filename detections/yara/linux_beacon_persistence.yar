rule RND_CyberStrikeAI_Linux_Beacon_Persistence_Implementation {
 meta:
  description = "Native-backed generated Linux beacon persistence code-lineage fingerprint; not proof persistence ran or malicious use"
  author = "Local static IOC research"
  date = "2026-11-10"
  sample_sha256 = "cbf1045bb2d4de52142b68d825d265588e1c94ec7d4132284deea8fef67fe4d4"
 strings:
  $build = "cyberstrike-ai/tmp/c2/payloads/build-" ascii
  $func = "main.persistLinux" ascii
  $cron = "(crontab -l 2>/dev/null; echo '%s') | sort -u | crontab -" ascii
  $bash = "(nohup %s &>/dev/null &) # cs" ascii
  $result = "persistence installed via .bashrc" ascii
 condition:
  uint32(0) == 0x464c457f and filesize < 20MB and all of them
}

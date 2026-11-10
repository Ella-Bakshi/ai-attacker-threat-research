import "pe"

rule TOOL_RogueWinRM_Identity_Native_Strings {
 meta:
  description = "Software identity fingerprint for RogueWinRM; legitimate security tool also cited in a CyberStrikeAI intrusion report"
  classification = "tool_identity; does not prove malicious use, campaign membership, or compromised publisher"
  source = "https://github.com/antonioCoco/RogueWinRM/releases/tag/1.1"
  evidence = "Local PE bytes and Ghidra references at 0x140001440/0x140001470"
  known_reported_md5 = "74f57b3e897a4960dcdd5b7e8a54f9df"
  observed_release_1_1_sha256 = "bac5fc4fa68e57e2bee2fc5670ba914ef1707b16f52d2ee773956275e00a5ebb"
 strings:
  $identity = "\nRogueWinRM \n\n" ascii
  $usage = "-l <port>: listening port (default 5985 WinRM)" ascii
  $error = "Wrong Argument: %s\n" ascii
 condition:
  uint16(0) == 0x5a4d and pe.machine == pe.MACHINE_AMD64 and all of them
}

# Sheet Attack: India targeting evidence

Publisher: **Zscaler ThreatLabz**. Publication date: **2026-01-27**. Reviewed: **2026-11-10**.

The primary report links this campaign to Indian government or diplomatic targets and assesses AI-assisted malware development. This is a separate campaign; no ARTEX, CyberStrikeAI or CRAFTY FALCON relationship has been established. India is a campaign-level targeting association, not a claim that each value identifies an exclusively Indian victim or a current compromise.

This folder contains **72 source-reported IOC records**, **12 additional report artifacts**, and **1 supporting/context records**. Three hashes of one file count as three indicator values, not three malware samples. Host artifacts require correlation. Legitimate provider, DNS, CDN and certificate infrastructure is not a block list.

[CSV](indicators.csv) · [JSON with source locators and confidence scope](indicators.json) · [Sources](sources.json) · [Supplement overview](../README.md)

| Type | Indicator (defanged where applicable) | Source-reported role | Category | Confidence |
|---|---|---|---|---|
| domain | coadelhi[.]in | Payload-hosting domain | sourced-iocs | Medium |
| domain | gov-service-in-default-rtdb[.]firebaseio[.]com | FIREPOWER C2 domain | sourced-iocs | Medium |
| domain | govs-services-in-default-rtdb[.]firebaseio[.]com | FIREPOWER C2 domain | sourced-iocs | Medium |
| domain | hciaccounts[.]in | Payload-hosting domain | sourced-iocs | Medium |
| domain | hcidelhi[.]in | Payload-hosting domain | sourced-iocs | Medium |
| domain | hcidoc[.]in | Payload-hosting domain | sourced-iocs | Medium |
| domain | hcisupport[.]in | Payload-hosting domain | sourced-iocs | Medium |
| domain | webdevurl-cc389-default-rtdb[.]firebaseio[.]com | FIREPOWER C2 domain | sourced-iocs | Medium |
| ipv4 | 15[.]207[.]85[.]170 | Download IP address (hciaccounts[.]in) | sourced-iocs | Medium |
| md5 | 03141afe5c20d37620c085cdbeb4058b | The reversed Portable Executable (PE) file has been reconstructed to form the proper Dropper .NET binary.; source filename: details.png | sourced-iocs | High |
| md5 | 0729db72ab4ad9b2ac7a82918c744388 | SHEETCREEP; source filename: Proof.png | sourced-iocs | High |
| md5 | 0f7730a78490c61964b3bfc05eb59ea7 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| md5 | 119b836b4e1e7be8c3be8fe921f72bfb | FIREPOWER; source filename: N/A | sourced-iocs | High |
| md5 | 12669c29e00057abf20c73a434eb3dd2 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| md5 | 1ede39cb02b8aaa75063febc167db565 | Phishing PDF; source filename: Pay.pdf | sourced-iocs | High |
| md5 | 21dacb6cf6da872f1f3c7b6c876a8a92 | Dropper LNK launcher; source filename: AttachmentLetter.LNK | sourced-iocs | High |
| md5 | 41a3752e6ea83d25731f22e1c17f59e2 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| md5 | 5001c32b386cc8346079db7b2629d777 | SHEETCREEP and MAILCREEP Dropper launcher; source filename: d.exe | sourced-iocs | High |
| md5 | 556a567a2c5c27a6aa5660e2e6bcce7b | SHEETCREEP; source filename: detail.png | sourced-iocs | High |
| md5 | 62a23220b0249a15503f5ad762ed5889 | Loader; source filename: GServices.vbs | sourced-iocs | High |
| md5 | 6bed5e271eddf5cb86a5964b8c2f51b6 | Archive containing the SHEETCREEP payload.; source filename: Document.zip | sourced-iocs | High |
| md5 | 7269779e3fe07b1d96564117461ec75b | SHEETCREEP Dropper launcher; source filename: chrome.exe | sourced-iocs | High |
| md5 | 87c7d69c6131406afdd0a08e89329d0a | SHEETCREEP; source filename: details.png | sourced-iocs | High |
| md5 | a0b6869accba2c9ad3e1f79268a810d4 | PowerShell document stealer; source filename: N/A | sourced-iocs | High |
| md5 | cd5aab2b0f8d2b42e7a6537303d6345d | FIREPOWER; source filename: N/A | sourced-iocs | High |
| md5 | e48f1000c86b93cf428a13a0b7384e0d | FIREPOWER; source filename: N/A | sourced-iocs | High |
| md5 | ed4dd29c57a38f2bb1934acbaeadeeba | MAILCREEP; source filename: ds.png | sourced-iocs | High |
| md5 | f9a2da8f12179414663a230f11edca20 | SHEETCREEP; source filename: edge.exe | sourced-iocs | High |
| sha1 | 147055a1341737625cf0e878b7ebd5acf09d1883 | SHEETCREEP Dropper launcher; source filename: chrome.exe | sourced-iocs | High |
| sha1 | 16410fe2c44272005ca3c2ce994d24e9c2e731f6 | Archive containing the SHEETCREEP payload.; source filename: Document.zip | sourced-iocs | High |
| sha1 | 2f46595d58bef1c70ca757e18bb04443b2d5ce72 | Dropper LNK launcher; source filename: AttachmentLetter.LNK | sourced-iocs | High |
| sha1 | 6140ed17fa47e0fa166449eaf2b2770fec0fedbd | PowerShell document stealer; source filename: N/A | sourced-iocs | High |
| sha1 | 7bc5d288ec260765a146136194d815ff3c697df8 | MAILCREEP; source filename: ds.png | sourced-iocs | High |
| sha1 | 8735e1af5134d1cd173b55b089e31becb0261677 | SHEETCREEP and MAILCREEP Dropper launcher; source filename: d.exe | sourced-iocs | High |
| sha1 | 8f9843607ff0ed83ca58e21612b41d6e744beb81 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha1 | 97712c11b83c31ba03b747cf39a49cd0e208c5f5 | Phishing PDF; source filename: Pay.pdf | sourced-iocs | High |
| sha1 | a38eab1ac01201b651b2efdebc78e994402976f1 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha1 | a55c18a82203cf1efafac6f3c47642ab60c74ffc | SHEETCREEP; source filename: details.png | sourced-iocs | High |
| sha1 | aa9b4410004d43e4e5cc1fc2cda1956bc5663b03 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha1 | ac06003a774af5a8e4be349fc6f0e65cea116370 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha1 | b8fd6b4eece68095caeb26bdd1090ab7959f24aa | The reversed Portable Executable (PE) file has been reconstructed to form the proper Dropper .NET binary.; source filename: details.png | sourced-iocs | High |
| sha1 | cdecfe8e1cacd1af204a5da52f6c02eb16fdea8b | SHEETCREEP; source filename: edge.exe | sourced-iocs | High |
| sha1 | daeeb031a9617e6f1b7bf4d85de9c75f62021c82 | SHEETCREEP; source filename: Proof.png | sourced-iocs | High |
| sha1 | e333ae0948ede0cf1368deec53a1eda18210e75e | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha1 | e9d9d8c0c818ba9208e61eaf49af4c1b37f4eb59 | SHEETCREEP; source filename: detail.png | sourced-iocs | High |
| sha1 | e9eeda092500d7c7f278672d35f733e0e26f0e2c | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha1 | f68cd104bfa2ac9992a98936c6e97c41e680b698 | Loader; source filename: GServices.vbs | sourced-iocs | High |
| sha256 | 20d72c8580b4d5ef4f771c91ce1d1207e5416fa789d8216a73a0abb8e030644f | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha256 | 309a39ba10cd7c7075837b63d247fa45764f5496fdae215e95a3f4b65ab6dfc3 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha256 | 363fca9534e5cb69e40330473bcbd0acc439cf81a555234eed250f65c98478e3 | Phishing PDF; source filename: Pay.pdf | sourced-iocs | High |
| sha256 | 43fb05d9fc179f791b1a2814f7116ee577b6e48f62eee63af039350260d7fe2b | The reversed Portable Executable (PE) file has been reconstructed to form the proper Dropper .NET binary.; source filename: details.png | sourced-iocs | High |
| sha256 | 59abb997927e471472a1c487dea0180d11e9c99774bb138ace46771acba9c3d8 | Archive containing the SHEETCREEP payload.; source filename: Document.zip | sourced-iocs | High |
| sha256 | 61b2b6b61474398a966e26d3b909542450fcab9b6670558cecd6fabc1015bbce | SHEETCREEP and MAILCREEP Dropper launcher; source filename: d.exe | sourced-iocs | High |
| sha256 | 644dda0ea5db1eb5f07ccfccddb909c6ee57235c4465adbfc342da6867cdb71a | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha256 | 71794df37a107472e8d0829387741953f9e6c7778519b11f061c79ff6fb0f386 | SHEETCREEP; source filename: Proof.png | sourced-iocs | High |
| sha256 | 86d8b3fe209b3f1d9a20865ff1ee5d6015941c2a5394861118c8d6ec3695f1a6 | PowerShell document stealer; source filename: N/A | sourced-iocs | High |
| sha256 | 889b4b1e13b66aff349282eae3999783f5542f961b433a7d4653c5281e7f4d3e | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha256 | 989ad43bb9e328d786664247c3af4c17be28932760113708a9c6de977d69652c | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha256 | 9ab6d01a6df367ee505e59850438e6926dfb61c2ebfbe4e03eba48f70ee36ac3 | Loader; source filename: GServices.vbs | sourced-iocs | High |
| sha256 | 9eebbf8899a1cf4156a872e9b8cde2a8f6ab364b8089550510938405c622cc58 | SHEETCREEP; source filename: edge.exe | sourced-iocs | High |
| sha256 | a97cc81a2f7c05bfc498b71999176c2aeb6e3ad273e48eb1f5c1c5647419c642 | MAILCREEP; source filename: ds.png | sourced-iocs | High |
| sha256 | b56062033df06738b66c38b3fa2f82a7e8c558336a4790c83c7faad595172167 | SHEETCREEP; source filename: details.png | sourced-iocs | High |
| sha256 | bb11bea463ab1b976c3716591f93eccc71c1a2d1c389a371416b140cd8faa6f0 | SHEETCREEP; source filename: detail.png | sourced-iocs | High |
| sha256 | bec00fa5a87195f182511ecc5292a716c79bc74e17bd1138c8fb2f2285df1b46 | Dropper LNK launcher; source filename: AttachmentLetter.LNK | sourced-iocs | High |
| sha256 | de14ca6d93dadbc1ec216700d76ad2d0e7b9ebceb95de68c631d0a1c01c915c4 | FIREPOWER; source filename: N/A | sourced-iocs | High |
| sha256 | eea5cb7795d86e4612edcc6f0085d151e1b7a7351646caf26955c2ac35158971 | SHEETCREEP Dropper launcher; source filename: chrome.exe | sourced-iocs | High |
| url | https://docs[.]google[.]com/spreadsheets/d/1cB8jzFpQcixridoEz_eDvLnjCTx79gKFQSoFiuOErdM/edit | C2 URL | sourced-iocs | Medium |
| url | https://docs[.]google[.]com/spreadsheets/d/1cdSJvZ7tx6CPBuEa66uTVWmSD4zABnZOLjM87pRXkTE/edit | C2 URL | sourced-iocs | Medium |
| url | https://docs[.]google[.]com/spreadsheets/d/1wgx4gj3-YGGAwmtr1DRu4n1QkznK2pYoKO6C4GTmquY/edit | C2 URL | sourced-iocs | Medium |
| url | https://hciaccounts[.]in/Documents[.]zip | Download URL and SHEETCREEP payload | sourced-iocs | Medium |
| url | https://storage[.]googleapis[.]com/testfirebase-b24a8[.]appspot[.]com/config1[.]txt | SHEETCREEP backup configuration URL | sourced-iocs | Medium |
| url | https://testfirebase-b24a8-default-rtdb[.]firebaseio[.]com/(12336)005056C0000186/details[.]json | SHEETCREEP backup configuration URL | sourced-iocs | Medium |
| ipv4 | 8[.]8[.]8[.]8 | Legitimate Google DNS connectivity check, not malicious C2 | legitimate-service-context | Low |
| filename | AttachmentLetter.LNK | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | Document.zip | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | GServices.vbs | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | Pay.pdf | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | Proof.png | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | chrome.exe | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | d.exe | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | detail.png | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | details.png | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | ds.png | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | edge.exe | Reported artifact filename; correlate with associated file hashes | report-host-network-artifacts | Low |
| filename | text.log | Source-described host/C2-workspace artifact; not framework-exclusive | report-host-network-artifacts | Low |

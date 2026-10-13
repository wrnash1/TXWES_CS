# Quiz: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is open-note but must reflect your own work. Questions are written to match the difficulty and style of the CompTIA Security+ SY0-701 exam.

---

## Question 1

A forensic examiner arrives at a scene and discovers a laptop running Windows that has been involved in a suspected data theft incident. The examiner's first priority is to capture volatile evidence before shutting down the system. Which action should the examiner perform FIRST?

A) Create a forensic disk image of the hard drive

B) Capture the contents of RAM using a memory acquisition tool

C) Collect Windows event logs from the Application and Security channels

D) Connect a write blocker and verify the drive hash

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Disk imaging is important but captures non-volatile data that persists through power-off. RAM contents — running processes, network connections, encryption keys — are immediately lost when the system shuts down. Volatile data must be captured first.
- Why C is incorrect: Event logs are stored on disk (non-volatile) and will survive shutdown. Collecting logs before RAM means losing all volatile data.
- Why D is incorrect: Write blockers and hash verification are used before imaging a storage device. They are not relevant to live memory acquisition and do not need to happen before RAM capture.

---

## Question 2

A forensic investigator runs `dd if=/dev/sdb of=/mnt/forensic/evidence.img bs=4096 conv=noerror,sync` and then computes MD5 hashes of both the source drive and the image. The hashes match. What has been established?

A) The evidence.img file contains no malware

B) The image is an exact bit-for-bit copy of the original drive and has not been modified

C) The original drive is write-protected and cannot be altered

D) The imaging process was faster than FTK Imager would have been

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Hash matching establishes that the copy is identical to the source. It says nothing about the content of the files. Malware present on the original drive will be present in the image — the hash proves copying accuracy, not file safety.
- Why C is incorrect: Hash matching does not indicate write protection. A write blocker is a separate device that prevents writes. Hash matching simply proves the image matches the source at the time of imaging.
- Why D is incorrect: Tool speed comparison is not established by hash verification. Hash comparison is a data integrity proof, not a performance metric.

---

## Question 3

An investigator uses the Volatility `pslist` plugin to list running processes but does not see a process named `mal.exe` that a threat intelligence report says should be present on a compromised system. The investigator then runs `psscan` and finds `mal.exe`. What does this indicate?

A) The memory image is corrupted and pslist cannot fully parse it

B) The malware has unlinked itself from the OS process list, a technique known as DKOM (Direct Kernel Object Manipulation)

C) psscan is less reliable than pslist and the mal.exe entry is a false positive

D) The malware was not active at the time the memory image was captured

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: If the memory image were corrupted, psscan would also fail to find valid EPROCESS structures. The fact that psscan finds the process while pslist does not is evidence of deliberate manipulation, not image corruption.
- Why C is incorrect: psscan is the more exhaustive search method — it scans raw memory for EPROCESS structures directly rather than walking the linked list. Its findings are considered more reliable for detecting hidden processes, not less.
- Why D is incorrect: If the process was not active, neither pslist nor psscan would find it. Both pslist and psscan analyze the same memory image — if psscan finds a live EPROCESS structure, the process was present in memory when the image was captured.

---

## Question 4

A forensic examiner needs to image a hard drive seized from a suspect in a criminal investigation. She attaches the drive to her forensic workstation. Before connecting the drive, she inserts a device between the drive's data connector and the workstation's port. This device allows the examiner to read all data from the drive but prevents any write operations from reaching it. What is this device?

A) A forensic hub

B) A RAID controller

C) A write blocker

D) A hash accelerator

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A forensic hub is not a standard forensic term. Forensic hubs do not perform the specific function described — blocking writes while permitting reads.
- Why B is incorrect: A RAID controller manages multiple disk arrays for redundancy or performance. It does not have a mode that prevents writes to a single attached evidence drive.
- Why D is incorrect: Hash accelerators are hardware devices that speed up cryptographic hash computation. They do not intercept storage device communications to block writes.

---

## Question 5

A Windows security log shows the following sequence for user `admin` from source IP `185.220.101.45`: Event 4625 (failed logon) × 847 attempts over three minutes, followed by Event 4624 (successful logon). The IP address geolocates to an anonymous Tor exit node. What does this evidence suggest?

A) A legitimate administrator forgot their password and eventually guessed it correctly

B) A brute-force or credential stuffing attack succeeded in authenticating to the admin account

C) The system is generating false positives due to a misconfigured authentication policy

D) The account was compromised through a phishing attack that obtained the password

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: 847 failed attempts over three minutes from a Tor exit node is not consistent with a legitimate user who forgot their password. The source IP is also a forensically significant indicator — Tor exit nodes are specifically used to anonymize attacker traffic, not legitimate administrator access.
- Why C is incorrect: 847 consecutive 4625 events followed by 4624 is a clearly interpretable pattern consistent with automated attack activity. Misconfigured authentication policies could generate false failures, but not in this pattern from an external anonymous IP.
- Why D is incorrect: Phishing attacks obtain credentials through social engineering — the victim provides credentials to a fake site. The event sequence here (many failures followed by success) is the signature of automated password guessing, not credential theft via phishing.

---

## Question 6

A forensic examiner reviews the MAC times for a suspicious file on a compromised server. The file was reportedly created on the server in March. The Modified time shows January, the Accessed time shows March, and the Created time shows March. The system was deployed in February. A January Modified time for a file created in March is impossible. What does this indicate?

A) The file system is corrupted and timestamps are unreliable

B) The attacker practiced timestomping to make the malicious file appear to predate the server's deployment

C) The file was created by restoring from a backup made before server deployment

D) MAC times on Windows systems automatically revert to the compile date of the executable

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Isolated impossible timestamps on a single file, while all other files have consistent timestamps, suggest targeted manipulation rather than general corruption. Widespread corruption would affect many files.
- Why C is incorrect: If the file were restored from a backup, the backup would have to predate the server deployment to produce a January timestamp — but the server was not deployed until February. This is internally inconsistent.
- Why D is incorrect: Windows does not automatically set file timestamps to compile dates. The PE compile timestamp is an embedded field within the file itself, not the file system MAC timestamp. File system timestamps are set by the OS when files are created, modified, or accessed.

---

## Question 7

During a corporate investigation of a suspected insider data theft, the investigator needs to access the personal laptop the employee uses for work. The employee has signed the company's acceptable use policy (AUP), which states that "company resources and systems are subject to monitoring and investigation." The laptop was purchased by the employee with personal funds. What does this situation represent?

A) The investigator has full authority to seize and image the laptop because the AUP covers all devices used for work

B) The company-owned AUP does not apply to personal devices; a search warrant is required to access the personal laptop

C) The AUP may provide limited authorization, but access to a personal device involves additional privacy considerations that legal counsel should evaluate

D) The employee forfeited all privacy rights on the personal laptop by using it for work

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: AUP consent provisions are generally interpreted to apply to company-owned devices. Extending that consent to employee-owned personal devices is legally questionable and depends on jurisdiction, the specific AUP language, and the applicable state/federal privacy laws.
- Why B is incorrect: While a search warrant may ultimately be required, stating categorically that the AUP provides zero authority and a warrant is always required is an oversimplification. The AUP language, the nature of the investigation, and applicable law all factor in — which is why legal counsel must be involved.
- Why D is incorrect: Employees do not forfeit all privacy rights on personal property by using it for work. This is the central tension in BYOD investigations and the reason legal counsel involvement is essential before proceeding.

---

## Question 8

A forensic investigator is analyzing a USB drive from a suspect and needs to recover image files that were deleted before the drive was seized. The drive was formatted after the images were deleted. Which technique is MOST likely to recover the JPEG images?

A) Timeline analysis using Plaso

B) File carving from unallocated space using JPEG magic bytes

C) Event log analysis for file deletion events

D) Memory forensics using Volatility to find file handles

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Timeline analysis (Plaso/log2timeline) reconstructs activity timelines from file system metadata and logs. It cannot recover deleted files from unallocated space — it analyzes existing file system structures and log entries.
- Why C is incorrect: Windows event logs record process creation, authentication, and service events. File deletion events are not captured in standard Windows event logs (though Object Access auditing can track deletions if explicitly configured). USB drives used as removable media typically have no event logs of their own.
- Why D is incorrect: Memory forensics examines RAM. A seized USB drive contains no RAM. File handles in memory would only be relevant if the USB drive is currently mounted on a running system — not for post-seizure offline analysis.

---

## Question 9

A digital forensic examiner testifies in court that she created a forensic image of the suspect's hard drive. Defense counsel asks how the examiner can prove the image has not been modified since collection. What is the examiner's best response?

A) She will testify that she personally maintained custody of the image at all times

B) She will present the MD5 and SHA-256 hashes computed at the time of imaging and demonstrate that current hashes of the image are identical, proving no modification occurred

C) She will note that FTK Imager creates read-only images that cannot be modified

D) She will show that the drive was placed in a sealed evidence bag immediately after imaging

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Personal custody testimony is valuable for chain of custody but cannot mathematically prove the data is unchanged. A person could theoretically be mistaken, mislead, or compromised. Cryptographic hash verification is the objective, verifiable proof.
- Why C is incorrect: FTK Imager creates image files that are stored as regular files and can be modified with any hex editor. The image format itself does not prevent modification after creation. The E01 format includes embedded hashes that detect modification, but the image file itself is not inherently immutable.
- Why D is incorrect: An evidence bag with a seal prevents physical access but does not address digital modification of a file stored separately on forensic media. Digital integrity is proven cryptographically, not physically.

---

## Question 10

A corporate HR investigation requires access to an employee's company-issued laptop and work email account to investigate allegations of financial fraud. Who should be involved before the investigation begins?

A) The IT helpdesk team only, since they have the technical skills needed

B) The employee's manager, so they can advise on the investigation scope

C) Legal counsel and HR, to ensure the investigation complies with employment law, privacy regulations, and evidence handling requirements

D) An external forensic vendor, because internal staff have a conflict of interest

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: IT helpdesk staff have technical access to devices but are not qualified to assess the legal and employment law implications of a corporate investigation. Acting without legal guidance can create liability and render evidence inadmissible.
- Why B is incorrect: The employee's manager should generally not be involved in an investigation of that employee — the manager may be a witness, a co-conspirator, or may inadvertently warn the employee, allowing destruction of evidence.
- Why D is incorrect: External forensic vendors are sometimes appropriate, but the core issue in this question is legal and HR oversight, not vendor selection. Internal security teams can conduct valid forensic investigations; what matters is involving legal and HR before proceeding.

---

---

## Question 11

A forensic investigator discovers a steganography tool in the suspect's Downloads folder. The investigator suspects that sensitive documents were hidden inside image files before being sent to an external email address. Which technique does steganography use to conceal data?

- A) Encrypting data with a symmetric key and storing the ciphertext as a file
- B) Embedding data within the least significant bits of image pixel values so the visual change is imperceptible
- C) Compressing data using a lossless algorithm and renaming the output file with a .jpg extension
- D) Encoding data in Base64 and appending it to the end of an image file after the EOF marker

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Encryption protects data confidentiality but does not hide the existence of the data. Encrypted files are visible as files. Steganography's goal is to conceal the fact that a message exists at all, not merely to protect its contents.
- Why C is incorrect: Renaming a compressed archive with a .jpg extension is file extension manipulation, not steganography. The file would not visually display as an image and could be identified immediately by examining magic bytes.
- Why D is incorrect: Appending data after the EOF marker is a simple hiding technique but is trivially detectable by examining file size and the bytes after the expected end-of-file marker. True steganography modifies the carrier file's existing structure.

---

## Question 12

An investigator is examining a Windows system and needs to recover deleted browser history files. The files were deleted three weeks ago. The NTFS volume has been in continuous use since the deletion. Which factor MOST significantly reduces the likelihood of recovering the deleted files?

- A) The NTFS Master File Table (MFT) records are removed when files are deleted
- B) The deleted file's data blocks may have been overwritten by subsequent file writes during three weeks of use
- C) NTFS encrypts deleted file data to prevent unauthorized recovery
- D) Windows Defender automatically wipes deleted files to prevent privacy violations

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: NTFS MFT records are not immediately removed when a file is deleted — the MFT entry is marked as available for reuse. The entry itself may persist for some time, and tools like MFTECmd can parse deleted MFT records to identify file metadata even after deletion.
- Why C is incorrect: NTFS does not encrypt deleted file data. Standard NTFS deletion simply marks blocks as unallocated. BitLocker encrypts the entire volume, but this applies equally to active and deleted data.
- Why D is incorrect: Windows Defender does not wipe deleted files. Windows Defender is an antimalware tool. Secure file deletion requires explicit use of tools like sdelete or the Cipher /W command.

---

## Question 13

A mobile forensics examiner is attempting to acquire data from a locked iOS device seized in a criminal investigation. The device is running the current iOS version and has USB Restricted Mode enabled. What does USB Restricted Mode prevent?

- A) Charging the device via USB
- B) USB data connections to forensic acquisition tools if the device has not been unlocked for more than one hour
- C) Cellular network connections while the device is connected to a computer
- D) All data transmission including Bluetooth when the screen is locked

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: USB Restricted Mode affects data connections only, not power delivery. Charging still functions normally through a locked USB Restricted Mode device.
- Why C is incorrect: USB Restricted Mode has no effect on cellular network connectivity. The device continues to make and receive calls and data connections over the cellular network regardless of USB connection state.
- Why D is incorrect: USB Restricted Mode specifically restricts USB data connections. Bluetooth connectivity is governed by separate settings and is not affected by USB Restricted Mode.

---

## Question 14

A cloud forensics investigator needs to collect logs from a SaaS email platform for a data exfiltration investigation. The organization does not own or control the underlying cloud infrastructure. What is the PRIMARY challenge unique to cloud forensics compared to traditional on-premises investigations?

- A) Cloud log files use proprietary binary formats that require vendor-specific tools to parse
- B) Logs stored in the cloud are automatically deleted after 24 hours by law
- C) The investigator cannot independently verify that logs are complete and unmodified without cooperation from the cloud provider
- D) Cloud services do not generate authentication or access logs

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Major cloud providers (Microsoft 365, Google Workspace, AWS) export logs in standard formats such as JSON, CSV, and Common Log Format. Proprietary binary formats are not the primary challenge.
- Why B is incorrect: There is no universal law requiring log deletion after 24 hours. Cloud providers retain logs according to their configurable retention policies, which may range from days to years depending on tier and configuration.
- Why D is incorrect: Cloud services generate extensive authentication and access logs. Azure AD, Google Workspace Admin, and AWS CloudTrail all produce detailed audit logs. Access to these logs, not their absence, is the forensic challenge.

---

## Question 15

A forensic examiner is investigating a SQLite database file recovered from a suspect's mobile device. The examiner needs to recover records that were deleted from a table. Which characteristic of SQLite's storage format makes this possible?

- A) SQLite keeps a complete transaction log of all DELETE statements in a separate .log file
- B) SQLite's page-based storage allocates pages for reuse without immediately overwriting deleted row data, leaving remnant data in database pages
- C) SQLite requires a recycle bin confirmation before permanently removing any record
- D) SQLite automatically creates encrypted backups of all tables before any DELETE operation

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: SQLite does maintain a write-ahead log (WAL) for transaction durability, but this log is not a forensic archive — it is overwritten as the database cycles through pages. Deleted record remnants in the database page structure are the primary recovery mechanism.
- Why C is incorrect: SQLite is a database engine used by applications, not an operating system with a recycle bin. DELETE operations execute immediately without user confirmation within the database engine.
- Why D is incorrect: SQLite does not create encrypted backups before DELETE operations. SQLite's storage model is based on B-tree pages — when rows are deleted, the page space is marked as free for reuse but the data may persist until overwritten by a subsequent write.

---

## Question 16

During a Windows forensic investigation, the examiner exports the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry key and finds an unfamiliar entry pointing to `C:\Users\Public\svchost32.exe`. What does this registry key represent and why is this finding significant?

- A) A critical Windows kernel driver that should not be removed
- B) A user preference setting for display scaling on high-DPI monitors
- C) An autorun entry that executes the specified program at every system startup — the unusual path suggests a persistence mechanism planted by an attacker
- D) A Windows Update service binary scheduled to run once after a recent patch installation

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: The Run key is not for kernel drivers. Drivers are loaded through the HKLM\SYSTEM\CurrentControlSet\Services registry path. The Run key is specifically for user-mode programs that launch at logon.
- Why B is incorrect: Display scaling preferences are stored in HKCU\Control Panel\Desktop and related paths, not in the Run key. The Run key has no role in display configuration.
- Why D is incorrect: Windows Update uses its own service mechanisms and does not typically place binaries in C:\Users\Public\. The path C:\Users\Public\ is a user-accessible shared folder, not a standard Windows system directory — placing executables there is a common attacker technique to avoid detection heuristics that focus on system directories.

---

## Question 17

A network forensics examiner is reviewing a PCAP file captured during a suspected data exfiltration incident. The examiner observes large volumes of outbound DNS TXT record queries averaging 200 bytes each, sent at regular 30-second intervals to a single external domain. Normal DNS queries on this network are under 50 bytes. What technique does this pattern most likely represent?

- A) DNS amplification attack where the attacker is using the internal resolver to flood external targets
- B) DNS tunneling where data is encoded within DNS query fields to exfiltrate data through a permitted protocol
- C) DNS poisoning where the attacker is injecting false records into the local DNS cache
- D) A misconfigured DNS server performing zone transfers at 30-second intervals

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A DNS amplification attack sends queries to external DNS resolvers to generate large responses directed at a victim. The queries originate from spoofed source IPs and target open resolvers — the pattern would not show regular 30-second intervals from a single internal host to one external domain.
- Why C is incorrect: DNS cache poisoning involves injecting forged DNS responses into a resolver's cache. It does not produce outbound query traffic from a client at regular intervals. Cache poisoning targets the response path, not the query path.
- Why D is incorrect: DNS zone transfers (AXFR) are initiated by secondary DNS servers and transfer all zone records, not individual TXT queries. Zone transfers occur infrequently (on change notification or at scheduled intervals), and legitimate zone transfers are large bulk transfers, not regular small queries.

---

## Question 18

An examiner is reviewing Windows Prefetch files (`C:\Windows\Prefetch\`) during an investigation. The suspect claims they never ran a particular executable. The examiner finds a .pf file for the executable with a last execution timestamp from the date in question. What does the presence of this Prefetch file prove?

- A) The executable is currently running on the system
- B) The executable was executed on the system on the date recorded in the Prefetch file
- C) The executable was downloaded from the internet and stored in the Downloads folder
- D) The executable was flagged as malicious by Windows Defender

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Prefetch files are created and updated when an executable runs — they are historical records, not indicators of current execution state. A Prefetch file persists long after the program exits.
- Why C is incorrect: Prefetch files track execution, not download origin. There is no download location metadata in a Prefetch file. Browser history, zone identifier alternate data streams (ADS), and download manager logs are the sources for download origin information.
- Why D is incorrect: Windows Defender detections are logged in separate event logs and the Defender scan history, not in Prefetch files. Prefetch files are created by the Superfetch/SysMain service to optimize future application load times.

---

## Question 19

A forensic investigator is analyzing network traffic and discovers that a compromised workstation is connecting outbound to an HTTPS URL on port 443 at randomized 5–15 minute intervals. The connections are short (under 2 seconds), transfer minimal data, and the domain was registered 48 hours before the observed traffic. What attacker technique does this pattern describe?

- A) SQL injection probing the organization's external web application
- B) Command and control (C2) beaconing using HTTPS to blend with legitimate web traffic
- C) A misconfigured auto-update service checking for software patches
- D) DNS-over-HTTPS (DoH) resolver traffic from a privacy-focused browser

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: SQL injection attacks target a web application server, not outbound connections from a workstation to an external HTTPS endpoint. SQL injection appears as inbound traffic to the organization's web server, not outbound periodic connections.
- Why C is incorrect: Legitimate auto-update services connect to known vendor domains (windowsupdate.com, update.microsoft.com, etc.) that have established long-term registrations. A 48-hour-old domain is a strong indicator of a newly created attacker-controlled infrastructure — legitimate software vendors do not use recently registered domains for update services.
- Why D is incorrect: DoH traffic from browsers targets known DoH providers (1.1.1.1, 8.8.8.8, dns.google) with consistent connection patterns. The combination of randomized intervals, minimal data transfer, and a 48-hour-old domain is not consistent with DoH resolver behavior.

---

## Question 20

A forensics examiner reviews a suspect's hard drive and finds that a directory contains dozens of .jpg files. When the examiner opens several of these files, they display normal-looking photographs. However, threat intelligence indicates that this suspect used steganography to hide encrypted data inside image files. Which approach would allow the examiner to determine whether hidden data is present in these images?

- A) Rename the files with a .zip extension and attempt to open them as archives
- B) Compute the SHA-256 hash of each file and compare it against known-good JPEG hashes
- C) Use a steganography detection tool (steganalysis) to analyze statistical anomalies in pixel data that indicate data has been embedded
- D) Review the EXIF metadata of each image using a metadata viewer to find embedded documents

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Renaming a JPEG with a .zip extension will not reveal steganographic content — the embedded data is distributed across pixel values, not stored as a concatenated archive after the JPEG data. A steganographic JPEG would not open as a valid ZIP file.
- Why B is incorrect: Comparing SHA-256 hashes against known-good values would detect file modification but is impractical for detecting steganography. There is no database of known-good hashes for every possible legitimate JPEG. Two images that appear visually identical but contain different steganographic payloads would produce different hashes — but this comparison does not reveal which image has hidden data.
- Why D is incorrect: EXIF metadata is stored in a standard header structure and contains camera, date, location, and settings data. Steganographic tools embed data in pixel values (LSB encoding), not in EXIF fields. Reviewing EXIF metadata will not detect LSB steganography.

---

*End of Quiz — Module 12*

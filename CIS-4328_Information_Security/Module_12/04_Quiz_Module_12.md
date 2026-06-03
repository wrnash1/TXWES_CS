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

*End of Quiz — Module 12*

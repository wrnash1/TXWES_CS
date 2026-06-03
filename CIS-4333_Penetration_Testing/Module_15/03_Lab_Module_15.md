# Lab Activity: Module 15 — Post-Report Cleanup and Debriefing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication

---

## Objective

In this lab you will simulate the complete post-engagement phase of a penetration test.
Starting from a provided engagement log that documents artifacts planted during a prior
testing session, you will: remove all artifacts systematically from a Metasploitable 2 target,
verify removal, draft a cleanup attestation, compute evidence file hashes for chain-of-custody
documentation, and write a partial retest report section. By completing this lab you will have
practiced every post-engagement skill tested on PT0-002 Domain 5.

---

## Prerequisites

- Complete the Module 15 video lecture and reading guide before beginning
- Kali Linux VM (attacker) and Metasploitable 2 VM (target) must be running and on the same
  host-only network
- Metasploitable 2 default credentials: `msfadmin` / `msfadmin`
- You should have completed the Module 12 or Module 13 lab that established the artifacts
  this lab requires you to clean up. If you did not, use the provided seed script in Canvas
  (Lab_15_Seed.sh) to plant the required artifacts before beginning.

---

## Scenario Background

You are the lead tester wrapping up an engagement against a fictional target. During the
prior testing session the following artifacts were created on the Metasploitable 2 target
(IP: `192.168.56.101`):

1. A file `/tmp/pentest_tool.sh` (a bash script placed during testing)
2. A cron job entry in `/etc/cron.d/pentest_cron` that runs `/tmp/pentest_tool.sh` every
   five minutes
3. A local user account named `testuser99` created with `useradd`
4. A web shell at `/var/www/dvwa/hackable/uploads/cmd.php`
5. A modified entry in `/etc/hosts` that added `192.168.56.1 malicious-c2.lab`

Your job is to remove all five artifacts, verify removal, compute SHA-256 hashes of two
evidence files, and produce the cleanup documentation.

---

## Step-by-Step Instructions

### Part 1 — Establish SSH Access to Target (5 minutes)

From your Kali VM, connect to the Metasploitable 2 target:

```bash
ssh msfadmin@192.168.56.101
```

Accept the host key fingerprint if prompted. Verify you are logged in by running:

```bash
whoami && hostname
```

Expected output: `msfadmin` and the hostname of the Metasploitable 2 machine. Take a
screenshot of this output for your submission.

### Part 2 — Document Existing Artifacts (10 minutes)

Before removing anything, confirm each artifact is present. Run the following verification
commands and capture the output:

```bash
ls -la /tmp/pentest_tool.sh
cat /etc/cron.d/pentest_cron
id testuser99
ls -la /var/www/dvwa/hackable/uploads/cmd.php
grep malicious-c2 /etc/hosts
```

For each command, record whether the artifact was found (Present) or not found (Absent) in
the engagement log table provided in Part 5.

### Part 3 — Artifact Removal (20 minutes)

Remove each artifact in sequence. After each removal, run the verification command again to
confirm the artifact is gone. Capture before-and-after terminal output for your submission.

**Step 3a — Remove the pentest tool script:**

```bash
sudo rm /tmp/pentest_tool.sh
ls /tmp/pentest_tool.sh 2>&1
```

Expected output of the second command: `ls: cannot access '/tmp/pentest_tool.sh': No such
file or directory`

**Step 3b — Remove the cron job:**

```bash
sudo rm /etc/cron.d/pentest_cron
ls /etc/cron.d/pentest_cron 2>&1
```

**Step 3c — Delete the test user account:**

First verify the account exists, then delete it:

```bash
id testuser99
sudo userdel -r testuser99
id testuser99 2>&1
```

Expected output after deletion: `id: 'testuser99': no such user`

**Step 3d — Remove the web shell:**

```bash
sudo rm /var/www/dvwa/hackable/uploads/cmd.php
ls /var/www/dvwa/hackable/uploads/cmd.php 2>&1
```

**Step 3e — Restore the /etc/hosts file:**

View the current state of `/etc/hosts`, identify the line you need to remove, and edit it:

```bash
cat /etc/hosts
sudo sed -i '/malicious-c2/d' /etc/hosts
grep malicious-c2 /etc/hosts
echo "Hosts file entry removed - no output above confirms success"
```

### Part 4 — Evidence Chain of Custody (15 minutes)

Your engagement evidence folder on Kali contains two screenshot files. Navigate to your
evidence directory (or use the provided sample files in `~/lab15_evidence/`):

```bash
ls -la ~/lab15_evidence/
```

Compute SHA-256 hashes for both files:

```bash
sha256sum ~/lab15_evidence/evidence_screenshot_01.png
sha256sum ~/lab15_evidence/evidence_screenshot_02.png
```

Record both hash values. These hashes are your chain-of-custody record — if the files are
ever modified, the hashes will no longer match.

Next, create an encrypted archive of the evidence folder:

```bash
zip -e --password pentest2026 ~/lab15_evidence_archive.zip ~/lab15_evidence/
ls -lh ~/lab15_evidence_archive.zip
```

Note: In a production environment you would use GPG encryption rather than zip password
protection. The zip method is used here for lab simplicity.

Record the archive filename, creation timestamp, and both SHA-256 hashes in your
cleanup attestation document (Part 5).

### Part 5 — Produce the Cleanup Attestation (20 minutes)

Using a text editor or your word processor, create a cleanup attestation document containing
the following sections:

**Section 1 — Engagement Reference**

```
Engagement: Metasploitable 2 Lab Assessment
Lead Tester: [Your Name]
Testing Dates: [Your lab session dates]
Cleanup Date: [Today's date]
```

**Section 2 — Artifact Inventory and Cleanup Log**

Create a table with five rows (one per artifact) and these columns:

| Artifact ID | Description | Location | Status Before Cleanup | Cleanup Action | Status After Cleanup | Verified By |
|-------------|-------------|----------|-----------------------|----------------|----------------------|-------------|

Fill in all fields based on your work in Parts 2 and 3. The "Status Before Cleanup" column
should say Present or Absent based on your Part 2 findings. The "Status After Cleanup"
column should say Removed or Not Found.

**Section 3 — Evidence Chain of Custody**

| Evidence File | SHA-256 Hash | Collection Date | Storage Location | Handling Notes |
|---------------|--------------|-----------------|------------------|----------------|

Fill in the hashes from Part 4.

**Section 4 — Attestation Statement**

Write a three-to-four sentence attestation paragraph stating that all artifacts listed in
Section 2 have been removed from the target environment, that evidence files have been
hashed and stored in encrypted archives, and that the environment has been returned to its
pre-test state to the best of your knowledge. Sign with your name and date.

### Part 6 — Retest Report Section (15 minutes)

Using the following two hypothetical findings from the original engagement, draft the
findings table section of a retest report:

**FIND-001** (MS17-010 on `192.168.56.101`): Client applied patch KB4012212.
During retest, the Metasploit module `exploit/windows/smb/ms17_010_eternalblue` no longer
produces a session — the host returns an error at the exploit stage.

**FIND-002** (Weak SSH password on `192.168.56.101`): Client set a new strong password.
During retest, Hydra with the `rockyou.txt` wordlist does not crack the SSH password within
a 15-minute brute-force window. However, the SSH service still runs on the default port 22
and has no rate limiting, meaning a slower attack is still theoretically viable.

Create the following retest findings table:

| Finding ID | Original Risk | Retest Date | Verification Method | Remediation Status | Notes |
|------------|---------------|-------------|--------------------|--------------------|-------|

Assign the correct remediation status (Remediated / Partially Remediated / Not Remediated)
for each finding based on the descriptions above. Justify your classification for FIND-002
in the Notes column.

---

## Deliverables

Submit a single document to Canvas containing:

1. Part 1 screenshot (SSH login confirmation)
2. Part 2 artifact presence verification output (five commands with output)
3. Part 3 before-and-after removal output for all five artifacts
4. Part 4 SHA-256 hashes for both evidence files
5. Part 5 complete cleanup attestation document
6. Part 6 retest findings table with remediation status and justification
7. A 75–100 word reflection: Why is a signed cleanup attestation legally significant for
   the tester (not just the client)?

---

## Grading Criteria

| Component | Points |
|-----------|--------|
| SSH login screenshot | 5 |
| Artifact presence verification (all 5) | 10 |
| Artifact removal with before/after verification (all 5) | 25 |
| SHA-256 hashes computed and recorded | 10 |
| Cleanup attestation — all four sections complete | 25 |
| Retest findings table with correct status and justification | 20 |
| Reflection response | 5 |
| **Total** | **100** |

---

## Troubleshooting Guide

- **Cannot SSH into Metasploitable 2**: Verify both VMs are on the same host-only adapter
  in VirtualBox/VMware. Ping `192.168.56.101` from Kali to confirm connectivity.
- **Permission denied on rm or userdel**: Use `sudo` before the command. The msfadmin user
  has sudo access on Metasploitable 2.
- **Artifact not found during verification**: Some artifacts may not have been seeded
  correctly. Use the Lab_15_Seed.sh script from Canvas to replant them and restart from Part 2.
- **sha256sum not available**: On some minimal Kali builds, use `openssl dgst -sha256
  filename` as an alternative.

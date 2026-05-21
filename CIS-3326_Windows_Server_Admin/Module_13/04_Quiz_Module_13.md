# Quiz: Module 13 - Windows Server Backup and Recovery

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A domain controller has been infected with malware that deleted several Active Directory user objects two days ago. The AD Recycle Bin feature is enabled on the domain. Backups exist but restoring from backup would require taking the DC offline. Which recovery method should the administrator use first?

A) Perform a non-authoritative restore by booting the DC in Directory Services Restore Mode (DSRM) and restoring from the most recent backup tape.
B) Use `Restore-ADObject` in PowerShell to recover the deleted objects from the AD Recycle Bin without taking the DC offline or performing any backup restoration.
C) Seize all five FSMO roles to a healthy DC, then rebuild the infected DC from scratch and re-join it to the domain.
D) Perform an authoritative restore by booting in DSRM, restoring the backup, and running `ntdsutil` to mark the deleted objects as authoritative before rebooting.

* **Correct Answer:** B) Use `Restore-ADObject` in PowerShell to recover the deleted objects from the AD Recycle Bin without taking the DC offline or performing any backup restoration.
* **Distractor Analysis:**
  * *Why A is incorrect:* A non-authoritative restore from backup would recover the DC's AD database to the backup state, but since the deletion already replicated to all other DCs, the restored objects would be overwritten again by inbound replication. Non-authoritative restore is appropriate for database corruption, not for recovering deleted objects that have already replicated.
  * *Why C is incorrect:* Seizing FSMO roles and rebuilding the DC is a drastic, time-consuming operation appropriate for permanent DC failure — not for a malware incident where AD Recycle Bin can recover specific deleted objects in seconds without any downtime.
  * *Why D is incorrect:* An authoritative restore would work but requires booting the DC into DSRM (offline), restoring a backup, marking objects authoritative with `ntdsutil`, and rebooting — a lengthy process. When AD Recycle Bin is enabled, `Restore-ADObject` accomplishes the same result faster and without any outage.

---

### Question 2

A Windows Server administrator runs a full Windows Server Backup of a domain controller each night. The next morning, the server's C: drive fails completely. The administrator needs to restore the server to full operation, including the OS, installed roles, and all configuration. Which Windows Server Backup restore type should be performed?

A) System State restore, which recovers only the Active Directory database, SYSVOL, Registry, and boot files without restoring the full OS installation.
B) Bare-Metal Recovery (BMR), which restores the full server image — including the OS, installed roles, and all data — to new or replacement hardware.
C) File and Folder restore, which recovers individual files from the backup to a specified destination path.
D) Critical Volume restore, which restores only the volumes marked as critical by the backup job, excluding user data volumes.

* **Correct Answer:** B) Bare-Metal Recovery (BMR), which restores the full server image — including the OS, installed roles, and all data — to new or replacement hardware.
* **Distractor Analysis:**
  * *Why A is incorrect:* System State restore recovers AD-specific data (ntds.dit, SYSVOL, Registry, COM+ Class Registration, and boot files) but requires a functioning OS to be present. It cannot be used when the C: drive has failed and the OS is gone.
  * *Why C is incorrect:* File and Folder restore recovers individual files or folders to a target path — it requires a running OS and is used for data recovery scenarios, not for rebuilding a failed system drive from scratch.
  * *Why D is incorrect:* Critical Volume restore recovers volumes that are necessary for the OS to boot (typically C:) but does not include user data volumes. In practice, a full BMR restore is the correct choice when the goal is complete server recovery on new hardware after a total drive failure.

---

### Question 3

An administrator accidentally modifies the default domain password policy GPO, lowering the minimum password length from 12 to 6 characters, and the change replicates to all domain controllers. A backup of the domain controller from before the change exists. Which restore procedure correctly undoes only the GPO change without affecting any other AD objects created since the backup?

A) Perform a non-authoritative restore of the DC from backup — replication from other DCs will automatically restore the correct GPO settings after the DC reboots.
B) Perform an authoritative restore in DSRM: restore the backup, use `ntdsutil` to mark the specific GPO object as authoritative with a higher USN, then reboot so the corrected GPO replicates outward to all other DCs.
C) Delete the current default domain password policy GPO and re-create it manually with the correct settings using the Group Policy Management Console.
D) Run `gpupdate /force` on all domain controllers to force them to re-read the backup copy of the GPO from SYSVOL.

* **Correct Answer:** B) Perform an authoritative restore in DSRM: restore the backup, use `ntdsutil` to mark the specific GPO object as authoritative with a higher USN, then reboot so the corrected GPO replicates outward to all other DCs.
* **Distractor Analysis:**
  * *Why A is incorrect:* A non-authoritative restore alone would not restore the correct GPO. After the DC reboots from a non-authoritative restore, inbound replication from peer DCs would overwrite the restored GPO with the current (incorrect) version, since all other DCs already hold the modified GPO with a higher USN.
  * *Why C is incorrect:* Manually re-creating the default domain password policy GPO is possible but risky — the default domain policy GPO has a fixed GUID (`31B2F340-016D-11D2-945F-00C04FB984F9`) and contains many settings beyond password policy. Manual recreation risks missing settings that were not modified and does not follow the recommended authoritative restore procedure.
  * *Why D is incorrect:* `gpupdate /force` re-applies the current GPO settings from SYSVOL — it does not revert GPO contents to a previous backup state. Running it after the incorrect change would simply re-enforce the wrong 6-character minimum on all machines.

---

### Question 4

An organization's Recovery Time Objective (RTO) for its primary file server is 4 hours and its Recovery Point Objective (RPO) is 1 hour. The current backup strategy runs a full backup weekly on Sunday and incremental backups each weekday night. The file server fails on Friday afternoon. Approximately how much data could be lost, and does the current strategy meet the RPO?

A) Up to 5 days of data could be lost because only the full Sunday backup is used for recovery; incremental backups are not used in a bare-metal restore scenario.
B) Up to approximately 18 hours of data could be lost (since Thursday night's incremental backup), which exceeds the 1-hour RPO; the backup strategy does not meet the RPO requirement.
C) Up to approximately 18 hours of data could be lost (since Thursday night's incremental), which does not meet the 1-hour RPO. The strategy should be changed to hourly or continuous data protection backups.
D) No data would be lost because incremental backups include all changed files and the restore chain Sunday + Mon + Tue + Wed + Thu incrementals covers the full dataset up to Friday morning.

* **Correct Answer:** C) Up to approximately 18 hours of data could be lost (since Thursday night's incremental), which does not meet the 1-hour RPO. The strategy should be changed to hourly or continuous data protection backups.
* **Distractor Analysis:**
  * *Why A is incorrect:* Incremental backups are used in restoration; the restore chain is Sunday full + Monday through Thursday incrementals. The data loss is not 5 days — it is approximately the time elapsed since Thursday night's last incremental, which is roughly 18 hours of work on Friday.
  * *Why B is incorrect:* The first part of answer B correctly identifies the data loss window, but it stops at noting the RPO is not met without prescribing the corrective action. Answer C is more complete and actionable for an exam scenario.
  * *Why D is incorrect:* While the restore chain is correct, D incorrectly claims no data would be lost. Friday's work (from after Thursday night's backup until the failure) is not captured in any backup and would be lost. The RPO is not met.

---

### Question 5

An administrator needs to restore a deleted Organizational Unit (OU) that contained 300 user accounts. The domain does not have the AD Recycle Bin feature enabled. A system state backup taken 24 hours ago exists. Which procedure correctly restores the OU and its user accounts without deleting user accounts created in other OUs since the backup?

A) Restore Active Directory from the system state backup in a non-authoritative mode — replication will restore only the deleted OU while preserving newer objects on other DCs.
B) Boot the DC into Directory Services Restore Mode (DSRM), restore the system state backup non-authoritatively, then use `ntdsutil` to perform an authoritative restore of only the deleted OU subtree, and reboot to allow inbound replication to update all other objects.
C) Run `Get-ADOrganizationalUnit -Filter * | Restore-ADObject` in PowerShell to recover the OU and its contents from the deleted objects container.
D) Create a new OU with the same name, then import the 300 user accounts from a CSV file exported before the deletion occurred.

* **Correct Answer:** B) Boot the DC into Directory Services Restore Mode (DSRM), restore the system state backup non-authoritatively, then use `ntdsutil` to perform an authoritative restore of only the deleted OU subtree, and reboot to allow inbound replication to update all other objects.
* **Distractor Analysis:**
  * *Why A is incorrect:* A purely non-authoritative restore restores the backup database on that DC, but when the DC reboots and reconnects to the domain, inbound replication from other DCs will overwrite the restored OU and user objects with their current state (deleted), since the deletion already replicated with a higher USN. Non-authoritative restore alone does not recover deleted objects.
  * *Why C is incorrect:* `Restore-ADObject` works from the AD Recycle Bin — it does not function without the Recycle Bin enabled. When the Recycle Bin is not enabled, deleted objects are fully stripped of most attributes after a configurable tombstone period and cannot be recovered this way.
  * *Why D is incorrect:* Manually creating an OU and importing user accounts from a CSV would require a pre-existing export with all 300 users' attributes (passwords, group memberships, profile paths, etc.). This approach is incomplete, error-prone, and does not restore SID-based permissions, group memberships, or account history — all of which are preserved by an authoritative restore.

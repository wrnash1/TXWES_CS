# Reading Guide: Module 13 - Windows Server Backup and Recovery

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 13 – Windows Server Backup and Recovery**! This week's study material covers how to protect Windows Server data and system state using built-in backup tools and how to recover from failures ranging from deleted files to a completely failed Domain Controller. Backup and recovery scenarios are consistently tested on both AZ-800 and AZ-801 exams.

As a student, you will learn Windows Server Backup, Active Directory recycle bin and authoritative restore, Volume Shadow Copy Service (VSS), and how Recovery Time Objective (RTO) and Recovery Point Objective (RPO) drive backup strategy decisions. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Windows Server Backup (WSB)**: A built-in backup feature installed as a Windows feature. It supports full server backups, system state backups, and individual volume or folder backups to local disks, network shares, or Windows Azure. It uses VSS for application-consistent backups.
* **System State Backup**: A backup of the critical operating system components: the registry, boot files, COM+ class registration database, and — on a Domain Controller — the AD DS database (NTDS.dit), SYSVOL, and certificate services database. Required for DC recovery.
* **Authoritative Restore (AD DS)**: A restore method that forces the recovered AD DS data to replicate outward to all other DCs, overwriting any later changes. Used when an object (such as an OU full of users) is accidentally deleted from all DCs and must be recovered from a backup. Performed using `ntdsutil` with the "authoritative restore" command.
* **Non-Authoritative Restore**: The default AD DS restore method. The restored DC accepts replication from other DCs and updates itself to reflect the current state of the directory. Used to recover a single failed DC when the deletion or corruption has not propagated across all DCs.
* **Active Directory Recycle Bin**: An AD DS feature (requires a minimum domain functional level of Windows Server 2008 R2) that retains deleted objects in a "deleted" state for a configurable period (default 180 days), preserving all attributes. Objects can be restored with a single PowerShell cmdlet (`Restore-ADObject`) without needing a backup.
* **Volume Shadow Copy Service (VSS)**: A Windows framework that creates point-in-time, application-consistent snapshots of volumes. VSS coordinates with applications (SQL Server, Exchange) to quiesce writes before the snapshot is taken, ensuring data integrity. Previous Versions in Windows Explorer uses VSS shadows.

---

### 2. Certification Exam Tips

* **Authoritative vs. non-authoritative restore decision**: AZ-800 and AZ-801 heavily test this distinction. If one DC failed but the directory is intact on other DCs, use non-authoritative restore — the DC will replicate current data from its peers. If the wrong change (mass deletion, bad GPO) replicated to all DCs, use authoritative restore to push the recovered data back out.
* **AD Recycle Bin before authoritative restore**: If AD Recycle Bin is enabled, always try `Restore-ADObject` first — it is faster, preserves all attributes, and does not require taking a DC offline. Only fall back to authoritative restore from backup if Recycle Bin is not enabled or the retention period has expired.
* **RTO vs. RPO in strategy questions**: Recovery Time Objective (RTO) is the maximum acceptable downtime. Recovery Point Objective (RPO) is the maximum acceptable data loss (time since last backup). More frequent backups lower RPO but increase storage and cost. Exam scenarios ask you to choose a backup frequency or method that satisfies given RTO/RPO requirements.
* **Microsoft Learn Reference**: Review backup and recovery documentation at [Microsoft Learn – Windows Server Backup](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-backup/windows-server-backup-overview) and [Microsoft Learn – AD DS Backup and Recovery](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-guide).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the backup and recovery documentation at [Microsoft Learn: Windows Server Backup Overview](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-backup/windows-server-backup-overview) and the AD DS recovery guide at [Microsoft Learn: AD Forest Recovery Guide](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-guide). Focus on system state backup, authoritative restore procedures, and the AD Recycle Bin.
* **Required Video:** Watch the video lecture on **Windows Server Backup and Recovery** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will install Windows Server Backup, perform a system state backup of a Domain Controller, enable the Active Directory Recycle Bin, delete and restore an AD user object using `Restore-ADObject`, and review VSS shadow copies on a file server volume.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the backup documentation at [Microsoft Learn: Windows Server Backup Overview](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-backup/windows-server-backup-overview).
* [ ] Read the AD DS recovery guide at [Microsoft Learn: AD Forest Recovery Guide](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-guide).
* [ ] Watch the video lecture on **Windows Server Backup and Recovery** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.

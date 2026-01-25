# CIS-3325: Operating System Administration Labs (LPI/LFCSA Alignment)

## Lab 1: Advanced CLI & Scripting
**Objective**: Automate tasks using Bash scripting and advanced grep/sed/awk.

1.  **Archiving**: Create a compressed tarball of the `/etc` directory in your home folder: `tar -czvf etc_backup.tar.gz /etc`.
2.  **Searching**: Find all files in `/etc` that have been modified in the last 24 hours.
3.  **Scripting**: Create a script `backup_user.sh` that takes a username as an argument and backs up their home directory.
4.  **Automation**: Schedule a `cron` job that runs your backup script every night at midnight.

## Lab 2: Storage Management & File Systems
**Objective**: Manage disks, partitions, and logical volumes.

1.  **Disk Inventory**: Run `lsblk` to view all attached storage devices.
2.  **Partitions**: Use `fdisk` or `parted` (conceptually) to explain how to create a new partition.
3.  **LVM**: List all Physical Volumes (PV), Volume Groups (VG), and Logical Volumes (LV) on the system.
4.  **Mounting**: Create a temporary mount point `/mnt/data` and mount a disk to it.

## Lab 3: System Hardening & Log Analysis
**Objective**: Secure the OS and monitor system events.

1.  **Log Rotation**: Inspect `/etc/logrotate.conf`. Why is log rotation important for server stability?
2.  **Journalctl**: Filters logs to show only "Critical" or "Error" messages from the current boot.
3.  **SELinux**: Check the status of SELinux using `sestatus`.
4.  **Users**: Delete the user `labuser` created in previous modules and ensure their home directory is also removed.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.

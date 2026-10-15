# Video Script: CIS-3325 Operating System Administration (CompTIA Linux+ XK0-005)
## Module 05: Enterprise Automation with Bash Shell Scripting (Part 3)
### Recorded by Professor Nash | Texas Wesleyan University

**Runtime:** 18:45 minutes  
**Target Certification Domain:** CompTIA Linux+ Domain 4.1 (Given a scenario, configure and execute basic Bash scripts)

---

## Part 1: Automated Archival Architecture in Linux

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA Linux+ / Linux Foundation &bull; Operating System Administration &bull; Module 05</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ / Linux Foundation &bull; Operating System Administration" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ / Linux Foundation &bull; Operating System Administration</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**[CAMERA: Cut to terminal workbench displaying /etc filesystem]**

Welcome back, class. In Part 1 and Part 2 of Module 05, we mastered Bash variable assignment, positional parameters, conditional exit statuses, and loop constructs. Today in Part 3, we bring everything together into a mission-critical system administration task: writing a fully automated, idempotent backup and archival script using `tar`, `gzip`, and date formatting.

In production system administration, manual backups are an invitation to catastrophic data loss. As a Linux system administrator, you must automate repetitive operational tasks so they run deterministically without human intervention. Today, we will write a production-grade backup script that compresses the `/etc` configuration directory, verifies file integrity, names the archive with a precise timestamp, and stores it securely in a target destination.

Let's dissect the core commands we will use.

---

## Part 2: Dissecting `tar` and Compression Flags
**[SHOW SCREEN: Highlighting tar syntax: `tar -czvf /destination/backup.tar.gz /source` ]**

The primary tool for archiving in Linux is `tar` — which stands for Tape Archive. `tar` groups multiple files and directories into a single archive file, preserving file permissions, ownership, and directory hierarchies.

Notice the flags we are using:
- `-c`: **Create** a new archive file.
- `-z`: Filter the archive through **gzip** compression, reducing file size significantly.
- `-v`: **Verbosely** list the files being processed. Excellent for debugging and log tracking.
- `-f`: Specify the **filename** of the archive. *Exam rule:* The `-f` flag must immediately precede the archive name.

If we want higher compression at the cost of CPU cycles, we would use `-j` for `bzip2` (`.tar.bz2`) or `-J` for `xz` (`.tar.xz`). On CompTIA Linux+, you will be asked to distinguish between `-z` (`gzip`), `-j` (`bzip2`), and `-J` (`xz`). Memorize that difference.

---

## Part 3: Writing the Production-Grade Backup Script
**[SHOW SCREEN: Writing `backup_etc.sh` in vim/nano]**

Now, let's open our editor and write `backup_etc.sh`. Notice how we adhere to enterprise shell scripting best practices:

```bash
#!/bin/bash
# ==============================================================================
# Script Name: backup_etc.sh
# Purpose:     Automate compressed archival of /etc configuration hierarchy
# Author:      Texas Wesleyan University - CIS-3325 System Administration
# ==============================================================================

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Configuration Variables
SOURCE_DIR="/etc"
DEST_DIR="${HOME}/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="etc_backup_${TIMESTAMP}.tar.gz"
TARGET_PATH="${DEST_DIR}/${ARCHIVE_NAME}"

echo "=== [$(date)] Starting Automated Archival Procedure ==="

# 1. Ensure backup directory exists
if [ ! -d "${DEST_DIR}" ]; then
    echo "Creating backup directory: ${DEST_DIR}"
    mkdir -p "${DEST_DIR}"
fi

# 2. Execute tar archive with error handling
echo "Archiving ${SOURCE_DIR} to ${TARGET_PATH}..."
if tar -czf "${TARGET_PATH}" "${SOURCE_DIR}" 2>/dev/null; then
    ARCHIVE_SIZE=$(du -h "${TARGET_PATH}" | awk '{print $1}')
    echo "✓ Backup completed successfully."
    echo "  Archive: ${TARGET_PATH}"
    echo "  Size:    ${ARCHIVE_SIZE}"
else
    echo "❌ Error: Backup failed during tar execution!" >&2
    exit 1
fi

# 3. Verify archive integrity
echo "Verifying archive integrity via gzip test..."
if gzip -t "${TARGET_PATH}"; then
    echo "✓ Archive integrity verified. Gzip test passed."
else
    echo "❌ Error: Corrupted archive detected!" >&2
    exit 2
fi

echo "=== [$(date)] Backup Job Complete ==="
exit 0
```

Notice the defensive programming lines:
1. `set -euo pipefail`: Prevents silent script failures on unset variables or failed pipeline commands.
2. `TIMESTAMP=$(date +"%Y%m%d_%H%M%S")`: Guarantees unique, chronological filenames that sort cleanly in directories.
3. `gzip -t`: Tests the compressed archive's cyclic redundancy check (CRC) to ensure no corruption occurred during write operations.

---

## Part 4: Permissions, Execution, and Lab Deliverables
**[SHOW SCREEN: Setting permissions with `chmod +x` and verifying with `ls -la`]**

Once your script is saved, you must give it execute permissions before running it:
```bash
chmod +x backup_etc.sh
./backup_etc.sh
```

Inspect the destination directory:
```bash
ls -lh ~/backups/
```
You will see your newly created `.tar.gz` archive with its accurate timestamp and compression ratio.

**Your Module 05 Deliverable:**
1. Save your completed script as `backup_etc.sh`.
2. Execute the script in your Linux virtual machine.
3. Capture a clear terminal screenshot showing the script execution output and the `ls -lh ~/backups/` directory listing.
4. Submit the script file and your verification screenshot to Canvas.

In our next module, we will explore Linux storage management, partitioning with `fdisk` and `parted`, and building logical volumes with LVM. I will see you in Module 06!

# Operating System Labs (LPI/CompTIA Linux+ Alignment)

## Lab 1: Essential Command Line & File System
**Objective**: Master navigation, file manipulation, and the Linux directory structure (FHS).

1.  **Navigation**: Navigate to `/var/log`. List all files in human-readable format.
2.  **File Creation**: Create a directory in your home folder called `Lab1`. Inside it, create five empty files named `file1.txt` through `file5.txt`.
3.  **Redirection**: Run `ls -l /etc > /home/student/Lab1/etc_list.txt`.
4.  **Searching**: Use `grep` to find the string "root" in `/etc/passwd`.

## Lab 2: Users, Groups, and Permissions
**Objective**: Understand the Linux security model and permission strings.

1.  **Permissions**: Change the permissions of `file1.txt` so that only the owner can read/write, and no one else has any access.
2.  **Ownership**: Verify the owner and group of `/etc/shadow`. Why can't you read it as a normal student user?
3.  **Sudo**: Use `sudo` to create a new user named `labuser`.
4.  **Group Management**: Create a group called `research` and add `student` and `labuser` to it.

## Lab 3: Process and Service Management
**Objective**: Monitor system resources and manage background services.

1.  **Top**: Run `top` (or `htop` if installed). Identify the process with the highest CPU usage.
2.  **Killing Processes**: Start a `sleep 1000 &` process. Find its PID and kill it.
3.  **Systemd**: Use `systemctl status sshd`. Is the SSH service running?
4.  **Logs**: View the last 20 lines of the system journal using `journalctl -n 20`.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.

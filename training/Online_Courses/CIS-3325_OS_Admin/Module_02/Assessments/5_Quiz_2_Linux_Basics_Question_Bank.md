### 5. Quiz 2: Linux Basics (Question Bank)
**Question 1**
Which directory in the Linux Filesystem Hierarchy Standard (FHS) is specifically designated to hold system-wide configuration files?
A) /bin
B) /var
C) /etc
D) /home
*   **Correct Answer:** C) /etc
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `/bin` contains essential user command binaries (like `ls` and `cp`), not configuration files.
    *   *Why B is incorrect:* `/var` contains variable data that changes rapidly, such as system logs and print spools.
    *   *Why D is incorrect:* `/home` contains the personal directories and files for individual users, not system-wide configurations.

**Question 2**
You are currently in the directory `/home/user/documents/`. You want to navigate directly to the `/var/log/` directory using an absolute path. Which command should you use?
A) cd ../../var/log
B) cd /var/log
C) cd var/log
D) cd ~/var/log
*   **Correct Answer:** B) cd /var/log
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is a relative path utilizing `../` to go up two directories. While it works, it is not an *absolute* path.
    *   *Why C is incorrect:* Missing the leading forward slash makes this a relative path; the shell will look for a folder named `var` inside your current `documents` directory and fail.
    *   *Why D is incorrect:* The tilde `~` expands to the user's home directory (`/home/user/`). This command would try to navigate to `/home/user/var/log`, which likely doesn't exist.

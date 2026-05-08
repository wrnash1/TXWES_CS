### 3. Reading Guide: LPI Linux Essentials Chapter 5
**High-Yield Concepts:**
1. **The root user:** The superuser in Linux. The root user ignores all permission restrictions. You should never log in directly as root; instead, use the `sudo` command to execute administrative tasks temporarily.
2. **chown:** Command to change the owner and/or group of a file (e.g., `chown alice:sales report.txt`).
3. **umask:** The default permission mask applied when a new file or directory is created. It subtracts permissions from a base of 666 (files) or 777 (directories).

---

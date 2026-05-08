### 5. Quiz 3: Users and Permissions (Question Bank)
**Question 1**
An administrator executes the command `chmod 644 confidential.txt`. What permissions does this command assign to the file?
A) The owner has read and write access, while the group and others have read-only access.
B) The owner has full access (read, write, execute), while the group has read-only access.
C) The owner has read-only access, while the group and others have read and write access.
D) The owner and the group have read and write access, while others have no access.
*   **Correct Answer:** A) The owner has read and write access, while the group and others have read-only access.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Full access is represented by a 7 (4+2+1). The first digit here is a 6 (4+2 = read+write).
    *   *Why C is incorrect:* This describes permissions of 466, which is an invalid and insecure configuration.
    *   *Why D is incorrect:* This describes permissions of 660, not 644. The digit 4 represents read-only access.

**Question 2**
Which file in a standard Linux system contains the securely hashed passwords for local user accounts?
A) /etc/passwd
B) /etc/shadow
C) /etc/group
D) /var/log/auth.log
*   **Correct Answer:** B) /etc/shadow
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Historically, passwords were stored here, but today `/etc/passwd` only contains user information (UID, home directory, shell) and an 'x' indicating the password is in the shadow file.
    *   *Why C is incorrect:* `/etc/group` defines local groups and their members, not passwords.
    *   *Why D is incorrect:* The `auth.log` records authentication attempts (logins, sudo usage), not the actual password hashes.

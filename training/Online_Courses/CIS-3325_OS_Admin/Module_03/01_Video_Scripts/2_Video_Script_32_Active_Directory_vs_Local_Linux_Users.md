### 2. Video Script 3.2: Active Directory vs. Local Linux Users
**Estimated Duration:** 5 minutes
**Visual:** Split screen. Left: `/etc/passwd` file in Linux. Right: Active Directory Users and Computers in Windows.
**[Alt-text: Left side shows a text file listing local Linux users separated by colons. Right side shows the graphical ADUC interface listing domain users.]**
**Audio:** "When you run the `useradd` command in Linux, you are creating a local user. That user's information is stored in the `/etc/passwd` file, and their hashed password is in `/etc/shadow`. They can only log into that specific Linux server. Active Directory, on the other hand, creates Domain Users. Once created in the central AD database, that user can log into thousands of different Windows machines. While Linux *can* be joined to Active Directory via tools like SSSD or winbind, its default state is local user management."

---

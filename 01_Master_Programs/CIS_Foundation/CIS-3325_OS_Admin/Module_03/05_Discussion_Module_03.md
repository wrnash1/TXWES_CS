# Discussion Forum: Module 03 - File Permissions and Ownership

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content.

---

### Scenario A - Compromised SUID Binary

A security audit of a production web server reveals an unexpected SUID binary at
/usr/local/bin/syscheck owned by root with permissions -rwsr-xr-x. No one on the team remembers
creating it or authorizing it. The server hosts a public-facing e-commerce application.

1. Explain exactly what an attacker could accomplish if they planted this SUID binary. Why is
   having a root-owned SUID executable particularly dangerous compared to a normal executable?
2. Describe the exact sequence of commands you would run to investigate this file, including how
   to find when it was created, what user account might have created it, and what the binary does.
3. Beyond removing this specific file, what two ongoing controls would you implement to detect
   unauthorized SUID files in the future?

---

### Scenario B - Shared Project Directory Permissions

Your team is setting up a shared development server where eight developers must all read and
write code in /opt/codebase. New files created by any developer should automatically belong to
the devteam group so all team members can read them. Developers should not be able to delete
each other's work.

1. Write the exact sequence of commands (mkdir, chown, chmod) to create this shared directory
   with all three requirements met: shared write access, automatic group inheritance, and
   deletion protection. Explain the purpose of each command.
2. A new developer named ramos joins the team. Write the commands to create their account, set
   a password, add them to devteam, and verify the group membership.
3. Explain how the umask setting interacts with this directory. If ramos has umask 077, will the
   SGID group inheritance still work? What is the practical implication for your team setup?

---

### Scenario C - Sensitive Configuration File Breach

An audit reveals that a database configuration file at /etc/myapp/db.conf containing the
production database password is readable by all users (permissions 644). An intern who recently
left the company had access to this server. You need to assess the damage and fix the permissions.

1. Explain why chmod 644 on a file containing a password is a serious security violation. Who
   specifically can read a file with permissions 644, and what is the risk if any of those
   users are compromised or malicious?
2. Write the exact commands to change the permissions on /etc/myapp/db.conf so that only the
   application's service account (named appservice) can read and write it, and no other user
   has any access.
3. Beyond changing file permissions, what two additional steps should you take after discovering
   that a sensitive credential file was world-readable? Consider both the technical remediation
   and the organizational response.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 03 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Permissions are not bureaucracy. They are the lock on the door. Every misconfigured permission
is an unlocked door somewhere in your system. The scenarios in this discussion represent real
incidents that happen in real organizations - SUID backdoors planted by attackers, shared
directories that turn into free-for-alls, and credential files that sit exposed for months or
years because nobody thought to check. When you deeply understand permissions - not just the
syntax but the why behind every decision - you become the administrator who prevents incidents
rather than the one who discovers them. Think carefully about what you write here.

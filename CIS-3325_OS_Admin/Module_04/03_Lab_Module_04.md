# Lab 04: User and Group Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will create and manage user accounts and groups, configure password aging,
test the usermod -aG behavior, lock and unlock accounts, and configure sudo access using visudo.
These are core daily administration tasks and heavily tested on the Linux+ exam.

**What you will practice:**

- useradd with various flags
- passwd and chage for password management
- usermod -aG for group membership
- groupadd and groupdel
- usermod -L and -U for account locking
- visudo for sudo configuration
- id and groups for verification

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin
- You have watched both parts of the Module 04 video lecture
- You have read the Module 04 Reading Guide

---

### Part 1 - Exploring Existing Identity Files

**Step 1.1 - Review /etc/passwd**

```bash
cat /etc/passwd
```

Count the total number of user accounts:

```bash
wc -l /etc/passwd
```

Show only accounts with UID 1000 or higher (regular users):

```bash
awk -F: '$3 >= 1000 {print $1, $3, $6, $7}' /etc/passwd
```

**Step 1.2 - Review /etc/shadow (requires sudo)**

```bash
sudo cat /etc/shadow | grep -v "^#"
```

Note the hash format. Lines with * or ! in the password field are locked or have no password.

**Step 1.3 - Review /etc/group**

```bash
cat /etc/group | grep -v "^#"
```

Find the sudo group and note its members:

```bash
grep "^sudo:" /etc/group
```

**Step 1.4 - Review /etc/skel**

```bash
ls -la /etc/skel/
```

Note the template files that new users receive.

---

### Part 2 - Creating User Accounts

**Step 2.1 - Create users with different configurations**

Create a developer user with a home directory and bash shell:

```bash
sudo useradd -m -s /bin/bash -c "Developer Account" dev1
id dev1
ls -la /home/dev1/
```

Create a second developer:

```bash
sudo useradd -m -s /bin/bash -c "Developer Account 2" dev2
```

Create a service account with no login shell:

```bash
sudo useradd -r -s /usr/sbin/nologin -c "Web Application Service" webappuser
id webappuser
```

Verify the UID range difference between dev1 and webappuser:

```bash
id dev1
id webappuser
```

dev1 should have UID 1000+ and webappuser should have UID under 1000 (system account).

**Step 2.2 - Set passwords**

```bash
sudo passwd dev1
```

Enter a password when prompted. For lab purposes, use a simple memorable password like
Lab$ecure1.

```bash
sudo passwd dev2
```

Set the same or different password.

**Step 2.3 - Configure password aging**

```bash
sudo chage -M 90 -W 14 dev1
sudo chage -l dev1
```

Verify the password aging policy shows max 90 days and 14-day warning.

Force a password change at next login for dev2:

```bash
sudo chage -d 0 dev2
sudo chage -l dev2
```

The "Last password change" should show as "password must be changed."

---

### Part 3 - Group Management and Membership

**Step 3.1 - Create groups**

```bash
sudo groupadd developers
sudo groupadd devops
sudo groupadd readonly
cat /etc/group | grep -E "developers|devops|readonly"
```

**Step 3.2 - Add users to groups with usermod -aG**

```bash
sudo usermod -aG developers dev1
sudo usermod -aG developers dev2
sudo usermod -aG devops dev1
id dev1
id dev2
```

dev1 should now be in both developers and devops. dev2 should be in developers only.

**Step 3.3 - Demonstrate the -aG vs -G difference**

First, check dev1's current groups:

```bash
id dev1
```

Record all groups shown.

Now accidentally use -G without -a:

```bash
sudo usermod -G readonly dev1
id dev1
```

dev1 is now ONLY in readonly. All other supplementary groups (developers, devops) were removed.

Now fix it properly by adding all needed groups back:

```bash
sudo usermod -aG developers,devops dev1
id dev1
```

dev1 should now be in developers, devops, and readonly.

This demonstrates why -aG is critical.

**Step 3.4 - Verify /etc/group**

```bash
grep "developers\|devops\|readonly" /etc/group
```

Confirm both dev1 and dev2 are listed in developers.

---

### Part 4 - Account Locking and Unlocking

**Step 4.1 - Lock an account**

```bash
sudo usermod -L dev2
sudo grep "^dev2:" /etc/shadow
```

The hash should now start with ! indicating the account is locked.

Attempt to switch to the locked account:

```bash
sudo su - dev2
```

Expected result: Authentication failure or "This account is currently not available" message.

**Step 4.2 - Unlock the account**

```bash
sudo usermod -U dev2
sudo grep "^dev2:" /etc/shadow
```

The ! prefix should be removed. Verify the unlock worked.

**Step 4.3 - Alternative lock with passwd**

```bash
sudo passwd -l dev1
sudo grep "^dev1:" /etc/shadow
```

passwd -l also locks an account by prefixing the hash with !!.

```bash
sudo passwd -u dev1
```

passwd -u unlocks it.

---

### Part 5 - sudo Configuration with visudo

**Step 5.1 - View current sudo configuration**

```bash
sudo cat /etc/sudoers
```

Note the line granting sudo group members full access:
%sudo   ALL=(ALL:ALL) ALL

**Step 5.2 - Grant full sudo access to dev1**

```bash
sudo visudo
```

Inside visudo, add this line after the root line:

```
dev1    ALL=(ALL:ALL) ALL
```

Save and exit (Ctrl+X, Y, Enter for nano; :wq for vi/vim).

Test the configuration:

```bash
sudo su - dev1
sudo whoami
exit
```

dev1 should be able to run sudo commands.

**Step 5.3 - Grant limited sudo access**

```bash
sudo visudo
```

Add a line granting dev2 permission to run only systemctl for the ssh service:

```
dev2    ALL=(root) /usr/bin/systemctl restart ssh, /usr/bin/systemctl status ssh
```

Test from dev2's account:

```bash
sudo su - dev2
sudo systemctl status ssh
sudo systemctl restart ssh
sudo systemctl restart nginx
exit
```

The first two commands should succeed. The third (nginx) should fail with a "not allowed" error.

**Step 5.4 - Remove the custom sudo entries**

After testing, remove the custom sudo entries to restore the clean state:

```bash
sudo visudo
```

Delete the lines you added for dev1 and dev2.

---

### Part 6 - The su Command

**Step 6.1 - Switch user with login shell**

```bash
sudo su - dev1
pwd
echo $HOME
exit
```

With the hyphen, su - loads dev1's full environment including home directory.

**Step 6.2 - Switch user without login shell**

```bash
sudo su dev1
pwd
echo $HOME
exit
```

Without the hyphen, you switch to dev1 but the environment variables still reference the
previous user's settings.

Note the difference in the current directory and $HOME variable between the two approaches.

---

### Part 7 - Cleanup

Remove the test accounts and groups created in this lab:

```bash
sudo userdel -r dev1
sudo userdel -r dev2
sudo userdel webappuser
sudo groupdel developers
sudo groupdel devops
sudo groupdel readonly
```

Verify cleanup:

```bash
grep -E "^dev1:|^dev2:|^webappuser:" /etc/passwd
grep -E "^developers:|^devops:|^readonly:" /etc/group
```

Both commands should return no output, confirming the accounts and groups were removed.

---

### Part 8 - Analysis Questions

**Question 1:** In Step 3.3, you accidentally ran usermod -G readonly dev1 and it removed dev1
from the developers and devops groups. Explain the exact mechanism: what does -G do without -a,
and why is this the default behavior? Write the correct command you should always use to add a
user to a group.

**Question 2:** You created webappuser with /usr/sbin/nologin as the shell. Explain why this is
important for service accounts. What would happen if a service account had /bin/bash as its shell
and the application running as that account was compromised?

**Question 3:** You used visudo to edit /etc/sudoers. The lab asked you to never use nano or vi
directly on this file. Explain exactly what could go wrong if you edited /etc/sudoers directly
with nano, introduced a syntax error, and saved it. What would the impact be and how would you
recover?

**Question 4:** chage -d 0 forces a password change at next login. Explain why this is a
security best practice for new user accounts. What is the risk if a new user account is created
without this control and the temporary password is sent over email?

**Question 5:** Ubuntu uses the sudo group for privilege escalation while RHEL uses the wheel
group. You need to grant a new user sudo access on both systems in your environment. Write the
exact commands for each platform.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 2, Step 2.1 showing id dev1 and id webappuser (note UID difference)
2. Screenshot of Part 2, Step 2.3 showing chage -l dev1 output
3. Screenshot of Part 3, Step 3.3 showing id dev1 BEFORE the -G mistake, AFTER the mistake, and after the fix
4. Screenshot of Part 4, Step 4.1 showing /etc/shadow with the ! lock prefix
5. Screenshot of Part 5, Step 5.2 showing successful sudo whoami as dev1
6. Screenshot of Part 5, Step 5.3 showing denied access when dev2 tries sudo for nginx
7. Screenshot of Part 6 showing the difference between su - and su (without hyphen) in pwd output
8. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| UID comparison screenshot (dev1 vs webappuser) | 10 |
| chage -l dev1 screenshot | 10 |
| -aG vs -G demonstration (3 screenshots) | 15 |
| Shadow file lock (!) screenshot | 10 |
| sudo whoami as dev1 screenshot | 10 |
| Limited sudo denial screenshot | 10 |
| su vs su - difference screenshot | 5 |
| Analysis Question 1 (-aG explanation) | 5 |
| Analysis Question 2 (service account shells) | 5 |
| Analysis Question 3 (visudo safety) | 5 |
| Analysis Question 4 (chage -d 0) | 5 |
| Analysis Question 5 (sudo vs wheel) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

**Challenge Step 1 — Implement password quality enforcement with PAM**

Configure the pam_pwquality module to enforce a minimum password length of 14 characters
with complexity requirements across all local accounts:

```bash
sudo apt install -y libpam-pwquality
sudo cp /etc/security/pwquality.conf /etc/security/pwquality.conf.bak
sudo tee /etc/security/pwquality.conf > /dev/null << 'EOF'
minlen = 14
dcredit = -1
ucredit = -1
lcredit = -1
ocredit = -1
maxrepeat = 3
EOF
cat /etc/security/pwquality.conf
```

Test the policy by attempting to set a weak password for dev1:

```bash
sudo passwd dev1
```

Try entering "password" and then "Password1!" and observe which are rejected. Then set a
compliant password. Document the rejection messages and explain in two sentences what each
pwquality.conf parameter controls.

**Challenge Step 2 — Configure sudo with command aliasing and logging**

Create a production-style sudoers configuration using command aliases and verify audit
logging:

```bash
sudo visudo -f /etc/sudoers.d/lab-policy
```

Enter the following content using visudo (it will validate syntax before saving):

```
Cmnd_Alias NETWORK_CMDS = /usr/sbin/iptables, /usr/bin/ss, /usr/sbin/ip
Cmnd_Alias SERVICE_CMDS = /usr/bin/systemctl start *, /usr/bin/systemctl stop *, /usr/bin/systemctl restart *, /usr/bin/systemctl status *
Cmnd_Alias FORBIDDEN = /usr/bin/su, /usr/sbin/visudo, /usr/bin/passwd root

dev1 ALL=(root) NOPASSWD: NETWORK_CMDS, SERVICE_CMDS
dev1 ALL=(root) !FORBIDDEN
```

Test the policy:

```bash
sudo -u dev1 sudo systemctl status ssh
sudo -u dev1 sudo su -
sudo tail -20 /var/log/auth.log | grep sudo
```

Document which commands succeeded and which were denied. Explain in two sentences how the
! (negation) operator in sudoers prevents privilege escalation even when broader rules exist.

**Challenge Step 3 — Audit all accounts for security compliance**

Write a security audit report for all local user accounts by examining /etc/passwd,
/etc/shadow, and running chage checks:

```bash
awk -F: '$7 !~ /nologin|false/ && $3 >= 1000 {print $1}' /etc/passwd
for user in $(awk -F: '$7 !~ /nologin|false/ && $3 >= 1000 {print $1}' /etc/passwd); do
  echo "=== $user ==="; chage -l $user; echo
done
sudo awk -F: '$2 == "" {print $1 ": NO PASSWORD SET"}' /etc/shadow
sudo awk -F: '$2 ~ /^[^!$]/ && $2 != "x" {print $1 ": UNSHADOWED PASSWORD"}' /etc/shadow
find /home -maxdepth 1 -type d | while read d; do
  ls -la "$d" | head -3
done
```

Document all findings. Identify any accounts that: have no password set, have shells
allowing login but no password aging configured, or have home directories with overly
permissive ownership. Propose remediation commands for each finding.

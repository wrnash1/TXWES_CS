# Lab: Module 07 — User and Group Administration

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Lab Overview

In this lab you will build a complete user and group administration environment simulating a small software company's Linux infrastructure. You will create user accounts, configure groups, set password policies, configure sudo access, and investigate the configuration files that support everything you build.

**Estimated Time:** 60–90 minutes

**Required Environment:** Linux VM (Ubuntu 22.04 LTS or RHEL/Rocky Linux 9 recommended). All tasks can be performed on any major Linux distribution with minor command adjustments noted in the instructions.

---

## Prerequisites

- Completion of Module 07 video lectures (Parts 1 and 2)
- A running Linux VM with sudo access
- Basic familiarity with the terminal from previous modules

---

## Scenario

You are a Linux systems administrator for **Ramrod Software**, a fictional company. Your manager has asked you to:

1. Create user accounts for three new employees
2. Organize them into appropriate groups
3. Set a company password policy
4. Grant the senior developer sudo access to restart the web service only
5. Configure and verify the sudoers policy
6. Investigate the identity configuration files

---

## Task 1 — Explore Existing User Infrastructure

Before adding anything, understand what already exists.

### Step 1.1 — Examine /etc/passwd

```bash
# Count the number of user accounts
wc -l /etc/passwd

# Find the first regular user account (UID >= 1000)
awk -F: '$3 >= 1000 {print}' /etc/passwd

# Display accounts that can log in (not nologin/false)
grep -v "nologin\|false" /etc/passwd

# Show just usernames and UIDs
awk -F: '{print $1, $3}' /etc/passwd | sort -k2 -n | tail -10
```

Record the last assigned UID in your lab notes.

### Step 1.2 — Examine /etc/group

```bash
# List all groups
cat /etc/group

# Find groups with GID >= 1000 (regular groups)
awk -F: '$3 >= 1000 {print}' /etc/group

# Check if wheel or sudo group exists
grep "^wheel\|^sudo" /etc/group
```

### Step 1.3 — Examine Default Settings

```bash
# View useradd defaults
useradd -D

# View login.defs
grep -v "^#\|^$" /etc/login.defs

# View skeleton directory
ls -la /etc/skel
```

---

## Task 2 — Create Groups for the Development Team

Create three groups to organize the new employees.

### Step 2.1 — Create Groups

```bash
# Create the development team groups
sudo groupadd -g 2000 developers
sudo groupadd -g 2001 qa
sudo groupadd -g 2002 devops

# Verify creation
grep "developers\|qa\|devops" /etc/group
```

### Step 2.2 — Verify Group IDs

```bash
# Use getent to verify (NSS-aware)
getent group developers
getent group qa
getent group devops
```

**Lab Question 1:** What would happen if you tried to create a group with a GID already in use? Test this:

```bash
# This should fail with an error
sudo groupadd -g 2000 testgroup
echo "Exit code: $?"
```

Record the error message and exit code.

---

## Task 3 — Create User Accounts

Create accounts for three employees.

### Step 3.1 — Create the Senior Developer (Alice Wilson)

```bash
sudo useradd \
  -m \
  -c "Alice Wilson, Senior Developer" \
  -s /bin/bash \
  -g developers \
  -G devops \
  -u 2001 \
  awilson

# Verify the account
grep awilson /etc/passwd
id awilson
ls -la /home/awilson
```

### Step 3.2 — Create the QA Engineer (Bob Martinez)

```bash
sudo useradd \
  -m \
  -c "Bob Martinez, QA Engineer" \
  -s /bin/bash \
  -g qa \
  -u 2002 \
  bmartin

grep bmartin /etc/passwd
id bmartin
```

### Step 3.3 — Create a Contractor Account (Temp User)

```bash
sudo useradd \
  -m \
  -c "Temp Contractor" \
  -s /bin/bash \
  -g developers \
  -e $(date -d "+30 days" +%Y-%m-%d) \
  contractor1

grep contractor1 /etc/passwd
sudo chage -l contractor1
```

**Lab Question 2:** What does the `-e` flag with a future date accomplish? In what file is this expiration stored?

---

## Task 4 — Set Passwords and Password Policy

### Step 4.1 — Set Initial Passwords

```bash
# Set passwords for each account
sudo passwd awilson
# Enter: TempPass123! (or any password your VM's policy accepts)

sudo passwd bmartin
sudo passwd contractor1
```

### Step 4.2 — Apply Company Password Policy

Ramrod Software requires:

- Maximum password age: 90 days
- Minimum password age: 1 day (prevents immediate re-use cycling)
- 14-day warning before expiration
- 30-day inactive period before account is disabled
- Alice must change her password at first login

```bash
# Apply policy to awilson
sudo chage -m 1 -M 90 -W 14 -I 30 awilson

# Force password change at first login
sudo chage -d 0 awilson

# Apply policy to bmartin
sudo chage -m 1 -M 90 -W 14 -I 30 bmartin

# Contractor has a shorter policy
sudo chage -m 0 -M 30 -W 7 contractor1

# Verify all policies
sudo chage -l awilson
sudo chage -l bmartin
sudo chage -l contractor1
```

### Step 4.3 — Examine the Shadow File

```bash
# View shadow entries for the new accounts (root required)
sudo grep "awilson\|bmartin\|contractor1" /etc/shadow

# Identify each field in awilson's entry
# Field 1: username
# Field 2: hash (starts with $6$ for SHA-512)
# Field 3: last changed (epoch days)
# Field 4: minimum age
# Field 5: maximum age
# Field 6: warning
# Field 7: inactive
# Field 8: expiration
```

**Lab Question 3:** In Alice's shadow entry, field 3 shows the last changed date as epoch days. Calculate today's date in epoch days using:

```bash
echo $(($(date +%s) / 86400))
```

What value did you get? Does it match field 3 of Alice's shadow entry? (It should be 0 because we set `-d 0` to force expiration.)

---

## Task 5 — Modify User Accounts

### Step 5.1 — Add Alice to a New Group

The DevOps team has been given access to a new `docker` group. Add Alice to it.

```bash
# Check what groups Alice currently belongs to
id awilson
groups awilson

# Add her to docker group (create it first)
sudo groupadd docker
sudo usermod -aG docker awilson

# Verify she kept all previous groups
id awilson
```

**Lab Question 4:** What would have happened if you ran `sudo usermod -G docker awilson` (without `-a`)? Test it with a throwaway command to confirm your understanding.

### Step 5.2 — Change Bob's Shell

```bash
# View Bob's current shell
grep bmartin /etc/passwd

# Change to zsh (if installed) or bash
sudo usermod -s /bin/bash bmartin

# Verify
grep bmartin /etc/passwd
```

### Step 5.3 — Lock and Unlock an Account

Simulate the contractor being temporarily suspended.

```bash
# Lock the account
sudo usermod -L contractor1

# Check the shadow file — note the ! prepended to the hash
sudo grep contractor1 /etc/shadow

# Check status
sudo passwd -S contractor1

# Unlock the account
sudo usermod -U contractor1

# Verify unlock
sudo passwd -S contractor1
sudo grep contractor1 /etc/shadow
```

---

## Task 6 — Configure sudo Access

### Step 6.1 — Grant Alice sudo Access for Web Service Restart Only

Alice needs to restart the HTTP service for deployments but should not have full sudo access.

```bash
# Create a targeted sudoers rule
sudo visudo -f /etc/sudoers.d/ramrod_developers

# Add this content (type it in the editor):
# Cmnd_Alias WEBSERVICE = /bin/systemctl restart httpd, /bin/systemctl restart nginx, /bin/systemctl status httpd, /bin/systemctl status nginx
# awilson  ALL=(ALL)  NOPASSWD: WEBSERVICE
```

### Step 6.2 — Grant the DevOps Group Broader Access

```bash
sudo visudo -f /etc/sudoers.d/ramrod_devops

# Add this content:
# %devops  ALL=(ALL)  ALL
```

### Step 6.3 — Verify sudo Rules

```bash
# List allowed sudo commands for awilson
sudo -l -U awilson

# List allowed commands for the current user
sudo -l
```

### Step 6.4 — Test sudo Access (if you have a test user session)

```bash
# As awilson, these should work:
sudo systemctl status nginx

# These should be blocked:
sudo cat /etc/shadow      # Should fail — not in her alias
sudo useradd testuser     # Should fail
```

---

## Task 7 — Examine and Verify Everything

### Step 7.1 — Inventory All New Objects

```bash
# All users created in this lab
for user in awilson bmartin contractor1; do
  echo "=== $user ==="
  grep "^$user:" /etc/passwd
  id "$user"
  sudo chage -l "$user" | grep -E "Password expires|Last password change|Account expires"
  echo ""
done

# All groups created in this lab
for group in developers qa devops docker; do
  echo "=== $group ==="
  getent group "$group"
  echo ""
done
```

### Step 7.2 — Find All Files Owned by New Users

```bash
# Find files owned by awilson
find /home/awilson -user awilson -ls 2>/dev/null

# Find files outside home directory owned by new users
sudo find / -user awilson -not -path "/home/*" -ls 2>/dev/null | head -20
```

### Step 7.3 — Check /etc/skel Propagation

```bash
# Confirm skel files were copied to awilson's home
ls -la /home/awilson
ls -la /etc/skel
diff <(ls /etc/skel) <(ls -A /home/awilson)
```

---

## Task 8 — Cleanup (Optional — If Using a Shared VM)

If this is a shared or reused VM, clean up your lab work.

```bash
# Remove users and their home directories
sudo userdel -r awilson
sudo userdel -r bmartin
sudo userdel -r contractor1

# Remove groups (only if no users have these as primary)
sudo groupdel developers
sudo groupdel qa
sudo groupdel devops
sudo groupdel docker

# Remove sudoers drop-in files
sudo rm /etc/sudoers.d/ramrod_developers
sudo rm /etc/sudoers.d/ramrod_devops

# Verify cleanup
grep "awilson\|bmartin\|contractor1" /etc/passwd
```

---

## Lab Deliverables

Prepare a short lab report (can be notes or screenshots) covering:

1. The output of `id awilson` after all group additions in Task 5
2. The shadow file entries for all three users (Task 4.3)
3. The output of `sudo -l -U awilson` (Task 6.3)
4. Answers to Lab Questions 1 through 4
5. One command you found most useful and why

---

## Troubleshooting Guide

| Problem | Solution |
|---|---|
| `useradd: user 'X' already exists` | Use `userdel -r X` first, or choose a different username |
| `groupadd: group 'X' already exists` | The group is already there; skip creation |
| `sudo: /etc/sudoers.d/X: syntax error` | Run `sudo visudo -cf /etc/sudoers.d/X` to check syntax |
| `passwd: Authentication token manipulation error` | Try `sudo passwd username` as root |
| `userdel: user X is currently used by process Y` | Use `sudo pkill -u X` first, then retry |
| `chage: command not found` | Install with `sudo apt install login` or `sudo dnf install shadow-utils` |

# Lab: Module 04 — Text Processing and Editors

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Lab Overview

**Estimated Time:** 60–75 minutes

**Environment:** Linux VM (Ubuntu 22.04 LTS or equivalent); no root required for most tasks; sudo needed for Part 4

**Purpose:** Apply nano, vim, grep, sed, awk, and pipeline utilities to realistic sysadmin scenarios involving log analysis and configuration management.

---

## Objectives

By the end of this lab you will be able to:

- Open, edit, and save files using both nano and vim
- Use vim mode switching, navigation, and substitution commands
- Search files with grep using flags for case, line numbers, inversion, and recursion
- Transform text streams with sed substitution and deletion
- Extract and aggregate fields using awk
- Chain sort, uniq, cut, and wc into analysis pipelines

---

## Pre-Lab Setup

Run this block once to create all required sample files:

```bash
mkdir -p ~/lab04

# Web access log
cat > ~/lab04/access.log << 'EOF'
2024-03-15 08:00:01 192.168.1.10 GET /index.html 200 2048
2024-03-15 08:01:15 10.0.0.22 POST /login 401 512
2024-03-15 08:02:30 192.168.1.10 GET /dashboard 200 15360
2024-03-15 08:03:44 10.0.0.22 POST /login 401 512
2024-03-15 08:04:01 10.0.0.22 POST /login 401 512
2024-03-15 08:05:12 172.16.0.5 GET /report.csv 200 102400
2024-03-15 08:06:25 192.168.1.10 GET /admin 403 256
2024-03-15 08:07:10 192.168.1.15 GET /index.html 200 2048
2024-03-15 08:08:55 10.0.0.1 GET /status 200 128
2024-03-15 08:09:30 10.0.0.22 POST /login 401 512
EOF

# System users excerpt
cat > ~/lab04/users.csv << 'EOF'
username,uid,gid,shell,home
root,0,0,/bin/bash,/root
daemon,1,1,/usr/sbin/nologin,/usr/sbin
www-data,33,33,/usr/sbin/nologin,/var/www
jsmith,1001,1001,/bin/bash,/home/jsmith
mjones,1002,1002,/bin/bash,/home/mjones
svcacct,1003,1003,/usr/sbin/nologin,/var/svcacct
bjohnson,1004,1004,/bin/bash,/home/bjohnson
EOF

# Sample config file
cat > ~/lab04/app.conf << 'EOF'
# Application Configuration
# Last updated: 2024-03-01

hostname=old-server-01
domain=example.com
port=80
max_connections=100
log_level=INFO

# Database settings
db_host=db01.example.com
db_port=5432
db_name=appdb
db_user=appuser

# Security settings
ssl_enabled=false
allowed_ips=10.0.0.0/8
EOF
```

---

## Part 1 — nano (10 minutes)

### Task 1.1 — Basic Editing

1. Open the config file with nano:

```bash
nano ~/lab04/app.conf
```

2. Navigate to the `hostname=` line and change `old-server-01` to `web-prod-01`.

3. Navigate to the `port=80` line and change it to `port=443`.

4. Change `ssl_enabled=false` to `ssl_enabled=true`.

5. Save the file with **Control+O** and confirm the filename. Exit with **Control+X**.

6. Verify your changes:

```bash
grep -E "hostname|port|ssl" ~/lab04/app.conf
```

**Expected output:**

```
hostname=web-prod-01
port=443
ssl_enabled=true
```

### Task 1.2 — nano Search

1. Open the file again: `nano ~/lab04/app.conf`

2. Press **Control+W**, search for `db_host`, press Enter.

3. Confirm the cursor jumped to that line.

4. Exit without changes: **Control+X** (answer N if prompted).

**Checkpoint:** Describe in your own words what the caret symbol in nano's shortcut legend represents.

---

## Part 2 — vim (20 minutes)

### Task 2.1 — Mode Practice

1. Open a new file:

```bash
vim ~/lab04/vimtest.txt
```

2. You are in Normal mode. Press `i` to enter Insert mode. Type:

```
server_name=app01
environment=production
version=3.2.1
debug=false
```

3. Press **Escape** to return to Normal mode.

4. Save with `:w` and confirm.

### Task 2.2 — Navigation

1. In Normal mode, use `gg` to jump to line 1.

2. Press `j` three times to move to line 4 (`debug=false`).

3. Press `0` to move to the start of the line, then `$` to move to the end.

4. Press `G` to jump to the last line.

5. Type `:1` to jump back to line 1.

### Task 2.3 — Editing Commands

1. Move your cursor to the `version=3.2.1` line.

2. Press `dd` to delete the line.

3. Move to the `environment=production` line.

4. Press `yy` to yank it.

5. Press `p` to paste it below the current line.

6. Press `u` to undo the paste.

7. Press `:set number` to enable line numbers.

### Task 2.4 — Search and Replace

1. Press `/debug` and Enter to search for "debug".

2. Confirm the cursor jumps to the match.

3. In Command-line mode, run:

```vim
:%s/false/true/g
```

4. Verify the change, then run:

```vim
:%s/true/false/gc
```

Respond with `y` to confirm the first replacement, `n` to skip the second if there are two.

5. Save and quit: `:wq`

6. Verify:

```bash
cat ~/lab04/vimtest.txt
```

### Task 2.5 — vim on a Config File

1. Open the access log:

```bash
vim ~/lab04/access.log
```

2. Using `:set number`, enable line numbers.

3. Search for `401` — note which lines match.

4. Without saving, quit with `:q!`

**Checkpoint:** What is the difference between `:q` and `:q!`?

---

## Part 3 — grep (15 minutes)

Work with the access log throughout this section.

### Task 3.1 — Basic Searches

```bash
# Find all 401 responses
grep "401" ~/lab04/access.log

# Find all POST requests
grep "POST" ~/lab04/access.log

# Case-insensitive search for "get"
grep -i "get" ~/lab04/access.log
```

Record how many lines each command returns.

### Task 3.2 — Line Numbers and Inversion

```bash
# Show line numbers for 403 responses
grep -n "403" ~/lab04/access.log

# Show all lines that are NOT 200 responses
grep -v "200" ~/lab04/access.log
```

**Question:** The grep -v output shows 401 and 403 lines. Write a grep command that shows only lines that are neither 200 nor 401.

*Hint: pipe two grep -v commands together.*

### Task 3.3 — Count and Files

```bash
# Count how many 401 errors occurred
grep -c "401" ~/lab04/access.log

# Count successful requests
grep -c "200" ~/lab04/access.log
```

### Task 3.4 — Recursive and Fixed String

```bash
# Search all files in ~/lab04 for "ssl"
grep -r "ssl" ~/lab04/

# Use -l to show only filenames
grep -rl "ssl" ~/lab04/

# Fixed string: search for the IP with dots as literal characters
grep -F "192.168.1.10" ~/lab04/access.log
```

**Question:** Why might `grep "192.168.1.10"` match lines it should not? What does the dot mean in a regular expression?

### Task 3.5 — Context Flags

```bash
# Show 2 lines of context around a 403 response
grep -C 2 "403" ~/lab04/access.log
```

---

## Part 4 — sed (10 minutes)

### Task 4.1 — Substitution

```bash
# Replace "example.com" with "txwes.edu" in app.conf (output only, no file change)
sed 's/example.com/txwes.edu/g' ~/lab04/app.conf

# Verify the file was NOT changed
grep "example.com" ~/lab04/app.conf
```

### Task 4.2 — In-Place Edit

```bash
# Make a backup first
cp ~/lab04/app.conf ~/lab04/app.conf.bak

# Replace in-place
sed -i 's/example.com/txwes.edu/g' ~/lab04/app.conf

# Verify the change
grep "txwes\|example" ~/lab04/app.conf
```

### Task 4.3 — Deleting Lines

```bash
# View the config without comments or blank lines
sed '/^#/d; /^$/d' ~/lab04/app.conf
```

**Question:** What does `^#` match? What does `^$` match?

### Task 4.4 — Combining sed with grep

```bash
# Show active (non-comment) database settings
grep "^db_" ~/lab04/app.conf | sed 's/db_/database_/'
```

---

## Part 5 — awk and Pipelines (15 minutes)

### Task 5.1 — Field Extraction

```bash
# Print timestamp and IP from access log
awk '{ print $1, $2, $3 }' ~/lab04/access.log

# Print only HTTP method and status code
awk '{ print $4, $6 }' ~/lab04/access.log

# Print last field (bytes) only
awk '{ print $NF }' ~/lab04/access.log
```

### Task 5.2 — CSV with Custom Delimiter

```bash
# Extract username and shell from users.csv (skip header)
awk -F, 'NR > 1 { print $1, $5 }' ~/lab04/users.csv

# Print only users with /bin/bash shell
awk -F, '$4 == "/bin/bash" { print $1 }' ~/lab04/users.csv
```

### Task 5.3 — Aggregation

```bash
# Sum total bytes transferred
awk '{ total += $7 } END { print "Total bytes:", total }' ~/lab04/access.log

# Count requests per IP
awk '{ count[$3]++ } END { for (ip in count) print count[ip], ip }' ~/lab04/access.log
```

### Task 5.4 — The Full Analysis Pipeline

Build a pipeline that answers: "Which IP addresses made the most 401 requests?"

```bash
grep "401" ~/lab04/access.log \
  | awk '{ print $3 }' \
  | sort \
  | uniq -c \
  | sort -nr
```

Record the output. Which IP generated the most authentication failures?

### Task 5.5 — Additional Pipeline Work

```bash
# List all unique HTTP methods used, sorted
awk '{ print $4 }' ~/lab04/access.log | sort | uniq

# Count lines in access.log
wc -l ~/lab04/access.log

# Extract bytes column and find total and count
awk '{ print $7 }' ~/lab04/access.log | sort -n

# Show usernames from users.csv in uppercase
awk -F, 'NR > 1 { print $1 }' ~/lab04/users.csv | tr 'a-z' 'A-Z'
```

---

## Challenge Tasks (Optional)

### Challenge 1 — Log Report Script

Using only the tools from this module, generate a summary report of the access log that shows:

- Total request count
- Count of 200, 401, and 403 responses
- Top 3 IP addresses by request count
- Total bytes transferred

Write the pipeline commands (not a script) to produce each line of this report.

### Challenge 2 — Config Diff

Using sed, write a single command that:

- Removes all comment lines (lines starting with #)
- Removes all blank lines
- Replaces all remaining `=` signs with ` : ` (space colon space)

Apply it to app.conf and redirect the output to a new file `~/lab04/app_clean.conf`.

### Challenge 3 — vim Macro

In vim, record a macro on the `q` key that:

1. Moves to the end of the line (press `$`)
2. Appends a comment ` # updated` to the end of the line (press `a` then type ` # updated`, then Escape)
3. Moves down one line

Apply the macro to the first 3 non-comment lines in app.conf using `3@q`.

---

## Submission Requirements

Submit a text file named `lab04_answers.txt` containing:

1. Output of Task 3.2 challenge: the grep -v pipeline excluding both 200 and 401
2. Answer to Task 3.4 question about regex dots
3. Answer to Task 4.3 question about `^#` and `^$`
4. Output of Task 5.4 pipeline (top 401 offenders)
5. Answer to the checkpoint after Task 2.4
6. Challenge 1 commands (if completed)

---

## Grading Rubric

| Section | Points |
|---|---|
| Part 1 — nano editing and verification | 10 |
| Part 2 — vim mode practice and substitution | 20 |
| Part 3 — grep with all flag types | 20 |
| Part 4 — sed substitution and deletion | 15 |
| Part 5 — awk and pipeline | 25 |
| Written answers to checkpoint questions | 10 |
| **Total** | **100** |

Challenge tasks are extra credit (up to 15 points).

---

*End of Module 04 Lab*

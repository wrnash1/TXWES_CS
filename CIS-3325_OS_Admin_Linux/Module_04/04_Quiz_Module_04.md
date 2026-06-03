# Quiz: Module 04 — Text Processing and Editors

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A Linux administrator opens a file with vim and wants to begin typing text. The cursor is positioned correctly but every key press moves the cursor instead of inserting characters. What must the administrator do first?

A. Press Escape to enter Insert mode

B. Press `i` to enter Insert mode

C. Type `:insert` in Command-line mode

D. Press `v` to enter Visual mode

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect because pressing Escape moves FROM Insert mode TO Normal mode, not into Insert mode. This is a common reversal error.
- **B** is correct. Pressing `i` enters Insert mode, allowing text to be typed before the cursor position.
- **C** is incorrect. There is no `:insert` command in vim. Commands like `:w` and `:q` are used in Command-line mode, but inserting text is done via mode keys, not colon commands.
- **D** is incorrect. Visual mode (`v`) is used for selecting text for operations like copy/delete, not for typing new text.

---

### Question 2

An administrator edits `/etc/ssh/sshd_config` in vim and realizes they made several errors. They want to exit immediately without saving any changes. Which command accomplishes this?

A. `:wq`

B. `:q`

C. `:q!`

D. `:x`

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. `:wq` saves the file and then quits — the opposite of the desired action, as it would preserve the erroneous edits.
- **B** is incorrect. `:q` quits only when there are no unsaved changes. Because changes exist, vim will refuse and display `E37: No write since last change`. It does not discard changes silently.
- **C** is correct. `:q!` forces quit, discarding all unsaved changes. The `!` overrides vim's protection against losing work.
- **D** is incorrect. `:x` is equivalent to `:wq` — it saves if changes exist, then quits. This would preserve the errors.

---

### Question 3

An administrator runs the following command:

```bash
grep -v "200" /var/log/access.log
```

What does this command display?

A. Only lines that contain exactly the string "200"

B. All lines except those containing "200"

C. Line numbers for every occurrence of "200"

D. A count of lines that do not contain "200"

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. That describes `grep "200"` without the `-v` flag. `-v` inverts the match behavior.
- **B** is correct. The `-v` flag inverts grep's output, printing all lines that do NOT match the pattern. It is commonly used to filter out noise from log files.
- **C** is incorrect. Line numbers are shown with the `-n` flag, not `-v`.
- **D** is incorrect. A count is produced with the `-c` flag. `-v` combined with `-c` would count non-matching lines, but this question asks about `-v` alone.

---

### Question 4

An administrator needs to replace every occurrence of the word "staging" with "production" in a 5,000-line configuration file using vim. Which command performs this operation on the entire file?

A. `:%s/staging/production/`

B. `:%s/staging/production/g`

C. `:s/staging/production/g`

D. `/staging:s//production/`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Without the `g` flag, the substitution replaces only the first occurrence of "staging" on each line. A line containing "staging" twice would only have the first replaced.
- **B** is correct. `:%s/staging/production/g` — the `%` addresses all lines, `s` performs substitution, and `g` replaces all occurrences on each line.
- **C** is incorrect. `:s/staging/production/g` operates only on the current line, not the entire file. The `%` prefix is required to address all lines.
- **D** is incorrect. This is not valid vim syntax. The search and substitute commands are separate operations.

---

### Question 5

An administrator uses the following sed command:

```bash
sed '/^#/d' /etc/ntp.conf
```

What is the result?

A. Lines beginning with `#` are replaced with empty lines

B. Lines beginning with `#` are printed and all other lines are deleted

C. Lines beginning with `#` are deleted from the output

D. The file `/etc/ntp.conf` is permanently modified to remove comment lines

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. The `d` command in sed deletes the entire line from the output stream. It does not replace the line with a blank line.
- **B** is incorrect. This describes the opposite behavior. `d` deletes matching lines; non-matching lines are passed through normally.
- **C** is correct. The `d` command deletes lines that match the address pattern from sed's output. `^#` matches lines starting with `#`. The original file is unchanged.
- **D** is incorrect. Without the `-i` flag, sed writes to standard output and does not modify the source file. This is a critical distinction that prevents accidental file corruption.

---

### Question 6

An administrator wants to extract the first field from a colon-delimited file. Which awk command is correct?

A. `awk '{ print $1 }' file`

B. `awk -F: '{ print $1 }' file`

C. `awk -d: '{ print $1 }' file`

D. `awk '{ print FS$1 }' file`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Without specifying a field separator, awk defaults to whitespace. If the file uses colons as delimiters, `$1` would contain the entire line content up to the first whitespace, not the first colon-delimited field.
- **B** is correct. `-F:` sets the field separator to a colon. $1 then refers to the first colon-delimited field.
- **C** is incorrect. `-d` is a cut option, not an awk option. awk uses `-F` for the field separator.
- **D** is incorrect. `FS` is the built-in variable holding the field separator character, not a flag to prepend to field references. This syntax is invalid.

---

### Question 7

An administrator runs this pipeline:

```bash
awk '{ print $1 }' server.log | sort | uniq -c | sort -nr | head -5
```

What does this pipeline produce?

A. The 5 most recent unique entries in the first field

B. The 5 most frequently occurring values in the first field, in descending order

C. The 5 alphabetically first unique values in the first field

D. A count of all lines in server.log

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. The pipeline has no time-awareness. `head -5` after `sort -nr` gives the top 5 by count, not by recency. Recency would require a different approach such as `tail`.
- **B** is correct. awk extracts field 1. sort arranges values so duplicates are adjacent. uniq -c prepends a count to each unique value. sort -nr sorts by that count numerically in descending order. head -5 shows the top 5.
- **C** is incorrect. An alphabetical sort would be produced by `sort` without `-n` and without the final `sort -nr`. Adding `sort -nr` converts it to a frequency sort.
- **D** is incorrect. `wc -l` counts lines. This pipeline counts distinct values of the first field by frequency.

---

### Question 8

A sysadmin needs to search all `.conf` files under `/etc` for the string `Listen 443`, ignoring case. Which command is correct?

A. `grep "Listen 443" /etc/*.conf`

B. `grep -i -r "Listen 443" /etc/`

C. `grep -l "Listen 443" /etc/`

D. `grep -F -v "listen 443" /etc/`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `/etc/*.conf` only matches `.conf` files directly under `/etc` and does not recurse into subdirectories like `/etc/apache2/`. Many config files live in subdirectories.
- **B** is correct. `-i` enables case-insensitive matching (handles "Listen", "listen", "LISTEN"). `-r` recursively searches the entire `/etc/` directory tree.
- **C** is incorrect. `-l` lists only filenames and does not perform case-insensitive matching (no `-i` flag). It also does not recurse without `-r`.
- **D** is incorrect. `-v` inverts the match — this would show all lines that do NOT contain "listen 443". `-F` treats it as a fixed string, which prevents case-insensitive matching with `-i` and is paired with the wrong inversion flag.

---

### Question 9

An administrator needs to display the total number of lines in a log file. Which command provides this information?

A. `wc -w logfile.txt`

B. `wc -c logfile.txt`

C. `wc -l logfile.txt`

D. `wc -n logfile.txt`

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. `-w` counts words (whitespace-separated tokens), not lines.
- **B** is incorrect. `-c` counts bytes (characters), which equals the file size in bytes, not the number of lines.
- **C** is correct. `-l` counts newline characters, which equals the number of lines.
- **D** is incorrect. `-n` is not a valid wc option. Line numbers in grep output use `-n`, but `wc` does not have a `-n` flag.

---

### Question 10

An administrator runs the following command:

```bash
sort /tmp/ips.txt | uniq -d
```

What does the output represent?

A. All unique IP addresses with duplicates removed

B. Only the IP addresses that appear more than once

C. The count of each IP address sorted numerically

D. The IP addresses sorted and deduplicated

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. That describes `sort -u` or `sort | uniq` without flags. `-d` specifically selects only the duplicated lines.
- **B** is correct. `uniq -d` prints only lines that appear more than once in the (sorted) input. This is useful for finding repeated entries such as duplicate IP addresses or repeated error messages.
- **C** is incorrect. Counts are produced by `uniq -c`. Adding `sort -n` would then sort numerically, but the command shown uses `uniq -d` with no sort flags.
- **D** is incorrect. That describes `sort | uniq` without any flags, or `sort -u`. The `-d` flag changes the behavior to show only duplicates rather than eliminating them.

---

## Answer Key

| Question | Answer |
|---|---|
| 1 | B |
| 2 | C |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | C |
| 10 | B |

---

*End of Module 04 Quiz*

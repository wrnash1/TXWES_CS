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

### Question 11 (5 points)

An administrator runs `cut -d: -f1,3 /etc/passwd`. What does this command output?

A. The first and third lines of `/etc/passwd`.
B. The first and third characters of each line.
C. The first and third colon-delimited fields from each line (username and UID).
D. Lines from `/etc/passwd` that contain exactly three colon-delimited fields.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Selecting lines by number would use `sed -n '1p;3p'` or `head`/`tail`. `cut` operates on fields within each line.
- **B** is incorrect. Character extraction uses `-c` with `cut`, not `-f`. For example, `cut -c1-3` would extract the first 3 characters.
- **C** is correct. `-d:` sets the field delimiter to a colon; `-f1,3` selects the first and third fields. In `/etc/passwd`, field 1 is the username and field 3 is the UID.
- **D** is incorrect. `cut` always processes every line — it does not filter lines based on field count.

---

### Question 12 (5 points)

Which of the following sed commands modifies a file in place, replacing "localhost" with "127.0.0.1" throughout?

A. `sed 's/localhost/127.0.0.1/g' config.txt > config.txt`
B. `sed -n 's/localhost/127.0.0.1/g' config.txt`
C. `sed -i 's/localhost/127.0.0.1/g' config.txt`
D. `sed 's/localhost/127.0.0.1/' config.txt | tee config.txt`

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect and destructive. Redirecting to the same file (`> config.txt`) truncates the file before sed reads it, resulting in an empty file. Never redirect a command's output to the same file it reads.
- **B** is incorrect. `-n` suppresses default output (print only when explicitly requested with `p`). Without `-i`, no in-place modification occurs. The file would be unchanged.
- **C** is correct. The `-i` flag tells sed to edit the file in place. Combined with the global `g` flag, every occurrence of "localhost" is replaced throughout the file.
- **D** is incorrect. `tee config.txt` would also cause a conflict — the file would be truncated before sed finishes reading it, similar to the `>` redirect problem.

---

### Question 13 (5 points)

An administrator runs `sort -k2 -n employees.txt`. What does the `-k2` option specify?

A. Keep only the first 2 lines of the file.
B. Sort using the second field as the sort key.
C. Skip the first 2 header lines before sorting.
D. Use 2 spaces as the field separator.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Limiting output lines uses `head -2`. The `-k` option in `sort` specifies the key field for sorting.
- **B** is correct. `-k2` tells `sort` to use the second whitespace-delimited field as the sort key. Combined with `-n`, the sort is numeric on that field.
- **C** is incorrect. There is no skip-header option in `sort`. You would need to pipe through `tail -n +2` to skip a header line before sorting.
- **D** is incorrect. The field separator for `sort` is set with `-t`. For example, `sort -t: -k3 -n` would sort `/etc/passwd` numerically by the third colon-delimited field.

---

### Question 14 (5 points)

A sysadmin runs `grep -c "ERROR" /var/log/app.log`. The output is `47`. What does this mean?

A. The file contains 47 characters matching "ERROR".
B. 47 lines in the file contain the string "ERROR".
C. The string "ERROR" appears exactly 47 times across all lines.
D. There are 47 files in `/var/log` containing "ERROR".

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `-c` counts lines, not characters. Character counting uses `wc -c` or `grep -o "ERROR" | wc -l`.
- **B** is correct. `grep -c` reports the count of matching lines (one count per file). A line that contains "ERROR" three times is still counted as one matching line.
- **C** is incorrect. If a single line contains "ERROR" twice, `grep -c` still counts it as one line. The count of total occurrences (not lines) would require `grep -o "ERROR" | wc -l`.
- **D** is incorrect. When given a single file as argument, `grep -c` reports the count for that file only — not the number of files containing the string. That would require `grep -rl "ERROR" /var/log/ | wc -l`.

---

### Question 15 (5 points)

In vim, what is the effect of pressing `o` while in Normal mode?

A. Opens a file browser to select another file.
B. Moves the cursor to the end of the current line.
C. Creates a new empty line below the current line and enters Insert mode.
D. Overwrites the current line with the clipboard contents.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Opening a file browser is not a default vim Normal mode action. You would use `:e filename` or a plugin like NERDTree.
- **B** is incorrect. Moving to the end of the current line is done with `$` in Normal mode.
- **C** is correct. Pressing `o` opens a new line below the cursor and automatically places vim in Insert mode. Its counterpart `O` opens a new line above the current line.
- **D** is incorrect. There is no "overwrite current line with clipboard" single-keystroke command in standard vim. Pasting the yank register uses `p` (below) or `P` (above).

---

### Question 16 (5 points)

An administrator wants to display only the lines in `/etc/passwd` where the user's shell is `/bin/bash`. Which awk command accomplishes this?

A. `awk '/bash/ { print }' /etc/passwd`
B. `awk -F: '$7 == "/bin/bash" { print $1 }' /etc/passwd`
C. `awk -F: '{ print $7 }' /etc/passwd | grep bash`
D. `awk '{ print $7 }' /etc/passwd`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is partially useful but imprecise. `/bash/` would also match lines where "bash" appears elsewhere in the entry, such as in a comment field or home path. An exact field comparison is more reliable.
- **B** is correct. `-F:` sets the delimiter to a colon; `$7 == "/bin/bash"` performs an exact match on the seventh field (the shell). This is precise and avoids false positives.
- **C** would work to list shells but only outputs field 7 after filtering — you would not see the usernames. The question asks for lines where the condition is met, implying more context is needed.
- **D** is incorrect. Without `-F:`, awk uses whitespace as the delimiter. In `/etc/passwd`, all fields are colon-separated with no internal spaces, so `$7` would be empty for most lines.

---

### Question 17 (5 points)

A sysadmin runs `tr 'a-z' 'A-Z'` on the text "hello world". What is the output?

A. `HELLO WORLD`
B. `hello world` (unchanged)
C. `dlrow olleh`
D. `hELLO wORLD`

**Correct Answer: A**

**Distractor Analysis:**

- **A** is correct. `tr 'a-z' 'A-Z'` translates every lowercase letter to its uppercase equivalent. All alphabetic characters become uppercase; spaces and other characters are left unchanged.
- **B** is incorrect. `tr` with valid character ranges performs the translation. The input would be modified.
- **C** is incorrect. Reversing a string is not a `tr` operation. String reversal is done with `rev` or `tac`.
- **D** is incorrect. `tr 'a-z' 'A-Z'` applies uniformly to all lowercase letters including the `h`. There is no behavior that would skip the first character.

---

### Question 18 (5 points)

An administrator uses vim to search for the word "timeout" in a configuration file by pressing `/timeout` and Enter. After finding the first match, how do they jump to the next occurrence?

A. Press `/` again and re-type `timeout`.
B. Press `n`.
C. Press `Enter`.
D. Press `Ctrl+N`.

**Correct Answer: B**

**Distractor Analysis:**

- **A** works but is inefficient. Retyping the search string repeatedly is not the intended workflow. The `n` key exists specifically to repeat the last search.
- **B** is correct. After a successful search in vim, pressing `n` jumps to the next match in the same direction. Pressing `N` jumps to the previous match.
- **C** is incorrect. In Normal mode, pressing `Enter` moves the cursor to the beginning of the next line. It does not repeat a search.
- **D** is incorrect. `Ctrl+N` in vim's Insert mode triggers word completion, not search navigation. In Normal mode, it moves the cursor down one line.

---

### Question 19 (5 points)

What does the `uniq` command require about its input in order to correctly identify and remove duplicate lines?

A. The input must be sorted so that duplicate lines are adjacent.
B. The input must be piped from `find`.
C. The input must contain only numeric data.
D. The input must be in CSV format with headers.

**Correct Answer: A**

**Distractor Analysis:**

- **A** is correct. `uniq` only detects duplicates when they are consecutive (adjacent). If a file contains "apple", "banana", "apple" in that order, `uniq` would output all three lines since the two "apple" lines are not adjacent. Sorting the input first ensures all identical lines are grouped together.
- **B** is incorrect. `uniq` can receive input from any command or file. It has no dependency on `find`.
- **C** is incorrect. `uniq` works on any text data — strings, mixed content, log lines. Numeric-only input is not required.
- **D** is incorrect. `uniq` has no awareness of CSV format. It operates on raw lines regardless of content structure.

---

### Question 20 (5 points)

An administrator runs this command: `grep -E "^(ERROR|WARN)" /var/log/app.log`. What does the `-E` flag enable?

A. Case-insensitive matching across the entire line.
B. Extended regular expression syntax, allowing `|` (alternation) and grouping with `()`.
C. Recursive directory searching.
D. Exact string matching without regex interpretation.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Case-insensitive matching is enabled by `-i`. The `-E` flag has nothing to do with case sensitivity.
- **B** is correct. `-E` (Extended regex) enables alternation with `|`, grouping with `()`, `+` (one or more), `?` (zero or one), and `{n,m}` repetition. Without `-E`, the parentheses and pipe would be treated as literal characters requiring backslash escaping.
- **C** is incorrect. Recursive directory searching is enabled by `-r`. The `-E` flag is about regex syntax, not search scope.
- **D** is incorrect. Fixed-string matching (no regex) is enabled by `-F`. `-E` does the opposite — it enables more powerful regex features, not less.

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
| 11 | C |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | C |
| 16 | B |
| 17 | A |
| 18 | B |
| 19 | A |
| 20 | B |

---

*End of Module 04 Quiz*

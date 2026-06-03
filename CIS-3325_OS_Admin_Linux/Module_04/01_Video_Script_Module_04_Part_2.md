# Video Script: Module 04 — Text Processing and Editors (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Production Notes

- **Screen recording**: Terminal emulator (dark theme, 18pt font)
- **Demonstrations**: Build a realistic log-parsing scenario across all tools
- **Slide overlays**: Syntax templates displayed as callout boxes
- **Pacing**: Explain output before moving to next command

---

## SEGMENT 1 — Opening and Recap (0:00–1:00)

### Narration

Welcome back to Module 04, Part 2. In Part 1 you learned to edit files with nano and vim and to search them with grep. Now we add the heavy-lifting tools: sed, awk, and a collection of pipeline utilities — sort, uniq, cut, wc, tr, and xargs. We finish by building a realistic log-parsing pipeline that ties everything together.

Let's set up a realistic data file to use throughout this video.

### On-Screen Demo

```bash
cat > /tmp/weblog.txt << 'EOF'
2024-03-15 08:12:01 192.168.1.10 GET /index.html 200 1234
2024-03-15 08:12:45 10.0.0.1 POST /login 401 512
2024-03-15 08:13:10 192.168.1.15 GET /dashboard 200 8901
2024-03-15 08:14:00 10.0.0.1 POST /login 401 512
2024-03-15 08:14:05 10.0.0.1 POST /login 401 512
2024-03-15 08:15:22 192.168.1.10 GET /admin 403 256
2024-03-15 08:16:01 172.16.0.5 GET /index.html 200 1234
2024-03-15 08:17:30 192.168.1.15 GET /report.csv 200 45678
EOF
```

---

## SEGMENT 2 — sed: The Stream Editor (1:00–5:30)

### Narration

sed stands for Stream Editor. It reads input line by line, applies instructions, and writes the result to standard output. It is non-interactive — you write the instruction in the command, not interactively. That makes it perfect for scripting.

The most-used sed operation is substitution:

```
sed 's/pattern/replacement/flags' file
```

### On-Screen Demo

```bash
sed 's/GET/HTTP-GET/' /tmp/weblog.txt
```

### Narration

By default, sed only replaces the first occurrence on each line. Add the `g` flag to replace all occurrences on every line:

### On-Screen Demo

```bash
sed 's/192.168/10.10/g' /tmp/weblog.txt
```

### Narration

An important point: by default, sed outputs to the terminal. It does not change your file. To modify the file in place, use the **-i** flag:

### On-Screen Demo

```bash
# Make a copy first so we don't destroy our demo file
cp /tmp/weblog.txt /tmp/weblog_copy.txt
sed -i 's/GET/HTTP-GET/g' /tmp/weblog_copy.txt
cat /tmp/weblog_copy.txt
```

### Narration

On some systems — notably macOS and older BSD variants — `-i` requires an extension argument like `-i.bak` which creates a backup. On GNU/Linux sed, `-i` works without the extension. For portable scripts, use `-i.bak`.

Next: deleting lines. The `d` command deletes every line matching a pattern:

### On-Screen Demo

```bash
sed '/200/d' /tmp/weblog.txt
```

### Narration

That outputs only the lines that do not contain "200" — the errors and other codes. We essentially inverted grep's behavior.

You can also address lines by number. Delete line 1:

### On-Screen Demo

```bash
sed '1d' /tmp/weblog.txt
```

### Narration

Or delete a range:

### On-Screen Demo

```bash
sed '2,4d' /tmp/weblog.txt
```

### Narration

A common sysadmin use case: strip comments and blank lines from a config file to see only the active settings:

### On-Screen Demo

```bash
sed '/^#/d; /^$/d' /etc/ssh/sshd_config | head -20
```

### Narration

Two instructions separated by a semicolon. The first deletes lines starting with `#`. The second deletes blank lines. The result is a clean view of the active configuration.

---

## SEGMENT 3 — awk: Field-Based Processing (5:30–9:30)

### Narration

awk is a full programming language built around the concept that every line of input is a record divided into fields. By default, fields are separated by whitespace and numbered $1, $2, $3, and so on. $NF always refers to the last field, regardless of how many fields exist.

The basic structure is:

```
awk 'pattern { action }' file
```

Let's print only the IP address (field 3) and the HTTP status code (field 6) from our log:

### On-Screen Demo

```bash
awk '{ print $3, $6 }' /tmp/weblog.txt
```

### Narration

Print with a custom separator — a tab:

### On-Screen Demo

```bash
awk '{ print $3 "\t" $6 }' /tmp/weblog.txt
```

### Narration

Add a condition: only print lines where the status code (field 6) is not 200:

### On-Screen Demo

```bash
awk '$6 != "200" { print $3, $6 }' /tmp/weblog.txt
```

### Narration

Change the field separator with **-F**. If your file uses colons — like /etc/passwd — use `-F:`:

### On-Screen Demo

```bash
awk -F: '{ print $1, $7 }' /etc/passwd | head -10
```

### Narration

That prints every username and their login shell.

awk also supports BEGIN and END blocks. BEGIN runs before any input is processed. END runs after all input is processed. This lets you print headers and totals:

### On-Screen Demo

```bash
awk 'BEGIN { print "IP\t\tStatus" } { print $3, $6 } END { print "---\nTotal lines: " NR }' /tmp/weblog.txt
```

### Narration

NR is a built-in awk variable meaning "number of records" — it counts the lines processed.

A practical example: sum the bytes transferred (field 7) across all requests:

### On-Screen Demo

```bash
awk '{ total += $7 } END { print "Total bytes: " total }' /tmp/weblog.txt
```

### Narration

This is the kind of quick report you would run from cron or a monitoring script to track bandwidth usage without a dedicated tool.

---

## SEGMENT 4 — Pipeline Utilities (9:30–13:00)

### Narration

Now let's cover the supporting cast — tools that you combine in pipelines.

### sort

sort arranges lines alphabetically by default. The important flags:

- `-n` sorts numerically instead of lexicographically
- `-r` reverses the order
- `-k` sorts by a specific field
- `-u` sorts and removes duplicates

### On-Screen Demo

```bash
# Sort IPs from the log
awk '{ print $3 }' /tmp/weblog.txt | sort

# Sort HTTP status codes numerically
awk '{ print $6 }' /tmp/weblog.txt | sort -n

# Reverse sort
awk '{ print $7 }' /tmp/weblog.txt | sort -n -r
```

### uniq

uniq removes or counts adjacent duplicate lines. It only works on sorted input — which is why sort and uniq are almost always paired.

### On-Screen Demo

```bash
# Count occurrences of each IP
awk '{ print $3 }' /tmp/weblog.txt | sort | uniq -c | sort -nr
```

### Narration

The `-c` flag prefixes each unique line with a count. Combining `sort | uniq -c | sort -nr` gives you a frequency table from highest to lowest — an essential pattern for analyzing logs.

### cut

cut extracts specific fields from delimited text. Use `-d` for delimiter and `-f` for field number.

### On-Screen Demo

```bash
# Extract usernames from /etc/passwd
cut -d: -f1 /etc/passwd

# Extract first and last field
cut -d: -f1,7 /etc/passwd | head -5
```

### wc

wc counts words, lines, or characters. Most commonly used with `-l` for line count:

### On-Screen Demo

```bash
wc -l /tmp/weblog.txt
wc -w /tmp/weblog.txt
grep "401" /tmp/weblog.txt | wc -l
```

### Narration

That last command counts how many 401 errors appear in the log.

### tr

tr translates or deletes characters. Useful for case conversion and stripping unwanted characters:

### On-Screen Demo

```bash
echo "Hello World" | tr 'a-z' 'A-Z'
echo "line1:line2:line3" | tr ':' '\n'
```

### xargs

xargs takes standard input and passes it as arguments to a command:

### On-Screen Demo

```bash
# Find all .log files and count their lines
find /var/log -name "*.log" 2>/dev/null | head -5 | xargs wc -l
```

---

## SEGMENT 5 — Building a Pipeline (13:00–15:00)

### Narration

Let's tie everything together with a realistic scenario. Your manager asks: "Which IP addresses are generating the most authentication failures, and how many failures per IP?"

### On-Screen Demo

```bash
grep "401" /tmp/weblog.txt \
  | awk '{ print $3 }' \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -10
```

### Narration

Walk through the pipeline:

1. `grep "401"` — filter to only authentication failure lines
2. `awk '{ print $3 }'` — extract the IP address field
3. `sort` — arrange IPs so duplicates are adjacent
4. `uniq -c` — count consecutive duplicates
5. `sort -nr` — sort numerically in descending order
6. `head -10` — show only the top ten offenders

This is the pattern you will use repeatedly in incident response, capacity planning, and daily operations.

One more practical pipeline: count the total bytes served to each unique IP:

### On-Screen Demo

```bash
awk '{ bytes[$3] += $7 } END { for (ip in bytes) print bytes[ip], ip }' /tmp/weblog.txt \
  | sort -nr
```

### Narration

Here awk maintains an associative array where the key is the IP and the value accumulates bytes. The END block prints all entries. sort orders by bytes descending.

These pipelines require no external tools beyond the standard Linux utilities. They run on every Linux system without installing anything. For a sysadmin, this skill set is the difference between spending 30 minutes manually sifting a log file and getting the answer in 5 seconds.

That concludes Module 04. In Module 05 we shift to process management — how to observe, control, and schedule the processes running on your system. See you there.

---

## Summary Slide

### Part 2 Key Commands

- `sed 's/old/new/g' file` — substitute all occurrences; add `-i` to edit in place
- `sed '/pattern/d' file` — delete lines matching pattern
- `awk '{ print $1, $NF }' file` — print first and last fields
- `awk -F: '{ print $1 }' /etc/passwd` — colon-delimited fields
- `awk 'BEGIN{} { action } END{}' file` — header/total blocks
- `sort -n -r -k2 -u` — numeric, reverse, by field 2, unique
- `uniq -c` — count occurrences; always sort input first
- `cut -d: -f1` — extract field from delimited input
- `wc -l` — count lines
- `tr 'a-z' 'A-Z'` — character translation
- `xargs` — convert stdin to command arguments
- Pipeline pattern: `grep | awk | sort | uniq -c | sort -nr | head`

---

*End of Module 04 Part 2 Script*

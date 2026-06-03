# Video Script: Module 04 — Text Processing and Editors (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Production Notes

- **Screen recording**: Terminal emulator (dark theme, 18pt font)
- **Demonstrations**: All commands typed live; errors shown and corrected intentionally
- **Slide overlays**: Key shortcuts displayed as callout boxes during demos
- **Pacing**: Pause 2 seconds after each command output before continuing narration

---

## SEGMENT 1 — Opening and Context (0:00–1:30)

### Narration

Welcome back to CIS-3325, OS Administration Linux. I'm Professor Nash, and this is Module 04, Part 1: Text Editors and grep.

Before we dive in, let's anchor this module in your day-to-day work as a sysadmin. Nearly everything you do on a Linux system involves text. Configuration files, log files, scripts, cron jobs, user lists — all of it is plain text. If you cannot confidently open, edit, and search text files from the command line, you will be blocked at every turn.

In Part 1 today we cover two major skills. First, the two editors you will actually use on the job: nano and vim. Second, grep — the tool for searching text. In Part 2 we add sed, awk, and a set of pipeline utilities that let you build one-liners powerful enough to replace entire scripts.

Let's also note the CompTIA Linux+ alignment. Objective 1.3 covers file manipulation, and 2.1 touches on system service configuration — both of which require editing files. Every command we demonstrate today has appeared on the Linux+ exam.

---

## SEGMENT 2 — nano: The Approachable Editor (1:30–5:00)

### Narration

We start with nano because it is the safest choice when you just need to get something done without memorizing a command language. Nano is installed by default on Debian, Ubuntu, and most RHEL derivatives.

Let's open a file.

### On-Screen Demo

```bash
nano /tmp/demo.txt
```

### Narration

The moment nano opens, you can see the control legend at the bottom of the screen. Those caret symbols — `^` — mean the Control key. So `^O` means Control+O.

Let me type some content.

### On-Screen Demo

*Type inside nano:*

```
This is line one.
This is line two.
Configuration files are plain text.
```

### Narration

Now let's walk through the shortcuts you must know.

To write — that is, save — the file: **Control+O**. Nano will prompt you to confirm the filename. Press Enter to accept.

To exit: **Control+X**. If you have unsaved changes, nano will ask if you want to save them first.

To cut a whole line: **Control+K**. The line disappears into a cut buffer.

To paste what you cut: **Control+U** — think "uncut."

To search: **Control+W**, then type your search string and press Enter. Press **Control+W** again to find the next match.

### On-Screen Demo

*Demonstrate Control+W search for "two"*

### Narration

One practical feature worth knowing: `nano -l` opens the file with line numbers displayed. That is useful when you are debugging a script and an error message references a line number.

### On-Screen Demo

```bash
nano -l /tmp/demo.txt
```

### Narration

When should you use nano? Use it when you are working on a simple config file, you are helping a user remotely and they have never used vim, or you are in a restricted environment where you want to minimize mistakes. Nano does not have modes — what you type appears in the document immediately.

---

## SEGMENT 3 — vim: The Powerful Editor (5:00–11:00)

### Narration

Now we talk about vim. Vim has a reputation for being intimidating, and I will not pretend that reputation is unearned — there is a reason "how do I exit vim" is one of the most searched programming questions on the internet. But once you understand the modal design, vim becomes one of the fastest editing tools available. And on production servers, vim is almost always present when nano is not.

The single most important concept in vim is this: **vim has modes**. When vim opens, you are in Normal mode. Normal mode is for navigation and commands — keypresses are commands, not text input. Insert mode is where you actually type text. Command-line mode is where you run operations like save and quit.

Let's open a file.

### On-Screen Demo

```bash
vim /tmp/vimtest.txt
```

### Narration

We are now in Normal mode. You can tell because there is no `-- INSERT --` indicator at the bottom. If I press a letter like `j`, I move down — I do not type the letter `j` into the file.

### Slide Overlay: Normal Mode Navigation

```
h — left
l — right
j — down
k — up
```

### Narration

The hjkl navigation comes from the original vi editor running on terminals without arrow keys. The arrow keys work in modern vim too, but hjkl lets your fingers stay on the home row.

To enter Insert mode, press **i**. You will see `-- INSERT --` appear at the bottom. Now keystrokes type text.

### On-Screen Demo

*Press i, type:*

```
hostname=web01
domain=txwes.edu
port=8080
```

### Narration

Press **Escape** to return to Normal mode. Always press Escape before issuing a command. This is the habit that will save you from most vim confusion.

Now let's save. In Normal mode, type **:w** and press Enter. The colon puts you in Command-line mode — you can see the colon appear at the bottom of the screen.

### On-Screen Demo

*Type :w, press Enter*

### Narration

To quit: **:q**. To save and quit in one step: **:wq**. To quit without saving — discard all changes — use **:q!** The exclamation mark forces the action.

### On-Screen Demo

*Demonstrate :wq*

### Narration

Now let's talk about editing commands in Normal mode. These are what make vim fast.

**dd** deletes the entire current line and places it in the buffer.

**yy** yanks — copies — the current line.

**p** pastes the buffer contents after the current line.

**u** undoes the last action. You can press u repeatedly to undo multiple steps.

**Control+R** redoes.

### On-Screen Demo

```bash
vim /tmp/vimtest.txt
```

*Navigate to "port=8080" line, press dd to delete, then p to paste below another line*

### Narration

Searching in vim: in Normal mode, press **/**, type your search term, and press Enter. Press **n** to jump to the next match, **N** for the previous match.

### On-Screen Demo

*Type /domain, press Enter, press n*

### Narration

The most powerful Normal mode command for sysadmins is the global substitution. In Command-line mode:

```
:%s/old/new/g
```

The percent sign means "every line in the file." The `s` means substitute. The `g` flag means every occurrence on each line, not just the first.

### On-Screen Demo

```vim
:%s/txwes/texaswesleyan/g
```

### Narration

You can add a `c` flag — `:%s/old/new/gc` — to confirm each substitution individually. Vim will prompt you with `y/n/a/q` for each match.

Let me show you one more thing before we leave vim. When you open vim with two filenames, you can split the window. But for now, the one last command to know cold is **:set number** — it turns on line numbers, which is invaluable when an error message gives you a line reference.

### On-Screen Demo

```vim
:set number
```

---

## SEGMENT 4 — When to Use Nano vs. Vim (11:00–12:00)

### Narration

Here is the practical decision framework.

Use **nano** when you are new to the environment, the edit is small and quick, you are working interactively with a user who is not technical, or you are documenting steps for others to follow.

Use **vim** when you are on a minimal server that only has vi/vim installed, you are doing repeated find-and-replace across a file, you need macros or complex multi-line edits, or speed matters because you are editing across many lines.

In practice, competent sysadmins know both. The Linux+ exam tests vim specifically — you should know the mode names, the key commands, and what :wq versus :q! do.

---

## SEGMENT 5 — grep: Searching Text (12:00–15:00)

### Narration

The last topic for Part 1 is grep — the Global Regular Expression Print utility. grep searches files or standard input for lines matching a pattern and prints those lines.

The basic syntax is:

```
grep [options] pattern [file...]
```

Let's create a sample log file and work with it.

### On-Screen Demo

```bash
cat > /tmp/access.log << 'EOF'
192.168.1.10 GET /index.html 200
192.168.1.15 GET /login.html 200
10.0.0.1 POST /login.html 401
10.0.0.1 POST /login.html 401
192.168.1.10 GET /admin.html 403
10.0.0.5 GET /index.html 200
EOF
```

### Narration

Search for all lines containing "401":

### On-Screen Demo

```bash
grep "401" /tmp/access.log
```

### Narration

Case-insensitive search with **-i**:

### On-Screen Demo

```bash
grep -i "GET" /tmp/access.log
```

### Narration

Show line numbers with **-n** — critical when you need to know where in a large file a match appears:

### On-Screen Demo

```bash
grep -n "403" /tmp/access.log
```

### Narration

Invert the match with **-v** — show every line that does NOT match. This is extremely useful for filtering out noise:

### On-Screen Demo

```bash
grep -v "200" /tmp/access.log
```

### Narration

Recursive search through a directory with **-r** — search all files under a path:

### On-Screen Demo

```bash
grep -r "PermitRootLogin" /etc/ssh/
```

### Narration

Show only filenames that contain a match with **-l**:

### On-Screen Demo

```bash
grep -rl "PermitRootLogin" /etc/
```

### Narration

Count matches per file with **-c**:

### On-Screen Demo

```bash
grep -c "401" /tmp/access.log
```

### Narration

Finally, **-F** treats the pattern as a fixed string rather than a regular expression. This is important when your search string contains characters like `.`, `*`, or `[` that have special meaning in regex:

### On-Screen Demo

```bash
grep -F "192.168.1.10" /tmp/access.log
```

### Narration

Without `-F`, the dots in the IP address would match any character. With `-F`, they match literal dots.

That wraps up Part 1. You now have the tools to open and edit any text file on a Linux system and to search files efficiently. In Part 2 we build on this foundation with sed, awk, and the pipeline tools that let you process text at scale. See you there.

---

## Summary Slide

### Part 1 Key Commands

- `nano file` — open with nano; Control+O save, Control+X exit, Control+W search
- `vim file` — open with vim; i = Insert, Esc = Normal, :w save, :q quit, :wq both, :q! discard
- Vim navigation: h/j/k/l; dd delete line; yy yank; p paste; /pattern search; :%s/old/new/g replace
- `grep pattern file` — search for pattern
- `grep -i` case-insensitive; `-n` line numbers; `-v` invert; `-r` recursive; `-l` filenames only; `-c` count; `-F` fixed string

---

*End of Module 04 Part 1 Script*

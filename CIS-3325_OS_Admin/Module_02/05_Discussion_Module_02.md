# Discussion Forum: Module 02 - File System Hierarchy and Navigation Commands

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

### Scenario A - Disk Full Alert

You receive an alert at 2:00 AM that the root filesystem on a production Linux server is 99%
full. Services are starting to fail because they cannot write log files or temporary data.

1. Describe a sequence of at least three commands you would run immediately to identify which
   directory or file is consuming the most disk space. Include the exact commands and explain
   what each one tells you.
2. The /var/log directory is full of log files from a web server. What two approaches could
   you take to recover space quickly while minimizing impact on the running service?
3. How would using separate partitions for /var, /tmp, and / at install time have prevented
   this situation from affecting all system services simultaneously?

---

### Scenario B - Incident Response File Search

A security incident response team suspects that an attacker placed a malicious script somewhere
on the server within the last 24 hours. You need to locate recently created or modified files.

1. Write the exact find command you would use to locate all files in /home and /tmp that have
   been modified within the last 24 hours. Explain each flag in your command.
2. Once you find a suspicious file, you want to check whether it contains known malicious
   keywords like "wget" or "curl" or "chmod 777". Write the grep command you would use and
   explain its flags.
3. The attacker may have also created hidden files (files starting with a dot). How would you
   include hidden files in your search, and why are dot-files a common attacker technique?

---

### Scenario C - New Administrator Onboarding

You are mentoring a junior administrator who comes from a Windows background and is confused by
the Linux filesystem layout. They keep asking "where is the C drive?" and trying to save files
to desktop shortcuts.

1. Explain the single-tree filesystem concept to a Windows user in plain language. How is mounting
   a disk in Linux fundamentally different from a drive letter assignment in Windows?
2. Identify three specific FHS directories that a new Linux administrator must memorize and
   explain why each one matters for day-to-day administration tasks.
3. The junior administrator wants to use a graphical file manager instead of the terminal. What
   are two professional reasons why terminal-based navigation and file management are essential
   skills even if a GUI is available?

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 02 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Every Linux administrator spends a large portion of their day navigating directories and searching
for files. The filesystem hierarchy is not an arbitrary decision - every directory's location was
chosen for a reason. When you understand why the map is drawn the way it is, you stop guessing
and start knowing. Think carefully about the scenarios above and connect them to the lab commands
you practiced this week. The ability to find what you need quickly - whether a configuration file,
a log, or a suspicious script - is what separates a reactive administrator from a proactive one.

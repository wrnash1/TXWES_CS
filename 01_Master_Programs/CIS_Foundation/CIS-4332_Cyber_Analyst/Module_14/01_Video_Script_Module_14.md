# Video Script: Module 14 — Security Automation and Scripting for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Slide 1 — Introduction

Welcome to Module 14: Security Automation and Scripting for Analysts. I am Professor Nash.

We have covered detection, response, forensics, and compliance. In this module we focus on a skill that multiplies your effectiveness across all of those domains: automation.

Security analysts are drowning in data. Thousands of log lines per second. Hundreds of alerts per shift. Vulnerability scan outputs spanning thousands of findings. The analyst who can write a Python script to parse, filter, and summarize that data in seconds instead of spending hours doing it manually is exponentially more productive.

Automation is no longer a "nice to have" skill for security analysts. It is a career-defining competency.

---

## Slide 2 — Why Automation Matters

Consider these daily analyst tasks:

Parsing a 50,000-line firewall log to find all connections to a specific IP address. Manually, this takes 30 minutes. With a two-line Python script using `grep` or pandas, it takes 5 seconds.

Correlating IP addresses from a threat intelligence feed against your SIEM's last 24 hours of network connections. Manually, impossible at scale. With a Python script hitting your SIEM's REST API, it runs in minutes.

Generating a weekly vulnerability management report showing unpatched critical CVEs by system owner. Manually, hours of spreadsheet work. With a Python script pulling from the scanner's API, it runs in minutes and can be scheduled.

Automation frees analyst time for judgment work — the work machines cannot do.

---

## Slide 3 — Python for Security Analysts

Python is the dominant scripting language in security operations. It is readable, has extensive library support for security tasks, and is the language of choice for most security tools and APIs.

Key Python libraries for security analysts:

- `re` — regular expressions for log parsing
- `requests` — HTTP API interaction
- `pandas` — data manipulation and analysis
- `json` — parsing API responses and log data
- `csv` — reading and writing CSV data
- `subprocess` — running OS commands from Python scripts
- `datetime` — timestamp parsing and manipulation
- `hashlib` — hash generation for file integrity

You do not need to be a software engineer to write useful security scripts. You need to understand core Python constructs: variables, loops, conditionals, functions, and file I/O.

---

## Slide 4 — Regular Expressions for Log Analysis

Regular expressions, or regex, are patterns that describe text. They are essential for extracting structured data from unstructured log files.

A log line like this contains several fields:

`2024-03-15 14:32:17 192.168.1.45 DENY TCP 10.0.0.1:443`

A regex pattern can extract the IP address, action (DENY), protocol, and destination port from this line, regardless of how many thousands of lines surround it.

Key regex concepts analysts must know:

- Character classes: `\d` (digit), `\w` (word character), `\s` (whitespace)
- Quantifiers: `+` (one or more), `*` (zero or more), `{n}` (exactly n)
- Anchors: `^` (start of line), `$` (end of line)
- Groups: `()` — capture a matched group for extraction
- Alternation: `|` — match this OR that

Regex is available in Python's `re` module, in SIEM query languages, in grep, and in many other security tools.

---

## Slide 5 — Parsing Logs with Python

Let us walk through a practical log parsing example. You have a Windows Security event log export in CSV format. You need to extract all Event ID 4625 (failed login) entries and count failures by username.

The Python approach:

1. Open the CSV file using Python's `csv` module or `pandas`
2. Filter rows where the EventID column equals 4625
3. Extract the username field from each matching row
4. Count occurrences using a dictionary or `Counter` from the `collections` module
5. Sort by count and output the top offenders

This script produces in seconds what would take an analyst 45 minutes to extract manually from a log viewer. And once written, it runs in perpetuity at no additional cost.

---

## Slide 6 — Automating Scans

Security scanners — Nmap, Nessus, OpenVAS — have command-line interfaces that Python can call using the `subprocess` module.

An analyst can write a Python script that:

- Reads a list of IP addresses from a text file
- Runs an Nmap scan against each IP
- Parses the Nmap XML output for open ports
- Compares the result against a baseline of approved open ports
- Writes a report of any port that should not be open

This is a simple version of what enterprise vulnerability management systems do. Understanding the underlying automation concept helps you understand and tune those systems.

---

## Slide 7 — API Integration with Security Tools

Modern security tools expose REST APIs that allow analysts to programmatically query data, create tickets, and trigger actions. This is the foundation of security automation.

Common REST API operations:

- `GET` — retrieve data (query alerts, get asset information)
- `POST` — create data (submit IoCs, create incidents)
- `PUT/PATCH` — update data (change ticket status)
- `DELETE` — remove data

Python's `requests` library handles all of these operations. A typical API interaction:

1. Authenticate using an API key in the request header
2. Make a GET request to the API endpoint
3. Parse the JSON response
4. Process the data (filter, correlate, summarize)
5. Take action or write output

Security tools with REST APIs that analysts commonly integrate with include VirusTotal, MISP, Splunk, QRadar, ServiceNow, Cortex XSOAR, and PagerDuty.

---

## Slide 8 — SOAR Platforms

SOAR stands for Security Orchestration, Automation, and Response. SOAR platforms are purpose-built systems for automating security operations workflows.

A SOAR platform connects your security tools — SIEM, ticketing system, threat intelligence feeds, endpoint detection tools, email gateway, firewall — and enables you to build automated workflows called playbooks.

A SOAR playbook for a phishing alert might:

1. Receive the alert from the SIEM
2. Extract the sender domain from the email headers
3. Query VirusTotal API for the domain reputation
4. Query the email gateway for all employees who received the same sender
5. If malicious: automatically quarantine the email across all inboxes, create an IR ticket, and send a notification to the security team
6. If inconclusive: create a ticket for analyst review with all context pre-populated

This workflow runs in under 60 seconds. Manually, it takes 15–30 minutes per incident.

---

## Slide 9 — SOAR vs. SIEM

Students frequently confuse SOAR and SIEM. They are complementary, not competing.

A SIEM ingests log data, correlates events, and generates alerts. It tells you that something happened.

A SOAR receives those alerts, enriches them with additional context from other tools, and executes response actions. It tells you (and does) what to do about what happened.

The SIEM is your detection engine. The SOAR is your response automation engine. In a mature SOC, alerts flow from SIEM to SOAR for automated enrichment and response.

---

## Slide 10 — Building a SOAR Playbook

SOAR playbooks are built as visual workflow diagrams or as code, depending on the platform. Popular SOAR platforms include Palo Alto Cortex XSOAR, IBM Security QRadar SOAR, Splunk SOAR, and open-source TheHive/Cortex.

A well-designed SOAR playbook follows these principles:

Define clear trigger conditions — exactly which alert type or event type starts the playbook.

Define decision points — where the playbook branches based on enrichment results.

Minimize false automation — actions that could disrupt legitimate business operations (account lockouts, firewall blocks) should require analyst approval.

Log every action — all automated actions should be recorded with timestamps in the case record.

Test before production deployment — run playbooks in test mode against real-world scenarios before enabling live automation.

---

## Slide 11 — Automation Ethics and Risk

Automation is powerful and carries risk. A script with a logic error running against production data can cause significant damage.

Key automation risk management principles:

Test in a safe environment before running against production.

Scope automation narrowly — scripts should do one thing well, not everything.

Implement dry-run modes — the ability to run a script and show what it would do without actually doing it.

Require human approval for destructive or disruptive actions — automated account lockouts, firewall rule additions, and file deletions should not run without analyst review.

Version control your scripts — keep scripts in a Git repository so you can track changes and roll back.

---

## Slide 12 — Regex in SIEM Query Languages

SIEM platforms including Splunk, QRadar, and Microsoft Sentinel all support regex in their query languages.

In Splunk Search Processing Language (SPL), the `rex` command extracts fields using regex:

`rex field=_raw "(?i)failed.*?(?P<username>\w+)"`

This extracts the word after "failed" and names it "username" for use in subsequent SPL operations.

Understanding regex in SIEM queries allows analysts to extract custom fields from log data that was not parsed by the SIEM's built-in parsers — unlocking insight from log formats the SIEM has never seen before.

---

## Slide 13 — Python Script Security

Analyst-written scripts need basic security hygiene:

Never hardcode credentials. Use environment variables or a secrets management tool to supply API keys and passwords to scripts.

Validate and sanitize inputs. Scripts that accept user input or external data should validate that data before using it.

Log script activity. Scripts that make changes should log what they did and when.

Use least privilege for service accounts running scripts. A script that only reads from a database should not run under credentials with write or delete permissions.

---

## Slide 14 — CySA+ Exam Connection

The CySA+ CS0-003 exam tests automation and scripting concepts in several ways. You should be able to:

- Explain what a SOAR platform does and how it differs from a SIEM
- Describe how Python and scripting support security analyst workflows
- Understand regex concepts and read basic regex patterns
- Identify API interaction concepts (REST, GET/POST, JSON responses)
- Recognize the risks of automated security actions and appropriate safeguards

Expect scenario questions that describe an analyst workflow and ask whether automation, a SOAR playbook, or a script would improve it.

---

## Slide 15 — Summary

Module 14 covered security automation and scripting. We examined Python for security use cases including log parsing, scan automation, and API integration. We explored regular expressions as the foundation of log analysis automation. We introduced SOAR platforms as purpose-built automation environments and distinguished them from SIEM. We covered the ethics and risks of automation in security operations.

---

## Slide 16 — Looking Ahead

In Module 15 we turn to Advanced Threat Hunting — hypothesis-driven search for threats that evade automated detection. You will work with MITRE ATT&CK, endpoint telemetry, and EDR/XDR platforms to build and execute structured hunts.

Complete all Module 14 activities before our next session.

---

End of Module 14 Video Script — 225 lines

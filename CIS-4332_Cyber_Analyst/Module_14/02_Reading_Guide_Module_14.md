# Reading Guide: Module 14 — Security Automation and Scripting for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Introduction

Module 14 develops your security automation and scripting skills. These skills are among the highest-demand capabilities in the current security job market because they multiply analyst productivity at scale. A script that runs in 5 seconds replaces 30 minutes of manual log review. A SOAR playbook that fires in under 60 seconds replaces a 20-step manual investigation workflow.

The CySA+ CS0-003 exam tests automation concepts across multiple domains. Domain 1 (Security Operations) includes SOAR and automation tools. Domain 2 (Vulnerability Management) includes scripted scan automation and API integration. You are not expected to write production code on the exam, but you must understand what automation does, how it works, and how it applies to analyst scenarios.

This reading guide builds the conceptual foundation and practical vocabulary you need.

---

## Section 1 — High-Yield Glossary

**SOAR (Security Orchestration, Automation, and Response)** — A category of security platform that integrates security tools, automates repetitive analyst tasks, and orchestrates multi-step response workflows (playbooks) triggered by alerts or events.

**REST API (Representational State Transfer Application Programming Interface)** — A web-based interface that allows programmatic access to a service's data and functionality using standard HTTP methods (GET, POST, PUT, DELETE). Most security tools expose REST APIs.

**Playbook (SOAR context)** — An automated workflow in a SOAR platform that defines a sequence of actions, decision points, and integrations to be executed in response to a specific trigger event or alert type.

**Python** — A high-level, interpreted programming language that is the dominant language for security scripting due to its readability, extensive library ecosystem, and broad adoption in security tools.

**Regular Expression (Regex)** — A pattern-matching language that describes sequences of characters. Used extensively in log parsing, data extraction, and SIEM query languages.

**SPL (Search Processing Language)** — Splunk's query language for searching and transforming indexed log data. Supports regex, statistical aggregation, and field extraction.

**JSON (JavaScript Object Notation)** — A lightweight, human-readable data interchange format used by virtually all REST APIs to structure request and response data.

**Enrichment** — The process of adding contextual information to an alert or event — such as IP reputation, file hash analysis, or user account details — to support analyst decision-making.

**Orchestration** — The coordination of multiple security tools and systems to execute a multi-step workflow automatically, typically managed by a SOAR platform.

**Dry Run** — An execution mode for scripts and automated workflows where all actions are simulated and logged, but no changes are made to production systems. Used for testing automation before live deployment.

**API Key** — A secret token used to authenticate API requests. Should never be hardcoded in scripts; should be stored in environment variables or a secrets manager.

**pandas** — A Python library for data manipulation and analysis, widely used for processing tabular security data including log exports and vulnerability scan outputs.

---

## Section 2 — Python for Security Analysts

### Core Python Concepts Required

You do not need to be a developer to write useful security automation. You need command of these constructs:

**Variables and data types** — strings, integers, lists, dictionaries, booleans.

**File I/O** — opening files, reading lines, writing output.

```python
with open("firewall.log", "r") as f:
    for line in f:
        print(line)
```

**String operations** — searching strings, splitting on delimiters, formatting output.

**Control flow** — `if/elif/else` conditionals, `for` and `while` loops.

**Functions** — defining reusable code blocks with `def`.

**Error handling** — using `try/except` to handle failures gracefully.

### Essential Security Libraries

**`re` — Regular expressions:**

```python
import re
pattern = r"(\d{1,3}\.){3}\d{1,3}"
matches = re.findall(pattern, log_line)
```

This extracts all IPv4 addresses from a log line.

**`requests` — HTTP API calls:**

```python
import requests
response = requests.get(
    "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8",
    headers={"x-apikey": api_key}
)
data = response.json()
```

**`csv` — CSV parsing:**

```python
import csv
with open("events.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["EventID"] == "4625":
            print(row["TargetUserName"])
```

**`collections.Counter` — Frequency counting:**

```python
from collections import Counter
usernames = ["admin", "jdoe", "admin", "admin", "jsmith"]
counts = Counter(usernames)
print(counts.most_common(3))
```

**`hashlib` — Hash computation:**

```python
import hashlib
with open("suspicious.exe", "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()
print(sha256)
```

---

## Section 3 — Regular Expressions Deep Dive

### Why Analysts Need Regex

Security logs are text. Useful security data is embedded in that text in predictable but varied formats. Regex is the tool that extracts structure from unstructured text at scale.

### Core Regex Syntax

| Pattern | Meaning | Example Match |
|---------|---------|---------------|
| `\d` | Any digit (0–9) | `4`, `7`, `2` |
| `\w` | Word character (a–z, A–Z, 0–9, `_`) | `admin`, `192` |
| `\s` | Whitespace (space, tab, newline) | ` `, `\t` |
| `.` | Any character except newline | `a`, `5`, `@` |
| `+` | One or more of preceding | `\d+` matches `443`, `80` |
| `*` | Zero or more of preceding | `\w*` matches empty or any word |
| `{n,m}` | Between n and m of preceding | `\d{1,3}` matches `1` to `999` |
| `^` | Start of line | `^ERROR` matches lines starting with ERROR |
| `$` | End of line | `\d$` matches lines ending with a digit |
| `()` | Capture group | `(\d+\.\d+\.\d+\.\d+)` captures an IP |
| `\|` | Alternation (OR) | `DENY\|BLOCK` matches either |

### Practical Regex Examples for Security

Extract IPv4 addresses:

```text
\b(?:\d{1,3}\.){3}\d{1,3}\b
```

Extract Windows Event IDs from log lines:

```text
EventID[:\s]+(\d{4,5})
```

Extract email addresses:

```text
[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}
```

Match base64-encoded PowerShell `-EncodedCommand` arguments:

```text
-[Ee]n[Cc]o[Dd]e[Dd][Cc]o[Mm][Mm]a[Nn][Dd]\s+([A-Za-z0-9+/=]+)
```

---

## Section 4 — REST API Integration

### The API Interaction Pattern

Every REST API integration follows the same basic pattern regardless of the target tool:

1. Obtain an API key or OAuth token through the tool's settings
2. Store the key in an environment variable: `export VT_API_KEY=your_key_here`
3. Read the key in Python: `api_key = os.environ.get("VT_API_KEY")`
4. Construct the API request URL and headers
5. Send the request using `requests.get()` or `requests.post()`
6. Parse the JSON response: `data = response.json()`
7. Extract the fields you need and use them

### Common Security Tool APIs

**VirusTotal** — Submit file hashes, URLs, and IPs for reputation lookup. Returns malicious/benign/suspicious verdict from 70+ antivirus engines.

**Shodan** — Query internet-facing asset information by IP. Returns open ports, services, and banner data.

**MISP (Malware Information Sharing Platform)** — Share and query IoCs in a threat intelligence community. Full REST API for event and attribute management.

**Splunk REST API** — Query Splunk searches programmatically and retrieve results as JSON.

**ServiceNow API** — Create, update, and query incident tickets from external scripts.

### API Rate Limits

Most security APIs enforce rate limits — a maximum number of requests per minute or day. Scripts must handle rate limiting gracefully using `time.sleep()` between requests or by checking response headers for remaining quota.

---

## Section 5 — SOAR Platforms

### How SOAR Works

A SOAR platform sits between your detection tools (SIEM, EDR) and your response tools (ticketing, firewalls, email gateways). It receives alerts, enriches them, makes automated decisions, and executes response actions.

The three components of SOAR:

**Orchestration** — Connecting multiple tools through integrations (API connectors). The SOAR platform becomes the hub that all tools plug into.

**Automation** — Executing repetitive tasks automatically without analyst intervention. IoC enrichment, alert triage, evidence collection.

**Response** — Taking actions in security tools — creating tickets, blocking IPs at the firewall, quarantining endpoints, locking user accounts.

### SOAR Playbook Design Principles

A well-designed playbook is:

**Triggered precisely** — Only fires on the specific alert type it was designed for. Broad triggers cause playbooks to fire on irrelevant events.

**Enrichment-first** — Gather all available context before taking any action. Never act on an alert before enriching it.

**Decision-gated** — High-impact actions (account lockout, firewall block, endpoint isolation) are gated behind analyst approval or confidence thresholds.

**Logged thoroughly** — Every action the playbook takes is recorded with a timestamp in the case record.

**Testable** — The playbook has a test mode where it executes the full logic but simulates actions rather than executing them.

### Analyst-Supervised vs. Fully Automated Actions

SOAR playbooks span a spectrum from fully automated to analyst-supervised:

Fully automated (low risk): creating a ticket, enriching an alert with reputation data, sending a notification.

Analyst-supervised (medium risk): blocking a known-malicious IP, quarantining an email.

Always analyst-approved (high risk): locking a user account, isolating an endpoint, deleting a file.

---

## Section 6 — Automation Risk and Ethics

### Script Safety Principles

Test in isolation before production deployment. A script that accidentally queries the wrong API endpoint can generate enormous charges or corrupt data.

Implement dry-run modes as a standard feature in any script that makes changes. The command-line flag `--dry-run` should print what would happen without doing it.

Use least-privilege service accounts. Scripts running on a schedule should authenticate with accounts that have only the permissions required for the script's specific function.

Never hardcode credentials. Rotating API keys and passwords across dozens of scripts that have them hardcoded is operationally painful and a security risk.

Version-control all scripts in a git repository. This provides audit trail, rollback capability, and collaboration without duplication.

### Automation Bias

Automation bias is the tendency to trust automated output without critical evaluation. In security, automation bias is dangerous. A SOAR playbook that automatically closes alerts as false positives based on an imperfect heuristic will eventually suppress a real incident.

All automated decisions should be periodically reviewed by analysts to verify the automation is behaving correctly.

---

## Section 7 — CySA+ Exam Focus Areas

The exam tests automation concepts at the conceptual and application level:

- Know what SOAR does and how it differs from SIEM
- Understand REST API concepts — HTTP methods, JSON, authentication
- Know Python's role in security automation — libraries, use cases
- Understand regex as a log parsing tool — be able to interpret simple patterns
- Recognize SOAR playbook design principles — triggers, enrichment, decision gates
- Identify automation risks — hardcoded credentials, automation bias, untested scripts

---

## Study Checklist

- [ ] Define all glossary terms without referencing notes
- [ ] Describe what SOAR does and name three security tools a SOAR could integrate with
- [ ] Name five Python libraries used in security scripting and describe each
- [ ] Write a regex pattern that extracts IPv4 addresses and explain each component
- [ ] Describe the five-step REST API interaction pattern
- [ ] Explain the difference between analyst-supervised and fully automated SOAR actions
- [ ] List three automation safety principles
- [ ] Complete the Module 14 Lab
- [ ] Complete the Module 14 Quiz
- [ ] Post your Module 14 Discussion initial post by Wednesday

---

## Required Resources

- Python Standard Library Documentation — docs.python.org (free)
- Python `requests` library documentation — docs.python-requests.org (free)
- regex101.com — Interactive regex testing tool (free)
- Palo Alto Cortex XSOAR Documentation — cortex.pan.dev (free)
- CompTIA CySA+ CS0-003 Exam Objectives — Domain 1 (Security Operations)
- Module 14 Video Lecture (Professor Nash)

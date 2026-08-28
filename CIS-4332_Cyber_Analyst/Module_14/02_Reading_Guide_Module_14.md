# Reading Guide: Module 14 — Security Automation and Scripting for Analysts

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4332 &BULL; CYBERSECURITY ANALYST & THREAT HUNTING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

## 9. Supplemental Resources

**1. Python `requests` Library Documentation**
<https://docs.python-requests.org/en/latest/>
The official documentation for the `requests` HTTP library — the standard tool for REST API calls in Python security scripts. The documentation covers making GET and POST requests, reading JSON responses, setting headers for API key authentication, handling HTTP error codes (including 429 rate limits), and using sessions for efficient repeated queries. Working through the quickstart section and the authentication chapter builds the foundational skills needed to complete any security API integration task, including VirusTotal, Shodan, and SIEM API queries.

**2. regex101.com — Interactive Regular Expression Tester**
<https://regex101.com>
A free, browser-based regular expression development and testing tool. Paste a sample log line and build a regex pattern interactively — the tool highlights which characters are matched, explains each component of the pattern in plain English, and shows capture groups and their extracted values. For security analysts learning to parse log files (firewall logs, Windows event exports, Sysmon output), regex101 dramatically shortens the iteration cycle for building extraction patterns. The site supports Python (re module) flavor, which ensures patterns tested here work directly in Python scripts.

**3. Palo Alto Cortex XSOAR Playbook Documentation**
<https://cortex.pan.dev/docs/xsoar/playbooks>
The official documentation for Cortex XSOAR (formerly Demisto), one of the most widely deployed SOAR platforms in enterprise SOCs. The playbook documentation covers trigger configuration, task types (automated, conditional, manual), integration connector setup, and case management. Even for teams using Splunk SOAR or Microsoft Sentinel automation, the conceptual architecture documented here — enrichment tasks, conditional branching, action tasks, and sub-playbooks — applies across all SOAR platforms and directly maps to the playbook design concepts tested on the CySA+ exam.

---

## Required Resources

- Python Standard Library Documentation — docs.python.org (free)
- Python `requests` library documentation — docs.python-requests.org (free)
- regex101.com — Interactive regex testing tool (free)
- Palo Alto Cortex XSOAR Documentation — cortex.pan.dev (free)
- CompTIA CySA+ CS0-003 Exam Objectives — Domain 1 (Security Operations)
- Module 14 Video Lecture (Professor Nash)

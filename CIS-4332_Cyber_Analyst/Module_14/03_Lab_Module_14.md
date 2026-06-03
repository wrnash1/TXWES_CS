# Lab Activity: Module 14 — Security Automation and Scripting for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Lab Overview

This lab develops hands-on Python scripting and automation skills in three areas: log parsing with regular expressions, API integration with a threat intelligence service, and SOAR playbook design. You will write Python scripts, analyze their output, and design an automated workflow for a real-world analyst task.

**Estimated Time:** 2–3 hours

**Tools Required:** Python 3.10 or later (free: python.org), Python `requests` library (`pip install requests`), text editor or IDE (VS Code recommended), VirusTotal free API account (register at virustotal.com — free tier provides 500 API calls/day), provided lab data files from Canvas Module 14 Lab folder.

**Lab Files (download from Canvas):**

- `lab14_firewall.log` — 5,000-line simulated firewall log
- `lab14_events.csv` — Windows Security event log export in CSV format
- `lab14_iocs.txt` — List of 20 IP addresses for threat intelligence lookup

---

## Part 1 — Log Parsing with Regular Expressions

### Step 1.1 — Examine the Log Format

Open `lab14_firewall.log` in a text editor. The log format is:

```text
TIMESTAMP HOSTNAME ACTION PROTOCOL SRC_IP:SRC_PORT DST_IP:DST_PORT BYTES
```

Example line:

```text
2024-03-15 14:32:17 fw-corp-01 DENY TCP 10.0.4.23:52341 185.220.101.47:443 2841
```

### Step 1.2 — Write a Log Parser

Write a Python script named `parse_firewall.py` that:

1. Opens `lab14_firewall.log` and reads all lines
2. Uses the `re` module to extract timestamp, action, source IP, destination IP, destination port, and byte count from each line
3. Filters for DENY actions only
4. Counts the number of DENY events per destination IP
5. Prints the top 10 destination IPs by DENY count in descending order

Starter regex pattern (complete the capture groups in your script):

```python
import re
pattern = (
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+\S+\s+(ALLOW|DENY)"
    r"\s+\w+\s+(\d{1,3}(?:\.\d{1,3}){3}):\d+"
    r"\s+(\d{1,3}(?:\.\d{1,3}){3}):(\d+)\s+(\d+)"
)
```

In your lab report include:

1. Your completed `parse_firewall.py` script
2. The script output showing the top 10 denied destination IPs and their counts
3. An assessment of whether the top denied IP appears suspicious and why

### Step 1.3 — Windows Event Log Analysis

Write a Python script named `analyze_events.py` that:

1. Opens `lab14_events.csv` using `csv.DictReader`
2. Filters for Event ID 4625 (failed logon) entries
3. Counts failed logons per target username and prints any username with more than 10 failures
4. Counts failed logons per source IP and prints any IP with more than 15 failures

In your lab report include:

1. Your completed `analyze_events.py` script
2. The script output
3. An assessment of whether the highest-count account and IP indicate a brute force attempt

---

## Part 2 — Threat Intelligence API Integration

### Step 2.1 — Set Up VirusTotal API Access

Register for a free VirusTotal account at virustotal.com. Copy your API key from profile settings.

Store your API key as an environment variable. Do not hardcode it in your script.

On Windows (PowerShell):

```powershell
$env:VT_API_KEY = "your_api_key_here"
```

On Linux/macOS:

```bash
export VT_API_KEY="your_api_key_here"
```

### Step 2.2 — Write the IP Reputation Checker

Write a Python script named `vt_check.py` that:

1. Reads IP addresses from `lab14_iocs.txt` (one per line)
2. Reads the API key from the `VT_API_KEY` environment variable using `os.environ.get()`
3. Queries `https://www.virustotal.com/api/v3/ip_addresses/{ip}` for each IP
4. Extracts from the JSON response: malicious count, suspicious count, harmless count, country, and AS owner
5. Sleeps 15 seconds between requests to respect the free tier rate limit of 4 requests per minute
6. Writes results to `vt_results.csv` with columns: IP, Malicious, Suspicious, Harmless, Country, AS Owner, Verdict

Apply this verdict logic in your script:

- Malicious count 5 or higher: HIGH RISK
- Malicious count 1–4: SUSPICIOUS
- Malicious count 0 and Suspicious above 0: REVIEW
- All counts zero: CLEAN

In your lab report include:

1. Your completed `vt_check.py` script
2. The `vt_results.csv` output
3. Count of IPs in each verdict category
4. A cross-reference identifying any HIGH RISK IPs that also appeared in the top denied IPs from Step 1.2, and your assessment of what that correlation means

---

## Part 3 — SOAR Playbook Design

For this part you will design (not implement) a SOAR playbook for the following scenario.

### Scenario

Your SIEM fires an alert titled "Potential Account Takeover" when a user account logs in from a new country that has never appeared in their login history AND the login occurs within 30 minutes of a failed MFA attempt from a different country. This alert fires 3–5 times per day.

### Step 3.1 — Playbook Design Document

Create a SOAR playbook design document in your lab report with these sections:

**Trigger:** The exact SIEM alert that initiates the playbook.

**Enrichment Steps:** At least five automatic data enrichment actions performed before any decision. For each action specify the data source or tool.

**Decision Logic:** A description or table showing what conditions lead to automated action versus analyst escalation.

**Automated Actions (no analyst approval required):** List actions with justification for why analyst approval is not needed.

**Analyst-Gated Actions (require analyst approval):** List higher-impact actions and explain why they require approval.

**Notification:** Who is notified, by what channel, and for which decision branch.

**Case Documentation:** What data is automatically written to the IR ticket.

### Step 3.2 — Playbook Metrics

Answer the following in your lab report:

1. Estimate the manual analyst time currently required to investigate one alert from start to close, assuming it is a false positive. Show a step-by-step time breakdown.
2. Estimate analyst time for the same false positive scenario after your playbook is implemented.
3. Calculate hours saved per week assuming an average of 4 alerts per day, 7 days per week.

---

## Part 4 — Reflection Questions

Answer the following in your lab report (3–5 sentences each):

1. Your script uses `time.sleep(15)` to respect the API rate limit. What would happen if you removed it? What approach would you use to process 5,000 IPs quickly within rate limits?
2. Your SOAR playbook gates account lockout behind analyst approval. Describe one scenario where fully automated lockout would cause significant business harm, and one where waiting for analyst approval would cause significant security harm.
3. In Step 1.3 you flagged accounts with more than 10 failed logons. Why might a legitimate account trigger this threshold, and how would you refine the logic to reduce false positives while preserving detection accuracy?

---

## Deliverables

Submit a single PDF to Canvas containing:

1. Part 1 — Both scripts with outputs and analysis
2. Part 2 — Script, CSV output, and cross-reference analysis
3. Part 3 — Playbook design document and metrics calculations
4. Part 4 — Reflection question answers

**Grading:** 100 points total. Parts 1 and 2 are worth 30 points each. Part 3 is worth 25 points. Part 4 is worth 15 points.

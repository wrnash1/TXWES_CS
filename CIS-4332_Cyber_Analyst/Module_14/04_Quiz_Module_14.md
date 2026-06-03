# Quiz: Module 14 — Security Automation and Scripting for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Instructions

Select the best answer for each question. Distractor analysis is provided after each question to support exam preparation.

---

## Question 1

A security analyst wants to automatically enrich every phishing alert in the SIEM with VirusTotal domain reputation data and create an IR ticket in ServiceNow — all within 90 seconds of the alert firing, without manual intervention. Which platform is designed specifically to enable this type of automated, multi-tool response workflow?

- A) SIEM (Security Information and Event Management)
- B) SOAR (Security Orchestration, Automation, and Response)
- C) EDR (Endpoint Detection and Response)
- D) UEBA (User and Entity Behavior Analytics)

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: A SIEM ingests log data, correlates events, and generates alerts. It does not natively integrate with external services like VirusTotal or ticketing systems and does not execute multi-step response workflows. The SIEM triggers alerts; a SOAR acts on them. Why B is correct: SOAR platforms are purpose-built to connect multiple security tools through API integrations and execute automated, multi-step workflows (playbooks) triggered by alerts. Enriching an alert with VirusTotal data and creating a ServiceNow ticket automatically is a textbook SOAR use case. Why C is incorrect: EDR monitors and responds to endpoint-level threats. It does not orchestrate workflows across multiple tools or integrate with ticketing and threat intelligence platforms. Why D is incorrect: UEBA analyzes user and entity behavior patterns to detect anomalies. It is a detection and analytics technology, not a workflow automation platform.

---

## Question 2

An analyst writes a Python script to parse a firewall log and extract all destination IP addresses from DENY records. The log line format is `TIMESTAMP ACTION PROTO SRC_IP:PORT DST_IP:PORT`. Which Python approach correctly extracts the destination IP using a regular expression?

- A) Split the line on spaces and take the 5th element, then split on colon to isolate the IP
- B) Use `re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)` and assume the second match is the destination IP
- C) Use `re.search(r"DENY\s+\w+\s+\S+\s+(\d{1,3}(?:\.\d{1,3}){3}):\d+", line)` and extract group 1
- D) Read the entire file into memory as a string and count occurrences of the word DENY

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Splitting on spaces is fragile if any field contains a space or the delimiter varies. It also does not target the DENY action specifically, so it would apply to ALLOW records too. Why B is incorrect: `re.findall` with a generic IP pattern on a log line containing both source and destination IPs returns both IPs. Assuming the second match is the destination is fragile — if the timestamp or other fields contain IP-like patterns, the positional assumption breaks. Why C is correct: This regex anchors the extraction to the DENY action pattern, skips the protocol and source IP fields with `\S+`, then captures the destination IP in group 1 using a precise pattern. `re.search()` returns a match object and group 1 is exactly the destination IP. This is precise, targeted, and robust to format variation in other fields. Why D is incorrect: Counting DENY occurrences in a string tells you nothing about destination IP addresses. This approach extracts no structured data at all.

---

## Question 3

A security analyst stores a VirusTotal API key directly in a Python script as a string literal: `api_key = "4f3a9b2c..."`. A colleague reviews the script and flags this as a security risk. Why is hardcoding credentials in a script a security concern?

- A) Python scripts run more slowly when string literals are used for authentication
- B) If the script is shared, committed to a version control repository, or stored in a shared location, the API key is exposed to anyone who can read the script
- C) VirusTotal requires API keys to be stored in encrypted files, so plain string literals will cause authentication failures
- D) Hardcoded API keys expire faster than environment-variable-stored keys

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: String literal API keys have no effect on script execution speed. Authentication performance is determined by network latency and API server response time, not variable storage type. Why B is correct: Hardcoded credentials are a persistent security anti-pattern. If a script is committed to a git repository — even a private one — the credential exists in the commit history forever, even after it is removed from the current file. If the repository is accidentally made public, or if a repository is compromised, every hardcoded credential is exposed. The correct practice is to store credentials in environment variables, a secrets manager (like HashiCorp Vault), or an encrypted configuration file. Why C is incorrect: VirusTotal's API does not enforce storage format requirements. The key can be passed in any way as long as it appears in the correct HTTP header. This is a fabricated technical requirement. Why D is incorrect: API key expiration policies are set by the service provider based on administrative configuration, not by how the key is stored locally.

---

## Question 4

In Splunk SPL, an analyst runs the following search to investigate failed logons: `index=wineventlog EventCode=4625 | stats count by user | sort -count`. What does the `| stats count by user | sort -count` portion of this search do?

- A) Filters events to show only the most recent failed logon for each user
- B) Counts the total number of Event ID 4625 records per user account and sorts them from highest to lowest count
- C) Searches for the string "count" in the user field and removes duplicate entries
- D) Converts the event log entries to JSON format sorted alphabetically by username

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: `stats count by user` does not filter to the most recent event — it aggregates all matching events and produces a count for each unique user value. Filtering to the most recent event would use `latest()` or `dedup`. Why B is correct: `stats count by user` is a Splunk aggregation command that groups all matching events by the `user` field and produces a count of how many events exist for each user. `sort -count` sorts the results by the count field in descending order (the `-` prefix means descending). Together this produces a frequency table of failed logons by username, sorted with the highest count first — exactly what you need to identify brute force targets. Why C is incorrect: `stats` is an aggregation command, not a string search or deduplication command. It does not search the user field for the string "count." Why D is incorrect: `stats` does not perform data format conversion. SPL has separate commands (`eval`, `outputlookup`, `collect`) for output formatting, and none of this search produces JSON.

---

## Question 5

A SOAR playbook is triggered when a user account generates more than 50 failed SSH login attempts in 10 minutes. The playbook is designed to automatically lock the account without analyst review. An analyst raises a concern that this automation could cause availability issues. Which scenario best illustrates the legitimate risk of fully automated account lockout?

- A) A threat actor uses the lockout mechanism intentionally to lock out administrator accounts by generating 51 failed login attempts against those accounts
- B) The account lockout will cause the SIEM to generate additional alerts, increasing analyst workload
- C) Automatic lockouts cannot be reversed without restarting the SOAR platform
- D) SSH failed login attempts always indicate brute force attacks and should always be locked immediately

**Correct Answer:** A

**Distractor Analysis:** Why A is correct: This describes a lockout abuse attack — also called an account lockout denial-of-service. An attacker who knows the lockout threshold can intentionally generate exactly enough failed attempts against high-value accounts (domain administrators, service accounts) to lock them out, disrupting operations without ever successfully authenticating. Fully automated lockout without analyst review creates a weaponizable denial-of-service vector against the organization's own accounts. This is a documented attack pattern that playbook designers must account for. Why B is incorrect: Additional SIEM alerts from a lockout event are a minor operational concern, not a material risk. Alert volume is managed through tuning, not by avoiding correct security actions. Why C is incorrect: Account lockouts are reversed through standard Active Directory or LDAP administrative procedures, not by restarting the SOAR platform. This is a fabricated technical limitation. Why D is incorrect: 50 failed SSH attempts in 10 minutes is strongly suspicious but not 100% conclusive. A misconfigured script, automated batch job, or monitoring tool using incorrect credentials could generate this pattern without any malicious intent. Automated lockout must account for these false-positive scenarios.

---

## Question 6

Which of the following Python code snippets correctly reads an API key from an environment variable and uses it in a VirusTotal API request header?

- A) `requests.get(url, auth=("username", "password"))`
- B) `api_key = os.environ.get("VT_API_KEY"); requests.get(url, headers={"x-apikey": api_key})`
- C) `api_key = input("Enter API key: "); requests.get(url, params={"key": api_key})`
- D) `requests.get(url, verify=False, api_key="VT_API_KEY")`

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: `auth=("username", "password")` uses HTTP Basic Authentication, which is not the authentication method VirusTotal uses. VirusTotal requires an API key passed in the `x-apikey` request header. Why B is correct: `os.environ.get("VT_API_KEY")` reads the API key from an environment variable — the correct security practice. `headers={"x-apikey": api_key}` passes it in the correct VirusTotal-required header field. This is both functionally correct and follows credential security best practices. Why C is incorrect: Prompting the user for an API key interactively with `input()` is impractical for automated scripts and makes the key visible in terminal history. VirusTotal also does not use a `params` key field for authentication — it uses a request header. Why D is incorrect: `verify=False` disables SSL certificate verification, which is a security vulnerability. `api_key` is not a valid parameter for `requests.get()`. This call will fail with a TypeError and also introduces a man-in-the-middle vulnerability.

---

## Question 7

An analyst wants to use regex to extract Windows Event IDs from log lines. A sample line is: `Security    Information    3/15/2024    14:32:17    Microsoft-Windows-Security-Auditing    4625`. Which regex pattern correctly extracts the Event ID (the 4-5 digit number near the end of the line)?

- A) `\w+`
- B) `\d{4,5}$`
- C) `[A-Z]+`
- D) `.*(\d{4,5})`

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: `\w+` matches any word character sequence (letters, digits, underscore). It would match every word in the line, not specifically the numeric Event ID. Why B is correct: `\d{4,5}` matches exactly 4 or 5 consecutive digits — the correct length range for Windows Event IDs. The `$` anchor ensures the match is at the end of the line, which is where the Event ID appears in this log format. This combination is specific enough to reliably extract the Event ID without matching other numeric fields. Why C is incorrect: `[A-Z]+` matches sequences of uppercase letters only. Event IDs are numeric; this pattern would match "Security" and "Information" but not the Event ID number. Why D is incorrect: `.*(\d{4,5})` uses a greedy `.*` quantifier that will consume as much of the line as possible before the `\d{4,5}` group, potentially matching the wrong number. Without the end anchor, this pattern may also match date components. Option B with the `$` anchor is more precise.

---

## Question 8

A security team implements a SOAR playbook that automatically blocks firewall egress to any IP that VirusTotal reports as malicious with 10 or more engine detections. Within a week, an employee reports that their organization's backup service is not uploading to the cloud. Investigation reveals that the backup provider's IP address was temporarily reported as malicious by VirusTotal (likely a false positive) and was auto-blocked. Which SOAR design principle would have prevented this issue?

- A) The playbook should run on a weekly schedule rather than in real time to allow analyst review of findings before action
- B) High-impact automated actions such as firewall blocks should be gated behind analyst approval, especially for egress rules affecting production services
- C) The playbook should use a higher detection threshold (50 or more engines) before auto-blocking any IP
- D) SOAR playbooks should not integrate with firewall management systems because the risk of blocking legitimate traffic is too high

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Running on a weekly schedule defeats the purpose of automated threat response. Malicious IPs need to be blocked quickly. The solution is not slower automation but supervised automation for high-impact actions. Why B is correct: The SOAR design principle of gating high-impact, potentially disruptive actions behind analyst approval would have prevented this. An analyst reviewing the VirusTotal result before executing the firewall block would have recognized the backup provider IP, checked the context, identified the likely false positive, and either skipped the block or applied a temporary exception. Automatic firewall egress blocking without review is high-risk precisely because of scenarios like this one. Why C is incorrect: Raising the threshold to 50 engines would miss most real threats. VirusTotal's free threshold community standards generally treat 5–10 engines as high-confidence malicious. Waiting for 50 would mean not blocking confirmed threats. The threshold is not the design flaw; the lack of human review for the blocking action is. Why D is incorrect: SOAR integration with firewall management is a legitimate and widely used capability. The issue is not the integration itself but the absence of human approval for high-impact actions within the integration.

---

## Question 9

What is the primary functional difference between a SIEM and a SOAR platform in a mature SOC?

- A) A SIEM stores log data and a SOAR displays dashboards
- B) A SIEM detects and alerts; a SOAR enriches, orchestrates, and automates response actions triggered by those alerts
- C) A SIEM is used by Tier 1 analysts and a SOAR is used by Tier 3 analysts only
- D) A SIEM and SOAR perform identical functions and organizations only need one

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: While SIEMs do store log data and display dashboards, this description omits the SIEM's core function of correlation and alerting. The SOAR's function is not merely dashboarding. Why B is correct: This is the precise functional distinction. The SIEM's job is data collection, correlation, and alert generation — it detects. The SOAR's job is to receive those alerts, enrich them with context from integrated tools, execute automated decision logic, and trigger response actions — it acts. In a mature SOC, alerts flow from SIEM to SOAR for automated enrichment and response. They are complementary layers of the same operational stack. Why C is incorrect: Both SIEM and SOAR are used across analyst tiers. Tier 1 analysts work in SIEM daily for alert triage; SOAR playbooks automate much of what Tier 1 does. The platforms are not segregated by tier. Why D is incorrect: SIEM and SOAR perform distinctly different functions that do not overlap. A SIEM without SOAR requires manual analyst effort for every enrichment and response action. A SOAR without a SIEM has no alert source to trigger on. Organizations need both.

---

## Question 10

An analyst is evaluating whether to automate the following tasks using Python scripts. Which task presents the HIGHEST risk if the script contains a logic error?

- A) Generating a weekly report of unpatched critical CVEs from the vulnerability scanner's API output
- B) Automatically deleting all files in a directory that match a filename pattern associated with known malware
- C) Querying VirusTotal for the reputation of 100 IP addresses and writing results to a CSV file
- D) Sending a daily summary email to the security team with the previous day's alert counts by category

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: A logic error in a reporting script produces an incorrect report — an analyst error of commission, not a destructive action. The underlying data is unaffected and the error is correctable. Why B is correct: Automatic file deletion based on a filename pattern match is irreversible if the pattern is too broad. A logic error — such as a regex that matches more broadly than intended — could delete legitimate system files, application files, or user documents, causing system instability, application failure, or data loss. Deletion operations are the highest-risk category for automated scripts because they are potentially irreversible and can affect files far beyond the intended scope. This type of script requires extensive testing, dry-run validation, and scope restrictions. Why C is incorrect: A logic error in a VirusTotal reputation check produces incorrect CSV output — an analytical error. The underlying systems are unaffected. The worst outcome is making a wrong risk decision based on bad data, which is a judgment error, not a destructive automated action. Why D is incorrect: A logic error in a summary email script sends incorrect statistics to the security team. This is an informational error. The underlying data and systems are unaffected.

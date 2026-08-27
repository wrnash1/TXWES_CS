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

---

## Question 11

A Python script queries the VirusTotal API for 200 IP addresses. After the first four requests, the API returns HTTP 429. What does this response code indicate and what is the correct fix?

- A) The API key is invalid; the analyst must re-register for a VirusTotal account
- B) The server is temporarily unavailable; retry all 200 requests immediately
- C) The request rate limit has been exceeded; the script must add a delay between requests to stay within the allowed quota
- D) The IP address format is invalid; the regex used to extract IPs is incorrect

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: HTTP 429 is a standard rate-limiting response, not an authentication failure. An invalid API key returns HTTP 401 Unauthorized or HTTP 403 Forbidden. Why B is incorrect: Retrying all requests immediately after receiving HTTP 429 will produce more 429 responses — the rate limit window has not reset. Immediate retry loops can cause the API service to throttle or ban the caller's account. Why C is correct: HTTP 429 Too Many Requests is the standard rate-limiting response defined in RFC 6585. It means the client has sent more requests than the API allows in the defined time window. The correct fix is to insert delays between requests — for VirusTotal's free tier, one request every 15 seconds (4 per minute). The fix is typically implemented with `time.sleep()` in Python. Why D is incorrect: HTTP 429 is an HTTP-level response about request frequency, not a validation error about request content. Invalid URL formats would produce HTTP 400 Bad Request or a connection error before the API even processes the request.

---

## Question 12

An analyst writes a Python script that opens a CSV file using `csv.DictReader`. What is the primary advantage of `DictReader` over reading the file with `open()` and splitting each line on commas?

- A) `DictReader` is faster because it uses compiled C code to process CSV data
- B) `DictReader` automatically handles quoted fields, embedded commas, and headers — mapping each row to a dictionary keyed by column name
- C) `DictReader` can process CSV files larger than available RAM by streaming data from disk
- D) `DictReader` encrypts the file contents during processing to protect sensitive log data

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: While the csv module is implemented in C for performance, the primary advantage of DictReader is not speed — it is ease and correctness of structured data access. Why B is correct: CSV files frequently contain quoted fields that include commas (e.g., a field value like "Smith, John" would break a naive split-on-comma approach). `csv.DictReader` handles RFC 4180 CSV quoting rules correctly and maps each row to an ordered dictionary where keys are the column headers from the first row. This makes field access by name (e.g., `row["EventID"]`) instead of by index, which is more readable, maintainable, and resilient to column reordering. Why C is incorrect: `csv.DictReader` reads rows on demand, which is memory-efficient, but this is not its distinguishing advantage over a manual split approach. Both approaches process the file line by line. Why D is incorrect: `csv.DictReader` performs no encryption. It is a data parsing library, not a security or cryptography library.

---

## Question 13

A SOAR playbook receives a phishing alert and automatically enriches the reported URL by querying a URL analysis API. The API returns a JSON response. Which Python code correctly accesses the `malicious` field nested inside a `data > attributes > last_analysis_stats` path in the response?

- A) `response.malicious`
- B) `response.json()["data"]["attributes"]["last_analysis_stats"]["malicious"]`
- C) `response.text.data.attributes.last_analysis_stats.malicious`
- D) `json.loads(response)["malicious"]`

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: `response` is a `requests.Response` object. It does not have a `.malicious` attribute. Accessing JSON fields from a requests response requires first calling `.json()` to parse the response body as a Python dictionary. Why B is correct: `response.json()` parses the response body JSON string and returns a Python dictionary. Nested JSON objects are accessed using sequential dictionary key lookups: `["data"]` accesses the top-level key, `["attributes"]` goes one level deeper, `["last_analysis_stats"]` goes another level, and `["malicious"]` retrieves the target value. This is the correct Python pattern for navigating nested JSON API responses. Why C is incorrect: `response.text` returns the raw JSON as a Python string. Python strings do not support dot-notation attribute access for JSON fields. This code would raise an AttributeError. Why D is incorrect: `json.loads()` deserializes a JSON string, not a `requests.Response` object. This would raise a TypeError. Additionally, the path navigates to `["malicious"]` at the top level, which does not match the nested structure described in the scenario.

---

## Question 14

An analyst creates a SOAR playbook that automatically sends a Slack notification to the #security-alerts channel every time the SIEM generates an alert. Within 24 hours, the team disables the playbook because Slack is flooded with hundreds of messages. Which playbook design principle was violated?

- A) Enrichment-first — the playbook should have enriched alerts before notifying
- B) Triggered precisely — the playbook fired on every alert type instead of being scoped to specific high-priority alert categories
- C) Decision-gated — the playbook should have required analyst approval before sending any Slack message
- D) Logged thoroughly — the playbook should have written all notifications to a case record before sending

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: The enrichment-first principle governs whether the playbook gathers context before acting. Failing to enrich does not explain why the Slack channel was flooded — the flood is caused by the trigger scope being too broad. Why B is correct: The triggered-precisely principle states that playbooks should only fire on the specific alert types they were designed for. A playbook that triggers on all SIEM alerts without a category or severity filter will fire hundreds or thousands of times per day in a production environment. The correct design is to scope the trigger to a specific alert type (e.g., "only Critical severity phishing alerts") or a severity threshold so that notifications reach the channel only for alerts that genuinely require immediate human attention. Why C is incorrect: The decision-gated principle governs high-impact actions like account lockouts and endpoint isolation. Sending a Slack notification is a low-impact action that does not require analyst approval. The problem is not the absence of approval gates — it is that the trigger is too broad. Why D is incorrect: Logging playbook actions is important for audit trails but is not related to the flood problem. Logging does not prevent the playbook from firing too broadly.

---

## Question 15

A security analyst writes a Python script to parse Windows Event ID 4624 logon events and flag any logon from a non-RFC-1918 source IP address. Which regex correctly matches IPv4 addresses that are NOT RFC-1918 private addresses (i.e., not 10.x.x.x, 172.16–31.x.x, or 192.168.x.x)?

- A) The regex approach alone cannot reliably distinguish public from private IPs; the script should extract all IPs and use Python's `ipaddress` module to check `ip.is_private`
- B) `r"^(?!10\.|172\.(1[6-9]|2\d|3[01])\.|192\.168\.)(\d{1,3}\.){3}\d{1,3}$"`
- C) `r"\b(?:185|198|203)\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"`
- D) `r"\b(?!127\.0\.0\.1)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"`

**Correct Answer:** A

**Distractor Analysis:** Why A is correct: While option B is technically a reasonable negative-lookahead regex, the most reliable and maintainable approach for IP classification in Python is to use the built-in `ipaddress` module. `ipaddress.ip_address(ip_string).is_private` returns True for all RFC-1918 ranges, link-local, and loopback addresses without requiring complex regex. This approach handles edge cases, avoids regex errors, and is the standard professional practice. Option B is functionally close but is fragile and harder to maintain or extend. Why B is incorrect as the best answer: Although this regex attempts to implement RFC-1918 exclusion with negative lookaheads, it is complex, difficult to verify for correctness, and does not account for link-local (169.254.x.x), loopback (127.x.x.x), or APIPA ranges. The `ipaddress` module is the canonical correct tool for this task. Why C is incorrect: This pattern only matches IPs beginning with 185, 198, or 203 — a handful of specific public IP prefixes. It would miss all other public IP addresses, making it functionally useless as a general public IP detector. Why D is incorrect: This pattern excludes only 127.0.0.1 loopback. It does not exclude any of the RFC-1918 ranges, so it would match private IPs as if they were public, producing a flood of false positives on internal logons.

---

## Question 16

A junior analyst's Python automation script runs every 30 minutes on a shared server to collect and process security data. The script uses the service account `svc_security_auto` which has been granted Domain Admin privileges "for convenience." Which security principle does this violate and what is the correct remediation?

- A) Separation of duties — the script should be reviewed by two analysts before running
- B) Least privilege — the service account should be granted only the specific permissions required for the script's data collection tasks, not Domain Admin
- C) Non-repudiation — the script needs to sign its output files with a digital certificate
- D) Defense in depth — the script should run on an isolated network segment

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Separation of duties governs whether the same person can authorize and execute a sensitive action. It is not the principle being violated by a service account having excessive privileges. Why B is correct: The principle of least privilege requires that every account, process, and service be granted only the minimum permissions necessary to perform its defined function. A data collection script does not need Domain Admin rights — it needs read access to the specific data sources it queries. Granting Domain Admin "for convenience" means that if the script is ever compromised (through a vulnerability in a dependency, a logic error, or a supply chain attack), the attacker inherits full domain control. The remediation is to audit what the script actually accesses and create a service account with only those specific read permissions. Why C is incorrect: Non-repudiation is about proving that an action was performed by a specific party. Output file signing is unrelated to the access rights of the service account. Why D is incorrect: Network segmentation is a defense-in-depth control but does not address the excessive privilege of the service account. Segmentation limits what the account can reach from the network; privilege limits what the account can do. Both are important but the specific violation described is least privilege.

---

## Question 17

An analyst wants to test a Python script that calls an external REST API before deploying it in production. The production API has usage costs and rate limits. Which testing approach best validates the script's logic without consuming production API quota?

- A) Run the script against the production API with a small dataset of 5 records before running the full dataset
- B) Mock the API response — create a local function or use a mocking library to return predetermined JSON responses and test the script's parsing and decision logic against those responses
- C) Disable SSL certificate verification with `verify=False` to use a test endpoint without certificates
- D) Comment out the API call and manually verify the output by reading the source code

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Testing against the production API, even with a small dataset, consumes quota, may trigger rate limits, and creates real entries in the production system logs. It also does not allow testing of edge cases (API errors, malformed responses, empty results) without manipulating production data. Why B is correct: Mocking replaces the actual API call with a local substitute that returns predetermined responses. Python's `unittest.mock` library provides `patch` decorators that intercept API calls and return whatever JSON the test defines. This allows testing all code paths — normal responses, error responses (HTTP 429, 500), malformed JSON, missing fields — without any external dependency, cost, or quota consumption. Mocking is the industry-standard approach for testing code with external dependencies. Why C is incorrect: Disabling SSL verification is a security vulnerability and has nothing to do with avoiding production API costs. It does not create a test environment. Why D is incorrect: Commenting out the API call and reading the code does not actually execute the parsing and decision logic. Logic bugs only manifest when code runs. This is not testing — it is manual code review, which has value but does not validate runtime behavior.

---

## Question 18

A SOAR playbook automatically closes phishing alerts as false positives when the reported URL has zero VirusTotal detections. Over three months, the playbook closes 94% of alerts automatically. An analyst discovers that a credential harvesting site operating for less than 24 hours evaded VirusTotal detection (no detections on VirusTotal at time of check) and was closed by the playbook as a false positive. Which concept does this scenario illustrate?

- A) Rate limiting — the playbook exceeded the API quota and missed the detection
- B) Automation bias combined with a detection gap — relying solely on VirusTotal reputation for zero-day phishing sites misses newly registered malicious URLs that have not yet been catalogued
- C) Hardcoded credentials — the API key was embedded in the playbook and stolen by the attacker
- D) Insufficient logging — the playbook did not record the URL and therefore could not detect the attack

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Rate limiting produces HTTP 429 errors and causes API calls to fail — it does not cause incorrect classification of URLs that were successfully queried. Why B is correct: This scenario illustrates two related problems. First, automation bias: the playbook treats VirusTotal's "zero detections" verdict as conclusive evidence of legitimacy without considering that newly deployed malicious sites are routinely undetected by reputation databases for hours to days. Second, it demonstrates the detection gap inherent in reputation-based analysis: URL reputation services can only detect URLs that have been reported and catalogued. Zero-day phishing infrastructure specifically exploits this gap. The playbook design flaw is using a single intelligence source with a binary "zero = clean" rule without incorporating additional signals (domain age, registrar, hosting provider, URL path patterns). Why C is incorrect: Credential theft of the API key would prevent the playbook from making API calls at all (HTTP 401/403 responses), not cause incorrect classification decisions. Why D is incorrect: Insufficient logging affects post-incident investigation ability but does not cause the incorrect classification. The playbook incorrectly classified the URL because of its decision logic, not because it failed to log the URL.

---

## Question 19

Which Python code correctly writes a list of dictionaries to a CSV file with a header row derived from the dictionary keys?

- A) `open("output.csv", "w").write(str(results))`
- B) `with open("output.csv", "w", newline="") as f: writer = csv.DictWriter(f, fieldnames=results[0].keys()); writer.writeheader(); writer.writerows(results)`
- C) `json.dump(results, open("output.csv", "w"))`
- D) `pd.DataFrame(results).to_csv("output.csv", index=True)`

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Converting a list of dictionaries to a string with `str()` produces Python's internal dictionary representation — curly braces, quotes, and colons — which is not valid CSV format. This output cannot be opened correctly by Excel, a SIEM, or any standard CSV parser. Why B is correct: `csv.DictWriter` is designed exactly for this use case. `fieldnames=results[0].keys()` derives the header columns from the first dictionary's keys. `writeheader()` writes the header row. `writerows(results)` writes all dictionaries as rows in the correct field order. The `newline=""` parameter prevents `csv.writer` from adding extra blank lines on Windows. This is the canonical correct approach. Why C is incorrect: `json.dump()` writes JSON format, not CSV format. The output file would contain JSON syntax, not comma-separated values. A JSON file with a `.csv` extension would confuse any tool expecting CSV. Why D is incorrect: While `pandas` would work, it is not part of Python's standard library and requires installation. More importantly, `index=True` adds an unwanted numeric index column to the CSV output. The standard library `csv.DictWriter` solution in option B is correct and requires no dependencies.

---

## Question 20

A security team wants to use automation to reduce mean time to detect (MTTD) for insider threat scenarios involving large data uploads to personal cloud storage. Which combination of automated capabilities best addresses this detection goal?

- A) Deploy a SOAR playbook that blocks all outbound HTTPS traffic to consumer cloud storage domains
- B) Configure the SIEM to alert on NetFlow data showing sustained high-volume outbound transfers to cloud storage IP ranges, and use a SOAR playbook to automatically correlate the source user identity, check for concurrent DLP policy violations, and create a priority case for analyst review
- C) Run a weekly Python script that exports firewall logs and emails a report of the top 10 data-sending IPs to the security manager
- D) Enable full SSL inspection on the perimeter firewall to decrypt and log all cloud storage traffic content

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Blocking all outbound HTTPS to consumer cloud storage is an extremely broad preventive control that disrupts legitimate business use (employees accessing authorized cloud tools). It addresses the threat through prevention, not detection, and is not an automation strategy — it is a firewall rule that an analyst would need to manage manually for exceptions. Why B is correct: This answer combines all the right automation elements for insider threat detection: SIEM-based detection using NetFlow for behavioral pattern recognition (sustained high-volume transfers), SOAR enrichment to add user identity context and cross-reference DLP violations (multi-source correlation), and automated case creation to deliver a complete enriched alert to the analyst. This is precisely how a mature SIEM+SOAR stack is used to reduce MTTD — detect the behavioral pattern automatically, enrich it with relevant context automatically, and surface a prioritized case to the human analyst. Why C is incorrect: A weekly report has an MTTD of up to 7 days from the exfiltration event — completely inadequate for insider threat response. Automation that runs weekly rather than in real-time or near-real-time does not meaningfully improve MTTD. Why D is incorrect: Full SSL inspection is a visibility technique, not an automated detection or response capability. It generates significantly more data but does not by itself alert on insider threat behavior. It also raises legal and privacy considerations for employee monitoring.

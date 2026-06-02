# Quiz: Module 03 - OSINT and Passive Reconnaissance

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash
**Instructions:** Select the single best answer for each question.

---

## Question 1

Which of the following best describes passive reconnaissance in the context of penetration testing?

- A) Sending ICMP echo requests to target systems to identify live hosts before scanning
- B) Gathering information about a target using publicly available sources without directly interacting with the target's systems
- C) Running an authenticated Nessus scan against in-scope servers with credentials provided by the client
- D) Attempting to log into web applications using default credentials discovered during enumeration

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Passive reconnaissance uses publicly available sources — WHOIS, DNS, search engines, Shodan, social media — without sending any traffic to the target's systems. No fingerprints are left on the target's logs.
- Why A is incorrect: Sending ICMP echo requests directly to target systems is active reconnaissance (host discovery). It interacts directly with target infrastructure and requires authorization.
- Why C is incorrect: An authenticated Nessus scan actively connects to and scans target servers. This is active vulnerability scanning, not passive reconnaissance.
- Why D is incorrect: Attempting to log into web applications is active testing (exploitation/credential attacks). It directly interacts with target systems.

---

## Question 2

A penetration tester queries a target domain's name server with the command `dig axfr @ns1.target.example target.example` and receives a complete list of all DNS records for the domain. What does this indicate?

- A) The target's firewall is misconfigured and is passing all DNS traffic to external hosts
- B) The target's name server is misconfigured to allow zone transfers from any requesting host, leaking the complete DNS zone
- C) The tester has successfully exploited a DNS injection vulnerability and injected false records
- D) The target domain is using DNSSEC, which makes zone data publicly available for validation

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: A successful AXFR (zone transfer) from a name server indicates that the server is misconfigured to allow zone transfers without restricting the requesting host. This is a security misconfiguration that leaks all DNS records in the zone to any requester.
- Why A is incorrect: A firewall misconfiguration would not cause a zone transfer to succeed. The AXFR response comes from the DNS server's own configuration allowing unrestricted transfers.
- Why C is incorrect: A successful zone transfer is a read operation that returns existing records. DNS injection involves inserting false records into DNS — a completely different attack.
- Why D is incorrect: DNSSEC signs DNS records to prevent tampering but does not make zone data public or authorize unrestricted zone transfers.

---

## Question 3

A penetration tester uses the Google search operator `site:example.com filetype:pdf "confidential"` during passive reconnaissance. Which of the following best describes what this technique is and what it targets?

- A) Active reconnaissance — the query contacts the example.com web server directly to retrieve PDF files
- B) Passive reconnaissance — the query searches Google's existing index for PDF files on the target domain containing the word "confidential"
- C) Vulnerability scanning — the query identifies whether example.com's web server has directory listing enabled
- D) Social engineering — the query gathers employee names from PDF documents to use in phishing campaigns

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Google dorking queries Google's pre-existing index. The tester's traffic goes to Google's servers, not the target's. This makes it passive reconnaissance — no packets are sent to example.com during the search.
- Why A is incorrect: The query contacts Google, not the target's web server. Passive reconnaissance does not directly interact with target systems.
- Why C is incorrect: Identifying directory listing requires sending a request to the web server. Google dorking may reveal open directories through indexed results, but the query itself is not a vulnerability scan.
- Why D is incorrect: While PDF documents may contain employee names, the technique itself is OSINT/passive reconnaissance, not social engineering. Social engineering involves deception-based interaction with people.

---

## Question 4

Which tool pre-installed on Kali Linux automates the collection of email addresses, subdomains, and employee names from multiple public sources including Google, LinkedIn, Shodan, and certificate transparency logs?

- A) Nmap
- B) Metasploit
- C) theHarvester
- D) Burp Suite

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: theHarvester is specifically designed for passive OSINT collection, querying multiple public data sources to discover email addresses, subdomains, hostnames, employee names, and open ports associated with a target domain.
- Why A is incorrect: Nmap is an active network scanner that discovers hosts, open ports, and services by sending packets to target systems. It is active reconnaissance.
- Why B is incorrect: Metasploit is an exploitation framework used in the exploitation phase. While it has some auxiliary scanning modules, it is not an OSINT collection tool.
- Why D is incorrect: Burp Suite is a web application testing proxy used for active web application security testing. It is not a passive OSINT tool.

---

## Question 5

A penetration tester queries Shodan for assets belonging to a target organization using the filter `org:"Target Corp"` and discovers several internet-facing devices with outdated firmware versions. Is this technique passive or active reconnaissance, and why?

- A) Active reconnaissance, because the tester's computer must connect to Shodan's servers to perform the query
- B) Active reconnaissance, because Shodan's crawlers connect to target systems, which constitutes unauthorized access
- C) Passive reconnaissance, because the tester queries Shodan's pre-indexed database without sending any traffic directly to the target's systems
- D) Passive reconnaissance, but only if the tester has a paid Shodan subscription — free queries are considered active

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Querying Shodan is passive reconnaissance because the tester's traffic goes to Shodan's servers, not the target's. Shodan's own crawlers previously collected the data from the target. The tester retrieves stored results — no interaction with the target occurs during the query.
- Why A is incorrect: Connecting to Shodan's servers to perform the query does not constitute active reconnaissance against the target. The relevant distinction is whether traffic reaches the target's systems.
- Why B is incorrect: Shodan's crawlers operate independently and continuously across the internet. Their activity is not under the tester's control during the engagement query, and it predates the engagement.
- Why D is incorrect: The subscription level has no bearing on whether a technique is classified as passive or active. The classification depends on whether the tester's activity reaches target systems.

---

## Question 6

During WHOIS reconnaissance on a target domain, a tester finds that the domain expires in three weeks and DNSSEC is listed as "unsigned." Which two security concerns do these findings raise?

- A) Domain expiration means the organization cannot be legally tested; DNSSEC absence means DNS records are encrypted
- B) Domain expiration creates a domain hijacking risk if the organization fails to renew; DNSSEC absence means DNS responses are not cryptographically signed and are vulnerable to spoofing attacks
- C) Domain expiration means the engagement must conclude before the expiration date; DNSSEC absence means zone transfers are automatically permitted
- D) Domain expiration means the tester should avoid scanning the domain; DNSSEC absence indicates the domain uses split-horizon DNS

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: An expiring domain that is not renewed can be registered by an attacker, redirecting the organization's traffic to a malicious host (domain hijacking). DNSSEC unsigned means DNS responses lack cryptographic authentication, making the domain vulnerable to DNS spoofing and cache poisoning.
- Why A is incorrect: Domain expiration has no bearing on testing authorization. DNSSEC provides authentication of DNS records, not encryption — its absence does not mean records are encrypted.
- Why C is incorrect: The engagement is governed by the RoE dates, not the domain expiration date. DNSSEC absence does not automatically permit zone transfers.
- Why D is incorrect: There is no standard recommendation to avoid scanning based on domain expiration. Split-horizon DNS is a configuration technique unrelated to DNSSEC.

---

## Question 7

A penetration tester reviews TXT DNS records for a target domain and finds the following: `"v=spf1 include:_spf.google.com include:sendgrid.net ~all"`. What does this reveal about the target organization?

- A) The organization uses Google Workspace for email and SendGrid for transactional or marketing email delivery
- B) The organization's email server is vulnerable to open relay attacks
- C) The organization uses two separate mail servers that both require MX record entries
- D) The SPF record is malformed and indicates the organization has no email security controls

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct: An SPF record listing `include:_spf.google.com` indicates the organization sends legitimate email through Google (Google Workspace / Gmail). `include:sendgrid.net` indicates they also send through SendGrid, which is commonly used for transactional email, marketing campaigns, or password reset notifications. This is valuable OSINT about the organization's email infrastructure.
- Why B is incorrect: An SPF record is an email authentication mechanism. Its presence does not indicate an open relay vulnerability — it actually helps prevent email spoofing.
- Why C is incorrect: SPF records identify authorized sending sources, not mail server count. MX records identify mail servers.
- Why D is incorrect: The record shown is syntactically valid SPF. The `~all` tag means SPF failures result in soft-fail treatment, which is a legitimate policy choice.

---

## Question 8

A tester finds that a developer at the target organization has a public GitHub repository containing a configuration file committed three months ago. The file contains what appears to be a hardcoded AWS access key and secret. What is the correct immediate action?

- A) Use the AWS credentials to enumerate the organization's cloud environment before they expire
- B) Document the finding thoroughly and notify the client immediately since the credentials may still be active and represent an active risk
- C) Ignore the finding since it is outside the authorized IP scope of the penetration test
- D) Delete the file from the GitHub repository to prevent the credentials from being misused by others

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Discovered credentials represent a potentially active, high-severity risk that should be immediately escalated to the client. They need to determine if the key is still valid and revoke it if so. Document the finding precisely including the repository URL and commit details.
- Why A is incorrect: Using discovered credentials to access cloud systems without explicit authorization in the RoE is unauthorized access — even if the credentials were found publicly. This is a CFAA violation.
- Why C is incorrect: OSINT findings are not limited by IP scope. A publicly exposed credential is a legitimate finding regardless of the testing scope for active exploitation.
- Why D is incorrect: Deleting files from a third party's repository is unauthorized activity and would destroy evidence. Only the repository owner can remove the file.

---

## Question 9

Which of the following Google dork queries is best suited to discover open directory listings on a target domain that might expose files not meant to be public?

- A) `site:example.com filetype:html`
- B) `intitle:"index of" site:example.com`
- C) `inurl:example.com`
- D) `site:example.com ext:php`

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: `intitle:"index of"` matches pages where "index of" appears in the HTML title tag — the standard Apache and Nginx directory listing title. Combined with `site:example.com`, this specifically finds open directory listings on the target domain.
- Why A is incorrect: `filetype:html` finds HTML pages but does not specifically target directory listings. Most web pages are HTML, so this query returns a broad and unfocused result set.
- Why C is incorrect: `inurl:example.com` is not a standard Google dork syntax for finding directory listings. This query would return pages where "example.com" appears in the URL.
- Why D is incorrect: `ext:php` finds PHP files but not directory listings specifically. This query is useful for finding exposed PHP scripts but not for identifying directory browsing enabled on the server.

---

## Question 10

A penetration tester queries `crt.sh` for certificates issued to `*.example.com` and discovers a subdomain `legacy-erp.example.com` that does not appear in any public DNS records or on the company website. What is the significance of this finding?

- A) The subdomain is a honeypot deployed by the security team and should be avoided
- B) The certificate was likely issued in error and the subdomain probably does not resolve to any system
- C) The subdomain may represent a legacy or forgotten system that still has a valid certificate and may still be running, making it a potentially high-value reconnaissance target
- D) Certificate transparency logs are unreliable and this finding should be disregarded without further verification

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Certificate transparency logs capture every certificate ever issued. A subdomain appearing only in CT logs — not in public DNS or the website — indicates a potentially forgotten legacy system. Legacy systems are frequently under-patched, under-monitored, and represent high-value targets during penetration testing.
- Why A is incorrect: While some organizations do deploy honeypots, assuming any discovered system is a honeypot without evidence is not a valid reason to ignore a legitimate finding. Document it and verify during active testing.
- Why B is incorrect: Certificate issuance requires domain validation — the certificate was issued for a real reason. Assuming it was an error without investigation would miss a potentially significant finding.
- Why D is incorrect: Certificate transparency logs are a reliable, public, cryptographically-verified record of issued certificates. They are a standard and trusted OSINT source in professional penetration testing.

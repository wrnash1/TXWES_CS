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

---

### Question 11 (5 points)

A penetration tester searches LinkedIn for employees at the target organization and discovers that three job postings list "experience with Palo Alto NGFW, Splunk SIEM, and ServiceNow required." What type of intelligence does this provide, and why is it valuable during reconnaissance?

- A) It confirms the organization uses those products, revealing specific technology stack details that inform attack surface mapping and tool selection
- B) It is irrelevant to penetration testing since job postings describe desired skills, not actual deployed systems
- C) It constitutes active reconnaissance because the tester's browser connects to LinkedIn's servers, which may be monitored by the target
- D) It is only useful for social engineering campaigns and has no value for technical network penetration testing

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: Job postings requiring specific product experience strongly indicate those products are in use. Knowing the NGFW vendor, SIEM platform, and ITSM system shapes attack methodology, informs evasion choices, and identifies monitoring capabilities the tester must account for.
  - Why B is incorrect: While job postings describe desired skills, they reliably reflect current technology in use. Organizations hire for the tools they operate, making job postings a high-confidence OSINT indicator of deployed technology.
  - Why C is incorrect: Querying LinkedIn is passive reconnaissance. The tester's traffic reaches LinkedIn's servers, not the target's infrastructure. LinkedIn is a third-party public data source.
  - Why D is incorrect: Technology stack intelligence from job postings has direct value for technical testing — informing which exploit modules, evasion techniques, and lateral movement paths are most relevant to the specific environment.

---

### Question 12 (5 points)

Which DNS record type is specifically used to identify the mail servers authorized to receive email for a domain, and why is this record valuable during passive reconnaissance?

- A) TXT record — because it contains SPF authorization data for outbound email
- B) NS record — because it identifies the name servers responsible for the zone
- C) MX record — because it identifies the mail servers for the domain, which may reveal email hosting providers, on-premises mail servers, or spam filtering services
- D) CNAME record — because it maps alias hostnames to canonical names, revealing internal naming conventions

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: MX (Mail Exchange) records point to the hostnames of mail servers for the domain. Their values reveal whether the organization uses cloud email (Google Workspace, Microsoft 365), on-premises Exchange, or third-party filtering services (Proofpoint, Mimecast) — all of which inform phishing simulation planning and email infrastructure understanding.
  - Why A is incorrect: TXT records can contain SPF data about authorized sending sources, but TXT records do not identify the mail servers that receive email for the domain.
  - Why B is incorrect: NS records identify the authoritative name servers for the DNS zone, not the mail servers. This is useful OSINT but answers a different question about the target's infrastructure.
  - Why D is incorrect: CNAME records create aliases pointing to canonical hostnames. They reveal naming conventions and may expose internal or staging systems, but they do not identify mail servers.

---

### Question 13 (5 points)

A tester finds a cached Google result showing the target's `/admin/config.php` page from six months ago. The current live page returns a 403 Forbidden. What is the reconnaissance value of the cached result?

- A) None — the cached result is outdated and the 403 response confirms the page is inaccessible
- B) The cached result may reveal application configuration details, parameter names, or internal paths that no longer appear in the live response, informing later active testing
- C) The cached result should be downloaded and submitted to the client as evidence of a current vulnerability
- D) Accessing a cached Google result constitutes active reconnaissance against the target

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Cached pages preserve historical content that may reveal sensitive information — configuration parameters, internal path structures, admin panel field names, or version strings — that is useful for planning active testing even if the live page is now restricted. This is a legitimate passive OSINT technique.
  - Why A is incorrect: Historical data has reconnaissance value even when the live resource is restricted. Cached content reveals what was previously exposed and informs attack path planning.
  - Why C is incorrect: A cached page from six months ago does not constitute evidence of a current vulnerability. It is reconnaissance data that informs later investigation, not a finding to report directly.
  - Why D is incorrect: Accessing a Google cache retrieves data from Google's servers, not the target's. This is passive reconnaissance.

---

### Question 14 (5 points)

During OSINT collection, a tester uses `theHarvester -d targetcorp.com -b all` and receives output including email addresses in the format `firstname.lastname@targetcorp.com`. Why is the email format specifically valuable beyond just having a list of addresses?

- A) Email addresses can be directly used to brute-force VPN login portals without additional information
- B) The naming convention (firstname.lastname) reveals the organization's likely username format, which can be used to construct usernames for Active Directory enumeration and password spray attacks in later phases
- C) The email addresses can be used to register accounts on social media platforms in the target employees' names
- D) The format is only useful if the organization uses Microsoft 365 — otherwise email formats have no value in penetration testing

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Many organizations use the same format for email addresses and Active Directory usernames (firstname.lastname or first initial + last name). Knowing the format lets the tester construct a username list for later phases such as password spraying, LDAP enumeration, or Kerberos pre-authentication attacks without needing to enumerate AD directly.
  - Why A is incorrect: Email addresses alone are not sufficient to brute-force VPN portals — the username format used by the VPN may differ, and brute-forcing is an active technique requiring authorization. The value described is reconnaissance-level intelligence, not a direct attack capability.
  - Why C is incorrect: Creating social media accounts in employees' names is impersonation fraud and is completely outside the scope of authorized penetration testing.
  - Why D is incorrect: Username format intelligence is valuable regardless of the email hosting provider. Active Directory username conventions are typically the same whether email is hosted in Microsoft 365, Google Workspace, or on-premises.

---

### Question 15 (5 points)

What is the purpose of querying `robots.txt` and `sitemap.xml` on a target web server during passive or early active reconnaissance?

- A) To download all files on the web server for offline analysis without triggering rate limiting
- B) To identify paths the organization wants search engines to avoid indexing — which often reveals admin panels, API endpoints, or internal application paths not intended for public discovery
- C) To enumerate all user accounts registered on the target web application
- D) To determine whether the web server supports HTTP/2 or HTTP/3 protocol versions

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `robots.txt` instructs web crawlers which paths to avoid, but is itself publicly accessible. Paths listed in `Disallow:` directives often reveal sensitive directories like `/admin`, `/api`, `/internal`, or `/backup`. `sitemap.xml` maps the application's URL structure. Both are useful reconnaissance sources.
  - Why A is incorrect: Neither file allows downloading other server files. They are text documents that describe URL paths, not download mechanisms.
  - Why C is incorrect: Neither file contains user account information. User enumeration requires different techniques such as registration form probing or API endpoint testing.
  - Why D is incorrect: HTTP protocol version detection requires analyzing response headers or performing active connection testing — not reading robots.txt or sitemap.xml.

---

### Question 16 (5 points)

A penetration tester uses `Maltego` during passive reconnaissance. Which of the following best describes Maltego's primary capability and how it differs from theHarvester?

- A) Maltego is a network scanner that sends probes to target systems; theHarvester is a password cracking tool
- B) Maltego is a link-analysis and graph visualization tool that maps relationships between entities (domains, emails, people, organizations) from OSINT sources; theHarvester focuses on bulk collection of specific data types from search engines and public databases
- C) Maltego is a web application fuzzer; theHarvester is a DNS brute-forcing tool
- D) Both tools are identical in function — Maltego is just the commercial version of theHarvester

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Maltego excels at visualizing relationships between discovered entities — connecting people to domains, domains to IP addresses, IP addresses to organizations — using transforms against public data sources. theHarvester focuses on bulk collection of emails, subdomains, and hosts. They are complementary tools serving different reconnaissance analysis needs.
  - Why A is incorrect: Neither Maltego nor theHarvester are network scanners or password crackers. Both are passive OSINT tools. Maltego does offer active transforms but its primary value is relationship mapping of publicly available data.
  - Why C is incorrect: Maltego is not a web application fuzzer and theHarvester is not a DNS brute-forcer. DNS brute-forcing (like dnsenum or gobuster dns) is a separate active technique.
  - Why D is incorrect: Maltego and theHarvester are entirely different tools with different architectures, data sources, and use cases. Maltego is not simply a commercial version of theHarvester.

---

### Question 17 (5 points)

A tester reviewing Shodan results for a target organization finds a device with the banner: `220 ProFTPD 1.3.5 Server (TargetCorp FTP) [203.0.113.45]`. Why is version information in service banners significant during reconnaissance?

- A) It allows the tester to immediately exploit the service without further analysis
- B) It identifies the specific software and version, enabling the tester to research known CVEs and assess whether unpatched vulnerabilities likely exist on that service
- C) Banner information is unreliable because administrators routinely falsify it to mislead attackers
- D) Version information in banners is only relevant for web servers — FTP and other service banners carry no reconnaissance value

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Service banners identify software name and version, enabling CVE database lookups to identify known vulnerabilities. ProFTPD 1.3.5 has multiple known CVEs including remote code execution vulnerabilities. This intelligence shapes the exploitation phase planning.
  - Why A is incorrect: Version information informs research and planning — it does not automatically enable exploitation. The tester must verify the vulnerability applies, check whether it is in scope, and have authorization before attempting exploitation.
  - Why C is incorrect: While some administrators do modify banners, most production systems run default banners. Treating all banners as falsified without evidence is not standard practice and would cause testers to miss real vulnerabilities.
  - Why D is incorrect: Version intelligence from any service banner — FTP, SSH, SMTP, Telnet — is equally valuable. Any service running known-vulnerable software is a potential attack vector regardless of the protocol.

---

### Question 18 (5 points)

Which of the following best describes the Wayback Machine (web.archive.org) as a passive OSINT tool during a penetration test?

- A) It is a tool for testing how quickly a web server serves archived content under load
- B) It is an archive of historical web page snapshots that can reveal previously exposed sensitive content, deprecated endpoints, old login pages, or technology stack details no longer visible on the live site
- C) It stores a real-time mirror of the target website and reflects any changes made by the tester in real time
- D) It only archives publicly accessible .gov and .edu domains and is not useful for commercial target reconnaissance

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The Wayback Machine archives historical snapshots of web pages dating back decades. For penetration testing, it reveals previously exposed paths, old admin panels, legacy API endpoints, source code comments, and technology versions that may still be running or that inform understanding of the application's history.
  - Why A is incorrect: The Wayback Machine is an archival research tool, not a load testing or performance measurement tool.
  - Why C is incorrect: The Wayback Machine stores historical snapshots — it does not reflect real-time changes to either the live site or any tester activity.
  - Why D is incorrect: The Wayback Machine archives websites across all domain types including commercial (.com), government (.gov), education (.edu), and international domains. It is widely used for commercial target reconnaissance.

---

### Question 19 (5 points)

During passive reconnaissance, a tester discovers that the target organization's DMARC record is: `v=DMARC1; p=none; rua=mailto:dmarc@targetcorp.com`. What security implication does a `p=none` policy reveal?

- A) The organization has fully enforced email authentication and all spoofed emails will be rejected at the recipient's mail server
- B) The organization is only monitoring DMARC reports but has not enforced a reject or quarantine policy, meaning spoofed emails purporting to be from the domain may still be delivered to recipients
- C) The organization has disabled email entirely and uses only internal messaging platforms
- D) A `p=none` policy indicates DNSSEC is also disabled, creating a combined DNS vulnerability

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: DMARC `p=none` is a monitoring-only policy. Emails that fail DMARC checks are still delivered — only a report is sent to the `rua` address. This means the domain may be susceptible to email spoofing in phishing simulations, which is valuable reconnaissance intelligence for the social engineering phase if authorized.
  - Why A is incorrect: Full enforcement requires `p=reject` or `p=quarantine`. With `p=none`, no enforcement action is taken against failing messages — they are delivered normally.
  - Why C is incorrect: DMARC policy has no connection to whether email is used. A `p=none` policy is a common early-stage deployment choice for organizations actively using email who want to collect monitoring data before enforcing.
  - Why D is incorrect: DMARC policy and DNSSEC are independent controls. A `p=none` DMARC policy has no bearing on whether DNSSEC is enabled or disabled for the zone.

---

### Question 20 (5 points)

A penetration tester performing passive reconnaissance finds that an employee at the target organization posted a photo on social media showing their workstation. In the background, the computer screen displays what appears to be an internal ticketing system URL: `https://helpdesk.internal.targetcorp.com`. What is the reconnaissance value of this discovery?

- A) None — internal hostnames cannot be accessed from the internet and are irrelevant to external testing
- B) The internal hostname reveals a potentially accessible internal service and naming convention; it becomes a target for DNS resolution, VPN access testing, or post-exploitation lateral movement after an initial foothold is established
- C) The tester should contact the employee to obtain their login credentials for the ticketing system
- D) The finding should be submitted to LinkedIn as a terms of service violation

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Internal hostnames revealed through OSINT are valuable reconnaissance data. Even if not directly accessible externally, the hostname reveals the internal naming convention (subdomain.internal.domain), potentially resolves during VPN testing, and becomes a priority lateral movement target after an internal foothold is established during testing.
  - Why A is incorrect: Internal hostnames are not irrelevant — they are high-value targets during the post-exploitation and lateral movement phases. They also help map the internal network structure during planning.
  - Why C is incorrect: Contacting employees to solicit credentials is social engineering, which requires explicit separate authorization in the RoE. It is also outside the scope of passive reconnaissance.
  - Why D is incorrect: Observing publicly posted information on social media is a legitimate OSINT technique. There is no terms of service violation in viewing a public post, and LinkedIn is not a reporting channel for social media content.

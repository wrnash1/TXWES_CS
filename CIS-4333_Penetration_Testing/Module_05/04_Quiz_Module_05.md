# Quiz: Module 05 — Reconnaissance and OSINT

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

**Instructions:** Select the single best answer for each question. Questions are aligned to CompTIA PenTest+ PT0-002 Domain 2: Information Gathering and Vulnerability Scanning.

---

### Question 1

A penetration tester uses Shodan to search for open ports and software versions associated with a target organization's IP range. Which category of reconnaissance does this activity represent?

- A) Active reconnaissance, because Shodan directly scans the target's IP range
- B) Passive reconnaissance, because the tester is querying a third-party database and not interacting with the target's systems
- C) Social engineering, because Shodan accesses device banners without consent
- D) Physical reconnaissance, because Shodan reveals geographic locations of servers

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The tester is querying Shodan's database — a third-party service that performs its own scanning. The tester has no direct interaction with the target's systems. This is passive reconnaissance by definition.
- **Why A is incorrect:** Shodan does the scanning; the tester only queries Shodan's stored results. Direct interaction with the target would be active recon.
- **Why C is incorrect:** Social engineering involves human manipulation, not database queries. Banner collection by Shodan is automated technical scanning, not a social technique.
- **Why D is incorrect:** Physical reconnaissance involves physically observing a location. Geographic IP data is a by-product of the query, not the defining characteristic of the technique.

---

### Question 2

A tester attempts a DNS zone transfer against an authorized target using the command `dig axfr @ns1.example.com example.com`. The server returns the complete zone. What is the significance of this result?

- A) It is expected behavior — all DNS servers support zone transfers by default for transparency
- B) The zone transfer reveals only the SOA record, which is not useful for reconnaissance
- C) The misconfigured DNS server exposed every hostname, IP address, and record in the zone, significantly expanding the known attack surface
- D) This result confirms that the target is using DNSSEC, which requires open zone transfers

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A successful AXFR returns the complete DNS zone — every A, MX, CNAME, TXT, and other record. This is a critical DNS misconfiguration that hands the tester a complete map of all hostnames and IPs, exposing internal naming conventions and systems.
- **Why A is incorrect:** Zone transfers should be restricted to authorized secondary DNS servers only. An unrestricted zone transfer is a misconfiguration, not standard behavior.
- **Why B is incorrect:** A successful AXFR returns all zone records, not just SOA. The full record set is highly valuable for attack surface mapping.
- **Why D is incorrect:** DNSSEC validates DNS data integrity using cryptographic signatures. It has no relationship to zone transfer permissions. Open zone transfers and DNSSEC are independent configurations.

---

### Question 3

Which Google dork syntax would most effectively find PDF documents hosted on a specific organization's domain?

- A) `intext:pdf site:example.com`
- B) `filetype:pdf site:example.com`
- C) `inurl:pdf example.com`
- D) `cache:example.com filetype:pdf`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The `filetype:` operator restricts results to files with the specified extension. Combined with `site:` to restrict to the target domain, this efficiently surfaces all indexed PDFs hosted on that domain.
- **Why A is incorrect:** `intext:pdf` searches for the word "pdf" in the body of web pages — it does not filter for PDF file type. It would return HTML pages mentioning PDFs rather than actual PDF documents.
- **Why C is incorrect:** `inurl:pdf` searches for the string "pdf" in URLs. Some PDF files may be found this way, but many PDFs have non-descriptive URL paths that would be missed. It is far less precise than `filetype:`.
- **Why D is incorrect:** The `cache:` operator retrieves a cached version of a specific URL — it does not perform a broad search across a domain. It also cannot be meaningfully combined with `filetype:` as shown.

---

### Question 4

During reconnaissance, a tester discovers that a developer at the target organization has a public GitHub repository containing a configuration file with AWS access keys committed six months ago. The keys were later removed in a subsequent commit. What is the correct interpretation of this finding?

- A) The keys are no longer a risk because they were removed from the repository
- B) The keys may still be valid and accessible through the repository's commit history, representing a potential credential exposure
- C) This finding is outside scope because GitHub is a third-party platform
- D) Git commit history is encrypted and the old keys cannot be retrieved by an attacker

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Git stores the complete history of all commits. Removing sensitive data from the latest commit does not purge it from the history. Anyone who clones the repository can use `git log` and `git show` to retrieve all prior commit content, including the removed keys.
- **Why A is incorrect:** Removing credentials from the latest commit creates a false sense of security. The commit history preserves the original content. The keys should be revoked and rotated in the AWS console regardless.
- **Why C is incorrect:** If the GitHub repository is associated with the target organization and falls within the authorized scope of the engagement, it is a valid finding. Public GitHub repositories are OSINT sources.
- **Why D is incorrect:** Git commit history is not encrypted. It is stored as plain objects in the `.git` directory and transmitted without encryption in public repositories. History is fully accessible to anyone with read access.

---

### Question 5

A penetration tester is in the passive reconnaissance phase and wants to identify all subdomains of a target organization that have had TLS certificates issued. Which technique best accomplishes this without directly querying the target's systems?

- A) Run `nmap -sV` against the target IP range to find all web servers
- B) Query Certificate Transparency logs using a service such as crt.sh
- C) Perform a DNS zone transfer from the target's authoritative name server
- D) Use Nikto to crawl all subdomains and enumerate SSL certificates

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Certificate Transparency logs are public records maintained by certificate authorities. Querying crt.sh is entirely passive — no target interaction occurs. Every publicly trusted certificate issued to subdomains of the target domain is recorded, making this one of the most effective passive subdomain discovery techniques.
- **Why A is incorrect:** Nmap is an active scanning tool that sends packets to target systems. Running `nmap -sV` is active reconnaissance and violates the passive recon constraint in this scenario.
- **Why C is incorrect:** A DNS zone transfer (AXFR) directly queries the target's name server — this is active reconnaissance. It also requires the target's DNS server to be misconfigured to succeed.
- **Why D is incorrect:** Nikto is an active web application scanner. It sends HTTP requests directly to target servers, making it active recon and inappropriate for the passive phase.

---

### Question 6

theHarvester is being used during the reconnaissance phase. A tester runs `theHarvester -d targetcorp.com -b linkedin`. What type of information does this command primarily attempt to collect?

- A) Open ports and running services on targetcorp.com IP addresses
- B) Vulnerability details for software running on targetcorp.com servers
- C) Employee names and email address patterns from LinkedIn profiles associated with the target domain
- D) SSL certificate chains and cipher suites for targetcorp.com HTTPS endpoints

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The `-b linkedin` flag directs theHarvester to search LinkedIn for information associated with the target domain. LinkedIn searches primarily return employee names and, combined with domain information, help identify email address formats used by the organization.
- **Why A is incorrect:** Open port and service enumeration is performed by active scanning tools like Nmap. theHarvester does not probe IP addresses for running services.
- **Why B is incorrect:** Vulnerability identification is the role of scanners like Nessus or OpenVAS. theHarvester gathers identity and infrastructure information, not vulnerability data.
- **Why D is incorrect:** SSL certificate inspection is performed by tools like sslscan, testssl.sh, or Shodan's certificate indexing. theHarvester does not directly inspect TLS configurations.

---

### Question 7

Which of the following best describes the purpose of Maltego in the context of penetration testing reconnaissance?

- A) Maltego is a port scanner that maps network topology through active probing
- B) Maltego is a vulnerability scanner that identifies missing patches on target systems
- C) Maltego is a link analysis and visualization tool that maps relationships between entities such as domains, IPs, people, and organizations using transforms
- D) Maltego is a password cracking tool that brute-forces login portals identified during reconnaissance

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Maltego's core function is graphical link analysis. It starts with one entity (such as a domain) and applies transforms — automated queries to data sources — to discover and visualize related entities. The resulting graph maps the complete intelligence picture of the target.
- **Why A is incorrect:** Maltego does not send network probes or scan ports. Network mapping through active probing is done by tools like Nmap or Masscan.
- **Why B is incorrect:** Vulnerability scanning is the role of dedicated tools such as Nessus, OpenVAS, or Qualys. Maltego gathers and visualizes OSINT relationships, not vulnerability data.
- **Why D is incorrect:** Maltego has no password cracking capability. Password attacks are handled by tools like Hydra, Hashcat, or John the Ripper.

---

### Question 8

A client engagement begins and the tester has received written authorization with a defined scope. The tester wants to identify technology stack information about the client's web application without sending a single packet to the client's servers. Which two sources would best accomplish this? (Choose the best single answer that covers both.)

- A) Run Nmap with `-sV` and `-O` flags against the client's web server
- B) Check Shodan for indexed banner information and review archived versions of the client's website in the Wayback Machine
- C) Use Nikto to perform a passive web application scan with no active probing
- D) Run sqlmap in crawl mode against the client's login page

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Shodan stores banner data from its own periodic scans — querying it is passive. The Wayback Machine stores historical web snapshots — querying it is also passive. Both sources can reveal technology stack information (web server version from banners, frameworks from HTML comments and file extensions) without any contact with the client.
- **Why A is incorrect:** Nmap `-sV` and `-O` send active probes directly to the target. This is active reconnaissance and violates the constraint of not sending packets to the client's servers.
- **Why C is incorrect:** Nikto does not have a passive mode. It always sends HTTP requests to the target web server, making it active recon by definition.
- **Why D is incorrect:** sqlmap sends SQL injection payloads to the target application. This is exploitation-level active interaction, not passive reconnaissance.

---

### Question 9

During OSINT collection, a tester finds that a target company's job posting reads: "Senior Systems Administrator — 5 years experience with Microsoft Active Directory, VMware vSphere, and Palo Alto Networks Panorama required." What is the primary penetration testing value of this information?

- A) It confirms that the company is currently experiencing security incidents requiring additional staff
- B) It reveals likely technologies in the target environment, enabling more targeted scanning and exploitation research
- C) Job postings are not useful for penetration testing because they describe desired skills, not current technology
- D) This information can be used immediately to authenticate to Active Directory without additional enumeration

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Job postings reliably reflect the actual technology in use at an organization — you do not hire for skills you do not need. Knowing the target runs Active Directory, VMware vSphere, and Palo Alto Panorama allows the tester to prioritize relevant CVEs, configure targeted Nmap scripts, and prepare appropriate exploitation modules before ever touching the target.
- **Why A is incorrect:** A hiring posting for a sysadmin does not indicate a security incident. Organizations hire for growth, attrition, and many other reasons unrelated to security problems.
- **Why C is incorrect:** Job postings are consistently among the most reliable OSINT sources for technology stack identification. Organizations only list technologies they actually use when defining job requirements.
- **Why D is incorrect:** Technology identification does not provide authentication credentials. Significant additional enumeration and exploitation would be required to obtain any form of access.

---

### Question 10

A penetration tester is conducting reconnaissance and wants to enumerate all publicly accessible records for a domain, then attempt to identify whether the DNS server is misconfigured. Which sequence of commands reflects the correct professional approach?

- A) Begin with `nmap -p 53 target.com` then escalate to exploiting DNS vulnerabilities
- B) Run `dig target.com ANY` to review all available records, then run `dig axfr @ns1.target.com target.com` to test for zone transfer — document results either way
- C) Use `sqlmap --dns-domain target.com` to extract database content through DNS
- D) Run Metasploit's `auxiliary/scanner/dns/dns_amp` module to assess DNS record availability

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** This is the correct professional DNS enumeration sequence. `dig ANY` retrieves all accessible record types. The zone transfer attempt tests for the AXFR misconfiguration. Whether the transfer succeeds or is refused, both outcomes are documented as findings — a successful transfer is a critical misconfiguration; a refusal confirms the security control is in place.
- **Why A is incorrect:** `nmap -p 53` scans the DNS port and is appropriate for port confirmation, but jumping directly from a port scan to DNS exploitation skips enumeration and documentation. The sequence described is not professional practice.
- **Why C is incorrect:** sqlmap is a SQL injection tool that can use DNS as an exfiltration channel. It is not a DNS enumeration tool and has no role in standard DNS record inspection.
- **Why D is incorrect:** The `dns_amp` Metasploit module tests for DNS amplification — a DoS attack vector. It is not an enumeration tool and running it as a reconnaissance activity would be outside the scope of most engagements.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**

---

### Question 11 (5 points)

A tester uses `recon-ng` during passive reconnaissance. Which of the following best describes how `recon-ng` differs from `theHarvester`?

- A) `recon-ng` is an active network scanner; `theHarvester` is a passive OSINT collector
- B) `recon-ng` is a modular Python framework with a Metasploit-like interface that aggregates OSINT from many sources via interchangeable modules; `theHarvester` is a focused single-purpose tool for collecting emails, subdomains, and hostnames
- C) `recon-ng` only searches LinkedIn; `theHarvester` only searches Google
- D) Both tools are identical — `recon-ng` is simply the updated version of `theHarvester`

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: `recon-ng` follows a Metasploit-style modular architecture with workspaces, modules for dozens of data sources, and a structured database for storing findings. `theHarvester` is a focused, simpler tool that queries specific sources for emails, subdomains, and hostnames. They are complementary tools with different architectures and use cases.
  - Why A is incorrect: Both tools are passive OSINT collectors. `recon-ng` does not send active probes to target systems — it queries third-party data sources.
  - Why C is incorrect: Both tools query multiple sources. `recon-ng` has modules for LinkedIn, Shodan, Bing, Google, and many others. `theHarvester` also supports multiple sources via its `-b` flag.
  - Why D is incorrect: `recon-ng` and `theHarvester` are entirely separate tools with different architectures, authors, and design philosophies. Neither is an update of the other.

---

### Question 12 (5 points)

During passive reconnaissance a tester queries `crt.sh` and discovers that the target organization has a certificate issued for `vpn.internal.targetcorp.com`. What is the significance of this finding?

- A) It confirms the VPN service is vulnerable to certificate-based attacks and should be immediately exploited
- B) It reveals an internal hostname that suggests a VPN gateway may exist, which becomes a priority target for active scanning during the authorized testing phase
- C) Certificate transparency records are unreliable because certificates are often issued for systems that no longer exist
- D) The finding is irrelevant unless the tester can also obtain the private key associated with the certificate

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: A certificate issued for `vpn.internal.targetcorp.com` reveals that a VPN gateway likely exists at that hostname. VPN gateways are high-value targets because they provide remote access to the internal network. This OSINT finding shapes active scanning priorities during the authorized testing phase.
  - Why A is incorrect: Discovering a hostname via certificate transparency does not confirm any vulnerability. It identifies a potential target for further investigation — not an immediately exploitable system.
  - Why C is incorrect: Certificate transparency logs are cryptographically verified and highly reliable. While some certificates may be issued for systems that are later decommissioned, the finding is worth investigating rather than dismissing.
  - Why D is incorrect: The private key is not needed to exploit most VPN gateway vulnerabilities. The hostname discovery itself is the reconnaissance value — it enables targeted scanning, CVE research, and exploitation planning.

---

### Question 13 (5 points)

A penetration tester discovers through OSINT that the target organization recently experienced a significant data breach that was publicly reported. How does this information affect the reconnaissance phase?

- A) It is irrelevant — past breaches have no bearing on current penetration testing
- B) It may indicate previously exposed credentials that could still be valid, unpatched vulnerabilities that enabled the breach, or persistent attacker access that the tester may encounter during the engagement
- C) The tester should report the breach to law enforcement before proceeding with the engagement
- D) The existence of a prior breach means the current engagement should focus exclusively on social engineering

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: A prior breach is high-value OSINT. Breach reports often identify specific vulnerabilities or attack vectors used, exposed credentials may still be in use, and organizations that suffered breaches sometimes have lingering unpatched systems. This intelligence directly shapes the testing methodology and prioritization.
  - Why A is incorrect: Historical breach intelligence is specifically valuable reconnaissance data. Organizations that have been breached once are statistically more likely to have persistent security gaps that a penetration test should evaluate.
  - Why C is incorrect: Reporting a publicly known breach to law enforcement is not the tester's obligation — the breach is already known and reported. The tester's job is to use the intelligence professionally within the authorized scope.
  - Why D is incorrect: Prior breach intelligence informs all testing phases, not just social engineering. It is most immediately useful for identifying specific technical vulnerabilities and potentially exposed credentials.

---

### Question 14 (5 points)

Which Google dork operator would a penetration tester use to search specifically for pages containing a particular word in the URL path of a target domain?

- A) `site:targetcorp.com filetype:admin`
- B) `inurl:admin site:targetcorp.com`
- C) `intitle:admin site:targetcorp.com`
- D) `cache:targetcorp.com admin`

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: `inurl:` matches pages where the specified text appears in the URL path. Combined with `site:`, this finds pages on the target domain whose URL contains "admin" — commonly revealing admin panels, admin directories, or administrative API endpoints.
  - Why A is incorrect: `filetype:admin` is not a valid Google dork operator. `filetype:` is used with file extensions (e.g., `filetype:pdf`), not with words like "admin."
  - Why C is incorrect: `intitle:` matches pages where the specified text appears in the HTML page title, not the URL. This could find pages titled "Admin" but would miss admin URLs with different titles.
  - Why D is incorrect: `cache:` retrieves a cached version of a specific URL. It does not search for pages containing a keyword in the URL path.

---

### Question 15 (5 points)

A tester discovers through WHOIS that the target organization's domain registrar contact email is `it-admin@targetcorp.com` and the technical contact phone number is publicly listed. Why might this information be documented in the reconnaissance notes?

- A) The email and phone number can be used to authenticate to domain management portals without additional credentials
- B) The contact information identifies a named technical employee and a direct contact channel — valuable for social engineering simulation if explicitly authorized, and for understanding the target's IT organizational structure
- C) WHOIS contact information is never accurate because most organizations use privacy protection services
- D) The phone number should be called immediately to verify that it is still active before continuing reconnaissance

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: Named technical contacts reveal real employees and their roles. In engagements where social engineering is in scope, this information identifies high-value targets for pretexting. Even without social engineering scope, understanding the IT contact structure informs threat modeling and organizational mapping.
  - Why A is incorrect: WHOIS contact information does not provide authentication credentials. Domain management portals require proper authentication — a contact email or phone number alone does not grant access.
  - Why C is incorrect: While many organizations do use WHOIS privacy protection, many do not, and historical WHOIS records often contain real contact information even when current records are masked. This data is worth documenting and verifying.
  - Why D is incorrect: Calling the phone number without authorization is a social engineering activity that requires explicit scope approval. It is not a standard passive reconnaissance step and could constitute unauthorized contact with the target.

---

### Question 16 (5 points)

Which of the following best describes the reconnaissance value of analyzing a target organization's SPF, DKIM, and DMARC DNS records together?

- A) They reveal the organization's internal Active Directory structure and domain controller hostnames
- B) Together they reveal the organization's email infrastructure (sending sources, signing keys, and enforcement policy), indicating susceptibility to email spoofing and the effectiveness of email security controls
- C) SPF, DKIM, and DMARC records only affect inbound email and provide no outbound intelligence value
- D) These records can only be read by mail servers — penetration testers cannot access them directly

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: SPF identifies authorized sending sources (revealing cloud providers and mail infrastructure). DKIM reveals whether emails are cryptographically signed. DMARC reveals the enforcement policy (none/quarantine/reject) and reporting address. Together they tell the tester how susceptible the domain is to spoofing — critical intelligence for authorized phishing simulation planning.
  - Why A is incorrect: SPF/DKIM/DMARC records relate to email authentication and do not reveal Active Directory structure or domain controller hostnames. Active Directory enumeration requires different techniques.
  - Why C is incorrect: SPF, DKIM, and DMARC records are publicly readable DNS TXT records. Any tool that queries DNS — including `dig` and `nslookup` — can retrieve them. They are not limited to mail server access.
  - Why D is incorrect: DNS TXT records are publicly accessible. `dig TXT targetcorp.com` retrieves SPF records. `dig TXT _dmarc.targetcorp.com` retrieves DMARC records. These are standard passive reconnaissance queries.

---

### Question 17 (5 points)

A tester performs OSINT and finds the target organization's headquarters address, a photo of the building's entrance on the company website, and the name of their physical security vendor from a LinkedIn post by an employee. What type of reconnaissance does this represent, and how might it be used in an authorized engagement?

- A) This is active reconnaissance because the tester visited the physical location to observe it
- B) This is passive OSINT that could inform a physical security assessment if that component is authorized in the RoE — enabling the tester to understand entry point layout and security vendor products before any authorized physical testing begins
- C) Physical reconnaissance findings are outside the scope of any penetration test and should be discarded
- D) This information should be shared with law enforcement as it indicates the organization may be planning a physical security audit

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: Gathering public information about physical premises from the organization's own website and employee social media posts is passive OSINT. If physical security testing is authorized in the RoE, this intelligence informs entry point analysis, understanding of installed security products, and social engineering pretext development.
  - Why A is incorrect: The tester reviewed publicly available online sources — the company website and LinkedIn. No physical visit occurred, making this passive reconnaissance.
  - Why C is incorrect: Physical security intelligence is a standard and legitimate component of comprehensive penetration testing engagements. Many organizations specifically request physical security assessments alongside network testing.
  - Why D is incorrect: Reviewing publicly available information about an organization's facilities does not constitute a reportable concern. This is standard OSINT practice within authorized engagement boundaries.

---

### Question 18 (5 points)

During passive reconnaissance, a tester uses `theHarvester -d targetcorp.com -b linkedin` and discovers 47 employee profiles including titles like "Senior Network Engineer" and "Cloud Infrastructure Architect." What specific reconnaissance value do job titles provide?

- A) Job titles allow the tester to immediately guess those employees' passwords using common password patterns
- B) Job titles reveal organizational roles and technical responsibilities, helping map who manages specific systems — useful for understanding decision-making chains and identifying technically privileged individuals who may be targets for social engineering if authorized
- C) Job titles on LinkedIn are never accurate and this information should not be used in the engagement
- D) LinkedIn job titles can only be used for social engineering and have no value for technical network penetration testing

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: Job titles map organizational structure and technical responsibility. A "Senior Network Engineer" likely administers network infrastructure. A "Cloud Infrastructure Architect" likely manages cloud environments. This intelligence shapes threat modeling, identifies high-privilege targets for authorized social engineering, and informs which systems to prioritize during technical testing.
  - Why A is incorrect: Job titles do not reveal passwords. Password guessing based on personal information requires much more specific data (pet names, birthdays, etc.) and would constitute an unauthorized attack technique unless credential testing is specifically authorized.
  - Why C is incorrect: LinkedIn profiles are a standard and widely used OSINT source. While not 100% accurate, they are reliable enough to inform organizational mapping and are explicitly recognized as an OSINT source in PT0-002 exam objectives.
  - Why D is incorrect: Technical job titles have direct value for network penetration testing — they identify who administers specific systems, which informs escalation paths, pivot targets, and exploitation prioritization.

---

### Question 19 (5 points)

What is the primary security risk of a domain with no DMARC record at all, as discovered during DNS reconnaissance?

- A) The absence of a DMARC record prevents the domain from sending any email
- B) Without a DMARC record, there is no email authentication policy in place, meaning anyone can send spoofed emails appearing to come from that domain with no automatic rejection or quarantine
- C) A missing DMARC record makes the domain's MX records invisible to external mail servers
- D) The absence of DMARC only affects internal email routing and has no impact on external spoofing risk

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: DMARC provides receiving mail servers with instructions for handling messages that fail SPF or DKIM checks. Without any DMARC record, there is no policy — receiving servers make their own decisions, and many will deliver spoofed emails. This makes the domain susceptible to email spoofing attacks including phishing campaigns using the organization's domain name.
  - Why A is incorrect: DMARC governs how receiving servers handle authentication failures — it has no effect on whether the legitimate domain can send email.
  - Why C is incorrect: MX records are independent of DMARC. The absence of a DMARC record has no effect on MX record visibility or resolution.
  - Why D is incorrect: DMARC specifically addresses external email spoofing. It is an outbound reputation control that protects external recipients from receiving spoofed emails. Its absence is primarily an external risk.

---

### Question 20 (5 points)

A penetration tester discovers during OSINT that a target organization's website source code (visible in a browser's View Source) contains HTML comments including version strings for the framework and a commented-out test endpoint: `<!-- TEST API: /api/v1/internal/test-auth-bypass -->`. What is the correct professional response to this finding?

- A) Immediately send requests to the test endpoint to confirm whether it is still accessible before documenting the finding
- B) Document the finding precisely (source location, comment text, potential risk) and include it in the reconnaissance notes; testing the endpoint requires authorization and would occur during the active testing phase if it falls within scope
- C) Discard the finding because HTML comments in public source are not considered vulnerabilities
- D) Notify the client immediately and halt all reconnaissance because the endpoint name suggests a security bypass

- **Correct Answer:** B

- **Distractor Analysis:**
  - Why B is correct: The HTML comment is a passive OSINT finding — it was discovered by reading publicly available page source without touching the server. It should be documented precisely with its source and potential risk. Testing whether the endpoint is live and accessible is an active reconnaissance or exploitation activity requiring authorization under the RoE.
  - Why A is incorrect: Sending requests to the endpoint before documenting it or confirming authorization is active reconnaissance/testing against a specific target path — this must be authorized before proceeding.
  - Why C is incorrect: Exposed version strings and internal endpoint paths in public HTML source are legitimate reconnaissance findings. They may reveal specific versions for CVE research and suggest forgotten internal endpoints that could present security risks.
  - Why D is incorrect: The finding is significant but does not warrant halting reconnaissance. The correct response is precise documentation followed by inclusion in the planned active testing phase — not an emergency stop of the engagement.

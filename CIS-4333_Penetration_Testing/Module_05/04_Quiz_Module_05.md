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

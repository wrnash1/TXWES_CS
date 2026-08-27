# Reading Guide: Module 05 — Reconnaissance and OSINT

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Introduction

Module 05 covers the reconnaissance phase of a penetration test — systematically gathering intelligence about a target before any active interaction. This phase is also called "information gathering" in the PT0-002 exam objectives and falls within Domain 2: Information Gathering and Vulnerability Scanning, which accounts for 22% of the exam.

Reconnaissance is the phase where professional testers distinguish themselves. A well-executed recon phase produces a detailed map of the target's attack surface, enabling focused and efficient testing. A rushed recon phase leads to missed vulnerabilities and wasted effort in later phases.

**Legal and Ethical Reminder:** Reconnaissance — even passive techniques — must be conducted only against systems and organizations you are explicitly authorized to test. Written authorization defining scope is required before beginning any recon activity. Unauthorized reconnaissance may violate the Computer Fraud and Abuse Act (CFAA) and similar laws.

---

## 1. Passive vs. Active Reconnaissance

### Definitions

**Passive Reconnaissance** collects intelligence without directly interacting with the target's systems. The target cannot detect you because you are not generating traffic against their infrastructure. Sources include public search engines, cached data, third-party databases, and public records.

**Active Reconnaissance** involves direct interaction with target systems. DNS queries to target name servers, port scanning, banner grabbing, and web crawling are active techniques. These generate log entries on the target and can trigger IDS/IPS alerts. Active recon requires confirmed written authorization.

### Comparison Table

| Characteristic | Passive Recon | Active Recon |
|----------------|--------------|-------------|
| Target interaction | None | Direct |
| Detectability | Undetectable | Generates logs |
| Authorization required | Yes (for target) | Yes (explicitly) |
| Example tools | Shodan, theHarvester | Nmap, Nikto |
| Data freshness | May be cached/stale | Real-time |
| PenTest+ domain | Info Gathering | Info Gathering + Scanning |

---

## 2. OSINT Techniques and Tools

### Google Dorking (Google Hacking)

Google advanced search operators find publicly indexed but obscure information. The Google Hacking Database (GHDB) at Exploit-DB catalogs proven dorks by category.

| Operator | Syntax | Use Case |
|----------|--------|---------|
| `site:` | `site:example.com` | Restrict to one domain |
| `filetype:` | `filetype:pdf` | Find specific file types |
| `inurl:` | `inurl:admin` | URL contains keyword |
| `intitle:` | `intitle:"index of"` | Page title contains phrase |
| `intext:` | `intext:"password"` | Page body contains text |
| `cache:` | `cache:example.com` | Google's cached copy |

### theHarvester

Primary use: email harvesting and subdomain enumeration against multiple OSINT sources simultaneously.

```bash
# Single source
theHarvester -d example.com -b google

# Multiple sources with output file
theHarvester -d example.com -b bing,linkedin,twitter -l 500 -f report.html

# All available sources
theHarvester -d example.com -b all -l 200
```

Key options:

| Flag | Meaning |
|------|---------|
| `-d` | Target domain |
| `-b` | Data source(s) |
| `-l` | Limit number of results |
| `-f` | Output file (html or xml) |
| `-s` | Start result number |

### Shodan

Shodan indexes internet-connected device banners. It is passive from the tester's perspective — you query Shodan's database, not the target.

```text
hostname:example.com
org:"Example Corp"
net:203.0.113.0/24
port:3389 country:US
product:"Apache httpd" version:"2.4.49"
vuln:CVE-2021-44228
ssl:"example.com"
```

Shodan reveals: open ports, software versions, SSL certificates, geographic distribution, and Internet of Things devices with default credentials.

### Maltego

Maltego performs graphical link analysis using transforms. Each transform queries one data source and returns related entities.

Common transform chains:

- Domain → DNS → IP Addresses → Netblocks → Organizations
- Domain → Email Addresses → People → Social Profiles
- IP Address → Autonomous System → Organization

Editions: Community (free, rate-limited), Pro, and Enterprise.

---

## 3. DNS Enumeration

### DNS Record Types Reference

| Record Type | Full Name | Information Revealed |
|-------------|-----------|---------------------|
| A | Address | Hostname to IPv4 mapping |
| AAAA | IPv6 Address | Hostname to IPv6 mapping |
| MX | Mail Exchange | Mail server hostnames and priority |
| NS | Name Server | Authoritative DNS servers |
| TXT | Text | SPF, DKIM, verification tokens, internal info |
| CNAME | Canonical Name | Aliases; reveals internal naming conventions |
| SOA | Start of Authority | Primary NS, admin email, zone serial |
| PTR | Pointer | Reverse DNS — IP to hostname |
| SRV | Service | Service location records (VoIP, LDAP, etc.) |

### DNS Enumeration Commands

```bash
# Basic lookups
nslookup example.com
host example.com
dig example.com ANY

# Record-specific queries
dig example.com MX
dig example.com NS
dig example.com TXT
dig example.com SOA

# Reverse lookup
dig -x 203.0.113.10

# Zone transfer (AXFR) — active, requires authorization
dig axfr @ns1.example.com example.com
host -t axfr example.com ns1.example.com
```

### Subdomain Enumeration Tools

```bash
# Sublist3r — passive subdomain discovery
sublist3r -d example.com -o subs.txt

# Amass — passive mode (no direct target contact)
amass enum -passive -d example.com

# Amass — active mode (DNS brute force — requires authorization)
amass enum -active -d example.com -brute

# DNSrecon
dnsrecon -d example.com -t std
dnsrecon -d example.com -t axfr
```

---

## 4. WHOIS and Certificate Transparency

### WHOIS Lookups

```bash
whois example.com
whois 203.0.113.0
```

WHOIS reveals: registrar, registration and expiration dates, name servers, and sometimes registrant contact information. Historical WHOIS data is available through services such as ViewDNS.info and DomainTools.

### Certificate Transparency Logs

Every publicly trusted TLS certificate is logged in Certificate Transparency logs. Querying [crt.sh](https://crt.sh) reveals all subdomains that have had certificates issued:

```text
https://crt.sh/?q=%.example.com
```

This surfaces development, staging, and internal subdomains that were accidentally exposed, even if they are no longer in DNS.

---

## 5. Social Media and People OSINT

### LinkedIn Intelligence

LinkedIn provides:

- Employee names, titles, and organizational hierarchy
- Technology stack clues from job postings and skills sections
- Contractor and vendor relationships
- Recent organizational changes (hiring, departures)

### GitHub and Source Code Repositories

GitHub is a critical OSINT source because developers accidentally commit secrets.

```bash
# Trufflehog — scans git history for high-entropy strings and known patterns
trufflehog github --org=examplecorp

# gitleaks — secret detection
gitleaks detect --source=/path/to/repo
```

Common accidental exposures: API keys, OAuth tokens, database connection strings, private keys, internal IP addresses, and architecture documentation.

### Email Format Discovery

Knowing one employee's email reveals the format for all employees. Common formats:

```text
firstname.lastname@company.com
f.lastname@company.com
firstnamelastname@company.com
flastname@company.com
```

Tools: Hunter.io, Clearbit, and Phonebook.cz.

---

## 6. Passive DNS and Historical Intelligence

### Passive DNS Sources

| Tool | Type | Key Features |
|------|------|-------------|
| SecurityTrails | Commercial | Full WHOIS history, passive DNS, subdomains |
| VirusTotal | Free/Commercial | Passive DNS, related domains, file/URL analysis |
| RiskIQ PassiveTotal | Commercial | Professional passive DNS, threat intel |
| Shodan | Free/Commercial | Banners, historical data, certificates |
| Wayback Machine | Free | Historical website snapshots |

Historical website snapshots at archive.org can reveal former technology stacks, employee information, and accidentally published internal content.

---

## 7. Reconnaissance Methodology Flowchart

```text
START: Confirm Written Authorization + Define Scope
         |
         v
Passive OSINT Phase
  - WHOIS + cert transparency
  - Shodan + theHarvester
  - LinkedIn + GitHub
  - Google dorks
  - Wayback Machine
         |
         v
DNS Intelligence
  - Record enumeration (A, MX, NS, TXT, CNAME)
  - Subdomain discovery (passive)
  - Zone transfer check (if authorized)
         |
         v
People Intelligence
  - Employee list + email format
  - Org hierarchy
  - Technology stack from job postings
         |
         v
Document All Findings (Source + Timestamp)
         |
         v
Reconnaissance Report → Input to Scanning Phase
```

---

## 8. PenTest+ Exam Tips

- **Domain weight**: Information Gathering is 22% of PT0-002. Expect multiple questions on recon tools and techniques.

- **Passive vs. Active distinction**: The exam frequently presents scenarios and asks you to classify the technique. Key rule: if you touch the target's systems, it is active.

- **Tool identification questions**: Know what each tool does — Shodan (internet device search), theHarvester (email/subdomain), Maltego (link analysis/visualization), Recon-ng (modular recon framework).

- **DNS record types**: Expect questions asking which record type reveals mail servers (MX), which reveals aliases (CNAME), and which contains SPF data (TXT).

- **Zone transfers**: AXFR is a misconfiguration; it returns the complete DNS zone. Know that this is active recon and requires authorization.

- **Google dork operators**: `site:`, `filetype:`, `inurl:`, `intitle:`, `intext:` — know the syntax and use case for each.

- **Legal boundary**: The exam tests that students know passive recon against unauthorized targets is still potentially illegal depending on jurisdiction and use of findings.

- **Recon-ng**: A modular Python recon framework similar in concept to Metasploit. Modules gather OSINT from various sources. The exam may reference it as an alternative to theHarvester.

---

## 9. Legal and Ethical Framework

All reconnaissance activities in this course occur within the following boundaries:

- Written authorization defines the target scope before any activity begins
- Passive recon tools used against live targets outside the course lab require explicit authorization
- Data collected about individuals is handled per applicable privacy laws
- Findings are disclosed responsibly per the engagement's rules of engagement
- No reconnaissance tools are used against systems outside the authorized lab environment

Unauthorized reconnaissance may violate: Computer Fraud and Abuse Act (18 U.S.C. § 1030), Electronic Communications Privacy Act, state computer crime laws, and foreign equivalents.

---

## 10. Study Checklist

- [ ] Explain the difference between passive and active reconnaissance with examples of each
- [ ] Demonstrate Google dork syntax for at least three operator types
- [ ] Run theHarvester against an authorized domain and interpret the output
- [ ] Perform DNS enumeration using `dig` and identify at least five record types
- [ ] Describe what Shodan indexes and three types of information it reveals
- [ ] Explain how Certificate Transparency logs enable subdomain discovery
- [ ] Identify two risks of accidental GitHub exposure and the tools used to find them
- [ ] Complete the Module 05 lab activity in the authorized lab environment
- [ ] Review the PT0-002 exam objectives for Domain 2 prior to the quiz

---

---

## 11. Supplemental Resources

**1. theHarvester — Official GitHub Repository and Documentation**
[https://github.com/laramies/theHarvester](https://github.com/laramies/theHarvester)
The official theHarvester repository includes usage documentation, supported data sources, and API key configuration. Reading the source documentation ensures accurate understanding of what each `-b` source collects and how to interpret output — directly applicable to Module 05 lab work.

**2. OSINT Framework — Categorized Intelligence Tool Directory**
[https://osintframework.com/](https://osintframework.com/)
A comprehensive tree of OSINT tools organized by target type (username, email, domain, IP, social networks). Reviewing the DNS and domain branches reinforces the passive reconnaissance tool landscape covered in Module 05 and introduces additional professional resources beyond the core tools.

**3. Hunter.io — Email Format Discovery and Verification**
[https://hunter.io/](https://hunter.io/)
Hunter.io allows testers to identify the email format used by an organization and verify whether specific email addresses are publicly known. The free tier supports a limited number of queries suitable for lab exercises, directly illustrating the email format discovery concepts covered in Module 05 Section 5.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**

# Video Script: Module 05 — Reconnaissance and OSINT

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

### SLIDE 1 — Introduction (0:00–1:00)

Welcome back to CIS-4333 Penetration Testing. I am Professor Nash, and this is Module 05: Reconnaissance and OSINT.

Before we dive in, the standard reminder: everything we discuss in this course applies exclusively to authorized engagements. You must have written permission before conducting any reconnaissance against a target. We will be practicing in sandboxed lab environments only.

Today we cover one of the most critical phases of any penetration test — the reconnaissance phase. This is where skilled testers spend the majority of their time. The more you know about a target before you ever touch a keyboard, the more effective and focused your testing will be.

By the end of this module you will understand the difference between passive and active reconnaissance, apply core OSINT tools, perform DNS enumeration, and leverage social media intelligence — all within the scope of a professional engagement.

---

### SLIDE 2 — Reconnaissance Overview (1:00–2:30)

Reconnaissance maps to the first phase of the penetration testing lifecycle as defined by CompTIA PenTest+. It feeds directly into scoping and planning, and the intelligence you gather here shapes every phase that follows.

There are two primary categories.

**Passive Reconnaissance** — gathering information without directly interacting with the target's systems. You are using public sources, cached data, and third-party services. The target has no way to detect you because you are not touching their infrastructure.

**Active Reconnaissance** — directly interacting with target systems. Port scanning, banner grabbing, DNS zone transfers. This generates logs. The target can detect you. This is why active recon only happens after written authorization is confirmed.

Think of it this way: passive recon is like reading everything publicly written about a company. Active recon is walking up and knocking on their doors and windows.

---

### SLIDE 3 — The OSINT Framework (2:30–4:00)

OSINT stands for Open Source Intelligence. It is the practice of collecting information from publicly available sources to build a profile of a target organization.

The OSINT Framework at osintframework.com provides a visual map of hundreds of tools and techniques organized by information type. It covers:

- Username lookups
- Email addresses
- Domain and IP intelligence
- People searches
- Social networks
- Public records

For the PenTest+ exam, you need to know the major OSINT categories and representative tools. In professional practice, you use a combination based on the engagement scope.

Key principle: document everything. Every piece of intelligence you gather goes into your notes with the source and timestamp. This becomes part of your deliverable.

---

### SLIDE 4 — Google Dorking (4:00–5:30)

Google dorking, also called Google hacking, uses advanced search operators to find information that is technically public but not easily discoverable through normal search.

Common operators:

```text
site:targetcompany.com filetype:pdf
site:targetcompany.com inurl:admin
intitle:"index of" site:targetcompany.com
intext:"password" site:targetcompany.com
filetype:xls site:targetcompany.com "employee"
cache:targetcompany.com
```

The Google Hacking Database, known as GHDB, maintained by Exploit-DB, catalogs thousands of dorks organized by category: files containing passwords, sensitive directories, error messages, vulnerable servers, and more.

Practical example: searching for `filetype:pdf site:university.edu "confidential"` might surface documents that were accidentally indexed. This is entirely passive — you are querying Google's index, not the target's servers.

Important: even though you are only querying Google, always stay within your authorized scope. Do not use dorks to gather information about systems outside your engagement scope.

---

### SLIDE 5 — theHarvester (5:30–7:00)

theHarvester is one of the most widely used OSINT tools for email harvesting and subdomain enumeration. It queries multiple public data sources simultaneously.

Basic syntax:

```bash
theHarvester -d targetcompany.com -b google
theHarvester -d targetcompany.com -b bing,linkedin,twitter
theHarvester -d targetcompany.com -b all -l 500 -f output.html
```

The `-d` flag specifies the target domain. `-b` specifies the source — google, bing, linkedin, twitter, shodan, censys, and many more. `-l` limits results. `-f` exports to file.

What it finds:

- Email addresses (useful for phishing simulations if in scope)
- Subdomain names
- IP addresses
- Employee names from LinkedIn
- Virtual hosts

On the PenTest+ exam, remember that theHarvester is classified as a passive OSINT tool when it queries third-party sources like Google. It becomes semi-active when it performs direct DNS lookups.

---

### SLIDE 6 — Shodan (7:00–8:30)

Shodan is a search engine for internet-connected devices. While Google indexes websites, Shodan indexes banners — the information that services broadcast when you connect to them. It scans the entire internet continuously and stores what it finds.

Searching Shodan:

```text
hostname:targetcompany.com
org:"Target Company Inc"
net:203.0.113.0/24
port:22 org:"Target Company"
product:"Apache httpd" version:"2.4.49"
vuln:CVE-2021-44228
```

What Shodan reveals about a target:

- Open ports and services across all their public IP space
- Software versions from banners
- Geographic location of servers
- SSL certificate information, including internal hostnames that leak
- Default credentials on IoT devices
- Exposed industrial control systems

Shodan is entirely passive from your perspective — you are querying Shodan's database, not the target. A basic free account returns limited results. Professional accounts and the API provide much deeper access.

---

### SLIDE 7 — Maltego (8:30–10:00)

Maltego is a graphical link analysis tool for visualizing relationships between entities — people, organizations, domains, IP addresses, email addresses, phone numbers, and more.

It works through transforms — automated queries that take one piece of information and return related entities. For example:

- Start with a domain name
- Run transform "DNS to IP" to get IP addresses
- Run transform "IP to Netblock" to get the network range
- Run transform "Domain to Email" to get associated email addresses
- Run transform "Email to Person" to connect to LinkedIn profiles

The power of Maltego is visualization. Complex relationships that would take hours to map manually are displayed as a graph in minutes.

Maltego Community Edition is free with rate limits. Maltego Pro and commercial transforms provide access to premium data sources including VirusTotal, Shodan, HaveIBeenPwned, and threat intelligence feeds.

For PenTest+, understand that Maltego is used in the planning and reconnaissance phase, and that transforms represent individual OSINT queries to specific data sources.

---

### SLIDE 8 — DNS Enumeration (10:00–12:00)

DNS enumeration is the process of extracting DNS records to map an organization's infrastructure. Even passively, DNS records reveal a great deal.

Key DNS record types:

| Record | Purpose | Pentest Value |
|--------|---------|---------------|
| A | Domain to IPv4 | Maps hostnames to IPs |
| AAAA | Domain to IPv6 | IPv6 infrastructure |
| MX | Mail servers | Email infrastructure |
| NS | Name servers | DNS infrastructure |
| TXT | Text records | SPF, DKIM, internal info |
| CNAME | Aliases | Reveals internal naming |
| SOA | Zone authority | Admin contact, serial |
| PTR | Reverse DNS | IP to hostname |

Command-line DNS lookups:

```bash
# Basic lookups
nslookup targetcompany.com
host targetcompany.com
dig targetcompany.com ANY

# Specific record types
dig targetcompany.com MX
dig targetcompany.com TXT
dig targetcompany.com NS

# Zone transfer attempt (active — requires written authorization)
dig axfr @ns1.targetcompany.com targetcompany.com
```

DNS zone transfers (AXFR) are a legacy mechanism that, if misconfigured, returns the complete DNS zone — every hostname, IP, and record. This is active reconnaissance. Many organizations still have this misconfiguration on internal DNS servers.

Sublist3r and Amass are dedicated subdomain enumeration tools:

```bash
sublist3r -d targetcompany.com -o subdomains.txt
amass enum -passive -d targetcompany.com
amass enum -active -d targetcompany.com
```

The `-active` flag on Amass performs DNS brute-forcing — this is active recon and requires written authorization.

---

### SLIDE 9 — WHOIS and Certificate Transparency (12:00–13:30)

WHOIS records provide registration information for domains and IP address blocks. Even with privacy protection, WHOIS can reveal:

- Registrar and registration date
- Name servers
- Registrant contact information in some cases
- Historical WHOIS through services like ViewDNS.info

```bash
whois targetcompany.com
whois 203.0.113.45
```

Certificate Transparency logs are a goldmine for subdomain discovery. Every SSL/TLS certificate issued by a public CA is logged. The site [crt.sh](https://crt.sh) searches these logs:

```text
https://crt.sh/?q=%.targetcompany.com
```

This returns every subdomain that has ever had a certificate issued — including development, staging, and internal subdomains that may have been accidentally exposed to the internet.

---

### SLIDE 10 — Social Media OSINT (13:30–15:30)

Social media is one of the richest sources of intelligence for a penetration tester. People post information that individually seems harmless but collectively reveals significant vulnerabilities.

**LinkedIn** — organizational structure, employee names, job titles, technologies used. Job postings say things like "looking for a Python developer with AWS and Splunk experience" — that reveals the technology stack. LinkedIn also reveals the hierarchy: who reports to whom, recent hires, and contractors.

**Twitter/X and Facebook** — employees often post about work, conference attendance, and photos of workspaces that might show whiteboards with internal project names or network diagrams.

**GitHub and GitLab** — this one is critical. Developers frequently accidentally commit:

- API keys and tokens
- Database passwords in configuration files
- Internal IP addresses and hostnames
- Private code that reveals application architecture

Tools for GitHub OSINT:

```bash
# Trufflehog — scans commit history for secrets
trufflehog github --org=targetcompany

# gitleaks
gitleaks detect --source=. --report-path=gitleaks.json
```

**Job postings** — perhaps the most underrated source. A job posting for a "Senior Network Engineer with Cisco ASA and Palo Alto experience" tells you exactly what firewall products they run.

---

### SLIDE 11 — People OSINT (15:30–17:00)

Individual employee information is valuable for social engineering assessments when explicitly in scope. Key data points to gather:

- Full name and professional title
- Email address format (first.last@company.com? f.last@company.com?)
- Phone number from email signatures or conference presentations
- Physical location, office, city
- Technical skills from LinkedIn and GitHub profiles
- Conference presentations on YouTube and SlideShare

Tools for people OSINT:

- **Hunter.io** — finds and verifies email addresses by domain
- **Clearbit** — enriches email addresses with company and social data
- **HaveIBeenPwned** — checks if an email appears in breach data

Understanding the email format is particularly important. If you find one employee's email, you know the format for all employees. Combined with the employee list from LinkedIn, you can construct a comprehensive target list for a phishing simulation — if social engineering is explicitly authorized in your scope.

---

### SLIDE 12 — Passive DNS and Historical Data (17:00–18:30)

Passive DNS databases store historical DNS query data. This reveals:

- What IP addresses a domain pointed to in the past
- Domains that shared an IP address
- Infrastructure that may have been retired but is still accessible

Tools:

- **SecurityTrails** — comprehensive passive DNS, WHOIS history, subdomains
- **VirusTotal** — search by domain or IP, shows passive DNS and related domains
- **RiskIQ/PassiveTotal** — professional passive DNS platform

The Wayback Machine at archive.org stores snapshots of websites going back decades. Old versions of websites can reveal:

- Former employee names and contact info
- Technology stack information
- Internal links and directory structure
- Content that was meant to be private but was briefly public

---

### SLIDE 13 — Building the Reconnaissance Report (18:30–20:00)

All intelligence gathered during reconnaissance must be documented. The recon report typically includes:

1. Scope summary — domains, IP ranges, and business units in scope
2. Network footprint — IP ranges, ASNs, hosting providers
3. Subdomain inventory — all discovered subdomains with resolution status
4. DNS records — complete DNS inventory
5. Email addresses — format identified and addresses discovered
6. Employee information — names, titles, organizational structure
7. Technology stack — web server, frameworks, software versions observed
8. Potential attack vectors — exposed services and interesting findings
9. Source documentation — where each piece of intelligence came from

This report feeds directly into the scanning and exploitation phases. Every finding should be traceable to its source.

---

### SLIDE 14 — PenTest+ Exam Alignment (20:00–21:30)

For the PT0-002 exam, focus on these areas from today's module.

The exam tests your ability to distinguish passive versus active reconnaissance. Know that passive recon does not touch the target directly while active recon does.

Know the primary tools: Shodan, theHarvester, Maltego, and what each is specifically used for.

DNS record types are tested — know A, MX, NS, TXT, CNAME, and what information each reveals.

Google dork operators are tested: site, filetype, inurl, intitle, intext.

OSINT categories tested: people, organizations, infrastructure, credentials. Know which tools apply to each category.

Legal and ethical constraints: reconnaissance requires written authorization even when using passive techniques against a target you do not own.

---

### SLIDE 15 — Closing and Lab Preview (21:30–22:30)

To summarize Module 05: reconnaissance and OSINT is the foundation of every successful penetration test. The information you gather here determines the quality of everything that follows.

Key takeaways:

- Passive recon does not touch target systems; active recon does
- OSINT tools like Shodan, theHarvester, and Maltego are force multipliers
- DNS enumeration reveals the entire network surface
- Social media and GitHub are rich intelligence sources
- Every finding must be documented with source and timestamp
- Written authorization is required before any reconnaissance on a target you do not own

In the lab for this module, you will use theHarvester, perform DNS enumeration, and practice Google dorking — all against authorized targets in our course lab environment.

In Module 06, we move into active scanning with Nmap and enumeration tools. See you there.

---

### End of Module 05 Video Script

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**

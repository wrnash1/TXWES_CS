# Video Script: Module 03 - OSINT and Passive Reconnaissance

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Estimated Duration:** 20-24 minutes
**Professor:** Nash

---

## Pre-Recording Checklist

- [ ] Title slide loaded: "Module 03 - OSINT and Passive Reconnaissance"
- [ ] Browser tabs open: WHOIS lookup, Shodan, Google search
- [ ] Terminal window ready for theHarvester and Maltego demos
- [ ] Reminder on screen: all demos use fictional or publicly consented targets only

---

## [00:00 - 01:30] Opening

**[SLIDE: Module 03 — OSINT and Passive Reconnaissance]**

Welcome back to CIS-4333. I'm Professor Nash. Modules 01 and 02 covered the pre-engagement phase — the documents, the legal framework, and the ethical obligations. Now we move into Phase 2 of the penetration testing methodology: information gathering and reconnaissance.

Module 03 is focused entirely on passive reconnaissance — specifically, Open Source Intelligence, or OSINT. Passive reconnaissance means gathering information about a target without directly interacting with their systems. You use publicly available sources, you leave no fingerprints on the target's servers, and you build a comprehensive picture of the target's attack surface before you ever send a single packet their way.

By the end of this module you will be able to:

- Define OSINT and explain its role in the penetration testing methodology
- Use WHOIS, DNS enumeration, and certificate transparency logs as reconnaissance sources
- Apply Google dorking techniques to discover exposed information
- Describe theHarvester and its role in email and subdomain discovery
- Identify social media, job postings, and LinkedIn as OSINT sources
- Explain why passive reconnaissance is valuable even when active scanning is authorized

---

## [01:30 - 04:30] What Is OSINT and Why Does It Matter?

**[SLIDE: OSINT Definition and Value]**

Open Source Intelligence — OSINT — is the collection and analysis of information from publicly available sources. "Open source" in this context does not mean open-source software. It means information that is openly available to anyone without authorization, hacking, or special access.

OSINT sources include:

- Domain registration records (WHOIS)
- DNS records (A, MX, NS, TXT, CNAME, SPF, DMARC)
- SSL/TLS certificate transparency logs
- Search engine results and cached pages
- Social media profiles (LinkedIn, Twitter, GitHub)
- Job postings and company websites
- Shodan and Censys — search engines for internet-facing devices
- Public code repositories (GitHub, GitLab, Bitbucket)
- Government records, court filings, and SEC disclosures

**[SLIDE: Why Passive Reconnaissance First?]**

There are two powerful reasons to lead with passive reconnaissance.

First: it is invisible to the target. No packets are sent to the target's systems. Their intrusion detection systems see nothing. Their firewall logs show nothing. This makes passive recon the safest phase for the tester — no risk of triggering alerts, no risk of accidentally disrupting services, no risk of exceeding scope.

Second: it builds your map before you start driving. The information gathered in passive reconnaissance directly shapes your active scanning and exploitation strategy. If WHOIS reveals the target recently transferred their domain, that is interesting. If LinkedIn reveals the CTO's email address format, that is useful for credential guessing. If Shodan shows an internet-facing device running a two-year-old firmware version, that is a potential target.

Professional penetration testers never skip passive reconnaissance. Skipping it means going into active scanning blind, which wastes time and misses context.

---

## [04:30 - 08:30] WHOIS, DNS, and Certificate Transparency

**[SLIDE: WHOIS and DNS Enumeration]**

Let's walk through the most fundamental passive reconnaissance sources.

### WHOIS

WHOIS is a protocol that returns registration information for domain names and IP address blocks. For a domain like `example.com`, a WHOIS query returns the registrant name and organization, the registrant's email address (when not privacy-protected), the registrar, creation and expiration dates, and the name servers.

For penetration testing, WHOIS is useful for:

- Identifying the organization's legal name and corporate structure
- Finding the registrant email format (e.g., `admin@example.com`) which may reveal email naming conventions
- Noting domain expiration dates (an expiring domain is a hijacking risk)
- Identifying the authoritative name servers (targets for DNS enumeration)

**[SHOW TERMINAL]**

A simple WHOIS lookup from the command line looks like this. Note: this example uses a public domain for illustration in an authorized educational context.

```text
whois example.com

Domain Name: EXAMPLE.COM
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
Registrar: RESERVED-Internet Assigned Numbers Authority
Created: 1995-08-14
Updated: 2023-08-14
Expiry: 2024-08-13
Name Server: A.IANA-SERVERS.NET
Name Server: B.IANA-SERVERS.NET
DNSSEC: signedDelegation
```

In a real engagement, you would look for the registrant contact details, organizational structure clues, and the name servers you will query next.

### DNS Enumeration

DNS records reveal a tremendous amount about an organization's infrastructure. Key record types to query:

- **A records**: map hostnames to IPv4 addresses — reveals server IPs
- **AAAA records**: map hostnames to IPv6 addresses
- **MX records**: identify mail servers — useful for phishing simulation scope
- **NS records**: identify authoritative name servers
- **TXT records**: often contain SPF, DKIM, DMARC, and sometimes verification tokens that reveal third-party services in use
- **CNAME records**: aliases that may reveal internal naming conventions or third-party hosting relationships

**[SHOW TERMINAL]**

```text
nslookup -type=MX example.com
dig ANY example.com
host -a example.com
```

DNS zone transfers are an older vulnerability — if a name server is misconfigured to allow any host to request a full zone transfer, you receive all DNS records for the domain in one query. Modern configurations restrict zone transfers, but it is still worth attempting.

```text
dig axfr @ns1.example.com example.com
```

### Certificate Transparency Logs

Every SSL/TLS certificate issued by a public Certificate Authority is logged in publicly accessible Certificate Transparency logs. This is a gold mine for subdomain enumeration. Sites like `crt.sh` allow you to query all certificates ever issued for a domain, revealing subdomains that may not be published in DNS or linked from the main website.

**[SHOW TERMINAL]**

Querying crt.sh via the command line:

```text
curl -s "https://crt.sh/?q=%.example.com&output=json" | python3 -m json.tool | grep name_value
```

This returns every subdomain that has ever had a certificate issued — including staging environments, development servers, and forgotten legacy systems that may still be running.

---

## [08:30 - 12:00] Google Dorking

**[SLIDE: Google Dorking — Advanced Search Operators]**

Google dorking is the use of advanced Google search operators to find specific types of information that a target has inadvertently exposed. This is entirely passive — you are querying Google, not the target's servers directly.

Key Google search operators for OSINT:

- `site:example.com` — limits results to a specific domain; use to map exposed pages
- `filetype:pdf site:example.com` — finds exposed documents of a specific type
- `inurl:admin site:example.com` — finds pages with "admin" in the URL
- `intitle:"index of" site:example.com` — finds open directory listings
- `"internal use only" site:example.com` — finds documents labeled for internal use that were indexed publicly
- `ext:env OR ext:config site:example.com` — finds exposed configuration files

**[SLIDE: What Google Dorking Finds]**

In real-world penetration tests, Google dorking has revealed:

- Exposed `.git` directories containing full source code
- Configuration files with database credentials
- Employee HR documents uploaded to public web servers
- Network diagrams and architecture documentation
- Internal wikis accidentally exposed to the internet
- Login portals for administrative interfaces

This information is publicly accessible. You are not hacking anything to retrieve it. But it tells you exactly where to look when active testing begins. The Google Hacking Database — GHDB — maintained by Offensive Security is a repository of thousands of documented Google dork queries organized by category. It is a standard resource for penetration testers.

---

## [12:00 - 15:30] theHarvester and Social Media OSINT

**[SLIDE: theHarvester — Email and Subdomain Discovery]**

theHarvester is a pre-installed tool in Kali Linux that automates the collection of email addresses, subdomains, hosts, employee names, and open ports from multiple public sources. It queries sources including search engines, PGP key servers, Shodan, LinkedIn, and certificate transparency logs.

**[SHOW TERMINAL]**

In the authorized lab environment, theHarvester is used like this:

```text
theHarvester -d example.com -b google,linkedin,shodan -l 500
```

The `-d` flag specifies the target domain. The `-b` flag specifies the data sources. The `-l` flag limits the number of results per source. Output includes discovered email addresses, subdomains, hostnames, and virtual hosts.

Email addresses are particularly valuable because they reveal:

- The email naming convention (firstname.lastname, first initial last name, etc.)
- Which employees are publicly associated with the organization
- Potential targets for phishing simulation (if authorized in the RoE)

### Social Media OSINT

LinkedIn is one of the most valuable OSINT sources for penetration testers. Employee profiles reveal:

- Technology stack (job postings and employee skills sections reference specific software, frameworks, and tools)
- Organizational structure (who reports to whom; who are the IT and security staff)
- Recent hires and departures (new employees are frequently targeted in social engineering)
- Office locations and physical addresses

Job postings are equally valuable. A job posting for "Senior AWS Engineer with experience in Kubernetes and Terraform" tells you the organization runs AWS with Kubernetes orchestration managed by Terraform. That is infrastructure intelligence.

GitHub is another critical source. Developers often accidentally commit credentials, API keys, internal IP addresses, and configuration files to public repositories. Tools like `trufflehog` and `gitrob` automate the search for secrets in public repositories.

---

## [15:30 - 18:30] Shodan — The Search Engine for Devices

**[SLIDE: Shodan — Internet-Connected Device Discovery]**

Shodan is a search engine that indexes internet-connected devices — not web pages. Shodan crawls the internet, connects to ports, grabs banners, and indexes the results. You can search Shodan for devices matching specific criteria: open port 22 with SSH running a specific version, cameras running a specific firmware, industrial control systems with publicly exposed web interfaces.

For penetration testing, Shodan is used to:

- Find internet-facing systems belonging to the target organization (search by organization name or IP range)
- Identify outdated software versions (banner grabbing reveals version strings)
- Discover exposed services that should not be internet-facing (database ports, administrative interfaces, industrial control panels)
- Identify the ASN (Autonomous System Number) and IP ranges associated with the target organization

**[SHOW TERMINAL]**

Shodan search examples (used against authorized targets in lab environments only):

```text
Shodan query: org:"Target Organization Name"
Shodan query: net:203.0.113.0/24
Shodan query: hostname:example.com port:22
```

Shodan provides this data passively from their own crawls — you are querying Shodan's database, not touching the target's systems.

---

## [18:30 - 21:00] Organizing OSINT — Maltego and Documentation

**[SLIDE: Maltego — Visualizing OSINT Relationships]**

Maltego is a graphical link analysis tool that visualizes relationships between OSINT data points. You can input a domain and Maltego will automatically run transforms — queries against multiple data sources — to discover associated email addresses, subdomains, IP addresses, phone numbers, and social profiles, displayed as a connected graph.

For large engagements, Maltego helps you see patterns that are not obvious when looking at flat lists. An employee whose email address links to a GitHub account that contains commits with a personal email and home IP address is a chain of relationships that Maltego visualizes clearly.

### Documentation During Passive Reconnaissance

Everything found during passive reconnaissance must be documented. Create a reconnaissance notes file with:

- Date and time of each query
- Tool or source used
- Query executed
- Results obtained
- Analysis notes (what does this finding suggest?)

This documentation feeds directly into your reconnaissance report section and provides the evidential basis for your active scanning plan.

---

## [21:00 - 23:00] Exam Tips and Summary

**[SLIDE: PT0-002 Exam Tips — Module 03]**

Key exam tips for this module:

First: passive reconnaissance does not touch the target's systems. If a question describes the tester interacting with target servers, sending packets, or running scans — that is active reconnaissance, not passive.

Second: WHOIS, DNS enumeration, certificate transparency, Google dorking, Shodan, theHarvester, LinkedIn, and GitHub are all passive OSINT sources and tools. Know them all.

Third: the value of passive reconnaissance is intelligence for active scanning. The exam may ask you to identify what passive recon revealed and how that shapes the next phase.

Fourth: Google dorking uses advanced search operators against Google's index. You are not touching the target's systems directly.

Fifth: Shodan indexes internet-connected devices passively. Querying Shodan is passive reconnaissance.

For additional study, visit **professormesser.com** and review the official PT0-002 objectives at **comptia.org**.

---

## [23:00 - 24:00] Closing

In Module 04 we move into active reconnaissance — specifically using Nmap for port scanning and service enumeration. You will send actual packets to target systems, so authorization must be fully in place before you begin.

Complete your quiz and lab, contribute to the discussion, and I'll see you in Module 04.

---

*All demonstrations are performed in authorized, isolated lab environments. No OSINT techniques demonstrated should be directed at organizations without explicit written authorization.*

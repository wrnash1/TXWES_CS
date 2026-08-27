# Reading Guide: Module 03 - OSINT and Passive Reconnaissance

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash

---

## Introduction

Module 03 covers passive reconnaissance — the information-gathering phase where a penetration tester builds a detailed picture of the target's attack surface using only publicly available sources. No packets are sent to target systems. No fingerprints are left on their servers. Done well, passive reconnaissance shapes every subsequent phase of the engagement and often reveals high-value attack vectors before a single exploit is attempted.

Passive reconnaissance maps to the **Information Gathering and Reconnaissance** phase of the PT0-002 methodology. The exam tests both the conceptual distinction between passive and active reconnaissance and the practical knowledge of specific OSINT tools and techniques.

---

## Section 1: Core Vocabulary

### Definitions You Must Know

**OSINT (Open Source Intelligence):** The collection and analysis of information from publicly available sources. "Open source" refers to the availability of the information — not open-source software. OSINT sources require no special access, hacking, or authorization, making OSINT gathering inherently passive.

**Passive Reconnaissance:** Information gathering that does not directly interact with the target's systems. The tester queries third-party sources — search engines, domain registries, certificate logs — that may hold information about the target without touching target infrastructure.

**Active Reconnaissance:** Information gathering that directly interacts with target systems — sending packets, initiating connections, running scans. Requires authorization and leaves traces in the target's logs. Covered in Module 04.

**WHOIS:** A query-response protocol that returns registration information for domain names and IP address blocks, including registrant details, registrar, creation and expiration dates, and authoritative name servers.

**DNS Enumeration:** The process of querying DNS records to map a target's infrastructure. Record types include A (IPv4), AAAA (IPv6), MX (mail servers), NS (name servers), TXT (SPF/DKIM/DMARC), CNAME (aliases), and PTR (reverse lookup).

**Zone Transfer (AXFR):** A DNS operation that replicates all records in a zone from a primary to a secondary name server. Misconfigured servers that allow zone transfers from any host leak all DNS records in a single query — a significant reconnaissance vulnerability.

**Certificate Transparency (CT) Logs:** Public, append-only logs of all SSL/TLS certificates issued by participating Certificate Authorities. Querying CT logs via tools such as `crt.sh` reveals subdomains that have ever had certificates issued, including staging and development systems.

**Google Dorking:** The use of advanced Google search operators to find specific types of information inadvertently exposed and indexed by Google. Operators include `site:`, `filetype:`, `inurl:`, `intitle:`, and `ext:`. The technique is passive — the tester queries Google, not target systems.

**Google Hacking Database (GHDB):** A repository maintained by Offensive Security containing thousands of documented Google dork queries organized by category. A standard reference for passive reconnaissance.

**theHarvester:** A Kali Linux tool that automates OSINT collection by querying Google, Bing, LinkedIn, Shodan, certificate transparency logs, and PGP key servers to discover email addresses, subdomains, hostnames, and employee names associated with a target domain.

**Shodan:** A search engine that indexes internet-connected devices by crawling ports and capturing service banners. Used to discover internet-facing assets, identify outdated software versions, and find exposed services that should not be publicly accessible.

**Maltego:** A graphical link analysis and data visualization tool that automates OSINT transforms and displays relationships between entities (domains, email addresses, IP addresses, social profiles) as an interactive graph.

**Recon-ng:** A Python-based web reconnaissance framework with a Metasploit-style module architecture. Automates collection from dozens of OSINT sources and stores results in a structured database.

**SOCMINT (Social Engineering Intelligence):** OSINT gathered specifically from social media platforms. Reveals organizational structure, technology stack, employee contact details, and physical locations.

**Attack Surface:** The total set of points through which an attacker could attempt to interact with or compromise a target. Passive reconnaissance is the process of mapping the attack surface before active testing begins.

---

## Section 2: OSINT Source Categories

### Passive Sources by Category

| Category | Sources | What It Reveals |
|---|---|---|
| Domain registration | WHOIS, RDAP | Registrant, registrar, name servers, expiration |
| DNS | Public resolvers, dig, nslookup | IP addresses, mail servers, subdomains, SPF/DMARC |
| Certificate logs | crt.sh, Google CT | All subdomains with issued certificates |
| Search engines | Google dorks, Bing, DuckDuckGo | Exposed files, open directories, login portals |
| Device search | Shodan, Censys, FOFA | Internet-facing devices, service versions, open ports |
| Code repositories | GitHub, GitLab, Bitbucket | Source code, credentials, internal IPs, config files |
| Social media | LinkedIn, Twitter, GitHub profiles | Employees, tech stack, organizational structure |
| Job postings | LinkedIn Jobs, company careers page | Technologies in use, team structure |
| Company website | About pages, press releases | Vendors, locations, key contacts |
| Public records | SEC filings, court records | Corporate structure, ownership, legal history |

---

## Section 3: DNS Record Types for OSINT

### Record Type Reference

| Record Type | Purpose | OSINT Value |
|---|---|---|
| A | Maps hostname to IPv4 | Server IP addresses |
| AAAA | Maps hostname to IPv6 | IPv6 infrastructure disclosure |
| MX | Identifies mail servers | Mail infrastructure; phishing scope |
| NS | Identifies authoritative name servers | DNS infrastructure targets |
| TXT | SPF, DKIM, DMARC, verification tokens | Third-party services; email security posture |
| CNAME | Canonical name alias | CDN providers, hosting relationships |
| PTR | Reverse lookup | Hostname from IP; naming conventions |
| SOA | Start of authority | Primary name server; admin contact |

### Zone Transfer Testing

A zone transfer request sent to a misconfigured name server returns every DNS record in the zone. Modern configurations restrict zone transfers to trusted secondaries, but it is worth testing on every engagement.

```text
dig axfr @ns1.nameserver.example target-domain.example
```

---

## Section 4: Google Dorking Reference

### Essential Search Operators

| Operator | Example | What It Finds |
|---|---|---|
| site | `site:example.com` | All indexed pages on a domain |
| filetype / ext | `filetype:pdf site:example.com` | Files of a specific type |
| inurl | `inurl:admin site:example.com` | Pages with a keyword in the URL |
| intitle | `intitle:"index of" site:example.com` | Open directory listings |
| intext | `intext:"internal use only"` | Pages containing specific text |
| cache | `cache:example.com` | Google's cached version of a page |

### High-Value Dork Patterns

Exposed configuration files: `ext:env OR ext:config OR ext:ini site:example.com`

Exposed database files: `ext:sql OR ext:db site:example.com`

Login portals: `inurl:login OR inurl:signin site:example.com`

Open Git directories: `intitle:"index of" ".git" site:example.com`

---

## Section 5: theHarvester Command Reference

### Key Flags

| Flag | Purpose |
|---|---|
| `-d` | Target domain |
| `-b` | Data sources (comma-separated: google, bing, linkedin, shodan, certspotter) |
| `-l` | Limit results per source |
| `-f` | Save output to XML and HTML file |

Example (authorized lab environment only):

```text
theHarvester -d target.example -b google,linkedin,shodan -l 500 -f output_file
```

### Output Categories

theHarvester returns email addresses, hostnames and subdomains, IP addresses, LinkedIn profiles, and Shodan-discovered banners. Email addresses are particularly valuable for revealing the organization's naming convention, which informs credential guessing and phishing simulation scope.

---

## Section 6: Shodan for Penetration Testing

### Common Shodan Search Filters

| Filter | Example | Purpose |
|---|---|---|
| org | `org:"Acme Corp"` | Finds all Shodan-indexed assets for an organization |
| net | `net:203.0.113.0/24` | Searches within an IP range |
| hostname | `hostname:example.com` | Finds hosts matching a hostname pattern |
| port | `port:3389` | Finds devices with a specific port open |
| product | `product:"Apache httpd"` | Finds specific software |
| country | `country:US` | Geographic filter |

### Why Shodan Is Passive

Querying Shodan searches Shodan's pre-indexed database — it does not send any traffic to the target. Shodan's own crawlers previously visited the target's systems. Your query retrieves stored results only.

---

## Section 7: Social Media and Code Repository OSINT

### LinkedIn Intelligence Value

LinkedIn provides organizational intelligence without any technical interaction. Key data points:

- Technology skills sections reveal the tech stack
- Job titles and reporting relationships reveal team structure
- Certifications indicate security team expertise
- Recent job postings describe infrastructure in specific technical terms

### GitHub Intelligence Value

Public repositories frequently contain accidentally exposed sensitive data:

- API keys and tokens hardcoded in source files
- Database connection strings with credentials
- Internal IP addresses and hostnames in configuration files
- Accidentally committed `.env` files
- Private SSH keys in repository history

Automated tools including `trufflehog` and `gitrob` search public repositories for secrets patterns. These searches are passive — they query public data only.

---

## Section 8: Documentation Standards

### Required Fields Per Finding

Every OSINT finding must be documented at the time of discovery:

- Date and time of the query
- Tool or source used
- Exact query or search performed
- Raw results obtained
- Analysis note explaining the significance of the finding

### Organization Categories

Organize findings into: network infrastructure, subdomains and hostnames, employee roster and roles, technology stack, email naming convention, exposed services and files, and third-party relationships.

This organized intelligence becomes the foundation of the active scanning plan and target prioritization for the exploitation phase.

---

## Section 9: PenTest+ PT0-002 Exam Tips

### Tip 1 — Passive vs. Active

Passive reconnaissance does not touch target systems. Any technique that sends packets to or initiates connections with the target is active. WHOIS, DNS lookups against public resolvers, Google dorks, theHarvester, and Shodan queries are all passive.

### Tip 2 — Tool Classification

Passive OSINT tools: WHOIS, theHarvester, Maltego, Recon-ng, Shodan, Censys, `crt.sh`. Active tool: Nmap (Module 04). Know the distinction.

### Tip 3 — Zone Transfer Significance

A successful AXFR indicates the target's DNS server is misconfigured to allow zone transfers from any host. This is a finding in itself — not just a method of obtaining DNS records.

### Tip 4 — Google Dorking Is Passive

Google dorks query Google's index. You are not touching target systems. The exam may ask whether this technique is passive or active — it is passive.

### Tip 5 — CT Logs Reveal History

Certificate transparency logs reveal every subdomain that ever had a certificate — including decommissioned systems that may still be running. This historical view is not available through DNS alone.

### Tip 6 — LinkedIn and Job Postings Count

Social media and job postings are explicitly tested OSINT sources. Know that LinkedIn reveals employees, tech stack, and org structure.

### Tip 7 — Shodan Is Passive

Querying Shodan is passive because Shodan's crawlers collected the data — not the tester's tools during the engagement.

### Tip 8 — Document Everything

Reconnaissance documentation is the foundation for the entire engagement. The exam expects testers to document findings as they are discovered, not retrospectively.

---

## Study Checklist

- [ ] Define OSINT and explain passive vs. active reconnaissance without notes
- [ ] List eight passive OSINT source categories and what each reveals
- [ ] Name and describe all eight DNS record types and their OSINT value
- [ ] Explain what a zone transfer is and why a successful AXFR is significant
- [ ] List five Google dorking operators and write an example query for each
- [ ] Describe theHarvester's purpose, key flags, and output categories
- [ ] Explain why querying Shodan is passive reconnaissance
- [ ] Identify three types of sensitive data commonly found in public GitHub repositories
- [ ] List the required fields for documenting each OSINT finding
- [ ] Complete Module 03 lab and attempt all ten quiz questions before checking answers

---

## 9. Supplemental Resources

**1. OSINT Framework — Categorized OSINT Tool Directory**
[https://osintframework.com/](https://osintframework.com/)
A comprehensive, community-maintained tree of OSINT tools and sources organized by category (username, email, domain, IP, social networks, and more). Useful for discovering additional passive reconnaissance resources aligned to the techniques covered in Module 03.

**2. Shodan — Search Engine for Internet-Connected Devices**
[https://www.shodan.io/](https://www.shodan.io/)
Shodan indexes banners, service information, and metadata from internet-connected devices. The free tier allows limited queries useful for practicing target organization lookups, banner analysis, and understanding what information is publicly exposed about networked infrastructure.

**3. Google Dorking Cheat Sheet — Exploit-DB Google Hacking Database**
[https://www.exploit-db.com/google-hacking-database](https://www.exploit-db.com/google-hacking-database)
The Exploit-DB Google Hacking Database (GHDB) catalogs hundreds of Google dork queries organized by category (sensitive files, login portals, exposed configuration files, and more). Reviewing the GHDB alongside Module 03 content reinforces practical Google dorking skills tested on PT0-002.

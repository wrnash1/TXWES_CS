# Reading Guide: Module 03 - OSINT and Passive Reconnaissance
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 03 - OSINT and Passive Reconnaissance**! This module covers the first technical phase of a penetration test: gathering intelligence about the target without directly interacting with their systems. Open Source Intelligence (OSINT) and passive reconnaissance allow testers to build a detailed profile of the target organization — its infrastructure, personnel, technologies, and potential weaknesses — using only publicly available data sources. This phase maps to the **Information Gathering and Vulnerability Scanning** domain of the CompTIA PenTest+ PT0-002 exam, which carries **22% of the exam weight**.

Passive reconnaissance is valuable precisely because it leaves no footprint on the target's systems. The organization cannot detect it through their IDS/IPS or firewall logs, making it a safe and critical first step before any active probing begins.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **WHOIS Queries**: A network protocol and corresponding command-line tool used to query domain registration databases (such as ARIN and ICANN registries) to retrieve information about a domain name or IP address block, including the registrant's organization, contact information, registration dates, and name servers. WHOIS lookups are entirely passive and leave no trace on the target's systems.

*   **DNS Interrogation (`dig`, `host`)**: The process of querying Domain Name System records to map a target's domain names to IP addresses, mail servers, and other infrastructure. Key record types tested on PT0-002 include A (IPv4), AAAA (IPv6), MX (mail), NS (name server), TXT (SPF/DKIM/DMARC), and CNAME (alias). Tools like `dig` and `host` perform these queries against public DNS resolvers, making the activity passive. DNS zone transfers (`dig axfr`) are semi-active and may expose entire subdomain listings if misconfigured.

*   **Shodan Search Filters**: Shodan is a specialized search engine that indexes internet-connected devices by scanning public IP space and recording their banners and service responses. Penetration testers use Shodan to passively identify a target's externally exposed services, software versions, and misconfigurations (e.g., exposed industrial control systems, default credentials, open databases) without touching the target's systems. Key filters include `hostname:`, `org:`, `port:`, and `product:`.

*   **Email Harvesting with theHarvester**: theHarvester is an OSINT tool that aggregates email addresses, subdomains, IP addresses, and employee names from public sources such as search engines, LinkedIn, PGP key servers, and certificate transparency logs. Harvested email addresses support later social engineering and password spray phases; subdomains expand the attack surface map; employee names enable targeted spear-phishing.

*   **Google Dorking**: The use of advanced Google search operators (`site:`, `filetype:`, `inurl:`, `intitle:`, `cache:`) to locate sensitive files, login pages, configuration files, and other target-specific information that is publicly indexed but not intentionally published. Google Dorking is entirely passive and is a standard PT0-002 exam topic.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Information Gathering and Vulnerability Scanning is **22% of PT0-002** — the largest single domain. OSINT and passive recon make up a significant portion of this weight.
*   **Passive vs. Active Distinction:** PT0-002 frequently tests the boundary between passive and active reconnaissance. Passive = no direct contact with target systems (DNS public queries, WHOIS, Shodan, Google Dorking). Active = direct contact (Nmap scans, banner grabbing). Know which tools fall in which category.
*   **Exam Trap — DNS Zone Transfer:** `dig axfr` is semi-active — it contacts the target's name server directly. It will appear in their DNS logs. PT0-002 may ask you to classify zone transfer attempts as active, not passive.
*   **Key OSINT Tools Tested:** theHarvester, Maltego, Recon-ng, Shodan, WHOIS, `dig`, `nslookup`, `host`, Google Dorking, LinkedIn OSINT, Censys, and certificate transparency logs (crt.sh). Know what each tool does and what type of data it collects.
*   **Certificate Transparency Logs:** crt.sh queries public certificate transparency logs to enumerate subdomains for a target domain. This is a powerful passive technique for expanding the attack surface that PT0-002 may test.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Passive Reconnaissance" and "OSINT" rooms within TryHackMe provide hands-on practice with theHarvester, WHOIS, DNS interrogation, and Shodan in a guided, browser-based environment with no local setup required.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Information Gathering section for OSINT and passive recon content mapped to PT0-002 domain 2.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Passive Reconnaissance and OSINT rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). These guided rooms walk through WHOIS lookups, DNS enumeration with `dig`, Shodan searches, and theHarvester usage in realistic scenarios with immediate feedback.
*   **Required Video:** Watch the Information Gathering and OSINT segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This free comprehensive course covers all PT0-002 domains; use chapter markers to navigate to the passive reconnaissance content.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Perform WHOIS lookup on a public domain: `whois example.com`**: You will retrieve and analyze registrant information, registration dates, and name servers for a sample domain, identifying what intelligence value this data provides to a penetration tester.
*   **Use `dig` to find MX and TXT records**: You will query DNS records to enumerate mail servers and identify SPF/DMARC configurations, then explain how this information could be used in a phishing or email spoofing scenario.
*   **Search Shodan for open web servers in a specific city**: You will use Shodan's search filters to locate publicly exposed services matching a target profile, practicing filter syntax and interpreting banner data to identify potential vulnerabilities without touching any target system.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Passive Reconnaissance and OSINT rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Information Gathering section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.

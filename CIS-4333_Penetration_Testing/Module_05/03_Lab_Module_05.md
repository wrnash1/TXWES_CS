# Lab Activity: Module 05 — Reconnaissance and OSINT

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Authorization and Legal Notice

> **REQUIRED BEFORE STARTING:** All reconnaissance activities in this lab are conducted exclusively against pre-authorized targets: the course-provided HackTheBox Starting Point machines, TryHackMe rooms linked below, or DVWA/Metasploitable running in your local isolated lab VM network. You have NO authorization to use any tool, technique, or command from this lab against any real organization, website, IP address, or domain that is not explicitly listed in this lab guide. Unauthorized reconnaissance is a federal crime under 18 U.S.C. § 1030 (CFAA). If you are unsure whether a target is authorized, STOP and contact Professor Nash before proceeding.

---

## Lab Overview

In this lab you will execute a structured reconnaissance workflow against authorized targets, applying the tools and techniques covered in Module 05. You will practice passive OSINT collection, DNS enumeration, and Google dorking in a legal, controlled environment.

**Estimated Time:** 90–120 minutes

**Authorized Lab Targets:**

- TryHackMe room: "Passive Reconnaissance" — [https://tryhackme.com/room/passiverecon](https://tryhackme.com/room/passiverecon)
- TryHackMe room: "Active Reconnaissance" — [https://tryhackme.com/room/activerecon](https://tryhackme.com/room/activerecon)
- Local Metasploitable 2 VM (IP: as assigned in your lab environment — confirm with your instructor)

---

## Prerequisites

- Kali Linux VM running and updated (or TryHackMe AttackBox)
- theHarvester installed (`sudo apt install theharvester`)
- `dig`, `nslookup`, and `host` available (standard on Kali)
- A free TryHackMe account and VPN connected
- Lab notebook or digital notes file open for documentation

---

## Part 1 — Passive OSINT with theHarvester (30 minutes)

### Step 1.1 — Target Scoping

Before running any tool, record your authorized target. For this lab, use the TryHackMe passive recon room target as directed in the room instructions.

In your lab notes, record:

- Target domain or IP
- Authorization source (this lab guide, TryHackMe room)
- Date and time of activity start

### Step 1.2 — Run theHarvester

Connect to the TryHackMe VPN. Launch theHarvester against the authorized practice domain provided in the TryHackMe Passive Reconnaissance room.

```bash
# Replace TARGET_DOMAIN with the domain specified in the TryHackMe room
theHarvester -d TARGET_DOMAIN -b bing -l 100

theHarvester -d TARGET_DOMAIN -b certspotter,dnsdumpster -l 100
```

Capture the output. In your lab notes, record:

- How many email addresses were discovered
- How many subdomains were discovered
- What sources returned the most results

### Step 1.3 — Google Dork Practice

Using Google (not the target's systems), practice the following dork patterns against the TryHackMe practice domain specified in the room:

```text
site:TARGET_DOMAIN
site:TARGET_DOMAIN filetype:pdf
intitle:"index of" site:TARGET_DOMAIN
```

Record any notable findings and whether results appear to be intentionally placed for training purposes.

---

## Part 2 — DNS Enumeration (30 minutes)

### Step 2.1 — Basic DNS Records

Using `dig`, enumerate the DNS records for the authorized target:

```bash
# Standard record lookup
dig TARGET_DOMAIN A
dig TARGET_DOMAIN MX
dig TARGET_DOMAIN NS
dig TARGET_DOMAIN TXT
dig TARGET_DOMAIN SOA
dig TARGET_DOMAIN AAAA
```

In your lab notes, create a table with columns: Record Type, Value, Significance. Fill in one row per record type found.

### Step 2.2 — Zone Transfer Attempt

Attempt a DNS zone transfer against the authorized target. Note: most hardened targets will refuse this. Observing the refusal is itself a finding.

```bash
# Get name servers first
dig TARGET_DOMAIN NS

# Attempt zone transfer against each NS returned
dig axfr @NS1_ADDRESS TARGET_DOMAIN
```

Record the result: did the zone transfer succeed, fail, or was it refused? What does each outcome tell you about the target's DNS security posture?

### Step 2.3 — Reverse DNS Lookup

If the DNS enumeration returned IP addresses, perform reverse lookups:

```bash
dig -x IP_ADDRESS
host IP_ADDRESS
```

Document any hostnames discovered through reverse DNS that were not revealed in forward lookups.

---

## Part 3 — Active Reconnaissance Room (20 minutes)

Complete the TryHackMe "Active Reconnaissance" room. This room provides a safe, pre-authorized environment for practicing active recon techniques including ping sweeps, port scanning basics, and web server fingerprinting.

As you work through the room, record:

- Which techniques generate network traffic vs. which are passive
- What information was revealed by each active technique that passive recon did not reveal
- Why authorization is critical before any active technique

Answer all room questions and take a screenshot of your completed room progress bar.

---

## Part 4 — Reconnaissance Report Template (20 minutes)

Using your findings from Parts 1–3, complete the following reconnaissance report template in your lab notes:

### Reconnaissance Report

**Engagement Name:** CIS-4333 Module 05 Lab

**Tester:** [Your name]

**Date:** [Today's date]

**Authorization Source:** TryHackMe lab environment — Professor Nash CIS-4333

**Target Scope:**

- Authorized domain(s): [list]
- Authorized IP(s): [list]

**Passive OSINT Findings:**

| Finding | Source | Value |
|---------|--------|-------|
| Email addresses | theHarvester | [count and examples] |
| Subdomains | theHarvester/DNS | [list] |
| Technology stack | [source] | [findings] |

**DNS Enumeration Findings:**

| Record Type | Value | Security Significance |
|-------------|-------|----------------------|
| A | [IPs] | [notes] |
| MX | [servers] | [notes] |
| NS | [servers] | [notes] |
| TXT | [content] | [notes] |

**Zone Transfer Result:** [Succeeded / Refused / Failed — and what this means]

**Identified Attack Surface:**

List any exposed services, interesting subdomains, email addresses, or technology stack information that could inform later testing phases.

**Recommended Next Steps:**

What scanning or exploitation activities would logically follow based on your findings?

---

## Deliverables

Submit the following to the Canvas assignment portal:

1. Screenshot of your theHarvester output showing discovered subdomains and email addresses
2. Screenshot of your `dig` DNS enumeration results for at least four record types
3. Screenshot of completed TryHackMe room progress (Active or Passive Recon room)
4. Completed reconnaissance report (text file, PDF, or Word document)
5. Short reflection (150–200 words): What was the most surprising piece of information you were able to gather using only passive techniques? What does this tell you about an organization's OSINT exposure?

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|---------|
| theHarvester output | 20 | Screenshot showing successful execution and interpreted output |
| DNS enumeration | 20 | All four record types queried, results documented in table |
| TryHackMe room | 20 | Completed room screenshot, room questions answered |
| Reconnaissance report | 25 | All sections completed with actual findings from lab |
| Reflection | 15 | 150–200 words, specific to lab experience, professional tone |
| **Total** | **100** | |

---

## Troubleshooting

**theHarvester returns no results:**
Some sources rate-limit free queries. Try a different `-b` source. The `dnsdumpster` and `certspotter` sources generally work without API keys.

**`dig` command not found:**
Install dnsutils with `sudo apt install dnsutils`.

**Zone transfer refused:**
This is expected on hardened targets. Document it as "AXFR refused — DNS zone transfer not permitted" and note that this is good security practice by the target.

**TryHackMe VPN not connecting:**
Download the OpenVPN config from your TryHackMe account settings and connect with `sudo openvpn username.ovpn`.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**

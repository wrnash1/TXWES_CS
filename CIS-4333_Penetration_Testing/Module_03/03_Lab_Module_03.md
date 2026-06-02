# Lab Activity: Module 03 - OSINT and Passive Reconnaissance

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash
**Total Points:** 100

---

## Authorization and Context Notice

All OSINT activities in this lab are performed against fictional organizations or against publicly designated practice targets that exist for educational use. No real organizations are targeted. All techniques demonstrated are passive — no packets are sent to any target systems. This lab is conducted in an authorized educational context.

---

## Lab Overview

In this lab you will practice passive OSINT techniques using publicly available sources, analyze sample DNS and WHOIS output, apply Google dorking operators, and document findings in a professional reconnaissance notes format. These tasks directly mirror real-world Phase 2 reconnaissance work and are tested on the CompTIA PenTest+ PT0-002 exam.

---

## Part 1: WHOIS and DNS Analysis (30 Points)

The following is sample WHOIS and DNS output for a fictional domain `targetcorp.example`. Analyze the output and answer the questions below.

### Sample WHOIS Output (Fictional)

```text
Domain Name: TARGETCORP.EXAMPLE
Registry Domain ID: 8842933_DOMAIN_EXAMPLE-VRSN
Registrar: FakeNames Registrar, LLC
Registrar URL: not-a-real-url.example
Updated Date: 2023-11-01
Creation Date: 2014-03-15
Expiry Date: 2024-03-15
Name Server: NS1.FAKEPROVIDER.EXAMPLE
Name Server: NS2.FAKEPROVIDER.EXAMPLE
Registrant Organization: TargetCorp Industries, Inc.
Registrant State/Province: Texas
Registrant Country: US
Registrant Email: domains@targetcorp.example
Admin Email: itadmin@targetcorp.example
Tech Email: techops@targetcorp.example
DNSSEC: unsigned
```

### Sample DNS Query Output (Fictional)

```text
targetcorp.example.   A       203.0.113.45
www.targetcorp.example.  CNAME  targetcorp.example.
mail.targetcorp.example. A      203.0.113.46
api.targetcorp.example.  A      203.0.113.47
dev.targetcorp.example.  A      10.10.1.100
vpn.targetcorp.example.  A      203.0.113.50

MX records:
10 mail.targetcorp.example.
20 mail2.targetcorp.example.

TXT records:
"v=spf1 include:_spf.google.com include:sendgrid.net ~all"
"google-site-verification=abc123fakeverificationtoken"
"MS=ms12345faketoken"

NS records:
NS1.FAKEPROVIDER.EXAMPLE
NS2.FAKEPROVIDER.EXAMPLE
```

### Question 1.1 — WHOIS Analysis (10 Points)

Answer the following questions based on the WHOIS output above. Write 2 to 3 sentences per answer.

Part A: What does the domain expiration date of 2024-03-15 suggest from a penetration testing and security assessment perspective? What risk does this create?

Part B: The DNSSEC field shows "unsigned." What does this mean, and why is it significant?

Part C: Three email addresses are visible: `domains@targetcorp.example`, `itadmin@targetcorp.example`, and `techops@targetcorp.example`. What information do these reveal about the organization's email naming convention and potential personnel?

### Question 1.2 — DNS Record Analysis (10 Points)

Answer the following questions based on the DNS output above. Write 2 to 3 sentences per answer.

Part A: The A record for `dev.targetcorp.example` resolves to `10.10.1.100`. Why is this finding significant from a reconnaissance perspective? What does it suggest about the network architecture?

Part B: The TXT records reveal `include:_spf.google.com` and `include:sendgrid.net`. What does this tell you about the organization's email infrastructure and third-party service relationships?

Part C: The TXT record contains `MS=ms12345faketoken`. What does this token indicate, and why is this type of verification token useful OSINT?

### Question 1.3 — Zone Transfer Attempt (10 Points)

Write the exact command you would use to attempt a DNS zone transfer against `NS1.FAKEPROVIDER.EXAMPLE` for the domain `targetcorp.example`. Then explain:

Part A: What output would a successful zone transfer produce?

Part B: What does a successful zone transfer indicate about the DNS server's configuration?

Part C: If the zone transfer is refused, what does that indicate and what alternative DNS enumeration techniques would you use next?

---

## Part 2: Google Dorking Analysis (25 Points)

For each of the following Google dork queries, explain what the query is designed to find, what type of sensitive information could be discovered, and what the security implication would be if results are returned.

Write 3 to 4 sentences per query.

### Query 2.1 (5 Points)

`site:targetcorp.example filetype:pdf "confidential"`

### Query 2.2 (5 Points)

`site:targetcorp.example inurl:login OR inurl:admin OR inurl:wp-login`

### Query 2.3 (5 Points)

`site:targetcorp.example ext:env OR ext:config OR ext:ini`

### Query 2.4 (5 Points)

`intitle:"index of" site:targetcorp.example`

### Query 2.5 (5 Points)

`site:github.com "targetcorp.example" password OR secret OR api_key`

---

## Part 3: Reconnaissance Notes Documentation (25 Points)

Using the data you analyzed in Parts 1 and 2, produce a professional reconnaissance notes document for the fictional TargetCorp engagement. Your notes must follow the documentation format specified below and include at least eight distinct findings.

### Required Documentation Format

For each finding, record:

Finding ID: (sequential number, e.g., RECON-001)

Date/Time: (use today's date and a plausible time)

Source: (WHOIS, DNS, Google dork, Shodan, LinkedIn, etc.)

Query or Method: (exact query or technique used)

Raw Result: (the data obtained)

Analysis: (what this finding means for the engagement and what active testing it suggests)

### Grading Criteria for Part 3

Your reconnaissance notes are graded on:

- Completeness: eight or more findings documented (10 points)
- Format compliance: all six required fields present for each finding (5 points)
- Analysis quality: analysis notes are specific, relevant, and actionable — not generic (10 points)

---

## Part 4: Reflection Questions (20 Points)

Answer each question in complete sentences. Write 4 to 5 sentences per response.

### Question 4.1 (5 Points)

You are conducting passive reconnaissance for an authorized penetration test. You discover through Google dorking that an internal network diagram PDF is indexed by Google and freely downloadable from the target's public web server. The diagram was labeled "For Internal Use Only." Describe what you do with this finding and how you document it. Does this finding require any special action beyond documentation?

### Question 4.2 (5 Points)

Explain why a penetration tester would perform extensive passive reconnaissance even when they have been given a white box test with full network diagrams and documentation. What additional value does OSINT provide beyond what the client has already disclosed?

### Question 4.3 (5 Points)

During passive reconnaissance you find a GitHub repository belonging to a TargetCorp developer that contains what appears to be a hardcoded AWS access key in a configuration file committed six months ago. The repository is public. Describe the exact steps you take from discovery through documentation. Does this finding change the scope of the test or require client notification before active testing begins?

### Question 4.4 (5 Points)

Explain the difference between passive reconnaissance and active reconnaissance. Give two specific examples of each. For each example, state whether it leaves traces in the target's logs and whether it requires authorization to be in place before it can be performed.

---

## Submission Instructions

Submit the following to the Canvas LMS assignment portal:

- One PDF or Word document containing all four parts of this lab
- File naming convention: `CIS4333_Lab03_LastName_FirstName.pdf`
- Due date: as listed in the course calendar

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part 1.1 — WHOIS Analysis | 10 | Three parts answered accurately; expiration risk, DNSSEC, and email convention all addressed |
| Part 1.2 — DNS Analysis | 10 | Three parts answered accurately; private IP significance, SPF/SendGrid, and MS token addressed |
| Part 1.3 — Zone Transfer | 10 | Correct command; successful output described; misconfiguration implication and alternatives explained |
| Part 2.1 — PDF dork | 5 | What it finds, what could be discovered, security implication all described |
| Part 2.2 — Login dork | 5 | Same criteria |
| Part 2.3 — Config file dork | 5 | Same criteria |
| Part 2.4 — Directory listing dork | 5 | Same criteria |
| Part 2.5 — GitHub credential dork | 5 | Same criteria |
| Part 3 — Recon Notes | 25 | Eight or more findings; all six format fields present; analysis is specific and actionable |
| Part 4.1 — Internal document discovery | 5 | Correct handling of accidentally indexed internal document |
| Part 4.2 — White box OSINT value | 5 | Explains what OSINT reveals beyond client-provided documentation |
| Part 4.3 — GitHub credential discovery | 5 | Correct steps from discovery through documentation; notification question addressed |
| Part 4.4 — Passive vs. active | 5 | Clear distinction; two examples each; log traces and authorization addressed |
| **Total** | **100** | |

---

*This lab is for authorized educational purposes only. All organizations, domains, and IP addresses are fictional. No actual systems are targeted.*

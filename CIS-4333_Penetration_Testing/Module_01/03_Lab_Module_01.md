# Lab Activity: Module 01 - Penetration Testing Methodology and Scoping

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash
**Total Points:** 100

---

## Authorization and Context Notice

This lab is conducted entirely as a document-drafting exercise. No technical scanning, exploitation, or network interaction is performed. All systems and organizations referenced are fictional. This exercise simulates the pre-engagement documentation phase of a professional penetration test in an authorized educational context.

---

## Lab Overview

In this lab you will draft two professional pre-engagement documents for a hypothetical penetration testing engagement: a **Scope of Work (SOW)** and a **Rules of Engagement (RoE)**. These documents are the foundation of every authorized penetration test. Producing them accurately is a core professional skill and a tested knowledge area on the CompTIA PenTest+ PT0-002 exam.

---

## Scenario

**Client:** Lone Star Financial Services, LLC (fictional)

Lone Star Financial Services is a regional bank holding company based in Fort Worth, Texas. Their IT Security Officer has contacted your firm, ClearPath Security Consulting (fictional), to conduct an annual external and internal network penetration test required for their PCI DSS compliance review. You are the lead penetration tester assigned to draft the pre-engagement documentation.

Key details provided by the client:

- External IP range: 203.0.113.0/28 (documentation range; 14 usable addresses)
- Internal corporate network: 10.100.0.0/22
- In-scope applications: `www.lonestarfinancial.example` and `api.lonestarfinancial.example`
- Third-party payment processing infrastructure is explicitly out of scope
- Test type: gray box — testers receive one standard employee-level Active Directory account
- Authorized testing window: Monday through Friday, 10:00 PM to 6:00 AM Central Time
- Engagement duration: two calendar weeks
- Social engineering and physical access attempts are not authorized
- Critical system disruption requires immediate halt and client notification

---

## Part 1: Draft the Statement of Work (35 Points)

Draft a professional Statement of Work document. Write in formal language as if it will be signed by both parties.

### Section 1.1 — Engagement Overview

**5 points.** Write 2 to 3 paragraphs describing the engagement. Include the client name, test type (gray box, external and internal network penetration test), the compliance driver (PCI DSS), and the testing firm name.

### Section 1.2 — Scope Definition

**10 points.** List all in-scope assets using proper CIDR notation for network ranges and fully qualified domain names for applications. Include a clearly labeled Out-of-Scope section that explicitly excludes the payment processing infrastructure and any unlisted systems.

### Section 1.3 — Testing Window and Schedule

**5 points.** Specify authorized testing days, hours, and total engagement duration formatted as a table with columns: Day or Date Range, Authorized Hours, and Time Zone.

### Section 1.4 — Deliverables

**5 points.** List all deliverables the client receives at conclusion. Minimum required: written penetration test report, executive summary, technical findings appendix with CVSS scores, and a remediation recommendations section.

### Section 1.5 — Assumptions and Constraints

**5 points.** Document assumptions (e.g., the client will provide one Active Directory test account before testing begins) and constraints (e.g., no denial-of-service testing against production systems, no social engineering, no physical access attempts).

### Section 1.6 — Signatures Block

**5 points.** Include a properly formatted signature block with lines for: Client Representative Name, Title, Date, Signature; and Testing Firm Representative Name, Title, Date, Signature.

---

## Part 2: Draft the Rules of Engagement (45 Points)

Draft a professional Rules of Engagement document. The RoE must be specific enough that any authorized tester could read it and know exactly what they are and are not permitted to do.

### Section 2.1 — Authorized Targets

**10 points.** Create an Appendix A listing all authorized targets. For each target include:

- IP address or CIDR range
- Hostname or domain name if applicable
- System type (web server, application server, database server, network device, etc.)
- Special considerations (e.g., "production system — avoid service disruption")

### Section 2.2 — Authorized Testing Techniques

**10 points.** List the specific techniques explicitly authorized for this engagement, organized by phase:

#### Reconnaissance Phase

Passive OSINT, active port scanning, service version enumeration, OS fingerprinting.

#### Vulnerability Analysis Phase

Automated scanning with approved tools, manual CVE research, configuration review.

#### Exploitation Phase

Exploitation of identified vulnerabilities within authorized scope, credential testing, privilege escalation attempts.

#### Post-Exploitation Phase

Network pivot within authorized ranges, data access demonstration only — no actual data exfiltration.

### Section 2.3 — Prohibited Techniques

**10 points.** List all explicitly prohibited activities. At a minimum include:

- Social engineering of employees
- Physical access attempts to premises
- Denial-of-service attacks against production systems
- Any testing of third-party payment processor infrastructure
- Exfiltration of actual customer or financial data
- Any technique not explicitly listed as authorized in Section 2.2

### Section 2.4 — Communication Protocol

**5 points.** Define communication requirements during the engagement including:

- Frequency and format of status updates (e.g., daily written email by 8:00 AM)
- Emergency contact information (name, phone number, email)
- Conditions requiring immediate notification (active real-world intrusion signs, critical service disruption, discovery of PII)

### Section 2.5 — Emergency Stop Conditions

**5 points.** List the specific conditions that require all testing to halt immediately and the IT Security Officer to be contacted. Include at minimum: signs of an active real-world intrusion by a third party, accidental disruption of a production service, and discovery of evidence of criminal activity on target systems.

### Section 2.6 — Data Handling Rules

**5 points.** Describe how sensitive data discovered during the engagement will be handled. Address: storage method (encrypted at rest), transmission method (encrypted in transit), retention period (e.g., destroyed 30 days after report delivery), and disclosure restrictions (report delivered only to named client representatives).

---

## Part 3: Reflection Questions (20 Points)

Answer each question in complete sentences. Aim for 3 to 5 sentences per answer.

### Question 3.1 — Verbal Authorization and the CFAA

**5 points.** Why is a verbal agreement insufficient as authorization for a penetration test? Reference the Computer Fraud and Abuse Act in your answer.

### Question 3.2 — SOW vs. RoE

**5 points.** Explain the difference between the SOW and the RoE. Why must both documents exist rather than combining them into a single document?

### Question 3.3 — Out-of-Scope Discovery

**5 points.** During the engagement you discover that the web server at `www.lonestarfinancial.example` connects to a backup server at 10.100.5.200, which is not listed in the RoE. Describe the exact steps you would take. Do not describe any technical actions taken against 10.100.5.200.

### Question 3.4 — Verbal Scope Expansion

**5 points.** The client's CEO calls you directly and verbally instructs you to expand the scope to include testing their mobile banking application. How do you respond, and what steps must occur before you can begin testing the mobile app?

---

## Submission Instructions

Submit the following to the Canvas LMS assignment portal:

- One PDF or Word document containing your complete SOW (Part 1), RoE (Part 2), and Reflection answers (Part 3)
- File naming convention: `CIS4333_Lab01_LastName_FirstName.pdf`
- Due date: as listed in the course calendar

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| SOW 1.1 — Engagement Overview | 5 | Client, test type, compliance driver, and firm all identified |
| SOW 1.2 — Scope Definition | 10 | CIDR and FQDN used; explicit out-of-scope section present |
| SOW 1.3 — Testing Window | 5 | Table format; days, hours, and time zone specified |
| SOW 1.4 — Deliverables | 5 | Four required deliverables listed |
| SOW 1.5 — Assumptions and Constraints | 5 | AD account assumption noted; three or more prohibitions listed |
| SOW 1.6 — Signatures Block | 5 | Both parties; name, title, date, signature lines present |
| RoE 2.1 — Authorized Targets | 10 | All in-scope IPs and domains in structured format with system types |
| RoE 2.2 — Authorized Techniques | 10 | Organized by phase; at least three techniques per phase |
| RoE 2.3 — Prohibited Techniques | 10 | All six minimum items included; language is unambiguous |
| RoE 2.4 — Communication Protocol | 5 | Update frequency, emergency contacts, notification triggers defined |
| RoE 2.5 — Emergency Stop Conditions | 5 | At least three conditions with specific triggering criteria |
| RoE 2.6 — Data Handling | 5 | Storage, transmission, retention, and disclosure all addressed |
| Reflection 3.1 — CFAA | 5 | CFAA cited; written authorization legally required |
| Reflection 3.2 — SOW vs. RoE | 5 | Clear distinction; complementary purposes explained |
| Reflection 3.3 — Out-of-Scope Discovery | 5 | Correct procedure: stop, document, notify; no unauthorized action |
| Reflection 3.4 — Verbal Scope Expansion | 5 | Refuses to proceed; requires signed written authorization |
| **Total** | **100** | |

---

*This lab is for authorized educational purposes only. All organizations and IP addresses are fictional. No actual systems are tested.*

# Lab: Module 16 — PenTest+ PT0-002 Exam Preparation and Capstone

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

- **Duration:** 3 hours
- **Format:** Written capstone assessment and exam preparation exercises
- **Materials:** Provided scenario packets, CVSS calculator access, reading guides from all modules
- **Note:** The capstone assessment is closed-book (no notes, no internet). The preparation exercises before it are open-resource.

This final lab is the capstone of CIS-4333. It assesses competency across all course content and all PT0-002 exam domains.

---

## Lab Objectives

By completing this lab, students will:

1. Demonstrate mastery of all five PT0-002 exam domains.
2. Apply CVSS scoring accurately to diverse finding types.
3. Demonstrate correct decision-making in legal and authorization scenarios.
4. Complete a 20-question simulated PT0-002 capstone assessment under exam conditions.
5. Develop a personal PT0-002 exam preparation action plan.

---

## Part 1: Pre-Capstone Review Exercises (60 minutes, open resource)

These exercises identify and address knowledge gaps before the closed-book capstone.

### Exercise 1.1: Tool Mapping Flash Review

Without referencing notes, write the primary use case for each tool:

1. Nmap
2. Metasploit
3. Aircrack-ng
4. GoPhish
5. Mimikatz
6. BloodHound
7. Responder
8. ScoutSuite
9. Frida
10. jwt_tool
11. Binwalk
12. SQLMap
13. Proxmark3
14. Hashcat
15. theHarvester

Then check your answers against the Module 16 reading guide tool reference table.

**Self-Assessment:** For any tool you missed or described incorrectly, review the corresponding module's reading guide before proceeding to the capstone.

### Exercise 1.2: CVSS Scoring Practice

Calculate the CVSS 3.1 Base Score for each of the following scenarios. Use the calculator at first.org/cvss/calculator/3.1 only to verify — attempt manual calculation first.

Scenario A: A SQL injection vulnerability in a public web application allows unauthenticated access to the complete customer database. Full CRUD operations are possible.

Scenario B: A locally exploitable privilege escalation in a desktop application requires a standard user account and grants local administrator access. System access only — no network exploitation.

Scenario C: An SSRF vulnerability in an internal web application (accessible only from the corporate network) allows read access to the AWS IMDS, returning IAM credentials for a role with full S3 access.

Scenario D: A reflected XSS vulnerability in the company's career portal requires a victim to click a crafted link. Successful exploitation steals the user's session cookie. The career portal is public-facing.

Scenario E: Default credentials (admin/admin) on a building management system's web interface, accessible from the internal corporate network. The BMS controls HVAC and door access for the facility.

**Lab Report Item 1:** Complete the CVSS scoring table. Format:

| Scenario | AV | AC | PR | UI | S | C | I | A | Score | Rating |
|----------|----|----|----|----|---|---|---|---|-------|--------|

### Exercise 1.3: Authorization Decision Scenarios

For each of the following situations, write one sentence describing the correct action:

1. During an authorized external web app test, the tester finds the application is hosted on a shared hosting platform with other tenants visible.

2. A phishing campaign captures 20 sets of real employee credentials within the first hour.

3. During an authorized physical test, the tester observes confidential documents in an unlocked office but the scope does not specifically mention document review.

4. An authorized cloud assessment discovers an S3 bucket containing backups from a subsidiary not listed in the scope.

5. Midway through a wireless test, the tester's deauthentication attack inadvertently disconnects a user from a VoIP call.

**Lab Report Item 2:** Submit your five authorization decision responses.

---

## Part 2: Capstone Assessment (45 minutes, CLOSED BOOK)

### Instructions

This assessment is closed book. No notes, no internet access, no references. 20 questions, 45 minutes.

Questions cover all five PT0-002 domains. Each question is worth 5 points. Passing threshold: 70% (14/20 correct).

The capstone questions are contained in the Capstone Question Bank distributed separately by the instructor. Students receive a unique question packet.

**After completing the capstone:**

Submit your answer sheet to the instructor. Do not discuss specific questions with classmates until grades are posted.

---

## Part 3: Capstone Scenario Analysis — Fictitious Full Engagement (45 minutes, open resource)

This section presents a complete fictional engagement scenario. Students analyze the entire engagement and produce outputs demonstrating end-to-end penetration testing competency.

### Engagement Background

**Client:** Northgate Technology Partners (fictional)

**Engagement Type:** Full-scope penetration test — external, internal, web application, and social engineering (no physical testing authorized)

**Scope:** 203.0.113.0/28 (external IPs), 10.50.0.0/16 (internal), web.northgate-tp.example (web application), app.northgate-tp.example (SaaS API)

**Duration:** 5 business days

**Authorized by:** Sarah Okonkwo, CISO (fictional)

### Engagement Finding Summary

Day 1 — External recon: theHarvester identified 4 employee email addresses. crt.sh revealed 12 subdomains. Shodan identified an exposed Confluence instance (CVE-2022-26134, CVSS 9.8) at confluence.northgate-tp.example.

Day 2 — Web application testing: app.northgate-tp.example has a BOLA vulnerability on /api/v2/users/{id}/profile. Authenticated as user_100, the tester accessed profiles for users 1–99 by iterating the ID. User 12 is an admin; the admin profile returns an API token with elevated privileges.

Day 3 — Social engineering: A spear phishing campaign targeting 12 employees (authorized in SOW) achieved a 33% click rate (4/12) and a 17% credential submission rate (2/12). Both submitters were finance department employees.

Day 4 — Internal network: Using escalated credentials from the API token, the tester gained access to the internal network via the API management system. BloodHound identified a path from the API service account to Domain Admin via Kerberoasting a service account (SVC_BACKUP).

Day 5 — Post-exploitation and cleanup: From the SVC_BACKUP cracked hash, the tester obtained Domain Admin credentials. Reached the file server at \\FILESERVER01 and confirmed access to the CFO's financial documents folder. All test artifacts removed. No persistence established.

### Step 3.1: Attack Chain Documentation

**Lab Report Item 3:** Write a complete attack chain narrative (400 words maximum) documenting the path from initial external reconnaissance to Domain Admin. Number each step and name the specific vulnerability or technique used.

### Step 3.2: CVSS Scoring for All Findings

**Lab Report Item 4:** Complete the CVSS table for all findings from the engagement (Confluence RCE, BOLA/privilege escalation, social engineering credential submission, Kerberoasting, Domain Admin access).

### Step 3.3: Executive Summary

**Lab Report Item 5:** Write a 300-word executive summary for the Northgate Technology Partners engagement. Non-technical audience. Include: overall posture, top 3 findings in plain language, and 3 priority action items with timelines.

### Step 3.4: Remediation Roadmap

**Lab Report Item 6:** Complete a 5-finding remediation roadmap table with risk rating, immediate action, long-term action, and responsible team for each finding.

---

## Part 4: Personal Exam Preparation Action Plan (15 minutes)

### Step 4.1: Domain Gap Analysis

Based on your capstone results (provided by instructor after Part 2 submission) and your self-assessment from Exercise 1.1, complete:

| PT0-002 Domain | Confidence (1–5) | Topics Needing Review | Resources to Use |
|---------------|-----------------|----------------------|-----------------|
| 1 — Planning | | | |
| 2 — Recon | | | |
| 3 — Attacks | | | |
| 4 — Reporting | | | |
| 5 — Tools | | | |

### Step 4.2: 30-Day Study Plan

Write a week-by-week study plan covering the 4 weeks before your planned PT0-002 exam date. Include:

- Daily study time commitment
- Resources for each week
- Practice exam schedule
- Hands-on lab days (HTB, THM)

**Lab Report Item 7:** Submit your domain gap analysis and 30-day study plan.

---

## Lab Report Submission

Your lab report must include:

- Lab Report Items 1–7
- CVSS scoring tables (Items 1 and 4)
- Authorization decision responses (Item 2)
- Attack chain narrative (Item 3)
- Executive summary (Item 5)
- Remediation roadmap (Item 6)
- Exam preparation plan (Item 7)

**Note:** Capstone answer sheet submitted separately under exam conditions.

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| CVSS scoring exercises (Item 1) | 10 |
| Authorization decisions (Item 2) | 5 |
| Capstone assessment (20 questions) | 50 |
| Attack chain narrative (Item 3) | 10 |
| Engagement executive summary (Item 5) | 10 |
| Remediation roadmap (Item 6) | 10 |
| Exam preparation plan (Item 7) | 5 |
| **Total** | **100** |

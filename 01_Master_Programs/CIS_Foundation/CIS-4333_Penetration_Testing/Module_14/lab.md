# Lab: Module 14 — Legal, Compliance, and Contractual Considerations

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

- **Duration:** 3 hours
- **Format:** Document review and drafting exercise — no live systems
- **Materials:** Deficient SOW draft (distributed by instructor), ROE template, bug bounty policy examples
- **Deliverable:** Revised SOW, ROE document, and bug bounty policy analysis

This lab develops the legal and contractual documentation skills required for professional penetration testing practice.

---

## Lab Objectives

By completing this lab, students will:

1. Identify legal and contractual deficiencies in a penetration testing scope of work.
2. Revise an SOW to meet professional standards.
3. Draft a rules of engagement document for a specific fictional engagement.
4. Analyze bug bounty program policies for completeness and legal adequacy.
5. Write a responsible disclosure notification to a fictional organization.

---

## Part 1: SOW Review and Revision (60 minutes)

### Deficient SOW Document

The following is a deficient scope of work document. Students will identify all deficiencies, explain the risk each creates, and revise the document to meet professional standards.

---

**SECURITY ASSESSMENT AGREEMENT**

Between: SecurityFirst LLC and Hartwell Industries

Date: [TBD]

We agree to do a security test of Hartwell's systems starting sometime next month. We'll test whatever needs to be tested and report what we find. Testing will be done by our team using standard tools. We'll send you a report when we're done.

Payment: $15,000 due upon completion.

Signed: John Smith (SecurityFirst), Bob Johnson (Hartwell IT)

---

### Step 1.1: Deficiency Analysis

Identify every deficiency in the deficient SOW above. For each deficiency, provide:

- What is missing or inadequate
- What specific risk this creates (legal, operational, or professional)
- What the corrected language should include

**Lab Report Item 1:** Submit a deficiency analysis table with at minimum 12 identified deficiencies. Format:

| Deficiency | Risk Created | Required Correction |
|------------|-------------|--------------------|
| | | |

### Step 1.2: Revised SOW

Write a complete, professionally adequate scope of work for the following engagement:

**Engagement Parameters:**

- **Client:** Hartwell Industries, Inc. (fictional)
- **Authorized by:** Dr. Angela Martinez, CISO (fictional, direct contact 555-0192)
- **Testing Firm:** CIS-4333 Security Labs (fictional student firm)
- **Engagement Type:** External network penetration test and web application assessment
- **Scope:** External IP ranges 198.51.100.0/28, the web application at shop.hartwell-ind.com, and the admin portal at admin.hartwell-ind.com
- **Out of scope:** All internal systems, the ERP system at erp.hartwell-ind.com, any third-party payment processor infrastructure
- **Testing Period:** First two weeks of the month (specific dates TBD at kickoff)
- **Testing Hours:** Business hours only (8 AM–5 PM Central Time) for web application testing; external port scanning may occur after hours
- **Deliverables:** Full technical report within 5 business days of test completion, executive summary, 30-day re-test for critical/high findings at no charge
- **Payment:** 50% upon signing, 50% upon report delivery

Your revised SOW must include all standard components identified in the reading guide.

**Lab Report Item 2:** Submit your complete revised SOW (minimum 600 words).

---

## Part 2: Rules of Engagement Development (45 minutes)

Using the same fictional engagement from Part 1, develop a complete Rules of Engagement document.

### ROE Requirements

Your ROE must include:

1. Testing hours (with specific time windows and time zone)

2. Permitted techniques (list at minimum 10 specific techniques)

3. Prohibited techniques (list at minimum 6 specific prohibitions — be specific)

4. Notification thresholds (at minimum 4 conditions requiring immediate client notification)

5. Emergency abort conditions (at minimum 3 conditions)

6. Emergency contacts (template with role, name placeholder, phone, alternate phone)

7. Test status communication protocol (frequency, format, recipients)

8. Out-of-scope system handling (what happens if the tester encounters an out-of-scope system with a critical vulnerability)

9. Data handling (how test data — captured credentials, screenshots — is handled)

10. Cloud provider testing policy (for any cloud-hosted applications in scope)

**Lab Report Item 3:** Submit your complete ROE document.

---

## Part 3: Bug Bounty Policy Analysis (30 minutes)

Review the following two fictional bug bounty policies and evaluate them against professional standards.

### Policy Alpha (from "TechCorp" — fictional):

"We welcome security researchers to help improve our security. Test our website and report any vulnerabilities you find to security@techcorp.example. We may pay rewards for significant findings. Do not attack our customers."

### Policy Beta (from "SecureBank" — fictional):

"SecureBank's vulnerability disclosure program covers the following assets: online banking portal (onlinebanking.securebank.example), mobile application (iOS and Android), and API (api.securebank.example).

Researchers may test for: authentication bypasses, SQL injection, XSS, IDOR, and other OWASP Top 10 vulnerability classes.

Researchers may not: access other customers' data, perform denial-of-service testing, conduct social engineering against employees, test physical locations.

SecureBank will not pursue legal action against researchers who follow these guidelines, report findings within 7 days of discovery, and do not disclose findings publicly within 90 days of submission.

Rewards: Critical ($5,000), High ($2,500), Medium ($500), Low ($100).

Report to: security@securebank.example | PGP key available at securebank.example/security"

### Step 3.1: Policy Comparison

**Lab Report Item 4:** Compare Policy Alpha and Policy Beta against the following criteria. Rate each policy: Adequate, Partially Adequate, or Inadequate for each criterion.

| Criterion | Policy Alpha | Policy Beta |
|-----------|-------------|-------------|
| Clear scope definition | | |
| Prohibited techniques | | |
| Legal safe harbor | | |
| Disclosure timeline | | |
| Communication channel | | |
| Reward structure | | |
| Good-faith standard | | |
| Overall assessment | | |

Write 200 words explaining which policy better protects the organization and which better protects the researcher.

### Step 3.2: Policy Improvement

For Policy Alpha, write a complete, professional bug bounty policy that addresses all deficiencies. Your policy should be appropriate for a mid-sized technology company (fictional TechCorp) with a public-facing website and mobile application.

**Lab Report Item 5:** Submit your revised Policy Alpha (minimum 300 words).

---

## Part 4: Responsible Disclosure Notification (30 minutes)

You are a security researcher (acting independently, not as a professional tester on a paid engagement). You have discovered a SQL injection vulnerability on the public website of "Meridian Community Hospital" (fictional) that allows read access to a database containing what appear to be patient appointment records. You discovered this accidentally while using the hospital's appointment scheduling page from your home computer. You did not intentionally conduct a security test.

### Step 4.1: Responsible Disclosure Letter

Write a responsible disclosure notification email to the hospital's security team. Your notification must:

- Clearly identify who you are (you may use a pseudonym)
- Describe what you discovered (without including sufficient detail to weaponize the finding)
- Describe how you discovered it (emphasize accidental discovery)
- State that you have not accessed any patient data beyond confirming the vulnerability's existence
- Request acknowledgment within 7 days
- State your intention to allow 90 days for remediation before any public disclosure
- Offer to provide additional technical details if requested

**Lab Report Item 6:** Submit your responsible disclosure notification.

### Step 4.2: Legal and Ethical Analysis

**Lab Report Item 7:** In 250 words, analyze the legal position of the researcher in this scenario. Consider: Did the accidental discovery violate the CFAA? Does the CFAA's "authorization" requirement distinguish between intentional and accidental access? What is the researcher's ethical obligation once they discover the vulnerability? Does the absence of a bug bounty program affect the researcher's obligations?

---

## Lab Report Submission

Your lab report must include:

- Lab Report Items 1–7
- Deficiency analysis table (minimum 12 deficiencies)
- Complete revised SOW
- Complete ROE document
- Bug bounty policy comparison and revision
- Responsible disclosure notification
- Legal analysis

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| SOW deficiency analysis (Item 1) | 20 |
| Revised SOW (Item 2) | 25 |
| Rules of Engagement document (Item 3) | 25 |
| Bug bounty analysis and revision (Items 4–5) | 15 |
| Responsible disclosure and legal analysis (Items 6–7) | 15 |
| **Total** | **100** |

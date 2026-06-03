# Lab: Module 11 — Social Engineering Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Authorization Statement

This lab simulates a complete phishing campaign against an isolated, professor-controlled test environment. All target email addresses are fictional accounts on a lab email server operated exclusively for this course. No real individuals, real organizations, or external email infrastructure are used.

Sending phishing emails to any real person, organization, or external email service using any tool or technique from this lab is a violation of federal law (18 U.S.C. § 1030, CAN-SPAM Act, 18 U.S.C. § 2701) and university policy. Any student found sending unauthorized phishing communications will receive a failing grade and be referred for disciplinary action.

---

## Lab Overview

- **Duration:** 3 hours
- **Environment:** Kali Linux VM connected to isolated lab network
- **Lab Email Server:** mail.lab.txwes-pentest.local (internal only, no external routing)
- **GoPhish Server:** Pre-installed at 10.99.50.10:3333 (admin), 10.99.50.10:80 (phish)
- **Lab Target Accounts:** 20 fictional employee accounts pre-created by instructor
- **Lab Domain:** txwes-lab-corp.local (fictional company for simulation)

---

## Lab Objectives

By completing this lab, students will:

1. Configure a GoPhish sending profile and email template.
2. Clone a login page for use as a credential capture landing page.
3. Launch an authorized phishing campaign against lab test accounts.
4. Analyze campaign results including open rate, click rate, and submission rate.
5. Develop a pretext for a simulated vishing scenario.
6. Write a professional phishing campaign finding for a penetration test report.

---

## Part 1: GoPhish Environment Setup (30 minutes)

### Step 1.1: Access the GoPhish Admin Panel

Open a browser on your Kali VM and navigate to:

```
https://10.99.50.10:3333
```

Accept the self-signed certificate warning. Log in with credentials provided by the instructor.

**Lab Report Item 1:** Screenshot the GoPhish dashboard showing the initial state (no campaigns). Describe the four main configuration components visible in the left navigation.

### Step 1.2: Configure Sending Profile

Navigate to Sending Profiles and create a new profile:

- **Name:** Lab-SMTP
- **From:** IT Security Team `<security@txwes-lab-corp.local>`
- **Host:** mail.lab.txwes-pentest.local:25
- **Username/Password:** Provided by instructor

Click "Send Test Email" and enter your own lab email address to confirm deliverability.

**Lab Report Item 2:** Screenshot the test email received. Note any email headers that reveal the sending infrastructure. In a real engagement, how would you minimize these tells?

### Step 1.3: Build the Email Template

Navigate to Email Templates and create a new template. You will simulate an IT department password-reset notification.

- **Name:** IT-Password-Reset
- **Subject:** Action Required: Password Expiration Notice — Account Security

Write the email body in HTML mode. Include:

- Company logo (lab logo URL provided by instructor)
- Urgency language about account expiration
- A call-to-action button linking to `{{.URL}}`
- Personalized greeting using `{{.FirstName}}`
- Signature from "IT Security Team — Txwes-Lab-Corp"

**Lab Report Item 3:** Screenshot your completed email template in preview mode. Identify three psychological influence principles from Cialdini's framework that your template employs.

---

## Part 2: Landing Page and Campaign Configuration (45 minutes)

### Step 2.1: Clone a Login Page

Navigate to Landing Pages and create a new page.

Click "Import Site" and enter:

```
http://mail.lab.txwes-pentest.local/owa
```

(This is the lab Outlook Web App clone — a fictional login page on the lab server.)

GoPhish will import the page HTML. Enable "Capture Submitted Data" and "Capture Passwords" options.

Set the Redirect URL to `http://mail.lab.txwes-pentest.local/owa` (redirect after submission).

**Lab Report Item 4:** Screenshot the imported landing page in GoPhish. Explain why redirecting to the legitimate login page after credential capture is important in a real engagement.

### Step 2.2: Upload Target List

Navigate to Users & Groups and create a new group named "Lab-Targets."

Import the target CSV provided by the instructor (20 fictional employees). The CSV format is:

```
First Name,Last Name,Email,Position
John,Smith,jsmith@txwes-lab-corp.local,Finance Analyst
...
```

**Lab Report Item 5:** How many unique departments are represented in the target list? Hypothesize which department will have the highest click rate and explain your reasoning using pretext analysis.

### Step 2.3: Create and Launch Campaign

Navigate to Campaigns and create a new campaign:

- **Name:** Module11-Lab-[YourName]
- **Email Template:** IT-Password-Reset
- **Landing Page:** (your cloned page)
- **Launch Date:** Immediate
- **Sending Profile:** Lab-SMTP
- **Groups:** Lab-Targets

Click Launch Campaign.

---

## Part 3: Campaign Monitoring and Analysis (45 minutes)

### Step 3.1: Real-Time Dashboard

Observe the campaign dashboard for 15 minutes. GoPhish simulates response behavior for the lab accounts automatically.

Record the following at 5-minute intervals:

- Emails sent
- Emails opened
- Links clicked
- Credentials submitted
- Reports made

**Lab Report Item 6:** Create a time-series table showing these five metrics at 5, 10, and 15 minutes. At what point did the majority of clicks occur? What does this tell you about attacker dwell time requirements?

### Step 3.2: Individual Event Timeline

Click on any target who submitted credentials to view their individual event timeline.

**Lab Report Item 7:** Screenshot the event timeline. Identify the timestamps for: email sent, email opened, link clicked, and data submitted. Calculate the time from receipt to submission. What does a short time-to-submit indicate about the effectiveness of urgency-based pretexts?

### Step 3.3: Export and Calculate Metrics

Export campaign results to CSV. In a spreadsheet, calculate:

- Overall open rate
- Overall click rate
- Overall submission rate
- Overall report rate
- Submission-to-click conversion rate (submissions ÷ clicks)

**Lab Report Item 8:** Fill in this findings table:

| Metric | Value | Industry Average | Risk Level |
|--------|-------|-----------------|------------|
| Click Rate | | ~15-25% | |
| Submission Rate | | ~8-12% | |
| Report Rate | | ~5-10% | |

Is the organization (fictional) above or below average? What CVSS score would you assign to a "25% credential submission rate on password-reset phishing"? Justify using the CVSS base score metrics (Attack Vector, Attack Complexity, etc.).

---

## Part 4: Vishing Pretext Development (30 minutes)

This portion does not use live calls. Students develop a vishing script for a simulated IT helpdesk call targeting a fictional employee.

### Step 4.1: Target Research Simulation

Review the fictional employee profile provided (instructor handout). The profile includes name, job title, department, manager name, and a list of systems they use.

### Step 4.2: Develop a Call Script

Write a vishing call script for the following scenario: You are calling as an IT security analyst. A "security alert" has flagged the target's account for unusual login activity. You need them to verify their identity and confirm their current password so you can unlock their account.

Your script must include:

1. Opening (introduction and establishment of credibility)
2. Urgency building (the security problem)
3. Verification request (ask for information)
4. Objection handling (for at least two common challenges)
5. Graceful exit (whether successful or not)

**Lab Report Item 9:** Submit your complete vishing script. Highlight in bold every Cialdini influence principle you deliberately employed. Then write a 100-word paragraph explaining the ethical boundary: at what point would this pretext cross from authorized security testing into impermissible manipulation?

---

## Part 5: Report Writing (30 minutes)

### Step 5.1: Write the Phishing Campaign Finding

Using the campaign results from Part 3, write a professional penetration test finding in the following format:

**Finding: Employee Susceptibility to Credential Phishing**

**Risk Rating:** [Critical/High/Medium/Low — justify]

**CVSS Score:** [calculate and show]

**Description:** [2–3 sentence technical description]

**Evidence:** [Reference the screenshot from Lab Report Item 7]

**Impact:** [What could an attacker do with captured credentials?]

**Remediation:** [At least three specific, prioritized recommendations]

**Lab Report Item 10:** Submit the complete formatted finding.

---

## Lab Report Submission

Your lab report must include:

- Lab Report Items 1–10 with all screenshots
- Campaign metrics table (Lab Report Item 8)
- Vishing script with analysis (Lab Report Item 9)
- Professional penetration test finding (Lab Report Item 10)

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Cleanup Procedures

1. Do not delete the campaign — the instructor will review campaign data for grading.
2. Log out of the GoPhish admin panel.
3. Delete any locally downloaded CSV files containing fictional employee data.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| GoPhish setup and configuration screenshots (Items 1–4) | 20 |
| Campaign analysis and metrics table (Items 5–8) | 35 |
| Vishing script with ethical analysis (Item 9) | 25 |
| Professional penetration test finding (Item 10) | 20 |
| **Total** | **100** |

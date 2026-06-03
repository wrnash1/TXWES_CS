# Reading Guide: Module 11 — Social Engineering Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

Social engineering exploits human psychology rather than technical vulnerabilities. This reading guide provides the theoretical and practical foundation for authorized social engineering assessments, including phishing simulations, vishing, pretexting, and employee awareness measurement. All techniques described require explicit written authorization from the organization being tested.

---

## Learning Objectives

After completing this module, students will be able to:

1. Describe the psychological principles that underlie social engineering attacks.
2. Design an authorized phishing campaign using GoPhish, including infrastructure setup, template creation, and metrics collection.
3. Develop a credible vishing pretext and explain the ethical constraints on impersonation.
4. Apply OSINT techniques to support pretext development.
5. Measure and report employee security awareness metrics.
6. Explain the ethical obligations specific to social engineering testing.
7. Map social engineering findings to PT0-002 exam objectives.

---

## Section 1: Psychology of Social Engineering

### 1.1 Cialdini's Principles of Influence

Robert Cialdini's foundational research on influence identifies six principles that social engineers exploit systematically:

**Reciprocity:** People feel obligated to return favors. An attacker who offers something first (a helpful tip, a small gift) increases compliance with subsequent requests.

**Commitment and Consistency:** Once people commit to a position or action, they prefer to remain consistent with that commitment. Getting a small "yes" (confirming your name and department) primes targets for a larger ask.

**Social Proof:** People look to others' behavior when uncertain. "Your colleagues have already updated their credentials" implies compliance is the norm.

**Authority:** People defer to perceived experts and authority figures. An "IT security audit" call from someone who sounds knowledgeable and confident achieves disproportionate compliance.

**Liking:** People comply more readily with requests from people they like. Building rapport before making a request significantly increases success rates.

**Scarcity:** Limited availability or time pressure impairs rational decision-making. "Your account will be locked in 10 minutes unless you verify" exploits this.

### 1.2 The Attack of the Moment

Social engineers study their targets' context. Attacking during a moment of stress, distraction, or transition increases success. New employees are more susceptible (uncertain about procedures), employees during major IT transitions (new email systems, policy updates) are more susceptible (confused about what is legitimate), and employees facing deadline pressure are more susceptible (less time to scrutinize requests).

### 1.3 Fear, Uncertainty, and Doubt

FUD (Fear, Uncertainty, Doubt) is a classic manipulation framework. Creating mild anxiety about a potential problem motivates action: "We have detected suspicious activity on your account" triggers both fear (my account may be compromised) and urgency (I should fix this now) without making a specific false claim.

---

## Section 2: Phishing Campaign Design

### 2.1 Pre-Campaign OSINT

Before designing a phishing campaign, thorough OSINT establishes the context needed to build credible pretexts.

**LinkedIn intelligence:**

- Organizational hierarchy (who reports to whom)
- Job titles and department names
- Recent hires and departures
- Skill endorsements (revealing technologies in use)
- Company updates (current projects, announcements)

**Company website intelligence:**

- Employee directory (where public)
- Press releases (executive announcements, product launches, acquisitions)
- Technology stack clues (job postings mention specific technologies)
- Email format inference (firstname.lastname@company.com)

**Email format validation:** Use the discovered format with free validation tools (Hunter.io, Clearbit) to confirm the pattern. A single confirmed email address reveals the format for all others.

### 2.2 Phishing Template Design

Effective phishing templates balance credibility with the testing goal.

**High-credibility elements:**

- Correct company logos and branding
- Real employee names and titles in the From/Signature fields
- References to real company events or systems
- Correct email domain (spoofed or typosquatted)
- Professional formatting identical to legitimate communications

**Call-to-action design:**

The template should request one specific action. Credential capture pages measure the most serious risk. Link-click tracking (without credential capture) measures engagement. File download simulations test endpoint security and DLP controls.

### 2.3 Credential Capture vs. Awareness Testing

Campaigns with credential capture pages reveal the most serious risk (employees willingly providing usernames and passwords to unknown sites) but also carry the highest data sensitivity burden. All submitted credentials must be immediately invalidated or, if real credentials are captured, the client must be notified immediately for forced password resets.

Campaigns that only track clicks without capturing credentials are lower risk and often sufficient for measuring susceptibility. The client and tester should agree on the approach in advance.

---

## Section 3: GoPhish Technical Implementation

### 3.1 Infrastructure Setup

GoPhish should be hosted on dedicated testing infrastructure, not on the tester's personal machine or corporate network. Key infrastructure requirements:

**Domain registration:** Register a domain visually similar to the target. Techniques include:

- Typosquatting: `verizon-security.com` instead of `verizon.com`
- Homoglyph attacks: Using visually similar Unicode characters (rarely effective now due to browser punycode display)
- Subdomain spoofing: `verizon.com.security-alert.net`
- TLD variation: `verizon.net`, `verizon.org`

**Email authentication records:**

Configure SPF, DKIM, and DMARC to maximize deliverability:

```
# SPF (TXT record at domain root)
v=spf1 ip4:YOUR_IP -all

# DMARC (TXT record at _dmarc subdomain)
v=DMARC1; p=none; rua=mailto:reports@yourdomain.com
```

**VPS selection:** Choose a hosting provider whose IP ranges are not blocklisted. Test deliverability before the campaign using tools like mail-tester.com.

### 3.2 GoPhish Configuration

GoPhish stores its configuration in `config.json`:

```json
{
  "admin_server": {
    "listen_url": "127.0.0.1:3333",
    "use_tls": true
  },
  "phish_server": {
    "listen_url": "0.0.0.0:80",
    "use_tls": false
  }
}
```

Always bind the admin interface to localhost or a trusted IP. Exposing the GoPhish admin panel to the internet exposes campaign data.

### 3.3 Template Variables

GoPhish templates support several variables:

| Variable | Value |
|----------|-------|
| `{{.FirstName}}` | Target's first name |
| `{{.LastName}}` | Target's last name |
| `{{.Email}}` | Target's email address |
| `{{.URL}}` | Unique tracking link |
| `{{.From}}` | Sender address |

The `{{.URL}}` variable generates a unique link per recipient, enabling individual tracking. Do not share this URL format outside the testing team — the tracking mechanism should not be apparent to targets.

### 3.4 Interpreting Campaign Results

GoPhish exports campaign results as CSV with per-event timestamps. Key metrics:

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| Open rate | Opens ÷ Delivered | 30–50% (email-dependent) |
| Click rate | Clicks ÷ Delivered | Industry average ~15–25% |
| Submission rate | Submissions ÷ Clicked | High = credential theft risk |
| Report rate | Reports ÷ Delivered | Goal: maximize this |

The time-to-click metric is also valuable. If 80% of clicks occur within 5 minutes of email delivery, targeted spear phishing during a busy time would have high effectiveness.

---

## Section 4: Vishing Techniques

### 4.1 Call Flow Design

A vishing assessment call follows a planned but adaptable flow:

1. **Opening:** State who you are (fictional identity), where you're from, and why you're calling. Be confident. Uncertainty invites suspicion.

2. **Credibility building:** Reference internal systems, recent events, or known colleagues. This establishes that you have insider knowledge.

3. **Need establishment:** Explain what you need and why. The reason should be urgent, routine, and plausible simultaneously.

4. **Objection handling:** Prepare responses to common challenges: "Can I call you back?" (provide a callback number that routes to your testing infrastructure), "Let me verify with my manager" (escalate urgency slightly), "I'll just submit a ticket" (explain why that won't resolve the issue in time).

5. **Request:** Make the specific ask clearly and confidently.

6. **Graceful exit:** Whether successful or not, end the call naturally. Do not reveal the test; maintain the pretext until the engagement concludes.

### 4.2 Caller ID Spoofing

Authorized vishing tests often use caller ID spoofing to display the target organization's main number or helpdesk number. Services like SpoofCard and VoIP.ms (and the Metasploit module `auxiliary/voip/callerID_spoof`) enable this in authorized testing contexts.

Legal note: The Truth in Caller ID Act (18 U.S.C. § 2326 note) prohibits spoofing with intent to defraud or harm. For authorized security testing, this prohibition does not apply, but get this authorization explicitly documented.

### 4.3 Vishing Metrics

Unlike phishing, vishing campaigns are typically smaller in scale but higher in impact per contact. Document:

- Number of calls attempted
- Number of calls completed
- Number of successful information disclosures or actions
- Type of information disclosed (password, access codes, internal system names)
- Average call duration
- Number of targets who suspected or challenged the caller

---

## Section 5: Ethical Framework for Social Engineering Testing

### 5.1 The Consent Hierarchy

Social engineering testing involves a consent asymmetry: the organization has consented to the test, but individual employees have not. This is legally acceptable but creates ethical obligations:

The organization's consent is sufficient for legal protection, but ethical practice requires minimizing harm to individual employees who are deceived as part of an authorized test.

### 5.2 Prohibited Pretext Categories

Regardless of written authorization, the following pretext types exceed ethical boundaries:

- Impersonating law enforcement (federal crime)
- Pretexts involving fabricated family emergencies or deaths
- Threats of job termination or legal action for non-compliance
- Impersonating medical personnel or fabricating health emergencies
- Pretexts targeting known vulnerable individuals (employees on medical leave, recently bereaved)

### 5.3 Data Handling Requirements

Credentials captured during a social engineering engagement are among the most sensitive data the tester will handle. Requirements:

- Encrypt captured credentials at rest immediately
- Limit access to testing team leads only
- Delete captured credentials at engagement end (or hand to client for forced reset)
- Never use captured credentials for any additional access beyond confirming validity
- Document the data handling process in the final report

### 5.4 Notification and Debrief

After the campaign concludes, a debrief serves both legal and cultural purposes. Employees who discover they were tested and not told may feel violated and mistrustful. A post-campaign communication from leadership that acknowledges the test, presents aggregate results, and announces follow-up training converts the test from a "gotcha" into a learning moment.

---

## Section 6: PT0-002 Exam Alignment

### 6.1 Social Engineering Attack Types

The PT0-002 exam requires students to identify and differentiate:

- Phishing, spear phishing, whaling, vishing, smishing
- Pretexting, elicitation, shoulder surfing, tailgating
- Baiting (infected USB, fake downloads)
- Quid pro quo (trading fake help for information)
- Watering hole (compromising sites the target visits)

### 6.2 Exam Scenario Patterns

Common PT0-002 scenarios involving social engineering:

A tester receives approval to test the organization's human element. Which tool would be MOST appropriate? (GoPhish)

During a vishing call, the target asks for the caller's employee ID number. Which response is BEST? (Provide a plausible fictional number — maintaining the pretext is part of the authorized test)

A phishing campaign captures 45 sets of real employee credentials. What is the FIRST action the tester should take? (Immediately notify the client so passwords can be forced-reset, then secure the credential data)

---

## Key Terms

**Phishing:** Deceptive email-based attack designed to manipulate recipients into taking harmful actions.

**Spear phishing:** Targeted phishing using personal details to increase credibility.

**Vishing:** Voice-based social engineering via telephone.

**Pretexting:** Creating a fabricated scenario to manipulate a target.

**Elicitation:** Extracting information through casual conversation without direct requests.

**Baiting:** Leaving physical or digital lures (infected USB drives) for targets to find.

**GoPhish:** Open-source phishing simulation framework.

**DMARC:** Domain-based Message Authentication, Reporting and Conformance — email authentication policy standard.

**Open rate:** Percentage of phishing email recipients who opened the message.

**Submission rate:** Percentage of recipients who submitted information to the phishing landing page.

---

## Review Questions

1. Describe three psychological principles from Cialdini's influence framework and explain how each is exploited in a phishing email.

2. What DNS records should be configured before launching a phishing campaign, and what does each accomplish?

3. Explain the difference between spear phishing and whaling. What OSINT sources would you use to develop targeting information for each?

4. A vishing test captures an employee's Active Directory password. What are the immediate steps the penetration tester must take?

5. What is the "no shaming" principle in social engineering reporting, and why is it important both ethically and practically?

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives, Domain 1.4, 2.1, 3.5
- Cialdini, R. B. (2006). *Influence: The Psychology of Persuasion.* Harper Business.
- Verizon DBIR (2023). Data Breach Investigations Report. verizon.com/business/resources/reports/dbir/
- GoPhish Documentation: https://docs.getgophish.com
- Hadnagy, C. (2010). *Social Engineering: The Art of Human Hacking.* Wiley.
- Truth in Caller ID Act, 47 U.S.C. § 227(e).

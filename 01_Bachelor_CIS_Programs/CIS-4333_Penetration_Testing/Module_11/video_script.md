# Video Script: Module 11 — Social Engineering Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Segments:** 6
- **Visual Aids:** GoPhish dashboard screenshots, phishing email examples (authorized), campaign metrics
- **Lab Environment:** Isolated GoPhish server, authorized test domain only

---

## Segment 1: The Human Element in Security (Lines 1–35)

[SLIDE: Module 11 Title Card]

Welcome to Module 11. We are shifting our focus from technical exploits to what is consistently the most successful attack vector in real-world breaches: social engineering.

Let me cite some numbers. Verizon's Data Breach Investigations Report consistently finds that over 80 percent of breaches involve a human element — phishing, stolen credentials, social manipulation. The technology stack can be hardened, patched, and monitored, but human beings are susceptible to urgency, authority, curiosity, and fear. Social engineers exploit these predictable psychological responses.

[SLIDE: Authorization is Non-Negotiable]

Before I describe a single technique, I need to be direct about authorization. Social engineering testing without explicit written authorization is illegal and deeply unethical. It involves intentional deception of real people. The client must specifically authorize social engineering as a component of the engagement. The scope document must define:

- Which employee populations are in scope (all employees vs. specific departments)
- Which attack vectors are permitted (email, phone, in-person)
- What actions constitute a successful test (click, credential submission, file download)
- What happens when an employee reports the test — the "white card" or abort protocol

Without all of this, you do not have authorization. You have a plan to harm people professionally and legally expose yourself.

[SLIDE: Why Social Engineering Testing Matters]

When properly authorized, social engineering assessments answer critical questions: How many employees would click a phishing link? Would staff provide sensitive information over the phone? Does security awareness training actually change behavior? What is the organization's baseline susceptibility, and how does it improve over time?

These answers drive meaningful security program investment. An organization that knows 35 percent of its employees click phishing links can justify and prioritize security awareness spending.

[PAUSE for transition]

---

## Segment 2: Phishing Campaign Fundamentals (Lines 36–75)

[SLIDE: Phishing Taxonomy]

Social engineering testing encompasses several attack vectors. Let us start with email-based phishing, the most common.

Phishing is a broad term for deceptive electronic communication designed to manipulate recipients into taking an action — clicking a link, submitting credentials, downloading a file, or transferring money.

Spear phishing is targeted phishing. Instead of a mass email, the attacker crafts a message specifically tailored to the target using personal details — their name, role, manager's name, recent company events.

Whaling targets senior executives. The same personalization principles apply, but the lure often relates to legal matters, board communications, or financial transactions.

Vishing is voice phishing — phone calls. Smishing is SMS phishing.

[SLIDE: Pretext Development]

A pretext is the fictional scenario that frames the attack. Effective pretexts exploit:

Authority — "This is the IT security team. We need you to verify your credentials."

Urgency — "Your account will be suspended in 2 hours unless you verify."

Fear — "We have detected unauthorized access to your account."

Curiosity — "Your package could not be delivered. Click here to reschedule."

Reciprocity — "As a thank-you for completing our survey, please click here to claim your reward."

The best pretexts combine multiple factors and are tailored to the target's context. A pretext about a "mandatory HR policy update" is more credible to an employee who recently received an HR communication.

[SLIDE: Open Source Intelligence for Pretexts]

Before crafting a phishing campaign, tester performs OSINT to build credibility. LinkedIn reveals names, job titles, department structures, and recent hires. Company press releases reveal executive names and current projects. Social media reveals personal interests and recent activities.

This information makes spear phishing emails extremely convincing. An email that mentions the target's manager by name, references a real current project, and comes from a spoofed or convincingly cloned domain will achieve far higher click rates than a generic phishing template.

[SLIDE: Phishing Metrics]

A phishing campaign produces measurable data:

- Open rate: Percentage of recipients who opened the email
- Click rate: Percentage who clicked the embedded link
- Submission rate: Percentage who submitted credentials
- Report rate: Percentage who reported the phishing attempt to IT

High report rates are actually a positive finding — they indicate effective security awareness. The ratio of submission rate to report rate tells the story of organizational security culture.

[PAUSE for transition]

---

## Segment 3: GoPhish Platform (Lines 76–115)

[SLIDE: GoPhish Overview]

GoPhish is an open-source phishing simulation framework that automates campaign management. It runs as a web application on your testing infrastructure and provides a full dashboard for campaign creation, target management, template building, and results tracking.

[SLIDE: GoPhish Architecture]

GoPhish consists of three key components:

The phishing server sends emails and hosts the landing page. It should be hosted on infrastructure the tester controls — a VPS with a convincingly registered domain, not a provider commonly blocklisted by email security gateways.

The admin interface is a web dashboard on port 3333 by default. This is where campaigns are configured and monitored.

Sending profiles define the SMTP relay configuration — how emails are sent and from what address.

[SLIDE: Campaign Setup Workflow]

Setting up a GoPhish campaign follows a defined sequence:

Step 1: Create a sending profile — configure SMTP server, from address, and header settings.

Step 2: Create a landing page — clone the target's login page or create a credential capture page. GoPhish's site import feature fetches and stores a copy of any public login page.

Step 3: Create an email template — the phishing email body. Include the tracking link using GoPhish's `{{.URL}}` template variable and the recipient's name with `{{.FirstName}}`.

Step 4: Create a user group — import the list of authorized targets as CSV.

Step 5: Create and launch a campaign — link all the above components and set the launch time.

[SLIDE: Domain Reputation and Infrastructure]

A critical operational detail: email deliverability. Modern email security gateways (Microsoft Defender, Proofpoint, Mimecast) evaluate sender reputation, SPF, DKIM, and DMARC records.

For realistic testing, configure:

SPF record: `v=spf1 ip4:[your_server_ip] -all` — authorizes your server to send for your domain.

DKIM: Cryptographically sign outgoing mail. GoPhish can use an SMTP relay that handles DKIM signing.

DMARC: Tells receiving servers what to do with SPF/DKIM failures. Start with `p=none` (monitor mode) for test infrastructure.

Age the domain 30+ days before a campaign. Fresh domains have zero reputation and are frequently filtered.

[SLIDE: Results and Reporting]

GoPhish tracks each event with a timestamp and unique identifier. The timeline view shows each target's progression: email sent → email opened → link clicked → data submitted.

For reporting, export campaign results to CSV and combine with the target list to calculate rates by department, role, and demographic cohort. This segmentation is valuable: "60% of new hires clicked vs. 15% of employees with more than 2 years tenure" tells a different story than an aggregate number.

[PAUSE for transition]

---

## Segment 4: Vishing and Pretexting (Lines 116–150)

[SLIDE: Vishing Fundamentals]

Vishing (voice phishing) uses telephone calls to manipulate targets. It is highly effective because the human voice conveys authority and emotion in ways that email cannot. Confidence, urgency, and improvisation make skilled vishers extremely successful.

In authorized testing, a visher typically calls employees impersonating:

- IT helpdesk requesting credential verification
- A vendor requesting account confirmation
- HR conducting a benefits survey
- An executive's assistant requesting urgent action

[SLIDE: Vishing Call Structure]

A vishing call follows a psychological script even when improvised:

Establish credibility: Name-drop real people, reference real systems, demonstrate knowledge of the organization.

Create pretext: Explain why you are calling and what you need.

Build rapport: Match the target's tone, use their name, be friendly.

Apply pressure: Introduce urgency or authority to accelerate compliance.

Request action: Ask for the specific information or action.

[SLIDE: Call Recording and Consent]

A legal note: many states require two-party consent for recording telephone calls. Before recording any vishing test call, confirm the applicable law for the target's jurisdiction and obtain appropriate authorization in the scope of work. Many organizations specifically request recordings as evidence; ensure the authorization covers this.

[SLIDE: Pretexting Concepts]

Pretexting is the broader practice of creating a fabricated scenario to manipulate a target. It underpins both phishing and vishing.

Effective pretexts are:

Plausible: The scenario makes sense in context. An IT helpdesk call about a security update is routine; a random survey about favorite movies is suspicious.

Internally consistent: Details align. Names, departments, and systems mentioned are real.

Responsive: The pretextor can answer follow-up questions without breaking character.

Emotionally engaging: The scenario triggers the psychological response that drives action.

[SLIDE: Legal Boundaries of Pretexting]

Federal law (18 U.S.C. § 1343 — wire fraud; 18 U.S.C. § 1030 — CFAA) and state laws impose limits on pretexting, even in authorized testing. Specifically:

- Impersonating a government official (FBI, IRS) is a federal crime under any circumstances.
- Making false statements to a financial institution violates the Gramm-Leach-Bliley Act's pretexting provisions.
- Pretexting to obtain medical information may violate HIPAA.

Authorized social engineering testing for security purposes is lawful, but these specific impersonation categories remain prohibited.

[PAUSE for transition]

---

## Segment 5: Employee Awareness Measurement and Ethical Considerations (Lines 151–195)

[SLIDE: Measuring Awareness Effectively]

The goal of social engineering testing is not to embarrass employees — it is to measure and improve the organization's security posture. This distinction drives every decision about campaign design, execution, and reporting.

Effective awareness measurement uses:

Baseline assessment: Pre-training campaign to establish current susceptibility rates.

Segmented analysis: Results by department, role seniority, and time with company.

Trending: Repeat campaigns after training to measure improvement.

Comparison benchmarks: Industry averages allow context. A 20% click rate is concerning in most industries but less alarming than the same rate in a healthcare organization handling PHI.

[SLIDE: The Ethics of Social Engineering Testing]

Authorized social engineering testing places testers in a position of significant power over real people who do not know they are being tested. This creates ethical obligations.

Proportionality: The test should be realistic but not weaponized. Pretexts that fabricate medical emergencies, death of a family member, or imminent job loss to manipulate targets cross an ethical line even if technically "authorized."

Data minimization: Capture only what is necessary to measure susceptibility. Do not retain real employee credentials beyond the engagement period, and secure them during the engagement.

No shaming: Test results must not be used to publicly identify or discipline individual employees without prior agreement with the client. The security team should receive aggregate data; HR receives individual data only for serious repeat offenders under a pre-agreed policy.

[SLIDE: The "White Card" Protocol]

Some organizations ask penetration testers to provide a "white card" — a document carried by testers that, if discovered or challenged, confirms the legitimacy of the test to the challenging party. This is standard for physical security tests.

For social engineering, the equivalent is a designated point of contact at the client who can verify the test in progress if an employee raises an alarm. The scope document should specify this contact and the process for halting a test if needed.

[SLIDE: Communicating Results to Clients]

When presenting social engineering test results:

Present data in aggregate first. Lead with organizational-level metrics, not individual names.

Frame findings constructively. "35% of employees in the finance department submitted credentials" is an actionable finding. "Here is a list of employees who failed" is a morale-damaging deliverable that rarely improves security.

Link findings to remediation. Security awareness training, simulated phishing programs, and reporting culture improvements are all measurable outcomes. Recommend specific, actionable next steps.

[PAUSE for transition]

---

## Segment 6: PT0-002 Alignment and Module Summary (Lines 196–240)

[SLIDE: PT0-002 Exam Objectives — Social Engineering]

Social engineering appears in multiple PT0-002 domains:

Domain 1 (Planning and Scoping): Rules of engagement for social engineering, authorization requirements, privacy considerations.

Domain 2 (Recon): OSINT techniques used in pretext development.

Domain 3 (Attacks): Specific social engineering attack types — phishing, vishing, smishing, pretexting, tailgating, shoulder surfing, elicitation, impersonation.

Domain 4 (Reporting): Documenting social engineering findings, awareness measurement metrics, remediation recommendations.

[SLIDE: Key Social Engineering Terms for the Exam]

Know these terms for PT0-002:

Elicitation: Extracting information through seemingly casual conversation, without making a direct request.

Shoulder surfing: Observing sensitive information by watching over a target's shoulder.

Tailgating/piggybacking: Following an authorized person through a secured entrance.

Pretexting: Creating a fabricated scenario to manipulate a target into providing information.

Baiting: Leaving infected media (USB drives) for targets to find and use.

Quid pro quo: Offering something of value in exchange for information or access.

[SLIDE: Common Exam Scenarios]

The PT0-002 exam frequently presents scenarios where the student must identify:

- Which attack vector is being described
- Whether the described action requires additional authorization
- What metrics indicate success in a social engineering campaign
- How to present findings ethically and constructively

[SLIDE: Module Summary]

Module 11 covered the full spectrum of social engineering testing: phishing campaign design and execution with GoPhish, vishing techniques and call structure, pretext development grounded in OSINT, employee awareness measurement methodologies, and the ethical obligations that govern authorized social engineering work.

Authorization is the foundation. Ethics is the framework. Measurement is the purpose.

Your lab for this module simulates a complete GoPhish campaign against an isolated test environment, allowing you to build, execute, and analyze a phishing simulation from end to end.

[END RECORDING]

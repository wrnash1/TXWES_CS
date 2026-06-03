# Reading Guide: Module 08 — Security Awareness and Training Programs

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Introduction

Module 08 addresses the human dimension of information security — the design, delivery, measurement, and culture-change dimensions of security awareness and training programs. The human element remains the most consistently exploited attack surface in the industry, making a well-managed awareness program one of the highest-value investments in a security portfolio.

CISM Domain 3 explicitly includes workforce training and awareness as a required program component. Candidates must understand not only what awareness programs contain but how to design them for measurable behavioral outcomes, how to measure their effectiveness, and how to build the organizational culture that sustains security behaviors over time.

---

## 1. Awareness, Training, and Education — The Three Levels

### 1.1 Definitions and Distinctions

| Level | Target Audience | Goal | Depth | Example |
|---|---|---|---|---|
| Awareness | All employees | Recognize threats; change daily behavior | Broad, surface-level | Annual phishing recognition training |
| Training | Role-specific groups | Develop specific skills and competencies | Moderate, skill-focused | Secure coding workshop for developers |
| Education | Security professionals | Build conceptual and theoretical foundations | Deep, formal | CISM certification program |

The CISM exam and NIST SP 800-50 use these three levels explicitly. Confusing awareness with training — treating them as interchangeable — is a frequent exam error.

### 1.2 Regulatory Training Requirements

Many regulatory frameworks mandate specific training content and frequencies. Security managers must understand these obligations when designing programs.

| Regulation | Training Requirement |
|---|---|
| HIPAA Security Rule | Annual security awareness training for all workforce members who handle ePHI |
| PCI DSS v4.0 (Req 12.6) | Formal security awareness program; training at hire and annually; phishing awareness |
| GLBA Safeguards Rule | Employee training as part of the written information security program |
| NIST SP 800-53 (AT Family) | Awareness and training controls for federal systems and their contractors |
| SOX | No specific training mandate; auditors expect reasonable workforce awareness controls |

---

## 2. Program Design — The ADDIE Model

### 2.1 ADDIE Framework Applied to Security Training

The ADDIE model (Analyze, Design, Develop, Implement, Evaluate) provides a disciplined approach to training development that produces programs with measurable behavioral outcomes rather than compliance checkboxes.

| Phase | Key Activities | Output |
|---|---|---|
| Analyze | Audience segmentation, behavior gap analysis, regulatory requirements review, threat landscape review | Needs assessment report; audience segments |
| Design | Learning objectives per segment, content outline, delivery method selection, assessment design | Design document; learning objectives |
| Develop | Content creation or acquisition, LMS configuration, simulation campaign setup | Training modules; simulation templates |
| Implement | Deployment schedule, manager communication, completion tracking, LMS administration | Deployed program; completion records |
| Evaluate | Kirkpatrick-level measurement, metric reporting, continuous improvement | Measurement report; program updates |

### 2.2 Writing Effective Learning Objectives

Learning objectives must be behavioral and measurable. The difference between a vague objective and an effective one determines whether you can measure success.

| Ineffective Objective | Effective Behavioral Objective |
|---|---|
| Understand phishing threats | Identify three characteristics of phishing emails and report suspicious messages using the company reporting tool |
| Know the data classification policy | Classify a document correctly using the four-level classification scheme and apply appropriate handling procedures |
| Be aware of password requirements | Create a password meeting policy requirements and configure MFA on all assigned accounts |

The test: can you observe whether an employee achieved this objective? If yes, it is measurable. If no, redesign it.

### 2.3 Audience Segmentation

A segmented program delivers content relevant to the specific risks each role faces, in language appropriate to their technical background, through channels they actually use.

| Audience Segment | Primary Risk Focus | Preferred Delivery |
|---|---|---|
| All employees | Phishing, social engineering, password hygiene, physical security | CBT, simulation, environmental cues |
| IT staff | Privileged access abuse, misconfiguration, patch management | Technical workshops, CBT, procedure training |
| Developers | Secure coding, OWASP Top 10, secrets management | Hands-on labs, secure coding courses |
| Finance and HR | Wire fraud, BEC, payroll fraud, PII handling | Scenario-based CBT, case studies |
| Executives | Regulatory accountability, board governance, cyber risk | Executive briefings, peer roundtables |
| Customer service | Social engineering via phone, verification procedures | Role-play exercises, scenario CBT |

---

## 3. Delivery Methods

### 3.1 Delivery Method Comparison

| Method | Engagement Level | Scalability | Cost | Best For |
|---|---|---|---|---|
| Instructor-led (in person) | High | Low | High | New hire orientation, high-risk roles, executive sessions |
| Live virtual classroom | Medium-High | Medium | Medium | Distributed teams, interactive workshops |
| Computer-based training (CBT) | Medium | High | Low per user | Organization-wide annual training, compliance documentation |
| Simulated phishing | High (at moment of failure) | High | Medium | Behavioral conditioning, measurement |
| Microlearning (2–5 min modules) | Medium | High | Low per unit | Reinforcement, just-in-time delivery |
| Posters and environmental cues | Low | Very High | Very Low | Ambient reinforcement, campaign support |
| Newsletters and communications | Low-Medium | High | Low | Ongoing awareness, threat-of-the-month updates |
| Gamification | High | Medium | Medium-High | Competitive environments, younger workforces |

### 3.2 Simulated Phishing — Design Principles

Phishing simulation is the single most effective behavioral measurement and training tool for the broad employee population. Key design principles:

- Use templates that reflect current real-world threats, not generic decade-old lures
- Vary difficulty across campaigns — easy lures to establish baseline, harder lures to test improvement
- Deliver immediate, non-punitive teachable moment feedback to users who click
- Track click rate, credential submission rate, and reporting rate as separate metrics
- Never use simulation to embarrass or punish — it destroys trust and reduces reporting behavior
- Test all employee populations including executives; treat them identically
- Run campaigns at irregular intervals (not predictable monthly on the same day)

### 3.3 The 70-20-10 Learning Model

The 70-20-10 model, drawn from organizational learning research, suggests that approximately 70 percent of effective learning comes from on-the-job experience, 20 percent from social learning and feedback from others, and 10 percent from formal training.

For security awareness program design, this means formal training (CBT, instructor-led) represents only the foundation. The majority of security learning comes from doing — experiencing simulations, receiving feedback, making decisions with security implications — and from the social reinforcement of peer behavior and leadership modeling.

---

## 4. Measuring Program Effectiveness

### 4.1 The Kirkpatrick Four-Level Model

The Kirkpatrick model is the industry standard for training evaluation and maps directly to CISM exam content.

| Level | Name | Measurement Approach | Maturity Required |
|---|---|---|---|
| 1 | Reaction | Post-training satisfaction surveys | Basic |
| 2 | Learning | Knowledge assessment scores, quiz pass rates | Basic |
| 3 | Behavior | Phishing click rates, policy violation rates, reporting rates | Intermediate |
| 4 | Results | Security incident rates, breach costs, regulatory findings | Advanced |

Most organizations measure at Levels 1 and 2 only. A mature program measures at Levels 3 and 4, which requires pre-program baseline data and multi-year tracking.

### 4.2 Key Performance Indicators by Program Component

| Program Component | KPI | Target Trend |
|---|---|---|
| Phishing simulation | Click rate | Decreasing year-over-year |
| Phishing simulation | Credential submission rate | Decreasing year-over-year |
| Phishing simulation | Reporting rate | Increasing year-over-year |
| CBT completion | Completion rate | 95%+ organization-wide |
| CBT completion | Assessment pass rate | 85%+ first attempt |
| Incident reporting | Reports submitted per quarter | Increasing (indicates healthy culture) |
| Policy violations | Repeat violations per employee | Decreasing |
| Phishing incidents | Real phishing incidents attributed to employee behavior | Decreasing |

### 4.3 Reporting to Leadership

Security awareness metrics should be presented to leadership in business terms, not technical statistics. Instead of "our phishing click rate decreased from 18% to 9%," present it as "we cut the number of employees vulnerable to phishing attacks in half over 12 months, reducing the likelihood of a credential-based breach by an estimated 50%."

---

## 5. Security Culture Change

### 5.1 What Security Culture Is

Security culture is the aggregate of shared attitudes, beliefs, and behaviors regarding security within an organization. It is evidenced by what employees do when no one is watching: whether they lock screens, question suspicious requests, report anomalies, and treat security as a shared responsibility rather than an IT problem.

Culture is distinct from compliance. A compliant organization does the minimum required. A culture-mature organization does what is right because employees understand why it matters.

### 5.2 The Culture Maturity Continuum

| Stage | Characteristics | Management Intervention |
|---|---|---|
| 1 — Non-Existent | Security ignored; violations common; no awareness | Basic mandatory training; establish policies |
| 2 — Compliance-Driven | Training completed to avoid consequences; minimal engagement | Improve content relevance; add role-specific content |
| 3 — Aware | Employees recognize threats; report incidents | Reinforce through leadership modeling; add measurement |
| 4 — Proactive | Employees actively participate; question security of new processes | Build recognition programs; embed in hiring/performance |
| 5 — Optimizing | Security considered in all decisions; employees advocate for it | Maintain and evolve; celebrate security contributions |

### 5.3 Leadership Behaviors That Drive Culture

Research in organizational culture consistently identifies leadership behavior as the primary driver of culture. For security, this means:

- Executives participating in phishing simulations without exemption
- Leaders visibly following security policies (MFA, clean desk, badge use)
- Security incidents discussed openly without blame culture to encourage reporting
- Security resources funded adequately, signaling that leadership values it
- Security outcomes included in executive performance reviews

### 5.4 Role-Based Training Depth Reference

| Role | Required Training Topics | Frequency |
|---|---|---|
| All employees | Phishing, social engineering, passwords, physical security, reporting | Annually + quarterly simulations |
| IT administrators | Privileged access, patch procedures, configuration baselines, incident response | Annually + role-specific updates |
| Software developers | OWASP Top 10, secure SDLC, code review, secrets management | Annually + project-specific |
| Finance personnel | BEC/wire fraud, verification procedures, PII handling | Annually + simulations targeting finance lures |
| HR personnel | Social engineering via recruiting channels, PII protection, background check data | Annually + targeted simulations |
| Security team | Advanced threat intelligence, incident response, forensics | Continuously (CPE/certification maintenance) |
| Executives | Risk governance, regulatory accountability, cyber insurance, tabletop exercises | Annually + board briefings |

---

## 6. CISM Exam Tips — Module 08

**Awareness vs. training distinction:**

- The exam uses these terms precisely — awareness is for all employees and focuses on recognition; training is role-specific and builds skills
- A question asking about reducing phishing susceptibility organization-wide is asking about awareness, not training
- A question about developers writing secure code is asking about training, not awareness

**ADDIE model:**

- Analyze comes first — you cannot design an effective program without understanding your audience and behavior gaps
- Evaluate is ongoing, not a one-time end-state
- The exam will present scenarios where an organization skipped Analysis; the answer will involve identifying that the program failed because it was not designed for the actual audience

**Kirkpatrick model:**

- Know all four levels by number and name
- Level 3 (Behavior) is the most relevant for security program managers — it measures actual behavior change
- The exam may present a scenario where an organization only measures Level 1 (satisfaction) and concludes the program is effective; the correct answer identifies this as an insufficient measurement approach

**Security culture:**

- Culture change requires leadership modeling, not just training content
- The exam recognizes that compliance-driven training produces compliance, not culture
- Untreated blame culture actively undermines security reporting — employees who fear punishment for mistakes stop reporting incidents

---

## 7. Key Terms Glossary

| Term | Definition |
|---|---|
| Security awareness | Broad-based program helping all employees recognize threats and understand their role in security |
| Security training | Role-specific skill development for employees with defined security responsibilities |
| Security education | Formal academic or professional development building deep conceptual security knowledge |
| ADDIE model | Instructional design framework: Analyze, Design, Develop, Implement, Evaluate |
| Kirkpatrick model | Four-level training evaluation framework: Reaction, Learning, Behavior, Results |
| Simulated phishing | Controlled phishing campaigns to measure employee susceptibility and deliver teachable moments |
| Microlearning | Short (2–5 minute) training modules delivering a single focused behavioral message |
| Just-in-time training | Training triggered at the moment of a relevant behavior to maximize retention |
| Security culture | Shared organizational attitudes, beliefs, and behaviors regarding security |
| Role-based training | Training content tailored to the specific security risks and responsibilities of a job function |
| Click rate | Percentage of employees who click a simulated phishing link; primary phishing simulation metric |
| Reporting rate | Percentage of employees who report a suspicious or simulated phishing message |
| Behavior gap analysis | Assessment of the difference between current and desired security behaviors in a workforce |

---

## 8. Required and Recommended Readings

**Required (Zero-Textbook-Cost resources):**

- NIST SP 800-50: Building an Information Technology Security Awareness and Training Program — [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-50/final) — Comprehensive guidance on awareness and training program design
- NIST SP 800-16 Rev 1: A Role-Based Model for Federal Information Technology/Cybersecurity Training — [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-16/rev-1/final) — Role-based training framework

**Recommended:**

- SANS Security Awareness Maturity Model — [sans.org/security-awareness-training](https://www.sans.org/security-awareness-training/resources/maturity-model/) — Five-stage maturity model for program assessment
- Verizon Data Breach Investigations Report (current year) — [verizon.com/dbir](https://www.verizon.com/business/resources/reports/dbir/) — Annual quantification of the human element in breaches

---

## 9. Study Checklist

- [ ] Distinguish security awareness, training, and education with examples of each
- [ ] Apply the ADDIE model to a security training design scenario
- [ ] Write a measurable behavioral learning objective for a given security topic
- [ ] Name all four Kirkpatrick levels and identify which is most relevant for security behavior change
- [ ] Describe the design principles for an effective phishing simulation program
- [ ] Identify the key metrics for measuring awareness program effectiveness
- [ ] Explain the difference between a compliance-driven culture and a security culture, and identify what leadership behaviors drive the transition
- [ ] Complete the Module 08 lab (role-based training curriculum design)
- [ ] Take the Module 08 quiz
- [ ] Post to the Module 08 discussion forum by Wednesday 11:59 PM

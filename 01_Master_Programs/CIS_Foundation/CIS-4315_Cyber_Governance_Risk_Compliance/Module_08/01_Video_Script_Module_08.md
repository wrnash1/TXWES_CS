# Video Script: Module 08 — Security Awareness and Training Programs

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Pre-Roll Slide

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Introduction (0:00–1:30)

[SHOW SLIDE: Module 08 Title Card — Security Awareness and Training Programs]

Welcome back, everyone. I'm Professor Nash, and this is Module 08 of CIS-4315.

In Modules 06 and 07 we built the charter, the policies, the architecture, and the controls. Now we need to address the factor that undermines all of those investments if ignored: people. Specifically, how do you build a security awareness and training program that actually changes behavior?

[PAUSE]

This is one of my favorite topics in the course because it lives at the intersection of security management and organizational psychology. You can have the best firewall in the world, the most carefully written policies, and a comprehensive control framework — and a single untrained employee clicking a phishing link can defeat all of it in seconds. The 2021 Verizon Data Breach Investigations Report found that 85 percent of breaches involved the human element. That number has remained stubbornly consistent for a decade.

[SHOW SLIDE: Module 08 Learning Objectives]

Today we're covering four major areas: designing an effective awareness and training program, delivery methods and their trade-offs, measuring program effectiveness, and driving culture change — the hardest part of this entire discipline.

Let's get into it.

---

## Section 1: Designing an Effective Security Awareness Program (1:30–6:30)

[SHOW SLIDE: Awareness vs. Training — A Critical Distinction]

First, let's be precise about terms, because the CISM exam uses them carefully. Security awareness and security training are not the same thing.

Security awareness is about recognizing threats and knowing that your behavior matters. Awareness programs target all employees. The goal is changed behavior: recognizing a phishing email, using a strong password, locking a workstation when stepping away.

Security training is about developing specific skills and competencies. Training programs target defined roles. A developer needs secure coding training. An incident responder needs forensics and containment procedures. A payroll administrator needs social engineering resistance training.

[PAUSE]

And then there's security education, which is the deepest level — formal degree programs, professional certifications like CISM or CISSP, and academic coursework. Education builds the conceptual foundations that training and awareness build upon.

[SHOW SLIDE: Know Your Audience First]

Effective program design starts with audience analysis. A single generic awareness program delivered identically to the factory floor, the IT department, the finance team, and the executive leadership team is almost guaranteed to fail. It will be too technical for some, too basic for others, and irrelevant to most.

[PAUSE]

Audience analysis asks: What are the security risks specific to this role? What behaviors do we need to change? What existing behaviors are we reinforcing? What level of technical depth is appropriate? What communication channels reach this audience effectively?

The output of this analysis is a segmented program where different employee populations receive different content, delivered through different channels, at different frequencies.

[SHOW SLIDE: The ADDIE Model Applied to Security Training Design]

A useful framework for training design is ADDIE: Analyze, Design, Develop, Implement, and Evaluate.

Analyze: Identify the target audience, current behavior gaps, and regulatory requirements. If you're in healthcare, HIPAA requires specific workforce training on PHI handling. If you're in financial services, you likely have SOX and GLBA training obligations.

Design: Define the learning objectives. What should employees be able to do differently after completing this training? Learning objectives must be behavioral and measurable — not "understand phishing" but "identify and report phishing emails using the company's one-click reporting tool."

[PAUSE]

Develop: Create or acquire the content. This is where most organizations spend too much time — on graphics and production values rather than behavioral design. Content should be engaging but the learning design is what produces behavior change, not the production quality.

Implement: Deploy the training. Timing, platform, and communication matter here. We'll cover delivery methods in the next section.

Evaluate: Measure whether the program worked. We'll cover measurement in Section 3.

---

## Section 2: Delivery Methods and Their Trade-offs (6:30–12:00)

[SHOW SLIDE: The Spectrum of Delivery Methods]

One of the most common mistakes in security awareness programs is relying on a single delivery method. People learn differently, and no single channel reaches everyone effectively. Effective programs use a mix of delivery methods.

[PAUSE]

[SHOW SLIDE: Instructor-Led Training]

Instructor-led training — whether in person or via live virtual classroom — has the highest engagement potential of any delivery method. A skilled instructor can respond to questions in real time, adjust pacing for the audience, and use interactive exercises that purely passive formats cannot match.

The trade-offs: it's expensive, it doesn't scale easily to thousands of employees, and the quality is highly dependent on the instructor. Instructor-led training is best used for high-risk roles, new hire orientation, and executive briefings.

[SHOW SLIDE: Computer-Based Training]

Computer-based training, or CBT, is the workhorse of most enterprise security awareness programs. It scales to any size organization, can be completed on-demand, provides consistent content, and generates completion records for compliance reporting.

[PAUSE]

The trade-offs: engagement is typically lower than instructor-led, passive click-through compliance is common without behavioral reinforcement, and the same module deployed year after year stops changing behavior. CBT works best when it is role-specific, short (under 15 minutes per module), and paired with reinforcement mechanisms.

[SHOW SLIDE: Simulated Phishing]

Simulated phishing campaigns are one of the highest-value tools in the security awareness toolkit. The methodology is straightforward: send fake phishing emails to employees, measure click rates, capture credential entry rates, and — critically — provide immediate teachable moment feedback to those who fall for the simulation.

The immediate feedback loop is what makes phishing simulation effective. When an employee clicks a link and immediately sees "This was a phishing simulation. Here's what you should have noticed," the lesson is delivered at the moment of maximum cognitive engagement.

[PAUSE]

Key program management considerations: vary the simulation templates to reflect current real-world threats, never shame employees publicly, track trends over time rather than punishing individual failures, and use simulations as a diagnostic tool to identify populations needing additional training.

[SHOW SLIDE: Microlearning and Just-in-Time Training]

Microlearning delivers content in very short bursts — two to five minutes — focused on a single behavioral topic. Research in learning science consistently shows that shorter, more frequent content outperforms annual marathon training sessions for behavioral retention.

Just-in-time training takes this further by triggering training at the moment of a relevant behavior. When an employee attempts to send an email containing what appears to be a Social Security number, a popup reminding them of the data classification policy and asking them to confirm they intend to send it is a form of just-in-time intervention.

[PAUSE]

[SHOW SLIDE: Printed Materials, Posters, and Environmental Cues]

Don't dismiss physical and environmental awareness tools. Security awareness posters in high-traffic areas serve as persistent reinforcement of key messages. Quick-reference cards near workstations, screen savers with security messages, and digital signage on common area displays all contribute to the ambient security culture.

These tools don't change behavior on their own, but they reinforce the messages delivered through more intensive training channels and signal that security is a continuous organizational priority rather than an annual checkbox.

---

## Section 3: Measuring Program Effectiveness (12:00–16:30)

[SHOW SLIDE: If You Can't Measure It, You Can't Manage It]

The most common weakness in security awareness programs is the inability to demonstrate effectiveness. Organizations invest significant resources in training but measure nothing beyond completion rates. "100 percent of employees completed annual security awareness training" tells you essentially nothing about whether behavior changed or risk was reduced.

[PAUSE]

Effective measurement requires defining what you're trying to change before you design the program, then measuring whether it changed.

[SHOW SLIDE: The Four Levels of Training Evaluation]

The Kirkpatrick model provides a useful four-level measurement framework.

Level 1 — Reaction: Did participants find the training valuable? Post-training surveys. Useful for content improvement but weakly correlated with behavior change.

Level 2 — Learning: Did participants acquire the intended knowledge or skill? Knowledge assessments, quiz scores. Better indicator of program content quality.

Level 3 — Behavior: Did participants change their behavior on the job? This is the level that matters most and is hardest to measure. Phishing simulation click rates, policy violation rates, security incident reporting rates, and password strength metrics are Level 3 indicators.

[PAUSE]

Level 4 — Results: Did the behavior change produce the desired business outcome? Reduction in security incidents attributable to human error, reduction in credential-based breaches, reduction in successful phishing attacks. Level 4 data is compelling for board reporting but requires a longer measurement window and careful attribution.

[SHOW SLIDE: Key Metrics by Program Component]

Let me give you specific metrics for the major program components.

For phishing simulation: track click rate (percent of employees who click the simulated phishing link), credential submission rate (percent who entered credentials), reporting rate (percent who reported the simulated phishing email through the proper channel), and trend over time.

For security training completion: track completion rate by department and role, assessment pass rate, repeat failure rate (employees who require remedial training), and exemption usage.

[PAUSE]

For incident reporting: track volume of reports (increasing reports often indicate a healthier security culture, not more incidents), report quality, and time from incident occurrence to report.

For overall program: track year-over-year phishing simulation click rates, policy exception requests, and security incident categories attributable to human behavior.

---

## Section 4: Culture Change — The Long Game (16:30–21:30)

[SHOW SLIDE: Why Culture Is the Hardest Part]

Everything we've covered so far — design, delivery, measurement — is the manageable part of security awareness. Culture change is where the real challenge lives. And without culture change, awareness programs produce compliance, not commitment. Employees complete the training because they have to, not because they've internalized why it matters.

[PAUSE]

Security culture is the collection of shared beliefs, values, and behaviors regarding security within an organization. In a strong security culture, employees think about security without being prompted, report suspicious activity because they feel responsible for protecting the organization, and push back on processes that compromise security rather than silently accepting them.

Building that kind of culture takes years and requires commitment from leadership that goes far beyond a CEO message in the annual training video.

[SHOW SLIDE: Leadership Behaviors That Drive Security Culture]

Let me be direct about what actually drives security culture. Employees watch what leaders do, not what they say.

If executives regularly bypass security controls — tailgating through badge readers, refusing MFA because it's inconvenient, pressuring IT to grant exceptions for VIPs — employees conclude that security is for other people. If security is treated as an obstacle to business rather than an enabler, that message propagates through the organization.

[PAUSE]

Conversely, when executives participate in phishing simulations without special treatment, visibly follow security policies, discuss security incidents without blame culture, and resource the security program adequately, employees receive a consistent message that security matters.

[SHOW SLIDE: The Role-Based Training Imperative]

One of the most effective culture-building tools is role-based training that connects security to the specific work employees do every day. Generic training says "don't click phishing links." Role-based training for a finance team says "wire transfer fraud specifically targets accounts payable — here's how to verify a payment request change, here's a real example of a business email compromise that cost a company $1.7 million."

[PAUSE]

That specificity makes security real and relevant. It shows employees that the training was designed for them, not recycled from a generic template. It builds credibility for the security program and increases engagement.

[SHOW SLIDE: Role-Based Training Categories]

Let me identify the key role-based training categories you need to plan for in a mature program.

All employees: phishing recognition, password hygiene, clean desk and screen lock, social engineering resistance, incident reporting.

IT staff: privileged access management, patch management procedures, configuration baseline requirements, secure remote administration.

Developers: OWASP Top 10, secure design principles, input validation, secrets management, secure SDLC practices.

Finance and HR: business email compromise, wire fraud procedures, payroll fraud awareness, PII handling requirements.

Executives: board-level risk briefings, cyber insurance considerations, business impact of security decisions, regulatory accountability.

---

## Section 5: Program Management and CISM Alignment (21:30–23:30)

[SHOW SLIDE: The Security Awareness Program Manager Role]

A security awareness program is a program, not a project. It requires ongoing management: content refresh cycles, simulation campaign calendars, metric reviews, stakeholder reporting, and budget management.

[PAUSE]

The program manager must coordinate across HR, Legal, Communications, IT, and business units. This is not a pure technical role — it requires strong communication skills, organizational awareness, and the ability to translate security requirements into language that resonates with non-technical stakeholders.

[SHOW SLIDE: CISM Domain 3 Connection]

For your CISM exam, Module 08 content maps directly to Domain 3. Key exam areas include the distinction between awareness, training, and education; the ADDIE model applied to security training design; the Kirkpatrick model for measuring training effectiveness; the characteristics of effective phishing simulation programs; and the organizational factors that drive security culture.

[PAUSE]

Remember that on the CISM exam, the emphasis is always on the management perspective. Questions are not asking you to design a CBT module — they're asking you how to manage a program that produces measurable risk reduction.

[SHOW SLIDE: Module 08 Summary]

Let's recap Module 08.

We covered the distinction between awareness, training, and education and why segmenting your audience is essential for effective program design. We explored the spectrum of delivery methods — instructor-led training, CBT, phishing simulation, microlearning, and environmental reinforcement — and the trade-offs of each.

We walked through the Kirkpatrick four-level measurement model and identified specific metrics for phishing simulation, training completion, and incident reporting. And we examined the organizational dynamics of security culture change, including the critical role of leadership behavior and the value of role-based training.

[PAUSE]

Your lab this week asks you to design a role-based training curriculum for a fictional organization, including learning objectives, delivery methods, and measurement plan. Your quiz covers awareness versus training distinctions, measurement models, and program design principles. The discussion explores real-world culture change scenarios.

This wraps up Module 08. In Module 09 we move into security incident management — what happens when, despite all these controls and training, something goes wrong.

[SHOW SLIDE: End Card]

---

*End of Video Script — Module 08*

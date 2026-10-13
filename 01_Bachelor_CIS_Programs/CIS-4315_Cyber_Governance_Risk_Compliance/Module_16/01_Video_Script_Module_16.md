# Video Script: Module 16 — CISM Exam Preparation and Capstone Review

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 22–24 minutes

## CISM Domain Alignment: All Four Domains — Domain 1 (Information Security Governance), Domain 2 (Information Risk Management), Domain 3 (Information Security Program Development and Management), Domain 4 (Incident Management)

---

### [SLIDE 1] Welcome to the Final Module

Welcome back, everyone. I am Professor Nash, and this is Module 16 — the final module of CIS-4315 Cyber Governance, Risk, and Compliance.

You have covered a tremendous amount of ground over the past fifteen modules. From the foundations of information security governance in Module 1, through risk management, security program development, incident response, and the regulatory landscape we just finished in Module 15 — you have built the conceptual and practical framework of a working information security manager.

This final module has three purposes. First, we will review all four CISM domains in an integrated way, connecting themes across the course. Second, I will share exam strategy — how to approach CISM exam questions, how to manage the adaptive testing format, and how to avoid the most common reasoning mistakes. Third, we will work through ten sample exam questions together so you can see CISM-style reasoning in action.

Let us get started.

---

### [SLIDE 2] The CISM Certification in Context

Before reviewing the domains, let me place the CISM in context.

The Certified Information Security Manager is an ISACA credential designed for information security management professionals. It is distinct from technical certifications like CISSP, CEH, or Security+. The CISM does not test whether you can configure a firewall or write exploit code. It tests whether you can govern, manage, and align an information security program to business objectives.

ISACA reports that the CISM is consistently ranked among the highest-compensated cybersecurity certifications globally. As of the most recent surveys, CISM holders earn a median salary premium of 20 to 25 percent over non-certified peers in comparable roles.

The exam itself consists of 150 questions delivered in a four-hour window. The format is scenario-based multiple choice — every question describes a situation and asks what a security manager should do, prioritize, or recommend. The exam is adaptive, meaning question difficulty adjusts based on your performance, and the passing score is reported on a scaled score of 450 out of 800.

Work experience requirements for certification — distinct from passing the exam — include five years of information security work experience with a minimum of three years in security management within the ten years prior to applying.

---

### [SLIDE 3] How to Think Like a CISM Exam Writer

Before domain review, the most important thing I can teach you about this exam is how its questions are written — because understanding the test-writer's intent is half the battle.

CISM exam questions are written from a governance and risk management perspective. The correct answer is almost always the one that:

Reflects management judgment rather than a technical decision.

Addresses the root cause rather than the symptom.

Prioritizes risk-based action over compliance-first action.

Considers the business context rather than applying a universal rule.

The most dangerous distractor answers on the CISM exam are technically correct statements that are contextually wrong. For example, "immediately implement compensating controls" might be technically appropriate in some contexts, but if the scenario describes a situation where a formal risk assessment has not yet been completed, the governance-aligned answer is "conduct a risk assessment first." The exam rewards the manager who knows what to do before doing it.

One more principle: when the exam asks what to do "first" or "most importantly," the correct answer is almost always a governance step — define scope, identify stakeholders, assess risk, align with business objectives — not a technical implementation step.

---

### [SLIDE 4] Domain 1 Review — Information Security Governance

Domain 1 represents approximately 17 percent of the CISM exam. It covers the governance structures, strategy alignment, and oversight mechanisms that direct the information security program.

The central concept in Domain 1 is that information security governance is a board and executive-level function. The CISO is responsible for managing the security program, but governance is the accountability structure above that — the board committees, executive charters, and oversight mechanisms that ensure security aligns with and supports business objectives.

Key Domain 1 concepts to recall:

Information security strategy must be derived from business strategy, not developed independently. Security goals must support business goals.

The security charter or mandate establishes the authority, scope, and reporting relationships of the security function. Without a charter, the CISO has no formal authority.

Policies are the highest level of governance documentation. Standards, procedures, and guidelines flow from policy. The board or senior executive approves policy; the CISO manages its operationalization.

Board-level communication must use business and risk language, not technical operations language. Key risk indicators, security investment return, and program maturity metrics are appropriate board-level content. Firewall rulesets are not.

Security governance metrics include KRIs (Key Risk Indicators), KPIs (Key Performance Indicators), and security scorecards. Mature programs report on residual risk trends, not just activity metrics.

The security governance model must address who is accountable, who is responsible, who must be consulted, and who must be informed — the RACI framework applied to security decisions.

---

### [SLIDE 5] Domain 2 Review — Information Risk Management

Domain 2 represents approximately 20 percent of the CISM exam. It covers the identification, analysis, evaluation, and treatment of information security risks.

The foundational concept in Domain 2 is that risk management is a continuous process, not a point-in-time event. Risks change as threats evolve, as the organization changes, and as controls are implemented or removed.

Key Domain 2 concepts to recall:

Risk is defined as the combination of the likelihood of a threat exploiting a vulnerability and the resulting business impact. Both dimensions must be assessed.

Risk appetite is the board-approved level of risk the organization is willing to accept in pursuit of its objectives. Risk tolerance is the acceptable deviation from that appetite. The security manager ensures that operational risk decisions stay within board-approved appetite.

The four risk treatment options are: risk avoidance (don't do the activity that creates the risk), risk mitigation (implement controls to reduce likelihood or impact), risk transfer (shift the financial consequence through insurance or contracts), and risk acceptance (formally acknowledge and accept the residual risk).

Risk acceptance requires formal documentation with management sign-off. Undocumented "deprioritization" of a known risk is not risk acceptance — it is negligence.

Asset classification drives risk prioritization. Not all data and systems carry equal risk. Crown jewel assets — those whose compromise would cause the most business harm — receive priority protection.

Third-party risk is a Domain 2 concept. Vendors and cloud providers who handle your data or connect to your systems extend your risk surface. Due diligence, contractual requirements, and ongoing monitoring are all risk management activities.

---

### [SLIDE 6] Domain 3 Review — Information Security Program Development and Management

Domain 3 represents approximately 33 percent of the CISM exam — the largest single domain. It covers how the security program is built, resourced, operated, and measured.

Key Domain 3 concepts to recall:

The security program translates governance direction and risk management decisions into deployed controls, documented processes, and measured outcomes. This is the "build and run" domain.

Security architecture aligns technical controls to the organization's risk profile and business architecture. It is not ad hoc tool deployment — it is a planned, documented structure.

Security awareness and training programs are governance requirements, not optional enhancements. Employees are the most frequently exploited vulnerability vector and the first line of defense.

Security metrics and reporting translate program performance into business-relevant information. Activity metrics (how many patches were applied) have limited governance value. Outcome metrics (what is our mean time to patch critical vulnerabilities?) have high governance value.

Resource management — people, technology, and budget — is an explicit Domain 3 topic. The security manager must be able to justify investments in risk terms and compete for resources using business cases, not technical arguments.

Controls integration involves ensuring security controls are embedded in business processes rather than bolted on. The earlier in a project lifecycle security is considered, the less it costs and the more effective it is.

Vendor management and third-party security are also Domain 3 topics. Contracts, SLAs, vendor assessments, and right-to-audit clauses are program management tools.

---

### [SLIDE 7] Domain 4 Review — Incident Management

Domain 4 represents approximately 30 percent of the CISM exam. It covers the preparation for, detection of, response to, and recovery from security incidents.

Key Domain 4 concepts to recall:

The incident response lifecycle has seven phases: Preparation, Detection and Analysis, Containment, Eradication, Recovery, Post-Incident Review, and in some models an explicit Lessons Learned phase. Know what actions occur in each phase.

Preparation is the most important phase because it determines how effective all other phases will be. A well-funded, well-practiced Preparation phase means every other phase runs more smoothly.

The incident response plan must be tested regularly through tabletop exercises, functional exercises, and full simulations. An untested plan is not a plan — it is a document.

Escalation criteria must be pre-defined. During an active incident is not the time to decide who needs to be notified. Pre-defined criteria based on severity, data type, and regulatory impact enable fast, consistent escalation decisions.

Regulatory notification obligations are incident management governance concerns, not purely compliance department concerns. The security manager must know the applicable deadlines — GDPR 72 hours, HIPAA 60 days, SEC four business days — and ensure they are incorporated into escalation procedures.

Post-incident review is mandatory for significant incidents. Its purpose is organizational learning, not blame assignment. Findings from post-incident reviews must translate into specific, time-bound improvements with assigned owners.

Forensic evidence handling must preserve chain of custody. Evidence collected improperly may be inadmissible in legal proceedings and may compromise the organization's legal position.

---

### [SLIDE 8] Integrative Themes Across All Four Domains

The CISM exam does not test each domain in isolation. Many questions require you to integrate concepts from multiple domains. Here are the most important cross-domain themes:

Risk is the connective tissue. Domain 1 sets the risk appetite. Domain 2 identifies and treats risks within that appetite. Domain 3 implements controls to reduce those risks. Domain 4 responds when those risks materialize despite controls. Every domain decision is risk-based.

Business alignment runs through every domain. Security exists to support business objectives, not to prevent them. Governance, risk management, program management, and incident response must all be understood through the lens of what the business needs.

Accountability must be explicit. Policies (Domain 1), risk acceptance decisions (Domain 2), control ownership (Domain 3), and escalation authority (Domain 4) all require named owners with formal authority. Security programs without clear accountability structures fail.

Continuous improvement is an expectation, not an aspiration. Risk assessments are repeated. Controls are tested and updated. Incident lessons are implemented. Programs are benchmarked and matured over time.

---

### [SLIDE 9] Exam Strategy — Eliminating Distractors

Let us talk about how to handle the specific types of wrong answers the CISM exam uses.

The first type of distractor is the technically correct but contextually wrong answer. Example: a question asks what a new CISO should do first upon joining an organization with an immature security program. One answer says "implement a SIEM platform." That may eventually be the right tool, but "first" in a governance context means understanding the business, assessing current state, and getting executive alignment — not buying software.

The second type is the right action at the wrong time. Example: a question about a breach in progress offers "conduct a post-incident review" as an option. Post-incident review is correct — but not during the incident. This tests whether you know the incident lifecycle sequence.

The third type is the overly extreme action. Example: a question about a vendor who fails a security assessment offers "immediately terminate the vendor contract." Termination may be warranted eventually, but the governance-aligned first step is to notify the vendor of findings, request a remediation plan, and assess the residual risk during the remediation period.

The fourth type is the option that ignores risk management process. Example: a question offers "implement compensating controls immediately" without assessing whether the control gap represents an acceptable risk. Governance requires assessment before action.

When you are unsure, ask: which answer reflects the management perspective, considers the business context, follows the correct process sequence, and addresses root cause rather than symptom?

---

### [SLIDE 10] Sample Exam Question 1

Here is our first sample question.

A newly appointed CISO discovers that the organization has no formal information security policy and no documented security strategy. Which action should the CISO take first?

Option A: Conduct a comprehensive vulnerability assessment of all systems.

Option B: Develop a draft information security policy for board approval.

Option C: Brief the board on the current security posture and obtain formal authorization for the security program.

Option D: Hire additional security staff to address the identified gaps.

The correct answer is C. Before drafting policies or implementing controls, the CISO needs formal executive and board authorization. A CISO without a mandate lacks the authority to require policy compliance, allocate resources, or hold business units accountable. Governance authority precedes policy development. Option B is tempting but premature without board buy-in. Options A and D are program activities that presuppose a governing mandate.

---

### [SLIDE 11] Sample Exam Questions 2 through 5

Question 2: An organization's risk assessment identifies a critical vulnerability in a legacy payment system. Remediation would require a 6-month system replacement project. The business unit owner wants to continue operations using the vulnerable system. What is the most appropriate action for the security manager?

Correct answer: Document the risk, propose compensating controls to reduce exposure during the interim period, and require formal risk acceptance sign-off from an executive with appropriate authority. Risk acceptance is valid when formally documented; informal continuation without sign-off is not.

Question 3: After a significant data breach, the post-incident review finds that the root cause was an unpatched vulnerability identified in a risk assessment 90 days earlier and listed as "low priority." What governance failure does this most directly represent?

Correct answer: The failure to manage identified risks through formal treatment or documented risk acceptance. The organization had knowledge of the risk and neither treated it nor formally accepted it — this is the governance definition of negligence.

Question 4: A business unit requests that the security team waive a policy requirement for encryption of customer data stored in a new application, citing cost and schedule pressure. What should the security manager do?

Correct answer: Evaluate the risk of the exception, propose compensating controls if feasible, escalate to executive authority for formal exception approval, and document the decision with a defined expiration date and review cycle.

Question 5: The board asks the CISO to present the organization's security metrics at the next quarterly meeting. Which set of metrics is most appropriate for a board audience?

Correct answer: Key risk indicators showing trend in residual risk, security investment aligned to risk priorities, and metrics measuring the effectiveness of critical controls — not operational activity counts or technical incident details.

---

### [SLIDE 12] Sample Exam Questions 6 through 10

Question 6: An organization acquires a smaller company and must integrate its IT systems. The acquired company has no formal security program. What should the acquiring organization do first?

Correct answer: Conduct a risk assessment of the acquired company's systems before integration, to understand what risks would be imported into the parent organization's environment.

Question 7: A security manager is asked to reduce the security budget by 20% due to economic pressures. Which approach best reflects CISM principles?

Correct answer: Perform a risk-based analysis identifying which investments provide the greatest risk reduction, present the business impact of each potential reduction to leadership, and provide a risk-informed recommendation that enables the board to make an explicit trade-off decision.

Question 8: An employee reports that a supervisor directed them to share credentials for a financial system with a contractor who had not completed background screening. What is the security manager's first priority?

Correct answer: Assess the access that occurred, contain any ongoing unauthorized access, and escalate to HR, legal, and executive management — because this represents both a security control failure and a potential HR and legal compliance matter.

Question 9: An organization's incident response plan has not been updated or tested in three years. A new cloud infrastructure was deployed 18 months ago. What is the most significant risk this situation creates?

Correct answer: The incident response plan may not address the organization's current environment, meaning that when an incident occurs in the cloud infrastructure, responders will not have the procedures, contacts, or decision authorities they need. The plan must be updated and tested to reflect the current state.

Question 10: A vendor notifies the organization that a subcontractor working on its behalf experienced a data breach involving the organization's customer records. What should the organization do first?

Correct answer: Assess the scope and nature of the breach to determine whether it triggers the organization's own regulatory notification obligations — because the organization, as the data controller or covered entity, bears direct regulatory responsibility regardless of where in the supply chain the breach occurred.

---

### [SLIDE 13] Career Pathways in Governance, Risk, and Compliance

As we approach the end of this course, let me speak briefly about where this knowledge takes you professionally.

The governance, risk, and compliance space within information security is one of the fastest-growing and highest-compensated specializations in the field. Organizations of every size and in every sector need professionals who can bridge the gap between technical security operations and business leadership.

Entry-level GRC roles include titles like Information Security Analyst (compliance focus), GRC Analyst, Risk Analyst, and Compliance Coordinator. These roles typically involve control testing, evidence management, vendor assessments, and policy maintenance.

Mid-career roles include Security Manager, Risk Manager, Compliance Manager, and Privacy Manager. These roles carry program ownership, audit management responsibility, and executive reporting relationships.

Senior roles include CISO, Chief Risk Officer, Chief Privacy Officer, VP of Compliance, and Director of Information Security. These roles sit in executive leadership and carry board-level accountability.

Certifications that complement the CISM and strengthen a GRC career profile include CRISC (Certified in Risk and Information Systems Control) for risk-focused roles, CDPSE (Certified Data Privacy Solutions Engineer) for privacy-oriented roles, CGEIT (Certified in the Governance of Enterprise IT) for governance-focused roles, and CISA (Certified Information Systems Auditor) for audit-oriented roles.

---

### [SLIDE 14] Continuing Education and Professional Community

The CISM certification requires 20 Continuing Professional Education hours per year and 120 hours over a three-year renewal period. This is not a burden — it is a structure that keeps your knowledge current in a field that changes rapidly.

Ways to earn CPE credits include attending ISACA chapter meetings and conferences, completing online courses and webinars, writing articles or speaking at industry events, and participating in professional volunteer activities.

I strongly encourage you to join your local ISACA chapter. Texas has active chapters in Dallas, Fort Worth, Houston, San Antonio, and Austin. Chapter membership provides networking, mentorship, job board access, and educational programming that complements what you have learned in this course.

The broader professional community — including organizations like IAPP for privacy professionals, ISC2, and ISSA — provides additional resources and networking opportunities as your career develops.

---

### [SLIDE 15] Course Closing and Final Reflections

We have reached the end of CIS-4315.

Over sixteen modules, you have covered the full scope of the CISM body of knowledge: governance structures, risk management frameworks, security program architecture, incident response governance, regulatory compliance, and the integrative judgment that ties it all together.

The most important thing I hope you take from this course is not any specific framework acronym or regulatory deadline — though those matter. The most important thing is the habit of asking the right questions.

When your organization faces a security decision, ask: what is the risk? Who has authority to accept or treat it? Does our current program address it? If an incident occurs, are we prepared?

When a compliance obligation arises, ask: does this standard represent the floor or should we exceed it? What controls satisfy this requirement and what other obligations do those same controls address? How does this fit into our unified compliance program?

When you report to leadership, ask: am I translating security into business risk language? Am I giving them information they can act on? Am I being honest about residual risk, not just about what is going well?

Those questions — asked consistently, documented carefully, and answered honestly — are what information security governance looks like in practice.

Thank you for your commitment to this course and to this profession. I look forward to hearing about your CISM success and your careers in the years ahead.

Good luck on the exam, and go do great things.

---

*End of Script — Module 16*

*Word count: approximately 2,700 words | Estimated delivery: 22–24 minutes at 110–125 words per minute*

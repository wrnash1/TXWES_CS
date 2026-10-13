# Video Script: Module 13 — Business Continuity Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Additional Coverage — Business Continuity and Disaster Recovery

---

### [00:00 – 01:30] Opening and Learning Objectives

**Visual:** Instructor on camera with title card: "Module 13 — Business Continuity Planning."

**Audio:**

"Welcome back to CIS-4315. I'm Professor Nash, and today we are tackling Module 13 — Business Continuity Planning, or BCP. This is one of the most operationally critical topics you will encounter on the CISM exam and in your career as a security professional.

Here is what you will be able to do by the end of this session. First, you will explain the purpose and scope of a Business Impact Analysis. Second, you will define and distinguish RPO, RTO, and MTPD. Third, you will identify and compare continuity strategies. Fourth, you will describe the structure of a complete BCP document. And fifth, you will differentiate among tabletop, simulation, and full-interruption tests.

Let's get into it."

---

### [01:30 – 04:00] What Is Business Continuity Planning?

**Visual:** Slide showing the BCP lifecycle: Initiation → BIA → Strategy → Plan Development → Testing → Maintenance.

**Audio:**

"Business Continuity Planning is the discipline of ensuring that critical business functions can continue — or recover rapidly — during and after a disruptive event. Notice I said *business* functions, not just IT systems. That distinction matters on the CISM exam.

BCP is broader than disaster recovery. DR is a subset of BCP focused on restoring technology infrastructure. BCP addresses the whole organization — people, processes, facilities, supply chains, communications, and technology together.

The drivers for BCP are both internal and external. Internally, executives want assurance that revenue-generating operations will survive a disruption. Externally, regulators, auditors, and customers increasingly require documented continuity plans. In financial services, for example, the FFIEC mandates BCP. In healthcare, HIPAA requires covered entities to have contingency plans. In critical infrastructure, NIST SP 800-34 provides the federal baseline.

The BCP lifecycle has six phases. We initiate the program, conduct a Business Impact Analysis, select strategies, write the plan, test it, and maintain it over time. Today we cover all six."

---

### [04:00 – 08:00] Business Impact Analysis Methodology

**Visual:** Slide — BIA Process Flow with five labeled steps. Diagram shows arrows from "Identify Critical Processes" through "Assign Recovery Priorities."

**Alt-text:** A five-step flowchart reading: (1) Identify Critical Business Processes → (2) Identify Dependencies → (3) Quantify Impact Over Time → (4) Define Recovery Time Objectives → (5) Assign Recovery Priorities.

**Audio:**

"The Business Impact Analysis is the foundation of your entire BCP program. Without a solid BIA, your recovery time objectives are guesses, your strategies are misaligned, and your plan will fail when you need it most.

Step one is identifying critical business processes. You do this through interviews with department heads, process documentation reviews, and sometimes through surveys. You are asking: What do we do, and which of those activities are essential to organizational survival?

Step two is identifying dependencies. Every process depends on something — an application, a database, a vendor, a physical location, or a specific person. You map those dependencies explicitly. If Accounts Receivable depends on the ERP system, and the ERP system depends on a single database server in one data center, that is a critical dependency chain.

Step three is quantifying impact over time. This is where BIA separates good programs from great ones. You construct an impact timeline — what happens at one hour of downtime, at four hours, at twenty-four hours, at seventy-two hours? Impact categories include financial loss, regulatory penalties, reputational damage, contractual breaches, and safety risks. Assigning dollar values and severity ratings to each category forces stakeholders to confront real consequences.

Step four is defining recovery objectives based on what that impact timeline reveals. The point at which the organization can no longer tolerate the outage sets your Maximum Tolerable Period of Disruption, and that drives your RTO.

Step five is assigning recovery priorities. Tier 1 processes recover first. Tier 2 can wait longer. Tier 3 can operate manually or defer entirely. This prioritization drives everything downstream — budget, strategy selection, testing schedules."

---

### [08:00 – 11:00] RPO, RTO, and MTPD Defined

**Visual:** Diagram showing a timeline with a disruption event, labeled arrows for RPO (backwards to last backup), RTO (forwards to recovery), and MTPD (total tolerable gap).

**Alt-text:** A horizontal timeline. A red lightning bolt marks the disruption point. An arrow pointing left is labeled RPO — Recovery Point Objective. An arrow pointing right from the disruption to a "Service Restored" marker is labeled RTO — Recovery Time Objective. A longer bracket spanning from disruption to the maximum acceptable outage end is labeled MTPD — Maximum Tolerable Period of Disruption.

**Audio:**

"Three metrics dominate BCP conversations, and you must be able to define each precisely for the CISM exam.

RPO — Recovery Point Objective — is the maximum age of data that the organization can afford to lose. If your RPO is four hours, you can lose up to four hours of transactions before the business suffers unacceptable harm. RPO directly dictates your backup frequency. If you back up daily but your RPO is one hour, you have a gap that must be closed.

RTO — Recovery Time Objective — is the maximum time allowed to restore a function to an acceptable service level following a disruption. If your RTO for order processing is two hours, your recovery architecture must be capable of bringing order processing back within two hours. RTO drives infrastructure decisions — hot standby, warm standby, or cold standby.

MTPD — Maximum Tolerable Period of Disruption — is the absolute maximum time an organization can survive without a critical function before consequences become irreversible. MTPD is always greater than or equal to RTO. If RTO is two hours but MTPD is eight hours, you have a six-hour window between planned recovery and catastrophic failure. That buffer is your safety margin.

Here is an important relationship: RPO and RTO are targets set by the business. Achieved RPO and RTO are measured in testing. If your tested recovery time exceeds your RTO, you have a gap that requires a strategy change. And MTPD is the hard ceiling — exceeding it means the organization may not survive.

On the exam, watch for questions that confuse RPO with RTO. Remember: RPO looks backward in time to data; RTO looks forward in time to recovery."

---

### [11:00 – 14:30] Continuity Strategies

**Visual:** Comparison table with five strategy types across columns: Strategy, Cost, Recovery Speed, Best For.

**Audio:**

"Once you have your BIA outputs and your RTOs, you select continuity strategies. There are five primary categories.

The first is **redundant systems and high availability**. This means active-active configurations, load balancing, and real-time replication. Recovery is near-instantaneous because the alternate system is already running. Cost is high. This is appropriate for Tier 1 processes with RTOs measured in minutes.

The second is **alternate site operations**. The organization pre-identifies a secondary work location — either owned or contracted. Staff can relocate and resume operations there. This is combined with data recovery to restore the full function.

The third is **manual workarounds**. Some processes can temporarily operate without technology — paper forms, manual calculations, phone trees. Manual workarounds are inexpensive but capacity-limited and error-prone. They are a bridge, not a destination.

The fourth is **mutual aid agreements**. Two organizations in the same industry agree to support each other during a disruption. This is common in smaller municipalities and cooperative networks. The challenge is that a regional disaster may affect both parties simultaneously, making the agreement worthless.

The fifth is **outsourcing and cloud elasticity**. Organizations use cloud platforms to spin up additional capacity or relocate processing on demand. AWS, Azure, and GCP all offer DR-as-a-service capabilities. Cloud strategies reduce capital investment but require careful contract review — your cloud provider's RTO commitments must align with your recovery objectives.

Strategy selection is never purely technical. It is a business decision weighted by cost, risk tolerance, regulatory requirements, and criticality tier. The information security manager's role is to present options with cost-benefit analysis and let the business make an informed choice."

---

### [14:30 – 17:00] BCP Plan Structure

**Visual:** Document outline on screen showing eight numbered sections.

**Audio:**

"A Business Continuity Plan is a formal document. It must be complete enough for someone unfamiliar with the process to execute it under stress. Here is the standard structure you should know.

Section one is the purpose, scope, and objectives. Who does this plan cover? What events trigger activation?

Section two is roles and responsibilities. This section names the Business Continuity Manager, the Crisis Management Team, departmental recovery leads, and alternates for each role. Every named role must have a backup.

Section three is the activation criteria and procedures. What thresholds trigger plan activation? Who has authority to declare an incident?

Section four is communication procedures. How do you notify employees, customers, regulators, and the media? This includes out-of-band communication methods because your primary systems may be unavailable.

Section five is recovery procedures by business unit. Each critical function has a step-by-step recovery runbook. These are the procedures your teams will execute under pressure.

Section six is resource requirements. What facilities, equipment, personnel, and vendor support are needed?

Section seven is the test and exercise schedule. Plans that are never tested are plans that will fail.

Section eight is the plan maintenance and review cycle. BCP must be a living document, not a shelf document."

---

### [17:00 – 20:00] BCP Testing Types

**Visual:** Three-column comparison table — Tabletop, Simulation, Full Interruption — with rows for Description, Disruption Level, Cost, and Frequency.

**Audio:**

"Testing is what separates a functional BCP from a false sense of security. ISACA recognizes three primary testing types, and you need to know when each is appropriate.

**Tabletop exercises** are discussion-based sessions where key personnel walk through a scenario step-by-step without activating systems or relocating staff. A facilitator presents injects — unexpected complications — and the team discusses their responses. Tabletops are low cost, low disruption, and excellent for identifying plan gaps and building team familiarity. Frequency: quarterly or semi-annually.

**Simulation exercises** — also called functional exercises — go one step further. Teams actually perform their recovery actions, but in a controlled environment. Systems may be partially activated. Staff may travel to the alternate site. Communication trees are executed. Simulations verify that procedures work in practice, not just in theory. They are more resource-intensive than tabletops. Frequency: annually.

**Full-interruption tests** — sometimes called full-scale or live cutover tests — shut down primary systems and force a complete failover to backup systems or alternate sites. This is the highest-fidelity test, but it carries real risk of extended downtime if the recovery fails. Organizations with mature programs and executive support perform full-interruption tests for their most critical functions. Frequency: annually or biannually for critical systems.

On the CISM exam, the question may ask which test type is most appropriate given a scenario. Key logic: if the scenario prioritizes low risk and team education, choose tabletop. If it prioritizes validating procedures without full cutover, choose simulation. If it prioritizes proving the actual recovery capability at full scale, choose full interruption."

---

### [20:00 – 22:30] BCP Maintenance

**Visual:** Slide showing BCP maintenance triggers: organizational changes, test results, technology changes, regulatory updates, post-incident reviews.

**Audio:**

"A BCP that is written once and never updated is a liability, not an asset. Maintenance must be systematic and triggered.

Scheduled reviews should occur at minimum annually, and more frequently for organizations in rapidly changing environments. The review asks: Has anything changed that affects our recovery assumptions?

Triggered reviews occur after specific events. A merger or acquisition changes which systems and people are in scope. A significant technology refresh changes your recovery architecture. A regulatory update may change your compliance obligations. And critically — every test, exercise, and actual incident should result in a lessons-learned review that updates the plan.

Ownership is essential. Each section of the BCP should have a named owner who is accountable for keeping it current. The Business Continuity Manager coordinates across owners but cannot maintain the plan alone.

Version control is non-negotiable. Every plan update must be versioned, dated, and archived. During an actual incident, you need confidence that the procedure you are executing is the current approved version.

Finally, distribution and accessibility. The plan must be accessible when your primary systems are down. Printed copies in off-site locations, encrypted copies on portable media, and cloud-hosted copies all serve this purpose."

---

### [22:30 – 24:00] Summary and Exam Tips

**Visual:** Bullet summary slide with six key takeaways.

**Audio:**

"Let's close with the key takeaways for Module 13.

First, BCP is broader than DR — it covers people, processes, and technology together.

Second, the BIA is the foundation — without it, all RTOs and strategies are guesses.

Third, RPO is about data loss tolerance; RTO is about recovery time tolerance; MTPD is the hard ceiling the organization cannot exceed.

Fourth, strategy selection is a business decision — present options with cost-benefit data.

Fifth, the plan structure must include roles, activation criteria, communication, runbooks, and a maintenance cycle.

Sixth, test regularly — tabletop for education, simulation for procedure validation, full interruption for proof of capability.

For the CISM exam, focus on the relationship between BIA outputs and strategy selection, and on distinguishing the three testing types. Those two areas appear frequently.

In Module 14, we move to Disaster Recovery Management — DR site types, failover procedures, cloud DR architectures, and backup strategies. I will see you there."

---

### Production Notes

- **Slides:** Minimum 18-point font. All diagrams need alt-text as scripted.

- **On-screen timers:** Display elapsed time in lower-left corner.

- **Caption file:** SRT format required for LMS upload.

- **B-roll suggestions:** Data center footage, network diagram overlays, tabletop exercise imagery.

- **Exam callout graphic:** Use a distinct gold banner for all CISM exam tips.

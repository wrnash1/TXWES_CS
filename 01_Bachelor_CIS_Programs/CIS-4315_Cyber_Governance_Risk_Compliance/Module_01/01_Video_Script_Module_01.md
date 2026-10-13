# Video Script: Module 01 — Information Security Governance Foundations

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 1 — Information Security Governance

---

### Pre-Roll Slate (0:00–0:15)

[SHOW SLIDE: Texas Wesleyan University logo, course title CIS-4315, Module 01 title card]

---

### Segment 1: Welcome and Module Roadmap (0:15–2:30)

[SHOW SLIDE: Module 01 — Information Security Governance Foundations | Learning Objectives]

Hello, and welcome to CIS-4315 — Cyber Governance, Risk, and Compliance. I am Professor Nash, and this is Module 01: Information Security Governance Foundations.

Before we get into the content, let me tell you exactly what we are building toward in this course. By the end of sixteen modules, you will have the knowledge base needed to sit for the ISACA Certified Information Security Manager exam — the CISM. That certification is one of the most respected credentials in the field of information security management, and everything we cover in this course maps directly to one of its four domains.

Module 01 sits squarely in CISM Domain 1: Information Security Governance. That domain accounts for approximately 17 percent of the CISM exam — it is the largest single domain, and it is foundational to everything else. You cannot manage risk, respond to incidents, or build a security program without first understanding governance.

Here is what we will cover in this module:

- The definition and purpose of information security governance
- How governance relates to and differs from security management
- The key frameworks that structure governance programs
- The roles and responsibilities involved in enterprise security governance
- The CIA triad and why it anchors every governance decision
- How security governance aligns with broader organizational strategy

Let us get started.

---

### Segment 2: Defining Information Security Governance (2:30–6:30)

[SHOW SLIDE: What Is Information Security Governance?]

The word "governance" gets used a lot in cybersecurity, so let us be precise about what it means in the ISACA context.

Information security governance is the system of policies, accountability structures, and decision-making processes through which an organization directs and controls its information security program. That is the formal definition, but let me break it down into plain language.

Governance answers three questions: Who is responsible? What direction are we heading? How do we know we are getting there?

[SHOW SLIDE: Governance vs. Management — Side-by-Side Comparison]

This distinction between governance and management is one of the most tested concepts on the CISM exam, so pay close attention.

Governance operates at the strategic level. It is performed by the board of directors, executive committees, and senior leadership. Governance sets direction, establishes accountability, and ensures that the security program aligns with the organization's mission and risk tolerance. The board does not manage firewalls — the board decides how much risk the organization is willing to accept and holds leadership accountable for operating within that boundary.

Management operates at the program and operational level. Management is where the CISO and the security team live. It is the day-to-day execution of the strategy that governance has set. Management writes policies, allocates resources, oversees controls, and reports results back up to the governance layer.

Think of it this way: governance is setting the destination and the rules of the road. Management is actually driving the car.

[SHOW SLIDE: CISM Exam Tip 1]

CISM Exam Tip: When you see a question about what the board of directors or steering committee should do, think governance. When you see a question about what the CISO or security program should do, think management. The exam tests this distinction constantly in scenario-based questions.

---

### Segment 3: The CIA Triad — The Core of All Governance Decisions (6:30–10:00)

[SHOW SLIDE: The CIA Triad — Confidentiality, Integrity, Availability]

Every governance decision in information security ultimately traces back to three fundamental security properties: Confidentiality, Integrity, and Availability. Together, these form the CIA triad, and they are the measuring stick against which every security control, policy, and program element is evaluated.

Confidentiality means ensuring that information is accessible only to those who are authorized to see it. Unauthorized disclosure — whether through a data breach, an insider threat, or simple misconfiguration — is a confidentiality failure. Think of the medical records of a patient, the trade secrets of a corporation, or the personal financial data of a customer.

Integrity means ensuring that information is accurate and has not been improperly altered. An integrity failure does not necessarily mean someone read something they should not have — it means something was changed without authorization. A payroll system where salaries have been manipulated, or a configuration file where a setting was silently modified, are integrity problems.

Availability means ensuring that authorized users can access the systems and data they need when they need them. A denial-of-service attack, a ransomware encryption, or even a poorly planned maintenance window can create availability failures. Availability is often underweighted in governance discussions, but for operational systems — hospitals, utilities, financial trading platforms — it can be the most critical property of all.

[SHOW SLIDE: CIA Triad and Risk Prioritization]

The reason governance teams must understand the CIA triad is that different assets have different CIA priority profiles. A public website has very high availability requirements and moderate confidentiality requirements. A healthcare records database has extremely high confidentiality requirements and high integrity requirements. Governance decisions about where to invest security resources must reflect these differences.

[SHOW SLIDE: CISM Exam Tip 2]

CISM Exam Tip: The exam will give you scenarios and ask you to identify which CIA property is most at risk or most important for a specific situation. Practice mapping scenarios to the correct CIA component. Availability failures are often underestimated — do not overlook them.

---

### Segment 4: Governance Frameworks and Models (10:00–14:30)

[SHOW SLIDE: Key Governance Frameworks — COBIT, ISO 27001, NIST CSF]

Organizations do not build governance programs from scratch. They rely on established frameworks that provide structure, best practices, and a common language. Let us review the three frameworks you absolutely must know for this course and for the CISM exam.

[SHOW SLIDE: COBIT 2019 Overview]

COBIT — which stands for Control Objectives for Information and Related Technologies — is ISACA's own governance framework. It is designed specifically for IT governance and management. COBIT provides a comprehensive set of governance objectives, design factors, and performance indicators. Because ISACA produces both COBIT and the CISM certification, COBIT concepts appear throughout the exam.

Key COBIT concepts to know: COBIT distinguishes between governance objectives — things like ensuring risk optimization and resource optimization — and management objectives, which cover building, running, and monitoring IT capabilities. The framework is built around the idea that governance and management are distinct functions requiring different structures and accountabilities.

[SHOW SLIDE: ISO/IEC 27001 Overview]

ISO/IEC 27001 is the international standard for Information Security Management Systems, commonly called an ISMS. An ISMS is a systematic approach to managing sensitive company information — it is not a single policy or a single tool, but an entire management system built on the Plan-Do-Check-Act cycle.

Organizations can achieve ISO 27001 certification by having an accredited auditor verify that their ISMS meets the standard's requirements. For governance purposes, ISO 27001 provides a structured approach to establishing security objectives, managing risks, defining roles and responsibilities, and demonstrating continuous improvement.

[SHOW SLIDE: NIST Cybersecurity Framework Overview]

The NIST Cybersecurity Framework — often called the NIST CSF — organizes security activities into five functions: Identify, Protect, Detect, Respond, and Recover. It is widely used in the United States, especially in critical infrastructure sectors and federal agencies. While it is not a certification standard like ISO 27001, it is an excellent governance communication tool because it gives boards and executives a clear, high-level picture of where the organization's security program stands.

For governance alignment purposes, the Identify function — which covers asset management, risk assessment, and governance — is where Module 01 content lives within the NIST CSF.

[SHOW SLIDE: Framework Comparison Table]

| Framework | Produced By | Primary Use | Certification Available |
|---|---|---|---|
| COBIT 2019 | ISACA | IT Governance | No (assessments only) |
| ISO/IEC 27001 | ISO/IEC | ISMS Governance | Yes |
| NIST CSF | NIST | Risk-based security program | No |

---

### Segment 5: Roles and Responsibilities in Security Governance (14:30–18:00)

[SHOW SLIDE: Governance Roles — Board, Executive, CISO, Security Steering Committee]

One of the most important things a security manager must understand is who owns what in the governance structure. Let me walk through the key roles.

The Board of Directors provides ultimate oversight. The board sets the organization's risk appetite — the amount and type of risk the organization is willing to accept in pursuit of its objectives. The board holds the CEO and executive team accountable for operating within that risk appetite. In many larger organizations, the board has a dedicated Risk Committee or Audit Committee that takes direct ownership of cybersecurity oversight.

The Chief Information Security Officer — the CISO — is the executive responsible for leading the information security program. The CISO translates board-level risk decisions into strategy and then delegates execution to the security management team. A critical CISM concept: the CISO must be able to communicate security in business terms — not in technical jargon — to earn and maintain executive support.

The Security Steering Committee is an interdisciplinary governance body that typically includes the CISO, CIO, CFO, legal counsel, and business unit leaders. Its job is to make governance decisions — approving security policies, prioritizing security investments, and reviewing the organization's risk posture. Without a functioning steering committee, security often becomes siloed in IT with no real business accountability.

Data Owners are business-side managers who own and are responsible for the data their departments create and use. They are responsible for classifying that data and making risk acceptance decisions about it. This is a crucial concept: data ownership belongs to the business, not to IT.

[SHOW SLIDE: CISM Exam Tip 3]

CISM Exam Tip: When an exam question asks about who should approve a security policy or who should accept residual risk, the answer is almost always the business owner or executive leadership — not the security team. The security team advises and recommends; business owners decide.

---

### Segment 6: Governance Program Components and Outcomes (18:00–21:30)

[SHOW SLIDE: Five Outcomes of Effective Information Security Governance]

ISACA identifies five essential outcomes that a well-functioning information security governance program should produce. These are not technical outputs — they are governance-level achievements.

First: Strategic alignment. The security program supports and enables the organization's business objectives. Security investments are justified in terms of business value, not just technical necessity.

Second: Risk management. Risks are identified, assessed, and managed to a level acceptable to the organization. This means the organization has a clear risk appetite statement and a process for operating within it.

Third: Resource management. Security resources — people, technology, and budget — are used efficiently and effectively. Governance ensures that security investments are prioritized based on risk, not on technological preference.

Fourth: Performance management. The security program has measurable objectives and metrics that allow governance bodies to assess whether the program is achieving its intended outcomes. We will dig deeply into metrics in Module 15.

Fifth: Value delivery. Security demonstrates that it delivers value to the organization — not just by preventing incidents, but by enabling business activities that might otherwise be blocked by unmanaged risk.

[SHOW SLIDE: Building the Governance Foundation — Policy Hierarchy]

Effective governance is built on a structured policy hierarchy. At the top is the Information Security Policy — a high-level, board-approved document that states the organization's commitment to information security and establishes the overall framework. Below that are Standards, which define mandatory requirements. Below standards are Guidelines and Procedures, which provide specific implementation guidance.

We will build out this policy hierarchy in detail in Module 06. But understand now that governance cannot function without this documented foundation. A security program that runs on informal agreements and unwritten practices is not a governed program — it is a set of habits.

---

### Segment 7: Module Summary and Exam Prep (21:30–23:30)

[SHOW SLIDE: Module 01 — Key Takeaways]

Let me bring this together with the key points from Module 01.

Information security governance is the set of policies, accountability structures, and decision-making processes that direct and control an organization's security program. It operates at the strategic level — board and executive — and is distinct from security management, which executes the strategy.

The CIA triad — Confidentiality, Integrity, Availability — is the foundational framework for evaluating the security requirements of every information asset. Governance decisions about where to invest must reflect each asset's CIA priority profile.

Key governance frameworks include COBIT 2019, ISO/IEC 27001, and the NIST Cybersecurity Framework. Each provides structure for different aspects of the governance program.

Governance roles span the board, executive leadership, the CISO, the security steering committee, and data owners. Understanding who owns each type of decision is critical for the CISM exam.

Effective governance produces five outcomes: strategic alignment, risk management, resource management, performance management, and value delivery.

[SHOW SLIDE: CISM Domain 1 Exam Readiness]

For the CISM exam, Domain 1 — Information Security Governance — is 17 percent of your score. Questions in this domain will test your ability to advise on governance structure, distinguish governance from management, align security strategy with business objectives, and recommend appropriate governance roles and accountability mechanisms.

Before we move to Module 02, complete the reading guide, the governance framework lab, the module quiz, and the discussion forum. The lab will give you hands-on practice building the kind of governance artifacts that security managers produce in the real world.

---

### End Card (23:30–24:00)

[SHOW SLIDE: Module 01 Complete | Next: Module 02 — Security Strategy and Business Alignment]

Thank you for joining me for Module 01. I will see you in Module 02, where we build on this governance foundation to develop a full information security strategy aligned to business objectives.

For additional CISM study resources, visit isaca.org.

---

Script End — Module 01 | Approximate Runtime: 22 minutes

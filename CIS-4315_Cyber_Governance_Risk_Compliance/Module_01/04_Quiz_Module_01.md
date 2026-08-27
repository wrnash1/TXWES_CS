# Quiz: Module 01 - Information Security Governance Foundations
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
What is the primary objective of Information Security Governance?
*   A) Installing host antiviruses on all employee workstations
*   B) Aligning the information security strategy with overall business objectives and goals
*   C) Blocking all inbound internet traffic at the perimeter firewall
*   D) Encrypting all database backups using AES-256
*   **Correct Answer:** B) Governance ensures security operations support business goals, manage risks, and conform to corporate policies.
*   **Distractor Analysis:**
    *   *Why B is correct:* Governance is a management discipline concerned with direction, accountability, and alignment — not the execution of specific technical controls.
    *   *Why A is incorrect:* Antivirus installation is a technical control implementation task, not a governance function.
    *   *Why C is incorrect:* Blocking internet traffic is an operational security decision, not a governance objective.
    *   *Why D is incorrect:* Selecting encryption algorithms is a standards and architecture decision, not governance.

---

**Question 2**
Which of the following most accurately describes **information security governance**?
*   A) The deployment and configuration of security tools such as firewalls, IDS, and endpoint protection platforms
*   B) The system of policies, accountability structures, and decision-making processes used to direct and control an organization's security program
*   C) The technical process of scanning networks to identify open ports and unpatched vulnerabilities
*   D) The practice of encrypting data at rest and in transit to meet compliance requirements
*   **Correct Answer:** B) Information security governance encompasses the oversight structures, policies, and accountability mechanisms that align security with business direction.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deploying security tools is a management and operations function, not governance.
    *   *Why B is correct:* Governance operates at the strategic, board-facing level — establishing direction, not executing controls.
    *   *Why C is incorrect:* Vulnerability scanning is a technical assessment activity within security management.
    *   *Why D is incorrect:* Encryption practices are a control implementation concern, distinct from governance oversight.

---

**Question 3**
A newly appointed CISO at a mid-size financial firm is asked to present the company's security program value to the board of directors. Which approach best demonstrates information security governance in action?
*   A) Presenting a list of all firewall rules currently in production
*   B) Showing a dashboard of server uptime percentages for the past quarter
*   C) Mapping security risks and investment decisions to the company's stated strategic objectives and risk tolerance
*   D) Detailing the technical specifications of the newly deployed SIEM platform
*   **Correct Answer:** C) Effective governance communicates security in business terms — connecting risk decisions to organizational strategy and the board's risk appetite.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Firewall rules are operational detail irrelevant to board-level governance discussions.
    *   *Why B is incorrect:* Server uptime is an availability metric, not a governance communication.
    *   *Why C is correct:* CISM emphasizes translating security activities into business value and risk language for executive stakeholders.
    *   *Why D is incorrect:* Technical SIEM specifications are not meaningful governance content for a board audience.

---

**Question 4**
Which of the following best distinguishes security **governance** from security **management**?
*   A) Governance involves deploying technical controls; management involves writing policies
*   B) Governance provides oversight, accountability, and strategic direction; management handles day-to-day operational execution
*   C) Governance is performed by IT staff; management is performed by the board of directors
*   D) Governance applies only to regulatory compliance; management applies only to risk assessment
*   **Correct Answer:** B) Governance (oversight, direction) operates at the board/executive level; management (execution, operations) operates at the CISO and program level.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the correct relationship — governance sets direction, not deployments.
    *   *Why B is correct:* This is the ISACA-standard distinction tested throughout CISM Domain 1.
    *   *Why C is incorrect:* This reverses the organizational levels — boards govern, IT staff executes.
    *   *Why D is incorrect:* Both governance and management engage with compliance and risk; the distinction is level of authority, not subject matter.

---

**Question 5**
An organization's information security program operates in isolation from the business units and lacks executive sponsorship. Which governance risk does this scenario most directly represent?
*   A) Excessive network segmentation reducing employee productivity
*   B) Misconfigured cloud storage buckets exposing sensitive data
*   C) Lack of alignment between security strategy and business objectives, reducing program effectiveness
*   D) Insufficient patch management leading to known vulnerability exploitation
*   **Correct Answer:** C) When security operates without executive sponsorship and business alignment, it cannot prioritize resources effectively or achieve organizational support.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Network segmentation is a technical architecture issue, not a governance alignment problem.
    *   *Why B is incorrect:* Misconfigured storage is an operational/configuration management failure.
    *   *Why C is correct:* CISM Domain 1 focuses specifically on this governance failure — the absence of strategic alignment undermines the entire security program.
    *   *Why D is incorrect:* Patch management gaps are a vulnerability management issue, not a governance structure problem.

---

**Question 6**
The CIA triad is the foundational model for information security. A hospital discovers that a nurse accessed patient records for a celebrity without a clinical need to do so. The records were not altered or deleted. Which element of the CIA triad was violated?

*   A) Integrity — because the nurse accessed data she was not authorized to modify
*   B) Availability — because the access created additional load on the EHR system
*   C) Confidentiality — because the records were accessed by someone without a legitimate need to know
*   D) Non-repudiation — because the access could not be attributed to the nurse

*   **Correct Answer:** C) The CIA triad violation is confidentiality — the information was disclosed to an unauthorized party without authorization, regardless of whether data was changed or the system was disrupted.
*   **Distractor Analysis:**
    *   *Why C is correct:* Confidentiality ensures that information is accessible only to those authorized. Accessing patient records without clinical need violates the need-to-know principle of confidentiality.
    *   *Why A is incorrect:* Integrity relates to accuracy and completeness of data. No modification occurred, so integrity was not violated.
    *   *Why B is incorrect:* Availability concerns whether systems are accessible to legitimate users. The system was available; the problem is who used it.
    *   *Why D is incorrect:* Non-repudiation is not one of the three elements of the CIA triad. It is a related security property but not the framework in question.

---

**Question 7**
An organization's security team is evaluating two proposed controls. Control A prevents malicious code from executing on endpoints. Control B detects that malicious code has already executed and generates an alert. Which statement most accurately classifies these controls by functional type?

*   A) Both are preventive controls because they both address malicious code
*   B) Control A is detective; Control B is preventive
*   C) Control A is preventive; Control B is detective
*   D) Both are corrective controls because they address a common threat

*   **Correct Answer:** C) Control A acts before the harm occurs (preventive); Control B acts after the harm has begun and identifies it (detective).
*   **Distractor Analysis:**
    *   *Why C is correct:* Preventive controls stop security events from occurring. Detective controls identify that a security event has occurred or is occurring. The classification is based on timing and effect, not the threat category addressed.
    *   *Why A is incorrect:* Classifying both as preventive ignores the functional difference between stopping an event and detecting one after it begins.
    *   *Why B is incorrect:* This reverses the correct classification. Preventing malicious code execution is preventive; detection comes after.
    *   *Why D is incorrect:* Corrective controls restore operations after an incident. Neither control described restores anything — they prevent or detect.

---

**Question 8**
The COBIT 2019 governance framework organizes its design factors around a core objective. What does COBIT 2019 use as its primary organizing principle for tailoring governance?

*   A) Compliance with ISO 27001 certification requirements
*   B) The specific regulatory environment applicable to the organization's industry
*   C) The organization's enterprise goals, IT-related goals, and enabler goals aligned in a goals cascade
*   D) The number of employees and annual IT budget of the organization

*   **Correct Answer:** C) COBIT 2019 uses a goals cascade that links enterprise goals to IT-related goals to enabler goals, ensuring governance is tailored to actual business objectives.
*   **Distractor Analysis:**
    *   *Why C is correct:* The COBIT 2019 goals cascade is the framework's core alignment mechanism — it translates stakeholder needs into specific governance objectives without prescribing a one-size-fits-all approach.
    *   *Why A is incorrect:* COBIT and ISO 27001 are separate frameworks. COBIT is not organized around ISO certification requirements.
    *   *Why B is incorrect:* Regulatory environment is one of COBIT's design factors, but it is not the primary organizing principle. The goals cascade drives the overall tailoring.
    *   *Why D is incorrect:* Size and budget are not COBIT design factors. COBIT is applicable to organizations of any size and budget.

---

**Question 9**
ISO 27001 is the international standard for information security management systems. What does ISO 27001 certification primarily attest?

*   A) That an organization has implemented all controls in Annex A of ISO 27002
*   B) That an organization's ISMS has been independently audited and conforms to the ISO 27001 standard for establishing, implementing, maintaining, and continually improving the management system
*   C) That an organization has zero known vulnerabilities in its production systems
*   D) That an organization has never experienced a data breach

*   **Correct Answer:** B) ISO 27001 certification attests that an organization's information security management system — not just individual controls — has been audited and conforms to the standard.
*   **Distractor Analysis:**
    *   *Why B is correct:* ISO 27001 certification is awarded for the ISMS as a management system — the policies, processes, roles, and oversight structure — not for a specific technical configuration or security outcome.
    *   *Why A is incorrect:* Organizations select applicable controls through the Statement of Applicability based on their risk assessment. ISO 27001 does not require implementing every Annex A control.
    *   *Why C is incorrect:* No certification attests to zero vulnerabilities. ISO 27001 audits processes and management systems, not the absence of technical vulnerabilities.
    *   *Why D is incorrect:* Organizations with strong ISMS programs may still experience breaches. ISO 27001 certifies the management framework, not a breach-free history.

---

**Question 10**
The NIST Cybersecurity Framework (CSF) 2.0 introduced a sixth function in addition to the original five. Which function was added in CSF 2.0, and what is its primary purpose?

*   A) Detect — to identify cybersecurity events through continuous monitoring
*   B) Govern — to establish and monitor the organization's cybersecurity risk management strategy, expectations, and policy
*   C) Protect — to develop and implement appropriate safeguards
*   D) Respond — to take action regarding a detected cybersecurity incident

*   **Correct Answer:** B) The Govern function was added in NIST CSF 2.0 to explicitly address organizational context, risk management strategy, roles, responsibilities, and policy oversight at the enterprise level.
*   **Distractor Analysis:**
    *   *Why B is correct:* CSF 2.0 added Govern to reflect that cybersecurity risk management must be driven by leadership and embedded in organizational strategy — not treated solely as a technical practice. Govern sits above and informs all other functions.
    *   *Why A is incorrect:* Detect was one of the five original CSF functions (Identify, Protect, Detect, Respond, Recover). It was not added in CSF 2.0.
    *   *Why C is incorrect:* Protect was also an original CSF function, not a 2.0 addition.
    *   *Why D is incorrect:* Respond was an original CSF function, not a 2.0 addition.

---

**Question 11**
An organization's security policy hierarchy consists of four tiers. Tier 1 is the information security policy; Tier 2 consists of topic-specific policies; Tier 3 consists of standards; and Tier 4 consists of procedures. An IT administrator asks which tier specifies the exact steps for revoking a departed employee's access credentials. Which tier should contain this guidance?

*   A) Tier 1 — the information security policy
*   B) Tier 2 — topic-specific policies
*   C) Tier 3 — standards
*   D) Tier 4 — procedures

*   **Correct Answer:** D) Step-by-step operational instructions belong at the procedure level (Tier 4), which provides the specific "how" for executing security requirements.
*   **Distractor Analysis:**
    *   *Why D is correct:* Procedures are the operational documents that translate policy intent into executable steps. Revoking access credentials is an operational task requiring specific sequenced instructions.
    *   *Why A is incorrect:* The Tier 1 policy states high-level intent and requirements but not step-by-step instructions.
    *   *Why B is incorrect:* Topic-specific policies may establish access management requirements but do not contain procedural steps for system administrators.
    *   *Why C is incorrect:* Standards specify configuration requirements and minimums but not the sequential execution steps.

---

**Question 12**
A security steering committee has been proposed as the governance mechanism for an organization's information security program. Which statement best describes the appropriate membership and function of this committee?

*   A) The committee should consist exclusively of IT staff who can evaluate technical security solutions
*   B) The committee should include senior business leaders, the CISO, Legal, and Compliance, and should provide strategic oversight, approve policies, and allocate security resources
*   C) The committee should consist of external auditors who independently assess security decisions
*   D) The committee should be chaired by the most senior IT engineer to ensure technical accuracy of security decisions

*   **Correct Answer:** B) The security steering committee's value comes from cross-functional business leadership participation, which ensures security decisions reflect organizational priorities and receive appropriate authority and resources.
*   **Distractor Analysis:**
    *   *Why B is correct:* An effective steering committee brings together business, legal, compliance, and security leadership to make governance-level decisions — not operational technical ones. This ensures security is a business function, not an IT silo.
    *   *Why A is incorrect:* IT-only composition limits the committee to technical perspective and removes the business alignment and authority needed for governance decisions.
    *   *Why C is incorrect:* External auditors assess and report; they do not govern. A governance committee makes decisions; an audit function evaluates them.
    *   *Why D is incorrect:* The most senior engineer is a technical expert, not a governance leader. Governance authority derives from business seniority and accountability, not technical rank.

---

**Question 13**
A data owner at a financial services firm is reviewing access to a critical system. What is the primary accountability assigned to the data owner role?

*   A) Performing daily backups of the data and verifying restoration procedures
*   B) Configuring the firewall rules that protect the system from external access
*   C) Determining the classification of the data and authorizing who is permitted to access it
*   D) Installing security patches on the servers that store the data

*   **Correct Answer:** C) The data owner's primary accountability is to define the data's classification level and authorize access — the business decisions about what the data is worth and who needs it.
*   **Distractor Analysis:**
    *   *Why C is correct:* The data owner is a business role responsible for determining sensitivity and appropriate use of data. Access authorization and classification are business judgments, not technical tasks.
    *   *Why A is incorrect:* Backup operations are performed by the data custodian (typically IT operations), not the data owner. The owner sets requirements; the custodian executes them.
    *   *Why B is incorrect:* Firewall configuration is an IT security operations function performed by technical staff, not the business data owner.
    *   *Why D is incorrect:* Patch management is a data custodian or system administrator function. The data owner does not perform technical maintenance on the systems.

---

**Question 14**
Which of the following describes the primary difference between the data owner and the data custodian?

*   A) Data owners are external consultants; data custodians are internal employees
*   B) Data owners hold business accountability for the data's classification and use; data custodians implement technical controls to protect it as directed by the owner
*   C) Data custodians set data retention policies; data owners delete data when retention periods expire
*   D) Data owners and data custodians perform identical functions under different names

*   **Correct Answer:** B) The data owner is a business accountability role; the data custodian is the technical stewardship role that implements the owner's requirements.
*   **Distractor Analysis:**
    *   *Why B is correct:* This division of responsibility is fundamental to the CISM governance model. Owners decide; custodians execute and protect. Neither role alone constitutes complete governance.
    *   *Why A is incorrect:* Both roles are typically internal to the organization. The owner-custodian model does not correspond to an internal-external distinction.
    *   *Why C is incorrect:* Retention policy is typically set by the data owner in conjunction with Legal; technical retention enforcement is a custodian function.
    *   *Why D is incorrect:* The roles are distinct and serve different functions. Conflating them creates governance gaps and accountability ambiguity.

---

**Question 15**
An organization's board of directors wants to understand whether the information security program is achieving its objectives. Which of the following governance artifacts would most directly answer their question?

*   A) The current network topology diagram showing all security zones and firewall placement
*   B) The organization's vulnerability scan report from the most recent quarterly assessment
*   C) A security program performance dashboard showing key risk indicators, security investment alignment, and residual risk levels against the organization's risk appetite
*   D) The complete list of open security incidents from the past twelve months

*   **Correct Answer:** C) A governance-level dashboard communicates program effectiveness in business risk terms — the language appropriate for board oversight.
*   **Distractor Analysis:**
    *   *Why C is correct:* Boards govern by overseeing risk and strategy, not by reviewing technical details. KRIs, investment alignment, and residual risk relative to appetite are the metrics boards can act on.
    *   *Why A is incorrect:* A network topology diagram is a technical architectural artifact with no governance interpretation value for non-technical board members.
    *   *Why B is incorrect:* A vulnerability scan report is operational data. Boards are not equipped to evaluate which CVEs are material — that translation is the security manager's job.
    *   *Why D is incorrect:* A raw incident list provides no program performance context. Without analysis of detection timeliness or business impact, the list does not answer the board's governance question.

---

**Question 16**
A multinational corporation operates in 12 countries and has recently adopted a centralized information security governance model. Regional IT managers complain that the global security policies do not account for country-specific data residency laws and local operational constraints. Which governance structure adjustment would best resolve this tension?

*   A) Eliminate regional IT manager roles and consolidate all security decisions at headquarters
*   B) Allow each country to develop entirely independent security policies with no reference to the global framework
*   C) Adopt a federated governance model in which global baseline policies set minimum requirements and regional policies address jurisdiction-specific requirements within those boundaries
*   D) Defer all country-specific security decisions to external legal counsel in each jurisdiction

*   **Correct Answer:** C) A federated governance model balances enterprise-wide consistency with the flexibility to address regional legal and operational realities — a recognized best practice for multinational security programs.
*   **Distractor Analysis:**
    *   *Why C is correct:* CISM governance principles support a tiered policy architecture where a global framework sets non-negotiable baseline requirements and regional supplements address local variances without contradicting the baseline. This preserves enterprise oversight while accommodating legitimate jurisdictional differences.
    *   *Why A is incorrect:* Eliminating regional roles removes the domain expertise needed to identify and respond to local legal and operational requirements, increasing compliance risk and operational friction.
    *   *Why B is incorrect:* Fully independent regional policies fragment the security program, create inconsistent protection levels, and undermine enterprise-wide risk visibility — the opposite of effective governance.
    *   *Why D is incorrect:* Legal counsel advises on compliance requirements but does not govern the security program. Delegating security governance decisions to external counsel creates accountability gaps and is not a recognized governance structure.

---

**Question 17**
A RACI matrix is being developed for a new security incident response process. The security operations center (SOC) manager is listed as "Accountable" for all incident response activities. Three analysts, the CISO, and the legal team are all listed as "Responsible" for the same activities. What is the primary governance problem with this RACI assignment?

*   A) The SOC manager should be listed as "Consulted" rather than "Accountable" for incident response
*   B) Having multiple parties listed as "Responsible" for the same activities creates role confusion, but the deeper problem is that "Accountable" should be a singular assignment — only one person can ultimately own the outcome
*   C) The legal team should not appear in any RACI for security processes
*   D) RACI matrices are not appropriate governance tools for operational processes like incident response

*   **Correct Answer:** B) A core RACI principle is that accountability must be singular — only one person or role can hold ultimate ownership for a given activity. Multiple "Responsible" parties are acceptable, but multiple "Accountable" parties create governance confusion over who owns the outcome.
*   **Distractor Analysis:**
    *   *Why B is correct:* The RACI model defines Accountable as the single owner who answers for the activity's completion and quality. When multiple "Responsible" parties exist without clear coordination, and accountability is ambiguous, no one is truly answerable — a governance failure.
    *   *Why A is incorrect:* The SOC manager's assignment as "Accountable" for incident response is appropriate given their operational authority. The problem is not the SOC manager's designation but the structural issue with multiple Responsible assignments and unclear singular accountability.
    *   *Why C is incorrect:* Legal teams are frequently and appropriately included in incident response RACI matrices, particularly for data breach notification decisions, regulatory reporting, and evidence handling guidance.
    *   *Why D is incorrect:* RACI matrices are widely used governance tools for operational processes, including incident response. ISACA and NIST both recommend RACI structures for defining roles in security processes.

---

**Question 18**
An organization's acceptable use policy (AUP) was last reviewed three years ago and does not address cloud storage services, personal mobile devices used for work, or AI-assisted productivity tools — all of which employees are now actively using. A policy review committee has been formed. Which aspect of information security governance does this situation most directly reflect?

*   A) A failure of the security operations center to monitor employee activity
*   B) A technical control gap requiring immediate deployment of mobile device management software
*   C) A policy lifecycle management failure — governance documents must be reviewed and updated regularly to remain aligned with the current threat and technology environment
*   D) A compliance violation requiring immediate regulatory notification

*   **Correct Answer:** C) Effective governance requires that policies remain current. An outdated AUP creates an undefined behavioral environment — employees cannot be held accountable for violating rules that do not exist, and the organization has no stated governance position on material security risks.
*   **Distractor Analysis:**
    *   *Why C is correct:* Policy lifecycle management — including scheduled reviews, change-triggered reviews, and version control — is a fundamental governance discipline. A three-year-old AUP that does not address current technology use represents a governance gap, not merely an operational one.
    *   *Why A is incorrect:* SOC monitoring is a detective control function. The governance problem here is the absence of policy guidance, not the absence of monitoring. You cannot enforce compliance with a policy that does not address the activity in question.
    *   *Why B is incorrect:* MDM deployment is a technical control response that may be warranted, but deploying technology without a governing policy still leaves the organization without defined acceptable use rules. The policy gap must be addressed first.
    *   *Why D is incorrect:* An outdated internal policy is not itself a regulatory violation. Whether regulatory notification is required depends on whether a specific breach or compliance failure has occurred — the scenario describes a policy gap, not an incident.

---

**Question 19**
The GRC (Governance, Risk, and Compliance) model integrates three previously siloed organizational functions. A company implements a GRC platform but continues to operate its security governance, risk management, and compliance programs independently with separate reporting chains and no shared data. Which statement best describes the organization's GRC maturity?

*   A) The organization has fully implemented GRC because it has deployed a GRC platform
*   B) The organization has achieved compliance-driven GRC because all three functions report separately
*   C) The organization has low GRC maturity — tool adoption without integration of processes, data, and reporting does not constitute effective GRC implementation
*   D) The organization needs a new GRC platform vendor, as the current tool is evidently not functioning

*   **Correct Answer:** C) GRC maturity is measured by the integration of governance, risk, and compliance processes and data — not by the presence of a software platform. Deploying a tool while maintaining organizational silos produces no meaningful GRC benefit.
*   **Distractor Analysis:**
    *   *Why C is correct:* ISACA's COBIT and leading GRC frameworks distinguish between tool adoption and capability maturity. True GRC integration requires shared risk taxonomies, unified reporting, cross-functional visibility, and coordinated decision-making — none of which are present in this scenario.
    *   *Why A is incorrect:* GRC platform deployment is a necessary but insufficient condition for GRC implementation. A platform populates its value only when the underlying processes are integrated. A tool running three separate, disconnected workflows is not GRC.
    *   *Why B is incorrect:* "Compliance-driven GRC" is not a recognized maturity designation. Separate reporting chains are a symptom of low maturity, not a defined GRC operating model.
    *   *Why D is incorrect:* The problem is organizational and process-related, not a platform deficiency. Switching vendors without addressing the structural separation of functions would produce the same outcome.

---

**Question 20**
A healthcare organization's board of directors approves an annual security budget of $2.1 million and formally adopts an information security risk appetite statement specifying that no single unmitigated risk should carry an ALE exceeding $400,000. Six months into the fiscal year, the CISO identifies a new risk with an estimated ALE of $650,000. No budget remains for additional controls. What is the CISO's most appropriate governance action?

*   A) Implement available no-cost compensating controls and informally accept the remaining exposure until next year's budget cycle
*   B) Escalate the risk to the board or risk committee with a documented analysis, because the ALE exceeds the approved risk appetite threshold and a formal acceptance or budget exception decision is required at the governance level
*   C) Transfer the entire risk to the organization's cyber liability insurer without further board involvement
*   D) Reduce the estimated ALE by revising the exposure factor downward until it falls within appetite, then document the adjusted figure in the risk register

*   **Correct Answer:** B) When an identified risk exceeds the board-approved risk appetite threshold and available resources are insufficient to bring it within appetite, the matter must be escalated to the level of authority that established the appetite — the board or risk committee — for a formal governance decision.
*   **Distractor Analysis:**
    *   *Why B is correct:* The risk appetite statement is a board-level governance decision. A risk that exceeds the stated appetite cannot be informally accepted by the CISO — that decision belongs to the authority that set the threshold. Formal escalation with documented analysis is the correct governance action, enabling the board to decide whether to formally accept the exceedance, authorize an emergency budget exception, or direct an alternative treatment.
    *   *Why A is incorrect:* Informal acceptance of a risk that materially exceeds the board-approved appetite is a governance failure. It deprives the board of the visibility needed to exercise oversight and creates an undocumented liability. The CISO does not have unilateral authority to accept risks above the board-set threshold.
    *   *Why C is incorrect:* Risk transfer through insurance may be an option the board considers, but it is a treatment decision — not a substitute for the governance escalation process. The CISO cannot unilaterally commit to an insurance strategy for a risk that exceeds the governance threshold without board-level direction.
    *   *Why D is incorrect:* Revising risk estimates to fit within appetite rather than to reflect actual exposure is a fundamental analytical and ethical failure. Risk registers must reflect honest assessments. Manipulating estimates to avoid governance scrutiny undermines the integrity of the entire risk management program.

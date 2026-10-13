# Quiz: Module 11 - Service Management Practices - Service Level Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the Service Level Management practice in ITIL 4?
*   A) To negotiate contracts with external IT suppliers and ensure they meet minimum technical performance standards.
*   B) To set clear, business-based targets for service levels and ensure that delivery of services is properly assessed, monitored, and managed against those targets.
*   C) To document and fulfill all user requests for standard services within agreed timeframes.
*   D) To investigate incidents that breach agreed response or resolution times and identify their root causes.
*   **Correct Answer:** B) The purpose of SLM is to set business-based service level targets and ensure service delivery is assessed and managed against those targets.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of Service Level Management as setting clear, business-based targets for service levels, and ensuring that delivery of services is properly assessed, monitored, and managed against those targets. SLM creates and maintains the shared understanding between service provider and customer about service quality expectations.
    *   *Why A is incorrect:* Negotiating and managing contracts with external suppliers is handled through the Supplier Management practice and underpinning contracts. SLM focuses on the relationship with the customer, not the supplier.
    *   *Why C is incorrect:* Documenting and fulfilling user requests is the purpose of Service Request Management. SLM sets performance targets and monitors service quality — it does not fulfill requests.
    *   *Why D is incorrect:* Investigating SLA-breaching incidents and finding root causes is Problem Management. SLM monitors performance against targets and manages the customer relationship around those targets.

---

**Question 2**
Which of the following most accurately describes the difference between a Service Level Agreement (SLA), an Operational Level Agreement (OLA), and an Underpinning Contract (UC)?
*   A) An SLA is between the service provider and an external supplier; an OLA is between the provider and the customer; a UC is an internal agreement between IT teams.
*   B) An SLA defines the service targets agreed with the customer; an OLA defines internal commitments between IT teams within the same organization; a UC is a legally binding contract with an external third-party supplier.
*   C) All three are identical in structure but differ only in the name used — SLA for customers, OLA for vendors, and UC for internal teams.
*   D) An SLA and an OLA are both external-facing agreements with customers; a UC is an internal agreement used only for infrastructure teams.
*   **Correct Answer:** B) An SLA is with the customer, an OLA is between internal teams, and a UC is a legally binding contract with an external third-party supplier.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 distinguishes these three agreement types by the parties involved. An SLA is agreed between the service provider and the customer. An OLA is between the service provider and an internal support group. A UC is a formal contract between the service provider and an external supplier. OLAs and UCs both underpin the SLA by ensuring internal and external parties deliver at the required level.
    *   *Why A is incorrect:* This reverses the relationships — the SLA is with the customer, not an external supplier, and the OLA is internal, not with the customer.
    *   *Why C is incorrect:* These are not interchangeable terms for the same agreement type. They are distinct agreement structures with different parties, different scopes, and different legal standing.
    *   *Why D is incorrect:* OLAs are internal agreements, not external-facing. They define commitments between IT teams within the same organization — not between the provider and customers.

---

**Question 3**
An IT service provider's monthly SLA report shows that all metrics are green: system availability is 99.9%, incident response time averages 8 minutes against a 15-minute target, and resolution time averages 3 hours against a 4-hour target. However, the quarterly customer satisfaction survey shows a satisfaction score of 42 out of 100 — the lowest on record. What does this situation most likely indicate?
*   A) The SLA metrics are incorrect — the IT team must have miscalculated availability and response time figures.
*   B) This is a watermelon SLA — the metrics appear green on the outside but do not reflect actual customer experience, indicating the targets are not measuring what matters most to customers.
*   C) The customer satisfaction survey is unreliable — customers tend to rate services poorly regardless of actual performance.
*   D) The IT team should increase the SLA targets (make them harder to meet) to force the team to perform better and improve satisfaction.
*   **Correct Answer:** B) This is a classic watermelon SLA — the technical metrics show green while customer satisfaction reveals that the SLA targets do not capture what actually matters to customers.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 specifically introduces the "watermelon SLA" concept to describe this scenario. When SLA metrics are consistently met but customers remain dissatisfied, it means the measured targets do not reflect the aspects of service quality that matter most to customers. The fix is to engage with customers to identify what they actually value and revise the SLA metrics accordingly.
    *   *Why A is incorrect:* There is no indication the metrics are miscalculated. The problem is not data accuracy — it is that the metrics being measured do not correspond to customer priorities.
    *   *Why C is incorrect:* ITIL 4 emphasizes that customer feedback is a critical input for SLM. Dismissing survey results contradicts the customer-engagement principle of SLM and eliminates a valuable signal for improvement.
    *   *Why D is incorrect:* Tightening existing targets without addressing whether those targets measure the right things would not resolve the dissatisfaction. The issue is the choice of metrics, not the threshold values.

---

**Question 4**
A company's SLA with its customers commits to 99.5% monthly availability for its order management system. The internal network team provides connectivity for this system. Which type of agreement should be in place between the IT service provider and the internal network team to support this SLA commitment?
*   A) A Service Level Agreement (SLA) — the network team is a customer of the IT service provider and should receive the same formal agreement.
*   B) An Underpinning Contract (UC) — the network team is an external supplier and requires a legally binding contract.
*   C) An Operational Level Agreement (OLA) — the network team is an internal support group within the same organization, and an OLA defines their internal commitments to support the SLA.
*   D) No formal agreement is needed — internal teams are expected to deliver without documentation.
*   **Correct Answer:** C) An OLA is appropriate between the IT service provider and an internal team like the network group, defining the internal commitments that underpin the SLA.
*   **Distractor Analysis:**
    *   *Why C is correct:* An OLA is an agreement between an IT service provider and another part of the same organization. The internal network team providing connectivity is an internal support group, not a customer. An OLA defines their specific commitments — such as network availability targets — that enable the overall SLA to be met.
    *   *Why A is incorrect:* An SLA is for external customers, not internal support teams. Treating the network team as a customer of the IT provider misidentifies the relationship.
    *   *Why B is incorrect:* An Underpinning Contract is for external third-party suppliers who are outside the organization. The internal network team is part of the same organization.
    *   *Why D is incorrect:* ITIL 4 requires that internal commitments supporting SLAs be formally documented. Undocumented expectations create ambiguity and make it difficult to identify where SLA failures originate.

---

**Question 5**
A service level review meeting reveals that the IT team has met every SLA metric for the past six months. The customer asks whether the agreed service level targets could be reviewed and updated to reflect new business requirements that have emerged since the SLA was originally signed. What does ITIL 4 Service Level Management say about this request?
*   A) SLAs are legally binding documents that cannot be changed until the contract expires — the customer must wait until the renewal date.
*   B) SLA reviews and updates are a normal part of Service Level Management. SLM requires ongoing engagement with customers to ensure targets remain relevant as business needs change.
*   C) Since all metrics are green, there is no justification for changing the SLA — the current agreement is performing well and should remain unchanged.
*   D) Only the service provider has the authority to propose SLA changes — customers may provide feedback but cannot initiate a review.
*   **Correct Answer:** B) SLM requires ongoing customer engagement and regular review of SLAs to ensure they remain aligned with evolving business needs.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 positions SLM as an ongoing practice that involves continual engagement with customers, not a one-time contract event. Regular reviews ensure that SLA targets remain relevant, meaningful, and aligned with actual business priorities. The customer's request to update targets based on changed requirements is exactly what SLM is designed to accommodate.
    *   *Why A is incorrect:* While SLAs may have contract terms, ITIL 4 SLM emphasizes flexibility and ongoing review rather than rigid contractual immutability. Treating an SLA as untouchable until expiry ignores the continual improvement and customer engagement principles of SLM.
    *   *Why C is incorrect:* Meeting current targets does not mean the targets are still the right ones. If the business has evolved, previously green metrics may no longer reflect what the customer actually needs. SLM requires proactive review, not just metric compliance.
    *   *Why D is incorrect:* SLM is a collaborative practice. Both parties — the service provider and the customer — contribute to SLA reviews. Customer-initiated reviews based on changed business needs are a healthy and expected part of the SLM process.

---

**Question 6 (5 points)**
A service provider has SLA commitments to a customer, OLAs with internal teams (network, storage, and server), and a UC with an external hosting vendor. The external hosting vendor fails to meet its contractual uptime commitment, causing the SLA with the customer to be breached. Which statement correctly describes the relationship between these agreements?

*   A) The UC breach automatically voids the SLA, so the customer cannot claim service credits.
*   B) The OLAs with internal teams are the correct agreements to invoke against the hosting vendor.
*   C) The SLA breach is the customer-facing impact; the provider must pursue the hosting vendor through the UC. OLAs and UCs underpin the SLA but do not eliminate the provider's accountability to the customer.
*   D) Since the breach was caused by an external vendor, the SLA obligations to the customer are suspended until the UC is resolved.

*   **Correct Answer:** C) The SLA breach is the customer-facing impact; the provider must pursue the hosting vendor through the UC. OLAs and UCs underpin the SLA but do not eliminate the provider's accountability to the customer.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 establishes that the service provider remains accountable to the customer under the SLA regardless of the cause of the failure. The UC is the mechanism the provider uses to hold the external vendor accountable — but the customer's rights under the SLA are separate. The provider cannot pass the breach to the customer simply because the root cause was a vendor failure.
    *   *Why A is incorrect:* A UC breach by a supplier does not void the SLA. The SLA remains in force between the provider and the customer. The provider bears the customer-facing consequences and recovers from the vendor through the UC.
    *   *Why B is incorrect:* OLAs govern internal team commitments within the same organization. They cannot be invoked against an external vendor — that is the role of the UC.
    *   *Why D is incorrect:* ITIL 4 does not recognize force majeure or third-party fault as automatic suspensions of SLA obligations unless specific SLA clauses address this. By default, the provider's obligations to the customer continue.

---

**Question 7 (5 points)**
An SLA for a payroll processing system includes the following clause: "If monthly availability falls below 99.5%, the service provider will issue a service credit of 10% of the monthly fee for each 0.5% of availability below the target." What ITIL 4 SLM concept does this clause represent, and what is its primary purpose?

*   A) A utility definition — it describes the functional capability the service provides to the customer.
*   B) A service credit and penalty clause — it creates a financial consequence for SLA breaches, incentivizing the provider to maintain committed service levels.
*   C) An OLA escalation trigger — it specifies when the service provider must escalate internally to the network team.
*   D) A warranty definition — it defines the conditions under which the service must perform.

*   **Correct Answer:** B) A service credit and penalty clause — it creates a financial consequence for SLA breaches, incentivizing the provider to maintain committed service levels.
*   **Distractor Analysis:**
    *   *Why B is correct:* Service credits are financial remedies specified in SLAs that activate when agreed targets are breached. Their purpose is twofold: they compensate the customer for poor service and they create a direct financial incentive for the provider to maintain performance. ITIL 4 recognizes that SLAs should include consequences for breaches — not just targets — to be effective governance instruments.
    *   *Why A is incorrect:* Utility in ITIL 4 refers to what the service does — its functional fit for purpose. A penalty clause is not a description of service functionality.
    *   *Why C is incorrect:* OLA escalation triggers govern internal team handoffs. This clause is a customer-facing financial mechanism in the SLA, not an internal escalation trigger.
    *   *Why D is incorrect:* Warranty in ITIL 4 refers to how a service performs — its fitness for use, covering availability, capacity, and continuity. While availability targets are part of warranty, a penalty clause specifying financial credits is not itself a warranty definition.

---

**Question 8 (5 points)**
According to ITIL 4, what is the recommended frequency for formal service level review meetings between the service provider and the customer, and what should those meetings accomplish?

*   A) Daily — to ensure that every SLA metric is trending positively before issues arise.
*   B) Only when an SLA breach occurs — reactive meetings are sufficient to manage service level performance.
*   C) Regularly (typically monthly or quarterly) — to review performance against targets, discuss trends, address issues proactively, and agree on improvement actions before breaches occur.
*   D) Annually — to renegotiate the SLA contract and update targets for the coming year.

*   **Correct Answer:** C) Regularly (typically monthly or quarterly) — to review performance against targets, discuss trends, address issues proactively, and agree on improvement actions before breaches occur.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 SLM emphasizes proactive customer engagement through regular service reviews. Monthly or quarterly meetings provide a structured cadence for reviewing performance data, identifying emerging trends, discussing improvements, and maintaining the collaborative relationship between provider and customer. Proactive reviews prevent small issues from becoming SLA breaches.
    *   *Why A is incorrect:* Daily review meetings would be operationally impractical for SLA governance. ITIL 4 does not recommend daily meetings for SLM — that level of frequency is appropriate for incident management, not service level governance.
    *   *Why B is incorrect:* Reactive-only meetings mean problems are only addressed after breaches occur, missing the early warning signals that regular reviews would catch. ITIL 4 consistently emphasizes proactive, not just reactive, management.
    *   *Why D is incorrect:* Annual-only meetings are too infrequent for effective SLM. Annual reviews may be appropriate for major contract renewals, but ongoing performance governance requires more frequent interaction.

---

**Question 9 (5 points)**
An SLA for a customer service platform specifies three metrics: (1) system availability ≥ 99.8%, (2) average incident response time ≤ 10 minutes, and (3) average incident resolution time ≤ 4 hours. All three metrics are currently being met. However, a new business requirement means that peak transaction volume has tripled, causing response times to slow noticeably even though they remain within the 10-minute target. What does this situation indicate about the SLA metrics?

*   A) The SLA is performing correctly — all metrics are green, so no changes are needed.
*   B) The SLA metrics may no longer reflect current business performance requirements. The response time target may need to be revised to reflect the new transaction volume reality.
*   C) The tripling of transaction volume is a force majeure event that automatically suspends the SLA.
*   D) The customer should lower their transaction volume to match the original SLA design parameters.

*   **Correct Answer:** B) The SLA metrics may no longer reflect current business performance requirements. The response time target may need to be revised to reflect the new transaction volume reality.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 SLM recognizes that SLA targets must evolve with business requirements. When the operational context changes significantly — such as a major increase in transaction volume — existing targets that were adequate before may become insufficient even when technically met. Proactive SLM involves reviewing whether targets remain fit for purpose as the business changes, not just tracking compliance with outdated thresholds.
    *   *Why A is incorrect:* Green metrics do not guarantee the SLA is still relevant. This scenario echoes the watermelon SLA concept — if performance is noticeably degrading from a user perspective even within targets, the targets need review.
    *   *Why C is incorrect:* ITIL 4 does not recognize increased business demand as a force majeure event. The provider and customer should collaboratively address capacity requirements through SLA review and potentially a capacity planning exercise.
    *   *Why D is incorrect:* Asking the customer to reduce their business activity to fit IT constraints contradicts the service orientation of ITIL 4. IT services must support business needs — not the reverse.

---

**Question 10 (5 points)**
In ITIL 4, utility and warranty are the two dimensions used to assess whether a service creates value. Which statement correctly distinguishes between utility and warranty in the context of an SLA?

*   A) Utility describes who is responsible for maintaining the service; warranty describes the cost of the service to the customer.
*   B) Utility describes what the service does (its functional purpose — fitness for purpose); warranty describes how well the service performs (its availability, reliability, and support — fitness for use).
*   C) Utility and warranty are interchangeable terms for the same concept — both describe the quality of a service.
*   D) Utility refers to the SLA penalty clauses; warranty refers to the SLA review meeting schedule.

*   **Correct Answer:** B) Utility describes what the service does (its functional purpose — fitness for purpose); warranty describes how well the service performs (its availability, reliability, and support — fitness for use).
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines utility as "fitness for purpose" — the service does what the customer needs it to do (e.g., an email service sends and receives email). Warranty is "fitness for use" — the service performs reliably under agreed conditions (e.g., email is available 99.9% of the time, with a 15-minute response time target). An SLA captures warranty commitments explicitly. Both are required for the service to create value — a service that works but is always unavailable (no warranty) creates no value, as does a highly available service that does the wrong thing (no utility).
    *   *Why A is incorrect:* Responsibility assignments and cost structures are separate governance topics — RACI matrices and financial management practices respectively. They do not define utility or warranty.
    *   *Why C is incorrect:* Utility and warranty are distinct and complementary concepts in ITIL 4's value co-creation model. Conflating them as interchangeable misrepresents a fundamental ITIL 4 distinction tested on the Foundation exam.
    *   *Why D is incorrect:* Penalty clauses and review schedules are SLM operational elements, not the definitions of utility and warranty. These ITIL 4 terms apply to service value assessment, not SLA contract mechanics.

---

**Question 11 (5 points)**
A hospital IT team includes the following clause in its EHR SLA: "If the EHR system is unavailable for more than 30 minutes during a business day, the IT team will notify the VP of Clinical Operations within 15 minutes of confirmed outage." Which aspect of SLA management does this clause represent?
*   A) An OLA target between the service desk and the infrastructure team
*   B) A proactive breach communication protocol embedded in the SLA
*   C) A UC penalty clause with an external vendor
*   D) An XLA outcome measurement requirement

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 best practice requires that SLAs include breach notification commitments — not just performance targets — so customers receive timely information when service commitments are at risk. This clause is an embedded communication protocol within the SLA.
    *   *Why A is incorrect:* An OLA target governs an internal IT-to-IT team commitment, not a customer-facing communication protocol.
    *   *Why C is incorrect:* A UC penalty clause governs the organization's recourse against an external supplier, not customer-facing outage communication.
    *   *Why D is incorrect:* An XLA measurement defines how user experience quality is measured, not how breach communications are structured.

---

**Question 12 (5 points)**
According to ITIL 4, which of the following best describes what "availability" measures in the context of an SLA?
*   A) The number of incidents that affected the service during the measurement period
*   B) The percentage of agreed service time during which the service is functional and accessible to users
*   C) The speed at which the service desk responds to user incidents
*   D) The number of hours IT staff spend maintaining the service each month

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines availability as the ability of a service to perform its agreed function when required, expressed as a percentage of agreed service time.
    *   *Why A is incorrect:* The number of incidents is an incident management metric, not the definition of availability. Availability measures time-based uptime, not incident count.
    *   *Why C is incorrect:* Response speed is a response time metric, not availability. Response time and availability are separate SLA targets.
    *   *Why D is incorrect:* Staff hours is a resource utilization metric with no direct relationship to the definition of service availability.

---

**Question 13 (5 points)**
An IT service manager states that the current SLA for the HR system was designed by the IT team two years ago without any customer input. Which ITIL 4 SLM principle does this design approach violate?
*   A) SLAs should be as short as possible to avoid complex legal language.
*   B) SLAs should be developed collaboratively with the customer to ensure they reflect actual business needs and priorities, not just IT-convenient metrics.
*   C) SLAs must only be signed by senior IT leadership and not by business stakeholders.
*   D) SLAs should be based on the IT team's existing monitoring capabilities, not on business requirements.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 SLM requires collaborative SLA design that reflects business priorities and customer-defined outcomes. A provider-only designed SLA risks becoming a watermelon SLA that measures what IT finds convenient rather than what matters to the customer.
    *   *Why A is incorrect:* SLA length is not an ITIL 4 design principle. Clarity and completeness matter more than brevity.
    *   *Why C is incorrect:* ITIL 4 requires customer involvement in SLAs, including customer-side signatories. Restricting signatures to IT leadership contradicts the collaborative engagement model.
    *   *Why D is incorrect:* SLAs must be based on business requirements first. If current monitoring cannot support a required metric, monitoring must be improved — not the SLA target lowered to match monitoring limitations.

---

**Question 14 (5 points)**
An organization's service review meeting reveals a pattern: P1 incidents are consistently resolved within the 2-hour SLA target, but the same P1 incidents tend to recur two to three times per quarter. Which additional practice should Service Level Management engage to address this pattern?
*   A) Service Request Management — to log the recurring P1s as service requests
*   B) Change Enablement — to immediately raise a standard change for each P1
*   C) Problem Management — to investigate the root cause of recurring incidents and prevent recurrence
*   D) Monitoring and Event Management — to disable the alerts that trigger the P1 incidents

*   **Correct Answer:** C
*   **Distractor Analysis:**
    *   *Why C is correct:* When incidents recur despite timely resolution, Problem Management is the correct practice to engage — it investigates root causes and implements permanent fixes to prevent recurrence.
    *   *Why A is incorrect:* Service Request Management handles standard, pre-approved fulfillment requests. Recurring P1 incidents are not service requests.
    *   *Why B is incorrect:* A standard change is a pre-authorized, low-risk repeatable change. A systemic P1 root cause fix would likely require a normal or emergency change after Problem Management identifies the fix — not a standard change raised reactively to each P1.
    *   *Why D is incorrect:* Disabling alerts would hide the problem rather than solve it, creating safety and compliance risks.

---

**Question 15 (5 points)**
Which ITIL 4 Guiding Principle most directly explains why a service provider should inform a customer about an SLA breach as soon as it is confirmed, rather than waiting for the next scheduled monthly report?
*   A) Keep It Simple and Practical
*   B) Optimize and Automate
*   C) Collaborate and Promote Visibility
*   D) Think and Work Holistically

*   **Correct Answer:** C
*   **Distractor Analysis:**
    *   *Why C is correct:* Proactive breach communication exemplifies Collaborate and Promote Visibility — sharing performance information transparently with stakeholders as soon as it is known, rather than concealing it until a scheduled report.
    *   *Why A is incorrect:* Keep It Simple and Practical is about eliminating unnecessary complexity in processes, not about communication timing.
    *   *Why B is incorrect:* Optimize and Automate focuses on process efficiency and automation adoption, not on stakeholder communication ethics.
    *   *Why D is incorrect:* Think and Work Holistically is about considering system-wide impacts. The communication timing principle is more precisely described by Collaborate and Promote Visibility.

---

**Question 16 (5 points)**
A service provider's SLA commits to 99.8% monthly availability. In a given month, the system experienced: (1) a 2-hour planned maintenance window on Saturday night, and (2) a 1-hour unplanned outage on Wednesday at 10 AM. The SLA's agreed service hours are Monday–Friday 8 AM–8 PM. The month has 720 total hours. How much downtime counts against the SLA?
*   A) 3 hours — both the maintenance window and the unplanned outage count
*   B) 1 hour — only the Wednesday business-hours outage counts
*   C) 2 hours — only the Saturday maintenance window counts
*   D) 0 hours — planned maintenance is always exempt and the 1-hour outage was minor

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* The SLA covers agreed service hours (Monday–Friday 8 AM–8 PM). Saturday night is outside agreed service hours, so the maintenance window does not count against the SLA. Wednesday at 10 AM is within agreed service hours, so the 1-hour unplanned outage counts.
    *   *Why A is incorrect:* Saturday is outside the agreed service window; that downtime cannot be counted against an SLA that only covers business hours.
    *   *Why C is incorrect:* The reverse — only the Saturday window counting is incorrect. Saturday is outside the service window; Wednesday is inside it.
    *   *Why D is incorrect:* The 1-hour Wednesday outage counts against the SLA regardless of its duration. There is no minimum duration threshold for SLA downtime in ITIL 4.

---

**Question 17 (5 points)**
An ITSM manager proposes replacing all SLA reports with a single customer satisfaction dashboard showing only Net Promoter Score and Customer Effort Score. A colleague argues this would make it impossible to identify what specifically caused satisfaction to drop. Which statement best resolves this disagreement?
*   A) The ITSM manager is right — XLA measurements make SLA reports unnecessary.
*   B) The colleague is right — NPS and CES alone provide insufficient diagnostic detail for root cause analysis of service failures.
*   C) Both approaches are wrong — neither SLAs nor XLAs should be used without management approval.
*   D) The choice depends entirely on whether the customer prefers technical or experiential reporting.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* XLA measurements like NPS and CES reveal that experience is suffering but do not identify which service component or metric is the cause. Technical SLA data (availability, response time, resolution time) provides the diagnostic granularity needed to investigate and fix underlying problems.
    *   *Why A is incorrect:* ITIL 4 recommends XLAs as a complement to SLAs, not a replacement. Eliminating technical SLA measurement removes essential diagnostic visibility.
    *   *Why C is incorrect:* Both SLAs and XLAs are ITIL 4-endorsed tools for managing service quality. There is no indication that management approval is the deciding factor.
    *   *Why D is incorrect:* While customer preferences matter in reporting design, the technical need for diagnostic data exists regardless of preference.

---

**Question 18 (5 points)**
A logistics company's IT department commits in its SLA to restore the warehouse management system within 4 hours of a P1 incident. The database team's OLA commits to providing a restored database within 2 hours of receiving an escalation. The server team has no formal OLA. In a P1 incident, the server team takes 3 hours to respond, leaving only 1 hour in the SLA window. What does this scenario demonstrate?
*   A) The OLA for the database team is set too tight.
*   B) The absence of a server team OLA allowed an uncontrolled dependency to break the SLA delivery chain.
*   C) The SLA target of 4 hours is too aggressive for this type of incident.
*   D) The incident should have been escalated to the UC vendor instead.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* Without a formal OLA, the server team had no committed response time and no accountability within the SLA delivery chain. ITIL 4 requires that all internal dependencies supporting an SLA be covered by OLAs with targets that support the overall SLA commitment.
    *   *Why A is incorrect:* The database team's OLA is not the cause of the failure — the missing server team OLA is.
    *   *Why C is incorrect:* A 4-hour P1 SLA is reasonable for a warehouse management system. The failure is a structural governance gap, not an unrealistic target.
    *   *Why D is incorrect:* There is no indication a UC vendor is involved in this scenario. The failure is internal — a missing OLA with the server team.

---

**Question 19 (5 points)**
According to ITIL 4, what is the primary goal of a service review meeting between the IT provider and the customer?
*   A) To negotiate new contract terms and adjust SLA penalty clauses
*   B) To review service performance, discuss any issues, and collaboratively agree on improvement actions
*   C) To present financial invoices and usage reports to the customer
*   D) To train the customer's staff on how to use the IT service correctly

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines service review meetings as structured governance interactions between the provider and customer to review performance, address concerns, and agree on improvement directions. They are relationship and performance management activities.
    *   *Why A is incorrect:* Contract renegotiation may occasionally arise from service review findings, but it is not the primary goal of the meeting. Service reviews are performance governance activities.
    *   *Why C is incorrect:* Financial invoicing is an account management or vendor management function, not the purpose of a service review meeting.
    *   *Why D is incorrect:* Customer training is an adoption enablement activity, not the purpose of a periodic service review meeting.

---

**Question 20 (5 points)**
An IT organization is designing its SLM practice from scratch. The team lead asks: "Who should we engage when determining what the SLA targets should be?" Which answer is most aligned with ITIL 4 SLM guidance?
*   A) Only the IT service manager and the CIO — business stakeholders lack the technical knowledge to contribute meaningfully to SLA design.
*   B) Only the customer's procurement team — they represent the business in all contract negotiations.
*   C) A broad group including business stakeholders, IT operations staff, service desk representatives, and where applicable, key suppliers — to ensure targets are realistic, meaningful, and supported end-to-end.
*   D) Only external ITIL consultants — they are best positioned to set industry-standard targets without internal bias.

*   **Correct Answer:** C
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 SLM requires broad stakeholder engagement in SLA design. Business stakeholders define what matters; IT operations confirms what is achievable; service desk contributes user-facing perspective; suppliers confirm what underpinning commitments are feasible. Only this multi-party engagement produces an SLA that is both meaningful and deliverable.
    *   *Why A is incorrect:* Excluding business stakeholders from SLA design is the primary cause of watermelon SLAs — targets that measure IT convenience rather than business value.
    *   *Why B is incorrect:* Procurement teams handle contractual terms; they are not the right source for determining what service levels matter to end users and operational teams.
    *   *Why D is incorrect:* External consultants can provide benchmarks and guidance, but only internal and customer stakeholders can define what is meaningful and achievable in the organization's specific context.

# Quiz: Module 02 - Rules of Engagement and Legal Considerations
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What must a penetration tester secure before executing any port scanning or exploit tools against a client network?
*   A) Public IP certificate
*   B) Written authorization from key stakeholders
*   C) Insurance coverage
*   D) A server license
*   **Correct Answer:** B) Without written, authorized consent, performing scanning or exploits is considered illegal hacking.
*   **Distractor Analysis:**
    *   *Why correct:* Without written, authorized consent, performing scanning or exploits is considered illegal hacking. Authorization is legally required.
    *   *Why A is incorrect:* A public IP certificate does not grant any legal authorization to test systems — it is not a recognized pre-engagement document.
    *   *Why C is incorrect:* While professional liability insurance is a best practice for testing firms, it does not substitute for written client authorization.
    *   *Why D is incorrect:* Server licenses govern software use rights, not the legal authorization to perform security testing against systems.

---

**Question 2**
In penetration testing, which of the following best defines a **regulatory compliance framework** such as PCI-DSS?
*   A) A set of industry-specific security standards and requirements that organizations must meet, often mandating regular penetration testing and security assessments as part of ongoing compliance obligations.
*   B) A cryptographic protocol that uses asymmetric key pairs to encrypt data in transit between a client and server, protecting confidentiality.
*   C) A software development methodology that breaks work into short sprints and uses daily standups to coordinate team tasks.
*   D) A network segmentation model where each layer of the architecture is isolated from others to prevent lateral movement between zones.
*   **Correct Answer:** A) A set of industry-specific security standards and requirements that organizations must meet, often mandating regular penetration testing and security assessments as part of ongoing compliance obligations.
*   **Distractor Analysis:**
    *   *Why A is correct:* PCI-DSS, HIPAA, SOX, and similar frameworks define mandatory security controls and assessment requirements. For example, PCI-DSS Requirement 11 specifically mandates annual external penetration testing for cardholder data environments.
    *   *Why B is incorrect:* This describes TLS/SSL encryption protocols, which are a technical control — not a compliance framework that mandates security assessments.
    *   *Why C is incorrect:* This describes Agile software development methodology, which is unrelated to security compliance frameworks.
    *   *Why D is incorrect:* This describes a network architecture concept (defense in depth / DMZ segmentation), not a compliance framework.

---

**Question 3**
A penetration tester's client has their web application hosted on AWS. The tester's Rules of Engagement authorize testing the application. Before beginning, what additional step is required?
*   A) No additional steps — the client authorization covers all infrastructure including cloud hosting.
*   B) Notify the client's IT department so they can monitor for alerts during testing.
*   C) Obtain separate permission from AWS using their vulnerability reporting or penetration testing request process.
*   D) Run only passive reconnaissance against the application since active testing of cloud systems is never permitted.
*   **Correct Answer:** C) Obtain separate permission from AWS using their vulnerability reporting or penetration testing request process.
*   **Distractor Analysis:**
    *   *Why C is correct:* Cloud service providers (AWS, Azure, GCP) own the underlying infrastructure and have their own acceptable use policies. Testing cloud-hosted systems without CSP notification or approval may violate their terms of service and potentially trigger their incident response teams.
    *   *Why A is incorrect:* Client authorization covers their application and data, but does not extend to the physical and virtual infrastructure owned and operated by the cloud provider.
    *   *Why B is incorrect:* Notifying the IT department is good practice for coordination but does not constitute legal authorization from the cloud provider.
    *   *Why D is incorrect:* Active testing of cloud-hosted applications is permitted, but it requires proper authorization from both the client and the cloud provider first.

---

**Question 4**
During a penetration test, a tester accidentally takes down a production web server that was in scope. What is the correct immediate action?
*   A) Attempt to restore the server using the exploited access and document the recovery steps.
*   B) Continue testing other in-scope systems and report the outage in the final report.
*   C) Immediately stop testing, notify the client's designated emergency contact as specified in the RoE, and document the incident.
*   D) Quietly move on — unintended outages are expected and covered by the liability clause in the MSA.
*   **Correct Answer:** C) Immediately stop testing, notify the client's designated emergency contact as specified in the RoE, and document the incident.
*   **Distractor Analysis:**
    *   *Why C is correct:* The RoE always specifies an emergency contact and escalation procedure for unintended outages. Immediate notification is a professional and contractual obligation. Failing to notify promptly can compound damages and destroy client trust.
    *   *Why A is incorrect:* Attempting self-recovery using exploited access could make the situation worse and create additional unauthorized changes. The client's operations team is better positioned to restore their own systems.
    *   *Why B is incorrect:* Continuing to test after causing a service disruption without notifying the client is a serious breach of professional conduct and contractual obligation.
    *   *Why D is incorrect:* Liability clauses typically require the tester to have acted within scope and with due care. Concealing an incident would likely void those protections and expose the tester to greater liability.

---

**Question 5**
Which document in a penetration testing engagement specifically limits what proprietary business information, network diagrams, and vulnerability findings can be shared outside the testing team?
*   A) Rules of Engagement (RoE)
*   B) Statement of Work (SOW)
*   C) Non-Disclosure Agreement (NDA)
*   D) System Security Plan (SSP)
*   **Correct Answer:** C) Non-Disclosure Agreement (NDA)
*   **Distractor Analysis:**
    *   *Why C is correct:* The NDA is a legally binding contract that restricts the tester from disclosing confidential information obtained during the engagement — including network architecture, discovered vulnerabilities, and business data — to unauthorized parties.
    *   *Why A is incorrect:* The RoE defines testing boundaries, permitted methods, and targets. It governs what the tester may do, not what information may be shared externally.
    *   *Why B is incorrect:* The SOW defines project scope, deliverables, timeline, and pricing. It is a commercial agreement, not a confidentiality instrument.
    *   *Why D is incorrect:* A System Security Plan documents an organization's security posture and controls (used in FedRAMP/FISMA contexts). It is produced by the system owner, not part of the penetration testing contract.

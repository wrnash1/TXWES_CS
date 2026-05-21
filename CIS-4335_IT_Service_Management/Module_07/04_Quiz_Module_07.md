# Quiz: Module 07 - Technical Management Practices - Change Enablement
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the Change Enablement practice in ITIL 4?
*   A) To deploy all approved changes into the live environment as quickly as possible without disrupting services.
*   B) To maximize the number of successful IT and service changes by ensuring risks are properly assessed, authorizing changes to proceed, and managing the change schedule.
*   C) To document all configuration items and maintain an accurate record of the current state of the IT infrastructure.
*   D) To restore service as quickly as possible following a disruption caused by an unauthorized change.
*   **Correct Answer:** B) The purpose of Change Enablement is to maximize successful changes through risk assessment, authorization, and schedule management.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of Change Enablement as maximizing the number of successful changes by ensuring that risks are properly assessed, authorizing changes to proceed, and managing the change schedule. This focuses on governance of change, not execution.
    *   *Why A is incorrect:* Deploying changes into the live environment is the responsibility of Deployment Management, not Change Enablement. Change Enablement authorizes; Deployment Management executes.
    *   *Why C is incorrect:* Documenting configuration items and maintaining infrastructure records is the purpose of Service Configuration Management, not Change Enablement.
    *   *Why D is incorrect:* Restoring service after a disruption is the purpose of Incident Management. Change Enablement is a preventive governance practice, not a reactive recovery practice.

---

**Question 2**
Which of the following most accurately describes a standard change in ITIL 4?
*   A) A change that requires a full risk assessment and approval from the Change Advisory Board before it can be implemented.
*   B) A change that must be implemented immediately to resolve a critical service failure, bypassing the normal authorization process.
*   C) A pre-authorized, low-risk, well-understood change that follows a documented procedure and does not require individual review each time it is performed.
*   D) A change initiated by a customer request that must be tracked through the service request management process before authorization.
*   **Correct Answer:** C) A standard change is pre-authorized, low-risk, well-understood, and follows a documented procedure without requiring individual review.
*   **Distractor Analysis:**
    *   *Why C is correct:* Standard changes are pre-authorized because the risk and the steps required have already been assessed and approved. Each individual occurrence does not require a new risk assessment or change authority review. Examples include routine password resets, user account provisioning, or applying pre-tested security patches.
    *   *Why A is incorrect:* That describes a normal change — one that requires individual risk assessment and authorization before implementation. Standard changes are already pre-authorized.
    *   *Why B is incorrect:* That describes an emergency change, which is implemented rapidly to address a critical failure. Emergency changes still require authorization, even if the process is expedited.
    *   *Why D is incorrect:* Customer-initiated requests for standard service actions are handled through Service Request Management. While there is overlap in low-risk activities, the definition given does not match standard change.

---

**Question 3**
A company is planning to upgrade the operating system on all 200 of its production servers. The change has never been performed at this scale before, carries significant risk of service disruption, and will affect multiple business units. Which change type applies, and what authorization process should be followed?
*   A) Standard change — the change is routine and can proceed using the pre-authorization already in place for OS updates.
*   B) Emergency change — the urgency of keeping all servers on a supported OS version means it must be fast-tracked through an Emergency CAB.
*   C) Normal change — the change requires individual risk assessment and should be reviewed by the appropriate change authority, likely including CAB advisory input given the risk and impact.
*   D) Normal change — the change is automatically approved once the service owner submits it, since OS upgrades are a standard IT activity.
*   **Correct Answer:** C) This is a normal change requiring individual risk assessment and change authority review, with CAB advisory input appropriate given its scale and risk.
*   **Distractor Analysis:**
    *   *Why C is correct:* A large-scale, high-risk change that has not been pre-authorized and affects multiple business units is a normal change. Normal changes require individual risk assessment and authorization from the appropriate change authority. Given the scale and risk, CAB advisory review is appropriate to inform the authorization decision.
    *   *Why A is incorrect:* Standard changes are pre-authorized for well-understood, low-risk activities performed routinely. A 200-server OS upgrade at an unprecedented scale does not meet these criteria.
    *   *Why B is incorrect:* Emergency changes are reserved for changes needed to resolve a major incident or prevent an imminent critical failure. Proactive, planned upgrades do not qualify as emergencies.
    *   *Why D is incorrect:* Normal changes are never automatically approved simply because the service owner submits them. They require assessment and authorization by the appropriate change authority.

---

**Question 4**
What is the role of the Change Advisory Board (CAB) in ITIL 4?
*   A) The CAB holds final authorization authority over all normal changes and must approve every change before it can proceed.
*   B) The CAB is responsible for deploying approved changes into the live environment and verifying that the changes succeeded.
*   C) The CAB provides advisory support to the change authority by reviewing and making recommendations on high-risk or high-impact normal changes.
*   D) The CAB manages the change schedule and ensures that no two changes are implemented during the same maintenance window.
*   **Correct Answer:** C) The CAB provides advisory support to the change authority — it reviews and recommends, but does not itself authorize changes.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 defines the CAB as an advisory body. It reviews high-risk or high-impact normal changes, discusses potential risks, and makes recommendations to the change authority. The change authority — which may be an individual or a group — holds the actual authorization power.
    *   *Why A is incorrect:* The CAB does not hold authorization authority. This is the most common exam trap related to the CAB. The change authority authorizes; the CAB advises.
    *   *Why B is incorrect:* Deploying and verifying changes in the live environment is the responsibility of Deployment Management, not the CAB.
    *   *Why D is incorrect:* Managing the change schedule is an activity within Change Enablement broadly, but it is not the defined role of the CAB specifically.

---

**Question 5**
An IT team needs to apply an emergency security patch to a critical production server after a zero-day vulnerability is actively being exploited. There is no time for a standard CAB review cycle. Which of the following best describes the correct approach under ITIL 4 Change Enablement?
*   A) Implement the patch immediately without any authorization, then document the change after the fact and notify the change authority.
*   B) Delay the patch until the next scheduled CAB meeting to ensure proper review and authorization.
*   C) Classify the change as an emergency change and obtain expedited authorization from the appropriate authority — such as an Emergency CAB or a senior change authority — before or as close to implementation as possible.
*   D) Classify the change as a standard change since security patching is a routine activity, and apply the pre-existing standard change authorization.
*   **Correct Answer:** C) Emergency changes require expedited — but still present — authorization through an ECAB or senior change authority.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 specifies that emergency changes must still be authorized, even when the process is accelerated. An Emergency CAB or designated senior authority provides expedited authorization. The change should be documented promptly, and a post-implementation review should follow to assess outcomes.
    *   *Why A is incorrect:* Implementing a change without any authorization — even in an emergency — violates Change Enablement principles. ITIL 4 requires that authorization be obtained, though the process is expedited for emergencies.
    *   *Why B is incorrect:* Delaying an emergency patch while active exploitation is occurring would directly harm the organization. Emergency changes exist precisely to avoid this scenario while still maintaining governance.
    *   *Why D is incorrect:* Standard changes are pre-authorized for routine, low-risk activities. A zero-day patch response to active exploitation is not a routine activity and does not qualify for standard change pre-authorization.

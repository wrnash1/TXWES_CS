# Quiz: Module 09 - Service Management Practices - Problem Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the Problem Management practice in ITIL 4?
*   A) To restore normal service operation as quickly as possible following an unplanned service disruption.
*   B) To reduce the likelihood and impact of incidents by identifying actual and potential causes of incidents and managing workarounds and known errors.
*   C) To authorize and schedule all changes to IT services and infrastructure to minimize the risk of disruption.
*   D) To fulfill user requests for standard services, such as password resets and software installations, within agreed timeframes.
*   **Correct Answer:** B) The purpose of Problem Management is to reduce the likelihood and impact of incidents by identifying causes and managing workarounds and known errors.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of Problem Management as reducing the likelihood and impact of incidents by identifying their actual and potential causes, and by managing workarounds and known errors. Unlike Incident Management, Problem Management focuses on prevention and root cause, not immediate restoration.
    *   *Why A is incorrect:* Restoring normal service operation as quickly as possible is the purpose of Incident Management, not Problem Management. Problem Management addresses underlying causes after or in parallel with restoration.
    *   *Why C is incorrect:* Authorizing and scheduling changes is the purpose of Change Enablement. Problem Management may raise change requests when a fix requires a change, but it does not authorize or schedule those changes.
    *   *Why D is incorrect:* Fulfilling user requests for standard services is the purpose of Service Request Management. These are planned, expected activities — not problem investigations.

---

**Question 2**
Which of the following most accurately describes a known error in ITIL 4?
*   A) An incident that has been escalated to a senior technical team because first-line support was unable to restore service.
*   B) A service disruption caused by a configuration error that was introduced during a recent change to the infrastructure.
*   C) A problem that has been analyzed and for which the root cause is understood, but for which a permanent resolution has not yet been implemented.
*   D) A risk identified during proactive problem analysis that has not yet caused any incidents.
*   **Correct Answer:** C) A known error is a problem whose root cause is understood but for which no permanent fix has yet been applied.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 defines a known error as a problem that has been analyzed and has a documented root cause and workaround, but has not yet been permanently resolved. Known errors are recorded in the Known Error Database so service desk staff can apply workarounds efficiently without re-diagnosing the same issue.
    *   *Why A is incorrect:* An escalated incident is still an incident — it describes a service disruption being handled through Incident Management. Escalation does not transform an incident into a known error.
    *   *Why B is incorrect:* A service disruption caused by a recent change is an incident (and possibly a problem to be investigated). It becomes a known error only after root cause analysis has been completed and the cause is documented.
    *   *Why D is incorrect:* That describes a potential problem identified through proactive Problem Management — a risk or vulnerability, not a known error. A known error requires that root cause analysis has already been completed.

---

**Question 3**
The service desk has received 47 tickets over the past month reporting that users are intermittently unable to connect to the corporate VPN. Each incident is resolved by restarting the user's VPN client — but the problem keeps recurring. What should the organization do next, and why?
*   A) Continue resolving each incident individually with the restart workaround, since the incidents are being resolved within SLA targets.
*   B) Raise a problem record to investigate the root cause of the recurring VPN failures and create a known error record with the documented workaround.
*   C) Classify the issue as a major incident and convene an emergency response team to resolve it immediately.
*   D) Submit a change request to replace the VPN system entirely, since repeated incidents indicate the technology is not fit for purpose.
*   **Correct Answer:** B) Recurring incidents with a common pattern should trigger a problem record to investigate root cause and formally document the workaround as a known error.
*   **Distractor Analysis:**
    *   *Why B is correct:* Forty-seven recurring incidents with the same symptom and the same workaround is exactly the scenario that triggers Problem Management. A problem record should be raised to investigate the underlying cause (why does restarting the client fix it?). In the meantime, the restart workaround should be formally documented as a known error in the KEDB so service desk staff can apply it efficiently without re-diagnosing each time.
    *   *Why A is incorrect:* Meeting SLA targets on individual incidents does not mean the problem is being managed. Without a problem record, the organization is spending ongoing effort resolving the same issue repeatedly and the root cause remains unaddressed.
    *   *Why C is incorrect:* A major incident requires a significant, immediate business impact. Forty-seven individual VPN incidents resolved within SLA do not constitute a single major incident requiring emergency response.
    *   *Why D is incorrect:* Replacing the entire VPN system is a significant, costly change that would not be justified without first completing root cause analysis. Root cause may reveal a simple configuration issue, software bug, or network setting — not a need for full replacement.

---

**Question 4**
A problem investigation has identified that a memory leak in a third-party application is the root cause of recurring server crashes. The vendor has acknowledged the defect but a patch will not be available for 60 days. The organization documents a workaround — restarting the affected service weekly — which prevents crashes. What is the correct status of this issue according to ITIL 4 Problem Management?
*   A) The problem is closed because a workaround has been implemented and service is stable.
*   B) The problem is closed because root cause has been identified and documented.
*   C) The issue is now a known error — root cause is understood, a workaround is in place, and error control manages it until the vendor patch is applied.
*   D) The issue remains an open incident because the server crashes have not been permanently resolved.
*   **Correct Answer:** C) With root cause understood and a workaround in place but no permanent fix yet, this is a known error managed through error control.
*   **Distractor Analysis:**
    *   *Why C is correct:* Once root cause analysis is complete and the cause is documented, a problem transitions to known error status. The workaround is documented in the KEDB, and error control monitors the situation until the permanent fix (the vendor patch) is implemented. The problem/known error record remains open during this period.
    *   *Why A is incorrect:* A workaround restores service but does not permanently resolve the underlying cause. The problem record — now a known error record — remains open until the permanent fix is applied.
    *   *Why B is incorrect:* Identifying and documenting root cause moves the issue from problem to known error status — it does not close it. The record stays open until the permanent resolution is implemented.
    *   *Why D is incorrect:* Individual incidents caused by the crashes may be closed once the workaround stabilizes service. But the underlying problem/known error is distinct from those individual incidents and remains open under Problem Management.

---

**Question 5**
Which of the following correctly describes the relationship between Problem Management and Change Enablement in ITIL 4?
*   A) Problem Management and Change Enablement are independent practices that never interact — changes are initiated only by project teams, not by problem investigations.
*   B) When Problem Management identifies a permanent fix that requires a change to infrastructure or services, it raises a change request that is authorized and managed through Change Enablement.
*   C) Problem Management has its own change authority and can authorize infrastructure changes directly without involving Change Enablement.
*   D) Change Enablement triggers Problem Management by raising a problem record every time a change causes an incident in the live environment.
*   **Correct Answer:** B) Problem Management raises change requests for permanent fixes, which are then authorized and managed through Change Enablement.
*   **Distractor Analysis:**
    *   *Why B is correct:* When Problem Management determines that a permanent fix requires a change to the infrastructure, application, or service, it raises a change request. That request is then assessed, authorized, and managed through Change Enablement. Problem Management identifies what needs to change; Change Enablement governs how and when that change occurs.
    *   *Why A is incorrect:* Problem Management and Change Enablement interact regularly. Root cause fixes frequently require changes to infrastructure, configuration, or software — making the handoff from Problem Management to Change Enablement a standard workflow.
    *   *Why C is incorrect:* Problem Management does not hold change authority. Authorization of changes — including those raised to fix known errors — belongs to Change Enablement and the designated change authority.
    *   *Why D is incorrect:* While Change Enablement does consider incident and problem data (for example, when assessing risk of a change), it does not automatically raise problem records. Changes that cause incidents may trigger reactive Problem Management, but this is not described as Change Enablement triggering Problem Management.

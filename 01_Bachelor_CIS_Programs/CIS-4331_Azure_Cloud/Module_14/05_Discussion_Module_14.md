# Discussion Forum: Module 14 — Azure Cost Management and Pricing

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Instructions

Read all three scenarios below. Choose ONE scenario to respond to in your initial post. Your initial post must be 175–225 words and address all the prompt questions for your chosen scenario. Then write two peer responses of 75–100 words each, engaging substantively with classmates who responded to any scenario.

**Due dates:** Initial post due by Day 3 of the module week. Peer responses due by Day 7.

---

## Scenario A — The Forgotten Dev Environment

A mid-size financial services firm onboarded 15 developers to Azure over six months. Each developer was given their own virtual machine for local testing. No budget alerts were configured. At the end of month five, the cloud administrator noticed the monthly Azure bill had grown to $4,200 — nearly double the projected $2,200. Investigation revealed that 12 of the 15 developer VMs had been running 24 hours a day, 7 days a week, including nights, weekends, and a two-week holiday shutdown when no one was in the office.

**Respond to the following:**

- Which specific Azure cost management features could have prevented or detected this situation before the bill doubled?
- What configuration changes would you implement immediately after discovering the problem?
- If you were presenting this situation to the VP of Technology, how would you frame the recommended solution to get approval for the configuration changes?

**Consider:** budget alerts, auto-shutdown, Dev/Test pricing, Azure Advisor, and tagging strategies in your response.

---

## Scenario B — The Migration Business Case

A regional hospital network operates 60 on-premises servers across three facilities in Texas. The IT director has been asked by the CFO to determine whether migrating to Azure would save money. The on-premises environment includes aging hardware (average 5 years old), high electricity costs due to hospital-grade power redundancy requirements, and an IT staff of 8 people who spend approximately 40% of their time on infrastructure maintenance. The CFO wants a three-year cost comparison.

**Respond to the following:**

- Which Azure tool is designed specifically to address the CFO's request, and what information would you need to gather before using it?
- The TCO Calculator includes an "Adjust Assumptions" step. Name two assumptions that would be especially important to customize for a hospital environment and explain why.
- Beyond the dollar savings shown in the calculator output, what non-financial benefits of cloud migration might be relevant for a hospital network specifically?

**Consider:** TCO Calculator inputs, data center overhead, IT labor costs, compliance implications, and disaster recovery in your response.

---

## Scenario C — Optimizing a Production Workload

A logistics company runs a fleet of 40 Azure virtual machines supporting a real-time shipment tracking platform. The VMs have been running on pay-as-you-go pricing for 18 months. Azure Advisor is showing a recommendation to purchase reserved instances and is also flagging 8 VMs as underutilized (average CPU below 6%). The company's cloud spend is currently $18,000/month. The CTO wants to reduce the bill by at least 30% without degrading application performance.

**Respond to the following:**

- Prioritize the two cost optimization actions you would take first and explain your reasoning.
- For the 8 underutilized VMs flagged by Advisor, what additional information would you gather before resizing them, and who would you involve in that decision?
- After implementing reserved instances and right-sizing, what ongoing practices would you put in place to prevent costs from drifting upward again over the next 12 months?

**Consider:** reserved instances, right-sizing, Azure Advisor, budget alerts, and cost governance in your response.

---

## Peer Response Guidelines

Your peer responses should do at least two of the following:

- Build on a point your classmate made with additional detail or a real-world example
- Respectfully challenge an assumption or recommendation and offer an alternative perspective
- Connect the scenario to concepts from a different module in this course
- Ask a clarifying question that would deepen the analysis

Responses that only say "great post" or restate the classmate's points without adding new analysis will not receive full credit.

---

## Grading Rubric — 10 Points Total

| Criteria | Points |
|---|---|
| Initial post addresses all prompt questions for the chosen scenario | 3 |
| Initial post demonstrates accurate understanding of Azure cost tools | 2 |
| Initial post is 175–225 words (penalty for significant deviation) | 1 |
| Peer response 1 adds substantive analysis or perspective | 2 |
| Peer response 2 adds substantive analysis or perspective | 2 |
| **Total** | **10** |

---

## Example Starter Phrases

To help you open your initial post with substance rather than filler:

- "In Scenario [X], the core issue is not just overspending — it is a governance gap in..."
- "The most important first action in this scenario is [specific tool/feature] because..."
- "Before presenting to the [CFO/CTO/VP], I would quantify the impact by..."
- "Azure Advisor flagging those VMs as underutilized is a useful starting point, but before acting I would want to know..."

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 14 Discussion*

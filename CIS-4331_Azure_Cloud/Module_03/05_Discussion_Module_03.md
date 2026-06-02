# Discussion Forum: Module 03 - Azure Virtual Machines and Scale Sets

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

This discussion asks you to apply Azure VM and Scale Set concepts to real infrastructure decisions. Choosing the right compute approach — VM size, availability configuration, and scaling strategy — has direct consequences for application reliability, cost, and operational complexity. These are the decisions cloud architects and DevOps engineers make routinely.

Read all three scenarios. Choose **one scenario** for your initial post. Identify your scenario at the start of your post.

---

## Scenario A: The Legacy Application Migration

Contoso Insurance is migrating a policy management system from on-premises servers to Azure. The application runs on Windows Server 2019, requires a proprietary network driver that must be installed at the OS level, and uses a third-party database engine that cannot be moved to a managed PaaS database service. The current on-premises server has 16 CPU cores and 64 GB RAM and handles approximately 500 concurrent users during business hours (8 AM to 6 PM Monday through Friday). Outside business hours, usage drops to near zero. The migration team is debating between two configurations: (1) a single large VM running 24/7, or (2) a VM Scale Set that scales between 1 and 4 instances based on CPU load.

In 175-225 words, address all of the following:

- The application requires a proprietary OS-level network driver. Which Azure compute service model (IaaS, PaaS, or SaaS) is required, and why? Could Azure App Service be used instead?
- Evaluate the two proposed configurations. Which better aligns with Azure's OPEX cost model, and which better handles the 8-to-6 usage pattern? What is the key risk in the single-large-VM approach that the Scale Set approach mitigates?
- The migration team wants a 99.99% SLA for this system. What Availability Zone configuration is required? How many VM instances must be running at minimum to achieve this SLA?

---

## Scenario B: The Student Developer Environment

Texas Wesleyan's Computer Science department (fictional scenario) wants to provide each of 120 CS students with a personal Azure development VM for the semester. The VMs will be used during class hours (MWF 9-11 AM, TR 2-4 PM) and for homework during evenings and weekends. Usage is genuinely unpredictable — some students work intensively for 8-hour sessions; others check in for 20 minutes. The IT administrator has a fixed budget of $8 per student per month. The VMs need to run Visual Studio Code, a Python environment, and occasionally compile small C++ programs. Each VM needs to be independently managed by the student.

In 175-225 words, address all of the following:

- Which VM size family and specific size recommendation would you make to stay within the $8/month budget while providing adequate performance? Use the reading guide's cost and family information to support your recommendation. Remember that students must deallocate VMs when not in use.
- A VM Scale Set would automate instance management, but is a Scale Set the right tool here? Explain why individual VMs are more appropriate than a Scale Set for this use case.
- The IT administrator is concerned that students will forget to deallocate their VMs overnight. Identify one Azure tool or approach (not covered in detail until Module 12/13 but researchable) that could automatically deallocate VMs at a scheduled time each day. Name the tool and describe what it does in one sentence.

---

## Scenario C: The Event-Driven Scaling Challenge

GameSphere is a browser-based gaming platform that hosts tournament events on weekend evenings. During normal weekday hours, the platform serves 2,000 concurrent players and runs comfortably on 4 VM instances in a Scale Set. On tournament evenings (Saturday 7 PM - 11 PM), player count surges to 25,000. The current Scale Set is configured with maximum 10 instances, and the scale-out rule adds 2 instances when CPU exceeds 70% for 5 minutes. The operations team has observed that during tournament launches, the CPU spikes to 95% across all instances simultaneously, and the 10-instance maximum is reached within 15 minutes. However, the scaling is reactive — by the time 10 instances are running, the first 10 minutes of the tournament have already experienced degraded performance.

In 175-225 words, address all of the following:

- The current reactive autoscale approach is causing performance problems at tournament launch. What Scale Set scaling mode (other than metric-based reactive autoscale) would prevent this problem? Describe exactly how you would configure it for the Saturday evening tournament pattern.
- The team also wants to increase the maximum instance count. The tournament needs to handle 25,000 concurrent players. If each instance handles approximately 2,500 players at 70% CPU, how many instances do you need at maximum? Should the minimum instance count change?
- After the tournament ends at 11 PM, the Scale Set needs to scale back in efficiently. What cool-down and scale-in rule configuration would you recommend to bring the instance count down from peak to normal within 30-40 minutes without over-scaling?

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Scenario identified at start. All three sub-questions addressed with technical accuracy. Uses Module 03 vocabulary (VM families, availability options, Scale Set terms). Word count 175-225. Demonstrates original reasoning. |
| 3-4 pts | Most sub-questions addressed. Minor technical gaps. Slightly outside word count. |
| 1-2 pts | Incomplete response or significant technical errors. |
| 0 pts | No initial post by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive responses to two classmates. Each response is 75+ words with technical content: challenge a sizing recommendation, propose an alternative availability strategy, add a cost calculation, or identify a constraint the original poster missed. |
| 2-3 pts | Two responses but one or both lack technical depth. |
| 1 pt | One response or superficial comments only. |
| 0 pts | No peer responses by Sunday deadline. |

---

## Professor Nash's Note

The cost optimization aspects of this module — particularly the stop vs. deallocate distinction — are not just exam content. I have seen teams lose thousands of dollars in cloud budget because a developer stopped a fleet of VMs at the end of the day without deallocating them. By the end of this course, I want every one of you to have the reflexive habit of deallocating (not just stopping) VMs you are not actively using. The Azure Portal's "Stop" button deallocates. The guest OS shutdown command does not. Know the difference and make it a professional habit.

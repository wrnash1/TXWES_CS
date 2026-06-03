# Discussion Forum: Module 15 — Automation and Programmability

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Overview

This discussion forum asks you to apply Module 15 automation and programmability concepts to realistic professional scenarios. Choose one of the three scenarios below, write an original post of 175–225 words, and respond substantively to at least one classmate's post on a different scenario.

---

## Scenario 1: Making the Case for Network Automation

A senior network engineer at a regional bank is preparing a business case to convince the CIO to invest in network automation tools, specifically Ansible and Cisco DNA Center. The bank has 12 branches, each with 3–5 Cisco switches and 2 routers, managed entirely by hand through CLI. The last major change — a VLAN reconfiguration — took the team of four engineers two weeks and introduced three outages due to configuration errors.

In your post, address the following:

* What is the most compelling technical argument for automation in this scenario?
* How does Ansible's idempotency feature directly address the risk of configuration errors in this bank scenario?
* What is the role of DNA Center's northbound API versus its southbound API in this deployment?
* What risks or challenges might the engineering team face when transitioning from manual CLI management to automation?

Think about both the immediate technical benefits and the organizational change management required to move an entire team from CLI-first to automation-first thinking.

---

## Scenario 2: Choosing Between NETCONF and RESTCONF

A network architect at a healthcare organization is designing a new automation platform for 300 Cisco IOS-XE switches. The team is debating whether to use NETCONF with XML or RESTCONF with JSON as the primary configuration protocol. The development team argues that REST/JSON is far easier to work with in Python. The operations team argues that NETCONF's transactional commit model is essential for their strict change management process, where a failed partial configuration is never acceptable.

In your post, address the following:

* What is the key technical difference between NETCONF's commit model and traditional CLI configuration?
* Why does the operations team's concern about partial configurations favor NETCONF over CLI?
* Can RESTCONF also provide transactional safety, and if so, how?
* If you were the architect, which protocol would you recommend and why?

Consider the healthcare organization's regulatory environment (HIPAA) and the risk of a misconfigured network segment exposing patient data.

---

## Scenario 3: Ansible vs. Puppet for a University Network

A university network team is selecting a configuration management tool to automate policy enforcement across 400 Cisco switches distributed across 20 campus buildings. The team is evaluating Ansible and Puppet. The IT department also manages several hundred Linux servers and wants a single tool that works for both network devices and servers. A junior engineer advocates for Ansible because he has already written several playbooks. A senior administrator prefers Puppet because the university already runs a Puppet master for its Linux infrastructure.

In your post, address the following:

* What is the fundamental architectural difference between Ansible and Puppet that most affects this decision?
* Why does the agent-based model of Puppet create a practical challenge for network switches specifically?
* Is it possible to use both tools in the same environment? Describe a scenario where this makes sense.
* What would you recommend and how would you justify your recommendation to the senior administrator?

Consider the total cost of ownership — including the effort to install and maintain agents on 400 switches versus managing an Ansible control node.

---

## Peer Response Guidelines

When responding to a classmate's post:

* Engage with their specific recommendation — do not simply restate the scenario.
* Add a technical detail, counterargument, or real-world example they did not mention.
* Keep your response between 75 and 125 words.
* Be professional and constructive.

---

## Grading Rubric

| Criterion | Points | Description |
|---|---|---|
| Technical accuracy | 4 | Automation concepts applied correctly; tools and protocols cited accurately |
| Depth of analysis | 3 | All prompt questions addressed; reasoning is clear and specific |
| Original post length | 1 | 175–225 words (verified by word count) |
| Peer response | 2 | Substantive reply to a classmate on a different scenario; adds new insight |
| **Total** | **10** | |

---

## Submission Deadline

Initial post due by 11:59 PM on the Wednesday of Module 15 week. Peer response due by 11:59 PM on Sunday of the same week.

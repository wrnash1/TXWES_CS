# Discussion Forum: Module 05 - Azure Virtual Networking

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

Network design in Azure has direct consequences for security, performance, cost, and operational complexity. The decisions you make about VNet structure, NSG rules, and hybrid connectivity define the security posture of your entire cloud environment. This discussion develops network architecture reasoning through three realistic scenarios.

Read all three scenarios. Choose **one scenario** for your initial post. Identify your scenario at the start of your post.

---

## Scenario A: The Three-Tier Web Application

Adatum Healthcare is deploying a patient-facing web application on Azure. The application has three tiers: a web tier (serves the patient portal), an application tier (business logic and API), and a database tier (SQL Server). Security requirements include: the database tier must never be directly reachable from the internet; the application tier must only be reachable from the web tier, not directly from the internet; only the web tier should have a public IP. All three tiers must communicate with each other. HIPAA compliance requires that all inter-tier communication stays within Azure's private network.

In 175-225 words, address all of the following:

- Design the subnet structure for this application. How many subnets are needed, and what address ranges would you assign to each (use the 10.0.0.0/16 address space)?
- Describe the NSG rules required for the database tier subnet. What inbound traffic should be explicitly allowed? What should be explicitly denied? Include the priority, source, destination, port, and action for at least two custom rules.
- The HIPAA requirement that inter-tier communication stays within Azure's private network is satisfied by default for resources within the same VNet. However, if the database tier needs to call an Azure Storage account for backup, how do you ensure that traffic also stays on the Azure private network?

---

## Scenario B: The Hybrid Cloud Migration

Morrison Manufacturing operates a production facility in San Antonio with an on-premises data center running manufacturing execution systems (MES). They are migrating their ERP system to Azure while keeping the MES on-premises. The ERP on Azure must communicate with the MES on-premises in real time, with latency under 10 milliseconds for transaction synchronization. The ERP also processes large batch reports each night that transfer 500 GB of data from on-premises to Azure. The company's CFO wants the lowest possible monthly cost. The CTO insists on no public internet traversal for any ERP-MES communication.

In 175-225 words, address all of the following:

- The CTO's requirement (no public internet) combined with the real-time latency requirement (under 10 ms) points to a specific connectivity solution. Is VPN Gateway or ExpressRoute more appropriate? Use the Module 05 reading guide comparison table to justify your answer with at least two criteria.
- The CFO's cost concern conflicts with the CTO's ExpressRoute preference (if that is your recommendation). Describe a hybrid approach that could satisfy both: what if VPN Gateway was used for the real-time low-volume synchronization traffic and a different mechanism handled the nightly 500 GB batch transfer?
- The manufacturing data transmitted between the MES and ERP contains proprietary process formulas. ExpressRoute is a private circuit but is not encrypted by default. What additional step would you recommend to address this confidentiality requirement?

---

## Scenario C: The NSG Security Incident

At 2:47 AM on a Tuesday, the security operations center (SOC) at Northgate Financial receives an alert: their Azure VM hosting an internal loan processing application is generating outbound network traffic to an IP address in an unusual geography. Investigation reveals that a developer inadvertently left TCP port 3389 (RDP) open to the internet in an NSG rule to "temporarily" fix a remote access issue three months ago. The VM appears to have been compromised through an RDP brute-force attack. The VM's NSG currently has these inbound rules: Priority 100 - Allow RDP from any source, Priority 200 - Allow HTTPS from any source, Priority 65500 - Deny all.

In 175-225 words, address all of the following:

- Identify the immediate remediation step for the NSG to stop the active compromise from spreading or enabling further access. Write the specific NSG rule change (or new rule) needed, including priority, source, destination port, and action.
- After the immediate fix, describe the correct long-term NSG configuration for secure remote VM administration. What source address restriction should be applied to RDP or SSH access? What is the name of the Azure service that provides browser-based SSH/RDP access without exposing those ports publicly at all?
- This incident started because a developer made a temporary change that became permanent. What governance mechanism (an Azure feature, not a policy) can automatically detect and alert on overly permissive NSG rules that expose management ports to the internet? Name the service and describe what it does in one sentence.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Scenario identified at start. All three sub-questions addressed with accurate networking content. Uses Module 05 vocabulary (NSG, VNet, Service Endpoint, ExpressRoute, VPN Gateway). Word count 175-225. Demonstrates original design reasoning. |
| 3-4 pts | Most sub-questions addressed. Minor technical inaccuracies. |
| 1-2 pts | Incomplete or significant technical errors. |
| 0 pts | No initial post by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive responses to two classmates. Each response is 75+ words with specific technical feedback: challenge a subnet design choice, propose a different NSG rule, question a connectivity recommendation, or add a compliance consideration. |
| 2-3 pts | Two responses submitted but lacking technical depth. |
| 1 pt | One response or superficial comments only. |
| 0 pts | No peer responses by Sunday deadline. |

---

## Professor Nash's Note

The Scenario C incident is based on a class of real-world Azure security incidents. Leaving RDP open to the internet — even "temporarily" — is one of the most common initial access vectors for cloud breaches. Microsoft Defender for Cloud flags exactly this type of configuration. In your career, you will encounter developers and administrators who make temporary network exceptions for convenience. Part of your role as a cloud professional is to build processes (NSG review cycles, Defender for Cloud alerts, Azure Policy) that catch these exceptions before they become incidents. Network security hygiene is not glamorous, but it prevents breaches.

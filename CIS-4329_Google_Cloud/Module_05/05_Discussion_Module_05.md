# Discussion — Module 05

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: VPC Network Design and Hybrid Connectivity

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose any scenario.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The Multi-Tier Production Network

A fintech startup is designing its production GCP environment for a payment processing application. The application has three tiers: a public-facing web API tier that accepts HTTPS traffic from the internet, an internal application tier that the web tier calls but should never be reachable from the internet, and a database tier that only the application tier should be able to reach. All three tiers will run on Compute Engine VMs in the same VPC. The security team requires that the attack surface be minimized at the network level.

In 175–225 words, address the following:

- How would you use network tags and firewall rules to enforce the traffic isolation between the three tiers? Describe each firewall rule needed (direction, protocol/port, source, and target).
- The web tier VMs will receive internet traffic. The database tier VMs should never have external IP addresses. The application tier VMs are internal-only but need to call the BigQuery API. What network configuration addresses each of these requirements?
- A developer asks to add `--no-address` to all VMs for maximum security. What must be configured to allow the web tier to still receive inbound internet traffic?

---

## Scenario B — The Hybrid Cloud Migration

A mid-size manufacturing company is migrating its ERP system to GCP. The ERP system in GCP must communicate with the company's on-premises manufacturing floor systems (factory automation servers, sensor networks) that cannot be moved to the cloud. The on-premises environment is connected via the company's corporate WAN to the company's headquarters data center. The expected data transfer between GCP and on-premises is approximately 800 Mbps at peak. The company's IT team has a limited budget and no existing presence at a Google colocation facility.

In 175–225 words, address the following:

- Which hybrid connectivity option is most appropriate given the bandwidth requirement and budget constraints? Explain your choice and why you did not choose the other option.
- Describe the network-level architecture: what exists on the on-premises side, what GCP resources are needed, and how traffic flows between them.
- The company's security team requires that all data in transit between on-premises and GCP be encrypted. Does your chosen connectivity option provide this by default, or do you need to configure it?

---

## Scenario C — The Multi-Project Network Governance Problem

A large enterprise runs 40 separate GCP projects — one per application team. Each team has its own VPC. Some teams need to share centralized services such as a database cluster, a logging aggregator, and an internal PKI certificate authority, all of which run in a dedicated `shared-services` project. Individual application teams should not be able to modify the network configuration of the shared services, but they must be able to use the shared services over private IP.

In 175–225 words, address the following:

- Compare VPC Peering and Shared VPC as solutions for this architecture. Which is more appropriate given the governance requirements, and why?
- If you chose VPC Peering, explain the scalability problem that arises as the number of projects grows. How many peering connections would you need if all 40 teams also need to peer directly with each other?
- If you chose Shared VPC, describe the IAM roles and project configuration required to grant application teams the ability to deploy VMs in the shared VPC's subnets without giving them control over the VPC itself.

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Identifies a firewall rule gap or security risk in the classmate's tier isolation design
- Points out a bandwidth or cost consideration the classmate overlooked in their hybrid connectivity choice
- Questions whether the classmate's chosen architecture scales to 40 teams and suggests an improvement
- References a specific gcloud command from the lab that would implement part of the classmate's design

Responses that consist only of agreement without substantive technical additions receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions accurately. Uses correct GCP networking terminology (VPC, subnet, firewall rule direction/action/target, VPC peering, Private Google Access). Justifies design choices with reference to security requirements, bandwidth constraints, or governance needs. 175–225 words.
- 3–4 pts: Addresses most sub-questions but uses vague terminology or lacks justification for network design decisions.
- 1–2 pts: Only addresses one sub-question or contains significant factual errors about GCP networking.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each contributing specific technical additions.
- 2 pts: Only one qualifying response, or both are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: VPC network design is one of the most common tasks in real GCP administration, and it is the area where mistakes are most consequential. An overly permissive firewall rule can expose a database to the internet; an overly restrictive one can break inter-tier communication and cause hours of debugging. In your posts, be specific about the direction (ingress vs. egress), the target (which VMs does this rule apply to), and the source or destination (where does the traffic come from or go to). Vague descriptions like "add a firewall rule to allow traffic" will not receive full credit.

---

End of Discussion — Module 05

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

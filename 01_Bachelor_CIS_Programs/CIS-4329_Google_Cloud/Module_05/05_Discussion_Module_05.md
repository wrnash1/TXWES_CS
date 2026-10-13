# Discussion: Module 05 — Virtual Private Cloud Networking

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion asks you to design and analyze real-world GCP network
architectures. Networking decisions have large downstream effects on security,
performance, and cost. The scenarios below reflect the kinds of challenges that
cloud engineers encounter when designing or inheriting network configurations.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — Network Architecture Design (Choose One)

A manufacturing company is migrating to GCP. Their environment includes:

- A production application running on 20 VMs across three tiers: web, app,
  and database
- A development environment for 15 engineers that should be isolated from
  production data
- An on-premises ERP system that the GCP application must communicate with
  over a private connection
- Compliance requirements stating that production database servers must not
  have internet access or external IPs

Design the full network architecture for this environment:

1. Design the VPC and subnet structure. Specify:
   - How many VPCs you would create and why
   - Subnet names, CIDR ranges, and regions for each tier
   - Whether you would use auto-mode or custom-mode and why
2. Design the firewall rules needed. For each rule specify:
   - Direction, action, source/destination, target (tag or SA), and purpose
   - How you would prevent the database VMs from accessing the internet
3. Recommend a hybrid connectivity solution for the on-premises ERP system.
   Specify Cloud VPN or Cloud Interconnect and justify based on the described
   requirements.
4. Describe how Private Google Access would benefit the database VMs given
   the compliance constraint.

---

## Prompt B — Network Security Incident Analysis (Choose One)

During a security review, the following configuration issues were discovered
in a GCP environment:

- The default VPC is in use across all workloads (production, dev, analytics)
- All VMs have external IP addresses
- The `default-allow-ssh` rule allows TCP:22 from 0.0.0.0/0 to all instances
- A developer team was given `roles/compute.networkAdmin` on the project to
  manage their own load balancers; they have since modified production firewall
  rules
- No VPC Flow Logs are enabled; there is no visibility into network traffic

Analyze each issue and propose remediations:

1. For each security issue identified above, explain:
   - The specific risk it creates
   - The concrete remediation steps (include specific GCP features or commands)
2. Propose a redesigned IAM structure that prevents developers from modifying
   production network resources while still allowing them to manage load
   balancers in their own environment.
3. Describe how you would implement network traffic monitoring going forward.
   Which services would you use and what would you look for?
4. Explain how Shared VPC could have prevented the permission boundary issue
   between developers and production network resources.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- Specific CIDR ranges in your subnet designs (e.g., 10.10.1.0/24)
- Specific firewall rule parameters (direction, priority, ports, targets)
- Explicit justification for each architectural decision

Your two peer responses must each be at least 100 words and do one of the
following:

- Identify an attack vector or failure scenario the original design does not
  address
- Propose a different subnet structure or connectivity option with reasoning
- Challenge a specific firewall rule design and explain the risk

---

## Discussion Tips

- Think in layers: perimeter (firewall), internal segmentation (subnets),
  monitoring (flow logs), and hybrid connectivity are all independent concerns.
- The ACE exam tests your ability to choose between VPC peering and Shared VPC
  for a given organizational model. Practice explaining the difference clearly.
- For firewall rule design, always work from the principle of least privilege:
  start with deny all, add specific allows only for what is needed.

---

## Reflection Question (Optional — Extra Credit)

In a traditional data center, a firewall is a physical or virtual appliance.
In GCP, firewall rules are software-defined and managed via IAM policies.
Discuss how this difference changes the security model. What new risks does
software-defined networking introduce, and what capabilities does it provide
that hardware firewalls cannot? Minimum 150 words.

---

End of Discussion — Module 05

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

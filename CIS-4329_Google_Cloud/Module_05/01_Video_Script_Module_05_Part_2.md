# Video Script — Module 05, Part 2

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: VPC Peering, Hybrid Connectivity, Private Google Access, and CLI

### Estimated Duration: 11–12 minutes

---

## Introduction to Part 2

Welcome back to Module 05. In Part 1 we covered VPC architecture, subnet configuration, firewall rules, and routes. In Part 2 we cover VPC peering, Private Google Access, Cloud VPN, Cloud Interconnect, and the gcloud commands for network management.

---

## Section 1: VPC Peering

**[SHOW SLIDE: Two VPCs labeled vpc-A and vpc-B with a peering arrow between them, private traffic flowing across]**

VPC peering allows two separate GCP VPC networks to communicate using private IP addresses. Traffic between peered VPCs travels over Google's private internal network — never over the public internet.

Use VPC peering when:

- You have separate projects (development, production) that need to communicate
- You want to share a centralized service (like a database) across multiple project VPCs
- You are using Shared VPC (covered below)

### Critical ACE Exam Fact: VPC Peering is Non-Transitive

**[SHOW SLIDE: Three VPCs A-B-C with peering A-to-B and B-to-C, but red X between A and C]**

This is one of the most frequently tested networking facts on the ACE exam. VPC peering is NOT transitive.

If VPC A is peered with VPC B, and VPC B is peered with VPC C, VMs in VPC A cannot communicate with VMs in VPC C. The peering relationship exists only between directly connected pairs. For A to communicate with C, you must create a direct peering between A and C.

### Shared VPC

Shared VPC is a related concept. It allows you to share a single VPC (the host project's VPC) across multiple GCP projects (service projects). All service project VMs use the host project's VPC, subnets, and firewall rules. This gives central network administration control over a multi-project organization while allowing individual project teams to deploy their own resources.

Shared VPC is administered by setting a project as the host project and then granting `roles/compute.networkUser` to service account principals in the service projects.

---

## Section 2: Private Google Access

**[SHOW SLIDE: VM without external IP using Private Google Access to reach storage.googleapis.com via internal path]**

By default, a VM that has no external IP address cannot reach Google APIs or services like Cloud Storage, BigQuery, or Cloud Logging. Private Google Access solves this.

When Private Google Access is enabled on a subnet, VMs in that subnet with only internal IP addresses can reach Google APIs and services through Google's internal network. The VMs do not need external IPs and their traffic never leaves Google's network.

Enable Private Google Access on a subnet:

```bash
gcloud compute networks subnets update my-subnet \
  --region=us-central1 \
  --enable-private-ip-google-access
```

Private Google Access is a critical feature for security-hardened environments where VMs are intentionally provisioned without external IPs to reduce attack surface. You still need Private Google Access enabled to let those VMs call GCS, BigQuery, or the Pub/Sub API.

For the ACE exam: if a question describes VMs without external IPs that cannot reach Cloud Storage or other Google services, enabling Private Google Access on the subnet is the solution.

---

## Section 3: Cloud VPN

**[SHOW SLIDE: On-premises network connected to GCP VPC via VPN tunnel over the internet with IPsec shield icon]**

Cloud VPN creates an encrypted IPsec tunnel between your on-premises network and your GCP VPC over the public internet. It allows private IP communication between on-premises resources and GCP resources as if they were on the same network.

There are two Cloud VPN configurations:

### Classic VPN

Classic VPN uses a single tunnel with a single gateway. It supports up to 3 Gbps throughput per tunnel. Classic VPN has a lower SLA and is suitable for development environments and lower-bandwidth requirements.

### HA VPN (High Availability VPN)

HA VPN uses two VPN gateways, each with two tunnel endpoints, for a total of four possible tunnels. It provides a 99.99% availability SLA. HA VPN is required for production environments with high-availability requirements.

When to use Cloud VPN:
- Bandwidth requirement under 1.5–3 Gbps
- Budget-sensitive hybrid connectivity
- Encrypting traffic over the public internet is acceptable

```bash
gcloud compute vpn-tunnels create my-vpn-tunnel \
  --peer-address=PEER_IP \
  --shared-secret=MY_SECRET \
  --target-vpn-gateway=my-vpn-gateway \
  --region=us-central1
```

---

## Section 4: Cloud Interconnect

**[SHOW SLIDE: On-premises data center connected to Google PoP with dedicated physical cable, no internet involved]**

Cloud Interconnect provides a direct physical connection to Google's network — bypassing the public internet entirely. There are two types:

### Dedicated Interconnect

A private physical fiber connection between your data center and a Google colocation facility (Point of Presence). Available in 10 Gbps and 100 Gbps increments. For organizations requiring multi-gigabit bandwidth to GCP with consistent, low-latency performance.

### Partner Interconnect

If your data center is not located near a Google colocation facility, you work with a network service provider (partner) who has a direct connection to Google. You get a sub-1Gbps to 10Gbps connection through the partner's infrastructure. More flexible geographically but with an added provider in the middle.

### VPN vs. Interconnect Decision

| Requirement | Correct Choice |
|---|---|
| Under 1.5 Gbps, budget sensitive | Cloud VPN (HA VPN for production) |
| 1.5 Gbps to 10 Gbps, consistent performance | Partner Interconnect |
| 10 Gbps to 100 Gbps, highest performance | Dedicated Interconnect |
| Traffic must stay off public internet entirely | Dedicated or Partner Interconnect |

---

## Section 5: gcloud Networking Commands

**[SHOW CONSOLE: Cloud Shell with gcloud compute networking commands]**

Create a custom VPC:

```bash
gcloud compute networks create my-vpc \
  --subnet-mode=custom
```

Create a subnet in the VPC:

```bash
gcloud compute networks subnets create my-subnet \
  --network=my-vpc \
  --region=us-central1 \
  --range=10.10.0.0/24
```

List networks:

```bash
gcloud compute networks list
```

List subnets:

```bash
gcloud compute networks subnets list
```

Create a firewall rule:

```bash
gcloud compute firewall-rules create allow-ssh-internal \
  --direction=INGRESS \
  --priority=1000 \
  --network=my-vpc \
  --action=ALLOW \
  --rules=tcp:22 \
  --source-ranges=10.10.0.0/24
```

List firewall rules:

```bash
gcloud compute firewall-rules list
```

Describe a firewall rule:

```bash
gcloud compute firewall-rules describe allow-ssh-internal
```

Enable Private Google Access on a subnet:

```bash
gcloud compute networks subnets update my-subnet \
  --region=us-central1 \
  --enable-private-ip-google-access
```

---

## Module 05 Summary

**[SHOW SLIDE: Summary bullet list]**

Let's wrap up Module 05. GCP VPCs are global; subnets are regional. Auto mode creates predefined subnets; custom mode gives full IP control. The implied default is deny-all ingress, allow-all egress. Firewall rules use direction, priority, action, target (tags or service accounts), and protocol/port. Network tags target firewall rules at logical VM groups.

VPC peering is non-transitive. Private Google Access lets VMs without external IPs reach Google APIs. Cloud VPN creates IPsec tunnels over the public internet — HA VPN for production with 99.99% SLA. Dedicated Interconnect provides direct physical connections at 10–100 Gbps. Partner Interconnect goes through a service provider for sub-10 Gbps needs.

Complete the lab, take the quiz, and post to the discussion. Module 06 covers Cloud Load Balancing and Cloud CDN.

---

End of Part 2 — Module 05

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

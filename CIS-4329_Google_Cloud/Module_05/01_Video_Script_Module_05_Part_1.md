# Video Script — Module 05, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Virtual Private Cloud — Architecture, Subnets, and Firewall Rules

### Estimated Duration: 13–15 minutes

---

## Introduction

Welcome to Module 05. I'm Professor Nash, and today we are covering Virtual Private Cloud — VPC networking. Networking is one of the most important and most tested topics on the Associate Cloud Engineer exam. If IAM controls who can do what, VPC controls what can communicate with what.

By the end of this module you will understand GCP's global VPC model, subnets, firewall rules, routes, and the connectivity options for hybrid environments. This module is challenging, but I promise we will build it up systematically. Let's start with the architecture.

---

## Section 1: VPC — A Global Resource

**[SHOW SLIDE: World map with one large VPC boundary spanning the entire globe, subnets shown as smaller boxes in different regions]**

Here is the first thing that makes GCP networking different from every other major cloud provider: in GCP, a VPC is a global resource. It is not tied to a region. A single VPC spans Google's entire global network.

Subnets, however, are regional. A subnet is a range of IP addresses in a specific region. You can have a single VPC with one subnet in `us-central1`, another subnet in `europe-west1`, and another in `asia-east1`. VMs in all three subnets are in the same VPC and can communicate with each other privately over Google's internal network — without their traffic ever touching the public internet.

Compare this to AWS: in AWS, a VPC is regional. If you want resources in two regions to communicate privately, you need VPC peering between two separate VPCs. In GCP, a single VPC already spans all regions.

This global VPC design is architecturally simpler for multi-region deployments and it means your routing configuration, firewall rules, and IAM policies are centralized in one VPC rather than scattered across multiple regional ones.

---

## Section 2: VPC Types

**[SHOW SLIDE: Auto vs. Custom VPC comparison table]**

GCP offers two types of VPCs:

### Auto Mode VPC

When you create an Auto mode VPC, GCP automatically creates one subnet in each region using predefined /20 CIDR blocks (e.g., `10.128.0.0/20` for `us-central1`). New subnets are automatically created in new regions as Google expands. Auto mode is convenient for getting started quickly.

The default VPC that comes with every new GCP project is an Auto mode VPC. It is already set up with firewall rules that allow SSH, RDP, and ICMP from anywhere.

### Custom Mode VPC

In a Custom mode VPC, you create subnets manually with the CIDR ranges you specify. You have full control over IP addressing. Custom mode is required for production environments because:

- It prevents IP address overlap when connecting to on-premises networks or other VPCs
- You control subnet sizing precisely
- You avoid the predefined /20 blocks which may conflict with existing networks

For the ACE exam: auto mode is for convenience and learning. Custom mode is for production. If a question asks about a production environment requiring specific IP addressing or hybrid connectivity, custom mode is the answer.

---

## Section 3: Subnets and IP Addressing

**[SHOW SLIDE: VPC with two subnets — 10.10.0.0/24 in us-central1, 10.20.0.0/24 in europe-west1]**

A subnet is a regional IP address range. When you create a subnet, you specify:

- The region (e.g., `us-central1`)
- The primary CIDR range (e.g., `10.10.0.0/24` — 256 addresses, 254 usable by VMs)
- Optionally, secondary CIDR ranges for Kubernetes pods and services

When a VM is created in a region, it gets an internal (private) IP address from the subnet for that region. This is the VM's primary internal IP. GCP reserves four addresses from each subnet: the network address, the default gateway, the second-to-last address (for Google future use), and the broadcast address.

VMs can optionally have an external (public) IP address that allows inbound connections from the internet. External IPs can be ephemeral (assigned from Google's pool, released when VM stops) or static (reserved specifically for your project and persistent across VM restarts).

**[PAUSE — Professor on camera]**

For the ACE exam: ephemeral external IPs do not expire on a timer — they persist as long as the VM is running. They are released when the VM is stopped or deleted. Static IPs are billed even when not in use, so always remember to release static IPs when you no longer need them to avoid unnecessary charges.

---

## Section 4: Firewall Rules

**[SHOW SLIDE: Firewall rule anatomy — direction, priority, match, action, target]**

This is the most tested section of the networking module. VPC firewall rules control what traffic is allowed into and out of your VMs.

### Implied Default Rules

Every VPC has two implied default rules that cannot be deleted:

- Implied deny-all ingress (priority 65535): blocks all inbound traffic unless an explicit allow rule permits it
- Implied allow-all egress (priority 65535): allows all outbound traffic unless an explicit deny rule blocks it

These are the baseline. Everything you add either creates exceptions to the ingress deny or restrictions to the egress allow.

### Firewall Rule Components

Each firewall rule has:

- Direction: `INGRESS` (inbound to VM) or `EGRESS` (outbound from VM)
- Priority: 0 (highest priority) to 65535 (lowest). Lower number = evaluated first.
- Action: `ALLOW` or `DENY`
- Target: which VMs the rule applies to — all instances, instances with a specific network tag, or instances with a specific service account
- Source/destination filter: for ingress, filter by source IP range or source tag. For egress, filter by destination IP range or destination tag.
- Protocol and port: `tcp:80`, `tcp:443`, `udp:53`, `icmp`, or `all`

### Network Tags as Firewall Targets

Network tags are one of the most powerful and most tested concepts in GCP networking. A tag is a string (like `http-server` or `db-tier`) that you apply to a VM. Firewall rules can target VMs by their network tags, allowing you to write rules that apply to a logical group of VMs regardless of where they live in the VPC.

Example: you want to allow HTTPS traffic to all web servers. Tag your web servers with `https-server`. Create one ingress firewall rule: allow TCP:443 from `0.0.0.0/0`, target tag `https-server`. Now any VM you tag with `https-server` automatically receives HTTPS traffic — no per-VM firewall configuration needed.

```bash
gcloud compute firewall-rules create allow-https \
  --direction=INGRESS \
  --priority=1000 \
  --network=default \
  --action=ALLOW \
  --rules=tcp:443 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=https-server
```

---

## Section 5: Routes

**[SHOW SLIDE: Route table showing system-generated routes and a custom static route]**

Routes define where network traffic is sent. Every VPC has system-generated routes:

- Local subnet routes: traffic destined for any subnet in the VPC is routed locally (within the VPC)
- Default internet route: a `0.0.0.0/0` route pointing to the internet gateway, which allows outbound internet access from VMs with external IPs

You can also create custom static routes to direct traffic to specific destinations through a VPN gateway, a VM acting as a network appliance, or another hop.

For the ACE exam: the default route (`0.0.0.0/0`) is what allows VMs with external IPs to reach the internet. If you delete this route, VMs lose outbound internet access even if they have external IPs. Private Google Access (covered in the lab) is a feature that allows VMs without external IPs to reach Google APIs using their internal IP through the internal network.

---

## Closing — Part 1

To summarize Part 1: GCP VPCs are global resources that span all regions. Subnets are regional IP address ranges within a VPC. Auto mode VPCs create predefined subnets automatically; custom mode gives you full control. Firewall rules use direction, priority, action, target, and source/destination to control traffic. The implied defaults are deny-all ingress and allow-all egress. Network tags let you target firewall rules at logical groups of VMs. Routes direct traffic to its destination.

In Part 2 we will cover VPC peering, Private Google Access, Cloud VPN, Cloud Interconnect, and the gcloud networking commands.

---

End of Part 1 — Module 05

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

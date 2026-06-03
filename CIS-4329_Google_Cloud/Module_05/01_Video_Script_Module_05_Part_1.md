# Video Script: Module 05 — Virtual Private Cloud Networking (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Introduction (1 minute)

Welcome to Module 05. This module covers Virtual Private Cloud networking —
the foundation of how your GCP resources communicate with each other and with
the outside world.

Networking is one of the more complex ACE exam topic areas. You need to
understand VPC architecture, subnets, firewall rules, routes, connectivity
options, and load balancing types.

In Part 1 we cover VPC concepts, subnets, firewall rules, and routes.
In Part 2 we cover VPC peering, Shared VPC, Cloud VPN, Cloud Interconnect,
load balancing, and Cloud Armor.

---

## Segment 2 — VPC Architecture (4 minutes)

### What is a VPC?

A Virtual Private Cloud (VPC) is a private, isolated network within GCP. It
defines the IP address space, connectivity rules, and routing for your cloud
resources.

Key characteristics of GCP VPCs that differ from other cloud providers:

- **Global by default**: A GCP VPC is a single global resource. It is not
  confined to a region. One VPC spans all GCP regions.
- **Subnets are regional**: Within a global VPC, subnets are regional resources.
  A subnet exists in a specific region and has a specific IP range.
- **No subnet in "all regions"**: You explicitly create subnets in each region
  where you need resources.

This design means a VM in `us-central1` and a VM in `europe-west1` can be on
the same VPC and communicate privately, as long as they share the same VPC.

### Auto-mode vs. Custom-mode VPCs

When you create a project, GCP creates a **default VPC** in auto mode. You
can also create custom VPCs.

#### Auto-mode VPC

- Automatically creates one subnet per region
- All subnets use a predefined /20 IP range from the 10.128.0.0/9 block
- Easy to get started but less flexible
- Not recommended for production (addresses can conflict with on-premises)

#### Custom-mode VPC

- You define every subnet manually — region, IP range, and settings
- Full control over IP addressing
- Recommended for production environments and anything connecting to
  on-premises networks

```bash
# Create a custom VPC
gcloud compute networks create lab05-vpc \
  --subnet-mode=custom \
  --mtu=1460

# Create a subnet in us-central1
gcloud compute networks subnets create lab05-subnet-us \
  --network=lab05-vpc \
  --region=us-central1 \
  --range=10.10.0.0/24

# Create a subnet in europe-west1
gcloud compute networks subnets create lab05-subnet-eu \
  --network=lab05-vpc \
  --region=europe-west1 \
  --range=10.20.0.0/24
```

**ACE Exam Tip:** Know the difference between auto-mode and custom-mode VPCs.
For production, custom is preferred. Converting auto to custom is possible
(one-way); converting custom back to auto is not.

---

## Segment 3 — Subnets (2 minutes)

### Subnet Properties

A subnet is a regional resource within a VPC. It has:

- **IP range**: CIDR notation (e.g., 10.10.0.0/24 provides 256 addresses;
  GCP reserves 4 per subnet: network, gateway, two for Google)
- **Region**: The region where this subnet's resources reside
- **Private Google Access**: When enabled, VMs with no external IP can still
  reach Google APIs via internal routing
- **Flow logs**: When enabled, records network flow data to Cloud Logging

### Secondary IP Ranges

Subnets can have secondary CIDR ranges — separate address spaces within the
same subnet. Used primarily for GKE pods and services:

- Primary range: VM internal IPs
- Secondary range 1: GKE pod IPs
- Secondary range 2: GKE service IPs

### Subnet Expansion

You can expand a subnet's primary IP range without any downtime. You cannot
shrink a subnet.

```bash
# Expand a subnet range
gcloud compute networks subnets expand-ip-range lab05-subnet-us \
  --region=us-central1 \
  --prefix-length=22
```

---

## Segment 4 — Firewall Rules (4 minutes)

### GCP Firewall Model

GCP firewall rules control inbound and outbound traffic to and from VM
instances. They are stateful — if you allow inbound traffic on a port, the
return traffic is automatically allowed.

Firewall rules are defined at the VPC level and applied to VMs using:

- **Network tags**: A tag attached to a VM; the rule targets VMs with that tag
- **Service accounts**: The rule targets VMs running as a specific service
  account
- **All instances in the VPC**: No target filter — applies to all VMs

### Firewall Rule Components

Every firewall rule has:

- **Direction**: INGRESS (inbound) or EGRESS (outbound)
- **Priority**: 0–65535; lower number = higher priority
- **Action**: ALLOW or DENY
- **Target**: Which VMs the rule applies to
- **Source/Destination**: IP ranges, tags, or service accounts
- **Protocol and ports**: TCP, UDP, ICMP, or all protocols

### Default Rules

Every VPC has implied rules that cannot be deleted but can be overridden with
higher-priority rules:

- **Implied deny all ingress** (priority 65535): Blocks all inbound traffic
  by default
- **Implied allow all egress** (priority 65535): Allows all outbound traffic
  by default

The default VPC also has these explicit default rules:

- `default-allow-internal`: Allow all traffic between VMs in the default VPC
- `default-allow-ssh`: Allow TCP:22 from 0.0.0.0/0
- `default-allow-rdp`: Allow TCP:3389 from 0.0.0.0/0
- `default-allow-icmp`: Allow ICMP from 0.0.0.0/0

These default rules are a security concern for production — allowing SSH from
0.0.0.0/0 means anyone can attempt to connect.

### Creating Firewall Rules

```bash
# Allow HTTP traffic to VMs tagged "web-server"
gcloud compute firewall-rules create allow-http \
  --network=lab05-vpc \
  --allow=tcp:80 \
  --direction=INGRESS \
  --target-tags=web-server \
  --source-ranges=0.0.0.0/0 \
  --priority=1000

# Allow SSH only from your office IP range
gcloud compute firewall-rules create allow-ssh-office \
  --network=lab05-vpc \
  --allow=tcp:22 \
  --direction=INGRESS \
  --target-tags=admin-access \
  --source-ranges=203.0.113.0/24 \
  --priority=900

# Deny all SSH from the internet (lower priority — overridden by above for tagged VMs)
gcloud compute firewall-rules create deny-all-ssh \
  --network=lab05-vpc \
  --deny=tcp:22 \
  --direction=INGRESS \
  --priority=1100

# List firewall rules
gcloud compute firewall-rules list --network=lab05-vpc
```

**ACE Exam Tip:** Lower priority number wins. A rule with priority 800 overrides
a rule with priority 1000 when both match the same traffic. The implied deny
is at 65535 — the highest possible (lowest priority) number.

---

## Segment 5 — Routes (2 minutes)

### What is a Route?

A route determines where network traffic is forwarded when a packet's
destination matches the route's destination range. Every VPC has automatically
created routes:

- **Default route** (0.0.0.0/0): Sends traffic to the internet via the default
  internet gateway. Exists in every VPC by default.
- **Subnet routes**: One route per subnet, ensuring traffic within the VPC
  uses internal routing.

### Static Routes

You can create custom static routes to direct traffic to specific destinations
via a specific next hop:

- Next hop types: instance, IP address, VPN gateway, internal load balancer,
  VPC network (for peering)

```bash
# Create a static route to an on-premises subnet via a VPN gateway
gcloud compute routes create to-on-prem \
  --network=lab05-vpc \
  --destination-range=192.168.0.0/16 \
  --next-hop-vpn-tunnel=vpn-tunnel-1 \
  --priority=1000
```

### Dynamic Routes with Cloud Router

Cloud Router uses BGP (Border Gateway Protocol) to dynamically exchange routes
with on-premises routers or other VPCs. Required for Cloud VPN with dynamic
routing and for Cloud Interconnect.

---

## Summary — Part 1

In Part 1 we covered:

- GCP VPC: global resource, regional subnets, auto vs. custom mode
- Subnet properties: IP ranges, Private Google Access, flow logs
- Firewall rules: direction, priority, targets (tags vs. service accounts)
- Default firewall rules and their security implications
- Routes: default routes, subnet routes, and static routes

In Part 2 we cover VPC peering, Shared VPC, Cloud VPN, Cloud Interconnect,
load balancing types, and Cloud Armor.

See you in Part 2.

---

End of Part 1 — Module 05

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/vpc/docs

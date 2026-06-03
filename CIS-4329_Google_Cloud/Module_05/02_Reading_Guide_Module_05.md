# Reading Guide: Module 05 — Virtual Private Cloud Networking

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide covers GCP Virtual Private Cloud (VPC) networking. Networking
is one of the broader ACE exam topic areas, covering VPC design, firewall rules,
hybrid connectivity, and load balancing.

**Estimated Reading Time:** 55–65 minutes

---

## Section 1 — VPC Fundamentals

### 1.1 GCP VPC Architecture

GCP VPCs have several unique characteristics compared to other cloud providers:

- **Global scope**: A VPC is a single global resource, not region-specific. One
  VPC can span every GCP region simultaneously.
- **Regional subnets**: Resources (VMs, GKE clusters, etc.) are attached to
  regional subnets within the global VPC.
- **Private RFC 1918 addressing**: Internal IPs use RFC 1918 ranges
  (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).
- **Software-defined**: VPCs are fully software-defined; there are no physical
  routers to configure.

### 1.2 Auto-mode vs. Custom-mode

#### Auto-mode VPC

Automatically creates one /20 subnet in each GCP region when the VPC is
created. All subnets use predefined IP ranges from 10.128.0.0/9.

When to avoid auto-mode:

- When connecting to on-premises networks (address conflicts likely)
- When you need precise control over IP ranges
- Production environments

#### Custom-mode VPC

No subnets are created automatically. You define every subnet explicitly.

Converting auto to custom is possible and irreversible:

```bash
gcloud compute networks update NETWORK_NAME --switch-to-custom-subnet-mode
```

### 1.3 Subnet Configuration

Subnets have several configurable properties:

- **Primary CIDR range**: IP range for VMs in this subnet
- **Secondary CIDR ranges**: Additional ranges for GKE pods and services
- **Private Google Access**: Allows VMs without external IPs to reach Google
  APIs and services via Google's internal network
- **VPC Flow Logs**: Captures network flow records to Cloud Logging
- **Purpose**: Regular subnet, or Proxy-only (for internal load balancers)

#### Subnet Reserved IPs

Each subnet reserves 4 IP addresses:

- `.0` — Network address
- `.1` — Default gateway
- `.254` — Unused (reserved for Google future use)
- `.255` — Broadcast

A /24 subnet provides 252 usable addresses.

---

## Section 2 — Firewall Rules

### 2.1 Rule Components

| Component | Description |
|---|---|
| Network | Which VPC the rule applies to |
| Priority | 0–65535; lower = higher priority |
| Direction | INGRESS or EGRESS |
| Action | ALLOW or DENY |
| Target | VMs by tag, service account, or all instances |
| Source (ingress) | IP ranges, tags, or service accounts of traffic origin |
| Destination (egress) | IP ranges of traffic destination |
| Protocols and ports | TCP, UDP, ICMP, or any |

### 2.2 Implied Rules

| Rule | Priority | Direction | Action |
|---|---|---|---|
| Implied deny all ingress | 65535 | INGRESS | DENY |
| Implied allow all egress | 65535 | EGRESS | ALLOW |

These rules cannot be deleted but can be overridden by creating rules with
lower priority numbers.

### 2.3 Tag-based vs. Service Account-based Targeting

#### Network tags

Tags are arbitrary strings attached to VM instances. Firewall rules can target
VMs with specific tags.

- Tags are manually assigned and can be changed at any time
- Any user with instance admin permissions can add/remove tags
- Risk: A misconfigured VM can accidentally receive a sensitive tag

#### Service account targeting

Rules target VMs running as a specific service account.

- More secure than tags — requires IAM permissions to change a VM's SA
- Cannot mix SA targeting with IP range sources in the same rule
- Preferred for production security-critical rules

### 2.4 Firewall Rule Best Practices

```bash
# Restrict SSH to specific source ranges rather than 0.0.0.0/0
gcloud compute firewall-rules create allow-ssh-restricted \
  --network=custom-vpc \
  --allow=tcp:22 \
  --source-ranges=10.0.0.0/8 \
  --target-tags=bastion

# Allow internal traffic between VMs in the same subnet
gcloud compute firewall-rules create allow-internal \
  --network=custom-vpc \
  --allow=tcp,udp,icmp \
  --source-ranges=10.10.0.0/24 \
  --priority=1000

# Deny all other ingress explicitly (overrides implied deny for visibility)
gcloud compute firewall-rules create deny-all-ingress \
  --network=custom-vpc \
  --action=DENY \
  --rules=all \
  --direction=INGRESS \
  --priority=65500
```

---

## Section 3 — VPC Peering

### 3.1 Overview

VPC peering creates a private connection between two VPCs. Traffic between
peered VPCs uses GCP's internal network (not the internet) and is free for
intra-region traffic.

### 3.2 Key Constraints

- **Non-transitive**: A→B peering and B→C peering does NOT give A access to C.
- **No overlapping IP ranges**: Subnets in peered VPCs must not overlap.
- **Subnet route exchange**: Primary subnet routes are automatically shared;
  custom static routes are not shared unless explicitly configured.
- **Both sides must accept**: Each VPC owner must create a peering configuration.

### 3.3 Peering Commands

```bash
# From Project A
gcloud compute networks peerings create peer-a-to-b \
  --network=vpc-a \
  --peer-project=project-b-id \
  --peer-network=vpc-b

# From Project B
gcloud compute networks peerings create peer-b-to-a \
  --network=vpc-b \
  --peer-project=project-a-id \
  --peer-network=vpc-a

# Check peering status
gcloud compute networks peerings list --network=vpc-a
```

---

## Section 4 — Shared VPC

### 4.1 Architecture

Shared VPC uses a host project / service project model:

```text
Organization
  ├── Host Project (owns VPC, subnets, firewall rules)
  │     └── shared-vpc (subnets: prod-subnet, dev-subnet)
  ├── Service Project A (app team)
  │     └── VMs use prod-subnet in host project's VPC
  └── Service Project B (data team)
        └── VMs use dev-subnet in host project's VPC
```

### 4.2 IAM Roles for Shared VPC

| Role | Where assigned | Effect |
|---|---|---|
| `roles/compute.networkAdmin` | Host project | Manage the shared VPC |
| `roles/compute.networkUser` | Subnet in host project | Allow SA to create instances in subnet |
| `roles/compute.xpnAdmin` | Organization | Enable/attach Shared VPC |

### 4.3 Setup Commands

```bash
# Enable Shared VPC hosting on the host project
gcloud compute shared-vpc enable HOST_PROJECT

# Associate a service project
gcloud compute shared-vpc associated-projects add SERVICE_PROJECT \
  --host-project=HOST_PROJECT

# Grant a service account in the service project access to a subnet
gcloud compute networks subnets add-iam-policy-binding prod-subnet \
  --region=us-central1 \
  --project=HOST_PROJECT \
  --member="serviceAccount:sa@SERVICE_PROJECT.iam.gserviceaccount.com" \
  --role=roles/compute.networkUser
```

---

## Section 5 — Hybrid Connectivity

### 5.1 Cloud VPN

Cloud VPN uses IPsec to create an encrypted tunnel between GCP and an
on-premises network or another cloud provider, over the internet.

| Feature | Classic VPN | HA VPN |
|---|---|---|
| SLA | 99.9% | 99.99% |
| Routing | Static or dynamic (BGP) | Dynamic BGP only (requires Cloud Router) |
| Tunnels | 1 per gateway | 2 per gateway (active/active) |
| Throughput | Up to 3 Gbps | Up to 3 Gbps per tunnel |

### 5.2 Cloud Router

Cloud Router enables dynamic routing using BGP. Required for HA VPN and
Cloud Interconnect.

```bash
# Create a Cloud Router
gcloud compute routers create my-router \
  --network=custom-vpc \
  --region=us-central1 \
  --asn=65001

# View BGP sessions
gcloud compute routers get-status my-router --region=us-central1
```

### 5.3 Cloud Interconnect

| Type | Bandwidth | Physical location |
|---|---|---|
| Dedicated Interconnect | 10 Gbps or 100 Gbps per circuit | Google colocation facility |
| Partner Interconnect | 50 Mbps to 50 Gbps | Service provider facility |

Cloud Interconnect bypasses the internet entirely. Traffic flows on Google's
private network between your premises and GCP. Required for scenarios with
strict data-in-transit requirements or consistent high bandwidth.

---

## Section 6 — Load Balancing

### 6.1 Load Balancer Selection Matrix

| Load Balancer | Layer | Scope | Traffic |
|---|---|---|---|
| External Application LB | L7 | Global | External HTTP/HTTPS |
| External Regional Application LB | L7 | Regional | External HTTP/HTTPS |
| External Passthrough Network LB | L4 | Regional | External TCP/UDP |
| Internal Application LB | L7 | Regional | Internal HTTP/HTTPS |
| Internal Passthrough Network LB | L4 | Regional | Internal TCP/UDP |
| Cross-region Internal Application LB | L7 | Multi-region | Internal HTTP/HTTPS |

### 6.2 External Application Load Balancer (Global)

The most commonly tested load balancer on the ACE exam:

- Layer 7 HTTP/HTTPS
- Global Anycast IP — traffic served from the PoP closest to the user
- SSL termination at the LB edge
- URL-based routing: route `/api/*` to one backend, `/static/*` to another
- Cloud CDN integration
- Cloud Armor integration for WAF and DDoS protection
- Backend types: MIGs, NEGs (Network Endpoint Groups), Cloud Storage buckets

### 6.3 Health Checks

All load balancers use health checks to determine backend availability:

```bash
# Create an HTTP health check
gcloud compute health-checks create http web-hc \
  --port=80 \
  --request-path=/health \
  --check-interval=10 \
  --timeout=5 \
  --healthy-threshold=2 \
  --unhealthy-threshold=3
```

---

## Section 7 — Cloud Armor

### 7.1 Overview

Cloud Armor is GCP's DDoS protection and WAF service. It is enforced at
Google's global edge network, before traffic reaches your backends.

Integration points:

- Attaches to backend services on External Application Load Balancer (global)
- Cannot be used with internal load balancers or passthrough load balancers

### 7.2 Security Policy Rules

Rules are evaluated in priority order (lowest number first). A default rule
at priority 2147483647 defines the default action (allow or deny).

```bash
# Allow traffic only from specific countries (geo restriction)
gcloud compute security-policies rules create 500 \
  --security-policy=my-policy \
  --expression="origin.region_code == 'US'" \
  --action=allow

# Deny all other traffic (default deny)
gcloud compute security-policies rules update 2147483647 \
  --security-policy=my-policy \
  --action=deny-403
```

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| VPC | Virtual Private Cloud — global private network in GCP |
| Subnet | Regional IP range within a VPC where resources are deployed |
| Auto-mode VPC | VPC that automatically creates subnets in every region |
| Custom-mode VPC | VPC where subnets are defined manually |
| Firewall rule | Stateful rule allowing or denying traffic to/from VM instances |
| Network tag | Label on a VM used to target firewall rules |
| VPC peering | Direct private connection between two VPCs; non-transitive |
| Shared VPC | Enterprise pattern connecting service projects to a host VPC |
| Cloud VPN | IPsec encrypted tunnel over the internet to GCP |
| HA VPN | High-availability VPN with 99.99% SLA and dual tunnels |
| Cloud Router | Dynamic BGP routing for VPN and Interconnect |
| Dedicated Interconnect | Physical 10/100 Gbps circuit to Google's network |
| Partner Interconnect | Interconnect via a service provider |
| Cloud Armor | DDoS protection and WAF for external application LB |
| NEG | Network Endpoint Group — defines backends at IP:port level |

---

## ACE Exam Focus Areas — Module 05

- Explain the difference between a VPC (global) and a subnet (regional).
- Describe auto-mode vs. custom-mode VPCs and when to use each.
- Explain firewall rule priority and how ALLOW/DENY interact.
- Describe VPC peering non-transitivity with examples.
- Explain the Shared VPC host/service project model.
- Choose between Cloud VPN and Cloud Interconnect for a given scenario.
- Select the correct load balancer type for a described use case.
- Describe where Cloud Armor integrates and what it protects against.

---

## Further Reading

- VPC overview: cloud.google.com/vpc/docs/vpc
- Firewall rules: cloud.google.com/vpc/docs/firewalls
- VPC peering: cloud.google.com/vpc/docs/vpc-peering
- Shared VPC: cloud.google.com/vpc/docs/shared-vpc
- Cloud VPN: cloud.google.com/network-connectivity/docs/vpn
- Load balancing overview: cloud.google.com/load-balancing/docs/load-balancing-overview
- Cloud Armor: cloud.google.com/armor/docs

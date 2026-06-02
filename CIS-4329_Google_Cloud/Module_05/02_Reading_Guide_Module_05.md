# Reading Guide — Module 05

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Virtual Private Cloud (VPC) — Networking Fundamentals

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

VPC networking is one of the most tested domains on the Associate Cloud Engineer exam. This reading guide covers the GCP global VPC model, subnet configuration, firewall rules and their statefulness, routes, VPC peering (including its non-transitive behavior), Private Google Access, Cloud VPN, Cloud Interconnect, and the gcloud CLI commands for network administration. Study every table carefully — the ACE exam frequently uses scenario-based networking questions that require you to apply multiple concepts simultaneously.

---

## 1. GCP VPC Architecture

### Global VPC vs. Regional Subnets

| Concept | Scope | Notes |
|---|---|---|
| VPC Network | Global | Spans all regions; one namespace for routes and firewall rules |
| Subnet | Regional | IP address range within one region |
| Firewall Rule | VPC level, enforced per-VM | Applies to all VMs in VPC unless filtered by tag or SA |
| Route | VPC level | Applies to all VMs unless filtered by tag |

### Auto Mode vs. Custom Mode VPC

| Feature | Auto Mode | Custom Mode |
|---|---|---|
| Subnet creation | Automatic — one per region | Manual — you create each subnet |
| CIDR blocks | Predefined /20 blocks (10.x.x.x range) | You specify any CIDR |
| New region support | Auto-creates subnet in new regions | No automatic expansion |
| IP overlap risk | Risk when connecting to other networks | Full control — you prevent overlap |
| Production use | Development and learning | Recommended for all production environments |

### IP Address Types for VMs

| Type | Scope | Persistence | Cost |
|---|---|---|---|
| Internal (private) IP | Within VPC | Persistent while VM running | Free |
| Ephemeral external IP | Public internet | Released on VM stop/delete | Free (while VM running) |
| Static external IP | Public internet | Persistent until you release it | Billed even when unattached |

---

## 2. Firewall Rules

### Implied Default Rules (Undeleteable)

| Rule | Direction | Priority | Action | Applies To |
|---|---|---|---|---|
| Implied deny-all ingress | INGRESS | 65535 | DENY | All VMs |
| Implied allow-all egress | EGRESS | 65535 | ALLOW | All VMs |

These rules always exist at the lowest priority. All custom rules override them.

### Firewall Rule Components

| Component | Values | Notes |
|---|---|---|
| Direction | INGRESS or EGRESS | Controls traffic direction |
| Priority | 0–65535 | Lower number = higher priority; evaluated first |
| Action | ALLOW or DENY | What to do when rule matches |
| Protocol/Port | `tcp:80`, `udp:53`, `icmp`, `all` | Specific or all traffic |
| Target | All, network tag, or service account | Which VMs the rule applies to |
| Source (ingress) | IP range or source tag | Filter for inbound traffic origin |
| Destination (egress) | IP range or destination tag | Filter for outbound traffic destination |

### Firewall Statefulness

GCP firewall rules are stateful. For connection-oriented protocols like TCP:

- If an ingress rule allows a TCP connection to be established, return packets for that connection are automatically permitted
- You do NOT need to create a separate egress rule to allow reply traffic
- This is different from traditional stateless packet filtering ACLs

### Network Tags vs. Service Account Targets

| Targeting Method | When to Use |
|---|---|
| Network tag | When VMs are identified by role/function (web-tier, db-tier) |
| Service account | When VMs are identified by the service account they run as (more secure, cannot be added by VM user) |

Service account targeting is more secure because only administrators with IAM permission to set service accounts on VMs can add that identity — unlike tags, which any user with access to modify VM metadata can apply.

### Default VPC Firewall Rules

The default VPC comes pre-configured with these rules:

| Rule Name | Direction | Allows | From |
|---|---|---|---|
| default-allow-internal | INGRESS | All TCP/UDP/ICMP | Subnets within same VPC |
| default-allow-ssh | INGRESS | TCP:22 | 0.0.0.0/0 |
| default-allow-rdp | INGRESS | TCP:3389 | 0.0.0.0/0 |
| default-allow-icmp | INGRESS | ICMP | 0.0.0.0/0 |

In production custom VPCs, none of these default rules exist. You must create your own.

---

## 3. Routes

### System-Generated Routes

| Route | Destination | Next Hop | Purpose |
|---|---|---|---|
| Default internet route | 0.0.0.0/0 | default-internet-gateway | Outbound internet access |
| Local subnet routes | Per-subnet CIDR | local | Internal VPC communication |

### Custom Static Routes

You can create custom routes to:

- Direct traffic to a VPN tunnel gateway
- Route traffic through a VM acting as a network appliance
- Override the default internet route for specific destinations

Custom routes with tags: routes can be limited to VMs with specific network tags using the `--tags` flag.

### Private Google Access

Private Google Access enables VMs with only internal IPs to reach Google API endpoints (storage.googleapis.com, bigquery.googleapis.com, etc.) without routing through the public internet.

```bash
gcloud compute networks subnets update SUBNET \
  --region=REGION \
  --enable-private-ip-google-access
```

When to enable: always, for any subnet containing VMs that should not have external IPs but need to access Google Cloud services.

---

## 4. VPC Peering

### What VPC Peering Does

- Connects two VPC networks (in the same or different projects) so VMs can communicate via internal IPs
- Traffic stays on Google's private network
- Both VPCs must peer with each other (bidirectional configuration required)

### Non-Transitive Peering — The Critical Exam Rule

```text
VPC-A <--> VPC-B  (peered)
VPC-B <--> VPC-C  (peered)
VPC-A             VPC-C  (NOT reachable — no direct peering)
```

For VPC-A to communicate with VPC-C, a direct peering between VPC-A and VPC-C must be created. There is no transitive routing through VPC-B.

### Shared VPC

Shared VPC is an alternative to peering for multi-project organizations:

- One project is designated the "host project" and owns the VPC and subnets
- Other "service projects" use the host project's VPC for their resources
- Central IAM control of networking with decentralized project resource management
- Requires `roles/compute.networkUser` in service projects

---

## 5. Hybrid Connectivity

### Cloud VPN

| Type | Tunnels | SLA | Max Throughput | Use Case |
|---|---|---|---|---|
| Classic VPN | 1 tunnel | 99.9% | 3 Gbps per tunnel | Dev/test, lower-bandwidth |
| HA VPN | 2 gateways, 4 tunnels | 99.99% | 3 Gbps per tunnel | Production hybrid |

Cloud VPN uses IPsec to encrypt all traffic over the public internet. Requires compatible VPN gateway on-premises (hardware or software).

### Cloud Interconnect

| Type | Bandwidth | Physical Connection | Use Case |
|---|---|---|---|
| Dedicated Interconnect | 10 Gbps or 100 Gbps | Direct to Google PoP | High-bandwidth, enterprise |
| Partner Interconnect | 50 Mbps to 10 Gbps | Through a service provider | Geographically flexible |

Cloud Interconnect does not use the public internet. Traffic flows directly between your facility and Google's network. No encryption at the IP layer by default (encryption provided by the physical connection security at the facility level, or by application-layer TLS).

### Decision Table

| Scenario | Correct Choice |
|---|---|
| Under 1.5 Gbps, budget-sensitive | Cloud VPN (HA VPN for production) |
| Must avoid public internet entirely | Dedicated or Partner Interconnect |
| Data center not near Google PoP | Partner Interconnect |
| 10–100 Gbps direct enterprise connection | Dedicated Interconnect |
| Connecting two GCP VPCs | VPC Peering or Shared VPC |

---

## 6. gcloud Networking Command Reference

### VPC and Subnet Operations

| Command | Description |
|---|---|
| `gcloud compute networks create NAME --subnet-mode=custom` | Create a custom VPC |
| `gcloud compute networks create NAME --subnet-mode=auto` | Create an auto-mode VPC |
| `gcloud compute networks list` | List all VPCs |
| `gcloud compute networks describe NAME` | View VPC details |
| `gcloud compute networks subnets create NAME --network=VPC --region=R --range=CIDR` | Create a subnet |
| `gcloud compute networks subnets list` | List all subnets |
| `gcloud compute networks subnets update NAME --region=R --enable-private-ip-google-access` | Enable Private Google Access |
| `gcloud compute networks delete NAME` | Delete a VPC (must have no subnets) |

### Firewall Rule Operations

| Command | Description |
|---|---|
| `gcloud compute firewall-rules create NAME --direction=INGRESS --action=ALLOW --rules=tcp:PORT --source-ranges=CIDR --target-tags=TAG` | Create an ingress allow rule |
| `gcloud compute firewall-rules list` | List all firewall rules |
| `gcloud compute firewall-rules describe NAME` | View rule details |
| `gcloud compute firewall-rules update NAME --priority=500` | Update rule priority |
| `gcloud compute firewall-rules delete NAME` | Delete a firewall rule |

### VM Tag Operations

| Command | Description |
|---|---|
| `gcloud compute instances add-tags VM --tags=TAG1,TAG2 --zone=Z` | Add network tags to a VM |
| `gcloud compute instances remove-tags VM --tags=TAG1 --zone=Z` | Remove network tags from a VM |

---

## 7. ACE Exam Tips

1. GCP VPCs are global — subnets are regional. A single VPC spans all regions without any special configuration. This is fundamentally different from AWS.

2. Firewall rules are stateful. You only need an ingress rule for a service — return traffic is automatically permitted. Do not create matching egress rules for services that only need inbound access.

3. VPC peering is non-transitive. A-to-B peering and B-to-C peering does not allow A-to-C communication. Each pair must have a direct peering relationship.

4. The implied deny-all ingress rule cannot be deleted. It exists at priority 65535. Any allow rule with a lower priority number overrides it.

5. Network tags target firewall rules at VM groups. Tag-based rules are the preferred pattern for production environments where VM membership in a tier changes over time.

6. Private Google Access enables API access for VMs without external IPs. If a VM with only an internal IP cannot reach Cloud Storage or BigQuery, enabling Private Google Access on its subnet is the fix.

7. Static external IPs are billed even when not attached to a VM. Always release unused static IPs.

8. Cloud VPN uses IPsec over the public internet. Cloud Interconnect bypasses the internet entirely. If a scenario requires traffic to stay off the public internet, the answer is Interconnect.

---

## 8. Network Topology Diagram Reference

### Single-Region Custom VPC

```text
Custom VPC (global)
  |
  +-- Subnet: 10.10.0.0/24 (us-central1)
       |
       +-- VM web-1  (tag: web-tier, internal: 10.10.0.2)
       +-- VM web-2  (tag: web-tier, internal: 10.10.0.3)
       +-- VM db-1   (tag: db-tier,  internal: 10.10.0.4)

Firewall Rules:
  allow-https:  INGRESS, tcp:443, from 0.0.0.0/0, target-tag: web-tier
  allow-db:     INGRESS, tcp:5432, from 10.10.0.0/24, target-tag: db-tier
  allow-ssh:    INGRESS, tcp:22, from 35.235.240.0/20 (IAP range), all VMs
```

### Hybrid VPC with Cloud VPN

```text
On-Premises (10.0.0.0/8)
       |
  [IPsec Tunnel] (Cloud VPN)
       |
GCP VPC (global)
  +-- Subnet: 192.168.1.0/24 (us-central1)
       +-- VMs communicating with on-prem via private IPs
```

---

## 9. Study Checklist

- [ ] Explain why GCP VPCs are global and give a practical benefit of this design
- [ ] Describe the difference between auto-mode and custom-mode VPCs with a recommendation for each context
- [ ] State the two implied default firewall rules that cannot be deleted
- [ ] Explain firewall rule statefulness and why it matters for rule design
- [ ] Create a firewall rule targeting VMs by network tag using gcloud
- [ ] Explain why VPC peering is non-transitive with a three-VPC example
- [ ] Describe Private Google Access and when it is required
- [ ] Compare Cloud VPN and Cloud Interconnect on the dimensions of bandwidth, cost, and internet use
- [ ] Create a custom VPC and subnet using gcloud
- [ ] Apply a network tag to a VM using gcloud
- [ ] Complete the Module 05 lab
- [ ] Take the Module 05 quiz
- [ ] Post your Module 05 discussion response

---

End of Reading Guide — Module 05

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

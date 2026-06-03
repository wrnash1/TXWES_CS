# Video Script: Module 05 — Virtual Private Cloud Networking (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Recap and Agenda (1 minute)

Welcome back. In Part 1 we covered VPC architecture, subnets, firewall rules,
and routes. In Part 2 we cover:

- VPC peering
- Shared VPC
- Cloud VPN and Cloud Interconnect
- Load balancing types
- Cloud Armor

---

## Segment 2 — VPC Connectivity: Peering and Shared VPC (4 minutes)

### VPC Peering

VPC peering connects two VPCs so that instances in each can communicate using
private IP addresses. The VPCs can be in the same project, different projects,
or different organizations.

Characteristics of VPC peering:

- **Non-transitive**: If VPC A peers with VPC B, and VPC B peers with VPC C,
  VPC A cannot communicate with VPC C through VPC B. Each peering must be
  established directly.
- **No IP range overlap**: Peered VPCs cannot have overlapping IP ranges.
- **Routes**: Subnet routes are automatically exchanged between peered VPCs.
  Custom static routes are not shared by default.
- **Symmetric**: Both sides must configure a peering request. Peering is active
  only when both sides accept.

```bash
# Peer VPC-A to VPC-B (run in VPC-A's project)
gcloud compute networks peerings create vpc-a-to-b \
  --network=vpc-a \
  --peer-project=project-b \
  --peer-network=vpc-b \
  --auto-create-routes

# Peer VPC-B to VPC-A (run in VPC-B's project — both sides required)
gcloud compute networks peerings create vpc-b-to-a \
  --network=vpc-b \
  --peer-project=project-a \
  --peer-network=vpc-a \
  --auto-create-routes
```

**ACE Exam Tip:** VPC peering is non-transitive. If a question involves three
VPCs that need to communicate, you need three separate peering relationships
(A-B, B-C, A-C), not a chain.

### Shared VPC

Shared VPC connects multiple GCP projects to a common, centrally managed VPC
network. It has two components:

- **Host project**: Owns the Shared VPC network and subnets. Network
  administrators in the host project manage all networking.
- **Service projects**: Projects that are attached to the host project. VMs in
  service projects can use subnets in the host VPC.

Benefits of Shared VPC:

- Central network management while delegating resource creation to teams
- Consistent firewall rules across all service projects
- Service project teams cannot modify network configuration

```bash
# Enable Shared VPC on the host project (requires organization admin)
gcloud compute shared-vpc enable HOST_PROJECT_ID

# Attach a service project
gcloud compute shared-vpc associated-projects add SERVICE_PROJECT_ID \
  --host-project=HOST_PROJECT_ID
```

**ACE Exam Tip:** Shared VPC requires an Organization node. It cannot be used
with personal Gmail accounts. When a question involves centralizing network
management across multiple projects in an enterprise, the answer is Shared VPC.

---

## Segment 3 — Cloud VPN and Cloud Interconnect (3 minutes)

### Cloud VPN

Cloud VPN connects your on-premises network to GCP using encrypted IPsec VPN
tunnels over the public internet.

Types:

- **Classic VPN**: Single tunnel; up to 3 Gbps; supports static routing only
- **HA VPN**: Two tunnels per gateway for 99.99% SLA; requires Cloud Router
  for dynamic BGP routing; recommended for production

```bash
# Create an HA VPN gateway
gcloud compute vpn-gateways create ha-vpn-gw \
  --network=lab05-vpc \
  --region=us-central1

# Create a Cloud Router for dynamic routing
gcloud compute routers create ha-vpn-router \
  --network=lab05-vpc \
  --region=us-central1 \
  --asn=65001
```

Use Cloud VPN when:

- Bandwidth requirement is under ~10 Gbps
- The connection is over the internet and encryption is acceptable
- Budget constraints favor a software VPN over dedicated circuits

### Cloud Interconnect

Cloud Interconnect provides a dedicated, physical connection between your
on-premises network and Google's network. Two types:

- **Dedicated Interconnect**: 10 Gbps or 100 Gbps physical circuit terminated
  at a Google colocation facility. Lowest latency; highest cost.
- **Partner Interconnect**: Connect through a service provider at lower
  bandwidth (50 Mbps to 50 Gbps). More flexible; available in more locations.

Cloud Interconnect traffic does not traverse the public internet. It stays on
Google's private network from your premises to GCP.

**ACE Exam Tip:** Use Cloud VPN for moderate bandwidth over the internet.
Use Cloud Interconnect when you need dedicated, consistent, high-bandwidth
connectivity (10+ Gbps) or when data must not travel over the public internet.

---

## Segment 4 — Load Balancing (4 minutes)

### GCP Load Balancer Types

GCP offers multiple load balancer types organized by traffic type, scope, and
whether they are external or internal.

#### External Global Load Balancers

- **External Application Load Balancer (HTTP/S LB)**: Layer 7; routes HTTP
  and HTTPS traffic globally. Supports URL-based routing, Cloud CDN, SSL
  termination, and Cloud Armor. Uses Google's global Anycast network.
- **External Proxy Network Load Balancer**: Layer 4 TCP/SSL; for non-HTTP
  traffic that requires global routing.

#### External Regional Load Balancers

- **External Regional Application Load Balancer**: Layer 7 HTTP/S but scoped
  to a region.
- **External Regional Network Load Balancer (passthrough)**: Layer 4; passes
  traffic directly to backends. Very high performance; preserves client IP.

#### Internal Load Balancers

- **Internal Application Load Balancer**: Layer 7; for internal HTTP/S
  services between VMs within the VPC.
- **Internal Passthrough Network Load Balancer**: Layer 4; for internal TCP/UDP;
  commonly used in front of internal services and third-party network appliances.

### Choosing the Right Load Balancer

| Use case | Load balancer type |
|---|---|
| Global HTTPS web app with CDN | External Application LB (Global) |
| Internal microservice HTTP API | Internal Application LB |
| TCP traffic, preserve client IP | External Passthrough Network LB |
| Internal database cluster TCP | Internal Passthrough Network LB |

```bash
# Create a backend service for an HTTP load balancer
gcloud compute backend-services create web-backend \
  --protocol=HTTP \
  --port-name=http \
  --health-checks=web-health-check \
  --global

# Add instance group to the backend service
gcloud compute backend-services add-backend web-backend \
  --instance-group=web-mig \
  --instance-group-region=us-central1 \
  --global

# Create a URL map
gcloud compute url-maps create web-url-map \
  --default-service=web-backend

# Create target HTTP proxy
gcloud compute target-http-proxies create web-http-proxy \
  --url-map=web-url-map

# Create forwarding rule (the load balancer's external IP)
gcloud compute forwarding-rules create web-lb-rule \
  --load-balancing-scheme=EXTERNAL \
  --global \
  --target-http-proxy=web-http-proxy \
  --ports=80
```

---

## Segment 5 — Cloud Armor (1 minute)

### What is Cloud Armor?

Cloud Armor is GCP's distributed denial-of-service (DDoS) protection and Web
Application Firewall (WAF) service. It integrates with the External Application
Load Balancer.

Capabilities:

- **DDoS protection**: Automatically mitigates volumetric DDoS attacks
- **IP allowlist/denylist**: Block or allow specific IP ranges
- **Preconfigured WAF rules**: ModSecurity-compatible rules for OWASP Top 10
  attacks (SQL injection, XSS, etc.)
- **Rate limiting**: Limit requests per IP per second
- **Adaptive Protection**: ML-based real-time attack detection

```bash
# Create a Cloud Armor security policy
gcloud compute security-policies create web-armor-policy \
  --description="WAF policy for web application"

# Add a rule to block a specific IP
gcloud compute security-policies rules create 1000 \
  --security-policy=web-armor-policy \
  --expression="inIpRange(origin.ip, '192.0.2.0/24')" \
  --action=deny-403

# Attach the policy to a backend service
gcloud compute backend-services update web-backend \
  --security-policy=web-armor-policy \
  --global
```

**ACE Exam Tip:** Cloud Armor attaches to backend services on the External
Application Load Balancer. It cannot be used with internal load balancers or
passthrough load balancers.

---

## Segment 6 — ACE Exam Tips for Networking (1 minute)

Key networking patterns on the ACE exam:

- **VPC is global; subnets are regional**: This is unique to GCP.
- **Auto mode vs. custom mode**: Custom is recommended for production.
- **VPC peering is non-transitive**: Three VPCs need three peering connections.
- **Shared VPC vs. VPC peering**: Shared VPC = central management, separate
  projects use host network. Peering = independent VPCs connect directly.
- **Cloud VPN vs. Interconnect**: VPN = internet-based, encrypted. Interconnect
  = dedicated circuit, no internet transit.
- **Load balancer selection**: Match the scenario to the correct LB type.
  External HTTPS with global distribution = External Application LB.
- **Firewall rule priority**: Lower number = higher priority.

---

## Summary — Module 05

Across both parts we covered:

- VPC architecture: global VPC, regional subnets, auto vs. custom mode
- Subnets: IP ranges, Private Google Access, secondary ranges for GKE
- Firewall rules: direction, priority, tag and SA targeting
- Routes: static and dynamic routing with Cloud Router
- VPC peering: non-transitive, no IP overlap, both sides required
- Shared VPC: host project / service project model for enterprise
- Cloud VPN: HA VPN for 99.99% SLA
- Cloud Interconnect: dedicated and partner for high-bandwidth connectivity
- Load balancing types: global, regional, external, internal, L4 vs. L7
- Cloud Armor: DDoS protection and WAF

The lab will have you create a custom VPC, configure firewall rules, deploy
VMs, and configure a load balancer.

---

End of Part 2 — Module 05

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/vpc/docs

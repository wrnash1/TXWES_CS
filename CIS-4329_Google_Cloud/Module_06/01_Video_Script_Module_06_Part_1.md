# Video Script — Module 06, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Load Balancing — Types, Architecture, and Backend Services

### Estimated Duration: 13–14 minutes

---

## Introduction

Welcome to Module 06. I'm Professor Nash, and today we cover Cloud Load Balancing and Cloud CDN. Load balancing is the mechanism that distributes user traffic across your fleet of backend servers, ensuring high availability and horizontal scalability. Cloud CDN accelerates delivery of static content by caching it at the network edge, close to your users.

These topics are consistently tested on the ACE exam. By the end of this module you will be able to choose the right load balancer for any scenario, understand the components of a Global HTTP(S) Load Balancer, configure health checks, and enable Cloud CDN.

---

## Section 1: Why Load Balancing?

**[SHOW SLIDE: Single server with users stacking up vs. load balancer distributing users across multiple servers]**

Without load balancing, all user requests go to one server. When that server gets overwhelmed, users experience slow responses and errors. When the server fails, your service goes down entirely.

Cloud Load Balancing solves this in three ways:

- Distribution: spreads incoming requests across multiple backend instances
- Health checking: continuously tests backends and stops sending traffic to unhealthy ones
- Scaling: works seamlessly with Managed Instance Groups to scale the backend fleet up and down

GCP's load balancers are fully managed. You do not provision load balancer VMs — Google manages the underlying infrastructure. You configure the load balancer's behavior through its components, which we will walk through now.

---

## Section 2: Load Balancer Types

**[SHOW SLIDE: Load balancer type comparison matrix — scope (global/regional), layer (4/7), traffic type (external/internal)]**

GCP has several load balancer types. The ACE exam tests your ability to select the right one for a scenario. The key selection dimensions are:

- Scope: global (single IP, routes to nearest backend worldwide) or regional (one region)
- Layer: Layer 7 (HTTP/HTTPS — application layer, can route by URL path) or Layer 4 (TCP/UDP — transport layer, IP and port only)
- Traffic direction: external (internet-facing) or internal (private VPC traffic only)

### Global External HTTP(S) Load Balancer

The most commonly tested load balancer on the ACE exam. Use when:

- You need a single global anycast IP address
- Users are distributed across multiple regions
- You need HTTPS termination at the load balancer (SSL offloading)
- You need URL-based routing (e.g., `/api` to one backend, `/static` to another)
- You want to enable Cloud CDN

This is an application layer (Layer 7) load balancer. It understands HTTP headers, cookies, and URLs.

### Regional External HTTP(S) Load Balancer

Similar to the global version but serves one region only. Does not provide a global anycast IP. Useful when compliance requirements demand that all traffic stay in one region.

### Regional External TCP/UDP Network Load Balancer

A Layer 4 load balancer that operates at the TCP/UDP protocol level. It does NOT understand HTTP. It distributes connections based on IP address and port. Use for non-HTTP protocols (gaming, MQTT, custom TCP protocols) or when you need to preserve the source IP address (HTTP load balancers do not preserve source IPs by default).

### Internal HTTP(S) Load Balancer

For private traffic between services inside a VPC. No public IP — only accessible from within the VPC or from connected networks (VPN, Interconnect). Use for microservices that communicate over HTTP/gRPC internally without any internet exposure.

### Internal TCP/UDP Load Balancer

For private TCP/UDP traffic inside a VPC. Use for internal non-HTTP services.

---

## Section 3: Global HTTP(S) Load Balancer Components

**[SHOW SLIDE: Architecture diagram — Frontend (global IP + forwarding rule + target proxy) → URL Map → Backend Service → Health Check → MIG backends]**

The Global HTTP(S) Load Balancer has several interconnected components. Understanding this architecture is essential for the ACE exam.

### Frontend Configuration

The frontend is what faces the internet. It consists of:

- Global external IP address (static anycast IP)
- Forwarding rule: maps the IP address + port to a target proxy
- Target proxy: for HTTPS, this is where the SSL certificate is configured; it decrypts incoming HTTPS traffic

### URL Map

The URL map is the routing brain. It maps URL paths to backend services. For example:

```text
/* (default) → web-backend-service
/api/* → api-backend-service
/static/* → static-backend-service
```

URL maps also support host-based routing (route `www.example.com` differently from `api.example.com`).

### Backend Service

A backend service defines:

- The backend group: which MIG (or NEG — Network Endpoint Group) receives traffic
- The health check: which HTTP path and port to probe for liveness
- Load balancing policy: how to distribute traffic (round robin, least connections, etc.)
- Session affinity: optional — pins a user to the same backend using cookie or IP hash
- CDN policy: optional — enables Cloud CDN caching

### Health Checks

Health checks run continuously from Google's probers. They send HTTP requests to the backend VMs and check for a success response (HTTP 200 by default). If a VM fails health checks for a configured number of consecutive attempts, the load balancer removes it from rotation. When it recovers, it is automatically added back.

**[PAUSE — Professor on camera]**

Here is a critical ACE exam point about health checks and firewall rules. Google's health check probers originate from two specific IP ranges: `35.191.0.0/16` and `130.211.0.0/22`. For health checks to work, your VPC firewall rules must allow ingress traffic from these two ranges to the health check port on your backend VMs. If you see a question about 502 errors or health checks failing, the answer is almost always: add the health check firewall rule allowing these source ranges.

---

## Section 4: SSL Certificates

**[SHOW SLIDE: SSL certificate options — Google-managed vs. self-managed]**

For HTTPS load balancers, you need an SSL certificate. GCP offers two options:

Google-managed SSL certificates: GCP automatically provisions, renews, and manages the certificate on your behalf. You just specify the domain name. Zero maintenance. This is the recommended approach for most use cases.

Self-managed (customer-provided) SSL certificates: you provide your own certificate and private key (e.g., from a commercial CA). You are responsible for renewal. Use this when you have an existing certificate or need to use a specific CA.

---

## Closing — Part 1

To summarize Part 1: GCP load balancers are selected based on scope (global vs. regional), layer (HTTP/HTTPS vs. TCP/UDP), and traffic direction (external vs. internal). The Global External HTTP(S) Load Balancer is the most important type for the ACE exam — it provides a single global anycast IP, HTTPS termination, URL-based routing, and Cloud CDN enablement. Its components are: frontend (IP + forwarding rule + target proxy), URL map, backend service, health check, and MIG backends. Health check firewall rules must allow traffic from `35.191.0.0/16` and `130.211.0.0/22`.

In Part 2 we will cover Cloud CDN, URL maps in depth, the gcloud commands for load balancer configuration, and the lab setup.

---

End of Part 1 — Module 06

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

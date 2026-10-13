# Video Script: Module 09 — Cloud Load Balancing and CDN (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction to Part 2

Welcome back. In Part 1 we built a Global HTTP(S) Load Balancer from scratch. In Part 2
we cover the remaining load balancer types — Network and Internal — then add Cloud CDN
and Cloud Armor to our architecture. We finish with the ACE exam selection framework.

---

### Section 1: External Network Load Balancer (Pass-Through)

The External Network Load Balancer operates at Layer 4 (transport layer). It is a
**pass-through** load balancer, meaning it does NOT terminate TCP/UDP connections.
Traffic passes directly to the backend instances, preserving the original client IP.

Key characteristics:

- **Regional** scope — backends must be in the same region
- **Protocol** — TCP, UDP, or other IP protocols (not HTTP-specific)
- **No SSL termination** — the backend handles TLS if needed
- **Preserves source IP** — the backend sees the real client IP address
- **Uses target pools or backend services** — older configurations use target pools;
  newer configurations use backend services with NEGs

```bash
# Create a target pool for Network LB (legacy method)
gcloud compute target-pools create my-target-pool \
  --region=us-central1 \
  --health-checks=my-tcp-health-check

# Add instances to the target pool
gcloud compute target-pools add-instances my-target-pool \
  --instances=web-vm-1,web-vm-2 \
  --instances-zone=us-central1-a

# Create a forwarding rule for the Network LB
gcloud compute forwarding-rules create my-network-lb \
  --region=us-central1 \
  --ports=80 \
  --target-pool=my-target-pool
```

#### When to Use Network LB

Use External Network LB when:

- You need to preserve the original client IP address
- You are load balancing non-HTTP protocols (e.g., game servers, custom TCP applications)
- You need ultra-low latency with no proxy overhead
- Regional scope is acceptable

---

### Section 2: Internal HTTP(S) Load Balancer

The Internal HTTP(S) Load Balancer serves traffic only within your VPC — no public
internet exposure. It operates at Layer 7 and supports URL-based routing, just like the
Global HTTP(S) LB.

Use cases:

- Microservices communication within a VPC
- Routing internal API traffic between services
- Service mesh architectures where services need smart routing

```bash
# Create an internal HTTP LB backend service
gcloud compute backend-services create my-internal-backend \
  --protocol=HTTP \
  --health-checks=my-http-health-check \
  --region=us-central1 \
  --load-balancing-scheme=INTERNAL_MANAGED

# Create an internal URL map
gcloud compute url-maps create my-internal-url-map \
  --default-service=my-internal-backend \
  --region=us-central1

# Create target HTTP proxy for internal LB
gcloud compute target-http-proxies create my-internal-proxy \
  --url-map=my-internal-url-map \
  --region=us-central1

# Create forwarding rule (internal — no global flag)
gcloud compute forwarding-rules create my-internal-lb-rule \
  --region=us-central1 \
  --load-balancing-scheme=INTERNAL_MANAGED \
  --network=my-vpc \
  --subnet=my-subnet \
  --target-http-proxy=my-internal-proxy \
  --target-http-proxy-region=us-central1 \
  --ports=80
```

---

### Section 3: Cloud CDN

Cloud CDN (Content Delivery Network) caches responses from your HTTP(S) Load Balancer
backends at Google's global edge Points of Presence (PoPs). Cached content is served
directly from the edge — reducing latency for end users and reducing load on your
backend instances.

#### Enabling Cloud CDN

Cloud CDN is enabled per backend service:

```bash
# Enable CDN on an existing backend service
gcloud compute backend-services update my-backend-service \
  --enable-cdn \
  --global

# Configure CDN cache mode
gcloud compute backend-services update my-backend-service \
  --cache-mode=CACHE_ALL_STATIC \
  --global
```

#### CDN Cache Modes

GCP offers three cache modes:

- **USE_ORIGIN_HEADERS** (default) — respects Cache-Control headers from the origin
- **CACHE_ALL_STATIC** — caches all static content regardless of Cache-Control
- **FORCE_CACHE_ALL** — caches all responses regardless of headers (use with caution)

#### Cache Invalidation

```bash
# Invalidate all cached content for a URL pattern
gcloud compute url-maps invalidate-cdn-cache my-url-map \
  --path="/*" \
  --global

# Invalidate a specific path
gcloud compute url-maps invalidate-cdn-cache my-url-map \
  --path="/images/logo.png" \
  --global
```

#### Signed URLs and Signed Cookies

For restricted content, Cloud CDN supports signed URLs and signed cookies. A signed URL
includes a cryptographic signature that restricts access to a specific URL for a limited
time. The signature is generated using a key you create:

```bash
# Create a Cloud CDN signing key
gcloud compute sign-url-keys create my-cdn-key \
  --key-file=cdn-key.bin \
  --backend-service=my-backend-service \
  --global
```

---

### Section 4: Cloud Armor

Cloud Armor is GCP's managed application-layer security service. It integrates directly
with the Global External HTTP(S) Load Balancer and provides:

- **DDoS protection** — adaptive protection against volumetric and application-layer
  DDoS attacks
- **WAF rules** — preconfigured rules based on OWASP Top 10 (SQL injection, XSS, etc.)
- **IP allow/deny lists** — block or allow specific IP ranges
- **Geo-based policies** — allow or deny traffic from specific countries

#### Creating a Cloud Armor Security Policy

```bash
# Create a security policy
gcloud compute security-policies create my-armor-policy \
  --description="Production WAF policy"

# Deny traffic from a specific IP range
gcloud compute security-policies rules create 1000 \
  --security-policy=my-armor-policy \
  --src-ip-ranges=192.0.2.0/24 \
  --action=deny-403

# Allow only traffic from specific countries (geo restriction)
gcloud compute security-policies rules create 2000 \
  --security-policy=my-armor-policy \
  --expression="origin.region_code == 'US' || origin.region_code == 'CA'" \
  --action=allow

# Default deny-all rule at lowest priority
gcloud compute security-policies rules create 2147483647 \
  --security-policy=my-armor-policy \
  --src-ip-ranges="*" \
  --action=deny-403

# Attach the security policy to a backend service
gcloud compute backend-services update my-backend-service \
  --security-policy=my-armor-policy \
  --global
```

Cloud Armor rules are evaluated in priority order — lower numbers are evaluated first.

---

### Section 5: ACE Exam — Load Balancer Selection Framework

Use this decision framework for exam scenarios:

| Requirement | Choose |
|---|---|
| Global HTTP/HTTPS, URL routing, CDN, WAF | Global External HTTP(S) LB |
| Regional HTTP/HTTPS, no global anycast needed | Regional External HTTP(S) LB |
| Non-HTTP TCP/UDP, preserve client IP, regional | External Network LB |
| Internal VPC microservices, HTTP routing | Internal HTTP(S) LB |
| Internal VPC TCP/UDP, no HTTP routing needed | Internal TCP/UDP LB |
| Non-HTTP TLS termination at global scale | External SSL Proxy LB |

Key exam rules:

- "Global" + "HTTPS" + "URL routing" = Global External HTTP(S) LB every time
- "Preserve client IP" = pass-through Network LB (not HTTP LB)
- "Internal" + "microservices" = Internal HTTP(S) LB
- Cloud CDN and Cloud Armor ONLY work with HTTP(S) Load Balancers — not TCP/UDP LBs

---

### Module 09 Summary

Module 09 covered the complete GCP load balancing portfolio:

- **Global HTTP(S) LB** — Layer 7, global anycast, URL routing, SSL termination, CDN,
  Cloud Armor
- **Network LB** — Layer 4, pass-through, preserves client IP, regional
- **Internal HTTP(S) LB** — Layer 7, VPC-internal, microservices routing
- **Cloud CDN** — edge caching integrated with HTTP(S) LB; three cache modes
- **Cloud Armor** — WAF and DDoS protection attached to backend services

For the ACE exam: know the component chain (forwarding rule → proxy → URL map → backend
service → health check), know which LB types are global vs. regional, and remember that
CDN and Armor only attach to HTTP(S) Load Balancers.

Complete the lab, take the quiz, and join the discussion. Module 10 covers Cloud
Operations — Monitoring, Logging, Trace, and Profiler.

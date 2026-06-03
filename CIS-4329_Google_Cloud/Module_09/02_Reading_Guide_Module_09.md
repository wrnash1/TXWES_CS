# Reading Guide: Module 09 — Cloud Load Balancing and CDN

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This reading guide accompanies the Module 09 video lectures. It covers the full GCP load
balancing portfolio, CDN caching, Cloud Armor security policies, and health check
configuration. Complete these readings before attempting the lab or quiz.

**Estimated reading time**: 60–75 minutes

---

### Learning Objectives

After completing this module's readings you will be able to:

- List all GCP load balancer types and their scope, protocol, and direction
- Describe the component chain of a Global External HTTP(S) Load Balancer
- Configure health checks, backend services, URL maps, and forwarding rules
- Explain SSL certificate types and the certificate provisioning process
- Enable Cloud CDN on a backend service and describe the three cache modes
- Create Cloud Armor security policies with IP-based and geo-based rules
- Select the correct load balancer type for a given ACE exam scenario

---

### Required Reading 1: Load Balancer Portfolio

**Source**: Google Cloud Documentation — Cloud Load Balancing Overview

**URL**: `https://cloud.google.com/load-balancing/docs/load-balancing-overview`

#### Load Balancer Portfolio Key Terms

- **Global load balancer**: Uses Google's global anycast network; a single IP routes
  users to the nearest healthy backend across all regions
- **Regional load balancer**: Backends restricted to a single region; lower cost but no
  global failover
- **Layer 7 (Application layer)**: Understands HTTP — can route based on URL path, host
  header, or HTTP method
- **Layer 4 (Transport layer)**: Routes based on IP address and port only; faster but
  no content-based routing
- **Pass-through**: The load balancer does not terminate the TCP connection; the backend
  sees the original client IP
- **Proxy-based**: The load balancer terminates the client connection and opens a new
  connection to the backend; backend sees the LB IP, not the client IP
- **Network Endpoint Group (NEG)**: A backend resource representing a set of IP:port
  endpoints; supports VMs, containers, serverless, and internet endpoints

#### Load Balancer Scope and Protocol Reference

| Load Balancer | Layer | Scope | Scheme | Proxy/Pass-Through |
|---|---|---|---|---|
| Global External HTTP(S) | 7 | Global | External | Proxy |
| Regional External HTTP(S) | 7 | Regional | External | Proxy |
| External SSL Proxy | 4 (SSL) | Global | External | Proxy |
| External TCP Proxy | 4 (TCP) | Global | External | Proxy |
| External Network (pass-through) | 4 | Regional | External | Pass-through |
| Internal HTTP(S) | 7 | Regional | Internal | Proxy |
| Internal TCP/UDP | 4 | Regional | Internal | Pass-through |

#### Load Balancer Portfolio ACE Exam Focus Points

- Only the Global External HTTP(S) LB supports Cloud CDN and Cloud Armor
- The External Network LB is pass-through — it preserves the original client IP
- Internal LBs are not accessible from the internet; they serve VPC-internal traffic only
- The Global HTTP(S) LB uses a single anycast IP — one IP works worldwide
- Regional HTTP(S) LB does not use anycast; it uses a regional IP

---

### Required Reading 2: Global HTTP(S) Load Balancer Components

**Source**: Google Cloud Documentation — Setting up a Global External HTTP Load Balancer

**URL**: `https://cloud.google.com/load-balancing/docs/https/setting-up-https`

#### HTTP(S) LB Component Chain

The Global HTTP(S) LB is assembled from five resource types in a chain:

```text
Internet → Forwarding Rule → Target Proxy → URL Map → Backend Service → Instance Group
```

#### Forwarding Rule

A forwarding rule binds a frontend IP address and port to a target proxy. It is the
entry point for all traffic. Attributes:

- IP address (static global IP or ephemeral)
- Port (typically 80 for HTTP, 443 for HTTPS)
- Protocol (HTTP, HTTPS, HTTP/2, gRPC)
- Target proxy reference

#### Target Proxy

The target proxy receives requests from the forwarding rule and consults the URL map.
Two types:

- `target-http-proxies` — for plaintext HTTP traffic
- `target-https-proxies` — for HTTPS; requires an SSL certificate reference

#### URL Map

The URL map defines routing rules. The default behavior sends all requests to the default
backend service. Path matchers can override the default for specific paths:

```yaml
# Conceptual URL map structure
defaultService: my-main-backend
hostRules:
  - hosts: ["api.example.com"]
    pathMatcher: api-matcher
pathMatchers:
  - name: api-matcher
    defaultService: my-api-backend
    pathRules:
      - paths: ["/v1/*"]
        service: my-v1-backend
      - paths: ["/v2/*"]
        service: my-v2-backend
```

#### Backend Service

A backend service defines:

- **Protocol** — HTTP, HTTPS, HTTP/2, gRPC
- **Health check** — how to determine if backends are healthy
- **Balancing mode** — `UTILIZATION` (CPU-based) or `RATE` (requests per second)
- **Capacity scaler** — scales down max capacity for gradual traffic shifting
- **Session affinity** — optional sticky sessions by client IP or cookie

#### Health Checks

Health checks probe backends on a configurable schedule. A backend is marked unhealthy
after `unhealthy-threshold` consecutive failures and healthy after `healthy-threshold`
consecutive successes.

```bash
# Create an HTTP health check
gcloud compute health-checks create http my-hc \
  --port=80 \
  --request-path=/healthz \
  --check-interval=10s \
  --timeout=5s \
  --healthy-threshold=2 \
  --unhealthy-threshold=3

# Create an HTTPS health check
gcloud compute health-checks create https my-https-hc \
  --port=443 \
  --request-path=/healthz
```

Health check traffic originates from GCP health check IP ranges: `35.191.0.0/16` and
`130.211.0.0/22`. Firewall rules must allow TCP on the health check port from these
ranges.

#### HTTP(S) LB ACE Exam Focus Points

- You cannot attach Cloud CDN or Cloud Armor to a Network LB — only to HTTP(S) LB
  backend services
- Health check firewall rules are required; missing them is a common setup mistake
- URL maps support both path-based and host-based routing
- A forwarding rule can only reference one target proxy; use separate forwarding rules
  for ports 80 and 443

---

### Required Reading 3: SSL Certificates

**Source**: Google Cloud Documentation — SSL Certificates Overview

**URL**: `https://cloud.google.com/load-balancing/docs/ssl-certificates`

#### SSL Certificate Key Terms

- **Google-managed certificate**: Provisioned and auto-renewed by GCP; only requires
  a domain name; DNS A record must point to the LB IP before provisioning begins
- **Self-managed certificate**: Customer uploads PEM-format certificate and private key;
  customer manages renewal
- **Certificate Manager**: Newer service supporting wildcard certs, certificate maps,
  and advanced rotation workflows
- **ACTIVE status**: Certificate is fully provisioned and serving; `PROVISIONING` means
  DNS has not yet resolved or certificate is pending issuance

#### SSL Certificate ACE Exam Focus Points

- Google-managed certs require DNS to already point at the LB IP — you cannot provision
  first and update DNS after
- Self-managed certs require the customer to track and replace expiring certificates
- Certificate provisioning typically takes 15–60 minutes after correct DNS propagation
- Wildcard certificates (`*.example.com`) require Certificate Manager, not the basic
  `ssl-certificates` resource

---

### Required Reading 4: Cloud CDN

**Source**: Google Cloud Documentation — Cloud CDN Overview

**URL**: `https://cloud.google.com/cdn/docs/overview`

#### Cloud CDN Key Terms

- **Cache hit**: Request served from Google edge PoP without forwarding to origin
- **Cache miss**: Request forwarded to origin backend; response cached for future requests
- **Cache key**: The URL components used to identify a unique cacheable response
- **TTL (Time To Live)**: How long a cached object remains valid before revalidation
- **Origin**: The Cloud Load Balancer backend that Cloud CDN caches responses from
- **PoP (Point of Presence)**: A Google edge location worldwide where cache is stored

#### CDN Cache Modes

- **USE_ORIGIN_HEADERS**: Respects `Cache-Control` and `Expires` headers from the
  backend; objects without these headers are not cached
- **CACHE_ALL_STATIC**: Caches all responses with static content types (CSS, JS, images,
  fonts) regardless of Cache-Control headers
- **FORCE_CACHE_ALL**: Caches all successful responses regardless of headers; overrides
  `Cache-Control: no-store`; use only for fully public content

#### Cloud CDN ACE Exam Focus Points

- Cloud CDN is enabled per backend service, not per URL map or forwarding rule
- Cache invalidation can target a single path or a wildcard pattern (`/*`)
- Signed URLs restrict access to CDN-served content for a specific time window
- CDN reduces origin load and latency but adds complexity for dynamic or personalized
  content that must not be cached

---

### Required Reading 5: Cloud Armor

**Source**: Google Cloud Documentation — Cloud Armor Overview

**URL**: `https://cloud.google.com/armor/docs/cloud-armor-overview`

#### Cloud Armor Key Terms

- **Security policy**: A set of rules evaluated in priority order (lower number = higher
  priority)
- **Rule**: Matches traffic by IP range, expression, or geo and applies an action
- **Action**: `allow`, `deny-403`, `deny-404`, `deny-502`, or `redirect`
- **Preconfigured WAF rules**: OWASP Top 10 rule sets (SQLi, XSS, LFI, RFI, etc.)
- **Adaptive Protection**: Machine-learning-based DDoS detection and auto-generated
  mitigation rules
- **Priority 2147483647**: The default rule at lowest priority; typically a catch-all
  deny or allow

#### Cloud Armor ACE Exam Focus Points

- Cloud Armor attaches to a backend service, not to a forwarding rule or URL map
- Lower priority number = evaluated first (priority 1000 is evaluated before 2000)
- Adaptive Protection is automatically enabled; no configuration required for basic DDoS
  protection
- Cloud Armor is ONLY compatible with Global External HTTP(S) LB and External SSL Proxy
  LB — not with Network LB or Internal LB

---

### Load Balancer Selection Summary

| ACE scenario phrase | Correct choice |
|---|---|
| "Global HTTPS with URL routing" | Global External HTTP(S) LB |
| "Preserve original client IP" | External Network LB (pass-through) |
| "DDoS protection and WAF" | Global HTTP(S) LB + Cloud Armor |
| "Cache static content at the edge" | Global HTTP(S) LB + Cloud CDN |
| "Internal microservices HTTP routing" | Internal HTTP(S) LB |
| "Non-HTTP TCP global proxy" | External TCP Proxy LB |

---

### Pre-Lab Checklist

Before starting Lab 09, confirm you can answer yes to each item:

- I can describe the five-component chain of a Global HTTP(S) Load Balancer
- I know the correct firewall IP ranges for health check traffic
- I understand the difference between Google-managed and self-managed SSL certificates
- I can explain the three Cloud CDN cache modes
- I understand that Cloud Armor rules use priority ordering (lower = evaluated first)

---

### Additional Resources

- Load balancing overview:
  `https://cloud.google.com/load-balancing/docs/load-balancing-overview`
- Cloud CDN docs:
  `https://cloud.google.com/cdn/docs`
- Cloud Armor docs:
  `https://cloud.google.com/armor/docs`
- ACE exam guide:
  `https://cloud.google.com/certification/guides/cloud-engineer`

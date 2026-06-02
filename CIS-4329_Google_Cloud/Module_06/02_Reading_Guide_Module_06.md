# Reading Guide — Module 06

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Load Balancing and Cloud CDN

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

Cloud Load Balancing and Cloud CDN are major ACE exam topics. This reading guide provides a comprehensive reference for load balancer types and selection, the component architecture of the Global HTTP(S) Load Balancer, health checks, Cloud CDN configuration, Cloud Armor, and the gcloud commands for building load balancer infrastructure. The exam tests both load balancer type selection (scenario-based) and configuration knowledge (health check firewall rules, URL maps, CDN requirements).

---

## 1. Load Balancer Type Comparison

### Selection Matrix

| Load Balancer | Scope | Layer | Traffic | Protocols | Key Use Case |
|---|---|---|---|---|---|
| Global External HTTP(S) LB | Global | 7 | External | HTTP, HTTPS, HTTP/2, gRPC | Global web apps, CDN, URL routing |
| Regional External HTTP(S) LB | Regional | 7 | External | HTTP, HTTPS | Single-region HTTPS with URL routing |
| Classic External HTTP(S) LB | Global | 7 | External | HTTP, HTTPS | Legacy; use Global External HTTP(S) for new deployments |
| External TCP/UDP Network LB | Regional | 4 | External | TCP, UDP | Non-HTTP protocols, source IP preservation |
| External SSL Proxy LB | Global | 4 | External | SSL/TLS | Non-HTTP SSL termination at global scale |
| External TCP Proxy LB | Global | 4 | External | TCP | Non-HTTP TCP at global scale |
| Internal HTTP(S) LB | Regional | 7 | Internal | HTTP, HTTPS, HTTP/2, gRPC | Internal microservices, east-west traffic |
| Internal TCP/UDP LB | Regional | 4 | Internal | TCP, UDP | Internal non-HTTP services |

### Key Selection Rules

Rule 1: HTTP/HTTPS with URL routing → HTTP(S) Load Balancer

Rule 2: Global users, single IP → Global External HTTP(S) LB

Rule 3: Non-HTTP protocols (gaming, MQTT, raw TCP) → TCP/UDP Network LB

Rule 4: Internal (private VPC) traffic → Internal LB

Rule 5: Cloud CDN required → must be Global External HTTP(S) LB

Rule 6: Source IP preservation needed → Network Load Balancer (Layer 4 pass-through)

---

## 2. Global HTTP(S) Load Balancer Architecture

### Component Overview

```text
Internet
    |
Forwarding Rule (IP + port)
    |
Target Proxy (SSL cert here for HTTPS)
    |
URL Map (host + path → backend service routing)
    |
Backend Service (health check + session affinity + CDN policy)
    |
Backend Group (MIG in a zone/region, or NEG)
    |
Individual VM instances
```

### Forwarding Rules

A forwarding rule maps a global external IP address and port to a target proxy. For HTTP, the port is 80. For HTTPS, the port is 443.

```bash
gcloud compute forwarding-rules create my-fwd-rule \
  --global \
  --target-http-proxy=my-proxy \
  --ports=80
```

### Target Proxies

| Proxy Type | Protocol | SSL Certificate Needed |
|---|---|---|
| target-http-proxy | HTTP | No |
| target-https-proxy | HTTPS | Yes |
| target-grpc-proxy | gRPC | Yes (HTTP/2) |

### URL Maps

URL maps define routing logic:

- Default backend: traffic that does not match any specific rule
- Host rules: match based on the HTTP `Host` header
- Path rules: for each host, match based on URL path prefixes

```bash
gcloud compute url-maps create my-url-map \
  --default-service=my-default-backend
```

Adding a path rule (route `/api` to a different backend):

```bash
gcloud compute url-maps add-path-matcher my-url-map \
  --path-matcher-name=api-paths \
  --default-service=default-backend \
  --backend-service-path-rules="/api/*=api-backend-service"
```

### Backend Services

Backend services define:

- The backend group (MIG or NEG)
- The associated health check
- The protocol (HTTP, HTTPS, HTTP/2)
- Session affinity settings (NONE, CLIENT_IP, GENERATED_COOKIE)
- Cloud CDN policy (enabled/disabled, cache mode)

### Network Endpoint Groups (NEGs)

NEGs are an alternative to MIGs as backends for the load balancer. Types:

- Zonal NEG: individual VM instances or container endpoints in a zone
- Serverless NEG: points to Cloud Run, App Engine, or Cloud Functions as a backend
- Internet NEG: points to external endpoints outside GCP (for hybrid load balancing)

For the ACE exam: when the scenario involves Cloud Run or App Engine as a backend for the load balancer, the answer is a Serverless NEG.

---

## 3. Health Checks

### Health Check Types

| Type | Protocol | Use When |
|---|---|---|
| HTTP | HTTP GET | Web servers returning HTTP responses |
| HTTPS | HTTPS GET | Encrypted backend responses |
| TCP | TCP connection | Non-HTTP services (just test TCP connectivity) |
| gRPC | gRPC | gRPC microservices |

### Health Check Parameters

| Parameter | Description | Default |
|---|---|---|
| Check interval | How often to probe | 10 seconds |
| Timeout | How long to wait for response | 5 seconds |
| Healthy threshold | Consecutive successes before marking healthy | 2 |
| Unhealthy threshold | Consecutive failures before marking unhealthy | 2 |

### Health Check Firewall Rule (Critical Exam Topic)

Google's health check probers originate from:

- `35.191.0.0/16`
- `130.211.0.0/22`

You must create an ingress firewall rule allowing TCP traffic from these ranges to the health check port on your backend VMs. Without this rule, the health check fails and no traffic is sent to the backend.

```bash
gcloud compute firewall-rules create allow-health-checks \
  --network=my-vpc \
  --action=ALLOW \
  --direction=INGRESS \
  --source-ranges=35.191.0.0/16,130.211.0.0/22 \
  --rules=tcp:80
```

---

## 4. Cloud CDN

### How Cloud CDN Works

1. User requests a resource (e.g., `/logo.png`)
2. Request hits the nearest Google edge PoP
3. If the response is in the CDN cache (cache hit): serve immediately from edge — fast
4. If not in cache (cache miss): forward to origin load balancer → backend VM → cache the response → return to user

### Cache Modes

| Mode | Behavior |
|---|---|
| CACHE_ALL_STATIC | Automatically caches responses with static content file extensions |
| USE_ORIGIN_HEADERS | Only caches responses with explicit `Cache-Control: public, max-age=N` headers |
| FORCE_CACHE_ALL | Caches all responses regardless of headers (use with caution) |

### Cache Key Configuration

By default, the full URL (including query string) is the cache key. You can customize:

- Exclude query string parameters that do not affect content (e.g., analytics tracking parameters)
- Include specific HTTP headers (e.g., `Accept-Language` for localization)
- Exclude specific cookies

### Cache Invalidation

Invalidate cached objects when content changes:

```bash
gcloud compute url-maps invalidate-cdn-cache my-url-map \
  --path="/static/*" \
  --host=www.example.com
```

### Signed URLs for Private CDN Content

To serve private content through CDN without public IAM access:

```bash
gcloud compute backend-services update my-backend \
  --signed-url-cache-max-age=3600 \
  --global
```

Then generate signed URLs using the CDN signing key — similar to Cloud Storage signed URLs.

---

## 5. Cloud Armor

Cloud Armor is GCP's WAF and DDoS protection service, attached to the Global HTTP(S) Load Balancer.

### Security Policy Rules

| Rule Type | Description |
|---|---|
| IP allowlist/blocklist | Allow or deny specific IP addresses or ranges |
| Geo-based filtering | Allow or deny by country/region |
| Preconfigured WAF rules | OWASP Top 10 protections (SQLi, XSS, etc.) |
| Adaptive protection | Machine learning DDoS detection and mitigation |
| Rate limiting | Throttle excessive requests from a single IP |

### Attaching a Security Policy

```bash
gcloud compute backend-services update my-backend-service \
  --security-policy=my-armor-policy \
  --global
```

For the ACE exam: Cloud Armor is the answer for DDoS protection, WAF rules, and geographic traffic filtering. It does NOT load balance traffic — it only filters it.

---

## 6. gcloud Load Balancing Command Reference

### Health Checks

| Command | Description |
|---|---|
| `gcloud compute health-checks create http NAME --port=80 --request-path=/health` | Create HTTP health check |
| `gcloud compute health-checks list` | List all health checks |
| `gcloud compute health-checks describe NAME` | View health check configuration |

### Backend Service gcloud Commands

| Command | Description |
|---|---|
| `gcloud compute backend-services create NAME --protocol=HTTP --health-checks=HC --global` | Create global backend service |
| `gcloud compute backend-services add-backend NAME --instance-group=MIG --instance-group-zone=Z --global` | Add MIG as backend |
| `gcloud compute backend-services update NAME --enable-cdn --global` | Enable Cloud CDN |
| `gcloud compute backend-services get-health NAME --global` | Check backend health status |

### URL Maps, Proxies, Forwarding Rules

| Command | Description |
|---|---|
| `gcloud compute url-maps create NAME --default-service=BACKEND` | Create URL map |
| `gcloud compute target-http-proxies create NAME --url-map=URL_MAP` | Create HTTP proxy |
| `gcloud compute target-https-proxies create NAME --url-map=URL_MAP --ssl-certificates=CERT` | Create HTTPS proxy |
| `gcloud compute forwarding-rules create NAME --global --target-http-proxy=PROXY --ports=80` | Create forwarding rule |
| `gcloud compute forwarding-rules list --global` | List global forwarding rules (shows IP) |

---

## 7. ACE Exam Tips

1. Global anycast IP + URL routing + CDN = Global External HTTP(S) Load Balancer. This combination is tested constantly. Nothing else provides all three.

2. Health check firewall rule is mandatory. Every question involving a broken health check or 502 errors with a healthy backend is about missing the `35.191.0.0/16` and `130.211.0.0/22` ingress rule.

3. Cloud CDN only works with Global HTTP(S) Load Balancer. If a question says "enable CDN for a TCP load balancer," that is not possible.

4. Internal load balancers have no public IP. If a scenario says "internal microservices communicating over HTTP," the answer is Internal HTTP(S) Load Balancer.

5. Network Load Balancer preserves source IP. HTTP(S) Load Balancers are proxy-based and do not preserve source IPs by default. When source IP preservation is a requirement, use Network LB.

6. Cloud Armor is a WAF, not a load balancer. It filters traffic; it does not distribute it. Always pair Cloud Armor with an HTTP(S) Load Balancer.

7. Serverless NEGs connect Cloud Run, App Engine, or Cloud Functions to a load balancer backend. This is the correct answer when the question involves serving serverless apps behind a load balancer with custom domain or CDN.

8. Session affinity (`GENERATED_COOKIE`) pins a user to the same backend VM for stateful applications. Use it when the application stores session state on the VM rather than in an external store.

---

## 8. Study Checklist

- [ ] Name each load balancer type and state when to use it (scope, layer, traffic direction)
- [ ] Draw the architecture of the Global HTTP(S) Load Balancer from memory with all components labeled
- [ ] State the two IP ranges that health check probers use and explain why firewall rules for them are required
- [ ] Explain what a URL map does and give an example of path-based routing
- [ ] Describe what Cloud CDN does and when it is appropriate
- [ ] Explain the three Cloud CDN cache modes
- [ ] Describe what Cloud Armor provides and how it attaches to a load balancer
- [ ] Build a Global HTTP(S) Load Balancer using gcloud (health check → backend service → URL map → target proxy → forwarding rule)
- [ ] Complete the Module 06 lab
- [ ] Take the Module 06 quiz
- [ ] Post your Module 06 discussion response

---

End of Reading Guide — Module 06

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

# Video Script — Module 06, Part 2

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud CDN, URL Maps, Cloud Armor, and gcloud Commands

### Estimated Duration: 10–12 minutes

---

## Introduction to Part 2

Welcome back to Module 06. In Part 1 we covered the types of load balancers and the architecture of the Global HTTP(S) Load Balancer. In Part 2 we cover Cloud CDN, URL maps in more depth, Cloud Armor for DDoS protection, and the gcloud commands you will use in the lab.

---

## Section 1: Cloud CDN

**[SHOW SLIDE: Map showing edge PoPs around the world with arrows showing content cached at edge instead of fetched from origin]**

Cloud CDN — Content Delivery Network — caches your web content at Google's global edge Points of Presence (PoPs). When a user in Tokyo requests your website, instead of the request traveling all the way to your origin servers in `us-central1`, Cloud CDN serves the cached response from a nearby PoP in Tokyo. This dramatically reduces latency for users far from your origin.

Cloud CDN integrates directly with the Global HTTP(S) Load Balancer — you simply enable it on the backend service with a checkbox or a single gcloud flag. There is no separate CDN infrastructure to manage.

### What Cloud CDN Caches

Cloud CDN caches HTTP responses that meet certain criteria:

- The response has a cache-control header with `public` and a `max-age` greater than zero
- The response status is 200, 203, 206, 300, 301, 302, 307, or 308
- The response is from a GET or HEAD request

Images, JavaScript files, CSS files, and other static assets are the primary use case. API responses that vary per user (authenticated, personalized) are NOT appropriate for CDN caching without careful cache key configuration.

### Cache Keys

By default, Cloud CDN uses the full request URL as the cache key. Two requests for the same URL from different users get the same cached response. You can customize cache keys to include or exclude specific HTTP headers, query string parameters, or cookies — this allows more fine-grained control over what is cached and what bypasses the cache.

### Cache Invalidation

When you update a static asset, users might still receive the old cached version from CDN edge nodes. You can either:

- Set short `max-age` values on responses so they expire quickly
- Use cache busting — append a version number to asset URLs (`/app.js?v=2024`)
- Manually invalidate the cache for specific paths using the Console or gcloud

```bash
gcloud compute url-maps invalidate-cdn-cache my-url-map \
  --path="/static/app.js" \
  --host=www.example.com
```

---

## Section 2: URL Maps — Routing Logic

**[SHOW SLIDE: URL map routing table with host rules and path rules]**

URL maps are the routing engine for the Global HTTP(S) Load Balancer. Let's look at their full capability.

A URL map has:

- Host rules: match based on the request `Host` header (e.g., `www.example.com` vs. `api.example.com`)
- Path rules: for each host, match based on URL path prefixes (e.g., `/api/v1/` vs. `/static/`)

Here is an example routing configuration:

```text
Host: www.example.com
  /static/* → static-backend-service (with CDN enabled)
  /api/*    → api-backend-service
  /*        → web-backend-service (default)

Host: admin.example.com
  /*        → admin-backend-service
```

This allows you to run multiple logical services behind a single load balancer IP address. The host rule differentiates between domains; the path rule differentiates between parts of a domain.

---

## Section 3: Cloud Armor

**[SHOW SLIDE: Cloud Armor positioned between internet and load balancer, filtering traffic]**

Cloud Armor is GCP's web application firewall (WAF) and DDoS protection service. It attaches to the Global External HTTP(S) Load Balancer's backend services as a security policy.

Cloud Armor can:

- Block traffic from specific IP addresses or IP ranges (for example, block a known attacker's IP)
- Allow traffic only from specific geographic regions (geo-blocking — block all traffic except from the US and EU)
- Apply OWASP Top 10 preconfigured WAF rules (SQL injection, cross-site scripting, etc.)
- Provide adaptive protection against large-scale DDoS attacks

For the ACE exam: Cloud Armor is the answer when a question asks about blocking DDoS attacks, implementing a WAF, or geo-restricting traffic. Cloud Armor is NOT a load balancer itself — it attaches to a load balancer backend service as a security policy layer.

```bash
gcloud compute security-policies create my-armor-policy \
  --description="Block malicious IPs"

gcloud compute security-policies rules create 1000 \
  --security-policy=my-armor-policy \
  --action=deny-404 \
  --src-ip-ranges=192.0.2.0/24

gcloud compute backend-services update my-backend \
  --security-policy=my-armor-policy \
  --global
```

---

## Section 4: gcloud Load Balancing Commands

**[SHOW CONSOLE: Cloud Shell with gcloud compute commands for load balancer setup]**

Creating a complete load balancer involves several gcloud commands. Here is the sequence:

Create a health check:

```bash
gcloud compute health-checks create http my-health-check \
  --port=80 \
  --request-path=/health
```

Create a backend service:

```bash
gcloud compute backend-services create my-backend-service \
  --protocol=HTTP \
  --port-name=http \
  --health-checks=my-health-check \
  --global
```

Add a MIG as a backend:

```bash
gcloud compute backend-services add-backend my-backend-service \
  --instance-group=my-mig \
  --instance-group-zone=us-central1-a \
  --global
```

Create a URL map:

```bash
gcloud compute url-maps create my-url-map \
  --default-service=my-backend-service
```

Create an HTTP target proxy:

```bash
gcloud compute target-http-proxies create my-http-proxy \
  --url-map=my-url-map
```

Create a forwarding rule (frontend):

```bash
gcloud compute forwarding-rules create my-forwarding-rule \
  --global \
  --target-http-proxy=my-http-proxy \
  --ports=80
```

List the load balancer's global forwarding rules to get the IP:

```bash
gcloud compute forwarding-rules list --global
```

Enable Cloud CDN on a backend service:

```bash
gcloud compute backend-services update my-backend-service \
  --enable-cdn \
  --global
```

---

## Module 06 Summary

**[SHOW SLIDE: Summary bullet list]**

Let's wrap up Module 06. GCP load balancers are chosen based on scope, layer, and traffic direction. The Global External HTTP(S) Load Balancer provides a single global anycast IP, HTTPS termination, URL-path routing, and integrates with Cloud CDN and Cloud Armor. Health checks require an ingress firewall rule from `35.191.0.0/16` and `130.211.0.0/22`. Components: frontend (IP + forwarding rule + target proxy), URL map, backend service, health check, and MIG backends.

Cloud CDN caches content at edge PoPs to reduce latency. URL maps route based on host and path rules. Cloud Armor provides WAF and DDoS protection as a security policy on backend services.

Key gcloud commands: `compute health-checks create`, `compute backend-services create`, `compute backend-services add-backend`, `compute url-maps create`, `compute target-http-proxies create`, `compute forwarding-rules create`.

Complete the lab, take the quiz, and post to the discussion. Module 07 covers Google Kubernetes Engine.

---

End of Part 2 — Module 06

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

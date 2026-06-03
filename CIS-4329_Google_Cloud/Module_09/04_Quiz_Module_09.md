# Quiz: Module 09 — Cloud Load Balancing and CDN

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A web application serves users worldwide. The team wants a single IP address that routes
users to the nearest healthy backend, with support for URL-based routing, SSL termination,
and Cloud CDN integration. Which load balancer should they use?

- A) External Network Load Balancer
- B) Global External HTTP(S) Load Balancer
- C) Regional External HTTP(S) Load Balancer
- D) Internal HTTP(S) Load Balancer

Correct answer: B — The Global External HTTP(S) Load Balancer is the only GCP load
balancer offering global anycast routing, URL-based routing, SSL termination at the load
balancer, and native Cloud CDN integration. The Network LB is Layer 4 pass-through with
no CDN. The Regional HTTP(S) LB is single-region. The Internal LB does not serve internet
traffic.

---

### Question 2

An application requires that backend servers receive the original client IP address in the
TCP connection. SSL termination occurs on the backend servers, not on the load balancer.
The application is regional. Which load balancer best fits these requirements?

- A) Global External HTTP(S) Load Balancer
- B) External SSL Proxy Load Balancer
- C) External Network Load Balancer (pass-through)
- D) Internal TCP/UDP Load Balancer

Correct answer: C — The External Network Load Balancer is a pass-through, Layer 4 load
balancer that preserves the original client IP address. It does not terminate SSL — the
backend handles TLS. It is regional, matching the requirement. The HTTP(S) LB and SSL
Proxy LB are both proxy-based and terminate the connection at the load balancer.

---

### Question 3

What is the correct order of the Global HTTP(S) Load Balancer component chain, from
internet to backend?

- A) Forwarding Rule → Backend Service → URL Map → Target Proxy → Instance Group
- B) Target Proxy → Forwarding Rule → URL Map → Backend Service → Instance Group
- C) Forwarding Rule → Target Proxy → URL Map → Backend Service → Instance Group
- D) URL Map → Forwarding Rule → Target Proxy → Backend Service → Instance Group

Correct answer: C — The correct chain is: Forwarding Rule (receives traffic from the
internet) → Target Proxy (HTTP or HTTPS proxy that reads the URL map) → URL Map (routes
to the correct backend service) → Backend Service (references instance groups and health
checks) → Instance Group (the actual backend VMs).

---

### Question 4

You are setting up an HTTP health check for a Global HTTP(S) Load Balancer. After
configuring the health check and backend service, the backends show as unhealthy even
though the web servers are responding correctly. What is the most likely cause?

- A) The health check path returns HTTP 200 instead of HTTP 204
- B) The firewall rules do not allow TCP traffic from GCP health check IP ranges
- C) The backend service protocol is set to HTTPS instead of HTTP
- D) The URL map is not referencing the backend service

Correct answer: B — Health check probes originate from `35.191.0.0/16` and
`130.211.0.0/22`. If firewall rules do not permit TCP traffic from these ranges to the
backend instances on the health check port, all probes fail and backends appear unhealthy.
This is the most common health check configuration mistake.

---

### Question 5

A team wants to use a Google-managed SSL certificate on their Global HTTPS Load Balancer.
They have created the certificate resource but the status shows `PROVISIONING` for over
two hours. What is the most likely cause?

- A) The SSL certificate was not attached to the target HTTPS proxy
- B) The forwarding rule is using port 80 instead of port 443
- C) The domain's DNS A record does not point to the load balancer's IP address
- D) Google-managed certificates require manual approval before provisioning

Correct answer: C — Google-managed SSL certificates require the domain's DNS A record to
resolve to the load balancer's IP address before certificate issuance can begin. If DNS
has not been updated or has not yet propagated, the certificate remains in `PROVISIONING`
status. There is no manual approval step — provisioning is fully automated once DNS is
correct.

---

### Question 6

Which of the following Cloud CDN cache modes caches responses regardless of the
`Cache-Control` headers returned by the backend?

- A) USE_ORIGIN_HEADERS
- B) CACHE_ALL_STATIC
- C) FORCE_CACHE_ALL
- D) ALWAYS_CACHE

Correct answer: C — `FORCE_CACHE_ALL` caches all successful responses from the origin
regardless of their `Cache-Control` headers, including responses with
`Cache-Control: no-store`. `USE_ORIGIN_HEADERS` respects the origin's cache headers.
`CACHE_ALL_STATIC` caches static content types but still respects no-cache directives
on dynamic content. `ALWAYS_CACHE` is not a valid GCP cache mode name.

---

### Question 7

You need to protect a Global HTTP(S) Load Balancer from SQL injection attacks and block
traffic originating from a specific country. Which service provides both capabilities?

- A) Cloud Firewall policies
- B) Cloud Armor
- C) Cloud NAT
- D) VPC Service Controls

Correct answer: B — Cloud Armor provides preconfigured WAF rules for OWASP Top 10
attacks (including SQL injection) and supports geo-based rule expressions to block
traffic from specific countries. Cloud Armor attaches directly to backend services on the
Global HTTP(S) LB. VPC Service Controls, Cloud Firewall policies, and Cloud NAT do not
provide application-layer WAF or CDN-integrated geo blocking.

---

### Question 8

In a Cloud Armor security policy, two rules are configured: rule priority 500 allows
traffic from `10.0.0.0/8`, and rule priority 1000 denies all traffic. A request arrives
from `10.1.2.3`. What action is taken?

- A) The request is denied because the deny rule exists in the policy
- B) The request is allowed because priority 500 is evaluated first and it matches
- C) The request is denied because the deny rule has a broader match
- D) No rule matches so the default GCP behavior allows the request

Correct answer: B — Cloud Armor evaluates rules in priority order from lowest to highest
number. Priority 500 is evaluated before priority 1000. The request from `10.1.2.3`
matches the `10.0.0.0/8` range at priority 500, so the allow action is applied and
evaluation stops. The deny rule at priority 1000 is never reached.

---

### Question 9

Which GCP load balancer type is required to route internal microservice traffic within a
VPC using HTTP path-based routing rules?

- A) External Network Load Balancer
- B) Global External HTTP(S) Load Balancer
- C) Internal HTTP(S) Load Balancer
- D) Internal TCP/UDP Load Balancer

Correct answer: C — The Internal HTTP(S) Load Balancer is a regional, VPC-internal Layer
7 load balancer that supports URL path-based and host-based routing for microservices
within a VPC. The External Network LB and Global External HTTP(S) LB face the public
internet. The Internal TCP/UDP LB is Layer 4 and does not support path-based routing.

---

### Question 10

A team wants to invalidate all CDN-cached content for their application after deploying
a new version. Which gcloud command accomplishes this?

- A) `gcloud compute backend-services update --clear-cdn-cache`
- B) `gcloud compute url-maps invalidate-cdn-cache MY_URL_MAP --path="/*" --global`
- C) `gcloud cdn cache invalidate --all --backend-service=MY_BACKEND`
- D) `gcloud compute forwarding-rules delete --cdn-cache MY_RULE`

Correct answer: B — `gcloud compute url-maps invalidate-cdn-cache` is the correct
command for cache invalidation. The `--path="/*"` wildcard pattern invalidates all
cached content. Options A, C, and D use incorrect command structures that do not exist
in the gcloud CLI.

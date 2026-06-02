# Quiz — Module 06

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Load Balancing and Cloud CDN

### 10 Questions | 10 Points Each | Total: 100 Points

---

## Question 1

Your company runs a web application that serves users across North America, Europe, and Asia. You need a single global IP address that routes users to the nearest healthy backend automatically, supports HTTPS termination, and can route `/api` requests to one set of VMs and `/static` requests to another. Which load balancer type is correct?

A. Regional TCP/UDP Network Load Balancer

B. Internal HTTP(S) Load Balancer

C. Global External HTTP(S) Load Balancer

D. Regional External HTTP(S) Load Balancer

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: A TCP/UDP Network Load Balancer operates at Layer 4 and cannot perform URL-based routing, HTTPS termination, or global anycast distribution.
- Why B is incorrect: The Internal HTTP(S) Load Balancer is for private traffic between services inside a VPC — it does not have a public IP and cannot serve external users.
- Why D is incorrect: A Regional External HTTP(S) Load Balancer serves one region only and cannot provide a single global IP that routes users across continents to the nearest backend.

---

## Question 2

You have configured a Global HTTP(S) Load Balancer with a Managed Instance Group backend. Users report intermittent 502 errors. You check the load balancer logs and see that the health check is failing. Which firewall rule is most likely missing?

A. An egress rule allowing the VMs to send health check responses to Google's servers.

B. An ingress rule allowing TCP traffic from `35.191.0.0/16` and `130.211.0.0/22` to reach the backend VMs on the health check port.

C. An ingress rule allowing all internet traffic to port 80 on the backend VMs.

D. A rule allowing the load balancer's frontend IP to communicate with the backend VMs directly.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: GCP firewall rules are stateful — if the inbound health check probe is allowed, the outbound response is automatically permitted without a separate egress rule.
- Why C is incorrect: Opening port 80 to all internet traffic is overly broad and not required for health checks; only the specific Google health check probe ranges need access to the health check port.
- Why D is incorrect: The Global HTTP(S) Load Balancer is a distributed proxy — there is no single load balancer frontend IP that connects to backends. Health check traffic originates from Google's dedicated health check IP ranges, not from a frontend IP.

---

## Question 3

Your application serves a large number of static images and JavaScript files that rarely change. Users worldwide are reporting slow page load times. You already have a Global HTTP(S) Load Balancer in place. Which feature can you enable to reduce latency and origin server load with minimal configuration changes?

A. Enable session affinity on the backend service to pin users to the same VM.

B. Add a second backend MIG in each region to handle local traffic.

C. Enable Cloud CDN on the backend service to cache static content at Google's edge nodes.

D. Switch to a Network Load Balancer, which has lower latency than the HTTP(S) Load Balancer.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Session affinity routes the same user to the same backend VM to preserve state — it does not cache content at the edge or reduce global latency for static assets.
- Why B is incorrect: Adding more MIGs increases backend capacity and reduces regional load, but users still retrieve content from your origin servers; it does not cache content at the network edge close to users.
- Why D is incorrect: Network Load Balancers operate at Layer 4 and have no concept of HTTP caching; Cloud CDN only works with the Global HTTP(S) Load Balancer, making a switch away counterproductive.

---

## Question 4

You need to load balance internal traffic between a set of microservices running on Compute Engine VMs within the same VPC. The microservices communicate using HTTP/2 (gRPC). No public IP addresses should be involved. Which load balancer type is correct?

A. Global External HTTP(S) Load Balancer with an SSL certificate

B. Regional External TCP/UDP Network Load Balancer

C. Internal HTTP(S) Load Balancer

D. Cloud Armor policy attached to an internal backend service

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: The Global External HTTP(S) Load Balancer has a public IP and is designed for external internet traffic — it is not appropriate for internal VPC microservice traffic with no public exposure.
- Why B is incorrect: The Regional External TCP/UDP Network Load Balancer also has a public-facing frontend and is designed for external traffic; it does not provide an internal-only load balancing endpoint.
- Why D is incorrect: Cloud Armor is a web application firewall layer that attaches to load balancers for DDoS protection and rule-based filtering — it is not a load balancer itself and cannot distribute traffic.

---

## Question 5

A backend VM in your HTTP(S) Load Balancer's Managed Instance Group is receiving traffic even though its application has crashed and it is returning HTTP 500 errors. What configuration change will cause the load balancer to stop sending traffic to this unhealthy instance?

A. Add a Cloud Armor security policy to block 5xx responses from reaching users.

B. Configure a URL map rule to redirect `/error` paths away from the broken instance.

C. Configure an HTTP health check on the backend service that checks for HTTP 200 responses, so the failing VM is automatically marked unhealthy and removed from rotation.

D. Enable Cloud CDN caching so that previously cached 200 responses are served instead of the live 500 errors.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Cloud Armor security policies filter incoming requests based on IP addresses, geo-location, and request attributes — they do not inspect backend response codes or control which backend VMs receive traffic.
- Why B is incorrect: URL map rules route traffic based on request path patterns — they do not monitor backend health or dynamically reroute traffic based on runtime errors from a specific VM.
- Why D is incorrect: Cloud CDN caches successful responses but does not serve stale cached content instead of live backend errors when the backend is still reachable but returning 5xx; health checks are the correct mechanism for removing failed instances from rotation.

---

## Question 6

You are designing a load balancer architecture for a new SaaS platform. The platform must serve traffic from a single global IP address, route requests for `app.example.com/api` to one set of VMs and `app.example.com/static` to a CDN-enabled backend, and protect against SQL injection attacks. Which combination of GCP services meets all three requirements?

A. Regional External HTTP(S) Load Balancer, URL map with path rules, VPC firewall rules

B. Global External HTTP(S) Load Balancer, URL map with path rules, Cloud Armor WAF policy

C. External TCP Proxy Load Balancer, URL map with host rules, Cloud Armor security policy

D. Global External HTTP(S) Load Balancer, Cloud CDN on all backends, Identity-Aware Proxy

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: A Regional External HTTP(S) Load Balancer does not provide a global anycast IP, which is a stated requirement. VPC firewall rules cannot perform SQL injection detection; that requires Cloud Armor's preconfigured WAF rules.
- Why C is incorrect: The External TCP Proxy Load Balancer operates at Layer 4 and does not understand HTTP paths, so URL map path-based routing is not supported. SQL injection protection requires a Layer 7 WAF.
- Why D is incorrect: Identity-Aware Proxy (IAP) provides authentication and access control for internal users — it does not provide SQL injection protection. Cloud Armor is the WAF service for OWASP Top 10 protections.

---

## Question 7

Which Cloud CDN cache mode causes CDN to cache responses only when the origin server explicitly includes a `Cache-Control: public, max-age=N` header in the response?

A. FORCE_CACHE_ALL

B. CACHE_ALL_STATIC

C. USE_ORIGIN_HEADERS

D. BYPASS_CACHE

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: `FORCE_CACHE_ALL` caches all cacheable responses regardless of origin headers — it overrides the origin's cache-control directives and caches responses that might not normally be cached. This is the aggressive mode, not the header-respecting mode.
- Why B is incorrect: `CACHE_ALL_STATIC` automatically caches responses with static content file extensions (`.jpg`, `.css`, `.js`, etc.) regardless of cache-control headers. It does not require the origin to send explicit cache headers.
- Why D is incorrect: `BYPASS_CACHE` is not a valid Cloud CDN cache mode. The three valid modes are `USE_ORIGIN_HEADERS`, `CACHE_ALL_STATIC`, and `FORCE_CACHE_ALL`.

---

## Question 8

Your company's security team requires DDoS protection and the ability to block traffic from specific countries on your public web application. The application runs behind a Global HTTP(S) Load Balancer. Which GCP service provides both of these capabilities?

A. VPC firewall rules with geo-based IP range blocklists

B. Cloud Armor security policies with geo-based filtering and adaptive protection

C. Private Google Access with allowlists for approved country IP ranges

D. Identity-Aware Proxy with conditional access policies based on user location

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: VPC firewall rules operate on IP addresses and ranges but do not natively understand geographic regions. Maintaining country-level IP blocklists manually is operationally impractical and does not provide DDoS adaptive protection.
- Why C is incorrect: Private Google Access enables VMs without external IPs to reach Google APIs — it is a routing feature, not a security policy service, and provides no traffic filtering or DDoS protection.
- Why D is incorrect: Identity-Aware Proxy controls access to applications based on authenticated user identity and can use access levels, but it is not a WAF or DDoS protection service. It does not inspect traffic at the network level for attack patterns.

---

## Question 9

You need to connect a Cloud Run service as a backend to a Global HTTP(S) Load Balancer so that it can be served at a custom domain with Cloud CDN enabled. What type of backend must you use?

A. A Managed Instance Group in the region where Cloud Run is deployed

B. A Zonal Network Endpoint Group pointing to the Cloud Run service's internal IP

C. A Serverless Network Endpoint Group pointing to the Cloud Run service

D. A backend bucket pointing to the Cloud Run service URL as an origin

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: A Managed Instance Group contains Compute Engine VM instances — it cannot represent a serverless Cloud Run service. Cloud Run is not a VM and does not run inside a MIG.
- Why B is incorrect: A Zonal NEG points to individual VM instances or container endpoints in a specific zone — it does not support Cloud Run, which is a serverless service without a fixed IP address.
- Why D is incorrect: A backend bucket points to a Cloud Storage bucket for static content serving. It is not designed to proxy requests to a Cloud Run service URL.

---

## Question 10

A developer runs the complete sequence of gcloud commands to create a Global HTTP(S) Load Balancer. The forwarding rule is created and the external IP is assigned. After 5 minutes, curl requests to the load balancer IP return HTTP 200 responses from the backend VMs. The developer then deletes the health check firewall rule. What happens next?

A. The load balancer immediately begins returning 503 Service Unavailable to all users.

B. Health check probes begin failing; after the unhealthy threshold of consecutive failures is reached, backends are marked unhealthy and traffic stops being served.

C. Nothing changes — the load balancer cached the last known healthy state and continues routing traffic indefinitely.

D. The load balancer automatically creates a replacement firewall rule to restore health check connectivity.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: The transition from healthy to unhealthy is not instantaneous. The health check must fail a configurable number of consecutive times (the unhealthy threshold, default 2) before a backend is marked unhealthy and removed from rotation. There is a delay measured in seconds to minutes depending on the check interval.
- Why C is incorrect: GCP load balancers do not cache health state indefinitely. Health checks run continuously on the configured interval. If probes cannot reach the backend VMs due to a missing firewall rule, the check fails and the backend health state degrades on the next check cycle.
- Why D is incorrect: GCP does not automatically modify firewall rules in response to health check failures. The responsibility for maintaining the correct firewall rules belongs to the operator. GCP's health check system reports the failure but does not self-heal the firewall configuration.

---

End of Quiz — Module 06

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

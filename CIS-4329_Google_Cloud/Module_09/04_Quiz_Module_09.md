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

---

### Question 11 (5 points)

A backend service behind a Global HTTP(S) Load Balancer has a health check configured
on port 80. The firewall policy allows traffic on port 80 from all sources, yet the
backends still show UNHEALTHY. What is missing?

- A) The health check must use port 443 for HTTPS backends
- B) A firewall rule allowing TCP traffic from `35.191.0.0/16` and `130.211.0.0/22`
   to the backend instances on port 80 is missing
- C) The URL map must explicitly list the health check path
- D) The backend service must be set to `INTERNAL` to use health checks

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Port 80 is valid for HTTP health checks; the protocol must match what the backend serves, not the external certificate configuration.
  - C) URL maps route traffic to backend services; they do not reference health check paths — that is configured on the health check resource itself.
  - D) Health checks apply to both external and internal backend services; there is no requirement to set the backend service to INTERNAL to enable health checks.

---

### Question 12 (5 points)

Which Cloud CDN cache mode causes Cloud CDN to cache only responses that the origin
explicitly marks as cacheable via `Cache-Control` or `Expires` headers?

- A) `FORCE_CACHE_ALL`
- B) `CACHE_ALL_STATIC`
- C) `USE_ORIGIN_HEADERS`
- D) `CACHE_DYNAMIC`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `FORCE_CACHE_ALL` overrides origin headers and caches everything, including responses marked `no-store`; it is the most aggressive mode.
  - B) `CACHE_ALL_STATIC` caches content with static MIME types (images, CSS, JS) regardless of `Cache-Control` headers but does not require the origin to mark responses cacheable.
  - D) `CACHE_DYNAMIC` is not a valid Cloud CDN cache mode name.

---

### Question 13 (5 points)

You need to attach a Cloud Armor security policy to your load balancer architecture.
At which component in the load balancer chain is the security policy attached?

- A) Forwarding rule
- B) Target HTTPS proxy
- C) URL map
- D) Backend service

- **Correct Answer:** D
- **Distractor Analysis:**
  - A) Forwarding rules receive traffic from the internet and route it to a target proxy; they have no security policy attachment point.
  - B) Target HTTPS proxies hold SSL certificate references and the URL map reference; they do not accept Cloud Armor security policies.
  - C) URL maps define routing logic from host/path patterns to backend services; Cloud Armor is applied at the backend service level, not the routing layer.

---

### Question 14 (5 points)

A team uses an External Network Load Balancer. They realize their backends are receiving
traffic from Google's load balancer IP addresses instead of the original client IPs.
Why does this happen with some configurations, and what load balancer type preserves
the original client IP without proxy rewrites?

- A) All load balancers proxy connections and rewrite source IPs; client IP is never
   preserved
- B) Proxy-based load balancers (HTTP(S), SSL Proxy, TCP Proxy) terminate the
   connection and originate a new one; a pass-through Network LB preserves the
   original client IP
- C) The External Network LB always rewrites the source IP; Internal LB preserves it
- D) Only Internal HTTP(S) LB preserves the original client IP

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Pass-through load balancers such as the External Network LB do not terminate connections and therefore preserve the original client IP at the TCP layer.
  - C) The External Network LB is a pass-through load balancer that does NOT rewrite the source IP; backends receive the original client IP directly.
  - D) The Internal HTTP(S) LB is a proxy-based Layer 7 load balancer; it terminates connections and the backend sees the load balancer's IP, not the original client.

---

### Question 15 (5 points)

You configure an HTTPS load balancer with a Google-managed SSL certificate for
`www.example.com`. After 24 hours the certificate is still in `PROVISIONING` state.
Which action is most likely to resolve this?

- A) Delete and recreate the certificate resource
- B) Verify that the DNS A record for `www.example.com` points to the forwarding
   rule's reserved static IP address
- C) Switch from a Google-managed certificate to a self-managed certificate
- D) Increase the backend service timeout to allow certificate provisioning to complete

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Recreating the certificate will not help if the underlying DNS misconfiguration is not fixed; the new certificate will also remain in `PROVISIONING`.
  - C) Switching to a self-managed certificate is a workaround, not a resolution; the root cause (DNS not pointing to the LB IP) must be addressed regardless of certificate type.
  - D) Backend service timeout controls the maximum time the load balancer waits for a backend response; it has no effect on SSL certificate provisioning.

---

### Question 16 (5 points)

A Cloud Armor security policy has three rules: priority 100 allows `10.0.0.0/8`,
priority 200 denies `10.5.0.0/16`, and priority 2147483647 is the default allow.
A request arrives from `10.5.1.1`. What is the outcome?

- A) The request is allowed because priority 100 matches and evaluation stops there
- B) The request is denied because priority 200 matches `10.5.1.1` and evaluation
   stops
- C) The request is allowed because the default rule at priority 2147483647 is the
   final authority
- D) The request is denied because the deny rule always overrides allow rules

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Although `10.5.1.1` is within the `10.5.0.0/16` range at priority 200, evaluation starts at the lowest priority number (100). The request matches `10.0.0.0/8` at priority 100 first, and evaluation stops at that allow action.
  - C) The default rule at priority 2147483647 is only evaluated if no earlier rule matches; since priority 100 matches, the default is never reached.
  - D) Cloud Armor does not give deny rules automatic precedence over allow rules; rules are evaluated strictly in priority order.

---

### Question 17 (5 points)

Which statement correctly describes the difference between a Global External HTTP(S)
Load Balancer and a Regional External HTTP(S) Load Balancer?

- A) The regional LB supports Cloud CDN; the global LB does not
- B) The global LB uses Google's anycast network with a single global IP; the
   regional LB serves a single region and does not support global anycast
- C) The regional LB supports URL-based routing; the global LB does not
- D) The global LB requires Cloud Armor; the regional LB does not

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud CDN integration is only available with the Global External HTTP(S) Load Balancer, not the regional variant.
  - C) Both the global and regional HTTP(S) load balancers support URL-based routing via URL maps; this is not a distinguishing feature.
  - D) Cloud Armor is optional on the global LB; it is not required and cannot be attached to the regional HTTP(S) LB at all.

---

### Question 18 (5 points)

A team needs to distribute TCP traffic (non-HTTP) to global backend pools with SSL
termination at the load balancer. Which load balancer type should they use?

- A) Global External HTTP(S) Load Balancer
- B) External TCP Proxy Load Balancer
- C) External Network Load Balancer
- D) Internal TCP/UDP Load Balancer

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The HTTP(S) Load Balancer handles HTTP and HTTPS (Layer 7) traffic only; it is not designed for generic TCP protocols.
  - C) The External Network Load Balancer is a pass-through Layer 4 load balancer; it does NOT terminate SSL — SSL termination happens on the backend, not the load balancer.
  - D) The Internal TCP/UDP Load Balancer is regional and VPC-internal; it cannot serve traffic from the public internet or provide global distribution.

---

### Question 19 (5 points)

What is the purpose of a named port on a GKE node port or managed instance group
when used with a load balancer backend service?

- A) Named ports enable the load balancer to route traffic to specific named
   containers inside a pod
- B) Named ports provide a symbolic name that maps the backend service's port to
   the actual port on each instance in the group, decoupling configuration from
   port numbers
- C) Named ports are required to enable SSL on a backend service
- D) Named ports restrict traffic to instances that have the named port explicitly
   opened in their firewall rules

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Named ports on instance groups are a compute-level concept; they do not route to containers inside a pod — that is a Kubernetes service/ingress concern.
  - C) SSL on a backend service is configured via the backend service protocol (HTTPS) and SSL certificates; named ports have no role in enabling SSL.
  - D) Firewall rules control which traffic reaches instances based on tags and IP ranges, not named port definitions on instance groups.

---

### Question 20 (5 points)

You want to route requests with the URL path `/api/*` to one backend service and all
other requests to a default backend service. Which load balancer component implements
this path-based routing logic?

- A) Forwarding rule
- B) Target HTTP proxy
- C) URL map
- D) Backend service

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Forwarding rules match on IP address, port, and protocol and direct traffic to a target proxy; they do not inspect URL paths.
  - B) Target HTTP proxies receive requests from the forwarding rule and reference a URL map; they delegate routing decisions to the URL map, not perform the routing themselves.
  - D) Backend services define the set of backends (instance groups, NEGs) and health check behavior; routing logic that determines which backend service receives a request lives in the URL map.

# Quiz: Module 06 – Cloud Load Balancing and Cloud CDN
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your company runs a web application that serves users across North America, Europe, and Asia. You need a single global IP address that routes users to the nearest healthy backend automatically, supports HTTPS termination, and can route `/api` requests to one set of VMs and `/static` requests to another. Which load balancer type is correct?

A) Regional TCP/UDP Network Load Balancer
B) Internal HTTP(S) Load Balancer
C) Global External HTTP(S) Load Balancer
D) Regional External HTTP(S) Load Balancer

*   **Correct Answer:** C) Global External HTTP(S) Load Balancer
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A TCP/UDP Network Load Balancer operates at Layer 4 and cannot perform URL-based routing, HTTPS termination, or global anycast distribution.
    *   *Why B is incorrect:* The Internal HTTP(S) Load Balancer is for private traffic between services inside a VPC — it does not have a public IP and cannot serve external users.
    *   *Why D is incorrect:* A Regional External HTTP(S) Load Balancer serves one region only and cannot provide a single global IP that routes users across continents to the nearest backend.

---

**Question 2**
You have configured a Global HTTP(S) Load Balancer with a Managed Instance Group backend. Users report intermittent 502 errors. You check the load balancer logs and see that the health check is failing. Which firewall rule is most likely missing?

A) An egress rule allowing the VMs to send health check responses to Google's servers.
B) An ingress rule allowing TCP traffic from Google's health check IP ranges (`35.191.0.0/16` and `130.211.0.0/22`) to reach the backend VMs on the health check port.
C) An ingress rule allowing all internet traffic to port 80 on the backend VMs.
D) A rule allowing the load balancer's frontend IP to communicate with the backend VMs directly.

*   **Correct Answer:** B) An ingress rule allowing TCP traffic from Google's health check IP ranges (`35.191.0.0/16` and `130.211.0.0/22`) to reach the backend VMs on the health check port.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GCP firewall rules are stateful — if the inbound health check probe is allowed, the outbound response is automatically permitted without a separate egress rule.
    *   *Why C is incorrect:* Opening port 80 to all internet traffic is overly broad and not required for health checks; only the specific Google health check probe ranges need access to the health check port.
    *   *Why D is incorrect:* Global HTTP(S) Load Balancer is a distributed proxy — there is no single load balancer IP that connects to backends. Health check traffic originates from Google's dedicated health check IP ranges, not from a frontend IP.

---

**Question 3**
Your application serves a large number of static images and JavaScript files that rarely change. Users worldwide are reporting slow page load times. You already have a Global HTTP(S) Load Balancer in place. Which feature can you enable to reduce latency and origin server load with minimal configuration changes?

A) Enable session affinity on the backend service to pin users to the same VM.
B) Add a second backend MIG in each region to handle local traffic.
C) Enable Cloud CDN on the backend service to cache static content at Google's edge nodes.
D) Switch to a Network Load Balancer, which has lower latency than the HTTP(S) Load Balancer.

*   **Correct Answer:** C) Enable Cloud CDN on the backend service to cache static content at Google's edge nodes.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Session affinity routes the same user to the same backend VM to preserve state — it does not cache content at the edge or reduce global latency for static assets.
    *   *Why B is incorrect:* Adding more MIGs increases backend capacity and reduces regional load, but users still retrieve content from your origin servers; it does not cache content at the network edge close to users.
    *   *Why D is incorrect:* Network Load Balancers operate at Layer 4 and have no concept of HTTP caching; Cloud CDN only works with the Global HTTP(S) Load Balancer, making a switch away counterproductive.

---

**Question 4**
You need to load balance internal traffic between a set of microservices running on Compute Engine VMs within the same VPC. The microservices communicate using HTTP/2 (gRPC). No public IP addresses should be involved. Which load balancer type is correct?

A) Global External HTTP(S) Load Balancer with SSL certificate
B) Regional External TCP/UDP Network Load Balancer
C) Internal HTTP(S) Load Balancer
D) Cloud Armor policy attached to an internal backend service

*   **Correct Answer:** C) Internal HTTP(S) Load Balancer
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The Global External HTTP(S) Load Balancer has a public IP and is designed for external internet traffic — it is not appropriate for internal VPC-to-VPC microservice traffic.
    *   *Why B is incorrect:* The Regional External TCP/UDP Network Load Balancer also has a public-facing frontend and is designed for external traffic; it does not provide an internal-only load balancing endpoint.
    *   *Why D is incorrect:* Cloud Armor is a web application firewall layer that attaches to load balancers for DDoS protection and rule-based filtering — it is not a load balancer itself and cannot distribute traffic.

---

**Question 5**
A backend VM in your HTTP(S) Load Balancer's Managed Instance Group is receiving traffic even though its application has crashed and it is returning HTTP 500 errors. What configuration change will cause the load balancer to stop sending traffic to this unhealthy instance?

A) Add a Cloud Armor security policy to block 5xx responses from reaching users.
B) Configure a URL map rule to redirect `/error` paths away from the broken instance.
C) Configure an HTTP health check on the backend service that checks for HTTP 200 responses, so the failing VM is automatically marked unhealthy and removed from rotation.
D) Enable Cloud CDN caching so that previously cached 200 responses are served instead of the live 500 errors.

*   **Correct Answer:** C) Configure an HTTP health check on the backend service that checks for HTTP 200 responses, so the failing VM is automatically marked unhealthy and removed from rotation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Armor security policies filter incoming requests based on IP addresses, geo-location, and request attributes — they do not inspect backend response codes or control which backend VMs receive traffic.
    *   *Why B is incorrect:* URL map rules route traffic based on request path patterns — they do not monitor backend health or dynamically reroute traffic based on runtime errors from a specific VM.
    *   *Why D is incorrect:* Cloud CDN caches successful responses but does not serve stale cached content instead of live backend errors when the backend is still reachable (just returning 5xx); health checks are the correct mechanism for removing failed instances from rotation.

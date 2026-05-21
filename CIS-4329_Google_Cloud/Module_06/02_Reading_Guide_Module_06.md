# Reading Guide: Module 06 – Cloud Load Balancing and Cloud CDN
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 06 – Cloud Load Balancing and Cloud CDN**! Load balancing distributes incoming traffic across multiple backend instances to maximize availability and performance. This module covers GCP's suite of load balancer types, how to choose between them, health checks, backend services, and Cloud CDN for caching static content at Google's edge. The ACE exam tests load balancer selection and configuration in scenario-based questions.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Global HTTP(S) Load Balancer**: A Layer 7 load balancer that distributes HTTP and HTTPS traffic globally based on URL maps. It uses Google's global anycast network so a single IP serves users from the nearest point of presence. It requires backends to be Managed Instance Groups (MIGs) or NEGs. Supports URL-based routing (send `/api` to one backend, `/static` to another).

*   **Network Load Balancer (TCP/UDP)**: A Layer 4 load balancer that distributes TCP or UDP traffic within a single region. It is not proxy-based — packets are passed through with their original source IPs preserved. Use it when you need to handle non-HTTP protocols or need to preserve client IP addresses.

*   **Internal Load Balancer**: Distributes traffic between internal (private IP) services within a VPC. Internal HTTP(S) Load Balancer is Layer 7 for internal microservices; Internal TCP/UDP Load Balancer is Layer 4. Neither type exposes a public IP.

*   **Health Check**: A probe that regularly tests whether backend instances are healthy and capable of serving traffic. Load balancers only send traffic to instances that pass the health check. Health checks can use HTTP, HTTPS, TCP, or gRPC protocols and are configured separately from firewall rules.

*   **Backend Service**: The GCP resource that defines the group of backends (MIGs or NEGs), the load balancing algorithm, session affinity settings, and the associated health check. A URL map routes requests to backend services.

*   **Cloud CDN**: A content delivery network built on Google's global edge infrastructure. When enabled on an HTTP(S) Load Balancer backend, Cloud CDN caches cacheable responses at edge nodes close to users. Cache keys, TTLs, and signed URLs for private content are all configurable. Cloud CDN reduces origin load and latency for static assets.

---

### 2. Certification Exam Tips

*   **Layer 7 vs. Layer 4 determines the load balancer type**: If the scenario mentions HTTP(S), URL routing, SSL termination, or content-based routing — the answer is an HTTP(S) Load Balancer. If it mentions TCP, UDP, preserving source IP, or non-HTTP protocols — the answer is a Network Load Balancer.

*   **Global vs. Regional**: HTTP(S) Load Balancer is global (one IP worldwide). Network Load Balancer is regional. Internal Load Balancers are always regional. The exam uses "global traffic" as a signal for HTTP(S) LB.

*   **Health checks must have matching firewall rules**: A common ACE exam trap is a scenario where a health check fails because there is no firewall rule allowing health check probe traffic (from `35.191.0.0/16` and `130.211.0.0/22`) to reach the backend VMs.

*   **Cloud CDN requires HTTP(S) LB**: Cloud CDN cannot be attached to a Network or Internal Load Balancer — it only works with the Global HTTP(S) Load Balancer as the frontend. The exam tests this dependency.

*   **Study Resource**: The freeCodeCamp ACE course covers load balancer types and Cloud CDN configuration with architecture diagrams: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Supplement with the official Cloud Load Balancing overview for the full product comparison table.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Cloud Load Balancing overview including the product comparison table that maps use cases to load balancer types: [Cloud Load Balancing Overview](https://cloud.google.com/load-balancing/docs/load-balancing-overview). The comparison table is directly exam-relevant.
*   **Required Reading**: Review Cloud CDN concepts including cache keys, cache modes, and signed URLs for private content: [Cloud CDN Overview](https://cloud.google.com/cdn/docs/overview).
*   **Required Video**: Watch the Load Balancing and CDN segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Load Balancing chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create an HTTP(S) Load Balancer with a MIG backend and enable Cloud CDN. Key commands to practice:

*   `gcloud compute health-checks create http my-health-check --port=80` — creates an HTTP health check
*   `gcloud compute backend-services create my-backend --protocol=HTTP --health-checks=my-health-check --global` — creates a global backend service
*   `gcloud compute url-maps create my-url-map --default-service=my-backend` — creates a URL map
*   `gcloud compute target-http-proxies create my-proxy --url-map=my-url-map` — creates an HTTP proxy frontend

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Load Balancing Overview](https://cloud.google.com/load-balancing/docs/load-balancing-overview) and study the product comparison table.
- [ ] Read the [Cloud CDN Overview](https://cloud.google.com/cdn/docs/overview) documentation page.
- [ ] Watch the Load Balancing segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create an HTTP(S) Load Balancer with a MIG backend and health check.
- [ ] Proceed to the weekly quiz.

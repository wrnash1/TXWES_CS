# Discussion — Module 06

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Load Balancing and Cloud CDN

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose any scenario.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The Broken Health Check Investigation

A startup has deployed a Global HTTP(S) Load Balancer in front of a Managed Instance Group of two web servers. The instance group shows two running VMs, and the load balancer has a forwarding rule with a global IP address. However, users are receiving 502 Bad Gateway errors. The on-call engineer checks the load balancer backend health and sees both instances listed as UNHEALTHY. The VMs are running and Apache is serving content on port 80 — a direct curl to each VM's external IP returns HTTP 200. The engineer is confused: the VMs work individually but the load balancer says they are unhealthy.

In 175–225 words, address the following:

- What is the root cause of the UNHEALTHY status even though the VMs respond correctly when accessed directly? Be specific about the technical reason.
- Describe the exact firewall rule that needs to be created to fix this issue. State the rule direction, source ranges, protocol, port, and target. Explain why these specific IP ranges are the source.
- After adding the correct firewall rule, the engineer waits 30 seconds but the backends still show UNHEALTHY. What health check parameters determine how quickly a backend transitions from UNHEALTHY to HEALTHY, and what is the minimum time the engineer must wait?

---

## Scenario B — The CDN Strategy Decision

A media company runs a news website that serves articles, images, and video thumbnails to users globally. The website has a Global HTTP(S) Load Balancer with two backend MIGs in `us-central1`. The engineering team is evaluating Cloud CDN to reduce load on their origin servers and improve load times for international users. The CTO asks the team to evaluate three CDN cache modes and recommend the best approach for their content mix.

In 175–225 words, address the following:

- Compare the three Cloud CDN cache modes (`USE_ORIGIN_HEADERS`, `CACHE_ALL_STATIC`, `FORCE_CACHE_ALL`) and explain which is most appropriate for a news website serving a mix of static images and dynamically generated article HTML.
- The website serves personalized "recommended articles" content via API calls at `/api/recommendations`. This content is unique per user and should never be served from a shared cache. How should the team configure the CDN or the backend to ensure this endpoint bypasses the cache?
- The engineering team updates article images frequently throughout the day. Describe two strategies for ensuring users receive updated images promptly rather than stale cached versions.

---

## Scenario C — The Load Balancer Type Selection Problem

A solutions architect at a consulting firm is designing cloud infrastructure for three separate clients simultaneously. Each client has a different requirement:

Client 1 wants a game server for a multiplayer mobile game that requires UDP connectivity and needs to preserve the original source IP address of each player's device for rate limiting and geographic analytics.

Client 2 runs a microservices architecture entirely inside a single GCP VPC. Services communicate over gRPC (HTTP/2). No service should be reachable from the internet; all load balancing is internal only.

Client 3 has a global e-commerce website with product pages at `/products`, checkout at `/checkout`, and a CDN-cached static asset directory at `/static`. They require a WAF to block OWASP Top 10 attacks.

In 175–225 words, address the following:

- For each client, state the specific load balancer type you would recommend and justify your choice using the key selection criteria (scope, layer, traffic direction, and any protocol or feature requirements).
- Client 3 asks whether they can use Cloud CDN on just the `/static` backend while leaving `/products` and `/checkout` uncached. Explain how the load balancer architecture makes this possible at the backend service level.
- The architect later learns that Client 1's budget is very tight and they cannot afford Cloud Interconnect. Does this affect your load balancer recommendation for Client 1? Explain why or why not.

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Identifies a technical error in the classmate's firewall rule specification (wrong source range, wrong direction, missing tag)
- Points out a CDN configuration edge case the classmate overlooked, such as authenticated API responses being accidentally cached
- Questions the classmate's load balancer type selection and provides a better-justified alternative with reference to a specific selection criterion
- Proposes a specific gcloud command from the lab that would implement part of the classmate's design recommendation

Responses that consist only of agreement without substantive technical additions receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions accurately. Uses correct load balancing terminology (health check, forwarding rule, backend service, URL map, CDN cache mode, security policy). Justifies design choices with reference to specific GCP features, IP ranges, or configuration parameters. 175–225 words.
- 3–4 pts: Addresses most sub-questions but uses vague terminology or lacks specific technical justification.
- 1–2 pts: Only addresses one sub-question or contains significant factual errors about GCP load balancing.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each contributing specific technical additions or corrections.
- 2 pts: Only one qualifying response, or both are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Load balancer health checks are one of the most reliably tested ACE exam topics, and Scenario A captures the single most common real-world mistake I have seen engineers make when deploying their first load balancer. The symptom — VMs respond when you curl them directly but the load balancer marks them unhealthy — is deeply counterintuitive until you understand that health check probes come from Google's prober infrastructure, not from your network. The probe traffic originates from `35.191.0.0/16` and `130.211.0.0/22`. Your VPC does not know about those addresses until you write a firewall rule that does. Once you understand that, you will never forget it, and you will immediately recognize the 502 error pattern on the exam.

---

End of Discussion — Module 06

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

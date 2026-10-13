# Video Script: Module 09 — Cloud Load Balancing and CDN (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 09. I am Professor Nash, and today we cover Cloud Load Balancing and
the Cloud CDN on Google Cloud Platform.

Load balancing is one of the most heavily tested topics on the ACE exam. Google Cloud
offers a portfolio of load balancers — each designed for a specific traffic type, scope,
and protocol. Choosing the wrong load balancer in a scenario question is a common way
to lose points.

By the end of this two-part video you will be able to describe all major GCP load balancer
types, configure an HTTP(S) Load Balancer with backend services and health checks, explain
URL maps and SSL certificate management, and describe how Cloud CDN and Cloud Armor
integrate with the HTTP(S) Load Balancer.

---

### Section 1: Why Load Balancing Matters

Load balancers serve two primary purposes:

- **Distribution** — spread incoming requests across multiple backend instances so no
  single instance is overwhelmed
- **High availability** — route traffic away from unhealthy instances automatically
  using health checks

Without load balancing, your architecture has a single point of failure and a hard
capacity ceiling. With it, you can add or remove backend capacity dynamically and survive
instance failures transparently.

---

### Section 2: GCP Load Balancer Portfolio Overview

GCP load balancers divide along three axes:

- **Scope**: Global vs. Regional
- **Protocol**: HTTP(S) vs. TCP/UDP/SSL
- **Traffic direction**: External (internet-facing) vs. Internal (VPC-internal)

Here is the complete portfolio:

| Load Balancer | Scope | Protocol | External/Internal |
|---|---|---|---|
| Global External HTTP(S) LB | Global | HTTP/HTTPS/HTTP2 | External |
| Regional External HTTP(S) LB | Regional | HTTP/HTTPS | External |
| External SSL Proxy LB | Global | SSL/TLS (non-HTTP) | External |
| External TCP Proxy LB | Global | TCP | External |
| External Network LB (pass-through) | Regional | TCP/UDP | External |
| Internal HTTP(S) LB | Regional | HTTP/HTTPS | Internal |
| Internal TCP/UDP LB | Regional | TCP/UDP | Internal |

For the ACE exam the most important distinction is **Global HTTP(S) vs. Regional Network
Load Balancer**. These two are tested most frequently.

---

### Section 3: Global External HTTP(S) Load Balancer

The Global External HTTP(S) Load Balancer is the most feature-rich option. It operates
at Layer 7 (application layer) and provides:

- **Global anycast IP** — a single IP that routes users to the nearest Google edge PoP
- **URL-based routing** — route `/api/*` to one backend, `/static/*` to another
- **SSL termination** — handles HTTPS at the load balancer; backends can use HTTP
- **Cloud CDN integration** — cache responses at Google's edge
- **Cloud Armor integration** — WAF and DDoS protection policies
- **Health checks** — automatic removal of unhealthy backends

#### Components of a Global HTTP(S) Load Balancer

A Global HTTP(S) Load Balancer is composed of multiple resources:

1. **Forwarding Rule** — binds a global IP and port to a target proxy
2. **Target HTTP(S) Proxy** — receives the request from the forwarding rule and
   consults the URL map
3. **URL Map** — defines routing rules: which path/host goes to which backend service
4. **Backend Service** — references one or more instance groups or NEGs
   (Network Endpoint Groups); defines the health check and balancing mode
5. **Health Check** — probes backend instances to verify they are serving traffic
6. **SSL Certificate** — attached to the HTTPS proxy for TLS termination

This chain is: Forwarding Rule → Proxy → URL Map → Backend Service → Instance Group.

---

### Section 4: Creating a Global HTTP(S) Load Balancer

Let us walk through the gcloud commands to build this chain from scratch.

#### Step 1: Create a Health Check

```bash
# HTTP health check on port 80, path /health
gcloud compute health-checks create http my-http-health-check \
  --port=80 \
  --request-path=/health \
  --check-interval=10s \
  --timeout=5s \
  --healthy-threshold=2 \
  --unhealthy-threshold=3
```

#### Step 2: Create a Backend Service

```bash
# Create a backend service using the health check
gcloud compute backend-services create my-backend-service \
  --protocol=HTTP \
  --health-checks=my-http-health-check \
  --global

# Add a managed instance group as a backend
gcloud compute backend-services add-backend my-backend-service \
  --instance-group=my-instance-group \
  --instance-group-zone=us-central1-a \
  --balancing-mode=UTILIZATION \
  --max-utilization=0.8 \
  --global
```

#### Step 3: Create a URL Map

```bash
# Default URL map sends all traffic to the backend service
gcloud compute url-maps create my-url-map \
  --default-service=my-backend-service

# Add a path rule for /api/* to a separate backend
gcloud compute url-maps add-path-matcher my-url-map \
  --path-matcher-name=api-matcher \
  --default-service=my-backend-service \
  --backend-service-path-rules="/api/*=my-api-backend-service"
```

#### Step 4: Create an SSL Certificate and Target HTTPS Proxy

```bash
# Create a Google-managed SSL certificate
gcloud compute ssl-certificates create my-ssl-cert \
  --domains=www.example.com

# Create target HTTPS proxy
gcloud compute target-https-proxies create my-https-proxy \
  --url-map=my-url-map \
  --ssl-certificates=my-ssl-cert
```

#### Step 5: Create a Forwarding Rule

```bash
# Reserve a global static IP
gcloud compute addresses create my-lb-ip \
  --ip-version=IPV4 \
  --global

# Create the forwarding rule on port 443
gcloud compute forwarding-rules create my-https-forwarding-rule \
  --address=my-lb-ip \
  --global \
  --target-https-proxy=my-https-proxy \
  --ports=443
```

```bash
# Also create a forwarding rule on port 80 to redirect HTTP to HTTPS
gcloud compute target-http-proxies create my-http-redirect-proxy \
  --url-map=my-url-map

gcloud compute forwarding-rules create my-http-forwarding-rule \
  --address=my-lb-ip \
  --global \
  --target-http-proxy=my-http-redirect-proxy \
  --ports=80
```

---

### Section 5: SSL Certificates

GCP supports three types of SSL certificates for load balancers:

- **Google-managed certificates** — GCP provisions and auto-renews certificates via
  Let's Encrypt; you only provide the domain name
- **Self-managed certificates** — you upload your own certificate and private key;
  you are responsible for renewal
- **Certificate Manager certificates** — newer, more flexible management via the
  Certificate Manager service; supports wildcard domains

For new deployments, use Google-managed certificates. They require that the domain's
DNS A record points to the load balancer IP before the certificate can be provisioned.

```bash
# List SSL certificates
gcloud compute ssl-certificates list

# Describe a certificate and check its status
gcloud compute ssl-certificates describe my-ssl-cert \
  --format="value(managed.status,managed.domainStatus)"
```

The status must be `ACTIVE` before HTTPS traffic is served. Certificate provisioning
typically takes 15–60 minutes after DNS propagation.

---

### Closing — Part 1

In Part 1 we covered:

- The GCP load balancer portfolio and selection criteria
- The components of a Global HTTP(S) Load Balancer (forwarding rule, proxy, URL map,
  backend service, health check)
- The gcloud commands to build a complete HTTP(S) LB stack
- SSL certificate types and provisioning

In Part 2 we cover Network Load Balancers, Internal Load Balancers, Cloud CDN, and
Cloud Armor integration.

See you in Part 2.

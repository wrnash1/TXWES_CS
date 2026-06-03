# Lab: Module 09 — Cloud Load Balancing and CDN

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will build a Global External HTTP(S) Load Balancer backed by a managed
instance group. You will configure a health check, backend service, URL map, and
forwarding rules. You will then enable Cloud CDN and create a basic Cloud Armor security
policy.

**Estimated time**: 75–90 minutes

**Cost estimate**: Under $2.00 USD if completed and cleaned up within the session

---

### Prerequisites

- A GCP project with billing enabled
- Cloud Shell or gcloud CLI authenticated
- Compute Engine API enabled

```bash
gcloud services enable compute.googleapis.com
```

---

### Part 1: Create Backend Infrastructure

#### Task 1.1: Create an Instance Template

```bash
gcloud config set project YOUR_PROJECT_ID

# Create an instance template running a simple web server
gcloud compute instance-templates create web-server-template \
  --machine-type=e2-micro \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --tags=http-server,allow-health-check \
  --metadata=startup-script='#! /bin/bash
apt-get update
apt-get install -y apache2
HOSTNAME=$(hostname)
cat > /var/www/html/health << HEALTHEOF
OK
HEALTHEOF
systemctl start apache2'
```

#### Task 1.2: Create a Managed Instance Group

```bash
# Create a regional managed instance group with 2 instances
gcloud compute instance-groups managed create web-mig \
  --template=web-server-template \
  --size=2 \
  --region=us-central1

# Set named ports (required for HTTP LB)
gcloud compute instance-groups managed set-named-ports web-mig \
  --named-ports=http:80 \
  --region=us-central1

# Verify instances are running
gcloud compute instance-groups managed list-instances web-mig \
  --region=us-central1
```

#### Task 1.3: Create Firewall Rules

```bash
# Allow HTTP traffic from internet to tagged instances
gcloud compute firewall-rules create allow-http-to-web \
  --network=default \
  --action=ALLOW \
  --rules=tcp:80 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=http-server

# Allow health check traffic from GCP health check IP ranges
gcloud compute firewall-rules create allow-health-check \
  --network=default \
  --action=ALLOW \
  --rules=tcp:80 \
  --source-ranges=130.211.0.0/22,35.191.0.0/16 \
  --target-tags=allow-health-check
```

---

### Part 2: Build the HTTP(S) Load Balancer

#### Task 2.1: Create a Health Check

```bash
gcloud compute health-checks create http lab09-health-check \
  --port=80 \
  --request-path=/health \
  --check-interval=10s \
  --timeout=5s \
  --healthy-threshold=2 \
  --unhealthy-threshold=3
```

#### Task 2.2: Create a Backend Service

```bash
# Create the backend service
gcloud compute backend-services create lab09-backend \
  --protocol=HTTP \
  --health-checks=lab09-health-check \
  --global

# Add the managed instance group to the backend service
gcloud compute backend-services add-backend lab09-backend \
  --instance-group=web-mig \
  --instance-group-region=us-central1 \
  --balancing-mode=UTILIZATION \
  --max-utilization=0.8 \
  --global

# Verify the backend service configuration
gcloud compute backend-services describe lab09-backend --global
```

#### Task 2.3: Create a URL Map

```bash
gcloud compute url-maps create lab09-url-map \
  --default-service=lab09-backend
```

#### Task 2.4: Create a Target HTTP Proxy and Forwarding Rule

```bash
# Create target HTTP proxy
gcloud compute target-http-proxies create lab09-http-proxy \
  --url-map=lab09-url-map

# Reserve a global static IP address
gcloud compute addresses create lab09-lb-ip \
  --ip-version=IPV4 \
  --global

# Get the IP address value
LB_IP=$(gcloud compute addresses describe lab09-lb-ip \
  --global \
  --format="value(address)")
echo "Load balancer IP: $LB_IP"

# Create the forwarding rule on port 80
gcloud compute forwarding-rules create lab09-http-rule \
  --address=lab09-lb-ip \
  --global \
  --target-http-proxy=lab09-http-proxy \
  --ports=80
```

#### Task 2.5: Test the Load Balancer

The load balancer takes 3–5 minutes to fully propagate. Test with curl:

```bash
# Wait a few minutes, then test
curl -I http://$LB_IP/

# Load test to see round-robin across both instances
for i in $(seq 1 10); do curl -s http://$LB_IP/ | grep "Hello"; done
```

You should see responses from both instances, confirming load balancing is working.

---

### Part 3: Enable Cloud CDN

#### Task 3.1: Enable CDN on the Backend Service

```bash
# Enable CDN with CACHE_ALL_STATIC mode
gcloud compute backend-services update lab09-backend \
  --enable-cdn \
  --cache-mode=CACHE_ALL_STATIC \
  --global

# Verify CDN is enabled
gcloud compute backend-services describe lab09-backend \
  --global \
  --format="value(enableCDN,cdnPolicy.cacheMode)"
```

#### Task 3.2: Test CDN Caching

```bash
# Make a request and check for CDN headers
curl -sI http://$LB_IP/ | grep -i "via\|age"
```

Look for the `Via: 1.1 google` header, which confirms traffic passes through Google's
CDN infrastructure.

---

### Part 4: Create a Cloud Armor Security Policy

#### Task 4.1: Create the Security Policy

```bash
# Create a new security policy
gcloud compute security-policies create lab09-armor-policy \
  --description="Lab 09 Cloud Armor policy"

# Add a rule to deny a specific test IP range
gcloud compute security-policies rules create 1000 \
  --security-policy=lab09-armor-policy \
  --src-ip-ranges=192.0.2.0/24 \
  --action=deny-403 \
  --description="Deny test IP range"

# Add a rule to allow all other traffic
gcloud compute security-policies rules create 2000 \
  --security-policy=lab09-armor-policy \
  --src-ip-ranges="*" \
  --action=allow \
  --description="Allow all other traffic"

# List the rules in the policy
gcloud compute security-policies describe lab09-armor-policy
```

#### Task 4.2: Attach the Security Policy to the Backend Service

```bash
gcloud compute backend-services update lab09-backend \
  --security-policy=lab09-armor-policy \
  --global

# Verify attachment
gcloud compute backend-services describe lab09-backend \
  --global \
  --format="value(securityPolicy)"
```

---

### Part 5: Reflection Questions

Answer these questions in your lab submission document:

1. Why do health check firewall rules need to allow traffic from `130.211.0.0/22` and
   `35.191.0.0/16` specifically?
2. What is the purpose of setting named ports on the managed instance group, and what
   happens if you omit this step?
3. What is the difference between enabling Cloud CDN with `USE_ORIGIN_HEADERS` vs.
   `CACHE_ALL_STATIC`? When would each be appropriate?
4. In the Cloud Armor policy you created, explain why rule priority 1000 is evaluated
   before priority 2000.
5. What component would you need to add to this architecture to serve traffic over
   HTTPS with an SSL certificate?

---

### Part 6: Cleanup

```bash
# Delete forwarding rules
gcloud compute forwarding-rules delete lab09-http-rule --global --quiet

# Delete target proxy
gcloud compute target-http-proxies delete lab09-http-proxy --quiet

# Delete URL map
gcloud compute url-maps delete lab09-url-map --quiet

# Delete backend service
gcloud compute backend-services delete lab09-backend --global --quiet

# Delete health check
gcloud compute health-checks delete lab09-health-check --quiet

# Delete the managed instance group
gcloud compute instance-groups managed delete web-mig \
  --region=us-central1 --quiet

# Delete instance template
gcloud compute instance-templates delete web-server-template --quiet

# Delete static IP
gcloud compute addresses delete lab09-lb-ip --global --quiet

# Delete security policy
gcloud compute security-policies delete lab09-armor-policy --quiet

# Delete firewall rules
gcloud compute firewall-rules delete allow-http-to-web allow-health-check --quiet
```

---

### Submission Checklist

- Managed instance group created with 2 instances
- Firewall rules created including health check IP ranges
- Health check, backend service, URL map, proxy, and forwarding rule all created
- Load balancer tested with curl showing responses
- Cloud CDN enabled and CDN header verified
- Cloud Armor policy created with at least one deny rule and attached to backend
- All 5 reflection questions answered
- All resources cleaned up

---

### Grading Rubric

| Task | Points |
|---|---|
| Backend infrastructure (MIG, firewall rules) | 15 |
| Complete LB chain created and tested | 30 |
| Cloud CDN enabled and tested | 20 |
| Cloud Armor policy created and attached | 15 |
| Reflection questions answered | 15 |
| Resources cleaned up | 5 |
| **Total** | **100** |

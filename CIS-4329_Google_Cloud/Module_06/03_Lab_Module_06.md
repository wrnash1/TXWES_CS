# Lab — Module 06

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Building a Global HTTP(S) Load Balancer with Cloud CDN

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Lab Overview

In this lab you will build a complete Global HTTP(S) Load Balancer using the gcloud CLI. You will create health checks, a Managed Instance Group as the backend, a backend service with Cloud CDN enabled, a URL map, a target HTTP proxy, and a forwarding rule. You will verify the load balancer is functioning and observe health check behavior, CDN enablement, and Cloud Armor policy attachment.

Estimated Time: 60–75 minutes

Points: 100

---

## Prerequisites

- A GCP project with billing enabled
- Cloud Shell or gcloud CLI configured with your project
- Completion of Module 05 lab (VPC knowledge assumed)

---

## Part 1 — Environment Setup (15 Points)

### Task 1.1 — Set Project and Region Variables

Open Cloud Shell and configure your environment variables.

```bash
gcloud config set project YOUR_PROJECT_ID

export REGION=us-central1
export ZONE=us-central1-a
export PROJECT_ID=$(gcloud config get-value project)
echo "Project: $PROJECT_ID | Region: $REGION | Zone: $ZONE"
```

### Task 1.2 — Enable Required APIs

```bash
gcloud services enable compute.googleapis.com
```

Verify the API is enabled:

```bash
gcloud services list --enabled --filter="name:compute.googleapis.com"
```

### Task 1.3 — Create a Custom VPC and Subnet

```bash
gcloud compute networks create lb-vpc \
  --subnet-mode=custom

gcloud compute networks subnets create lb-subnet \
  --network=lb-vpc \
  --region=$REGION \
  --range=10.10.0.0/24
```

Verify the subnet was created:

```bash
gcloud compute networks subnets list --filter="network:lb-vpc"
```

**Part 1 Deliverable**: Screenshot of the subnet list output showing `lb-subnet` in `us-central1` with CIDR range `10.10.0.0/24`.

---

## Part 2 — Instance Template and Managed Instance Group (25 Points)

### Task 2.1 — Create a Firewall Rule for HTTP Traffic

Allow HTTP traffic to backend VMs tagged `http-server`:

```bash
gcloud compute firewall-rules create lb-allow-http \
  --network=lb-vpc \
  --action=ALLOW \
  --direction=INGRESS \
  --source-ranges=0.0.0.0/0 \
  --rules=tcp:80 \
  --target-tags=http-server
```

### Task 2.2 — Create the Health Check Firewall Rule

This is the most critical firewall rule for load balancer functionality. Without it, the load balancer health check probers cannot reach the backend VMs, all instances are marked unhealthy, and no user traffic is served.

```bash
gcloud compute firewall-rules create allow-health-checks \
  --network=lb-vpc \
  --action=ALLOW \
  --direction=INGRESS \
  --source-ranges=35.191.0.0/16,130.211.0.0/22 \
  --rules=tcp:80 \
  --target-tags=http-server
```

Verify both rules exist:

```bash
gcloud compute firewall-rules list --filter="network:lb-vpc"
```

Confirm you see `lb-allow-http` and `allow-health-checks` in the output.

### Task 2.3 — Create an Instance Template

The startup script configures each VM to serve a simple HTTP response identifying the instance hostname. The `/health` endpoint is used by the health check.

```bash
gcloud compute instance-templates create lb-instance-template \
  --machine-type=e2-micro \
  --network=lb-vpc \
  --subnet=lb-subnet \
  --region=$REGION \
  --tags=http-server \
  --metadata=startup-script='#!/bin/bash
apt-get update -y
apt-get install -y apache2
HOSTNAME=$(hostname)
mkdir -p /var/www/html
cat > /var/www/html/index.html << HTMLEOF
<html><body>
<h1>Load Balancer Lab</h1>
<p>Served by: $HOSTNAME</p>
</body></html>
HTMLEOF
echo "OK" > /var/www/html/health
systemctl start apache2
systemctl enable apache2'
```

Verify the template was created:

```bash
gcloud compute instance-templates describe lb-instance-template \
  --format="value(name,properties.tags.items)"
```

### Task 2.4 — Create a Managed Instance Group

```bash
gcloud compute instance-groups managed create lb-mig \
  --template=lb-instance-template \
  --size=2 \
  --zone=$ZONE
```

Wait for the instances to reach `RUNNING` status. This takes 2–3 minutes while the startup script runs.

```bash
gcloud compute instance-groups managed list-instances lb-mig \
  --zone=$ZONE
```

Re-run the command every 30 seconds until both instances show `RUNNING`.

**Part 2 Deliverable**: Screenshot showing two instances in the `lb-mig` output with `RUNNING` status.

---

## Part 3 — Health Check and Backend Service (20 Points)

### Task 3.1 — Create the Health Check

```bash
gcloud compute health-checks create http lb-health-check \
  --port=80 \
  --request-path=/health \
  --check-interval=10 \
  --timeout=5 \
  --healthy-threshold=2 \
  --unhealthy-threshold=2
```

Verify the health check configuration:

```bash
gcloud compute health-checks describe lb-health-check
```

Note the `checkIntervalSec`, `timeoutSec`, `healthyThreshold`, and `unhealthyThreshold` values in the output.

### Task 3.2 — Set a Named Port on the Instance Group

The load balancer uses named ports to route traffic to the correct port on backend instances.

```bash
gcloud compute instance-groups managed set-named-ports lb-mig \
  --named-ports=http:80 \
  --zone=$ZONE
```

### Task 3.3 — Create the Backend Service

```bash
gcloud compute backend-services create lb-backend-service \
  --protocol=HTTP \
  --port-name=http \
  --health-checks=lb-health-check \
  --global
```

### Task 3.4 — Add the MIG as a Backend

```bash
gcloud compute backend-services add-backend lb-backend-service \
  --instance-group=lb-mig \
  --instance-group-zone=$ZONE \
  --global
```

### Task 3.5 — Verify Backend Health

Wait approximately 60 seconds after adding the backend, then check health status:

```bash
gcloud compute backend-services get-health lb-backend-service \
  --global
```

Both instances should show `HEALTHY`. If they show `UNHEALTHY`, troubleshoot in this order:

1. Confirm the health check firewall rule allows `35.191.0.0/16` and `130.211.0.0/22` on port 80
2. Confirm the startup script completed: SSH into a VM and check `curl localhost/health`
3. Confirm the named port is set on the MIG

**Part 3 Deliverable**: Screenshot of `get-health` output showing both backend instances with `HEALTHY` status.

---

## Part 4 — URL Map, Proxy, and Forwarding Rule (25 Points)

### Task 4.1 — Create the URL Map

```bash
gcloud compute url-maps create lb-url-map \
  --default-service=lb-backend-service
```

### Task 4.2 — Add a Path-Based Routing Rule

Add a path matcher that routes `/health` requests explicitly (demonstrating path routing syntax):

```bash
gcloud compute url-maps add-path-matcher lb-url-map \
  --path-matcher-name=health-paths \
  --default-service=lb-backend-service \
  --backend-service-path-rules="/health=lb-backend-service"
```

Describe the URL map to verify the path matcher:

```bash
gcloud compute url-maps describe lb-url-map
```

### Task 4.3 — Create the Target HTTP Proxy

```bash
gcloud compute target-http-proxies create lb-http-proxy \
  --url-map=lb-url-map
```

### Task 4.4 — Create the Forwarding Rule

```bash
gcloud compute forwarding-rules create lb-forwarding-rule \
  --global \
  --target-http-proxy=lb-http-proxy \
  --ports=80
```

### Task 4.5 — Get the Load Balancer's External IP

```bash
gcloud compute forwarding-rules list --global
```

Note the `IP_ADDRESS` column. Store it in a variable:

```bash
LB_IP=$(gcloud compute forwarding-rules describe lb-forwarding-rule \
  --global \
  --format="value(IPAddress)")
echo "Load Balancer IP: $LB_IP"
```

### Task 4.6 — Test the Load Balancer

Wait 2–3 minutes for the load balancer to propagate, then test:

```bash
curl http://$LB_IP/
```

Run the command multiple times to observe traffic distribution across the two backend VMs:

```bash
for i in {1..10}; do
  curl -s http://$LB_IP/ | grep "Served by"
done
```

If the load balancer is distributing traffic, you will see different hostnames from the two backend VMs over multiple requests.

**Part 4 Deliverable**: Screenshot showing the forwarding rules list with the load balancer IP, and the curl output showing responses from backend VMs. Show at least two different hostnames appearing in the repeated curl output if possible.

---

## Part 5 — Cloud CDN and Cloud Armor (15 Points)

### Task 5.1 — Enable Cloud CDN on the Backend Service

```bash
gcloud compute backend-services update lb-backend-service \
  --enable-cdn \
  --global
```

Verify CDN is enabled:

```bash
gcloud compute backend-services describe lb-backend-service \
  --global \
  --format="value(enableCDN)"
```

The output should be `True`.

### Task 5.2 — Create a Cloud Armor Security Policy

```bash
gcloud compute security-policies create lb-armor-policy \
  --description="Lab WAF and DDoS protection policy"
```

Add a rule to deny a test IP range. The `192.0.2.0/24` range is an RFC 5737 documentation address — it is not a real internet range and cannot affect legitimate traffic.

```bash
gcloud compute security-policies rules create 1000 \
  --security-policy=lb-armor-policy \
  --action=deny-404 \
  --src-ip-ranges=192.0.2.0/24 \
  --description="Block RFC 5737 documentation test range"
```

List the policy rules:

```bash
gcloud compute security-policies describe lb-armor-policy
```

### Task 5.3 — Attach the Security Policy to the Backend Service

```bash
gcloud compute backend-services update lb-backend-service \
  --security-policy=lb-armor-policy \
  --global
```

Verify the security policy is attached:

```bash
gcloud compute backend-services describe lb-backend-service \
  --global \
  --format="value(securityPolicy)"
```

The output should show the full resource path containing `lb-armor-policy`.

**Part 5 Deliverable**: Screenshot showing `enableCDN: True` and the security policy resource path in the backend service description.

---

## Cleanup — Required

Delete all resources to avoid ongoing charges. Run these commands in order:

```bash
gcloud compute forwarding-rules delete lb-forwarding-rule \
  --global --quiet

gcloud compute target-http-proxies delete lb-http-proxy --quiet

gcloud compute url-maps delete lb-url-map --quiet

gcloud compute backend-services delete lb-backend-service \
  --global --quiet

gcloud compute health-checks delete lb-health-check --quiet

gcloud compute instance-groups managed delete lb-mig \
  --zone=$ZONE --quiet

gcloud compute instance-templates delete lb-instance-template --quiet

gcloud compute security-policies delete lb-armor-policy --quiet

gcloud compute firewall-rules delete lb-allow-http \
  allow-health-checks --quiet

gcloud compute networks subnets delete lb-subnet \
  --region=$REGION --quiet

gcloud compute networks delete lb-vpc --quiet
```

Verify cleanup:

```bash
gcloud compute forwarding-rules list --global
gcloud compute backend-services list --global
gcloud compute networks list --filter="name:lb-vpc"
```

All three commands should return empty output or show no `lb-` resources.

---

## Grading Rubric — 100 Points

| Part | Task | Points |
|---|---|---|
| Part 1 | VPC, subnet created; subnet verified in list output | 15 |
| Part 2 | Both firewall rules created (HTTP + health check ranges); instance template with startup script; MIG with 2 running instances | 25 |
| Part 3 | HTTP health check configured; backend service created; both backends showing HEALTHY status | 20 |
| Part 4 | URL map with path matcher; target HTTP proxy; forwarding rule; load balancer IP shown; curl response from backend VMs | 25 |
| Part 5 | CDN enabled (True); Cloud Armor policy with deny rule; policy attached to backend service | 15 |

### Submission Requirements

Submit a single document (PDF or Google Doc) containing:

1. All required screenshots labeled by part and task number
2. The output of `gcloud compute forwarding-rules list --global` showing the load balancer IP
3. The output of `gcloud compute backend-services get-health lb-backend-service --global` showing HEALTHY backends
4. A written reflection (100–150 words) answering: Why is the health check firewall rule for `35.191.0.0/16` and `130.211.0.0/22` the most commonly missed step when building a load balancer, and what symptoms does a missing rule produce in the load balancer logs and user experience?

### Grading Notes

- The health check firewall rule is the most commonly missed step. If backends show UNHEALTHY, check this rule first before any other troubleshooting.
- Load balancer IP propagation takes 2–5 minutes after creating the forwarding rule. A connection error immediately after creation is normal — wait and retry.
- Cloud CDN cache hits may not be directly observable in this lab because the test responses have no cache-control headers. The deliverable is enabling CDN and verifying the flag is set, not observing an edge cache hit.
- Cloud Armor rule priority 1000 places the custom rule above the default allow-all rule (priority 2147483647) at the bottom of the policy.

---

End of Lab — Module 06

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

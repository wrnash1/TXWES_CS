# Lab: Module 05 — Virtual Private Cloud Networking

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will create a custom VPC, configure subnets and firewall rules,
deploy VMs to test connectivity, configure VPC peering, and deploy a load
balancer in front of a managed instance group.

**Estimated Time:** 90 minutes

**Prerequisites:**

- Active GCP project with billing enabled
- Compute Engine API enabled
- Cloud Shell access

**Learning Objectives:**

By the end of this lab you will be able to:

1. Create a custom-mode VPC with regional subnets
2. Configure targeted firewall rules using network tags
3. Deploy VMs and test intra-VPC connectivity
4. Configure VPC peering between two VPCs
5. Deploy an external HTTP load balancer in front of a MIG
6. Verify load balancer functionality and health check behavior

---

## Part 1 — Create a Custom VPC and Subnets (15 minutes)

### Step 1.1 — Set Environment Variables

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export ZONE=us-central1-a
```

### Step 1.2 — Create a Custom VPC

```bash
gcloud compute networks create lab05-vpc \
  --subnet-mode=custom \
  --mtu=1460 \
  --description="Lab 05 custom VPC"

# Verify
gcloud compute networks describe lab05-vpc
```

### Step 1.3 — Create Subnets

```bash
# Web tier subnet
gcloud compute networks subnets create lab05-web-subnet \
  --network=lab05-vpc \
  --region=$REGION \
  --range=10.10.1.0/24 \
  --description="Web tier subnet"

# App tier subnet
gcloud compute networks subnets create lab05-app-subnet \
  --network=lab05-vpc \
  --region=$REGION \
  --range=10.10.2.0/24 \
  --description="Application tier subnet"

# List subnets
gcloud compute networks subnets list --network=lab05-vpc
```

### Step 1.4 — Verify No Default Firewall Rules

```bash
# The custom VPC has NO default allow rules — confirm this
gcloud compute firewall-rules list --filter="network:lab05-vpc"
```

---

## Part 2 — Configure Firewall Rules (15 minutes)

### Step 2.1 — Allow SSH from Cloud Shell (Internal Google IPs)

```bash
# Allow SSH from all sources for lab purposes
# In production, restrict source-ranges to your office IP
gcloud compute firewall-rules create lab05-allow-ssh \
  --network=lab05-vpc \
  --allow=tcp:22 \
  --direction=INGRESS \
  --source-ranges=0.0.0.0/0 \
  --target-tags=ssh-access \
  --priority=1000 \
  --description="Allow SSH to tagged VMs"
```

### Step 2.2 — Allow HTTP to Web Tier

```bash
gcloud compute firewall-rules create lab05-allow-http \
  --network=lab05-vpc \
  --allow=tcp:80 \
  --direction=INGRESS \
  --source-ranges=0.0.0.0/0 \
  --target-tags=web-server \
  --priority=1000 \
  --description="Allow HTTP to web servers"
```

### Step 2.3 — Allow Internal Traffic Between Subnets

```bash
gcloud compute firewall-rules create lab05-allow-internal \
  --network=lab05-vpc \
  --allow=tcp,udp,icmp \
  --direction=INGRESS \
  --source-ranges=10.10.0.0/16 \
  --priority=1000 \
  --description="Allow all internal VPC traffic"
```

### Step 2.4 — Allow Health Check Probes

```bash
# GCP health checkers use these IP ranges
gcloud compute firewall-rules create lab05-allow-health-check \
  --network=lab05-vpc \
  --allow=tcp:80 \
  --direction=INGRESS \
  --source-ranges=130.211.0.0/22,35.191.0.0/16 \
  --target-tags=web-server \
  --priority=900 \
  --description="Allow load balancer health checks"
```

### Step 2.5 — Verify Rules

```bash
gcloud compute firewall-rules list \
  --filter="network:lab05-vpc" \
  --format="table(name,direction,priority,allowed,targetTags,sourceRanges)"
```

---

## Part 3 — Deploy VMs and Test Connectivity (20 minutes)

### Step 3.1 — Create a Startup Script

```bash
cat > web-startup.sh << 'EOF'
#!/bin/bash
apt-get update -y
apt-get install -y apache2
systemctl enable apache2
systemctl start apache2
echo "<h1>$(hostname) — Lab 05 Web VM</h1>" > /var/www/html/index.html
EOF
```

### Step 3.2 — Create Two Web VMs

```bash
# First web VM
gcloud compute instances create lab05-web-vm-1 \
  --zone=$ZONE \
  --machine-type=e2-micro \
  --subnet=lab05-web-subnet \
  --tags=web-server,ssh-access \
  --metadata-from-file=startup-script=web-startup.sh

# Second web VM
gcloud compute instances create lab05-web-vm-2 \
  --zone=$ZONE \
  --machine-type=e2-micro \
  --subnet=lab05-web-subnet \
  --tags=web-server,ssh-access \
  --metadata-from-file=startup-script=web-startup.sh

# List instances with internal and external IPs
gcloud compute instances list --filter="name:lab05"
```

### Step 3.3 — Test HTTP and SSH Connectivity

```bash
# Get external IPs
VM1_IP=$(gcloud compute instances describe lab05-web-vm-1 \
  --zone=$ZONE \
  --format='value(networkInterfaces[0].accessConfigs[0].natIP)')
VM2_IP=$(gcloud compute instances describe lab05-web-vm-2 \
  --zone=$ZONE \
  --format='value(networkInterfaces[0].accessConfigs[0].natIP)')

# Test HTTP (wait 60 seconds after creation)
curl -s http://$VM1_IP
curl -s http://$VM2_IP

# Test internal connectivity (SSH into VM1 and ping VM2)
VM2_INTERNAL=$(gcloud compute instances describe lab05-web-vm-2 \
  --zone=$ZONE \
  --format='value(networkInterfaces[0].networkIP)')

gcloud compute ssh lab05-web-vm-1 --zone=$ZONE \
  --command="ping -c 3 $VM2_INTERNAL"
```

---

## Part 4 — Deploy an External HTTP Load Balancer (25 minutes)

### Step 4.1 — Create an Instance Template

```bash
gcloud compute instance-templates create lab05-web-template \
  --machine-type=e2-micro \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --network=lab05-vpc \
  --subnet=lab05-web-subnet \
  --region=$REGION \
  --tags=web-server,ssh-access \
  --metadata-from-file=startup-script=web-startup.sh
```

### Step 4.2 — Create a Regional MIG

```bash
gcloud compute instance-groups managed create lab05-web-mig \
  --template=lab05-web-template \
  --size=2 \
  --region=$REGION

# Wait for instances to be running
gcloud compute instance-groups managed wait-until stable lab05-web-mig \
  --region=$REGION \
  --timeout=300
```

### Step 4.3 — Create a Health Check

```bash
gcloud compute health-checks create http lab05-lb-health-check \
  --port=80 \
  --request-path=/ \
  --check-interval=10 \
  --timeout=5
```

### Step 4.4 — Create Backend Service and Add MIG

```bash
# Set named port on the MIG
gcloud compute instance-groups managed set-named-ports lab05-web-mig \
  --named-ports=http:80 \
  --region=$REGION

# Create backend service
gcloud compute backend-services create lab05-web-backend \
  --protocol=HTTP \
  --port-name=http \
  --health-checks=lab05-lb-health-check \
  --global

# Add MIG to backend service
gcloud compute backend-services add-backend lab05-web-backend \
  --instance-group=lab05-web-mig \
  --instance-group-region=$REGION \
  --global
```

### Step 4.5 — Create URL Map, Proxy, and Forwarding Rule

```bash
gcloud compute url-maps create lab05-url-map \
  --default-service=lab05-web-backend

gcloud compute target-http-proxies create lab05-http-proxy \
  --url-map=lab05-url-map

gcloud compute forwarding-rules create lab05-forwarding-rule \
  --load-balancing-scheme=EXTERNAL \
  --global \
  --target-http-proxy=lab05-http-proxy \
  --ports=80

# Get the load balancer IP (takes 2-3 minutes to provision)
LB_IP=$(gcloud compute forwarding-rules describe lab05-forwarding-rule \
  --global --format='value(IPAddress)')
echo "Load Balancer IP: $LB_IP"
```

### Step 4.6 — Test the Load Balancer

```bash
# Wait 3-5 minutes for the LB to become active
# Then test multiple times to see different backends responding
for i in {1..5}; do
  curl -s http://$LB_IP
  sleep 1
done
```

---

## Lab Deliverables

Submit a lab report containing:

1. Output of `gcloud compute networks subnets list --network=lab05-vpc`.
2. Output of the firewall rules list showing all 4 rules.
3. Output of `curl` commands to both VM external IPs confirming HTTP response.
4. Output of the `ping` test showing internal connectivity between VMs.
5. Output of the load balancer test loop showing at least two different
   hostnames responding.
6. Answers to the lab questions.

**Lab Questions:**

1. Your custom VPC has no default allow rules. Why is this more secure than
   using the default VPC, and what is the risk of the default VPC's
   `default-allow-ssh` rule?
2. You have three VPCs: A, B, and C. VPC A is peered with VPC B. VPC B is
   peered with VPC C. Can a VM in VPC A communicate with a VM in VPC C?
   Explain why or why not.
3. What is the purpose of the `130.211.0.0/22` and `35.191.0.0/16` source
   ranges in the health check firewall rule?
4. Explain the difference between a URL map and a forwarding rule in the
   External Application Load Balancer architecture.
5. When would you choose Shared VPC instead of VPC peering for connecting
   multiple teams' GCP projects?

---

## Cleanup

```bash
# Delete load balancer components
gcloud compute forwarding-rules delete lab05-forwarding-rule --global --quiet
gcloud compute target-http-proxies delete lab05-http-proxy --quiet
gcloud compute url-maps delete lab05-url-map --quiet
gcloud compute backend-services delete lab05-web-backend --global --quiet
gcloud compute health-checks delete lab05-lb-health-check --quiet

# Delete MIG and template
gcloud compute instance-groups managed delete lab05-web-mig \
  --region=$REGION --quiet
gcloud compute instance-templates delete lab05-web-template --quiet

# Delete standalone VMs
gcloud compute instances delete lab05-web-vm-1 lab05-web-vm-2 \
  --zone=$ZONE --quiet

# Delete firewall rules
gcloud compute firewall-rules delete \
  lab05-allow-ssh lab05-allow-http \
  lab05-allow-internal lab05-allow-health-check --quiet

# Delete subnets
gcloud compute networks subnets delete \
  lab05-web-subnet lab05-app-subnet \
  --region=$REGION --quiet

# Delete VPC
gcloud compute networks delete lab05-vpc --quiet
```

---

End of Lab — Module 05

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

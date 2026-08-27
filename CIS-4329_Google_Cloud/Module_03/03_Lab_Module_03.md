# Lab: Module 03 — Compute Engine

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will create Compute Engine VMs, configure startup scripts,
take disk snapshots, create an instance template, deploy a managed instance
group with autoscaling, and work with preemptible VMs.

**Estimated Time:** 90 minutes

**Prerequisites:**

- Completed Module 01 lab (project configured, Cloud Shell working)
- Billing enabled on your project
- Compute Engine API enabled

**Learning Objectives:**

By the end of this lab you will be able to:

1. Create VMs with custom configurations and startup scripts
2. Connect to VMs via SSH using gcloud
3. Take persistent disk snapshots
4. Create instance templates
5. Deploy and scale a managed instance group
6. Configure autoscaling
7. Create and manage preemptible VMs

---

## Part 1 — Create a VM with a Startup Script (20 minutes)

### Step 1.1 — Enable Required API

```bash
gcloud services enable compute.googleapis.com

export PROJECT_ID=$(gcloud config get-value project)
gcloud config set compute/zone us-central1-a
gcloud config set compute/region us-central1
```

### Step 1.2 — Create a Startup Script File

```bash
cat > startup.sh << 'EOF'
#!/bin/bash
apt-get update -y
apt-get install -y apache2
systemctl enable apache2
systemctl start apache2
echo "<h1>Hello from $(hostname) — CIS-4329 Lab 03</h1>" \
  > /var/www/html/index.html
EOF
```

### Step 1.3 — Create the VM

```bash
gcloud compute instances create lab03-web-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=20GB \
  --boot-disk-type=pd-balanced \
  --metadata-from-file=startup-script=startup.sh \
  --tags=http-server
```

### Step 1.4 — Allow HTTP Traffic

```bash
gcloud compute firewall-rules create allow-http \
  --allow=tcp:80 \
  --target-tags=http-server \
  --description="Allow HTTP traffic to web VMs"
```

### Step 1.5 — Verify the VM and Startup Script

```bash
# List instances and note the external IP
gcloud compute instances list

# Get the external IP
EXTERNAL_IP=$(gcloud compute instances describe lab03-web-vm \
  --zone=us-central1-a \
  --format='value(networkInterfaces[0].accessConfigs[0].natIP)')
echo "External IP: $EXTERNAL_IP"

# Test the web server (wait 60-90 seconds after creation)
curl http://$EXTERNAL_IP
```

### Step 1.6 — SSH and Check Startup Script Logs

```bash
gcloud compute ssh lab03-web-vm --zone=us-central1-a

# Inside the VM:
sudo journalctl -u google-startup-scripts.service --no-pager
sudo systemctl status apache2
exit
```

---

## Part 2 — Disk Snapshots (15 minutes)

### Step 2.1 — Create a Snapshot

```bash
# Get the boot disk name
DISK_NAME=$(gcloud compute instances describe lab03-web-vm \
  --zone=us-central1-a \
  --format='value(disks[0].source)' | sed 's|.*/||')
echo "Disk: $DISK_NAME"

# Create a snapshot
gcloud compute disks snapshot $DISK_NAME \
  --zone=us-central1-a \
  --snapshot-names=lab03-snapshot-$(date +%Y%m%d)

# List snapshots
gcloud compute snapshots list
```

### Step 2.2 — Create a New Disk from the Snapshot

```bash
SNAPSHOT_NAME=$(gcloud compute snapshots list \
  --format='value(name)' | grep lab03 | head -1)

gcloud compute disks create lab03-restored-disk \
  --source-snapshot=$SNAPSHOT_NAME \
  --zone=us-central1-a \
  --type=pd-balanced

# Verify
gcloud compute disks list --filter="name:lab03"
```

**Question 2.2:** After creating the restored disk, is the original snapshot
still billable? What would you need to do to stop paying for it?

---

## Part 3 — Instance Template and Managed Instance Group (35 minutes)

### Step 3.1 — Create an Instance Template

```bash
gcloud compute instance-templates create lab03-web-template \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=20GB \
  --boot-disk-type=pd-balanced \
  --tags=http-server \
  --metadata-from-file=startup-script=startup.sh

# Describe the template
gcloud compute instance-templates describe lab03-web-template
```

### Step 3.2 — Create a Health Check

```bash
gcloud compute health-checks create http lab03-health-check \
  --port=80 \
  --request-path=/ \
  --check-interval=10 \
  --timeout=5 \
  --healthy-threshold=2 \
  --unhealthy-threshold=3
```

### Step 3.3 — Create a Regional Managed Instance Group

```bash
gcloud compute instance-groups managed create lab03-web-mig \
  --template=lab03-web-template \
  --size=2 \
  --region=us-central1 \
  --health-check=lab03-health-check \
  --initial-delay=120

# Monitor the MIG — wait for all instances to be RUNNING
gcloud compute instance-groups managed list-instances lab03-web-mig \
  --region=us-central1
```

### Step 3.4 — Configure Autoscaling

```bash
gcloud compute instance-groups managed set-autoscaling lab03-web-mig \
  --region=us-central1 \
  --max-num-replicas=5 \
  --min-num-replicas=2 \
  --target-cpu-utilization=0.60 \
  --cool-down-period=60

# Verify autoscaling configuration
gcloud compute instance-groups managed describe lab03-web-mig \
  --region=us-central1 | grep -A 10 autoscaler
```

### Step 3.5 — Manually Scale the MIG

```bash
# Scale up to 4 instances
gcloud compute instance-groups managed resize lab03-web-mig \
  --size=4 \
  --region=us-central1

# Observe instances appearing
gcloud compute instance-groups managed list-instances lab03-web-mig \
  --region=us-central1

# Scale back to 2
gcloud compute instance-groups managed resize lab03-web-mig \
  --size=2 \
  --region=us-central1
```

### Step 3.6 — Update the Instance Template (Rolling Update)

```bash
# Create an updated startup script
cat > startup-v2.sh << 'EOF'
#!/bin/bash
apt-get update -y
apt-get install -y apache2
systemctl enable apache2
systemctl start apache2
echo "<h1>Hello from $(hostname) — VERSION 2</h1>" \
  > /var/www/html/index.html
EOF

# Create a new template
gcloud compute instance-templates create lab03-web-template-v2 \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=20GB \
  --tags=http-server \
  --metadata-from-file=startup-script=startup-v2.sh

# Perform a rolling update
gcloud compute instance-groups managed rolling-action start-update lab03-web-mig \
  --version=template=lab03-web-template-v2 \
  --region=us-central1 \
  --max-unavailable=1

# Monitor the update
gcloud compute instance-groups managed list-instances lab03-web-mig \
  --region=us-central1
```

---

## Part 4 — Preemptible VM (10 minutes)

### Step 4.1 — Create a Preemptible VM

```bash
gcloud compute instances create lab03-preempt-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --preemptible \
  --no-restart-on-failure \
  --maintenance-policy=TERMINATE

# Verify preemptible status
gcloud compute instances describe lab03-preempt-vm \
  --zone=us-central1-a \
  --format='value(scheduling.preemptible)'
```

### Step 4.2 — Create a Spot VM

```bash
gcloud compute instances create lab03-spot-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --provisioning-model=SPOT \
  --instance-termination-action=STOP

gcloud compute instances describe lab03-spot-vm \
  --zone=us-central1-a \
  --format='value(scheduling.provisioningModel)'
```

---

## Lab Deliverables

Submit a lab report (PDF or Word) containing:

1. Output of `curl http://EXTERNAL_IP` showing your web page.
2. Screenshot of the startup script log showing apache2 installation.
3. Output of `gcloud compute snapshots list`.
4. Screenshot of the MIG instances list showing at least 2 RUNNING instances.
5. Output of the rolling update command and post-update instance list.
6. Output of `gcloud compute instances describe lab03-preempt-vm` showing
   the `scheduling.preemptible: true` field.
7. Answers to the lab questions.

**Lab Questions:**

1. What is the key difference between a zonal MIG and a regional MIG? When
   would you choose each?
2. Why is the `--initial-delay` parameter important when configuring
   autohealing on a MIG?
3. You need to run a data pipeline job that takes 4 hours, is fault-tolerant,
   and must minimize cost. Would you use a preemptible VM or a Spot VM? Why?
4. An instance template is immutable. Your team needs to add more memory to
   all VMs in a MIG. Describe the steps required.
5. What is the difference between stopping and deleting a Compute Engine VM
   in terms of billing and resource state?

---

## Cleanup

```bash
# Delete MIG (also deletes MIG instances)
gcloud compute instance-groups managed delete lab03-web-mig \
  --region=us-central1 --quiet

# Delete standalone VMs
gcloud compute instances delete lab03-web-vm \
  lab03-preempt-vm lab03-spot-vm \
  --zone=us-central1-a --quiet

# Delete instance templates
gcloud compute instance-templates delete lab03-web-template \
  lab03-web-template-v2 --quiet

# Delete health check
gcloud compute health-checks delete lab03-health-check --quiet

# Delete snapshot and extra disk
gcloud compute disks delete lab03-restored-disk \
  --zone=us-central1-a --quiet
gcloud compute snapshots delete $(gcloud compute snapshots list \
  --format='value(name)' | grep lab03) --quiet
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Canary Deployment with a MIG

Extend the rolling update from Part 3 to perform a canary deployment. Deploy
a new template version to only 1 instance while the remaining instances stay
on the current version, observe both versions serving traffic, then complete
the rollout.

1. Create a third startup script version that outputs `VERSION 3 — CANARY`:

```bash
cat > startup-canary.sh << 'EOF'
#!/bin/bash
apt-get update -y && apt-get install -y apache2
systemctl enable apache2 && systemctl start apache2
echo "<h1>$(hostname) — VERSION 3 CANARY</h1>" > /var/www/html/index.html
EOF

gcloud compute instance-templates create lab03-web-template-canary \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --tags=http-server \
  --metadata-from-file=startup-script=startup-canary.sh
```

1. Start a canary update targeting only 1 instance, with the rest pinned to v2:

```bash
gcloud compute instance-groups managed rolling-action start-update lab03-web-mig \
  --region=us-central1 \
  --version=template=lab03-web-template-v2,name=stable \
  --canary-version=template=lab03-web-template-canary,name=canary,target-size=1
```

1. List instances and confirm one canary and one stable instance are running:

```bash
gcloud compute instance-groups managed list-instances lab03-web-mig \
  --region=us-central1 \
  --format="table(name,instance,version.instanceTemplate,currentAction,lastAttempt.errors)"
```

1. Complete the canary rollout by updating all instances to the canary template:

```bash
gcloud compute instance-groups managed rolling-action start-update lab03-web-mig \
  --region=us-central1 \
  --version=template=lab03-web-template-canary
```

### Challenge 2: Autohealing Simulation

Force the autohealer to detect and replace an unhealthy instance by manually
breaking the health check endpoint on one VM.

1. SSH into one of the MIG instances and stop Apache:

```bash
# Identify an instance name
INSTANCE=$(gcloud compute instance-groups managed list-instances lab03-web-mig \
  --region=us-central1 --format="value(instance)" | head -1 | sed 's|.*/||')
ZONE=$(gcloud compute instances list --filter="name=$INSTANCE" \
  --format="value(zone)")

gcloud compute ssh $INSTANCE --zone=$ZONE --command="sudo systemctl stop apache2"
```

1. Watch Cloud Monitoring or poll the MIG status until the unhealthy instance is
   recreated (this may take 2–5 minutes based on health check thresholds):

```bash
watch -n 10 "gcloud compute instance-groups managed list-instances lab03-web-mig \
  --region=us-central1 --format='table(name,currentAction,instanceStatus)'"
```

### Reflection Questions

1. During the canary deployment you had one instance on the canary template and
   one on the stable template. If a load balancer were routing traffic to this
   MIG, approximately what percentage of requests would reach the canary
   instance? How does this controlled exposure help reduce risk when deploying
   new versions?
2. The autohealing initial delay is set to `120` seconds in this lab. If you set
   it to `10` seconds instead, what failure mode could occur immediately after
   a new instance is created by the MIG autoscaler?

---

End of Lab — Module 03

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

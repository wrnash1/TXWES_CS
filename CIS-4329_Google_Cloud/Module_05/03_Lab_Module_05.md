# Lab — Module 05

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: VPC — Custom Networks, Subnets, Firewall Rules, and Network Tags

### Points: 100

---

## Lab Overview

In this lab you will create a custom VPC with subnets in two regions, configure firewall rules using network tags, deploy VMs in the custom VPC, test connectivity between VMs, and verify that firewall rules correctly permit and block traffic based on tags. These skills are fundamental for the ACE exam and for designing production GCP networks.

All tasks use Cloud Shell. Complete this lab in your `txwes-gcp-lab-[your initials]` project.

Estimated completion time: 75–90 minutes.

---

## Prerequisites

- Modules 01–04 labs completed
- Compute Engine API enabled
- Active project configured in Cloud Shell

---

## Part 1: Create a Custom VPC (15 points)

### Task 1.1 — Create a Custom Mode VPC (5 points)

Create a new custom mode VPC. In custom mode, no subnets are created automatically:

```bash
gcloud compute networks create txwes-vpc \
  --subnet-mode=custom \
  --mtu=1460
```

List networks to confirm creation:

```bash
gcloud compute networks list
```

Deliverable: Screenshot of `gcloud compute networks list` showing `txwes-vpc`. Label it "Task 1.1".

### Task 1.2 — Create Subnets in Two Regions (10 points)

Create a subnet in `us-central1`:

```bash
gcloud compute networks subnets create txwes-subnet-us \
  --network=txwes-vpc \
  --region=us-central1 \
  --range=10.10.0.0/24
```

Create a second subnet in `us-east1`:

```bash
gcloud compute networks subnets create txwes-subnet-east \
  --network=txwes-vpc \
  --region=us-east1 \
  --range=10.20.0.0/24
```

List subnets to confirm both were created:

```bash
gcloud compute networks subnets list --network=txwes-vpc
```

Deliverable: Screenshot of the subnets list showing both subnets in their respective regions. Label it "Task 1.2".

---

## Part 2: Configure Firewall Rules (25 points)

### Task 2.1 — Allow Internal Traffic Between All VMs (5 points)

Allow all TCP, UDP, and ICMP traffic between VMs within the VPC (internal communication):

```bash
gcloud compute firewall-rules create txwes-allow-internal \
  --network=txwes-vpc \
  --direction=INGRESS \
  --priority=1000 \
  --action=ALLOW \
  --rules=tcp,udp,icmp \
  --source-ranges=10.10.0.0/24,10.20.0.0/24
```

Deliverable: Screenshot of the firewall rule creation success. Label it "Task 2.1".

### Task 2.2 — Allow SSH to VMs Tagged "bastion" (10 points)

Create an SSH rule that only allows port 22 access to VMs with the `bastion` tag:

```bash
gcloud compute firewall-rules create txwes-allow-ssh-bastion \
  --network=txwes-vpc \
  --direction=INGRESS \
  --priority=1000 \
  --action=ALLOW \
  --rules=tcp:22 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=bastion
```

Create an HTTP rule for VMs tagged `web-server`:

```bash
gcloud compute firewall-rules create txwes-allow-http \
  --network=txwes-vpc \
  --direction=INGRESS \
  --priority=1000 \
  --action=ALLOW \
  --rules=tcp:80 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=web-server
```

List all firewall rules for your VPC:

```bash
gcloud compute firewall-rules list --filter="network=txwes-vpc"
```

Deliverable: Screenshot showing all txwes-vpc firewall rules including the two just created. Label it "Task 2.2".

### Task 2.3 — Describe a Firewall Rule (10 points)

Describe the SSH bastion rule in detail:

```bash
gcloud compute firewall-rules describe txwes-allow-ssh-bastion
```

Review the output. Note the `targetTags`, `sourceRanges`, `direction`, and `allowed` fields.

Deliverable: Screenshot of the describe output. Label it "Task 2.3".

---

## Part 3: Deploy VMs in the Custom VPC (25 points)

### Task 3.1 — Create a Bastion VM with SSH Tag (10 points)

Create a VM in the us-central1 subnet with the `bastion` network tag:

```bash
gcloud compute instances create bastion-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --subnet=txwes-subnet-us \
  --network=txwes-vpc \
  --tags=bastion \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

List instances to confirm the VM is running:

```bash
gcloud compute instances list
```

Note the internal IP of `bastion-vm`.

Deliverable: Screenshot of the instances list showing `bastion-vm` with status RUNNING. Label it "Task 3.1".

### Task 3.2 — Create a Web Server VM (10 points)

Create a second VM in us-east1 with the `web-server` tag and a startup script installing Nginx:

```bash
gcloud compute instances create web-vm \
  --zone=us-east1-b \
  --machine-type=e2-micro \
  --subnet=txwes-subnet-east \
  --network=txwes-vpc \
  --tags=web-server \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --metadata=startup-script='#!/bin/bash
apt-get update && apt-get install -y nginx
echo "Hello from txwes-vpc web-vm" > /var/www/html/index.html'
```

Deliverable: Screenshot of the instances list showing both VMs. Label it "Task 3.2".

### Task 3.3 — Create a VM with No Tags (5 points)

Create a third VM with no network tags, to test that untagged VMs cannot receive SSH from the internet:

```bash
gcloud compute instances create internal-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --subnet=txwes-subnet-us \
  --network=txwes-vpc \
  --no-address \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

Note: `--no-address` creates the VM without an external IP. It can still communicate internally.

Deliverable: Screenshot of the instances list showing all three VMs. Label it "Task 3.3".

---

## Part 4: Test Connectivity (20 points)

### Task 4.1 — SSH into the Bastion VM (10 points)

SSH into the bastion VM using the IAP (Identity-Aware Proxy) tunnel, which uses Google's internal network and does not require an external IP firewall rule:

```bash
gcloud compute ssh bastion-vm \
  --zone=us-central1-a \
  --tunnel-through-iap
```

You may be prompted to add your SSH key — type `y` and press Enter.

Once connected, confirm the hostname:

```bash
hostname
```

Exit the SSH session:

```bash
exit
```

Deliverable: Screenshot of the hostname output inside the bastion VM SSH session. Label it "Task 4.1".

### Task 4.2 — Test Internal Communication (10 points)

Get the internal IP of `internal-vm`:

```bash
gcloud compute instances describe internal-vm \
  --zone=us-central1-a \
  --format="get(networkInterfaces[0].networkIP)"
```

SSH into the bastion VM and ping the internal VM using its internal IP:

```bash
gcloud compute ssh bastion-vm --zone=us-central1-a --tunnel-through-iap \
  --command="ping -c 3 INTERNAL_VM_IP"
```

Replace `INTERNAL_VM_IP` with the IP you retrieved. Ping should succeed because the `txwes-allow-internal` rule permits ICMP between the two subnet ranges.

Deliverable: Screenshot showing three successful ping responses. Label it "Task 4.2".

---

## Part 5: Verify Firewall Behavior (10 points)

### Task 5.1 — Confirm Web Server is Accessible on Port 80 (5 points)

Get the external IP of `web-vm`:

```bash
gcloud compute instances describe web-vm \
  --zone=us-east1-b \
  --format="get(networkInterfaces[0].accessConfigs[0].natIP)"
```

Open a browser and navigate to `http://EXTERNAL_IP`. You should see the Nginx page because `web-vm` has the `web-server` tag and the `txwes-allow-http` rule applies.

Deliverable: Screenshot of the browser showing the Nginx response. Label it "Task 5.1".

### Task 5.2 — Confirm Internal VM Has No External Access (5 points)

Verify that `internal-vm` has no external IP:

```bash
gcloud compute instances describe internal-vm \
  --zone=us-central1-a \
  --format="yaml(networkInterfaces[0])"
```

The output should show an `accessConfigs` section with no `natIP` field.

Deliverable: Screenshot of the describe output confirming no external IP. In your submission notes, explain why `internal-vm` can still communicate with other VMs internally even without an external IP. Label it "Task 5.2".

---

## Cleanup (5 points)

Delete all VMs and the custom VPC to avoid charges:

```bash
gcloud compute instances delete bastion-vm --zone=us-central1-a --quiet
gcloud compute instances delete web-vm --zone=us-east1-b --quiet
gcloud compute instances delete internal-vm --zone=us-central1-a --quiet
```

Delete firewall rules:

```bash
gcloud compute firewall-rules delete txwes-allow-internal --quiet
gcloud compute firewall-rules delete txwes-allow-ssh-bastion --quiet
gcloud compute firewall-rules delete txwes-allow-http --quiet
```

Delete subnets and VPC:

```bash
gcloud compute networks subnets delete txwes-subnet-us --region=us-central1 --quiet
gcloud compute networks subnets delete txwes-subnet-east --region=us-east1 --quiet
gcloud compute networks delete txwes-vpc --quiet
```

Deliverable: Screenshot of `gcloud compute networks list` showing only the default network remains. Label it "Cleanup".

---

## Reflection Questions

Answer in your submission document (2–4 sentences each):

1. Why is it recommended to use custom mode VPCs for production environments instead of auto mode?
2. The `txwes-allow-internal` rule allows traffic between VMs in both subnets. What specific property of the rule makes it apply to both `10.10.0.0/24` and `10.20.0.0/24`?
3. You created `internal-vm` with `--no-address`. It has no external IP, yet it could still be pinged from `bastion-vm`. Explain why this works and what would be required if `internal-vm` needed to call the Cloud Storage API.

---

## Grading Rubric

| Task | Points | Criteria |
|---|---|---|
| 1.1 Custom VPC created | 5 | Networks list shows txwes-vpc |
| 1.2 Two subnets in two regions | 10 | Subnets list shows both with correct CIDRs and regions |
| 2.1 Internal traffic firewall rule | 5 | Rule creation success message |
| 2.2 SSH bastion + HTTP rules listed | 10 | All txwes-vpc rules visible in list |
| 2.3 Firewall rule describe output | 10 | All fields (targetTags, direction, etc.) visible |
| 3.1 Bastion VM created with tag | 10 | VM RUNNING with bastion tag |
| 3.2 Web VM created with tag | 10 | Both VMs visible |
| 3.3 Internal VM with no external IP | 5 | All three VMs visible |
| 4.1 SSH into bastion VM confirmed | 10 | Hostname shown from inside VM |
| 4.2 Ping internal VM succeeds | 10 | Three successful ping responses |
| 5.1 Web VM accessible on port 80 | 5 | Browser screenshot with Nginx page |
| 5.2 Internal VM has no external IP | 5 | networkInterfaces output confirms no natIP |
| Cleanup | 5 | Networks list shows only default |
| Total | 100 | |

---

End of Lab — Module 05

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

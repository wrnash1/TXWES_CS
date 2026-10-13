# Lab: Module 15 — Hybrid DNS with Route 53 Resolver

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Lab Overview

In this lab you design and implement a hybrid DNS architecture using Route 53 Resolver. You simulate the hybrid connectivity problem: an application in a VPC needs to resolve on-premises hostnames, and on-premises clients need to resolve private AWS hostnames. You configure Route 53 Resolver Inbound and Outbound Endpoints, create Resolver Rules, test private hosted zone resolution within the VPC, and analyze the Transit Gateway topology needed to support a multi-VPC hub-and-spoke hybrid architecture.

**Estimated Time:** 75 minutes

**AWS Services Used:** Route 53 (Private Hosted Zones, Resolver), VPC, EC2, Security Groups, IAM

**Cost Estimate:** Under $1.50. Route 53 Resolver endpoints are charged at $0.125/hour each. Create and delete them within the lab session to minimize cost. One EC2 instance is used for testing.

---

## Prerequisites

- AWS account with console access
- Modules 1–14 completed
- Basic understanding of DNS (A records, name resolution, forwarding)

---

## Architecture

```text
[On-Premises Network (simulated)]       [AWS VPC: 10.0.0.0/16]
  DNS Server: 192.168.1.10              Private Hosted Zone: corp.internal
  Hostname: app01.corp.local             records: db.corp.internal -> 10.0.1.50

         |                                         |
         |  DNS Forward: corp.internal             |  Outbound Rule
         |  --> Outbound Endpoint IPs              |
         v                                         v
Route 53 Resolver                     Route 53 Outbound Endpoint
Inbound Endpoint (receives on-prem    (forwards corp.local queries to
queries about *.corp.internal)         simulated on-prem resolver)
```

In this lab, you simulate the on-premises environment using a second EC2 instance configured as a DNS client, and you test resolution using Route 53 Private Hosted Zone records.

---

## Part 1: Create the VPC and Subnets

### Step 1.1

If you have a VPC from a previous lab, use it. Otherwise:

1. Open the VPC console → **Create VPC**.
2. Select **VPC and more** (creates subnets and routing automatically).
3. IPv4 CIDR: `10.0.0.0/16`.
4. Number of Availability Zones: 2.
5. Number of public subnets: 2, private subnets: 2.
6. NAT Gateways: None (to avoid cost).
7. Name tag: `lab15-vpc`.
8. Create.

Note the VPC ID and the IDs of both private subnets.

---

## Part 2: Create a Private Hosted Zone

### Step 2.1

1. Open Route 53 → **Hosted zones → Create hosted zone**.
2. Domain name: `corp.internal`
3. Type: **Private hosted zone**.
4. VPCs to associate: select `lab15-vpc` in your current region.
5. Create hosted zone.

### Step 2.2 — Add a DNS Record

1. Inside the `corp.internal` hosted zone, choose **Create record**.
2. Record name: `db`
3. Record type: A
4. Value: `10.0.1.50` (simulated database IP).
5. TTL: 60
6. Create record.

This record simulates an internal DNS entry that AWS workloads need to resolve.

---

## Part 3: Create the Route 53 Resolver Inbound Endpoint

### Step 3.1 — Security Group for Resolver Endpoints

1. Open the EC2 console → **Security Groups → Create security group**.
2. Name: `resolver-endpoint-sg`, VPC: `lab15-vpc`.
3. Add inbound rule: Protocol UDP, Port 53, Source `10.0.0.0/16`.
4. Add inbound rule: Protocol TCP, Port 53, Source `10.0.0.0/16`.
5. Create.

### Step 3.2 — Inbound Endpoint

1. Open Route 53 → **Resolver → Inbound endpoints → Create inbound endpoint**.
2. Endpoint name: `lab15-inbound`
3. VPC: `lab15-vpc`
4. Security group: `resolver-endpoint-sg`
5. Add two IP addresses, one in each private subnet (select **Use an IP address that is automatically selected**).
6. Create endpoint.
7. Wait for the endpoint status to show **Operational** (2–3 minutes).
8. Record both IP addresses assigned to the endpoint. These are the IPs on-premises DNS servers would forward AWS-domain queries to.

---

## Part 4: Create the Route 53 Resolver Outbound Endpoint

### Step 4.1

1. Open Route 53 → **Resolver → Outbound endpoints → Create outbound endpoint**.
2. Endpoint name: `lab15-outbound`
3. VPC: `lab15-vpc`
4. Security group: `resolver-endpoint-sg`
5. Add two IP addresses, one in each private subnet (auto-select).
6. Create endpoint.
7. Wait for **Operational** status.

---

## Part 5: Create a Resolver Rule

### Step 5.1 — Forward Rule for On-Premises Domain

1. Open Route 53 → **Resolver → Rules → Create rule**.
2. Rule type: **Forward**
3. Rule name: `corp-local-forward`
4. Domain name: `corp.local`
5. Outbound endpoint: `lab15-outbound`
6. Target IP addresses: `192.168.1.10` (simulated on-premises DNS server IP).
7. Port: `53`
8. Create rule.

### Step 5.2 — Associate the Rule with the VPC

1. Open the rule `corp-local-forward`.
2. Choose **Associate VPC**.
3. Select `lab15-vpc`.
4. Associate.

This configuration means: any DNS query from within `lab15-vpc` for a hostname ending in `corp.local` will be forwarded to the on-premises DNS server at `192.168.1.10`.

---

## Part 6: Launch a Test EC2 Instance

### Step 6.1

1. Open EC2 → **Launch instance**.
2. Name: `dns-test-instance`
3. AMI: Amazon Linux 2023
4. Instance type: t3.micro
5. Key pair: Create or use an existing key pair.
6. Network: `lab15-vpc`, private subnet, auto-assign public IP: disabled.
7. Security group: Create new — allow SSH from your IP only.
8. Launch.

### Step 6.2 — Connect via Session Manager

1. Attach the IAM instance profile `AmazonSSMManagedInstanceCore` to the instance (or create an IAM role with that policy and attach it at launch).
2. Connect via Systems Manager → Session Manager (no SSH required, consistent with Module 13 lab).

---

## Part 7: Test Private Hosted Zone Resolution

### Step 7.1

In the Session Manager session on `dns-test-instance`, run:

```bash
dig db.corp.internal
```

Expected output: An A record resolving to `10.0.1.50`.

Also run:

```bash
nslookup db.corp.internal
```

Confirm the same result. Record the response in your lab document.

### Step 7.2 — Verify Default VPC DNS is Working

```bash
dig ec2.amazonaws.com
```

This should resolve to AWS public IP addresses, confirming standard internet DNS still works through the VPC resolver.

---

## Part 8: Analyze the Inbound Endpoint (Conceptual)

In a real hybrid environment with Direct Connect or VPN connectivity, the on-premises DNS server would be configured to forward queries for `corp.internal` to the Inbound Endpoint IPs you recorded in Step 3.2. Answer these questions in your lab document:

1. Draw or describe the DNS resolution path for an on-premises application resolving `db.corp.internal`. List each hop from the on-premises client to the final A record response.

2. Draw or describe the DNS resolution path for an AWS Lambda function resolving `app01.corp.local`. List each hop including which endpoint is used and which DNS server ultimately answers.

3. Why are two IP addresses required for each Resolver endpoint (one in each Availability Zone)? What would happen if you used a single IP address?

---

## Part 9: Transit Gateway Design Exercise

In your lab document (no console actions required), design a Transit Gateway topology for this scenario:

A company has four VPCs: `production`, `development`, `shared-services`, and `security`. Requirements:

- Production and development VPCs must NOT communicate directly with each other
- Both production and development must reach shared-services VPC
- All internet-bound traffic must route through the security VPC (which contains a firewall appliance) before leaving to the internet
- On-premises network connects via Direct Connect to Transit Gateway

Describe: How many Transit Gateway route tables are needed? Which attachments associate with which route table? Which routes are propagated vs. statically added?

---

## Reflection Questions

Answer in your lab submission document:

1. You created both an Inbound and Outbound Resolver endpoint. If the company only needed on-premises systems to resolve AWS private hostnames (but AWS systems did not need to resolve on-premises hostnames), which endpoint could be omitted?

2. Route 53 Resolver Rules can be shared with other AWS accounts using AWS Resource Access Manager. In an AWS Organizations environment with 20 accounts, why is centralizing Resolver Rules in a shared-services account preferable to creating the same rules in each account independently?

3. Your Private Hosted Zone is associated with `lab15-vpc`. If you had a second VPC (`lab15-vpc-2`) in the same region and wanted to resolve `db.corp.internal` from instances in that VPC, what single configuration change would you make?

---

## Cleanup

To avoid Route 53 Resolver endpoint charges ($0.125/hour each):

1. Delete Resolver Rule `corp-local-forward` (disassociate from VPC first).
2. Delete Outbound Endpoint `lab15-outbound`.
3. Delete Inbound Endpoint `lab15-inbound`.
4. Terminate EC2 instance `dns-test-instance`.
5. Delete Private Hosted Zone `corp.internal` (delete records first).
6. Delete security group `resolver-endpoint-sg`.
7. Optionally delete `lab15-vpc` if created in this lab.

---

## Submission Checklist

- Screenshot of Inbound Endpoint showing Operational status with two IP addresses
- Screenshot of Outbound Endpoint showing Operational status
- Screenshot of Resolver Rule `corp-local-forward` associated with `lab15-vpc`
- Screenshot of `dig db.corp.internal` output showing A record 10.0.1.50
- Written DNS path diagrams (questions 1 and 2 in Part 8)
- Written Transit Gateway design exercise (Part 9)
- Written answers to all three reflection questions

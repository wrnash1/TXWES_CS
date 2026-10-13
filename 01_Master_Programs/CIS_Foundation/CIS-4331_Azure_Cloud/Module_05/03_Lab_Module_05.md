# Lab Activity: Module 05 - Azure Virtual Networking

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 75-90 minutes
**Submission:** Canvas LMS — Module 05 Lab Assignment
**Prerequisite:** Azure for Students subscription, Azure CLI authenticated

---

## Learning Objectives

By completing this lab you will be able to:

- Create an Azure Virtual Network with multiple subnets using `az network vnet create`
- Create a Network Security Group and add inbound rules using `az network nsg rule create`
- Associate an NSG with a subnet
- Verify NSG rule configuration and understand rule evaluation order
- Deploy a VM into a specific VNet subnet and test network accessibility

---

## Part A: Create a Virtual Network and Subnets (25 Points)

### Step 1: Create Resource Group (3 Points)

```bash
az group create \
  --name "cis4331-lab05-[your-initials]-rg" \
  --location "eastus"
```

Include the output. Confirm `provisioningState` is `Succeeded`.

### Step 2: Create the Virtual Network with Initial Subnet (10 Points)

```bash
az network vnet create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --name "lab05-vnet" \
  --address-prefix "10.0.0.0/16" \
  --subnet-name "web-subnet" \
  --subnet-prefix "10.0.1.0/24"
```

Include the JSON output and answer:

1. The VNet address space is `10.0.0.0/16`. How many total IP addresses does this range contain?
2. The `web-subnet` uses `10.0.1.0/24`. How many usable IP addresses does this subnet provide (remember: Azure reserves 5)?
3. What Azure region is the VNet created in?

### Step 3: Add a Second Subnet (7 Points)

```bash
az network vnet subnet create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --vnet-name "lab05-vnet" \
  --name "db-subnet" \
  --address-prefix "10.0.2.0/24"
```

Include the output and answer: Can the `db-subnet` (10.0.2.0/24) and `web-subnet` (10.0.1.0/24) have overlapping address ranges? Explain why or why not.

### Step 4: List All Subnets (5 Points)

```bash
az network vnet subnet list \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --vnet-name "lab05-vnet" \
  --output table
```

Include the table output. Confirm both `web-subnet` and `db-subnet` appear.

---

## Part B: Create and Configure a Network Security Group (35 Points)

### Step 1: Create the NSG (5 Points)

```bash
az network nsg create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --name "web-nsg"
```

Include the output. Note the default rules that are automatically included.

### Step 2: Add Inbound HTTP Rule (8 Points)

```bash
az network nsg rule create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --nsg-name "web-nsg" \
  --name "allow-http" \
  --priority 100 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 80 \
  --access Allow
```

Include the output and answer:

1. The priority is set to 100. What does this mean in relation to the default deny rule at priority 65500?
2. The `--source-address-prefix "*"` means any source IP is allowed. In a production environment, what might you restrict this to instead, and why?

### Step 3: Add Inbound HTTPS Rule (5 Points)

```bash
az network nsg rule create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --nsg-name "web-nsg" \
  --name "allow-https" \
  --priority 110 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 443 \
  --access Allow
```

Include the output.

### Step 4: Add an SSH Rule for Administrative Access (7 Points)

Add an inbound rule allowing SSH (port 22) only from a specific IP range. Use `203.0.113.0/24` as the source (this is a documentation-only IP range — in production, use your actual admin IP):

```bash
az network nsg rule create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --nsg-name "web-nsg" \
  --name "allow-ssh-admin" \
  --priority 120 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefix "203.0.113.0/24" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 22 \
  --access Allow
```

Include the output and answer: Why is it a security best practice to restrict SSH access to specific source IP addresses rather than allowing it from all internet IPs (`*`)?

### Step 5: List All NSG Rules (5 Points)

```bash
az network nsg rule list \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --nsg-name "web-nsg" \
  --output table
```

Include the table output showing all custom rules you created plus the default rules.

### Step 6: Associate NSG with the Web Subnet (5 Points)

```bash
az network vnet subnet update \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --vnet-name "lab05-vnet" \
  --name "web-subnet" \
  --network-security-group "web-nsg"
```

Include the output. Take a screenshot of the subnet in the Azure Portal showing the NSG association.

---

## Part C: Deploy a VM into the VNet (25 Points)

### Step 1: Deploy a VM into the Web Subnet (15 Points)

```bash
az vm create \
  --resource-group "cis4331-lab05-[your-initials]-rg" \
  --name "lab05webvm" \
  --image "Ubuntu2204" \
  --size "Standard_B1s" \
  --admin-username "azureuser" \
  --generate-ssh-keys \
  --vnet-name "lab05-vnet" \
  --subnet "web-subnet" \
  --public-ip-sku Standard \
  --output json
```

Include the JSON output and answer:

1. What is the public IP address assigned to the VM?
2. What is the private IP address? Is it within the `web-subnet` range (10.0.1.0/24)?
3. The NSG you created allows HTTP (80) and SSH (22 from admin IP only). If you tried to SSH into this VM from a non-admin IP, what would happen? Which NSG rule would block or allow the connection?

### Step 2: Verify Network Configuration in Azure Portal (10 Points)

**[SHOW PORTAL — Navigate to the VM's Networking blade]**

Navigate to portal.azure.com and open your VM. Click "Networking" in the left menu.

Take a screenshot showing:

- The Network Interface
- The Subnet the VM is assigned to
- The NSG applied (should be `web-nsg`)
- The effective security rules listing

Include this screenshot in your submission.

---

## Part D: NSG Rule Analysis (15 Points)

Read the following NSG rule table and answer the analysis questions below.

### Given NSG Rule Table

| Priority | Name | Direction | Source | Destination | Port | Protocol | Action |
|---|---|---|---|---|---|---|---|
| 100 | allow-web | Inbound | * | * | 80, 443 | TCP | Allow |
| 200 | allow-ssh-internal | Inbound | 10.0.0.0/8 | * | 22 | TCP | Allow |
| 300 | deny-rdp | Inbound | * | * | 3389 | TCP | Deny |
| 65000 | AllowVnetInBound | Inbound | VirtualNetwork | VirtualNetwork | * | Any | Allow |
| 65500 | DenyAllInBound | Inbound | * | * | * | Any | Deny |

### Analysis Questions

1. (3 Points) A request arrives from an internet IP address (`8.8.8.8`) trying to reach port 80. Walk through the rules in priority order and identify which rule is the first to match. Is the traffic allowed or denied?

2. (3 Points) A VM in the same VNet at `10.0.1.5` tries to connect to port 22 (SSH) on the protected VM. Walk through the rules in priority order and identify which rule is the first to match. Is the traffic allowed or denied?

3. (3 Points) An internet attacker tries to connect to port 3389 (RDP — Remote Desktop Protocol). Walk through the rules and identify which rule fires first. Is the traffic allowed or denied?

4. (3 Points) An internet IP tries to reach port 8080 (a custom web application). Walk through all rules and explain what happens. Is the traffic allowed or denied?

5. (3 Points) The deny-rdp rule at priority 300 explicitly denies RDP. The DenyAllInBound rule at priority 65500 also denies all traffic. Is the deny-rdp rule at priority 300 redundant? Explain why you might or might not keep it despite the default deny-all at 65500.

---

## Resource Cleanup

Delete all lab resources:

```bash
az group delete \
  --name "cis4331-lab05-[your-initials]-rg" \
  --yes \
  --no-wait
```

Verify deletion in the Portal after 5-10 minutes.

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A: VNet and subnets creation | 25 | All commands run, outputs included, questions answered |
| Part B: NSG creation and rules | 35 | NSG created, all rules added, table output, Portal screenshot |
| Part C: VM deployment into VNet | 25 | VM created in correct subnet, Portal networking screenshot |
| Part D: NSG rule analysis questions | 15 | All 5 questions answered with accurate rule walkthrough |
| **Total** | **100** | |

---

## Troubleshooting

**VNet subnet address overlap error:** Subnet ranges must not overlap. `10.0.1.0/24` and `10.0.2.0/24` are valid (different third octets). `10.0.1.0/24` and `10.0.1.128/26` would overlap.

**NSG association fails:** Verify the NSG and subnet are in the same resource group and the names match exactly (case-sensitive in some CLI versions).

**VM does not get an IP in the correct subnet:** Verify the `--vnet-name` and `--subnet` parameters exactly match the names you created.

---

## Part 9 — Challenge Exercise

### Challenge 1: NSG Flow Log Analysis
Enable NSG flow logs on the NSG you created in the lab. Use `az network watcher flow-log create` to configure flow logging to an Azure Storage account (create a Basic storage account using `az storage account create` if needed). Generate some traffic by accessing the VM or attempting a blocked connection, then wait 5–10 minutes for logs to appear. Download a raw flow log JSON blob from the storage account and manually identify one allowed and one denied flow entry in the log. Document the source IP, destination IP, destination port, protocol, and decision (A=allow, D=deny) for each entry. Clean up the flow log configuration and storage account when complete.

### Challenge 2: Hub-and-Spoke Peering with Route Verification
Without deploying a firewall, build a minimal hub-and-spoke topology: create three VNets (one hub, two spokes) with non-overlapping address spaces, peer each spoke to the hub with `allowForwardedTraffic` enabled, and attempt to reach a VM in Spoke B from a VM in Spoke A via the hub. Document whether traffic flows and explain why it does or does not succeed without UDRs and a network virtual appliance in the hub. Specify exactly what additional Azure resource and configuration would be required to make spoke-to-spoke traffic flow through the hub.

### Reflection Questions
1. In the lab you created an NSG rule allowing SSH (port 22) from any source. In a production environment, why is `*` (any) an inappropriate source for SSH access, and what two NSG source configurations would be more secure? What Azure service eliminates the need for inbound SSH rules entirely?
2. VNet peering is described as non-transitive — traffic between Spoke A and Spoke B does not automatically flow through the Hub VNet. What is the architectural implication of this for organizations with dozens of spoke VNets? How does the hub-and-spoke pattern with Azure Firewall or an NVA address this limitation, and what is the trade-off in terms of latency and cost?

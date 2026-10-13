# Lab Activity: Module 08 — Azure Networking

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 100 | AZ-900 Alignment: Describe Azure networking services

---

## Lab Overview

In this lab you will build a segmented Azure network from scratch. You will create a Virtual Network with two subnets, deploy a Linux VM into the web subnet, create and configure a Network Security Group, and test traffic filtering by allowing and blocking specific ports. This lab gives you hands-on experience with the foundational networking constructs used in every real Azure architecture.

**Estimated Time:** 60–75 minutes

**Prerequisites:**

- Active Azure account (free trial or student subscription)
- Azure Cloud Shell access
- Completion of Lab Module 07 (familiarity with VM creation)

---

## Learning Objectives

By completing this lab you will be able to:

- Create an Azure Virtual Network with multiple subnets
- Deploy a VM into a specific subnet
- Create and configure a Network Security Group
- Associate an NSG with a subnet
- Test NSG rule enforcement by attempting blocked and allowed connections
- Interpret NSG effective security rules

---

## Part 1: Create the Resource Group and Virtual Network (10 minutes)

**Step 1.1 — Create the Resource Group**

Open Azure Cloud Shell (Bash) and run:

```bash
az group create \
  --name lab08-rg \
  --location eastus
```

**Step 1.2 — Create the Virtual Network**

Create a VNet with a 10.0.0.0/16 address space and a first subnet for the web tier:

```bash
az network vnet create \
  --resource-group lab08-rg \
  --name lab08-vnet \
  --address-prefix 10.0.0.0/16 \
  --subnet-name web-subnet \
  --subnet-prefix 10.0.1.0/24
```

**Step 1.3 — Add a Second Subnet**

Add a backend subnet for the application tier:

```bash
az network vnet subnet create \
  --resource-group lab08-rg \
  --vnet-name lab08-vnet \
  --name app-subnet \
  --address-prefix 10.0.2.0/24
```

**Step 1.4 — Verify the VNet**

```bash
az network vnet show \
  --resource-group lab08-rg \
  --name lab08-vnet \
  --output table
```

```bash
az network vnet subnet list \
  --resource-group lab08-rg \
  --vnet-name lab08-vnet \
  --output table
```

Confirm both subnets (web-subnet and app-subnet) are listed with correct address prefixes.

[SHOW AZURE PORTAL] Navigate to Virtual Networks > lab08-vnet > Subnets. Show both subnets in the Portal view.

---

## Part 2: Create and Configure a Network Security Group (15 minutes)

**Step 2.1 — Create the NSG**

```bash
az network nsg create \
  --resource-group lab08-rg \
  --name lab08-web-nsg
```

**Step 2.2 — View Default NSG Rules**

```bash
az network nsg show \
  --resource-group lab08-rg \
  --name lab08-web-nsg \
  --output table
```

Note the three default inbound rules: AllowVnetInBound (65000), AllowAzureLoadBalancerInBound (65001), and DenyAllInBound (65500).

**Step 2.3 — Add Rule: Allow SSH (Port 22)**

```bash
az network nsg rule create \
  --resource-group lab08-rg \
  --nsg-name lab08-web-nsg \
  --name AllowSSH \
  --protocol tcp \
  --direction inbound \
  --priority 100 \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 22 \
  --access allow
```

**Step 2.4 — Add Rule: Allow HTTP (Port 80)**

```bash
az network nsg rule create \
  --resource-group lab08-rg \
  --nsg-name lab08-web-nsg \
  --name AllowHTTP \
  --protocol tcp \
  --direction inbound \
  --priority 110 \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 80 \
  --access allow
```

**Step 2.5 — Add Rule: Deny HTTPS (Port 443) — Explicit Deny for Testing**

```bash
az network nsg rule create \
  --resource-group lab08-rg \
  --nsg-name lab08-web-nsg \
  --name DenyHTTPS \
  --protocol tcp \
  --direction inbound \
  --priority 120 \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 443 \
  --access deny
```

**Step 2.6 — Associate the NSG with the web-subnet**

```bash
az network vnet subnet update \
  --resource-group lab08-rg \
  --vnet-name lab08-vnet \
  --name web-subnet \
  --network-security-group lab08-web-nsg
```

**Step 2.7 — Verify NSG Rules**

```bash
az network nsg rule list \
  --resource-group lab08-rg \
  --nsg-name lab08-web-nsg \
  --output table
```

[SHOW AZURE PORTAL] Navigate to Network Security Groups > lab08-web-nsg > Inbound security rules. Show the three custom rules alongside the three default rules.

---

## Part 3: Deploy a VM into the web-subnet (15 minutes)

**Step 3.1 — Create the VM in the web-subnet**

```bash
az vm create \
  --resource-group lab08-rg \
  --name lab08-web-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s \
  --vnet-name lab08-vnet \
  --subnet web-subnet \
  --public-ip-sku Standard \
  --nsg ""
```

The `--nsg ""` flag prevents Azure from creating a new default NSG on the NIC — the subnet NSG (lab08-web-nsg) will be the only NSG in effect.

**Step 3.2 — Get the Public IP**

```bash
az vm show \
  --resource-group lab08-rg \
  --name lab08-web-vm \
  --show-details \
  --query publicIps \
  --output tsv
```

Note the public IP address for use in subsequent steps.

**Step 3.3 — SSH Into the VM and Install nginx**

```bash
# Replace <IP> with the public IP from Step 3.2
ssh -o StrictHostKeyChecking=no azureuser@<IP>
```

Once connected:

```bash
sudo apt-get update -y && sudo apt-get install -y nginx
sudo systemctl start nginx
sudo systemctl status nginx
exit
```

---

## Part 4: Test NSG Rule Enforcement (10 minutes)

**Step 4.1 — Test HTTP (port 80) — Should Succeed**

Open a browser and navigate to `http://<IP>`. You should see the nginx welcome page. This confirms the AllowHTTP rule (priority 110) is working.

**Step 4.2 — Test SSH (port 22) — Should Succeed**

From Cloud Shell:

```bash
ssh -o StrictHostKeyChecking=no azureuser@<IP>
```

You should successfully connect, confirming the AllowSSH rule (priority 100) is working. Type `exit` to disconnect.

**Step 4.3 — Review Effective Security Rules**

In the Azure Portal:

1. Navigate to the `lab08-web-vm` > **Networking** tab
2. Click **Effective security rules**
3. Review the merged view of both NIC-level and subnet-level NSG rules
4. Take a screenshot of this view for your deliverables

[SHOW AZURE PORTAL] Show the Effective Security Rules panel. Point out how Azure merges NIC-level and subnet-level rules and displays the effective combined rule set.

---

## Part 5: Modify NSG Rules (10 minutes)

**Step 5.1 — Remove the HTTP Allow Rule**

You will simulate an administrator inadvertently removing the HTTP allow rule and test the effect:

```bash
az network nsg rule delete \
  --resource-group lab08-rg \
  --nsg-name lab08-web-nsg \
  --name AllowHTTP
```

**Step 5.2 — Test HTTP Access**

Reload `http://<IP>` in your browser. The page should time out or refuse connection — the HTTP rule is gone, and the DenyAllInBound default rule (65500) now blocks port 80.

**Step 5.3 — Re-add the HTTP Allow Rule**

```bash
az network nsg rule create \
  --resource-group lab08-rg \
  --nsg-name lab08-web-nsg \
  --name AllowHTTP \
  --protocol tcp \
  --direction inbound \
  --priority 110 \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 80 \
  --access allow
```

Reload the browser — nginx welcome page should reappear.

---

## Part 6: Reflection Questions (5 minutes)

Answer in your lab submission document (2–3 sentences each):

**Question 1:** The default DenyAllInBound rule has priority 65500 and blocks all traffic not matched by a higher-priority rule. Why is it important that custom allow rules use priorities lower than 65500? What would happen if you accidentally set a priority of 70000?

**Question 2:** You associated the NSG with the subnet rather than with the individual VM's NIC. What is the difference in effect? When might you want to apply an NSG at the NIC level instead of the subnet level?

**Question 3:** In Step 5, removing the AllowHTTP rule immediately blocked web traffic. What does this demonstrate about NSG evaluation logic? How does this behavior differ from a traditional on-premises firewall where changes may require a service restart?

---

## Part 7: Cleanup Resources (5 minutes)

```bash
az group delete \
  --name lab08-rg \
  --yes \
  --no-wait
```

---

## Deliverables

Submit the following to Canvas:

1. **Screenshot 1** — Cloud Shell output of `az network vnet subnet list` showing both subnets with correct prefixes
2. **Screenshot 2** — Azure Portal showing NSG inbound rules (with your three custom rules visible)
3. **Screenshot 3** — Browser showing nginx welcome page at the VM's public IP (confirming HTTP allowed)
4. **Screenshot 4** — Azure Portal showing Effective Security Rules for lab08-web-vm
5. **Screenshot 5** — Browser showing connection failure after removing AllowHTTP rule
6. **Reflection Document** — Answers to the three reflection questions

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Screenshot 1: Both subnets created with correct prefixes | 10 |
| Screenshot 2: NSG with three custom rules visible | 20 |
| Screenshot 3: nginx welcome page in browser | 15 |
| Screenshot 4: Effective Security Rules in Portal | 20 |
| Screenshot 5: Browser failure after AllowHTTP deleted | 10 |
| Reflection Q1: Rule priority explanation | 8 |
| Reflection Q2: Subnet vs. NIC NSG difference | 8 |
| Reflection Q3: NSG evaluation logic | 9 |
| **Total** | **100** |

---

## Troubleshooting Tips

**VM creation fails with NSG error:** The `--nsg ""` parameter requires an empty string. If it fails, omit the `--nsg` parameter entirely and delete the auto-created NSG afterward from the NIC.

**SSH connection refused:** Verify the AllowSSH rule was created with priority 100 and direction "inbound." Also verify the VM's public IP is correct using `az vm show --show-details`.

**nginx page shows after AllowHTTP deleted:** Browser caching may show the old page. Open a private/incognito window and try again, or wait 30 seconds for the rule to propagate.

**Effective Security Rules panel is empty:** The panel may take 30–60 seconds to populate after NSG association. Refresh the page.

---

*Lab 08 — Module 08: Azure Networking | CIS-4331 | Texas Wesleyan University*

---

## Part 9 — Challenge Exercise

### Challenge 1: VNet Peering and Connectivity Test
Create a second VNet (`lab08-vnet-b`, address space `10.1.0.0/16`) with one subnet (`10.1.1.0/24`) in the same resource group. Deploy a second VM (`lab08-vm-b`) into this VNet with no public IP. Establish VNet peering between `lab08-vnet` and `lab08-vnet-b` in both directions using `az network vnet peering create`. From `lab08-web-vm`, attempt to ping `lab08-vm-b`'s private IP address. If the ping fails, diagnose why (check NSG rules on both subnets — ICMP may be blocked by default). Add an NSG rule to allow ICMP if needed. Document all commands, their outputs, and whether ping succeeds after each configuration change. Explain in 2–3 sentences what "non-transitive" peering means and how it would affect a scenario with three VNets (A, B, C) where A is peered to B and B is peered to C but A is not peered to C.

### Challenge 2: NSG Flow Logs and Effective Security Rules
Enable Network Watcher in the East US region using `az network watcher configure --enabled true --locations eastus`. Use `az network watcher show-effective-nsg --vm lab08-web-vm --resource-group lab08-rg` to retrieve the effective NSG rules for the VM. Compare the CLI output to what you saw in the Portal's Effective Security Rules panel. Add a new inbound NSG rule that allows HTTPS (port 443) from any source at priority 120. Then use `az network watcher test-connectivity` to test whether a connection from the VM to an external HTTPS endpoint (e.g., `microsoft.com:443`) would be allowed or denied. Document all commands and outputs and explain how the `test-connectivity` command differs from actually making a network connection.

### Reflection Questions
1. In this lab, you associated the NSG with the subnet rather than with individual VM NICs. A colleague suggests always attaching NSGs to NICs instead of subnets because it gives more granular per-VM control. Describe a specific scenario where NIC-level NSG attachment is genuinely required (a scenario that subnet-level NSGs cannot handle), and a scenario where subnet-level association is clearly superior.
2. The lab demonstrated that deleting an NSG allow rule immediately blocked traffic without any service restart. Azure NSGs are stateful — when an outbound connection is allowed, the corresponding inbound response is automatically permitted. Explain how stateful packet inspection in NSGs simplifies rule management compared to stateless packet filtering, and describe what additional rules would be required if Azure NSGs were stateless.

# Lab Activity: Module 07 — Azure Compute Services

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 100 | AZ-900 Alignment: Describe Azure compute and networking services

---

## Lab Overview

In this lab you will provision two foundational Azure compute resources: a Linux Virtual Machine and an Azure App Service web application. You will connect to the VM using SSH, install a web server, and deploy a sample application to App Service. This hands-on experience reinforces the IaaS vs. PaaS distinction that is central to the AZ-900 exam.

**Estimated Time:** 60–75 minutes

**Prerequisites:**

- Active Azure account (free trial or student subscription)
- Azure Cloud Shell access (no local install required)
- Basic familiarity with the Azure Portal

---

## Learning Objectives

By completing this lab you will be able to:

- Create and configure a Linux VM in the Azure Portal
- Connect to a VM using SSH from Azure Cloud Shell
- Install and verify a web server on an Azure VM
- Create an App Service Plan and Web App using Azure CLI
- Deploy a sample application using zip deploy
- Articulate the IaaS vs. PaaS management differences

---

## Part 1: Create a Resource Group (5 minutes)

All Azure resources require a resource group. You will use one resource group for the entire lab.

**Step 1.1 — Open the Azure Portal**

Navigate to portal.azure.com and sign in with your Azure credentials.

**Step 1.2 — Create the Resource Group**

1. In the search bar, type **Resource groups** and select it
2. Click **+ Create**
3. Fill in the form:
   - Subscription: your active subscription
   - Resource group name: `lab07-rg`
   - Region: East US
4. Click **Review + create**, then **Create**

```bash
# Alternative: Create the resource group using Azure CLI in Cloud Shell
az group create \
  --name lab07-rg \
  --location eastus
```

---

## Part 2: Create a Linux Virtual Machine (20 minutes)

**Step 2.1 — Navigate to Virtual Machines**

1. In the Azure Portal search bar, type **Virtual machines** and select it
2. Click **+ Create** > **Azure virtual machine**

**Step 2.2 — Configure Basics**

Fill in the Basics tab with the following values:

- Subscription: your subscription
- Resource group: `lab07-rg`
- Virtual machine name: `lab07-vm`
- Region: (US) East US
- Availability options: No infrastructure redundancy required
- Image: Ubuntu Server 22.04 LTS — x64 Gen2
- Size: Standard_B1s (1 vCPU, 1 GiB RAM — free tier eligible)
- Authentication type: SSH public key
- Username: `azureuser`
- SSH public key source: Generate new key pair
- Key pair name: `lab07-key`

**Step 2.3 — Configure Inbound Port Rules**

On the Basics tab, under Inbound port rules:

- Public inbound ports: Allow selected ports
- Select inbound ports: **SSH (22)** and **HTTP (80)**

**Step 2.4 — Review and Create**

1. Click **Next: Disks** and leave defaults (Standard SSD, OS disk only)
2. Click **Next: Networking** and leave defaults (new VNet will be created)
3. Click **Review + create**
4. Review the summary and click **Create**
5. When the key pair dialog appears, click **Download private key and create resource**
6. Save the `.pem` file to your local machine

**Step 2.5 — Wait for Deployment**

Deployment takes 2–3 minutes. When complete, click **Go to resource**.

```bash
# Alternative: Create VM using Azure CLI (Cloud Shell)
az vm create \
  --resource-group lab07-rg \
  --name lab07-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s \
  --public-ip-sku Standard
```

---

## Part 3: Connect to the VM and Install a Web Server (15 minutes)

**Step 3.1 — Note the Public IP Address**

On the VM Overview page, copy the **Public IP address**. You will use this to SSH into the VM.

**Step 3.2 — Open Azure Cloud Shell**

1. In the Azure Portal, click the **Cloud Shell** icon (terminal icon in the top navigation bar)
2. Select **Bash** when prompted
3. If prompted to create storage, click **Create storage**

**Step 3.3 — Upload Your SSH Key**

1. In Cloud Shell, click the **Upload/Download files** icon (paperclip icon)
2. Select **Upload** and upload your `lab07-key.pem` file
3. Set correct file permissions:

```bash
chmod 400 ~/lab07-key.pem
```

**Step 3.4 — SSH Into the VM**

Replace `<YOUR_PUBLIC_IP>` with the IP address from Step 3.1:

```bash
ssh -i ~/lab07-key.pem azureuser@<YOUR_PUBLIC_IP>
```

Type `yes` when prompted to accept the host fingerprint. You are now connected to your Azure VM.

**Step 3.5 — Install and Start nginx**

Run the following commands inside the SSH session:

```bash
# Update package index
sudo apt-get update -y

# Install nginx web server
sudo apt-get install -y nginx

# Start nginx and enable it to start on reboot
sudo systemctl start nginx
sudo systemctl enable nginx

# Verify nginx is running (look for "active (running)")
sudo systemctl status nginx
```

**Step 3.6 — Verify the Web Server**

Open a new browser tab and navigate to `http://<YOUR_PUBLIC_IP>`. You should see the default nginx welcome page reading "Welcome to nginx!" This confirms your VM is running and publicly accessible on port 80.

**Step 3.7 — Exit the SSH Session**

```bash
exit
```

You are now back in Azure Cloud Shell.

---

## Part 4: Create an App Service Web App (15 minutes)

**Step 4.1 — Create an App Service Plan**

In Azure Cloud Shell, run the following command:

```bash
az appservice plan create \
  --name lab07-plan \
  --resource-group lab07-rg \
  --sku B1 \
  --is-linux \
  --location eastus
```

The B1 (Basic) tier provides dedicated compute at low cost. The `--is-linux` flag creates a Linux-based plan.

**Step 4.2 — Create the Web App**

Replace `[initials]` with your actual initials to ensure a globally unique app name:

```bash
az webapp create \
  --name lab07webapp[initials] \
  --resource-group lab07-rg \
  --plan lab07-plan \
  --runtime "NODE|18-lts"
```

**Step 4.3 — Get the Web App URL**

```bash
az webapp show \
  --name lab07webapp[initials] \
  --resource-group lab07-rg \
  --query "defaultHostName" \
  --output tsv
```

Navigate to the returned URL (it will be `https://lab07webapp[initials].azurewebsites.net`). You should see the Azure App Service default placeholder page.

**Step 4.4 — Create and Deploy a Sample Application**

```bash
# Create a project directory
mkdir ~/lab07site && cd ~/lab07site

# Create index.html
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CIS-4331 Lab 07 - Azure App Service</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; padding: 60px; background: #f0f0f0; }
    h1 { color: #0078d4; }
  </style>
</head>
<body>
  <h1>Hello from Azure App Service!</h1>
  <p>Deployed by: [Your Full Name]</p>
  <p>Texas Wesleyan University — CIS-4331 Azure Cloud Computing</p>
  <p>Module 07: Azure Compute Services</p>
</body>
</html>
EOF

# Package the application
zip lab07site.zip index.html
```

```bash
# Deploy using zip deploy
az webapp deployment source config-zip \
  --name lab07webapp[initials] \
  --resource-group lab07-rg \
  --src ~/lab07site/lab07site.zip
```

**Step 4.5 — Verify the Deployment**

Refresh the App Service URL in your browser. You should now see your custom HTML page with your name and course information.

---

## Part 5: Reflection — IaaS vs. PaaS (5 minutes)

Answer the following questions in your submission document. Write 2–3 sentences per question.

**Question 1:** When you deployed nginx to the VM, you had to SSH in, run package manager commands, and manually start the service. When you deployed to App Service, you only created a zip file and ran one CLI command. What does this difference illustrate about the IaaS vs. PaaS responsibility model?

**Question 2:** Who is responsible for patching the Ubuntu operating system on your VM? Who is responsible for patching the underlying OS on the App Service plan? How does this affect the security posture of each environment?

**Question 3:** If your App Service app suddenly received 10 times its normal traffic, what Azure feature would allow it to scale automatically? How would you achieve the same result with a single VM, and why is that more complex?

---

## Part 6: Cleanup Resources (5 minutes)

To avoid ongoing charges, delete all resources created in this lab.

```bash
# Delete the resource group and all resources within it
az group delete \
  --name lab07-rg \
  --yes \
  --no-wait
```

Confirm the deletion has begun by checking the Azure Portal under Resource groups. The `--no-wait` flag returns control immediately while deletion runs in the background.

---

## Deliverables

Submit the following items to Canvas by the due date:

1. **Screenshot 1** — Azure Portal showing `lab07-vm` in the Running state with the public IP address visible
2. **Screenshot 2** — Browser showing the nginx default welcome page at your VM's public IP
3. **Screenshot 3** — Browser showing your custom HTML page at the App Service URL (with your name visible)
4. **Screenshot 4** — Cloud Shell showing successful output of the `az webapp deployment source config-zip` command
5. **Reflection Document** — Written answers to the three reflection questions in Part 5

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Screenshot 1: VM in Running state with public IP | 15 |
| Screenshot 2: nginx welcome page in browser | 15 |
| Screenshot 3: Custom HTML page on App Service URL | 20 |
| Screenshot 4: Successful zip deploy CLI output | 20 |
| Reflection Q1: IaaS vs. PaaS explanation | 10 |
| Reflection Q2: OS patching responsibility | 10 |
| Reflection Q3: Scaling comparison | 10 |
| **Total** | **100** |

---

## Troubleshooting Tips

**Cannot SSH into VM:** Verify the Network Security Group allows inbound TCP port 22. In the Portal, go to VM > Networking and check inbound port rules. Ensure the source is set to Any or your specific IP.

**nginx not showing in browser:** Verify the NSG allows inbound TCP port 80. Also confirm nginx is running with `sudo systemctl status nginx`. The service may have failed to start if there was a package conflict.

**App Service deployment fails with name conflict:** Azure app names must be globally unique across all Azure customers. Add more characters (e.g., your full name or a random number) to make the name unique.

**Cloud Shell session times out:** Cloud Shell sessions timeout after 20 minutes of inactivity. Simply re-open Cloud Shell — your uploaded files and created directories persist in the Cloud Shell storage mount.

---

*Lab 07 — Module 07: Azure Compute Services | CIS-4331 | Texas Wesleyan University*

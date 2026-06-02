# Lab Activity: Module 04 - Azure Container Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 45-60 minutes
**Submission:** Canvas LMS — Module 04 Lab Assignment
**Prerequisite:** Azure for Students subscription, Azure CLI installed and authenticated

---

## Learning Objectives

By completing this lab you will be able to:

- Deploy a container to Azure Container Instances using Azure CLI
- Check container status and retrieve the public access URL
- View live container logs from the CLI
- Observe the speed advantage of containers compared to VMs
- Delete container instances and clean up resources

---

## Part A: Deploy Your First Azure Container Instance (40 Points)

### Step 1: Create a Resource Group (5 Points)

```bash
az group create \
  --name "cis4331-lab04-[your-initials]-rg" \
  --location "eastus" \
  --tags "course=CIS4331" "module=04"
```

Include the JSON output in your submission. Note the time this command completes — you will compare it to your VM creation time from Module 03.

### Step 2: Deploy the Hello World Container (15 Points)

Deploy Microsoft's sample web container. Replace `[your-initials]` with your initials (lowercase, no spaces):

```bash
az container create \
  --resource-group "cis4331-lab04-[your-initials]-rg" \
  --name "lab04container[your-initials]" \
  --image "mcr.microsoft.com/azuredocs/aci-helloworld" \
  --dns-name-label "lab04hw[your-initials]" \
  --ports 80 \
  --output json
```

Note the time when this command completes. Include the full JSON output in your submission and answer:

1. How many seconds did container deployment take? Compare this to your Module 03 VM creation time. What does this difference illustrate about container startup speed?
2. What is the `"fqdn"` value in the `"ipAddress"` section? This is the URL where your container is publicly accessible.
3. What is the value of `"instanceView.currentState.state"`? What does this indicate?

### Step 3: Verify the Container in a Browser (10 Points)

Open a web browser and navigate to the FQDN from Step 2 (the URL will be in the format `lab04hw[your-initials].eastus.azurecontainer.io`).

Take a screenshot showing:

- The browser address bar with the full URL
- The "Welcome to Azure Container Instances!" page content

Include this screenshot in your submission.

### Step 4: Check Container Status via CLI (10 Points)

```bash
az container show \
  --resource-group "cis4331-lab04-[your-initials]-rg" \
  --name "lab04container[your-initials]" \
  --query "{Name:name, Status:instanceView.currentState.state, FQDN:ipAddress.fqdn, CPU:containers[0].resources.requests.cpu, Memory:containers[0].resources.requests.memoryInGb}" \
  --output table
```

Include the table output and answer:

1. How much CPU (in vCPUs) is allocated to this container by default?
2. How much memory (in GB) is allocated by default?
3. Based on the ACI per-second billing model, is a container with these default resource allocations more or less expensive per hour than a Standard_B1s VM? Explain your reasoning.

---

## Part B: Container Logs and Monitoring (25 Points)

### Step 1: View Container Logs (10 Points)

```bash
az container logs \
  --resource-group "cis4331-lab04-[your-initials]-rg" \
  --name "lab04container[your-initials]"
```

Refresh the container's web page in your browser 3-5 times to generate HTTP request log entries, then run the logs command again.

Include both log outputs in your submission (before and after browser refreshes) and answer:

1. What do the log entries show after your browser page refreshes? What does this confirm about the container serving HTTP requests?
2. Container logs are ephemeral — they are lost when the container is deleted. How does this differ from logs on a virtual machine, where logs persist on the OS disk after the VM is stopped?

### Step 2: Restart the Container (5 Points)

```bash
az container restart \
  --resource-group "cis4331-lab04-[your-initials]-rg" \
  --name "lab04container[your-initials]"
```

After the restart completes, verify the container is running again:

```bash
az container show \
  --resource-group "cis4331-lab04-[your-initials]-rg" \
  --name "lab04container[your-initials]" \
  --query "instanceView.currentState.state" \
  --output tsv
```

Include both command outputs. Answer: Is the container accessible at the same FQDN after restart? Why or why not?

### Step 3: Deploy a Second Container with Custom Resource Allocation (10 Points)

Deploy a second container with explicit CPU and memory settings:

```bash
az container create \
  --resource-group "cis4331-lab04-[your-initials]-rg" \
  --name "lab04container2[your-initials]" \
  --image "mcr.microsoft.com/azuredocs/aci-helloworld" \
  --dns-name-label "lab04hw2[your-initials]" \
  --ports 80 \
  --cpu 0.5 \
  --memory 1 \
  --output json
```

Include the output and answer:

1. This container was configured with 0.5 vCPU and 1 GB memory. The default container in Step A had 1 vCPU and 1.5 GB memory. If both containers run for exactly 1 hour, which costs more? (Use the approximate ACI rate of $0.0000149 per vCPU-second and $0.0000015 per GB-second to calculate.)
2. Show your calculation for both containers' 1-hour cost.

---

## Part C: Container Service Selection Analysis (25 Points)

For each scenario below, identify the most appropriate Azure container service: ACI, AKS, Container Apps, or App Service with container. Provide a 3-4 sentence justification citing specific characteristics from the reading guide.

### Scenario 1 (5 Points)

A marketing team needs to run a nightly data processing job that reads customer data from Azure Blob Storage, generates a report, and uploads it to SharePoint. The job takes 15-20 minutes to complete and must run at 2 AM each night. No human interaction is needed during the job.

**Your selection and justification:**

### Scenario 2 (5 Points)

A financial services company is building a new trading platform consisting of 12 microservices: order intake, risk analysis, market data feed, execution engine, notification service, audit logger, and 6 supporting services. The platform requires zero-downtime rolling deployments, horizontal scaling for individual services, and strong network isolation between services.

**Your selection and justification:**

### Scenario 3 (5 Points)

A startup is deploying their first web API built in Node.js. The team has no container orchestration experience. They need built-in SSL certificate management, custom domain support, and deployment slots (staging/production) for safe releases. The API runs as a single container.

**Your selection and justification:**

### Scenario 4 (5 Points)

A game development company builds a game matchmaking service. The service needs to scale from zero (no players) to thousands of requests per second during peak hours, then back to zero. The team wants to pay nothing during off-hours and does not want to manage Kubernetes clusters.

**Your selection and justification:**

### Scenario 5 (5 Points)

An enterprise security team wants to store their internally developed Docker container images for use by multiple development teams. They need role-based access control so that only authorized developers can push new images, and they want vulnerability scanning before images are deployed to production.

**Your selection and justification:**

---

## Part D: Resource Cleanup (10 Points)

Delete all resources to prevent ongoing charges:

```bash
az group delete \
  --name "cis4331-lab04-[your-initials]-rg" \
  --yes \
  --no-wait
```

After approximately 3-5 minutes, verify deletion:

```bash
az group list --output table
```

Confirm the lab resource group no longer appears. Include the output in your submission.

Answer: Why is cleaning up container resources equally important to cleaning up VM resources, even though ACI billing is per-second rather than per-hour?

---

## Submission Requirements

1. Resource group creation output (Part A, Step 1)
2. Container creation JSON output and three questions answered (Part A, Step 2)
3. Browser screenshot of Hello World page (Part A, Step 3)
4. Container status table output and three questions answered (Part A, Step 4)
5. Container logs before and after page refreshes, with questions answered (Part B, Step 1)
6. Restart command outputs and question answered (Part B, Step 2)
7. Second container creation output, cost calculation, and answers (Part B, Step 3)
8. All five container service selection analyses (Part C)
9. Deletion verification output and question answered (Part D)

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A: Resource group creation | 5 | Output included |
| Part A: Container creation + questions | 15 | Output included, all 3 questions answered accurately |
| Part A: Browser screenshot | 10 | Screenshot shows URL and page content |
| Part A: Container status + questions | 10 | Table output, all 3 questions answered with cost reasoning |
| Part B: Logs before/after + questions | 10 | Both log outputs, both questions answered |
| Part B: Restart verification | 5 | Both command outputs, question answered |
| Part B: Second container + cost calculation | 10 | Output, calculation shown, correct math |
| Part C: Five scenario selections | 25 | Each selection correct (3 pts) with adequate justification (2 pts) |
| Part D: Cleanup verification + question | 10 | Output shows group deleted, question answered |
| **Total** | **100** | |

---

## Troubleshooting

**DNS name label already taken:** DNS labels must be globally unique within a region. If `lab04hw[your-initials]` is taken, add a random 3-digit number: `lab04hw[your-initials]123`.

**Container stays in "Pending" state:** Wait 60-90 seconds and check status again. If still pending after 2 minutes, try a different region.

**Browser shows "This site can't be reached":** The container may still be starting. Wait 30 seconds and refresh. Also ensure you are using `http://` not `https://` — the Hello World container only exposes port 80 (HTTP).

**Cost calculation note:** ACI pricing may vary by region and over time. Use the rates provided in Step B3 for this lab calculation, or retrieve current rates from the Azure Pricing Calculator at learn.microsoft.com.

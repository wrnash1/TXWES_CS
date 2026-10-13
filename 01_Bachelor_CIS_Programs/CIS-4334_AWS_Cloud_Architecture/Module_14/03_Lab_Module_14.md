# Lab: Module 14 — AWS Cost Optimization Tools

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Lab Overview

In this lab you work with AWS cost management tools to analyze spending, configure budget alerts, apply cost allocation tags, create an S3 Lifecycle policy, and review Compute Optimizer recommendations. The lab emphasizes hands-on experience with the cost visibility and control tools tested on the SAA-C03 exam.

**Estimated Time:** 60 minutes

**AWS Services Used:** AWS Cost Explorer, AWS Budgets, S3, AWS Compute Optimizer, IAM (for tagging), AWS Billing and Cost Management

**Cost Estimate:** $0. All actions in this lab use existing account data and free-tier resources. Creating an S3 bucket with a lifecycle policy incurs no cost if the bucket is empty.

---

## Prerequisites

- AWS account with at least 30 days of billing history (for meaningful Cost Explorer data)
- IAM user with Billing console access (requires `ViewBilling` and `ModifyBillingService` permissions, or Administrator access)
- At least one EC2 instance running (or previously run) for Compute Optimizer data

---

## Part 1: Explore AWS Cost Explorer

### Step 1.1 — Open Cost Explorer

1. Sign in to the AWS Management Console.
2. Navigate to **Billing and Cost Management → Cost Explorer**.
3. If prompted, enable Cost Explorer (it takes up to 24 hours to populate for new activations).

### Step 1.2 — Daily Spend by Service

1. In Cost Explorer, set the time range to **Last 3 months**.
2. Set **Group by**: Service.
3. Set **Granularity**: Monthly.
4. Identify your top three spending services.

Record in your lab document:

- Top 3 services by spend
- The month with the highest total spend
- Whether spend is trending up, down, or flat

### Step 1.3 — Savings Plan and RI Coverage

1. In Cost Explorer, navigate to **Savings Plans → Coverage** (left navigation).
2. If you have no Savings Plans, the coverage will show 0% — note this as an optimization opportunity.
3. Navigate to **Reserved Instances → Utilization** and review any RI utilization data.
4. Note any underutilized RIs (utilization below 80%) or uncovered On-Demand hours.

### Step 1.4 — Cost Forecast

1. Return to the main Cost Explorer view.
2. Set **Granularity** to Monthly and extend the date range to include the next 3 months.
3. Cost Explorer displays a forecast (dashed line) extending beyond the current date.
4. Record the forecasted spend for the next month.

---

## Part 2: Configure AWS Budgets

### Step 2.1 — Create a Monthly Cost Budget

1. Navigate to **Billing and Cost Management → Budgets → Create budget**.
2. Select **Use a template → Monthly cost budget**.
3. Configure: Budget name = `MonthlySpendLimit`; Budgeted amount = 10% above your current monthly average (from Cost Explorer); Email recipients = your email address.
4. Choose **Create budget**.

### Step 2.2 — Create a Zero-Spend Budget (Free Tier)

1. Create a second budget.
2. Select **Use a template → Zero spend budget**.
3. Budget name: `FreeierAlert`
4. Email: your address.
5. Create.

This budget alerts you immediately if any charge is incurred — useful for sandbox accounts that should remain within Free Tier.

### Step 2.3 — Review Budget Dashboard

1. Open the Budgets dashboard.
2. Observe the status indicators for each budget.
3. Record in your lab document: What percentage of the monthly cost budget is currently consumed? Is the forecasted spend on track to exceed the budget?

---

## Part 3: Apply Cost Allocation Tags

### Step 3.1 — Tag an EC2 Instance (or S3 Bucket)

1. Open the EC2 console and select any running or stopped instance.
2. Choose **Tags → Manage tags → Add tag**.
3. Add these tags: `Project` = `CIS4334-Lab14`, `Environment` = `Lab`, `Owner` = your name.
4. Save the tags.

If no EC2 instances exist, tag an S3 bucket instead.

### Step 3.2 — Activate Tags in Billing

1. Navigate to **Billing and Cost Management → Cost allocation tags**.
2. Find the `Project`, `Environment`, and `Owner` tags you just created (they may take up to 24 hours to appear after first use).
3. If they are visible, select them and choose **Activate**.
4. Record in your lab document: Why must tags be activated before they appear in Cost Explorer? What happens to cost data for resources tagged before the activation date?

---

## Part 4: S3 Lifecycle Policy

### Step 4.1 — Create an S3 Bucket

1. Open the S3 console → **Create bucket**.
2. Bucket name: `lab14-lifecycle-<your-initials>` (must be globally unique).
3. Region: your default region.
4. Leave all other settings as default.
5. Create.

### Step 4.2 — Configure a Lifecycle Rule

1. Open the bucket → **Management → Lifecycle rules → Create lifecycle rule**.
2. Rule name: `StandardToArchive`
3. Rule scope: Apply to all objects in the bucket.
4. Configure transition 1: **S3 Standard-IA** after **30 days**.
5. Configure transition 2: **S3 Glacier Flexible Retrieval** after **90 days**.
6. Configure expiration: **Expire current versions** after **2555 days** (approximately 7 years).
7. Also enable: **Delete expired object delete markers** (keeps the bucket clean for versioned objects).
8. Create rule.

### Step 4.3 — Review the Rule

1. View the lifecycle rule in the Management tab.
2. In your lab document, draw or describe the data flow: what storage class does an object start in, and when does it transition? What happens after 7 years?
3. Answer: If you deleted an object from this bucket on day 45 after creation, which minimum storage duration charge would apply, and for how many additional days?

---

## Part 5: AWS Compute Optimizer

### Step 5.1 — Enable Compute Optimizer

1. Navigate to **AWS Compute Optimizer** (search in the console).
2. If not yet enabled, choose **Get started** and opt in. Note: Compute Optimizer requires at least 14 days of CloudWatch metrics to generate recommendations.

### Step 5.2 — Review EC2 Recommendations

1. Navigate to **EC2 instances** in Compute Optimizer.
2. If recommendations are available, open one instance recommendation.
3. Record the current instance type, recommended instance type, estimated monthly savings, and performance risk level (Low/Medium/High).
4. If no instances have recommendations yet (insufficient data), document what metric data Compute Optimizer needs and how long it takes to generate recommendations.

### Step 5.3 — Review Lambda Recommendations

1. Navigate to **Lambda functions** in Compute Optimizer.
2. If your functions from Module 12 labs are present, review memory recommendations.
3. Note whether any functions are flagged as over-provisioned in memory.
4. In your lab document: What is the relationship between Lambda memory, CPU allocation, and billing? Why would reducing Lambda memory sometimes increase total cost instead of reducing it?

---

## Reflection Questions

Answer in your lab submission document:

1. Cost Explorer shows your top three spending services. Select the second-highest service and propose one specific architectural change that would reduce its cost. Name the AWS pricing model, storage class, or feature that enables the reduction.

2. You configured both a monthly cost budget and a zero-spend budget. What is the behavioral difference between a Budget alert and a Budget Action? In what scenario would you use a Budget Action rather than just an email alert?

3. Your S3 Lifecycle policy transitions objects to Standard-IA after 30 days. A colleague suggests using Intelligent-Tiering instead of Lifecycle policies. Under what conditions is Intelligent-Tiering more cost-effective than a Lifecycle policy? Under what conditions is a Lifecycle policy more cost-effective?

4. Compute Optimizer recommended a smaller instance type for one of your EC2 instances. Before applying the recommendation, what three factors would you verify to ensure the smaller instance does not cause performance degradation?

---

## Cleanup

1. Delete the S3 bucket `lab14-lifecycle-<your-initials>` (must be empty first).
2. Delete both AWS Budgets (`MonthlySpendLimit` and `FreeierAlert`).
3. Remove the lab tags from the EC2 instance or S3 bucket you tagged.

There are no other billable resources created in this lab.

---

## Submission Checklist

- Screenshot of Cost Explorer showing top 3 services by spend (last 3 months)
- Screenshot of the monthly cost budget dashboard showing current vs. forecasted spend
- Screenshot of the S3 Lifecycle rule showing all three transitions/expiration rules
- Screenshot of a Compute Optimizer recommendation (or explanation of why data is insufficient)
- Written answers to all four reflection questions

---

## Part 9 — Challenge Exercise

### Challenge 1: Savings Plans Purchase Analysis
Use the AWS Savings Plans console to evaluate a real or simulated commitment and understand break-even calculations.
1. Navigate to AWS Cost Management → Savings Plans → Recommendations. If your account has On-Demand EC2 or Lambda spend, AWS will display recommended Savings Plan commitments with estimated savings. Record the recommended hourly commitment, estimated annual savings, and coverage percentage shown.
2. If no recommendations exist (new or free-tier account), use the Savings Plans pricing page to manually calculate: for an `m5.large` in `us-east-1` running 24/7, compare the 1-year No Upfront Compute Savings Plan effective rate against the On-Demand rate. Calculate the monthly savings and the total 12-month savings in dollars.
3. Navigate to Savings Plans → Purchase Savings Plan (do NOT complete the purchase). Document all the configurable fields: plan type options (Compute, EC2 Instance, SageMaker), term options (1 or 3 year), payment options (All, Partial, No Upfront), and hourly commitment field. Screenshot the purchase form.
4. Explain in 2–3 sentences why a Compute Savings Plan is generally preferable to an EC2 Instance Savings Plan for an organization that is actively modernizing from EC2 to containers and Lambda workloads.

### Challenge 2: Cost Allocation Tag Activation and Tagging Audit
Practice activating cost allocation tags and auditing resource tagging compliance across your account.
1. Navigate to AWS Billing → Cost allocation tags. Activate the `Name`, `Environment`, and `Project` tags (or any tags already applied to your resources). Note the message that activated tags appear in Cost Explorer after 24 hours.
2. Use the AWS CLI to list all EC2 instances and their current tags: `aws ec2 describe-instances --query "Reservations[*].Instances[*].{ID:InstanceId,Tags:Tags}" --output table`. Identify any instances missing the `Environment` or `Project` tag.
3. Apply missing tags to at least one resource using the CLI: `aws ec2 create-tags --resources <instance-id> --tags Key=Environment,Value=Lab Key=Project,Value=CIS4334`. Verify: `aws ec2 describe-tags --filters "Name=resource-id,Values=<instance-id>" --output table`.
4. Use Tag Editor (AWS Resource Groups → Tag Editor) to perform a multi-service tag search across your account: search for resources across EC2, S3, and Lambda that are missing the `Project` tag. Document the count of untagged resources found per service and explain why a high percentage of untagged resources is a cost visibility problem for finance teams.

### Reflection Questions
1. After completing Challenge 1, explain the trade-off between Compute Savings Plans and EC2 Instance Savings Plans in terms of flexibility versus discount depth. Under what specific organizational circumstances would you recommend locking into an EC2 Instance Savings Plan despite its lower flexibility — and what financial risk does that create if the organization's compute strategy changes during the commitment term?
2. Based on Challenge 2, explain how inconsistent resource tagging creates downstream problems beyond Cost Explorer visibility — specifically for chargeback models, budget alerting accuracy, and automated cost optimization tools like Compute Optimizer. How does the AWS Well-Architected Framework Cost Optimization pillar's principle of "implement cloud financial management" address tagging as an organizational discipline rather than a technical configuration?

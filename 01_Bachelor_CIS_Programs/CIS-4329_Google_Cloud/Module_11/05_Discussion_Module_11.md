# Discussion: Module 11 — Infrastructure as Code on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This discussion asks you to evaluate an infrastructure management scenario and recommend
an IaC strategy. You will apply the Deployment Manager and Terraform concepts from
Module 11 and reflect on the broader discipline of treating infrastructure like code.

**Initial post due**: Thursday at 11:59 PM Central

**Peer responses due**: Sunday at 11:59 PM Central

---

### Scenario

A startup called CloudSwift is building a SaaS platform on GCP. Their current situation:

- All infrastructure was created manually by one developer over six months using the
  Cloud Console
- No documentation exists for what resources exist or how they are configured
- The development, staging, and production environments have configuration drift — they
  are no longer identical
- The company recently hired two additional cloud engineers who need to provision
  resources independently without stepping on each other's work
- Leadership wants all infrastructure changes reviewed before they reach production
- The company plans to expand to AWS within 18 months for redundancy

The team is debating two approaches:

**Option A**: Adopt Cloud Deployment Manager. Write YAML configurations for all existing
resources, deploy them as Deployment Manager deployments, and enforce a policy that all
future changes go through configuration files.

**Option B**: Adopt Terraform with the GCP provider and a GCS remote state backend.
Write HCL for all existing resources, use `terraform import` to bring existing resources
under management, and configure a CI/CD pipeline that runs `terraform plan` on pull
requests.

---

### Response Requirements

#### Part 1: Tool Recommendation

Recommend either Option A or Option B for CloudSwift. In 4–5 sentences, justify your
recommendation by referencing at least three specific technical factors from the scenario
that make your chosen tool the better fit.

#### Part 2: State Management Plan

For your recommended tool, describe the state management strategy in 3–4 sentences. If
you chose Terraform, explain the remote state configuration and how concurrent-apply
conflicts will be prevented. If you chose Deployment Manager, explain how you would
handle the lack of a local state file and how you would track deployment history.

#### Part 3: Handling Existing Resources

The existing infrastructure was all created manually. In 3–4 sentences, describe the
process for bringing those existing resources under IaC management with your chosen tool.
What is the first step? What risks exist during this transition?

#### Part 4: Reflection

Have you ever experienced the problems described in CloudSwift's scenario — configuration
drift, undocumented infrastructure, or conflicting changes from multiple team members?
Describe the situation in 2–3 sentences and explain how IaC would have helped (or does
help). Hypothetical scenarios are acceptable.

---

### Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Justified tool recommendation with 3 specific technical factors | 30 |
| Part 2: Correct and specific state management strategy | 25 |
| Part 3: Accurate process for bringing existing resources under IaC | 25 |
| Part 4: Thoughtful reflection | 5 |
| Peer response 1: Substantive technical engagement | 7 |
| Peer response 2: Substantive technical engagement | 8 |
| **Total** | **100** |

---

### Peer Response Guidelines

A substantive peer response does at least one of the following:

- Argues for the other tool with specific technical reasons (e.g., challenges a Terraform
  recommendation with a Deployment Manager advantage, or vice versa)
- Identifies a technical gap or risk in the state management plan
- Adds a specific Terraform or Deployment Manager feature or command that would help
  with the existing-resource transition
- Raises a consideration about the AWS expansion plan that affects the tool choice

---

### Discussion Hints

The 18-month AWS expansion is a significant clue. Consider what changes when your
infrastructure spans two cloud providers and whether your recommended tool still works.

For the existing resources, think about what `terraform import` requires — it is not
a one-command migration. Each resource needs a written resource block in your `.tf` files
before import, and complex resources like managed instance groups have multiple sub-
resources to import individually.

For Deployment Manager, the equivalent of "importing" existing resources is writing a
new configuration that matches the existing resource state and creating a deployment.
However, Deployment Manager then owns those resources — deleting the deployment deletes
them. This requires careful planning.

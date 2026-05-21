# Reading Guide: Module 16 - Final Exam Prep & Terraform Associate 003 Certification

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction

Welcome to **Module 16 - Final Exam Prep & Terraform Associate 003 Certification**! This final module consolidates all concepts from the course into a structured review aligned with the official HashiCorp Certified: Terraform Associate (003) exam blueprint. This exam has no prerequisites and tests practical knowledge of Terraform's core workflow, language, state management, modules, backends, and the Terraform Cloud platform.

As a student, you will review the six official exam objective domains, identify high-priority topics for final study, work through scenario-based practice questions across all modules, and prepare for exam-day logistics. Completing this module puts you in a strong position to sit the Terraform Associate exam with confidence. Make sure to complete the checklists and the practice lab before scheduling your exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Terraform Associate 003 exam domains**: The six objective areas that structure the exam: (1) Understand Infrastructure as Code concepts, (2) Understand Terraform's purpose, (3) Understand Terraform basics, (4) Use the Terraform CLI outside the core workflow, (5) Interact with Terraform modules, (6) Navigate Terraform workflow, (7) Implement and maintain state, (8) Read, generate, and modify configuration, (9) Understand Terraform Cloud. Questions are weighted across these domains; state management and the core CLI workflow carry the most weight.
* **Core Terraform workflow**: The sequence `terraform init` → `terraform plan` → `terraform apply` → `terraform destroy`. Every exam scenario is grounded in this workflow. Know what each command does, what files it reads and writes, what flags modify its behavior, and what errors indicate at each stage.
* **Terraform state**: The JSON file (`terraform.tfstate`) that records the mapping between HCL resource declarations and real-world infrastructure. State is the source of truth Terraform uses to compute diffs. Know the implications of state corruption, the role of state locking, remote backends, and the security requirement to protect state from unauthorized access.

---

### 2. Certification Exam Tips

* **Review all nine exam objective domains:** The official exam review guide published by HashiCorp lists every tested topic. Read through the full list and honestly rate your confidence on each item. Allocate remaining study time to low-confidence areas first, particularly state management (Domain 7) and Terraform Cloud (Domain 9), which are consistently under-studied.
* **Know the difference between similar commands:** The exam frequently tests command distinctions: `terraform fmt` vs. `terraform validate`, `terraform refresh` vs. `terraform plan -refresh-only`, `terraform taint` (deprecated) vs. `terraform apply -replace`, `terraform state mv` vs. renaming a resource block. Write out a summary card for each pair.
* **Practice with the official sample questions:** HashiCorp publishes a free sample exam with 12 questions at the Terraform Associate certification page. Work through these under timed conditions. Review every question — including ones you answered correctly — to understand the reasoning behind all four answer choices.
* **Study Resource:** The official HashiCorp Terraform Associate 003 exam review guide lists every tested objective and links to the relevant documentation sections: [Terraform Associate 003 Exam Review — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Work through the complete Terraform Associate 003 exam review guide, which maps every exam objective to specific documentation pages and tutorials. Use it as a final checklist — if any linked page is unfamiliar, read it before exam day: [Terraform Associate 003 Exam Review — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003).
* **Required Video:** Watch the full review section of the Terraform Associate complete course playlist, which walks through practice questions, common exam traps, and a summary of each objective domain: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Run the full core workflow end-to-end from memory**: Without referring to notes, write a complete Terraform configuration for a simple cloud resource, run `terraform init`, `terraform validate`, `terraform fmt`, `terraform plan -out=tfplan`, and `terraform apply tfplan`. Verify the resource exists, then run `terraform destroy`. This rehearses the complete exam-relevant command sequence under time pressure.
* **Practice state inspection commands**: On an existing Terraform-managed environment, run `terraform state list`, `terraform state show <address>`, `terraform output`, and `terraform plan -refresh-only`. Document what each command returns. These commands appear directly in exam scenario questions.
* **Complete a timed practice exam**: Use the HashiCorp official sample questions or a community practice exam. Set a 60-minute timer for 57 questions (matching the real exam format). After completing it, review every incorrect answer against the official documentation before scheduling the real exam.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
* [ ] Complete the full Terraform Associate 003 exam review at [Terraform Associate 003 Exam Review — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003).
* [ ] Watch the review video in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
* [ ] Complete the timed practice exam described in the lab instructions.
* [ ] Schedule your Terraform Associate 003 exam at [HashiCorp Certifications — Credly / PSI](https://www.hashicorp.com/certifications/terraform-associate).

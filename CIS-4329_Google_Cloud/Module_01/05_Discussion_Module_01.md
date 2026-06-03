# Discussion: Module 01 — Cloud Computing Fundamentals and GCP Overview

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion activity asks you to apply Module 01 concepts to real-world
scenarios. You will post an original response and engage meaningfully with at
least two classmates. The goal is to practice the kind of architectural and
operational reasoning tested on the ACE exam.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — Resource Hierarchy Design (Choose One)

You have been hired as a cloud architect at a mid-sized university. The
university has four colleges (Business, Engineering, Science, Liberal Arts),
a central IT department, and a research division. The university's Google
Workspace domain is `university.edu`.

They are setting up GCP for the first time and need a resource hierarchy that:

- Keeps production and development workloads isolated from each other
- Allows each college to manage its own cloud spending independently
- Prevents any college from accidentally affecting another college's resources
- Lets central IT apply security policies across the entire organization

Design a GCP resource hierarchy (Organization, Folders, Projects) that meets
these requirements. In your post:

1. Draw or describe your hierarchy structure (text diagram is fine).
2. Explain which IAM roles you would grant at the Organization level vs. the
   Folder level vs. the Project level.
3. Identify at least two Organization Policy constraints you would apply at the
   Organization level and explain why.
4. Explain how billing accounts would be structured to allow per-college cost
   tracking.

---

## Prompt B — Cloud Migration Analysis (Choose One)

A local healthcare company currently runs its application on physical servers
in a company-owned data center. Their setup includes:

- 12 application servers running 24/7
- A large file storage system holding patient records
- A batch reporting job that runs nightly for 4 hours
- A web portal accessed by patients during business hours (9 AM–5 PM)

They are considering migrating to GCP. In your post:

1. For each workload above, recommend a GCP service and service model (IaaS,
   PaaS, or SaaS). Justify your choices.
2. Identify which workload would benefit most from preemptible VMs and explain
   why.
3. Discuss how sustained use discounts would or would not apply to the 24/7
   application servers.
4. Identify any compliance concerns (data residency, HIPAA) that would affect
   region selection, and explain how GCP tools address them.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- A direct answer to all numbered sub-questions in your chosen prompt
- At least one specific GCP service or feature name with a brief explanation
- Your reasoning, not just conclusions — explain why you made each choice

Your two peer responses must each be at least 100 words and do one of the
following:

- Respectfully challenge an assumption or recommendation in the post
- Build on the post by adding a consideration the original author did not address
- Share a real-world example that supports or complicates the post's conclusions

Responses like "Great post, I agree!" do not earn credit.

---

## Discussion Tips

- Use GCP documentation at cloud.google.com/docs to verify service names and
  capabilities before posting.
- The ACE exam frequently presents scenario-based questions. Practicing your
  reasoning here directly prepares you for the exam format.
- There is often more than one correct architectural answer. What matters is
  that your reasoning is sound and you address trade-offs.

---

## Reflection Question (Optional — Extra Credit)

After reading your classmates' posts, did any response change your thinking
about your own design? If so, describe what you would revise and why. If not,
explain which alternative approaches you considered and rejected.

Extra credit responses must be at least 150 words.

---

End of Discussion — Module 01

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

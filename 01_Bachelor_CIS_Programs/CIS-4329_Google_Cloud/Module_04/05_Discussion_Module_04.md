# Discussion: Module 04 — Cloud Storage

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion asks you to apply Cloud Storage design principles to real-world
data management problems. Object storage is the backbone of modern cloud data
architectures and an important part of cost optimization strategies.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — Data Lifecycle Architecture (Choose One)

A regional hospital generates the following types of digital data:

- Medical imaging files (MRI, CT scans): 2–5 GB each; accessed frequently for
  30 days post-procedure; then reviewed during annual checkups (once per year);
  must be retained for 10 years by law
- Electronic health records (PDFs): Accessed regularly for active patients;
  patients become inactive after discharge (roughly every 6 months); records
  must be retained for 7 years after the patient's last visit
- System log files: Generated continuously; accessed only if an incident occurs
  (roughly 5% chance in the first 7 days, near zero after 30 days); useful
  to retain for 90 days

Design a Cloud Storage strategy for each data type:

1. Specify the bucket location type (regional, dual-region, multi-region) and
   justify your choice for each data type.
2. Specify the initial storage class and the full lifecycle policy for each
   data type. Include specific conditions and actions in your answer.
3. Explain how you would enforce the retention requirements to prevent premature
   deletion — even by administrators.
4. Describe the access control model (uniform vs. fine-grained, which IAM
   roles) you would apply to each bucket and why.

---

## Prompt B — Cloud Storage Cost Optimization Review (Choose One)

Your team has inherited a Cloud Storage environment with the following issues
discovered during a cost audit:

- A single `us-multi-region` bucket contains all data types: active app assets,
  90-day-old log files, 2-year-old compliance archives, and versioned objects
  with hundreds of old versions accumulating
- No lifecycle policies exist on any bucket
- All data is in Standard storage class regardless of age
- Several buckets have `allUsers: objectViewer` access set from an old public
  website that was decommissioned
- Monthly Cloud Storage costs have grown 40% in the last 6 months without a
  corresponding increase in active data

Analyze each problem and propose a remediation plan:

1. Estimate which issues are contributing the most to the cost increase and
   explain your reasoning.
2. Design a revised bucket structure (how many buckets, what locations, what
   storage classes) that separates data by access pattern.
3. Write out the lifecycle policies you would implement for each bucket,
   including conditions and actions.
4. Identify the security risk of the public access configuration and describe
   the specific steps to remediate it.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- Specific storage class names and lifecycle condition/action parameters
- At least one cost calculation or estimation using the GCP pricing page
  (cloud.google.com/storage/pricing)
- Explicit reasoning for each architecture decision, not just conclusions

Your two peer responses must each be at least 100 words and do one of the
following:

- Identify a compliance or data residency consideration the original post did
  not address
- Propose a different storage class or lifecycle timeline and justify it
- Point out a configuration that could lead to unexpected cost or data loss

---

## Discussion Tips

- Use the Cloud Storage pricing calculator to compare monthly costs between
  storage classes at realistic data volumes.
- Think about access patterns carefully. The biggest cost optimization
  opportunities come from correctly identifying data that is in Standard but
  should be in Coldline or Archive.
- Retention policies and lifecycle policies serve different purposes. A
  retention policy prevents early deletion. A lifecycle policy automates
  transitions. They complement each other.

---

## Reflection Question (Optional — Extra Credit)

The Archive storage class offers the lowest cost but the highest retrieval fee.
Describe a scenario where Archive is the wrong choice even though the data is
accessed less than once per year. What storage class would you use instead and
why? Minimum 150 words.

---

End of Discussion — Module 04

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

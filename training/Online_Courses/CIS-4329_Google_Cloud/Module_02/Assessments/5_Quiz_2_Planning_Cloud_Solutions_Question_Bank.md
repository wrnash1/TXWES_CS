### 5. Quiz 2: Planning Cloud Solutions (Question Bank)
**Question 1**
Your company has 500 terabytes of historical financial records that must be retained for 7 years to comply with government regulations. You expect to access this data at most once a year during an audit. Which Google Cloud Storage class is the most cost-effective choice for this requirement?
A) Standard Storage
B) Nearline Storage
C) Coldline Storage
D) Archive Storage
*   **Correct Answer:** D) Archive Storage
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Standard is for frequently accessed, "hot" data and has the most expensive storage-at-rest costs.
    *   *Why B is incorrect:* Nearline is optimized for data accessed roughly once a month (like recent backups).
    *   *Why C is incorrect:* Coldline is optimized for data accessed roughly once a quarter (every 90 days). Archive is the absolute cheapest storage for data accessed less than once a year.

**Question 2**
You need to perform a massive batch-processing job that involves rendering 1,000 video files. The rendering software is designed to automatically retry a video if a server crashes. Which Compute Engine option will allow you to complete this task with the lowest possible compute costs?
A) E2 standard instances
B) Compute Engine instances with sustained use discounts
C) Spot (Preemptible) instances
D) App Engine standard environment
*   **Correct Answer:** C) Spot (Preemptible) instances
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Standard on-demand instances charge full price.
    *   *Why B is incorrect:* Sustained use discounts automatically apply when a VM runs for most of the month, but they are significantly less of a discount than Spot pricing.
    *   *Why D is incorrect:* App Engine is a Platform-as-a-Service for hosting web applications, not a raw compute instance for heavy video rendering batch jobs. Spot instances offer up to 90% off standard pricing, with the caveat that Google can terminate them at any time—perfect for fault-tolerant batch jobs.

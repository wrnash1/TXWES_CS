### 4. Lab 2: Estimating Costs and Provisioning Storage
**Objective:** Use the Pricing Calculator and create a multi-regional Cloud Storage bucket.
**Instructions:**
1. Open the Google Cloud Pricing Calculator in your browser.
2. Estimate the monthly cost of running 4 `e2-medium` Compute Engine instances in Iowa (us-central1) 24/7. Note the price.
3. Now, in the Google Cloud Console, navigate to **Cloud Storage -> Buckets**.
4. Click **Create**.
5. Name the bucket `txwes-backup-[your initials]` (bucket names must be globally unique across all of Google).
6. Under Location Type, select **Multi-region** and choose `us (multiple regions in United States)`.
7. Under Default storage class, select **Coldline**.
8. Create the bucket and upload a sample text file to it.
**Deliverable:** Submit a screenshot of your newly created Coldline bucket showing the uploaded file, along with the estimated monthly cost from step 2 written in the submission comments.

---

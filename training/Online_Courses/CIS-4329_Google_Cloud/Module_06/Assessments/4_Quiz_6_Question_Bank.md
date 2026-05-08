### 4. Quiz 6 (Question Bank)
**Question 1:** An application running on a Compute Engine instance needs to upload images to a Cloud Storage bucket. What is the most secure way to authenticate the application?
A) Hardcode your personal Google Cloud credentials into the application source code.
B) Assign a Service Account to the Compute Engine instance with the appropriate Storage permissions.
C) Make the Cloud Storage bucket completely public.
D) Use a primitive IAM Editor role.
*   **Correct:** B) Assign a Service Account to the Compute Engine instance.
*   **Distractor Analysis:** Hardcoding credentials is a massive security risk. Service accounts provide automatic, short-lived, managed credentials to compute resources securely.

---

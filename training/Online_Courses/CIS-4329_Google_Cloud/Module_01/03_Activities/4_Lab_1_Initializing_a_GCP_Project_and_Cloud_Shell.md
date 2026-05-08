### 4. Lab 1: Initializing a GCP Project and Cloud Shell
**Objective:** Use Cloud Shell to create a project and set a default compute region.
**Instructions:**
1. Log into your Google Cloud account.
2. Click the **Activate Cloud Shell** icon (`>_`) in the top right header.
3. Wait for the terminal to provision.
4. Run the following command to list your current projects: `gcloud projects list`
5. Create a new project (Note: Project IDs must be globally unique, so add your initials): `gcloud projects create txwes-ace-lab-[your initials]`
6. Set this new project as your active configuration: `gcloud config set project txwes-ace-lab-[your initials]`
7. Set your default compute zone to central US: `gcloud config set compute/zone us-central1-a`
**Deliverable:** Take a screenshot of your Cloud Shell showing the output of `gcloud config list`, confirming your project and zone are set.

---

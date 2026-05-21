# Quiz: Module 01 – GCP Overview: Regions, Zones, and Console Navigation
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
You want to receive an email notification if your Google Cloud spending exceeds $500 for the current month. You set up a budget and an alert threshold. What happens to your resources if the spending reaches $501?

A) All resources are immediately suspended to prevent further charges.
B) Compute instances are shut down, but storage remains active.
C) The resources continue to run normally, and you receive an email alert.
D) The project is automatically deleted.

*   **Correct Answer:** C) The resources continue to run normally, and you receive an email alert.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GCP budget alerts only trigger notifications (email or Pub/Sub messages). They do not cap spending or suspend resources automatically without custom automation.
    *   *Why B is incorrect:* GCP does not selectively shut down compute resources based on budget alerts; no native budget action targets specific resource types.
    *   *Why D is incorrect:* GCP will never automatically delete a project for crossing a billing threshold; deletion requires an explicit administrative action.

---

**Question 2**
At which level of the Google Cloud resource hierarchy are Billing Accounts attached to pay for consumed resources?

A) Organization level
B) Folder level
C) Project level
D) Resource level

*   **Correct Answer:** C) Project level
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While Organizations *own* Billing Accounts, the actual linkage that pays for a running VM happens by associating the Billing Account with a specific Project, not the Organization node itself.
    *   *Why B is incorrect:* Folders are used to group Projects for IAM policy inheritance and organizational structure, but Billing Accounts are not directly attached to Folders.
    *   *Why D is incorrect:* Individual resources such as a single VM or Cloud Storage bucket do not have their own Billing Accounts; they inherit the billing link from their parent Project.

---

**Question 3**
A GCP administrator needs to display the currently active SDK configuration — including the active project, account, and default region — on their local workstation. Which command is most appropriate?

A) `gcloud config list`
B) `gcloud projects describe`
C) `gcloud info --format=json`
D) `gcloud init --show-config`

*   **Correct Answer:** A) `gcloud config list`
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `gcloud projects describe` returns metadata about a specific project (project number, labels, lifecycle state) — not the local SDK configuration.
    *   *Why C is incorrect:* `gcloud info` outputs diagnostic information about the SDK installation environment, not the active configuration values.
    *   *Why D is incorrect:* `gcloud init --show-config` is not a valid gcloud flag; `gcloud init` launches an interactive setup wizard, not a configuration display command.

---

**Question 4**
Your team needs to deploy a web application that must remain available even if a single Google Cloud data center experiences a hardware failure. The application does not need to survive a full regional outage. Which deployment strategy meets this requirement at the lowest complexity?

A) Deploy the application to a single zone in one region.
B) Deploy the application across multiple zones within a single region.
C) Deploy the application across multiple regions using a global load balancer.
D) Deploy the application on-premises and connect it to GCP via Cloud VPN.

*   **Correct Answer:** B) Deploy the application across multiple zones within a single region.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single-zone deployment has no redundancy; a hardware failure in that zone takes the application offline entirely.
    *   *Why C is incorrect:* Multi-region deployment with a global load balancer provides resilience against full regional outages, which exceeds the stated requirement and adds significant cost and complexity.
    *   *Why D is incorrect:* Deploying on-premises introduces infrastructure management overhead, does not leverage GCP's availability features, and contradicts the cloud administration context.

---

**Question 5**
You are setting up a new GCP environment for your organization. You need to enforce a policy that prevents any Project in the entire organization from creating resources outside of specific approved regions. At which level of the resource hierarchy should you apply this Organization Policy constraint?

A) At the individual resource level for each VM and bucket.
B) At the Project level for every project separately.
C) At the Folder level for each team's folder.
D) At the Organization level so it automatically applies to all Folders and Projects.

*   **Correct Answer:** D) At the Organization level so it automatically applies to all Folders and Projects.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Applying constraints at the resource level is not how Organization Policies work; policies apply at Organization, Folder, or Project levels, not on individual resources.
    *   *Why B is incorrect:* Applying the policy separately to every Project is operationally unsustainable and risks missing new Projects created in the future.
    *   *Why C is incorrect:* Applying the policy at the Folder level only covers Projects within that folder; Projects in other folders or directly under the Organization node would be unprotected.

# Quiz — Module 01

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: GCP Overview — Regions, Zones, and Console Navigation

### 10 Questions | 10 Points Each | Total: 100 Points

---

## Question 1

You want to receive an email notification if your Google Cloud spending exceeds $500 for the current month. You set up a budget and an alert threshold at 100%. What happens to your running resources if the spending reaches $501?

A. All resources are immediately suspended to prevent further charges.

B. Compute instances are shut down, but Cloud Storage remains active.

C. The resources continue to run normally and you receive an email alert.

D. The project is automatically deleted after a 24-hour grace period.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: GCP budget alerts are notification-only mechanisms. They send emails and can publish to Pub/Sub, but they take no automated action against running resources. Suspension requires custom automation built by the administrator.
- Why B is incorrect: GCP has no native behavior that selectively stops compute but preserves storage when a budget threshold is crossed. Budget alerts do not distinguish between resource types.
- Why D is incorrect: GCP will never automatically delete a project because a billing threshold was exceeded. Project deletion is always an explicit administrative action and requires confirmation.

---

## Question 2

At which level of the Google Cloud resource hierarchy are Billing Accounts linked to pay for consumed resources?

A. Organization level

B. Folder level

C. Project level

D. Individual resource level

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: While Billing Accounts are owned by an Organization in enterprise setups, the actual payment linkage that causes a running VM or bucket to generate a bill occurs when the Billing Account is associated with a specific Project, not with the Organization node itself.
- Why B is incorrect: Folders are structural grouping containers for Projects. Billing Accounts are never directly linked to Folders; billing flows from the Project level upward to the Billing Account.
- Why D is incorrect: Individual resources such as VMs, Cloud Storage buckets, or Cloud SQL instances do not have their own Billing Account associations. They inherit billing from their parent Project.

---

## Question 3

A GCP administrator needs to display the currently active SDK configuration — including the active project, account email, and default region — on their local workstation. Which command is most appropriate?

A. `gcloud config list`

B. `gcloud projects describe`

C. `gcloud info --format=json`

D. `gcloud init --show-config`

Correct Answer: A

Distractor Analysis:

- Why B is incorrect: `gcloud projects describe PROJECT_ID` returns metadata about a specific project such as its project number, labels, and lifecycle state. It does not display the local SDK configuration context such as the active account or default zone.
- Why C is incorrect: `gcloud info` outputs diagnostic information about the gcloud SDK installation environment including version numbers, Python path, and log file locations. It is not used to display active configuration values.
- Why D is incorrect: `--show-config` is not a valid flag for `gcloud init`. The `gcloud init` command launches an interactive setup wizard that guides you through authenticating and selecting a project. It does not have a display-only mode.

---

## Question 4

Your team needs to deploy a web application that must remain available even if a single Google Cloud data center experiences a complete hardware failure. The application does not need to survive a full regional outage. Which deployment strategy meets this requirement at the lowest additional cost and complexity?

A. Deploy the application to a single zone in one region.

B. Deploy the application across multiple zones within a single region.

C. Deploy the application across multiple regions using a global load balancer.

D. Deploy the application on-premises and connect it to GCP via Cloud VPN.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: A single-zone deployment has no redundancy against zone failures. A hardware failure in that one zone takes the entire application offline, which directly violates the stated availability requirement.
- Why C is incorrect: Multi-region deployment with a global load balancer does provide resilience against full regional outages, but the scenario explicitly states that regional resilience is not required. Multi-region deployment adds substantial cost, latency management complexity, and data replication overhead that is unnecessary here.
- Why D is incorrect: On-premises deployment abandons GCP's availability zones entirely and introduces infrastructure management overhead. It does not solve the stated problem and is out of scope for a cloud administration course.

---

## Question 5

You are establishing governance for your organization's GCP environment. You need to enforce a policy that prevents any Project in the entire organization from creating resources outside of two approved regions, regardless of what IAM permissions individual users hold. What is the correct approach?

A. Apply the `roles/compute.admin` role restriction at the Organization level to block non-approved regions.

B. Manually configure each Project to deny resource creation outside approved regions.

C. Apply an Organization Policy constraint using `constraints/gcp.resourceLocations` at the Organization level.

D. Create a custom IAM role that excludes `compute.instances.create` permissions for non-approved regions.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: IAM roles control who can perform actions but cannot restrict resource creation to specific geographic regions. There is no IAM role that enforces region restrictions at the organizational level for all resource types.
- Why B is incorrect: Manually configuring every project is operationally unsustainable, especially as new projects are created. Projects added in the future would not be covered unless an administrator remembered to apply the configuration each time.
- Why D is incorrect: IAM roles and permissions do not operate at the geographic region level. You cannot create an IAM role that differentiates between creating a VM in `us-central1` versus `europe-west1`. Geographic restrictions are solely in the domain of Organization Policies.

---

## Question 6

Which of the following correctly describes the relationship between a GCP Zone and a GCP Region?

A. A region is a single data center; a zone is a group of data centers in the same country.

B. A zone is a geographic location containing multiple regions for low-latency connectivity.

C. A region is a geographic location containing multiple isolated zones; each zone has independent power and networking.

D. Regions and zones are interchangeable terms for the same concept in GCP documentation.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: The definitions are reversed. A region is the broader geographic location (equivalent to a metropolitan area of data centers), and a zone is a single isolated deployment area within that region.
- Why B is incorrect: This reverses the hierarchy. Zones are contained within regions, not the other way around. A zone does not contain regions.
- Why D is incorrect: Regions and zones are distinct concepts with different failure domains, different scopes, and different use cases in architecture decisions. They are not interchangeable.

---

## Question 7

A developer signs up for Google Cloud using a personal `@gmail.com` account and creates several projects. Which statement about the resource hierarchy for this account is correct?

A. A personal Gmail account automatically creates an Organization node that owns all projects.

B. Projects created under a personal Gmail account are not associated with any Organization node.

C. Google assigns a shared Organization node to all personal Gmail GCP accounts.

D. Personal Gmail accounts cannot create GCP Projects without first creating an Organization node.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Organization nodes are only created when a Google Workspace or Cloud Identity domain is associated with the account. Personal Gmail accounts do not trigger Organization node provisioning.
- Why C is incorrect: Google does not create shared Organization nodes for personal Gmail users. Each Organization node maps to a specific domain, and personal Gmail addresses (`@gmail.com`) are not managed domains.
- Why D is incorrect: Personal Gmail accounts can create GCP Projects and use GCP services without an Organization node. Many individual developers and students use GCP without any Organization node in their hierarchy.

---

## Question 8

An administrator grants the `roles/editor` role to a contractor at the Folder level. The folder contains five Projects. The contractor will be leaving the company next week. The administrator wants to revoke all GCP access for this contractor. What is the most efficient action?

A. Remove the `roles/editor` binding from each of the five Projects individually.

B. Remove the `roles/editor` binding from the Folder level.

C. Delete all five Projects to remove the contractor's access.

D. Reassign the contractor's account to a different Folder with no permissions.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Removing the binding project-by-project is inefficient and error-prone. Since the original grant was at the Folder level, the binding exists on the Folder, not on each individual Project. A project-level removal would not remove the Folder-level grant.
- Why C is incorrect: Deleting projects is a destructive action that would remove all resources in those projects, not just the contractor's access. This is a completely disproportionate response that would harm other users and workloads.
- Why D is incorrect: Moving an account to a different folder is not how IAM works. IAM grants are not attached to accounts in a folder membership sense; they are policy bindings on specific resources. The contractor's email must be removed from the IAM policy binding.

---

## Question 9

You are working in Cloud Shell and run `gcloud config set compute/zone us-east1-b`. You then close the browser tab. The next time you open Cloud Shell, which statement about your configuration is correct?

A. The zone setting is permanently lost because Cloud Shell is fully ephemeral.

B. The zone setting persists because Cloud Shell writes configuration to the persistent 5 GB home directory.

C. The zone setting reverts to `us-central1-a` because that is the Cloud Shell default.

D. The zone setting persists for 24 hours and then resets automatically.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: While the Cloud Shell VM itself is ephemeral (recycled after inactivity), the gcloud configuration files are stored in the home directory, which resides on persistent Cloud Storage. Configuration changes survive Cloud Shell session restarts.
- Why C is incorrect: Cloud Shell does not have a built-in default zone of `us-central1-a`. The zone reverts to whatever is saved in the gcloud configuration file in your home directory, not to a hardcoded system default.
- Why D is incorrect: There is no 24-hour expiration timer on gcloud configuration settings. Configuration persists until explicitly changed by the user or until the home directory storage is deleted.

---

## Question 10

Your organization wants to prevent anyone from creating downloadable service account keys across all GCP Projects, even if those users have the `roles/iam.serviceAccountAdmin` role. What is the correct control to implement?

A. Remove `roles/iam.serviceAccountAdmin` from all users across the organization.

B. Apply the `constraints/iam.disableServiceAccountKeyCreation` Organization Policy constraint at the Organization level.

C. Create a custom IAM role that omits the `iam.serviceAccountKeys.create` permission and assign it to all users.

D. Enable the Security Command Center and configure it to auto-delete service account keys.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Removing the IAM role would prevent users from managing service accounts at all, which is far more restrictive than necessary. The goal is specifically to prevent key creation while still allowing other service account management tasks.
- Why C is incorrect: Creating and assigning a custom role to every user is operationally complex and does not scale. New users would not be covered unless the administrator remembered to assign the custom role. Additionally, users with the original `serviceAccountAdmin` role could still create keys unless that role itself is replaced.
- Why D is incorrect: Security Command Center is a threat detection and security posture management service. It does not auto-delete IAM resources based on policy violations. Preventing key creation requires a preventive control, not a detective one.

---

End of Quiz — Module 01

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

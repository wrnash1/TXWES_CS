### 5. Quiz 1: Setting up an Environment (Question Bank)
**Question 1**
You want to receive an email notification if your Google Cloud spending exceeds $500 for the current month. You set up a budget and an alert threshold. What happens to your resources if the spending reaches $501?
A) All resources are immediately suspended to prevent further charges.
B) Compute instances are shut down, but storage remains active.
C) The resources continue to run normally, and you receive an email alert.
D) The project is automatically deleted.
*   **Correct Answer:** C) The resources continue to run normally, and you receive an email alert.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Budgets in GCP only trigger notifications (emails or Pub/Sub messages). They do not cap spending or suspend resources natively without custom automation.
    *   *Why B is incorrect:* GCP does not selectively shut down compute resources based on simple budget alerts.
    *   *Why D is incorrect:* GCP will never delete a project simply for crossing a billing threshold.

**Question 2**
At which level of the Google Cloud resource hierarchy are billing accounts attached to pay for consumed resources?
A) Organization level
B) Folder level
C) Project level
D) Resource level
*   **Correct Answer:** C) Project level
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While Organizations *own* Billing Accounts, the actual linkage that pays for a running VM happens by associating the Billing Account with the specific Project.
    *   *Why B is incorrect:* Folders are used to group projects for IAM and policy inheritance, not for direct billing linkages.
    *   *Why D is incorrect:* Individual resources (like a single VM) do not have their own billing accounts attached; they inherit the billing link from their parent Project.

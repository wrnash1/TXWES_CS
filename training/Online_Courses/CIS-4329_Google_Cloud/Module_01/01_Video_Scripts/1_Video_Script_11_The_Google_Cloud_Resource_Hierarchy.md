### 1. Video Script 1.1: The Google Cloud Resource Hierarchy
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Google Cloud Administration. Before you can spin up servers or databases, you must understand how Google organizes resources. Everything in GCP belongs to a strict hierarchy."
**Visual:** A tree diagram showing the hierarchy. Top: Organization Node. Middle: Folders. Bottom: Projects. Under Projects: Resources (VMs, Storage).
**[Alt-text: A tree diagram representing the GCP hierarchy. The root node is 'Organization (e.g., txwes.edu)'. Below it are 'Folders (e.g., HR, IT)'. Below Folders are 'Projects (e.g., Website-Prod)'. Below Projects are 'Resources (e.g., Compute Engine VMs, Cloud Storage buckets)'.]**
**Audio:** "At the very top is the Organization node. Below that are Folders, which let you group things by department. Below folders are Projects. Projects are the core organizational unit in GCP—every resource, like a VM or a bucket, must belong to a Project. Crucially, policies and permissions cascade downwards. If you grant someone Viewer access at the Folder level, they have Viewer access to every Project inside that folder."

---

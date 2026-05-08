### 4. Lab 4: Configuring DFS Namespaces and NTFS Permissions
**Objective:** Create a unified DFS Namespace and apply restrictive NTFS permissions to a shared folder.
**Instructions:**
1. Boot your Windows Server DC VM.
2. Open **Server Manager** and install the **DFS Namespaces** role service (under File and Storage Services).
3. On the C: drive, create a folder named `CorpData`. Inside it, create a folder named `Finance`.
4. Right-click `CorpData`, go to Properties -> Sharing -> Advanced Sharing. Share it and set Share Permissions to **Everyone: Full Control**.
5. Go to the Security tab (NTFS Permissions) of the `Finance` folder. Click Advanced. Disable inheritance. Remove 'Users'. Add your specific domain Admin account with Full Control.
6. Open **DFS Management** from the Tools menu.
7. Create a new Namespace. Set the server as your DC. Name the namespace `Public`. Select "Domain-based namespace".
8. Add a new folder to the namespace called `Corporate_Data` and set the target to your `\\[ServerName]\CorpData` share.
**Deliverable:** Take a screenshot of the DFS Management console showing your newly created namespace and folder target. Submit to Blackboard.

---

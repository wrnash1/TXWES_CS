# Reading Guide: Module 07 - File and Print Services

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 07 – File and Print Services**! This week's study material covers how Windows Server manages shared storage and networked printing. File Services — including SMB shares, NTFS permissions, DFS Namespaces, and File Server Resource Manager — and Print Services are tested on the AZ-800 exam in both configuration and troubleshooting scenarios.

As a student, you will learn how NTFS and Share permissions interact, how DFS creates a unified namespace across multiple servers, and how to deploy and manage shared printers through the Print Management console. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **NTFS Permissions vs. Share Permissions**: NTFS permissions apply to any access — local or remote — and offer granular control (Full Control, Modify, Read & Execute, Read, Write, etc.). Share permissions apply only to remote (network) access and have three levels: Full Control, Change, and Read. When both are configured, the most restrictive combination applies.
* **DFS Namespaces (DFSN)**: Allows administrators to group shared folders located on different servers under a single, unified path (e.g., `\\corp.local\Files`). Users connect to the namespace path rather than individual server share paths, simplifying access and enabling location transparency.
* **DFS Replication (DFSR)**: A multi-master replication engine that keeps the contents of folders synchronized across multiple servers. DFSR uses Remote Differential Compression (RDC) to replicate only the changed portions of files, reducing bandwidth usage.
* **File Server Resource Manager (FSRM)**: A Windows Server role service that provides Quota Management (limits how much disk space a user or folder can consume), File Screening (blocks specific file types such as .mp3 or .exe from being saved to a share), and Storage Reports.
* **Print Server Role**: A Windows Server role that centralizes printer management. When a printer is shared through a print server and published in AD DS, clients can search for printers by location or type without knowing the server name.
* **SMB (Server Message Block)**: The network file-sharing protocol used by Windows for all file and print sharing. SMB 3.0 and later support encryption, multichannel (using multiple network adapters simultaneously), and direct memory-to-memory transfers over RDMA-capable adapters (SMB Direct).

---

### 2. Certification Exam Tips

* **Most restrictive permission wins over the network**: AZ-800 frequently presents a Share + NTFS permission conflict scenario. When a user accesses a folder across the network, the effective permission is the most restrictive of (Share permissions) AND (NTFS permissions). Over the local console, only NTFS permissions apply.
* **DFSN vs. DFSR distinction**: A common exam distractor confuses DFSN (namespace — the unified path) with DFSR (replication — syncing content). Know that you can use DFSN without DFSR (a namespace pointing to a single server) and DFSR without DFSN (replicating a folder without a namespace).
* **FSRM quota types — hard vs. soft**: A hard quota prevents files from being saved once the limit is reached. A soft quota only triggers a notification or report but does not block writes. Know which to choose in a given scenario.
* **Microsoft Learn Reference**: Review file and print services at [Microsoft Learn – File Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview) and [Microsoft Learn – DFS](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview) for current SMB and DFS documentation.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the file server and DFS documentation at [Microsoft Learn: File Server SMB Overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview) and [Microsoft Learn: DFS Namespaces](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview). Focus on NTFS vs. Share permissions, DFS configuration, and FSRM quota management.
* **Required Video:** Watch the video lecture on **File and Print Services** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will create a shared folder, configure NTFS and Share permissions for different user groups, and verify effective permissions over the network. You will also install FSRM, create a storage quota, and configure a file screen to block executable files from a shared folder.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the file server documentation at [Microsoft Learn: File Server SMB Overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview).
* [ ] Read the DFS documentation at [Microsoft Learn: DFS Namespaces](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview).
* [ ] Watch the video lecture on **File and Print Services** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.

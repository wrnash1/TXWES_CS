### 1. Video Script 4.1: NTFS Permissions vs. Share Permissions
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 4. One of the most fundamental jobs of a Windows Server is acting as a File Server. When you share a folder on the network, you must understand the interaction between two entirely different sets of permissions: Share Permissions and NTFS Permissions."
**Visual:** A Venn diagram. Left circle: Share Permissions (Network Access Only). Right circle: NTFS Permissions (Local and Network Access). The overlap reads: "Most Restrictive Wins".
**[Alt-text: Venn diagram showing Share Permissions and NTFS Permissions. The overlapping center intersection is labeled 'Effective Permission: The Most Restrictive Wins'.]**
**Audio:** "Share permissions only apply when a user accesses the folder over the network. NTFS permissions apply to the files on the actual hard drive, regardless of whether you access them locally or over the network. The golden rule of Windows file sharing is: when both apply, the *most restrictive* permission wins. Best practice? Set the Share permission to 'Everyone: Full Control', and use the granular NTFS permissions to actually lock down the folders. Let NTFS do the heavy lifting."

---

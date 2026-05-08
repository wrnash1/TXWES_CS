### 5. Quiz 4: Storage and File Services (Question Bank)
**Question 1**
An administrator shares a folder named 'HR_Docs' on the network. The Share permissions are set to give the 'HR_Group' Read-Only access. The NTFS security permissions on the folder give the 'HR_Group' Full Control. When a user in the 'HR_Group' accesses the folder over the network, what are their effective permissions?
A) Full Control
B) Read-Only
C) Write-Only
D) No Access
*   **Correct Answer:** B) Read-Only
*   **Distractor Analysis:**
    *   *Why A is incorrect:* When Share and NTFS permissions conflict during network access, the most restrictive permission wins. Read-Only (Share) is more restrictive than Full Control (NTFS).
    *   *Why C is incorrect:* Neither permission grants Write-Only access.
    *   *Why D is incorrect:* The user is granted Read access, so they are not entirely blocked from the folder.

**Question 2**
A company has two file servers, one in New York and one in Los Angeles. Users currently have to remember two different server names (`\\NY-FS01\Data` and `\\LA-FS01\Data`) to access company files. Which Windows Server technology should you implement to allow users to access all files via a single, unified path like `\\company.local\SharedData`?
A) DFS Replication (DFSR)
B) File Server Resource Manager (FSRM)
C) DFS Namespaces (DFSN)
D) Storage Spaces Direct (S2D)
*   **Correct Answer:** C) DFS Namespaces (DFSN)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DFSR is used to synchronize the *contents* of folders across servers, but it does not create the unified naming path for users to access them.
    *   *Why B is incorrect:* FSRM is used for storage quotas and file screening (blocking specific file extensions), not for abstracting network paths.
    *   *Why D is incorrect:* S2D is a hyper-converged infrastructure feature used to pool direct-attached storage across clustered servers, not for creating a logical namespace for SMB file shares.

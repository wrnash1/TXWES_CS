### 2. Reading Guide: IAM Policies
**High-Yield Concepts:**
*   **Primitive vs. Predefined Roles:** Never use primitive roles (Owner/Editor/Viewer) in production. Use predefined roles (e.g., `roles/storage.objectAdmin`) to enforce least privilege.
*   **Custom Roles:** If a predefined role gives too much access, you can create a Custom Role by combining specific, granular API permissions.

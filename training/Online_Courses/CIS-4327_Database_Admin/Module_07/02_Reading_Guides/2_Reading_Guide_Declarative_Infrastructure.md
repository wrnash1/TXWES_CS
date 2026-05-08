### 2. Reading Guide: Declarative Infrastructure
**High-Yield Concepts:**
*   **State Files:** Terraform remembers what it built by storing a `.tfstate` file. If you run the code again, Terraform looks at the state file and changes nothing, because it is *idempotent*.

### 2. Reading Guide: Cloud Networking
**High-Yield Concepts:** 
*   **Firewall Rules:** In GCP, firewall rules are applied to the network, but enforced at the VM instance level. They are stateful, meaning if you allow an incoming request, the outgoing reply is automatically allowed.
*   **Network Tags:** Instead of writing firewall rules for specific IP addresses, you apply the rule to a Tag (like `web-server`), and assign that tag to any VM that needs the rule.

### 2. Reading Guide: Disaster Recovery
**High-Yield Concepts:**
*   **Authoritative vs. Non-Authoritative Restore:** If you restore a DC non-authoritatively, it pulls the newest AD data from other DCs. If you restore it *authoritatively*, you force the other DCs to accept your restored data (used when an object was accidentally deleted everywhere).

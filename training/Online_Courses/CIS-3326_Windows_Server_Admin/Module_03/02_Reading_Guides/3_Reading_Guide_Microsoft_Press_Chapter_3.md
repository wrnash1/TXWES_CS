### 3. Reading Guide: Microsoft Press Chapter 3
**High-Yield Concepts:**
1. **User Configuration vs. Computer Configuration:** Every GPO has two halves. Computer policies apply when the machine boots up (e.g., software installation). User policies apply when the human logs in (e.g., mapped drives, folder redirection).
2. **Enforce / Block Inheritance:** You can right-click a GPO and set it to "Enforced", meaning no lower-level OU can override it. Conversely, you can right-click an OU and "Block Inheritance", preventing higher-level GPOs from flowing down.
3. **gpupdate /force:** The command-line tool used on a client computer to force it to pull the latest Group Policies immediately, rather than waiting the standard 90 minutes.

---

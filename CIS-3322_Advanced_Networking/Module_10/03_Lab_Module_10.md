# Lab Activity: Module 10 - Access Control Lists (ACLs)
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

## Objective
Configure and verify systems matching the operational parameters of **Access Control Lists (ACLs)**.

---

## Prerequisites
*   Ensure you have access to a terminal or a runtime environment matching the course requirements (e.g., Linux, macOS, Windows, or a cloud/web terminal).
*   Ensure you have administrative privileges if required to install packages or configure system services.

---

## Step-by-Step Instructions
1. **Create extended ACL: `access-list 101 permit tcp any host 10.1.1.5 eq 80`**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
2. **Apply ACL to interface: `ip access-group 101 in`**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
3. **Verify matches: `show access-lists`**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.

---

## Troubleshooting Guide
*   *Error:* `Permission Denied`
    * *Fix:* Remember to run administrative command sequences using `sudo` or execute with administrative privileges (e.g., Run as Administrator on Windows).
*   *Error:* `Command Not Found`
    * *Fix:* Verify your environmental path settings, or double-check if the utility package is installed.

---

## Deliverables
1. Document your completed steps with screenshots or terminal output logs showing successful execution.
2. Submit your completion report to your Canvas LMS assignment portal for grading.

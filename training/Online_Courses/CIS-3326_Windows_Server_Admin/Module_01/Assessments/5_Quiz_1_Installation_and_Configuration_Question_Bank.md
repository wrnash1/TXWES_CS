### 5. Quiz 1: Installation and Configuration (Question Bank)
**Question 1**
Which of the following is a primary advantage of installing Windows Server using the Server Core option instead of Desktop Experience?
A) It provides a larger selection of pre-installed graphical management tools.
B) It has a reduced attack surface and lower hardware footprint.
C) It allows for the installation of Microsoft Office applications directly on the server.
D) It forces the use of IPv6 for all network communications.
*   **Correct Answer:** B) It has a reduced attack surface and lower hardware footprint.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Server Core removes almost all graphical tools; you must manage it remotely or via CLI.
    *   *Why C is incorrect:* You generally do not install client applications like Office on a server, and certainly not on Server Core which lacks a GUI.
    *   *Why D is incorrect:* Server Core supports both IPv4 and IPv6, just like the Desktop Experience.

**Question 2**
You have just installed a new Windows Server Core machine. Which command-line utility provides a simple, text-based menu to configure the hostname, IP address, and Windows updates?
A) ipconfig
B) sysdm.cpl
C) sconfig
D) ServerManager.exe
*   **Correct Answer:** C) sconfig
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ipconfig` only displays network settings; it does not provide an interactive menu to change hostnames or run updates.
    *   *Why B is incorrect:* `sysdm.cpl` opens the graphical System Properties dialog, which is not available natively in Server Core.
    *   *Why D is incorrect:* `ServerManager.exe` launches the graphical Server Manager, which is omitted from Server Core.

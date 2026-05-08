### 5. Quiz 1: OS Fundamentals (Question Bank)
**Question 1**
Which of the following describes a Type 1 hypervisor?
A) It runs as an application on top of an existing host operating system like Windows 10.
B) It runs directly on the server's bare-metal hardware.
C) It cannot run Linux virtual machines.
D) It requires Oracle VirtualBox to function.
*   **Correct Answer:** B) It runs directly on the server's bare-metal hardware.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a Type 2 hypervisor (hosted), not Type 1.
    *   *Why C is incorrect:* Type 1 hypervisors can run almost any supported OS, including Linux.
    *   *Why D is incorrect:* VirtualBox is a Type 2 hypervisor. Type 1 hypervisors include ESXi and Hyper-V.

**Question 2**
What is the primary function of an operating system's kernel?
A) To provide a graphical user interface (GUI) for the user.
B) To compile source code into executable binaries.
C) To manage hardware resources and act as a bridge between applications and data processing.
D) To run web browsers and word processors.
*   **Correct Answer:** C) To manage hardware resources and act as a bridge between applications and data processing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The GUI is a user-space application (like a desktop environment), not the kernel itself.
    *   *Why B is incorrect:* Compiling code is done by a compiler (like GCC), not the OS kernel.
    *   *Why D is incorrect:* Web browsers run in user space; the kernel simply provides them the resources they need to run.

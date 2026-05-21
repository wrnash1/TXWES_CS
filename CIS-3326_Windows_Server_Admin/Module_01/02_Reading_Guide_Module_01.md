# Reading Guide: Module 01 - Windows Server Installation and Editions

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 01 – Windows Server Installation and Editions**! This week's study material covers the different editions of Windows Server, deployment options, and the initial post-installation configuration steps required before a server can enter production. Understanding how to select the right edition and installation option is a foundational skill tested on the AZ-800 exam and applied in every real-world server deployment.

As a student, you will learn when to choose Server Core versus Desktop Experience, how to license each edition, and how to perform critical first-boot configuration tasks using `sconfig` and PowerShell. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Windows Server Editions (Standard vs. Datacenter)**: Standard edition licenses up to two Hyper-V virtual machine instances per physical license; Datacenter edition permits unlimited VMs on the same licensed host and unlocks additional features such as Storage Spaces Direct and Shielded VMs.
* **Server Core**: A minimal installation option that omits the graphical shell (Explorer, Start menu, most MMC snap-ins). It reduces the attack surface, lowers patching overhead, and decreases RAM consumption, but requires remote management tools or command-line interfaces for administration.
* **Desktop Experience**: The full GUI installation that includes Server Manager, all MMC snap-ins, and the Windows graphical shell. It is more approachable for new administrators but carries a larger attack surface than Server Core.
* **sconfig**: A text-based, menu-driven configuration tool built into Windows Server. It allows administrators to set the hostname, IP address, domain membership, remote management settings, and Windows Update policy without a full graphical interface — essential for Server Core post-install.
* **Windows Admin Center (WAC)**: A browser-based, locally deployed management platform that provides a modern GUI for administering Server Core machines, Hyper-V hosts, and failover clusters remotely. WAC is the strategic replacement for traditional MMC snap-ins.
* **KMS vs. MAK Activation**: Key Management Service (KMS) activates servers automatically by contacting an internal KMS host — ideal for large domain-joined environments. Multiple Activation Key (MAK) is a one-time activation key used for machines that cannot reach the corporate network, such as air-gapped systems.

---

### 2. Certification Exam Tips

* **Server Core for smallest footprint scenarios**: AZ-800 frequently presents a scenario requiring the smallest possible attack surface. The answer is Server Core. Know that it can be managed remotely via Windows Admin Center, PowerShell remoting (`Enter-PSSession`), or RSAT tools installed on an admin workstation.
* **`sconfig` vs. PowerShell cmdlets**: Exam questions may ask which tool provides interactive first-boot configuration on Server Core. `sconfig` offers a numbered menu; PowerShell cmdlets (`Rename-Computer`, `New-NetIPAddress`, `Add-Computer`) are the scripted equivalent. Know both.
* **Edition in-place upgrade**: You can upgrade Standard to Datacenter using `DISM /online /Set-Edition` without a full reinstall. Downgrade is not supported in place — this is a common exam distractor.
* **Microsoft Learn Reference**: Review the official installation options documentation at [Microsoft Learn – Get Started with Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/get-started-with-windows-server) for the most current edition comparison, installation walkthroughs, and Server Core management guides.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the Windows Server installation and editions documentation at [Microsoft Learn: Windows Server Get Started](https://learn.microsoft.com/en-us/windows-server/get-started/get-started-with-windows-server). Pay particular attention to the "Server Core vs Desktop Experience" and "Edition comparison" sections.
* **Required Video:** Watch the video lecture on **Windows Server Installation and Editions** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will install Windows Server in a virtual machine, configure the hostname and static IP address using `sconfig`, and join the server to a workgroup. You will also compare the Server Core and Desktop Experience installation options in terms of available tools and resource usage.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the Windows Server installation and editions documentation at [Microsoft Learn: Windows Server Get Started](https://learn.microsoft.com/en-us/windows-server/get-started/get-started-with-windows-server).
* [ ] Watch the video lecture on **Windows Server Installation and Editions** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.

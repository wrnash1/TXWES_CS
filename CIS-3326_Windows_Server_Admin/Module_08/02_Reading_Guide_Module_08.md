# Reading Guide: Module 08 - Remote Desktop Services (RDS)

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 08 – Remote Desktop Services (RDS)**! This week's study material covers how Windows Server delivers remote application and desktop sessions to users over the network. RDS enables centralized application hosting, thin-client computing, and secure remote access — all scenarios tested on the AZ-800 exam.

As a student, you will learn the roles that make up an RDS deployment, how to license RDS correctly, and how the RD Gateway secures external access. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **RD Session Host (RDSH)**: The server role that hosts Windows-based applications and desktops for remote users. Multiple users can connect simultaneously and run individual sessions on the same server, sharing its CPU and RAM.
* **RD Connection Broker**: The role service that manages and distributes user sessions across a farm of RD Session Host servers. It reconnects users to their existing disconnected sessions and provides load balancing to prevent any single host from being overloaded.
* **RD Gateway (RDG)**: A role service that allows remote users to connect to internal RDS resources from the internet over HTTPS (port 443), eliminating the need to expose RDP port 3389 directly or require a traditional VPN. It uses an SSL tunnel to wrap the RDP connection.
* **RD Web Access (RDWA)**: A role service that provides a web portal (typically at `https://servername/rdweb`) from which users can launch RemoteApp programs or full desktop sessions through a browser without installing a standalone RDP client.
* **RemoteApp**: A feature of RDS that allows individual applications to be streamed to a user's desktop so they appear to run locally while actually executing on the RD Session Host. The application window integrates with the user's local taskbar and Start menu.
* **RDS CAL (Client Access License)**: A per-user or per-device license required for each client that connects to an RD Session Host. Without valid RDS CALs managed by an RD Licensing server, connections are blocked after a 120-day grace period expires.

---

### 2. Certification Exam Tips

* **RD Gateway port and protocol**: AZ-800 commonly asks how to provide secure external RDS access without a VPN. The answer is RD Gateway, which uses HTTPS (port 443) — not the standard RDP port 3389. Know that RD Gateway can also enforce Network Access Protection (NAP) policies.
* **RD Connection Broker is required for session farms**: A single RDSH server does not need a Connection Broker. Once you have two or more RDSH servers forming a farm, the Connection Broker is required to distribute sessions and enable session reconnection.
* **Per-User vs. Per-Device CALs**: Per-Device CALs are assigned to a specific computer that accesses any RDS server in the organization. Per-User CALs are assigned to a user account and allow that user to connect from any device. Choosing the wrong type is a compliance violation.
* **Microsoft Learn Reference**: Review the RDS deployment guide at [Microsoft Learn – Remote Desktop Services](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remote-desktop-services-overview) for full role descriptions, deployment scenarios, and licensing guidance.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the RDS overview and role descriptions at [Microsoft Learn: Remote Desktop Services Overview](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remote-desktop-services-overview). Focus on role descriptions, the RD Gateway configuration, and licensing requirements.
* **Required Video:** Watch the video lecture on **Remote Desktop Services** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will deploy a basic RDS environment including the RD Session Host and RD Web Access roles. You will publish a RemoteApp program through the RDWA portal and test connecting to it from a client machine using the Remote Desktop client.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the RDS overview at [Microsoft Learn: Remote Desktop Services Overview](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remote-desktop-services-overview).
* [ ] Watch the video lecture on **Remote Desktop Services** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.

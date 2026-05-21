# Quiz: Module 08 - Remote Desktop Services (RDS)

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A company wants to allow external users to connect to internal Remote Desktop Services resources securely from the internet without requiring a traditional VPN, while keeping the RD Session Host servers off the public internet. Which RDS role service provides this capability?

A) RD Web Access, which publishes RemoteApp icons through a web portal accessible from any browser.
B) RD Connection Broker, which routes external user connections directly to available Session Hosts across the internet.
C) RD Gateway, which acts as a secure reverse proxy that tunnels RDP connections from the internet over HTTPS to internal RDS resources.
D) RD Licensing, which validates that remote users hold valid CALs before permitting internet-based connections.

* **Correct Answer:** C) RD Gateway, which acts as a secure reverse proxy that tunnels RDP connections from the internet over HTTPS to internal RDS resources.
* **Distractor Analysis:**
  * *Why A is incorrect:* RD Web Access provides a web portal for launching RemoteApp programs or full desktop sessions, but it does not provide the secure tunnel for external connectivity. RD Gateway provides the encrypted HTTPS tunnel that RD Web Access sessions travel through.
  * *Why B is incorrect:* The RD Connection Broker routes sessions among RD Session Hosts within the internal farm for load balancing and reconnection. It operates on the internal network and is not designed to handle external internet connections directly.
  * *Why D is incorrect:* RD Licensing manages and tracks Client Access Licenses for RDS connections — it is an administrative and compliance component, not a connectivity or security gateway for external users.

---

### Question 2

After deploying a farm of four RD Session Host servers, users report that when they reconnect after a brief disconnection, they are sometimes placed on a different server and lose their running session. Which RDS role service must be added to resolve this?

A) RD Gateway, configured to pin each user to a specific external IP address.
B) RD Connection Broker, which tracks active and disconnected sessions and reconnects users to the correct host.
C) RD Web Access, which stores session state in a browser cookie for seamless reconnection.
D) RD Virtualization Host, which persists VM state for each user across disconnections.

* **Correct Answer:** B) RD Connection Broker, which tracks active and disconnected sessions and reconnects users to the correct host.
* **Distractor Analysis:**
  * *Why A is incorrect:* RD Gateway manages secure external access — it does not track or maintain session-to-host mappings. Pinning users to external IP addresses would not reconnect them to their disconnected internal session.
  * *Why C is incorrect:* RD Web Access is a web portal for launching sessions — it does not maintain server-side session state. Browser cookies can store RemoteApp shortcuts but cannot track which RD Session Host holds a disconnected session.
  * *Why D is incorrect:* RD Virtualization Host is used for Virtual Desktop Infrastructure (VDI), where each user gets a personal VM. The scenario describes a Session Host farm, not a VDI deployment, and RD Virtualization Host is not used for session-based RDS farms.

---

### Question 3

An organization has deployed Remote Desktop Services. After the 120-day grace period expires on the RD Session Host, users receive a message that "The remote session was disconnected because there are no Remote Desktop License Servers available." What must be configured to resolve this?

A) Install a second RD Session Host server — the message indicates the existing server has reached its maximum session count.
B) Deploy an RD Licensing server, activate it with Microsoft, install RDS CALs, and configure the RD Session Host to point to the license server.
C) Enable Remote Desktop on the server in System Properties — the message indicates Remote Desktop is disabled for standard user connections.
D) Purchase Azure AD Premium licenses and enable Azure AD-based RDS licensing to replace the on-premises RD Licensing server.

* **Correct Answer:** B) Deploy an RD Licensing server, activate it with Microsoft, install RDS CALs, and configure the RD Session Host to point to the license server.
* **Distractor Analysis:**
  * *Why A is incorrect:* The error message specifically references an RD License Server, not server capacity. Adding a second RD Session Host would only distribute existing sessions — it would not resolve a licensing infrastructure absence.
  * *Why C is incorrect:* Remote Desktop being disabled would cause a different error (connection refused before a session is established) — not a message about missing license servers. The 120-day grace period explicitly indicates RDS is working but unlicensed.
  * *Why D is incorrect:* On-premises RDS deployments use on-premises RD Licensing servers with traditional RDS CALs. Azure AD Premium licenses are for cloud identity and Intune management — they are not a replacement for RDS CALs in a traditional on-premises RDS deployment.

---

### Question 4

A company wants to publish a single application (a legacy ERP software) to remote users so that the application appears to run on users' local desktops, integrated with their local Start menu and taskbar, without giving users access to a full remote desktop. Which RDS feature provides this experience?

A) RD Web Access configured to open a full desktop session when the ERP shortcut is clicked.
B) RemoteApp, which streams the application window to the user's local desktop where it appears and behaves like a locally installed application.
C) RD Virtualization Host with a personal virtual desktop assigned to each user running only the ERP application.
D) Application Virtualization (App-V), which packages the ERP application for streaming to client devices without RDS.

* **Correct Answer:** B) RemoteApp, which streams the application window to the user's local desktop where it appears and behaves like a locally installed application.
* **Distractor Analysis:**
  * *Why A is incorrect:* A full desktop session through RD Web Access gives users an entire remote desktop environment — including the taskbar, file explorer, and all applications on the Session Host — which is far more access than needed for a single legacy application.
  * *Why C is incorrect:* RD Virtualization Host with personal VDI desktops assigns each user a dedicated virtual machine. This is an expensive and complex solution for delivering a single application and gives users full VM-level access, not a seamlessly integrated application window.
  * *Why D is incorrect:* App-V (Application Virtualization) packages applications into isolated virtual environments that run locally on the client device — it requires the application to be installed on client machines and does not use RDS or RD Session Hosts for hosting.

---

### Question 5

An RDS administrator needs to ensure that only users who are members of the `RemoteWorkers` security group are permitted to establish RDP sessions through the RD Gateway, regardless of what other connections policies exist. Which RD Gateway component enforces this access control?

A) An RD Resource Authorization Policy (RD RAP) that specifies which internal resources the `RemoteWorkers` group can connect to.
B) An RD Connection Authorization Policy (RD CAP) that specifies which users or groups are permitted to connect through the RD Gateway at all.
C) A Security Filtering setting on the RD Gateway GPO that restricts which users can receive Gateway configuration settings.
D) An NTFS permission on the RD Gateway server's certificate that restricts which users can complete the TLS handshake.

* **Correct Answer:** B) An RD Connection Authorization Policy (RD CAP) that specifies which users or groups are permitted to connect through the RD Gateway at all.
* **Distractor Analysis:**
  * *Why A is incorrect:* An RD RAP (Resource Authorization Policy) controls which internal network resources (servers, ports) a connected user can reach after they have already been authorized by the CAP. The RAP alone does not control who can connect through the Gateway.
  * *Why C is incorrect:* Security Filtering on a GPO controls which computers or users receive the Group Policy settings — it is a policy targeting mechanism, not an RD Gateway connection access control mechanism.
  * *Why D is incorrect:* TLS certificate NTFS permissions control which accounts can read the certificate private key on the server — this is a server-side cryptographic configuration, not a user-authentication or connection-authorization mechanism for RD Gateway sessions.

# Quiz: Module 12 - Cloud and Container Penetration Testing
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is the primary goal of privilege escalation during post-exploitation on a compromised system?
*   A) Performing network reconnaissance to map the internal subnet.
*   B) Moving from a low-privilege user account to an administrator or root account to gain full control of the system.
*   C) Establishing a persistent backdoor that survives reboots without requiring re-exploitation.
*   D) Extracting and exfiltrating data from the compromised host to the attacker's server.
*   **Correct Answer:** B) Moving from a low-privilege user account to an administrator or root account to gain full control of the system.
*   **Distractor Analysis:**
    *   *Why B is correct:* Privilege escalation is the process of gaining higher access rights than initially obtained — typically moving from a standard user to administrator (Windows) or root (Linux). With elevated privileges, the tester can perform actions that demonstrate full system compromise: dumping credentials, modifying system configurations, installing persistence mechanisms, and accessing protected data. It is a key step that validates the real-world business impact of the initial access.
    *   *Why A is incorrect:* Network reconnaissance and subnet mapping are performed during the reconnaissance and scanning phases, not specifically during privilege escalation. Lateral movement (which uses escalated privileges) involves moving to other hosts, but the escalation step itself is about gaining higher privileges on the current system.
    *   *Why C is incorrect:* Establishing persistence is a separate post-exploitation activity that typically occurs after privilege escalation. Persistence ensures continued access — it is not the definition of privilege escalation itself.
    *   *Why D is incorrect:* Data exfiltration is a post-exploitation objective that may leverage escalated privileges but is a distinct activity. Escalation is specifically about increasing privilege level, not about extracting data.

---

**Question 2**
In the context of cloud penetration testing, which of the following best describes an **Instance Metadata Service (IMDS) attack**?
*   A) An attack that enumerates publicly accessible S3 storage buckets to identify files that have been inadvertently exposed to the internet without authentication.
*   B) An attack that exploits a Server-Side Request Forgery (SSRF) vulnerability in a cloud-hosted web application to query the instance metadata endpoint and retrieve temporary IAM role credentials.
*   C) An attack that abuses overly permissive IAM policies to escalate from a low-privilege cloud user role to an administrator role by attaching new policies to the compromised account.
*   D) An attack that escapes a Docker container by exploiting a mounted Docker socket to spawn a new privileged container with host filesystem access.
*   **Correct Answer:** B) An attack that exploits a Server-Side Request Forgery (SSRF) vulnerability in a cloud-hosted web application to query the instance metadata endpoint and retrieve temporary IAM role credentials.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cloud virtual machines expose a metadata service at `169.254.169.254` that provides instance configuration including temporary IAM credentials for any role attached to the instance. If the application running on that VM is vulnerable to SSRF — where the server makes HTTP requests to URLs controlled by user input — an attacker can use that SSRF to fetch `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>` and retrieve the credentials. These credentials can then authenticate to cloud APIs with the instance's permissions. This SSRF → IMDS chain is the canonical cloud escalation path tested on PT0-002.
    *   *Why A is incorrect:* This describes an S3 bucket misconfiguration attack — a distinct cloud vulnerability involving improperly secured object storage. It does not involve SSRF or instance metadata.
    *   *Why C is incorrect:* This describes IAM privilege escalation through policy manipulation — a separate cloud attack technique that exploits overly permissive IAM permissions directly. It does not involve the metadata service or SSRF.
    *   *Why D is incorrect:* This describes a Docker socket-based container escape — a container security technique. Container escape and IMDS attacks are distinct attack categories operating at different layers of cloud infrastructure.

---

**Question 3**
A penetration tester discovers a Docker container running with the `--privileged` flag enabled. Why does this configuration represent a critical security risk?
*   A) Privileged containers encrypt all network traffic using a stronger cipher, making traffic analysis more difficult for defenders.
*   B) The `--privileged` flag grants the container full access to all host devices and removes most kernel capability restrictions, enabling the container process to interact with the host system as if it were running directly on the host.
*   C) Privileged containers automatically pull updated images from a public registry, potentially introducing malicious code through supply chain compromise.
*   D) The `--privileged` flag enables root user access inside the container but does not affect the isolation boundary between the container and the host operating system.
*   **Correct Answer:** B) The `--privileged` flag grants the container full access to all host devices and removes most kernel capability restrictions, enabling the container process to interact with the host system as if it were running directly on the host.
*   **Distractor Analysis:**
    *   *Why B is correct:* Docker's `--privileged` flag disables the security boundaries that normally isolate a container from its host. It grants access to all host devices (including `/dev`), removes seccomp and AppArmor restrictions, and enables capabilities like `SYS_ADMIN` that allow mounting filesystems and loading kernel modules. An attacker inside a privileged container can mount the host's root filesystem, read host processes, and effectively operate as root on the underlying host — making privileged container compromise equivalent to full host compromise.
    *   *Why A is incorrect:* The `--privileged` flag has no effect on network traffic encryption. Container networking is controlled by Docker network drivers and TLS configuration — entirely separate from the privilege flag.
    *   *Why C is incorrect:* The `--privileged` flag does not control image pulling behavior or registry access. Image supply chain risks are addressed through image signing and trusted registries — not related to the privilege flag.
    *   *Why D is incorrect:* This is precisely backwards. The `--privileged` flag explicitly removes container isolation boundaries. A process running as root inside a privileged container can escape to the host — the isolation boundary is broken, not preserved.

---

**Question 4**
Before conducting a penetration test that includes AWS infrastructure, what authorization step is required beyond the client's standard written authorization letter?
*   A) No additional authorization is needed — the client's authorization letter covers all infrastructure they own, including cloud resources.
*   B) The tester must notify the cloud provider (AWS) according to its penetration testing policy, as some testing activities against cloud infrastructure require advance approval or are explicitly prohibited.
*   C) The tester must obtain a separate authorization letter from the cloud provider's legal team before any reconnaissance — even passive OSINT against publicly visible cloud resources.
*   D) Cloud infrastructure is considered out of scope for all penetration tests because cloud providers assume full security responsibility under the shared responsibility model.
*   **Correct Answer:** B) The tester must notify the cloud provider (AWS) according to its penetration testing policy, as some testing activities against cloud infrastructure require advance approval or are explicitly prohibited.
*   **Distractor Analysis:**
    *   *Why B is correct:* PT0-002 specifically tests that cloud penetration testing has additional authorization requirements. AWS, Azure, and GCP each publish penetration testing policies that define what types of testing are permitted, what requires advance notification, and what is prohibited (such as DDoS simulation or testing cloud provider infrastructure). A client's authorization letter covers their own systems but does not grant permission to test cloud provider-managed infrastructure or violate the cloud provider's terms of service. Failing to follow the cloud provider's policy can result in account suspension or legal action.
    *   *Why A is incorrect:* A client's authorization letter covers systems the client owns and controls, but cloud providers have their own policies governing what testing is permitted on their platforms. The client cannot grant permissions that the cloud provider has reserved or restricted.
    *   *Why C is incorrect:* Cloud providers generally do not require a separate legal authorization letter for all testing — they publish self-service policies that define permitted activities. The requirement is policy compliance and (for some activities) advance notification, not a formal legal document from the provider's legal team.
    *   *Why D is incorrect:* Cloud infrastructure owned and configured by the client (VMs, S3 buckets, IAM policies, security groups) is absolutely in scope for penetration testing. The shared responsibility model assigns the customer responsibility for their configurations — which is exactly what cloud penetration testing evaluates.

---

**Question 5**
A penetration tester finds that `/var/run/docker.sock` is mounted inside a running Docker container. Why does this represent a container escape vulnerability?
*   A) The Docker socket file contains the container's encryption keys, allowing an attacker to decrypt all inter-container network traffic.
*   B) Mounting the Docker socket inside a container gives processes in that container direct access to the Docker daemon on the host, allowing them to create new privileged containers with the host filesystem mounted — effectively escaping to root on the host.
*   C) The Docker socket is used for external API calls and its presence inside a container exposes the container's internal network to the internet.
*   D) Mounting the Docker socket increases the container's memory allocation, creating a denial-of-service risk if exploited by a resource-intensive process.
*   **Correct Answer:** B) Mounting the Docker socket inside a container gives processes in that container direct access to the Docker daemon on the host, allowing them to create new privileged containers with the host filesystem mounted — effectively escaping to root on the host.
*   **Distractor Analysis:**
    *   *Why B is correct:* The Docker socket (`/var/run/docker.sock`) is the Unix socket the Docker CLI uses to communicate with the Docker daemon running as root on the host. If this socket is mounted inside a container, any process in that container can send Docker API commands directly to the host daemon — for example, creating a new container with `--privileged` and `-v /:/host` to mount the entire host filesystem. The attacker can then chroot into the host filesystem and read or modify any host file, install a backdoor, or escalate to full host root access. This is one of the most common real-world container escape techniques.
    *   *Why A is incorrect:* The Docker socket is a control-plane communication channel — it does not store encryption keys or provide access to network traffic between containers. Container network encryption is handled at a different layer entirely.
    *   *Why C is incorrect:* The Docker socket is a local Unix domain socket used for local API communication between the Docker CLI and daemon. It does not expose the container's network to the internet and has no role in external network routing.
    *   *Why D is incorrect:* The Docker socket is a communication interface, not a resource allocation mechanism. It has no effect on container memory limits, and the vulnerability is privilege escalation/escape — not denial of service.

# Quiz: Module 14 — Threat Modeling in DevSecOps

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

Instructions: Select the single best answer for each question. Review the distractor analysis after completing the quiz.

---

### Question 1

An attacker compromises a container in a Kubernetes cluster. The container is running as root with `allowPrivilegeEscalation: true`. The attacker exploits a kernel vulnerability, escapes the container namespace, and gains root access to the underlying node. Which STRIDE category does this attack fall under?

- A) Information Disclosure — because the attacker gains access to data stored on the node
- B) Tampering — because the attacker modifies the container runtime environment
- C) Elevation of Privilege — because the attacker gains capabilities beyond what their container authorization permits
- D) Spoofing — because the container runtime process impersonates a privileged system process

Correct Answer: C — Elevation of Privilege is the STRIDE category for attacks where an actor gains capabilities beyond their authorization. The attacker started with container-level access and gained node-level root access — a privilege escalation. The violated security property is Authorization. This is the classic container escape threat that Security Contexts (`runAsNonRoot`, `allowPrivilegeEscalation: false`, `capabilities.drop: ALL`) and the PodSecurity `restricted` profile are designed to prevent.

Distractor Analysis:

- Why A is incorrect: While the attacker may gain access to data after the privilege escalation, the attack technique itself is privilege escalation. Information Disclosure describes the exposure of sensitive data to unauthorized parties, not the act of gaining elevated system access.
- Why B is incorrect: Tampering describes the unauthorized modification of data or code. The attacker is gaining unauthorized access to a higher privilege level, not modifying data. Container escape is an authorization failure, not an integrity failure.
- Why D is incorrect: Spoofing describes an attacker claiming to be someone they are not — an identity and authentication failure. The container escape does not involve identity impersonation; it involves exploiting a kernel vulnerability to break isolation boundaries.

---

### Question 2

A developer accidentally commits an AWS secret access key to a GitHub repository. The key is discovered 6 hours later and rotated. During those 6 hours, the key was used by an attacker to list S3 buckets and download files containing customer PII. Which STRIDE category best describes the initial threat that caused this incident?

- A) Repudiation — because the developer denied committing the secret when first questioned
- B) Tampering — because the attacker modified S3 bucket contents using the stolen key
- C) Information Disclosure — because the secret committed to the repository was exposed to unauthorized parties who could access and read it
- D) Denial of Service — because the attacker's S3 API calls consumed API rate limits

Correct Answer: C — Information Disclosure describes the exposure of sensitive data (the AWS secret key) to unauthorized parties (anyone who can read the repository, including external attackers who monitor GitHub for newly committed secrets). The violated security property is Confidentiality. The secret scanning gate in a CI/CD pipeline is the control designed to prevent this threat — detecting secrets before they are pushed.

Distractor Analysis:

- Why A is incorrect: Repudiation describes the inability to prove that an action occurred. The developer's denial is not a STRIDE threat — it is a human behavior. The threat that caused the incident was the exposure of the credential, which is Information Disclosure.
- Why B is incorrect: The attacker downloading PII is itself an Information Disclosure threat (customer data exposed). The S3 modifications (if any) would be Tampering. But the root cause that enabled the attack — the committed credential — is Information Disclosure of the secret key.
- Why D is incorrect: API rate limit consumption is a side effect of the attacker's activity. The S3 API calls themselves represent information disclosure (reading customer data). Denial of Service would require the attacker to degrade availability for legitimate users.

---

### Question 3

What are the four elements of a data flow diagram, and what visual shape conventionally represents each?

- A) Actor (circle), System (square), Message (arrow), Network (cloud shape)
- B) Process (circle/oval), Data store (parallel lines), External entity (rectangle), Data flow (directed arrow)
- C) Service (hexagon), Database (cylinder), User (stick figure), API (dashed arrow)
- D) Component (diamond), Repository (folder), Interface (rectangle), Event (wavy arrow)

Correct Answer: B — The four standard DFD elements from the Yourdon-Coad DFD methodology used in threat modeling are: Process (transformation of data, drawn as a circle or oval), Data store (persistence of data, drawn as two parallel horizontal lines), External entity (actor outside the system boundary, drawn as a rectangle), and Data flow (movement of data, drawn as a directed arrow labeled with the data carried). Trust boundaries are added as dashed lines separating zones.

Distractor Analysis:

- Why A is incorrect: "Actor," "System," "Message," and "Network" are elements of other diagram types (UML use case diagrams, sequence diagrams). They are not the standard DFD element vocabulary used in threat modeling.
- Why C is incorrect: Hexagons, cylinders, stick figures, and dashed arrows are from UML component and deployment diagrams, not threat modeling DFDs. Stick figures represent actors in UML use case diagrams, not external entities in DFDs.
- Why D is incorrect: Diamonds, folders, and wavy arrows are not standard DFD elements. These appear in other diagramming notations (BPMN, entity-relationship diagrams) but not in the DFD notation used for threat modeling.

---

### Question 4

A security engineer is reviewing a threat model for a microservices application. The model includes a data flow from the authentication service to a PostgreSQL database. The engineer identifies a threat: "An attacker who intercepts network traffic between the auth service and the database can read authentication tokens and session data in plaintext." Which STRIDE category applies, and what is the correct countermeasure?

- A) Tampering — encrypt the database files at rest using AES-256
- B) Spoofing — require the database to authenticate the auth service using a certificate
- C) Information Disclosure — require TLS for all connections between the auth service and the database, combined with a Network Policy that allows only the auth service pod to reach the database port
- D) Elevation of Privilege — apply `readOnlyRootFilesystem: true` to the auth service container

Correct Answer: C — Intercepting network traffic to read sensitive data is Information Disclosure — the violated security property is Confidentiality. The correct countermeasures are: TLS encryption for the data in transit (preventing interception from yielding readable data) and a Kubernetes Network Policy restricting which pods can reach the database port (reducing the attack surface). Both countermeasures together address the threat: TLS protects against passive interception, Network Policy prevents unauthorized pods from even initiating connections.

Distractor Analysis:

- Why A is incorrect: Encryption at rest protects data stored on disk from being read if an attacker gains physical or file system access. It does not protect data in transit between services. The threat describes interception of network traffic, which is a transit threat addressed by TLS.
- Why B is incorrect: Mutual TLS (mTLS) where the database authenticates the client is a Spoofing countermeasure — it prevents an unauthorized service from impersonating the auth service to the database. This is a valid additional control, but the primary threat described (intercepting traffic to read plaintext) is Information Disclosure, not Spoofing.
- Why D is incorrect: `readOnlyRootFilesystem` is an Elevation of Privilege countermeasure that prevents a compromised container from writing malware to its filesystem. It has no effect on network traffic interception.

---

### Question 5

An organization stores its OWASP Threat Dragon threat model as a JSON file (`threat-model.json`) committed to the application's Git repository. A SOC 2 auditor asks for evidence that the threat model has been reviewed and approved and has not been modified without authorization. What specific Git artifact satisfies this evidence request?

- A) The `README.md` file, which should contain a summary of the threat model findings
- B) The commit history for `threat-model.json`, showing the specific commits that modified the file, the commit author identities, the PR review approvals, and the merge timestamps
- C) The GitHub Actions workflow run log, which shows that the application was deployed successfully after the threat model was created
- D) The Threat Dragon export PDF, which includes a timestamp of when the model was last edited in the Threat Dragon web interface

Correct Answer: B — Git commit history is auditable evidence that documents who made each change to the threat model, when, and through what review process. If branch protection rules require PR approvals before merging, the PR and its approved reviews are attached to the merge commit. This creates a chain of custody: change author → review → approval → merge → commit hash. A commit hash is cryptographically tied to the file content, so any unreviewed modification would create a new commit detectable in the history.

Distractor Analysis:

- Why A is incorrect: A README summary of threat findings is useful documentation but is not tamper-evident audit evidence. The README itself could be modified without the threat model being updated, or vice versa.
- Why C is incorrect: A deployment workflow run log shows that the application was deployed — it does not show that the threat model was reviewed. Deployment success has no logical relationship to threat model review.
- Why D is incorrect: The Threat Dragon PDF export timestamp shows when the export was generated, not when the threat model was reviewed and approved. The timestamp is also not cryptographically tied to the file content and could be regenerated to show any desired time.

---

### Question 6

During a threat modeling session for a CI/CD pipeline, the team identifies this threat: "A developer's GitHub account is compromised. The attacker pushes a commit that modifies the GitHub Actions workflow file to exfiltrate all repository secrets to an external server during the next pipeline run." Which STRIDE category is this, and which combination of controls best mitigates it?

- A) Elevation of Privilege — mitigated by requiring MFA on GitHub accounts and pinning GitHub Actions to commit SHAs
- B) Tampering — mitigated by requiring MFA on GitHub accounts and enforcing branch protection rules that require PR review before any changes to workflow files can be merged
- C) Spoofing — mitigated by enabling GitHub secret scanning and rotating secrets after each pipeline run
- D) Repudiation — mitigated by enabling GitHub audit logs and shipping them to a SIEM

Correct Answer: B — Modifying the workflow file to steal secrets is Tampering — the attacker modifies code (a workflow definition) that they should not be able to modify, violating integrity. The violated property is Integrity. The countermeasures address both the compromise vector (MFA prevents account takeover) and the pipeline protection (branch protection with required reviews means a modified workflow file cannot be merged without a reviewer approving the change, giving a human a chance to spot the malicious modification).

Distractor Analysis:

- Why A is incorrect: Elevation of Privilege involves gaining capabilities beyond authorization. The compromised developer account already has push access — the threat is using that access to tamper with code. MFA is a correct partial control, but pinning GitHub Actions addresses supply chain Spoofing (malicious actions), not workflow file tampering by an account holder.
- Why C is incorrect: Secret scanning detects secrets that are committed to the repository but does not prevent workflow modification. The threat here is modification of the workflow to exfiltrate secrets at runtime, not committing secrets directly. This is Tampering, not Spoofing.
- Why D is incorrect: Audit logs enable Repudiation controls (non-repudiation evidence), but the primary threat is a modification attack (Tampering). Audit logs detect and record tampering after the fact but do not prevent it. The question asks for the STRIDE category and best mitigation — prevention through branch protection is stronger than detection through audit logs.

---

### Question 7

What is the purpose of a trust boundary in a data flow diagram, and where do STRIDE threats most commonly occur?

- A) A trust boundary marks the perimeter of the organization's network; threats occur inside the perimeter where internal attackers operate
- B) A trust boundary separates zones with different security trust levels; data flows that cross trust boundaries require validation and are the most common locations for STRIDE threats because they represent transitions between trust contexts
- C) A trust boundary defines the scope of a single microservice; threats occur at microservice boundaries because each microservice has its own authentication system
- D) A trust boundary is a firewall rule set; threats occur at firewall rule boundaries because firewalls are the primary enforcement point

Correct Answer: B — A trust boundary separates security zones with different trust levels — for example, the public internet and the application DMZ, or the application services and the database tier. Data crossing a trust boundary transitions from one trust context to another. This transition is where authentication, authorization, input validation, and encryption controls are required. Without proper controls at trust boundaries, an attacker in a lower-trust zone can interact with components in a higher-trust zone without the required validation. STRIDE threats are most dense at trust boundaries because this is where trust assumptions are explicitly tested.

Distractor Analysis:

- Why A is incorrect: Trust boundaries are not limited to network perimeters. They exist within the network between services, between namespaces, between containers and their host, and between a CI/CD runner and the deployment target. Modern cloud-native systems have many internal trust boundaries.
- Why C is incorrect: A trust boundary is not synonymous with a microservice boundary. While microservice-to-microservice calls may cross trust boundaries, the trust boundary concept is broader — it describes security zones, not service decomposition.
- Why D is incorrect: Trust boundaries in a DFD are a logical modeling concept, not a reference to specific enforcement mechanisms like firewalls. A trust boundary in a DFD means "data crossing this line requires validation" — the actual enforcement mechanism could be a firewall, TLS mutual auth, RBAC, or application-level input validation.

---

### Question 8

A team has identified a Repudiation threat in their threat model: "An engineer with cluster-admin access deletes RBAC bindings during an incident, and there is no audit evidence of who performed the deletion." What is the correct countermeasure set that directly addresses Repudiation for this threat?

- A) Apply the PodSecurity `restricted` profile to all namespaces to prevent privileged containers
- B) Enable Kubernetes audit logging at the `RequestResponse` level for RBAC API groups, ship logs to an immutable store (CloudWatch Logs or Elasticsearch with S3 backup), and configure SIEM alerts for `delete` operations on `rolebindings` and `clusterrolebindings`
- C) Require that all engineers use OIDC authentication instead of static kubeconfig credentials
- D) Implement Falco rules that detect `kubectl delete` commands executed from within containers

Correct Answer: B — Repudiation threats require non-repudiation controls: evidence that specific actions were performed by specific actors at specific times, stored in a tamper-resistant location. Kubernetes audit logging at `RequestResponse` level records every API call with the authenticated user identity, the resource, the verb, and the request/response bodies. Shipping to an immutable store (CloudWatch with retention locks, or S3 with Object Lock) prevents an attacker from deleting the evidence. SIEM alerting surfaces the action in real time for incident response.

Distractor Analysis:

- Why A is incorrect: PodSecurity restricted profile addresses Elevation of Privilege in the container runtime. It has no effect on Kubernetes API actions taken by cluster administrators.
- Why C is incorrect: OIDC authentication is a Spoofing countermeasure — it ensures that the identity of the engineer is properly verified. It does not provide non-repudiation evidence of actions taken. Even with OIDC, if audit logging is not enabled, there is no record of what was done.
- Why D is incorrect: Falco rules detect process execution inside containers, not Kubernetes API calls made from outside the cluster or from a kubectl session. A cluster-admin deleting RBAC bindings via kubectl from their workstation would not be detected by container-level Falco rules. Kubernetes audit logs are the correct mechanism for API-level non-repudiation.

---

### Question 9

What is "threat model as code," and what specific practice implements it in a DevSecOps workflow?

- A) Threat model as code means writing threat descriptions as Python classes that are evaluated by OPA to produce STRIDE findings automatically
- B) Threat model as code means storing the threat model document (Threat Dragon JSON export) in a Git repository alongside the application source code, with changes reviewed through pull requests and the model updated as part of the definition of done for features that introduce new components
- C) Threat model as code means generating threat models automatically from infrastructure-as-code files (Terraform, CloudFormation) using static analysis tools
- D) Threat model as code means encoding compliance controls as Rego policies that are evaluated by OPA and labeled with STRIDE categories as metadata

Correct Answer: B — Threat model as code is the practice of treating the threat model document as a first-class artifact in the software delivery process — version-controlled, reviewed, and updated alongside code changes. Threat Dragon exports its models as JSON files, which can be committed to a Git repository. Changes to the threat model — adding new threats, marking threats as mitigated, adding new components — go through the same PR review process as code changes. This provides audit history, enforces review, and keeps the threat model synchronized with the architecture.

Distractor Analysis:

- Why A is incorrect: Threat model as code does not mean generating STRIDE findings programmatically through code evaluation. STRIDE is applied by humans during a design session, not by an automated parser. The "as code" refers to the storage and management discipline, not the generation method.
- Why C is incorrect: While some tools can identify misconfigurations in IaC files (Checkov, tfsec), this is IaC scanning — not threat modeling. Threat modeling requires understanding system architecture, trust boundaries, and attacker motivations, which cannot be fully automated from IaC files alone.
- Why D is incorrect: This describes Compliance as Code (Module 13) — using OPA and Rego to enforce security policies. While Compliance as Code and Threat Model as Code are related practices in a DevSecOps program, they are distinct. Threat Model as Code is about documenting and versioning architectural threat analysis, not writing enforcement policies.

---

### Question 10

A security engineer is performing a threat modeling session for a new feature that adds an external payment processing API integration. The data flow is: API Pod → Payment Gateway (external HTTPS endpoint) → Payment Gateway → API Pod (callback). The engineer asks: "What data flows across the trust boundary here, and what STRIDE threats apply?" Select the most complete and accurate analysis.

- A) Only Denial of Service applies because the external payment gateway could be unavailable and cause the API to fail
- B) Spoofing (is the payment gateway endpoint authentic?), Tampering (can the callback data be modified in transit?), and Information Disclosure (are payment card details protected in transit?) all apply; countermeasures include TLS with certificate pinning, callback signature verification (HMAC or webhook secret), and PCI-DSS Requirement 4 TLS controls
- C) Only Tampering applies because the payment gateway is an external system that could modify the response data
- D) Repudiation and Elevation of Privilege do not apply to external API integrations, so only Information Disclosure is relevant

Correct Answer: B — A data flow crossing an external trust boundary (API Pod → Internet → Payment Gateway) has multiple applicable STRIDE threats. Spoofing: is the HTTPS endpoint the legitimate payment gateway or a man-in-the-middle? Countermeasure: TLS with certificate validation, certificate pinning for high-value integrations. Tampering: can a network attacker modify the payment callback data (amounts, status) before it reaches the API? Countermeasure: webhook signature verification using HMAC secrets provided by the payment gateway. Information Disclosure: payment card data transmitted in requests must be protected. Countermeasure: TLS (PCI-DSS Requirement 4 mandates TLS 1.2+ for cardholder data in transit). Multiple STRIDE categories typically apply at any trust boundary crossing.

Distractor Analysis:

- Why A is incorrect: Availability (DoS) is a valid concern for an external dependency — rate limiting, circuit breakers, and timeout handling address it. But focusing only on DoS misses the higher-severity threats: Spoofing (MITM impersonating the payment gateway) and Tampering (callback manipulation to change payment amounts) are Critical threats for a payment integration.
- Why C is incorrect: Limiting the analysis to Tampering misses the Spoofing threat (is the endpoint authentic?) and the Information Disclosure threat (payment card data in transit). Incomplete STRIDE analysis leaves Critical threats unidentified.
- Why D is incorrect: Repudiation does apply — if a payment transaction is disputed and the callback log is unavailable or mutable, there is no evidence of whether payment was received. Elevation of Privilege may apply if callback data is used to grant access or change user permissions. Eliminating STRIDE categories based on integration type rather than systematic analysis is the failure mode that STRIDE is designed to prevent.

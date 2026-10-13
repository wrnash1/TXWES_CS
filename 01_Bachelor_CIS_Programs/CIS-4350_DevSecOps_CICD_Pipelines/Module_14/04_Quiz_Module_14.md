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

---

### Question 11

A threat model for a CI/CD pipeline identifies the following threat: "An attacker who compromises a developer's machine submits a malicious pull request. The PR passes automated checks because no human reviews the security-sensitive changes." Which STRIDE category and corresponding control best address this threat?

- A) Spoofing — require MFA on GitHub accounts so the attacker cannot impersonate the developer
- B) Tampering — require CODEOWNERS review for security-sensitive paths so a human approves changes before merge
- C) Elevation of Privilege — add a Checkov IaC scan gate to the PR pipeline
- D) Denial of Service — enable GitHub Actions concurrency limits to prevent pipeline flooding

Correct Answer: B — The threat is that pipeline automation alone approves malicious code changes. Tampering describes unauthorized modification of code or data. The mitigation is a CODEOWNERS file requiring human review of security-sensitive paths (e.g., Terraform configurations, GitHub Actions workflow files, Dockerfile changes). Automation gates detect known vulnerability patterns, but CODEOWNERS ensures a security engineer reviews structural and logic changes that scanners may miss.

Distractor Analysis:

- Why A is incorrect: MFA addresses account takeover (Spoofing — impersonation), but the threat described assumes the attacker has already compromised the developer's machine, potentially including session tokens. MFA alone does not prevent a PR submitted from an already-authenticated compromised session.
- Why C is incorrect: Checkov IaC scanning gates catch misconfigurations, but a sophisticated malicious change (such as adding a secret exfiltration step to a GitHub Actions workflow) may not be flagged by a static analysis tool. Human review via CODEOWNERS is the required mitigation for logic-level threats.
- Why D is incorrect: Concurrency limits address resource exhaustion and DoS on the pipeline infrastructure, not the submission of malicious code by a compromised contributor.

---

### Question 12

In OWASP Threat Dragon, a threat model is exported as a JSON file. A team commits this file to their application's Git repository. What is the DevSecOps rationale for version-controlling the threat model artifact?

- A) The JSON file is required by GitHub Security to enable Code Scanning
- B) Version-controlling the threat model creates a historical record of the system's threat landscape, enables diff review when architecture changes, and ensures the threat model is updated alongside code changes rather than stored in a disconnected document repository
- C) GitHub automatically scans committed Threat Dragon JSON files and opens security issues for each identified threat
- D) Threat model JSON files are required by SOC 2 auditors as evidence of the organization's security posture; they must be in version control to be admissible

Correct Answer: B — Treating the threat model as a code artifact (Threat Model as Code) enables version-controlled review of security design changes. When a developer adds a new external API integration, a PR that modifies the threat model JSON alongside the code changes allows reviewers to assess whether new trust boundaries and threats have been identified and mitigated. This is the DFD-alongside-code principle in DevSecOps.

Distractor Analysis:

- Why A is incorrect: GitHub Code Scanning analyzes source code for vulnerabilities using SARIF-producing tools. Threat Dragon JSON files are not a required input for GitHub Code Scanning.
- Why C is incorrect: GitHub does not automatically analyze Threat Dragon JSON files. They must be opened in the Threat Dragon application for visualization and editing.
- Why D is incorrect: While SOC 2 auditors may accept version-controlled threat model documents as security design evidence, this is not the primary rationale. The DevSecOps rationale is the shift-left benefit of reviewing threat model changes alongside code changes.

---

### Question 13

A DFD for a microservices application shows a trust boundary between the `Order Service` and the `Payment Service`. Both services run in the same Kubernetes namespace. A security engineer argues that no trust boundary should exist between two services in the same namespace. Is this argument correct?

- A) Yes — Kubernetes namespace boundaries are equivalent to trust boundaries; services in the same namespace are mutually trusted by design
- B) No — trust boundaries in a DFD reflect the level of trust between communicating components, not their network topology. Services in the same namespace can have different trust levels if they process data of different sensitivity or are owned by different teams
- C) Yes — trust boundaries only apply at external network perimeters (internet-facing load balancers); internal service-to-service communication is always trusted
- D) No — every service-to-service data flow must have a trust boundary regardless of network location, because STRIDE requires analyzing all data flows

Correct Answer: B — Trust boundaries are semantic, not topological. A payment service processing cardholder data has higher sensitivity than an order service. Even within the same namespace, the payment service should require authenticated, authorized service-to-service communication (mutual TLS, service account RBAC, NetworkPolicy restrictions). The DFD trust boundary reflects the security control requirement at that interface, not a claim that the two services are on different networks.

Distractor Analysis:

- Why A is incorrect: Kubernetes namespaces are administrative boundaries, not security isolation boundaries. By default, pods in the same namespace can communicate freely unless a NetworkPolicy restricts this. Namespaces do not enforce mutual authentication between services.
- Why C is incorrect: The principle of Zero Trust explicitly rejects "trusted internal network" assumptions. Internal service-to-service communication that processes sensitive data requires authentication, authorization, and encryption regardless of network location.
- Why D is incorrect: While systematic STRIDE analysis of all data flows is valuable, not every flow requires an explicit trust boundary in the DFD. Trust boundaries mark the points where the trust level changes or where special scrutiny is required. Marking every single data flow as a trust boundary would make the DFD unreadable without adding analysis value.

---

### Question 14

During sprint planning, a developer proposes adding a feature that stores user authentication tokens in a new Redis cache shared between the API service and the session management service. Under the sprint-cadence threat modeling approach, what is the correct response?

- A) Log the change in the backlog and schedule a quarterly threat model review to assess the new Redis component
- B) Require the developer to conduct a brief threat modeling exercise for the new data store before the story is accepted into the sprint, identifying at least the Information Disclosure and Elevation of Privilege threats and their mitigations
- C) Treat the Redis cache as a purely technical implementation detail — threat modeling is only required for user-facing features
- D) Conduct a full PASTA-based threat model spanning the entire application before the sprint begins

Correct Answer: B — The introduction of a new shared data store for sensitive credentials is a DFD change that introduces at least one new trust boundary (API → Redis, Session Service → Redis) and a new data store element. Under sprint-cadence threat modeling, any change that modifies the DFD (new process, data store, trust boundary, or external entity) triggers a threat modeling activity for that change before implementation begins. A lightweight STRIDE analysis of the new component at design time takes 30 minutes and prevents Security vulnerabilities from being built into the sprint.

Distractor Analysis:

- Why A is incorrect: Deferring to a quarterly review means the Redis cache will be implemented and deployed before any threat analysis. By that point, fixing identified threats requires rework. This is the waterfall security model that DevSecOps is designed to replace.
- Why C is incorrect: Backend data stores — especially those holding authentication tokens — are high-value targets. Threat modeling is not limited to user-facing features. A Redis cache holding session tokens is arguably more sensitive than most user interfaces.
- Why D is incorrect: A full PASTA analysis for the entire application is appropriate for a new system or major redesign. For a sprint-level change (adding a cache component), a lightweight targeted STRIDE analysis is proportionate and actionable. Full threat model exercises for every sprint change would be impractical and would not be adopted.

---

### Question 15

A threat model identifies the threat: "A developer pushes a GitHub Actions workflow file that exfiltrates all `secrets.*` values to an external endpoint." The CI/CD team proposes the following mitigation: "Use SHA-pinned Actions." Does SHA pinning address this specific threat?

- A) Yes — SHA pinning prevents developers from modifying workflow files, which prevents the exfiltration threat
- B) No — SHA pinning prevents supply chain attacks where a third-party Action's tag is reassigned to malicious code. It does not prevent a developer from writing a malicious first-party workflow step that directly exfiltrates secrets
- C) Yes — SHA pinning enables GitHub to detect and block workflows that attempt to access secrets without authorization
- D) No — the correct mitigation is to use environment protection rules that require reviewer approval before secrets are made available to the workflow

Correct Answer: B — SHA pinning (`uses: actions/checkout@<sha>`) prevents an attacker from compromising the upstream Action repository and reassigning a tag to malicious code. It addresses supply chain threats to third-party Actions. However, it does not prevent a malicious first-party workflow step written directly in the `.yml` file from exfiltrating secrets — the developer controls the workflow content directly and can write any step they choose. The threat described is an insider or compromised-developer threat, not a supply chain threat.

Distractor Analysis:

- Why A is incorrect: SHA pinning applies to `uses:` references to external Actions, not to the workflow file itself. A developer with write access to the repository can still modify the workflow YAML file and add malicious steps.
- Why C is incorrect: GitHub does not scan workflow content for malicious secret access patterns by default. GitHub's secret protection features focus on preventing secrets from appearing in logs, not on detecting exfiltration attempts in workflow logic.
- Why D is incorrect: Environment protection rules are a valuable complementary control — they require reviewer approval before secrets for production environments are available to a workflow run. But this control can be bypassed if a reviewer is also the attacker, or if the workflow can target a non-protected environment. CODEOWNERS review of workflow file changes is the more direct mitigation for this threat.

---

### Question 16

The STRIDE threat "Repudiation" is often underestimated in cloud-native systems. Which combination of CI/CD pipeline events creates an unmitigated Repudiation risk?

- A) A GitHub Actions workflow that does not require code review before merging to main
- B) An EKS cluster where `kubectl apply` commands are executed directly by engineers without Kubernetes audit logging enabled, and where the CI/CD pipeline does not log which commit triggered each deployment
- C) A container image that is not signed with Cosign, making it impossible to verify who built the image
- D) A Terraform configuration without remote state backend, making it impossible to track infrastructure history

Correct Answer: B — Repudiation risk exists when an actor can deny having performed an action because no reliable audit record exists. If engineers can execute `kubectl apply` without audit logging, there is no record of who changed what in the cluster. If the pipeline does not log which git commit triggered each deployment, there is no chain of custody from code change to deployed artifact. Both gaps together make it impossible to reconstruct what happened during an incident.

Distractor Analysis:

- Why A is incorrect: Lacking code review creates a Tampering risk (unauthorized changes can be merged) but does not directly create a Repudiation risk. GitHub maintains immutable commit and PR history regardless of whether a review was required.
- Why C is incorrect: Unsigned images create a Tampering risk (no verification that the image was not modified after build) and a Spoofing risk (no verification of the image's origin). This is not primarily a Repudiation risk unless the signing event is also the audit record of who built the image.
- Why D is incorrect: Local Terraform state creates operational risks (concurrency conflicts, state loss) and Information Disclosure risk (state files in version control). The primary threat category is not Repudiation — Terraform's plan and apply outputs still exist in pipeline logs.

---

### Question 17

A threat model assigns severity using the DREAD scoring model. The threat "An attacker exploits an unpatched RCE vulnerability in the public-facing API container to achieve remote code execution" is scored as: Damage=10, Reproducibility=8, Exploitability=9, Affected Users=10, Discoverability=7. What is the DREAD score and severity tier?

- A) Score: 44, Severity: Medium
- B) Score: 8.8, Severity: High
- C) Score: 44, Severity: Critical
- D) Score: 8.8, Severity: Critical

Correct Answer: B — DREAD scores each dimension 1–10 and averages them: (10+8+9+10+7)/5 = 44/5 = 8.8. A score of 8.8 falls in the High severity tier (7.0–8.9) by the standard DREAD scale. A score of 9.0 or above would be Critical. Some organizations use >7.5 as Critical — the exact thresholds are organization-defined.

Distractor Analysis:

- Why A is incorrect: The sum 44 is intermediate — DREAD uses the average of the five dimensions, not their sum. The average is 8.8, which is in the High range under standard DREAD scoring.
- Why C is incorrect: The score is correct as an intermediate sum (44) but DREAD produces an average (8.8), not a sum. Reporting the sum as the score is an incorrect application of the DREAD model.
- Why D is incorrect: The score 8.8 is correct, but the severity tier at 8.8 is High, not Critical. Critical typically requires a score of 9.0+ on the standard DREAD scale. The exact threshold is configurable, but 8.8 is at the high end of High.

---

### Question 18

A security engineer wants to formally document that the threat "Unencrypted data in transit between microservices" has been accepted as a risk by the business for internal service-to-service communication that uses a non-public internal network. What is the correct documentation artifact and approval process?

- A) Create a `.trivyignore` entry for the CVE associated with unencrypted transport
- B) Add `// nosec` comments to the service code at the locations where unencrypted connections are established
- C) Create a risk acceptance register entry documenting the threat ID, business justification, named risk owner, compensating control (network-level encryption via VPN/private subnet), and expiry date for review
- D) Close the threat in Threat Dragon with status "Not Applicable" without additional documentation

Correct Answer: C — Risk acceptance requires a formal record: the threat being accepted, the business justification for acceptance over remediation, the compensating control that reduces (but does not eliminate) the risk, a named risk owner who is accountable, and an expiry date that triggers re-evaluation. This satisfies SOC 2 CC3.2 (risk assessment process) and audit requirements. The register entry transforms an informal decision into a traceable governance artifact.

Distractor Analysis:

- Why A is incorrect: `.trivyignore` suppresses container CVE findings, not threat model entries. This is the wrong tool for a threat model risk acceptance decision.
- Why B is incorrect: `// nosec` comments suppress SAST findings in source code. They are not a risk acceptance mechanism for architectural threats identified in a threat model.
- Why D is incorrect: Closing a threat as "Not Applicable" without documentation provides no evidence of deliberate risk acceptance. An auditor would see an unmitigated threat with no justification, which fails the governance requirement. The status change must be accompanied by documented reasoning.

---

### Question 19

A team's threat model for their Kubernetes deployment identifies the threat: "An attacker who obtains a Kubernetes service account token with `cluster-admin` binding can perform any operation in the cluster." The team mitigates this by implementing least-privilege RBAC for all service accounts. How should this mitigation be validated in the CI/CD pipeline?

- A) Run `kubectl auth can-i --list` in the pipeline to enumerate all permissions of all service accounts and fail the build if any service account has cluster-admin binding
- B) Scan RBAC manifests with Checkov (`CKV_K8S_42` — do not bind service accounts to cluster-admin) as part of the Kubernetes manifest scan job in the PR pipeline
- C) Use Falco to detect cluster-admin usage in production and alert the security team if a service account attempts a restricted operation
- D) Require manual review of all RBAC manifests before deployment via a CODEOWNERS rule on the `rbac/` directory

Correct Answer: B — Checkov provides automated validation of RBAC manifests in CI, specifically checking that service accounts are not bound to `cluster-admin`. This converts a threat model finding into a pipeline gate. When a developer commits RBAC changes, the pipeline automatically validates the mitigation is correctly implemented before the manifest can be merged and applied to the cluster. This is the "threat modeling to pipeline control" traceability the module describes.

Distractor Analysis:

- Why A is incorrect: `kubectl auth can-i --list` requires API server access from the pipeline runner, which would require granting the CI runner cluster credentials — creating a new privilege risk. It also requires a running cluster to be available, adding pipeline dependencies.
- Why C is incorrect: Falco runtime detection is a valid detective control for post-compromise monitoring, not a preventive validation of the mitigation. Falco would detect misuse after deployment, not validate that the RBAC manifests are correctly scoped before deployment.
- Why D is incorrect: CODEOWNERS review is a valid additional control but does not automatically validate the RBAC content. A reviewer could miss a cluster-admin binding in a complex manifest. Automated Checkov scanning combined with CODEOWNERS provides defense in depth, but Checkov alone provides the automated validation of the specific threat model mitigation.

---

### Question 20

A threat model for a multi-tenant SaaS application identifies that "Tenant A can access Tenant B's data if the data isolation logic in the API service has a bug." Which STRIDE category covers this threat and what type of pipeline control best validates the mitigation?

- A) Spoofing — add strong authentication; validate with penetration testing
- B) Elevation of Privilege — add row-level security to the database; validate with DAST authenticated scan that verifies tenant isolation across user sessions
- C) Information Disclosure — add authorization checks in the API; validate with unit tests and integration tests that verify data isolation between tenants
- D) Tampering — add input validation; validate with SAST scanning for injection vulnerabilities

Correct Answer: C — Cross-tenant data access is an Information Disclosure threat — sensitive data belonging to one tenant is disclosed to another. The root cause is a logic error in the authorization layer (incorrect tenant filtering in API queries). The primary mitigation is application-level authorization logic, and the correct validation is automated tests (unit and integration) that specifically verify tenant isolation. DAST can supplement but cannot replace tests that exercise data isolation logic at the application layer.

Distractor Analysis:

- Why A is incorrect: Spoofing involves impersonating a legitimate user — Tenant A claiming to be Tenant B. The threat described assumes Tenant A is legitimately authenticated but can access Tenant B's data due to a bug, not impersonation. Strong authentication does not prevent bugs in tenant filtering logic.
- Why B is incorrect: Elevation of Privilege involves gaining capabilities beyond authorization. Row-level security at the database layer is a valid defense-in-depth control for this threat, but it addresses the same Information Disclosure risk rather than a separate category. DAST authenticated scanning does test for tenant isolation but cannot cover all data access paths that unit tests can exercise.
- Why D is incorrect: Tampering involves unauthorized modification of data, not unauthorized reading of data. Input validation and SAST address injection vulnerabilities, not application-level tenant isolation logic bugs.

---

Quiz — Module 14 | CIS-4350 | Texas Wesleyan University | Professor Nash

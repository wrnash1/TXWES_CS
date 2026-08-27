# Quiz: Module 09 - Secrets Management: HashiCorp Vault and AWS Secrets Manager

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

A developer commits a database password to a public GitHub repository, realizes the mistake immediately, and removes it in the next commit. What is the correct security response?

- A) No action is needed because the secret is no longer in the current version of the repository
- B) Rotate the exposed credential immediately, then remove it from Git history using `git filter-repo` or BFG Repo-Cleaner, and audit for unauthorized use
- C) Delete the repository and create a new one without the secret in its history
- D) Make the repository private, which prevents anyone from reading the Git history

#### Q1 Correct Answer

B — The credential must be rotated immediately because anyone who observed the repository at any point during its exposure may have copied the secret. Removing a secret from a repository does not remove it from Git history — `git log` on any clone still shows it. `git filter-repo` or BFG Repo-Cleaner rewrites history to remove the secret. Audit logs should be checked for unauthorized use during the exposure window.

#### Q1 Distractor Analysis

- *Why A is incorrect:* The secret is permanently in Git history. Every clone of the repository, every cached view on GitHub, and any automated scraper that may have indexed the repository during the exposure window retains the secret.
- *Why C is incorrect:* Deleting the repository does not revoke the credential. Anyone who cloned the repository before deletion retains the secret in their local Git history. Rotation is the essential first step.
- *Why D is incorrect:* Making the repository private prevents future exposure but does not address any access that occurred during the period the repository was public. Rotation is still required.

---

### Question 2

Why must a GitHub Actions secrets scanning job use `fetch-depth: 0` in the `actions/checkout` step?

- A) `fetch-depth: 0` enables scanning of files in subdirectories, which the default shallow clone excludes
- B) The default shallow clone only retrieves the most recent commit; `fetch-depth: 0` retrieves the full Git history so secrets scanning can detect credentials committed in any prior commit
- C) `fetch-depth: 0` is required for Gitleaks to authenticate to GitHub and access private repository contents
- D) The default checkout downloads only staged changes; `fetch-depth: 0` ensures the working tree is fully populated

#### Q2 Correct Answer

B — By default, `actions/checkout` performs a shallow clone with `fetch-depth: 1`, retrieving only the most recent commit to minimize clone time. Gitleaks scans Git commit objects, not just the working tree. Without the full history, Gitleaks cannot detect secrets that were committed in earlier commits, even if those secrets remain in the repository history.

#### Q2 Distractor Analysis

- *Why A is incorrect:* `fetch-depth` controls the number of commits retrieved, not the directory depth of files included. Subdirectory files are included in any checkout regardless of fetch depth.
- *Why C is incorrect:* Gitleaks authentication to GitHub uses the `GITHUB_TOKEN` environment variable, not the `fetch-depth` parameter. These are independent configuration concerns.
- *Why D is incorrect:* The default `actions/checkout` populates the working tree completely. `fetch-depth` controls the depth of commit history fetched, not the completeness of the working tree.

---

### Question 3

Which HashiCorp Vault authentication method is designed for CI/CD pipeline authentication?

- A) GitHub auth — the pipeline uses a GitHub personal access token to authenticate to Vault
- B) AppRole — the pipeline authenticates using a role ID and secret ID to receive a Vault token
- C) Kubernetes auth — the pipeline authenticates using a Kubernetes service account JWT
- D) LDAP auth — the pipeline authenticates using a service account in the corporate directory

#### Q3 Correct Answer

B — AppRole is Vault's machine-to-machine authentication method designed for CI/CD pipelines and automated systems. The pipeline is provisioned with a role ID (a non-secret identifier) and a secret ID (a secret that can be rotated). Together, these authenticate the pipeline to Vault and return a Vault token scoped to a specific policy.

#### Q3 Distractor Analysis

- *Why A is incorrect:* GitHub auth is typically used for developer CLI access to Vault using personal access tokens, not for automated pipeline authentication. Personal access tokens are user-bound and rotate with user account changes.
- *Why C is incorrect:* Kubernetes auth is designed for pods running inside a Kubernetes cluster, where the pod's service account JWT provides identity. It is the correct choice for Kubernetes-hosted workloads but not for GitHub Actions runners.
- *Why D is incorrect:* LDAP auth is for human user authentication against a corporate directory. Service accounts may use LDAP auth in some configurations, but AppRole is the purpose-built choice for automated pipeline authentication.

---

### Question 4

What are dynamic secrets in HashiCorp Vault, and what security advantage do they provide over static secrets?

- A) Dynamic secrets are secrets that are automatically synchronized across multiple cloud regions, providing high availability
- B) Dynamic secrets are credentials generated on demand by Vault, are unique per request, and expire automatically after a configurable lease period — bounding the exposure window if a credential is leaked
- C) Dynamic secrets are secrets that are encrypted with a rotating key, making them unreadable without the current decryption key
- D) Dynamic secrets are secrets stored in environment variables that are regenerated on each container restart

#### Q4 Correct Answer

B — Vault's database secret engine (and other dynamic secret engines) creates a unique, time-limited credential each time a client requests access. If the credential is leaked, it expires automatically at the end of its lease. There is no persistent credential to steal — each deployment gets a different credential with a bounded lifetime.

#### Q4 Distractor Analysis

- *Why A is incorrect:* Multi-region synchronization describes a high-availability configuration of Vault's storage backend, not dynamic secrets. Dynamic secrets refer to on-demand generation of unique credentials.
- *Why C is incorrect:* Encryption with a rotating key describes key management, not dynamic secrets. Dynamic secrets are about generating unique credentials per request, not about the encryption of stored secrets.
- *Why D is incorrect:* Secrets regenerated on container restart are still static — they persist until the container restarts. Dynamic secrets are generated on demand by Vault's secret engines and expire based on a Vault-controlled lease, independent of container lifecycle.

---

### Question 5

A developer writes the following Dockerfile to authenticate to a private package registry during the build:

```dockerfile
FROM python:3.11-slim
ARG REGISTRY_TOKEN
RUN pip install --extra-index-url https://user:${REGISTRY_TOKEN}@registry.internal.example.com mypackage
```

What is the security problem with this approach, even if the final image does not contain any file with the token?

- A) The `ARG` instruction writes the token to a temporary file that can be read by any user in the container
- B) Each `RUN` instruction creates an image layer. The `REGISTRY_TOKEN` value is embedded in the layer metadata and recoverable via `docker history`, even though no file containing the token exists in the final filesystem
- C) The `ARG` instruction transmits the token value to Docker Hub during the build push phase
- D) The token is automatically printed to `docker build` standard output, which is captured in CI pipeline logs

#### Q5 Correct Answer

B — Docker images consist of layers, each corresponding to a `RUN` instruction. The full command string, including the `${REGISTRY_TOKEN}` value interpolated at build time, is stored in the layer metadata. `docker history --no-trunc` reveals the complete command. This data is present in the image manifest and recoverable by anyone with access to the image, including from a container registry.

#### Q5 Distractor Analysis

- *Why A is incorrect:* `ARG` values are not written to temporary files. They exist as environment variables in the build context. The exposure is in the image layer metadata, not a runtime file.
- *Why C is incorrect:* Docker build args are not transmitted to Docker Hub during push. The exposure is in the local image layers that are pushed as part of the image, not in a separate transmission during build.
- *Why D is incorrect:* Docker build output shows step progress but does not automatically expand and print `ARG` values. The exposure is in the image layer metadata, not in standard output.

---

### Question 6

What is OIDC federation in the context of GitHub Actions deploying to AWS, and what specific risk does it eliminate?

- A) OIDC federation allows GitHub Actions to share secrets with AWS Secrets Manager using an encrypted tunnel, eliminating man-in-the-middle risk
- B) OIDC federation creates a trust relationship between GitHub and AWS IAM. The pipeline authenticates using a short-lived JWT from GitHub and receives temporary AWS credentials, eliminating the need to store long-lived AWS access keys in GitHub Secrets
- C) OIDC federation synchronizes GitHub repository permissions with AWS IAM roles, eliminating manual IAM role management
- D) OIDC federation enables AWS Lambda to directly invoke GitHub Actions workflows, eliminating polling-based CI triggers

#### Q6 Correct Answer

B — With OIDC federation, an IAM role is configured to trust GitHub's OIDC provider. When the pipeline runs, GitHub issues a short-lived JWT asserting the identity of the workflow (repository, branch, environment). AWS IAM verifies the JWT signature against GitHub's public key and returns temporary credentials (an assumed-role session). No long-lived AWS access key or secret key needs to be stored in GitHub Secrets.

#### Q6 Distractor Analysis

- *Why A is incorrect:* OIDC federation is an authentication mechanism, not an encryption tunnel for secret synchronization. The specific risk eliminated is the storage of long-lived credentials, not man-in-the-middle attacks.
- *Why C is incorrect:* OIDC federation does not synchronize permission policies. IAM roles must still be manually configured with the appropriate permissions. The federation solves the authentication problem, not the authorization configuration problem.
- *Why D is incorrect:* OIDC federation is a GitHub-to-AWS authentication mechanism. It has nothing to do with Lambda invoking GitHub Actions workflows.

---

### Question 7

An organization stores their production database password in GitHub Secrets and injects it as an environment variable in their deployment pipeline. The security team requests a migration to HashiCorp Vault. What are two specific security capabilities Vault provides that GitHub Secrets cannot?

- A) Vault supports more secret types than GitHub Secrets, and Vault can be used from any operating system
- B) Vault provides per-access audit logging showing which pipeline run retrieved which secret, and Vault supports dynamic secrets with automatic expiry — capabilities GitHub Secrets does not provide
- C) Vault secrets are longer than GitHub Secrets and therefore more secure, and Vault can be accessed without internet connectivity
- D) Vault integrates with GitHub Actions using official GitHub-supported actions, and Vault encrypts secrets using AES-256

#### Q7 Correct Answer

B — GitHub Secrets stores static encrypted values with no per-read audit trail — you cannot see which pipeline run accessed the secret. Vault logs every secret read to its audit log (timestamp, accessor, path, operation), enabling security investigations. Vault's dynamic secrets capability generates unique credentials per request with automatic expiry, which GitHub Secrets cannot do.

#### Q7 Distractor Analysis

- *Why A is incorrect:* Both GitHub Secrets and Vault support arbitrary string secrets and are accessible from any OS. These are not meaningful security distinctions.
- *Why C is incorrect:* Secret length is not a security differentiator here. Access to Vault without internet is about deployment architecture, not a security capability advantage.
- *Why D is incorrect:* Both GitHub Secrets and Vault encrypt stored secrets. AES-256 usage alone is not a meaningful differentiation. The security advantages of Vault are audit logging and dynamic secrets.

---

### Question 8

A GitHub Actions pipeline injects a database password from GitHub Secrets into a deployment step. The developer adds a debugging step to troubleshoot a connection failure:

```yaml
- name: Debug environment
  run: env
```

What security risk does this step introduce, and how does GitHub attempt to mitigate it?

- A) The `env` command outputs all environment variables to pipeline logs. GitHub attempts to mitigate this by masking the values of secrets injected from GitHub Secrets in log output
- B) The `env` command creates a new environment variable file that persists on the runner and may be read by subsequent jobs
- C) The `env` command sends environment variable names to GitHub's telemetry system for monitoring
- D) The `env` command disables secret injection for the remainder of the job to prevent further exposure

#### Q8 Correct Answer

A — When GitHub Secrets are injected as environment variables, GitHub automatically masks their values in pipeline log output — any log line containing the secret value is replaced with `***`. This provides a layer of protection against accidental logging. However, the masking is pattern-based and can be bypassed if the secret is base64-encoded, split across log lines, or otherwise transformed before logging.

#### Q8 Distractor Analysis

- *Why B is incorrect:* The `env` command prints to standard output, not to a file. The output is captured in the pipeline log, not written to a persistent file on the runner.
- *Why C is incorrect:* GitHub does not transmit environment variable names to a telemetry system via the `env` command. The risk is log exposure, not telemetry exposure.
- *Why D is incorrect:* The `env` command is a standard shell utility. It does not interact with GitHub Actions' secret injection mechanism or disable it.

---

### Question 9

Which of the following correctly describes the recommended pattern for using secrets during a Docker image build without exposing them in any image layer?

- A) Store the secret in a `.env` file and add `.env` to `.dockerignore`, which prevents the file from being copied into the image
- B) Pass the secret as a `--build-arg` and delete it in the same `RUN` instruction using `unset`
- C) Use BuildKit's `--mount=type=secret` to provide the secret to a `RUN` instruction. The secret is available during the build step but is not stored in any layer
- D) Use a multi-stage build and only copy the final compiled artifact to the production stage, relying on stage isolation to prevent credential exposure

#### Q9 Correct Answer

C — BuildKit's `--mount=type=secret` syntax mounts the secret as a tmpfs file available only during the execution of that specific `RUN` instruction. It is not recorded in any layer metadata. After the `RUN` instruction completes, the secret is no longer accessible in the image.

#### Q9 Distractor Analysis

- *Why A is incorrect:* A `.env` file in `.dockerignore` prevents the file from being `COPY`'d into the image, but it does not address the case where a secret needs to be used during a `RUN` step. The secret would need to be passed another way, and that passing mechanism may still expose it.
- *Why B is incorrect:* `unset` in a `RUN` instruction affects the running shell's environment, but the full command string — including the `--build-arg` value interpolated into the command — is already stored in the layer metadata before `unset` executes. Layer metadata records the command as written, not the state after execution.
- *Why D is incorrect:* Multi-stage builds prevent artifacts from one stage reaching the final image, but they do not prevent layer metadata from intermediate stages being stored in the local Docker daemon's layer cache. An intermediate stage that used a `--build-arg` secret would still expose it in that stage's layer metadata.

---

### Question 10

A pipeline uses AWS Secrets Manager to retrieve database credentials at deployment time using OIDC federation. The IAM role trusted by the GitHub OIDC provider grants `secretsmanager:GetSecretValue` on `arn:aws:secretsmanager:us-east-1:123456789012:secret:myapp/production/*`. A developer proposes expanding the IAM role to also grant `secretsmanager:GetSecretValue` on `*` to simplify future onboarding. What DevSecOps principle does this violate, and what specific risk does it introduce?

- A) It violates the principle of defense in depth; the risk is that Secrets Manager becomes unavailable if the policy is too broad
- B) It violates the principle of least privilege; the risk is that a compromised pipeline can retrieve any secret in the AWS account, including secrets belonging to other applications or environments
- C) It violates the principle of separation of duties; the risk is that developers and operations staff share the same secret access permissions
- D) It violates the principle of immutable infrastructure; the risk is that the IAM policy cannot be rolled back if the broader permissions cause a compliance failure

#### Q10 Correct Answer

B — Least privilege requires granting only the permissions needed for the specific task. The `*` resource grant means a compromised pipeline job can retrieve every secret in the AWS account — production database passwords for other applications, third-party API keys, encryption keys. The blast radius of a pipeline compromise expands from "this application's secrets" to "every secret in the account."

#### Q10 Distractor Analysis

- *Why A is incorrect:* Broad IAM policies do not cause service unavailability. Defense in depth is about layering controls; the violated principle here is least privilege.
- *Why C is incorrect:* Separation of duties concerns the separation of roles between individuals (developer, operator, auditor). The described change is about resource scope in an IAM policy, not role separation between people.
- *Why D is incorrect:* Immutable infrastructure is about replacing infrastructure instead of modifying it in place. IAM policy rollback is operationally straightforward. The primary concern here is the security risk from overly broad permissions.

---

### Question 11 (5 points)

HashiCorp Vault's `kv` secrets engine has two versions: KV v1 and KV v2. Which capability does KV v2 provide that KV v1 does not, and why is it important for security?

- A) KV v2 supports dynamic secrets; KV v1 only stores static values
- B) KV v2 maintains a versioned history of secret values, enabling rollback if a secret is accidentally overwritten or corrupted
- C) KV v2 encrypts secrets with customer-managed keys; KV v1 uses Vault's internal encryption
- D) KV v2 supports OIDC authentication; KV v1 requires AppRole

#### Q11 Correct Answer

B — KV v2 stores up to a configurable number of previous secret versions. If an operator accidentally overwrites a production credential, the previous value can be retrieved and restored. This also creates an audit trail of when secret values changed, which supports incident investigation.

#### Q11 Distractor Analysis

- *Why A is incorrect:* Dynamic secrets are generated by dedicated secret engines (database, AWS, etc.) — they are not a KV v2 feature. Both KV v1 and KV v2 store static values.
- *Why C is incorrect:* Both KV v1 and KV v2 use Vault's internal encryption (backed by the configured storage backend). Customer-managed key options are a Vault Enterprise feature unrelated to the KV version.
- *Why D is incorrect:* Authentication methods (AppRole, OIDC, Kubernetes) are configured at the Vault auth path level, not at the secret engine level. Both KV versions support all authentication methods.

---

### Question 12 (5 points)

A GitHub Actions workflow stores a Vault token as a GitHub Secret and uses it to fetch database credentials at runtime. A security engineer points out this is "static secret to retrieve a static secret." What is the more secure pattern?

- A) Store the database credentials directly in GitHub Secrets, eliminating the Vault lookup step
- B) Use Vault's AppRole auth with a short-lived secret ID generated per pipeline run, or use OIDC-based JWT auth to Vault so no long-lived Vault token is stored anywhere
- C) Encrypt the Vault token with GPG before storing it in GitHub Secrets
- D) Store the Vault token in the repository's `.env.example` file and add it to `.gitignore`

#### Q12 Correct Answer

B — Vault supports JWT authentication where GitHub's OIDC token is exchanged for a Vault token. No long-lived Vault token or AppRole secret ID needs to be stored in GitHub Secrets. The Vault token issued is scoped to the pipeline's policy and expires with a short TTL after the job completes.

#### Q12 Distractor Analysis

- *Why A is incorrect:* Storing database credentials directly in GitHub Secrets reintroduces the original problem — a long-lived, static secret with no audit trail and no automatic rotation.
- *Why C is incorrect:* Encrypting the Vault token with GPG requires storing the GPG private key somewhere — shifting the problem, not solving it.
- *Why D is incorrect:* `.env.example` is intended for placeholder documentation — storing a real Vault token there and relying on `.gitignore` is insecure and error-prone.

---

### Question 13 (5 points)

AWS Secrets Manager supports automatic rotation for RDS database credentials. When rotation is triggered, what happens to applications currently using the old credential?

- A) All connections using the old credential are immediately terminated
- B) AWS rotates the credential in a phased manner: the new credential is set while the old credential remains valid for a configurable window, allowing applications to retrieve the new secret before the old one expires
- C) The application must be redeployed for the new credential to take effect
- D) AWS sends a webhook notification to the application, which must then call `GetSecretValue` to update its connection pool

#### Q13 Correct Answer

B — AWS Secrets Manager rotation uses a Lambda function that follows a four-step rotation process (createSecret, setSecret, testSecret, finishSecret). During this process, both the old and new credentials are valid temporarily, preventing connection failures. Applications that retrieve the secret before the rotation window closes receive the new credential.

#### Q13 Distractor Analysis

- *Why A is incorrect:* Immediate termination of connections would cause application outages — the rotation process is designed to be non-disruptive.
- *Why C is incorrect:* Application redeployment is not required — applications retrieve the current secret value from Secrets Manager at runtime; the credential update is transparent.
- *Why D is incorrect:* Secrets Manager does not send webhooks to application processes — the application is responsible for retrieving the current secret value, typically at startup or via a refresh interval.

---

### Question 14 (5 points)

A developer uses `printenv | grep DATABASE_PASSWORD` inside a running container to debug a connection issue. The output is visible in the container's stdout. Which Vault feature prevents the database password from being a long-lived static value that could be exposed this way repeatedly?

- A) Vault's seal/unseal mechanism prevents secrets from being read while Vault is sealed
- B) Vault's dynamic database secrets engine generates a unique, short-lived credential per deployment — even if captured, it expires within the lease TTL
- C) Vault's audit log records the `printenv` command and alerts the security team
- D) Vault's response wrapping prevents the credential from being displayed in plaintext

#### Q14 Correct Answer

B — With dynamic database secrets, each deployment receives a unique database username and password with a TTL (e.g., 1 hour). Even if an attacker captures the credential from stdout, it expires automatically. There is no persistent "master" database password to protect — each credential is single-use-ish and time-bounded.

#### Q14 Distractor Analysis

- *Why A is incorrect:* Vault's seal/unseal protects Vault's own storage encryption — it does not control how a credential behaves once it has been issued to a client.
- *Why C is incorrect:* Vault's audit log records access to Vault's API, not commands run inside containers — `printenv` in a container is not visible to Vault.
- *Why D is incorrect:* Response wrapping is a Vault feature that delivers secrets as single-use tokens — but once the secret is unwrapped and injected as an environment variable, it can be read with `printenv`. The defense against repeated exposure is the short TTL, not wrapping.

---

### Question 15 (5 points)

A GitHub Actions workflow has the following step: `run: echo "DB_PASS=${{ secrets.DB_PASSWORD }}" >> $GITHUB_ENV`. What security risk does this introduce?

- A) Writing to `$GITHUB_ENV` sets environment variables that are visible to subsequent steps and jobs in the workflow, expanding the exposure surface beyond the step that needs the secret
- B) The `echo` command causes the secret to be printed to the pipeline log in plaintext, bypassing GitHub's masking
- C) Writing to `$GITHUB_ENV` stores the secret in the runner's filesystem permanently after the job completes
- D) This pattern is safe — `$GITHUB_ENV` is an encrypted file that is never readable by workflow steps

#### Q15 Correct Answer

A — Environment variables set via `$GITHUB_ENV` persist for the remainder of the workflow run — they are visible to all subsequent steps and jobs. A secret that is only needed in one step should be passed only to that step's `env:` block, not added to the global environment. The expanded exposure surface increases the risk of accidental logging or misuse in a later step.

#### Q15 Distractor Analysis

- *Why B is incorrect:* GitHub masks the value of known secrets in log output — the echo command would be masked. The risk is exposure scope, not log masking bypass.
- *Why C is incorrect:* `$GITHUB_ENV` is a temporary file on the runner that is cleaned up after the job — it does not persist permanently. The security concern is the in-run scope, not post-run persistence.
- *Why D is incorrect:* `$GITHUB_ENV` is a plaintext file on the runner that subsequent steps read to populate their environment. It is not encrypted and is readable by any step in the same job.

---

### Question 16 (5 points)

Which of the following correctly describes Vault's `cubbyhole` secrets engine?

- A) A shared secret store accessible to all tokens with the `cubbyhole-read` policy
- B) A private secrets storage namespace that is scoped to a single Vault token — secrets stored in one token's cubbyhole are completely invisible to all other tokens, including root
- C) A temporary secrets cache that persists for 24 hours before automatic deletion
- D) A secrets engine that stores encrypted blobs in an external S3 bucket

#### Q16 Correct Answer

B — Each Vault token has its own isolated cubbyhole namespace. Secrets written to a token's cubbyhole are accessible only by that token. When the token is revoked, the cubbyhole and all its contents are destroyed. This is the basis of Vault's response wrapping pattern.

#### Q16 Distractor Analysis

- *Why A is incorrect:* The cubbyhole is explicitly per-token and private — it is the opposite of a shared namespace.
- *Why C is incorrect:* The cubbyhole's lifetime is tied to the token's lifetime, not a fixed 24-hour timer.
- *Why D is incorrect:* The cubbyhole stores data in Vault's internal storage alongside all other secrets — it does not use external S3 storage.

---

### Question 17 (5 points)

A Vault policy grants `capabilities = ["read"]` on `secret/data/myapp/+`. What does the `+` wildcard match?

- A) All paths recursively under `secret/data/myapp/`
- B) Exactly one path segment — single-level paths like `secret/data/myapp/db` but not `secret/data/myapp/db/password`
- C) All paths in the entire Vault secret store
- D) Only paths that begin with a digit

#### Q17 Correct Answer

B — In Vault policy path notation, `+` is a glob that matches exactly one segment (no slashes). It matches `secret/data/myapp/db` but not `secret/data/myapp/db/password`. The `*` wildcard matches any sequence including slashes (recursive). Using `+` scopes the policy to a single depth level, enforcing tighter least-privilege.

#### Q17 Distractor Analysis

- *Why A is incorrect:* Recursive matching requires the `*` wildcard — `+` is a single-segment glob.
- *Why C is incorrect:* Matching all paths requires `secret/*` at the top level — `+` scoped under `myapp/` does not affect paths outside `myapp/`.
- *Why D is incorrect:* `+` matches any single path segment regardless of content — it has no digit-only filtering.

---

### Question 18 (5 points)

An organization rotates their database credentials monthly using a manual process. A DevSecOps engineer proposes using Vault's dynamic database secrets engine with a 4-hour TTL. What metric improves most directly?

- A) Mean Time to Deploy (MTTD)
- B) Credential exposure window — the maximum time a leaked credential remains valid drops from 30 days to 4 hours
- C) Pipeline Gate Pass Rate — fewer builds fail because rotation does not interrupt credential availability
- D) Vulnerability Density — fewer CVEs are reported because the credentials change frequently

#### Q18 Correct Answer

B — The key security metric improved by dynamic secrets is the exposure window. With monthly rotation, a leaked credential is valid for up to 30 days. With a 4-hour TTL, the same leaked credential expires in at most 4 hours. This dramatically reduces the window of opportunity for an attacker to use the credential before it is invalidated.

#### Q18 Distractor Analysis

- *Why A is incorrect:* MTTD (Mean Time to Deploy) measures deployment speed — credential TTL does not directly affect deployment frequency.
- *Why C is incorrect:* Pipeline Gate Pass Rate measures how often CI builds pass security gates — dynamic credentials reduce exposure but do not directly affect pipeline pass rates.
- *Why D is incorrect:* Vulnerability Density measures application code vulnerabilities — credential rotation frequency is unrelated to code vulnerability counts.

---

### Question 19 (5 points)

A developer accidentally commits an AWS access key to a private GitHub repository. The repository is private and has never been public. Which statement best describes the required response?

- A) No action is required — private repository history is not accessible without repository access
- B) The key should still be rotated immediately, as any user with current or historical repository access may have seen it, and the key may have been cached by internal tooling or bots
- C) The developer should delete the commit using GitHub's interface, which permanently removes it from all views
- D) GitHub automatically detects and revokes AWS keys in private repositories, so no manual rotation is needed

#### Q19 Correct Answer

B — Even in a private repository, rotation is the correct response. Any collaborator who cloned the repo, any CI/CD system with repository access, any internal dependency scanner, or any GitHub integration (Dependabot, CodeQL, Actions) may have accessed the commit during its exposure window. Rotation is the only way to definitively close the exposure.

#### Q19 Distractor Analysis

- *Why A is incorrect:* Private does not mean inaccessible — all current collaborators and any systems with granted access could have read the key.
- *Why C is incorrect:* GitHub's UI does not provide a "delete commit" feature that removes data from Git history — the data persists in the underlying repository until `git filter-repo` is run and the history is force-pushed.
- *Why D is incorrect:* GitHub's secret scanning with push protection covers private repos with GitHub Advanced Security, but automatic revocation in private repos depends on provider partner programs — it is not universally available for all secret types. Manual rotation should not be skipped.

---

### Question 20 (5 points)

In the context of secrets management, what is "secret sprawl" and which tool category primarily addresses it?

- A) Secret sprawl is when secrets are copied across multiple storage locations (environment variables, config files, code, multiple secret stores) making them difficult to inventory, rotate, and audit — addressed primarily by a centralized secrets management platform like Vault or AWS Secrets Manager
- B) Secret sprawl is when a secret is too long to be stored in environment variables — addressed by secret compression tools
- C) Secret sprawl is when multiple services share the same secret value — addressed by RBAC policies
- D) Secret sprawl is when secrets are stored in different geographic regions — addressed by cloud provider replication features

#### Q20 Correct Answer

A — Secret sprawl occurs when secrets exist in many places: hardcoded in source files, in multiple environment variable configurations, in multiple vault paths, in multiple team members' local `.env` files. This makes rotation difficult (you must find and update every location), auditability impossible (you cannot know who accessed each copy), and increases breach surface. Centralized secrets management platforms address this by providing a single authoritative source.

#### Q20 Distractor Analysis

- *Why B is incorrect:* Secret length is not what "sprawl" refers to — sprawl is about proliferation of copies across locations.
- *Why C is incorrect:* Shared secrets are a related but distinct concern — RBAC controls access but does not address the sprawl of copies across locations.
- *Why D is incorrect:* Geographic distribution is a high-availability concern — "sprawl" refers to uncontrolled duplication, not intentional replication for availability.

---

Quiz — Module 09 | CIS-4350 | Texas Wesleyan University | Professor Nash

# Reading Guide: Module 08 — Software Composition Analysis and Supply Chain Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Describe the full scope of SCA beyond vulnerability scanning (license, policy, reachability)
- Compare Snyk and Black Duck on key capability dimensions
- Explain SPDX and CycloneDX SBOM formats, their origins, and optimal use cases
- Describe dependency confusion attacks and enumerate prevention strategies
- Configure cosign keyless signing for container images in CI
- Explain the four SLSA levels and what provenance documents contain

---

## Section 1 — SCA: Scope and Tools

### 1.1 SCA Capability Dimensions

| Capability | Description | Business Value |
|---|---|---|
| Vulnerability detection | CVE matching against NVD, GitHub Advisory, OSS Index | Security risk management |
| License compliance | Identify licenses; flag copyleft risks | Legal risk management |
| Transitive dependency tracking | Map complete dependency tree | Full risk visibility |
| Reachability analysis | Determine if vulnerable function is called | Reduce false positive noise |
| Policy enforcement | Define fail conditions for CI gates | Automated governance |
| Fix suggestions | Recommend upgrade paths | Developer efficiency |
| PR integration | Show new vulnerabilities on pull requests | Shift-left feedback |
| Dependency age | Flag unmaintained packages | Latent risk reduction |

### 1.2 Snyk vs. Black Duck Comparison

| Feature | Snyk | Black Duck |
|---|---|---|
| Primary audience | Developer-first | Enterprise security/legal teams |
| Reachability analysis | Yes (key differentiator) | Limited |
| License compliance | Good | Excellent (deep legal analysis) |
| Binary scanning | Limited | Excellent (BDA — no source needed) |
| Multi-language | 20+ languages | 30+ languages |
| IDE integration | VS Code, IntelliJ, others | IDE plugins available |
| PR decoration | Native GitHub/GitLab integration | Yes |
| CI integration | Native GitHub Actions | Jenkins, GitHub, others |
| SBOM generation | Yes (CycloneDX, SPDX) | Yes |
| Pricing model | SaaS subscription | Enterprise license |
| Open-source version | Snyk CLI (free tier) | No free tier |

### 1.3 Snyk Configuration

```yaml
# .snyk policy file
version: v1.25.0

ignore:
  SNYK-PYTHON-PYYAML-559098:
    - "*":
        reason: >
          PyYAML vulnerability in yaml.load() — we use yaml.safe_load() exclusively.
          Reviewed and accepted 2024-03-15 by SecurityTeam.
        expires: "2024-09-15T00:00:00.000Z"

patch: {}
```

The `.snyk` file tracks accepted risks with mandatory expiry dates — forcing periodic re-review.

---

## Section 2 — SBOM Formats Deep Dive

### 2.1 Package URL (purl) Standard

The Package URL (purl) is the universal component identifier used in CycloneDX and increasingly in SPDX:

```text
pkg:{ecosystem}/{namespace}/{name}@{version}?{qualifiers}#{subpath}

Examples:
pkg:pypi/flask@3.0.3
pkg:npm/%40angular/core@17.0.0
pkg:maven/org.springframework/spring-core@6.0.0
pkg:golang/github.com/gin-gonic/gin@v1.9.1
pkg:deb/debian/curl@7.88.1-10+deb12u4?distro=bookworm
```

### 2.2 CycloneDX VEX (Vulnerability Exploitability Exchange)

VEX documents accompany SBOMs and document the actual exploitability status of CVEs in a specific deployment:

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "vulnerabilities": [
    {
      "id": "CVE-2022-42969",
      "source": { "name": "NVD", "url": "https://nvd.nist.gov/" },
      "ratings": [{ "score": 9.8, "severity": "critical" }],
      "analysis": {
        "state": "not_affected",
        "justification": "code_not_reachable",
        "detail": "The vulnerable xmlrpc module is not imported or called in this application"
      }
    }
  ]
}
```

VEX states include:

- `affected` — the vulnerability is present and exploitable
- `not_affected` — component present but not exploitable (with justification)
- `fixed` — the vulnerability has been remediated
- `under_investigation` — status is being determined

### 2.3 SBOM Generation Tools Comparison

| Tool | Output Formats | Source Types | Best For |
|---|---|---|---|
| Syft | CycloneDX, SPDX, many others | Images, directories, files | General purpose |
| Trivy | CycloneDX, SPDX | Images, filesystems | Integrated with CVE scanning |
| cdxgen | CycloneDX | 20+ build manifests | Multi-language projects |
| Microsoft SBOM Tool | SPDX | Files, packages | Microsoft/GitHub environments |
| Tern | SPDX | Docker images (layer analysis) | Deep image layer inspection |

---

## Section 3 — Dependency Confusion Attacks

### 3.1 Attack Mechanics

```text
Victim's internal registry:  company-auth-utils@1.2.3 (private)
Attacker's public registry:  company-auth-utils@9.9.9 (malicious)

Package manager resolution:
1. Developer runs: npm install
2. npm checks both registries
3. npm finds 9.9.9 > 1.2.3 on public registry
4. npm downloads MALICIOUS package from public registry
```

### 3.2 Prevention Controls

| Control | Implementation | Effectiveness |
|---|---|---|
| Scoped packages | `@company/package-name` — org-scoped NPM packages | High — namespace reserved |
| Registry pinning | `.npmrc`: `@company:registry=https://private.registry/` | High |
| Lock files | `package-lock.json`, `poetry.lock` with integrity hashes | High — pins exact versions |
| Package integrity verification | npm `--verify-store` / pip hash checking | High |
| Private registry proxy | JFrog Artifactory, Nexus as pull-through cache with allowlist | Very High |
| Dependency review action | GitHub's `actions/dependency-review-action` in CI | Medium — detects new versions |

### 3.3 GitHub Dependency Review Action

```yaml
- name: Dependency Review
  uses: actions/dependency-review-action@v4
  with:
    fail-on-severity: high
    deny-licenses: GPL-3.0, AGPL-3.0
    allow-ghsas: GHSA-xxxx-xxxx-xxxx  # Known accepted advisory
```

This action runs on pull requests and blocks merges that introduce dependencies with:

- Vulnerabilities above the severity threshold
- Licenses that violate the policy
- Known malicious packages

---

## Section 4 — Code Signing and Sigstore

### 4.1 Sigstore Components

| Component | Function |
|---|---|
| cosign | CLI tool for signing and verifying container images and other artifacts |
| Fulcio | Certificate authority that issues short-lived signing certificates bound to OIDC identities |
| Rekor | Immutable transparency log recording all signatures — public, append-only |
| TSA | Timestamp Authority for RFC 3161 timestamps on signatures |

### 4.2 Keyless Signing Flow

```text
1. GitHub Actions workflow starts
2. Workflow requests OIDC token from GitHub (identity: github.com/org/repo, workflow path, ref)
3. cosign sends OIDC token to Fulcio
4. Fulcio verifies OIDC token and issues a short-lived X.509 certificate
5. cosign signs the image with an ephemeral key + certificate
6. Signature + certificate recorded in Rekor transparency log
7. Ephemeral key is discarded — no long-lived private key exists
```

### 4.3 Verification

```bash
# Verify image was signed by a specific GitHub Actions workflow
cosign verify \
  --certificate-identity="https://github.com/org/repo/.github/workflows/release.yml@refs/heads/main" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  myregistry.io/myapp:v1.2.3

# Output shows:
# Verification for myregistry.io/myapp:v1.2.3
# The following checks were performed on each of these signatures:
#   - The cosign claims were validated
#   - Existence of the claims in the transparency log was verified
#   - The code-signing certificate claims were validated
```

### 4.4 Admission Control with Policy Controller

The Sigstore Policy Controller (for Kubernetes) enforces image signature verification at admission:

```yaml
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: require-signed-images
spec:
  images:
    - glob: "myregistry.io/**"
  authorities:
    - keyless:
        url: https://fulcio.sigstore.dev
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subjectRegExp: "https://github.com/myorg/.*"
```

---

## Section 5 — SLSA Framework

### 5.1 SLSA v1.0 Levels

| Level | Requirements | What It Prevents |
|---|---|---|
| SLSA 1 | Build process scripted; provenance generated | Accidental errors; basic attestation |
| SLSA 2 | Version control; build service used; signed provenance | Unauthorized builds; tampering after build |
| SLSA 3 | Isolated builds; builds run on hardened platform | Compromised build environment; CI/CD tampering |

Note: SLSA v0.1 had Levels 1–4; SLSA v1.0 consolidates to Levels 1–3.

### 5.2 SLSA Provenance Document

A SLSA provenance document is an attestation answering five questions:

- What artifact was produced? (digest, name)
- Where did the source come from? (repository URL, commit SHA)
- Who built it? (builder identity, build platform)
- How was it built? (workflow file, build steps)
- When was it built? (timestamp)

```json
{
  "_type": "https://in-toto.io/Statement/v0.1",
  "predicateType": "https://slsa.dev/provenance/v1",
  "subject": [
    {
      "name": "myapp",
      "digest": { "sha256": "abc123..." }
    }
  ],
  "predicate": {
    "buildDefinition": {
      "buildType": "https://slsa-framework.github.io/github-actions-buildtypes/workflow/v1",
      "externalParameters": {
        "workflow": {
          "ref": "refs/tags/v1.2.3",
          "repository": "https://github.com/myorg/myapp",
          "path": ".github/workflows/release.yml"
        }
      }
    },
    "runDetails": {
      "builder": {
        "id": "https://github.com/actions/runner/releases/tag/v2.302.1"
      }
    }
  }
}
```

---

## Exam Tips for DSOE Certification

- SCA covers vulnerability, license, reachability, and policy — not just CVEs.
- Snyk's reachability analysis determines if a vulnerable code path is actually called — reduces false positives.
- SPDX is ISO 5962:2021 from the Linux Foundation; CycloneDX is from OWASP — know both origins.
- CycloneDX uniquely supports VEX for documenting whether CVEs are exploitable in your deployment.
- purl (Package URL) is the standard cross-ecosystem package identifier format.
- Dependency confusion: attacker publishes higher-versioned malicious package to public registry with internal package name.
- Prevention: scoped packages, registry pinning, lock files, private registry proxy.
- Sigstore/cosign keyless signing uses OIDC identity (GitHub Actions) + Fulcio CA + Rekor log — no long-lived keys.
- SLSA v1.0 has three levels. Level 3 requires isolated builds on a hardened platform.
- SLSA provenance documents: what was built, from where, by whom, how, and when.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| SCA | Software Composition Analysis — full lifecycle open-source risk management |
| Snyk | Developer-focused SCA platform with reachability analysis |
| Black Duck | Enterprise SCA platform by Synopsys with binary analysis |
| Reachability Analysis | Determining whether a vulnerable library function is actually called |
| SPDX | Software Package Data Exchange — ISO SBOM standard from Linux Foundation |
| CycloneDX | OWASP SBOM standard optimized for security use cases |
| VEX | Vulnerability Exploitability Exchange — documents CVE exploitability status |
| purl | Package URL — standardized cross-ecosystem package identifier |
| Dependency Confusion | Attack exploiting public/private registry name resolution |
| cosign | Sigstore CLI tool for artifact signing and verification |
| Fulcio | Sigstore certificate authority for short-lived OIDC-bound signing certs |
| Rekor | Sigstore transparency log for signatures |
| SLSA | Supply-chain Levels for Software Artifacts — supply chain integrity framework |
| Provenance | SLSA attestation document describing artifact origin and build process |

---

## 9. Supplemental Resources

**1. [Snyk documentation — CLI reference and CI/CD integration](https://docs.snyk.io/snyk-cli)**
Official Snyk CLI documentation covering all commands (`test`, `monitor`, `sbom`), severity threshold flags, JSON output format, and GitHub Actions integration. Includes language-specific scanning guides for Python, Node.js, Java, and Go.

**2. [SLSA framework — supply chain levels and requirements](https://slsa.dev/spec/v1.0/)**
The official SLSA specification defining the four integrity levels for software artifacts. Covers provenance requirements, build platform requirements, and examples of what satisfies each level. Essential for understanding modern software supply chain security requirements.

**3. [OpenSSF Sigstore documentation](https://docs.sigstore.dev/)**
Comprehensive documentation for the Sigstore project (cosign, Fulcio, Rekor). Covers keyless signing with OIDC, transparency log queries, policy verification, and integration with GitHub Actions and Kubernetes admission control.

---

Reading Guide — Module 08 | CIS-4350 | Texas Wesleyan University | Professor Nash

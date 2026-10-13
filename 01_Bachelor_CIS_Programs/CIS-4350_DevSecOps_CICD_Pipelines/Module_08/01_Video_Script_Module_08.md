# Video Script: Module 08 — Software Composition Analysis and Supply Chain Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 08 title card]

Welcome to Module 08. In Module 07 we covered dependency scanning as one layer of application security testing. In this module we go deeper on the supply chain — the entire chain of trust from developer to end user. Supply chain attacks have become one of the most significant security threats of the decade. The SolarWinds attack in 2020 and the XZ Utils backdoor in 2024 demonstrated that compromising a single upstream component can affect thousands of organizations downstream.

By the end of this module you'll understand SCA tools in depth, the two major SBOM formats, dependency confusion attacks, code signing for supply chain integrity, and the SLSA framework for supply chain levels.

---

### SEGMENT 2 — Software Composition Analysis in Depth (1:30–5:00)

[SLIDE: SCA tool architecture diagram]

Software Composition Analysis — SCA — is a broader discipline than simple vulnerability scanning. SCA tools analyze:

Open-source component inventory — which libraries are used, at which versions, including transitive dependencies.

Vulnerability detection — which components have known CVEs in the NVD, GitHub Advisory Database, or OSS Index.

License compliance — which open-source licenses are in use, whether they are compatible with the application's license, and whether any licenses impose copyleft requirements.

Outdated component detection — which dependencies are significantly behind the current release, even without active CVEs.

Policy enforcement — configurable rules that fail builds on specific vulnerability conditions, license types, or age thresholds.

Two leading commercial SCA platforms:

Snyk is developer-focused. It integrates with IDEs, GitHub pull requests, and CI pipelines. Snyk's killer feature is prioritization — it uses reachability analysis to determine whether a vulnerable function in a library is actually called by your code, reducing false positive noise.

```bash
# Snyk CLI scan
snyk test --severity-threshold=high --json > snyk-results.json

# Test a specific package manifest
snyk test --file=requirements.txt --package-manager=pip

# Monitor a project (uploads to Snyk dashboard)
snyk monitor --project-name=myapp

# In GitHub Actions
- uses: snyk/actions/python@master
  with:
    args: --severity-threshold=high
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

Black Duck by Synopsys is the enterprise SCA platform. It is particularly strong in license compliance, legal risk assessment, and multi-language monorepo support. Black Duck's "Black Duck Binary Analysis" can scan compiled artifacts without access to source code.

---

### SEGMENT 3 — SBOM Formats: SPDX and CycloneDX (5:00–9:00)

[SLIDE: SPDX vs. CycloneDX feature comparison]

Let's look at the two SBOM formats in more detail.

SPDX — Software Package Data Exchange — was created by the Linux Foundation and became an ISO standard in 2021 (ISO/IEC 5962:2021). It originated in the license compliance world and has excellent license tracking capabilities. SPDX documents can be in JSON, RDF, YAML, or tag-value format.

An SPDX JSON document has this structure:

```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "myapp-v1.2.3",
  "documentNamespace": "https://example.com/myapp-v1.2.3",
  "packages": [
    {
      "SPDXID": "SPDXRef-Package-flask",
      "name": "flask",
      "versionInfo": "3.0.3",
      "downloadLocation": "https://pypi.org/project/flask/3.0.3/",
      "licenseConcluded": "BSD-3-Clause",
      "externalRefs": [
        {
          "referenceCategory": "SECURITY",
          "referenceType": "cpe23Type",
          "referenceLocator": "cpe:2.3:a:palletsprojects:flask:3.0.3:*:*:*:*:*:*:*"
        }
      ]
    }
  ]
}
```

CycloneDX was created by OWASP and is optimized for security use cases. It supports VEX (Vulnerability Exploitability Exchange) documents that accompany the SBOM to document which CVEs are and aren't exploitable in your specific deployment. CycloneDX is typically preferred for security tooling integration.

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "version": 1,
  "metadata": {
    "timestamp": "2024-01-15T10:00:00Z",
    "component": {
      "type": "application",
      "name": "myapp",
      "version": "1.2.3"
    }
  },
  "components": [
    {
      "type": "library",
      "name": "flask",
      "version": "3.0.3",
      "purl": "pkg:pypi/flask@3.0.3",
      "licenses": [{ "license": { "id": "BSD-3-Clause" } }]
    }
  ],
  "vulnerabilities": []
}
```

The key identifier in CycloneDX is the `purl` — Package URL — a standardized string format identifying a package by ecosystem, name, and version. `pkg:pypi/flask@3.0.3`, `pkg:npm/lodash@4.17.21`, `pkg:maven/org.springframework/spring-core@6.0.0`.

---

### SEGMENT 4 — Dependency Confusion Attacks (9:00–12:00)

[SLIDE: Dependency confusion attack diagram]

Dependency confusion is a supply chain attack technique discovered by security researcher Alex Birsan in 2021. It exploits how package managers resolve package names when both public and private registries are configured.

Here's how it works: Your application uses a private internal package named `company-auth-utils`. This package exists only in your private registry. An attacker discovers the internal package name — perhaps through a leaked `package.json` or a public job posting. The attacker publishes a malicious package with the same name to the public npm registry (or PyPI) at a higher version number — say version 9.9.9.

When your developer runs `npm install`, the package manager checks both the private registry and the public registry. It finds `company-auth-utils@9.9.9` on the public registry — a higher version than your private `company-auth-utils@1.2.3`. It downloads and installs the malicious public package.

Birsan reported this vulnerability to dozens of companies including Apple, Microsoft, Shopify, and PayPal, and collected over $130,000 in bug bounties.

Prevention strategies:

Use scoped packages for internal packages — `@company/auth-utils` — which cannot be published to public npm by non-org members.

Configure package manager registry pinning to always prefer the private registry for specific package name patterns.

Use lock files (`package-lock.json`, `poetry.lock`, `Pipfile.lock`) to pin exact package versions and their integrity hashes.

Enable Subresource Integrity verification — npm and pip can verify SHA hashes of downloaded packages.

Use a repository manager (JFrog Artifactory, Nexus) as a pull-through proxy with explicit allowlisting of public packages.

```bash
# .npmrc configuration to use private registry for @company scope
@company:registry=https://registry.company.com/
//registry.company.com/:_authToken=${NPM_TOKEN}

# Block public registry for @company scope
@company:registry=https://registry.company.com/
//registry.npmjs.org/:always-auth=false
```

---

### SEGMENT 5 — Code Signing for Supply Chain Integrity (12:00–15:30)

[SLIDE: Sigstore/cosign signature verification flow]

Code signing provides cryptographic proof that an artifact was produced by a specific entity and has not been tampered with since signing. In a supply chain security context, signing covers:

Git commits — GPG or SSH signed commits prove authorship (covered in Module 02).

Container images — cosign signs images so consumers can verify they were produced by a trusted CI pipeline.

Release artifacts — JARs, Python wheels, npm packages can be signed and verified.

The Sigstore project provides a transparent, auditable signing infrastructure. cosign integrates with GitHub Actions OIDC to enable keyless signing — the signing key is derived from the CI pipeline's identity token, not a long-lived private key.

```yaml
# Keyless signing with cosign in GitHub Actions
- name: Sign container image with cosign (keyless)
  uses: sigstore/cosign-installer@v3
  - run: |
      cosign sign \
        --yes \
        myregistry.io/myapp:${{ github.sha }}
```

The resulting signature is stored in the container registry alongside the image and recorded in Sigstore's Rekor transparency log — a public, append-only log of all signatures.

Consumers verify:

```bash
cosign verify \
  --certificate-identity-regexp="https://github.com/myorg/myrepo" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  myregistry.io/myapp:v1.2.3
```

This verifies that the image was signed by a GitHub Actions workflow in the `myorg/myrepo` repository.

---

### SEGMENT 6 — SLSA Framework (15:30–19:00)

[SLIDE: SLSA levels pyramid — 1 to 4]

SLSA — Supply-chain Levels for Software Artifacts — pronounced "salsa" — is a security framework developed by Google and now hosted by the OpenSSF. SLSA defines four levels of supply chain integrity, with higher levels requiring stronger guarantees.

SLSA Level 1: Build process is scripted or automated. Basic documentation of the build process. Provides some protection against accidental tampering.

SLSA Level 2: Version control is used for all source. Build service is used (not just developer machines). Provenance is generated — a signed document describing where the artifact came from and how it was built.

SLSA Level 3: Source is verified — it came from version control and the build script is in the same repo. Build platform provides stronger security guarantees — isolated build environments.

SLSA Level 4 (now merged into Level 3 in SLSA v1.0): Two-party review of all changes to source. Hermetic builds — builds are fully isolated and reproducible.

Provenance is the key concept. A SLSA provenance document answers: Who built this? What source did they use? When was it built? What build system was used?

GitHub Actions natively generates SLSA provenance for artifacts:

```yaml
- name: Generate SLSA provenance
  uses: actions/attest-build-provenance@v1
  with:
    subject-name: myregistry.io/myapp
    subject-digest: sha256:abc123...
```

The provenance attestation is stored in the registry and can be verified by consumers:

```bash
gh attestation verify myregistry.io/myapp:v1.2.3 \
  --owner myorg
```

---

### SEGMENT 7 — Module Summary and Looking Ahead (19:00–21:00)

[SLIDE: Module 08 key takeaways]

Module 08 summary.

SCA tools — Snyk and Black Duck — provide vulnerability detection, license compliance, and policy enforcement for open-source dependencies. Snyk's reachability analysis reduces false positive noise.

SPDX is the ISO-standard SBOM format from the Linux Foundation with excellent license tracking. CycloneDX is the OWASP-standard format optimized for security use cases, including VEX support.

Dependency confusion attacks exploit package manager name resolution when public and private registries coexist. Use scoped packages, registry pinning, lock files, and repository managers to prevent this.

Code signing with cosign and Sigstore provides cryptographic proof of artifact provenance. Keyless signing via GitHub Actions OIDC eliminates long-lived private keys.

SLSA defines four levels of supply chain integrity. SLSA provenance documents where an artifact came from and how it was built. GitHub Actions can generate native SLSA provenance.

In Module 09 — our final module — we address secrets management in depth: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, dynamic secrets, and secret rotation. See you there.

---

*[END OF SCRIPT — Module 08]*

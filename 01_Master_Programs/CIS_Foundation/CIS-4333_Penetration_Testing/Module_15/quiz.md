# Quiz: Module 15 — Specialized Testing Environments

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

A penetration tester discovers an SSRF vulnerability in a web application running on an AWS EC2 instance. Which specific URL should the tester attempt to reach (in an authorized test) to retrieve the instance's IAM role credentials?

A. `http://192.168.1.1/latest/meta-data/iam/security-credentials/`

B. `http://169.254.169.254/latest/meta-data/iam/security-credentials/`

C. `http://169.254.169.254/v1/secret/aws/creds`

D. `http://100.100.100.200/latest/meta-data/iam/security-credentials/`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. 192.168.1.1 is a common default gateway address in private networks. The IMDS is not accessible at this address.
- B is correct. The AWS Instance Metadata Service (IMDS) is accessible at the link-local address 169.254.169.254. The path `/latest/meta-data/iam/security-credentials/` lists available IAM role names, and appending the role name returns temporary credentials.
- C is incorrect. This path resembles HashiCorp Vault's secret engine path syntax, not the AWS IMDS path.
- D is incorrect. 100.100.100.200 is Alibaba Cloud's equivalent of the IMDS. AWS uses 169.254.169.254.

---

**Question 2**

During an authorized OT security assessment of a manufacturing plant, a tester wants to enumerate all devices on the operational network. Which approach is MOST appropriate?

A. Run Nmap with the -sV flag to identify service versions.

B. Deploy a network tap and perform passive traffic analysis with Wireshark or a dedicated OT analysis platform.

C. Use masscan for rapid port discovery since speed minimizes disruption.

D. Run Shodan against the plant's external IP range to identify exposed OT devices.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Nmap version scanning generates network probes that can disrupt timing-sensitive OT protocols and potentially crash PLCs and HMIs that cannot handle unexpected network traffic. Active scanning is inappropriate in live OT environments.
- B is correct. Passive traffic analysis captures existing traffic without generating any probes. This safely identifies devices, protocols, and communications patterns without risking operational disruption.
- C is incorrect. Masscan sends probes at extremely high rates. This is even more disruptive than Nmap in a live OT environment and could cause control system failures.
- D is incorrect. Shodan scans public-facing IP addresses. Internal OT networks are not exposed to Shodan scanning. Even if they were, testing via Shodan does not provide the segmented internal network visibility needed for an OT assessment.

---

**Question 3**

A security researcher extracts a firmware image from an IoT security camera and runs Binwalk on the binary. Which output would indicate that the firmware contains a Linux filesystem worth examining further?

A. `JPEG image data` at offset 0x0100

B. `Squashfs filesystem, little endian` at offset 0x100000

C. `CRC32 polynomial table, little endian` at offset 0x0200

D. `ARM instructions, 32-bit` at offset 0x0000

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. JPEG image data indicates embedded graphics, likely icons or UI elements. It is not a filesystem worth examining for security purposes.
- B is correct. Squashfs is a compressed read-only Linux filesystem commonly used in embedded firmware. Extracting this filesystem reveals the device's operating system files, configuration, credentials, and application code.
- C is incorrect. A CRC32 polynomial table is a mathematical lookup table for checksum calculations. It does not indicate a filesystem.
- D is incorrect. ARM instructions indicate the start of executable code (the CPU is ARM32). This confirms the architecture but does not directly indicate a filesystem with examinable contents.

---

**Question 4**

A mobile application implements certificate pinning. A penetration tester is attempting to route the app's traffic through Burp Suite. Which approach would MOST effectively bypass certificate pinning on an Android device?

A. Install Burp's CA certificate in the Android system certificate store.

B. Use Frida with a certificate pinning bypass script to hook the certificate validation function at runtime.

C. Configure Burp Suite to use TLS 1.0 since older TLS versions bypass pinning.

D. Decompile the APK with Jadx and recompile with certificate pinning code removed, but do not re-sign the APK.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Many apps with certificate pinning explicitly check the certificate chain against embedded certificates, ignoring system certificate stores entirely. Installing the Burp CA to the system store is sufficient for apps without pinning but ineffective against apps that implement pinning.
- B is correct. Frida hooks the pinning validation function at runtime, overriding its return value to accept any certificate. This works regardless of how pinning is implemented (OkHttp, TrustKit, custom implementation) and does not require modifying the app binary.
- C is incorrect. TLS version negotiation is separate from certificate pinning. Downgrading to TLS 1.0 does not bypass certificate validation — it just changes the cipher suite negotiation.
- D is incorrect. Recompiling without pinning code is a valid approach, but re-signing the APK is required. Android enforces APK signature verification; an unsigned or improperly signed APK cannot be installed on a standard device. The recompile-and-resign approach is valid if properly executed.

---

**Question 5**

An API tester sends the following HTTP request and receives a successful response with another user's order data:

```
GET /api/v1/orders/10247
Authorization: Bearer [valid_token_for_user_A]
```

Order 10247 belongs to user B. Which OWASP API Security Top 10 category does this vulnerability fall under?

A. API2:2023 — Broken Authentication

B. API5:2023 — Broken Function Level Authorization

C. API1:2023 — Broken Object Level Authorization

D. API8:2023 — Security Misconfiguration

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. Broken Authentication involves weaknesses in the authentication mechanism — missing authentication, weak token validation, or insecure credential handling. The authentication (Bearer token) is working; the problem is that authorization does not validate ownership of the requested object.
- B is incorrect. Broken Function Level Authorization (BFLA) describes accessing privileged functions (admin endpoints, elevated operations) as a lower-privilege user. The issue here is accessing another user's object, not accessing an elevated function.
- C is correct. BOLA (Broken Object Level Authorization) describes APIs that accept user-controlled object identifiers without verifying that the requester is authorized to access that specific object. Accessing order 10247 as user A when it belongs to user B is a textbook BOLA example.
- D is incorrect. Security Misconfiguration describes issues like default configurations, unnecessary HTTP methods, missing security headers, and verbose error messages. BOLA is an authorization logic flaw, not a misconfiguration.

---

**Question 6**

A JWT is signed with algorithm RS256 (asymmetric). A tester suspects the server may be vulnerable to algorithm confusion. Which attack is being attempted if the tester modifies the JWT header to `"alg": "HS256"` and re-signs the token using the server's public key?

A. The tester is attempting to crack the JWT's HMAC key using a dictionary attack.

B. The tester is exploiting a vulnerability where the server uses the public key (intended for RS256 signature verification) as the HMAC secret for HS256, allowing signature forging.

C. The tester is attempting to bypass authentication by removing the signature entirely.

D. The tester is attempting to extend the token's expiration by modifying the `exp` claim.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. A dictionary attack against an HMAC secret tests many possible secret values. This attack uses the known public key, not a dictionary.
- B is correct. The algorithm confusion attack exploits JWT libraries that do not enforce the expected algorithm. If the server validates an HS256 token by using the public key as the HMAC secret (because it is the "trusted key"), an attacker who knows the public key (which is often public) can forge valid tokens.
- C is incorrect. Removing the signature is the `alg:none` attack. The algorithm confusion attack described here uses a specific algorithm (HS256) and a valid signature — forged using the public key as the HMAC secret.
- D is incorrect. Modifying the `exp` claim changes the expiration time but does not describe the algorithm confusion attack. Additionally, modifying any claim in a valid JWT invalidates the signature unless the attacker can re-sign.

---

**Question 7**

Which tool is specifically designed as an AWS exploitation framework with modules for IAM enumeration, privilege escalation, and cloud-specific post-exploitation?

A. ScoutSuite

B. Prowler

C. Pacu

D. CloudMapper

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. ScoutSuite is a multi-cloud security auditing tool that identifies misconfigurations. It is an assessment/audit tool, not an exploitation framework.
- B is incorrect. Prowler is an AWS security assessment tool that checks for compliance with security standards. It is also an audit tool, not an exploitation framework.
- C is correct. Pacu is the open-source AWS exploitation framework developed by Rhino Security Labs. It provides exploitation modules for IAM privilege escalation, credential extraction, data exfiltration, and persistence establishment.
- D is incorrect. CloudMapper is a visualization tool that creates network diagrams of AWS environments and identifies public exposure. It is an analysis tool, not an exploitation framework.

---

**Question 8**

A tester sends a GraphQL introspection query to an API and receives a full schema response including a field named `getUsersSensitiveData(userId: ID!)`. The response also shows that the query field has no documented authentication requirement. What is the MOST appropriate next testing step?

A. Document the introspection response as a security misconfiguration finding and stop testing.

B. Test the `getUsersSensitiveData` query with authenticated credentials to confirm it is accessible, then test with another user's credentials or no credentials to identify authorization bypass.

C. Disable introspection by recommending it to the client immediately.

D. Report this to the vendor since internal API fields should not be visible to clients.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Documenting introspection exposure is valid (introspection should be disabled in production), but stopping there misses the higher-value finding — whether the sensitive data endpoint has proper authorization controls.
- B is correct. The introspection response reveals a potentially sensitive endpoint. The next step is testing whether authorization is properly enforced: can any authenticated user access it? Can unauthenticated requests access it? Can user A access user B's data via this endpoint?
- C is incorrect. Disabling introspection is a remediation recommendation, not a testing step. Recommending it during testing before completing the assessment is premature.
- D is incorrect. The application being tested belongs to the client, not a third-party vendor (in this scenario). "Reporting to the vendor" conflates the client and vendor roles.

---

**Question 9**

A penetration tester is assessing a SCADA system at a water utility. The SCADA system uses Modbus TCP on a network segment shared with the corporate IT network. The tester wants to demonstrate that an attacker with access to the corporate network could send unauthorized write commands to the PLCs. Which constraint is MOST important when planning this test?

A. The test must use Metasploit modules specifically designed for Modbus to ensure accuracy.

B. The test must be performed in an isolated test environment (lab replicate of the production system) with plant engineers present and safety systems engaged.

C. The test should be conducted during business hours to ensure the maximum number of operators can observe the results.

D. The tester must obtain authorization only from the corporate IT security team since the test originates from the IT network.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Tool selection is secondary to safety. Whether Metasploit or direct Modbus libraries are used is a methodology detail; the critical constraint is that the test must not be performed against live operational systems.
- B is correct. Testing write commands against production PLCs in a water utility could cause operational disruptions with direct public safety consequences. The test must be performed in an isolated environment. Plant engineers must be present to immediately stop the test if safety is threatened, and safety systems must be engaged.
- C is incorrect. Conducting OT disruptive testing during business hours when the plant is fully operational is the opposite of safe practice. Critical OT testing should occur during scheduled maintenance windows.
- D is incorrect. OT systems are under the authority of the operations team, not just IT. Authorization must come from the appropriate plant management and operations leadership — not only from IT security, which typically does not have authority over operational safety.

---

**Question 10**

AWS IMDSv2 was introduced to mitigate SSRF-based attacks against the EC2 Instance Metadata Service. Which technical mechanism does IMDSv2 use to prevent SSRF attacks from accessing the IMDS?

A. IMDSv2 requires the requesting process to have a specific IAM permission to query the metadata service.

B. IMDSv2 requires a two-step process: a PUT request to obtain a session token, then a GET request using that token. Standard SSRF cannot perform the PUT request.

C. IMDSv2 moves the IMDS to a different IP address that is randomized per boot.

D. IMDSv2 encrypts the metadata with a key only accessible to the IAM role, preventing SSRF from reading credentials.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. IAM permissions control what the instance role can access in AWS, not whether a process can query the local IMDS. IMDS is local to the instance; IAM permissions operate at the AWS API level.
- B is correct. IMDSv2 requires: 1) A PUT request to `http://169.254.169.254/latest/api/token` with a TTL header to obtain a session token; 2) Subsequent GET requests must include the session token in an `X-aws-ec2-metadata-token` header. Classic SSRF typically exploits GET requests. While some SSRF vulnerabilities can make PUT requests, the two-step requirement significantly raises the attack complexity.
- C is incorrect. IMDSv2 uses the same IP address (169.254.169.254). The address is not randomized.
- D is incorrect. IMDSv2 does not encrypt the metadata response. The protection is in the required session token, not in encryption of the response content.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | B |
| 9 | B |
| 10 | B |

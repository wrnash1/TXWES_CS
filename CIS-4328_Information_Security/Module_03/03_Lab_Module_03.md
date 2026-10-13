# Lab Activity: Module 03 - Cryptography
## Course: CIS-4328_Information_Security (CompTIA Security+ (SY0-701))

---

**Objective:** Use GPG to generate asymmetric key pairs, export public keys, and encrypt a message.
**Instructions:**
1. Boot your Kali Linux VM.
2. Open a terminal and generate a new GPG key pair: `gpg --full-generate-key` (Select RSA, 2048 bit, and enter your details).
3. Export your public key to an armor-encoded file: `gpg --armor --export your.email@txwes.edu > public.key`
4. Exchange `public.key` files with a lab partner (or simulate by creating a second user).
5. Import your partner's public key: `gpg --import partner_public.key`
6. Encrypt a text file using their public key: `gpg --encrypt --recipient partner.email@txwes.edu secret.txt`
**Deliverable:** Take a screenshot of the terminal output showing the successful encryption of `secret.txt` resulting in the `secret.txt.gpg` file. Submit to Canvas.

---

## Part 9 — Challenge Exercise

### Challenge 1: OWASP Top 10 Vulnerability Mapping and Defense Design

Using the OWASP Top 10 2021 list at <https://owasp.org/www-project-top-ten/>, complete the following analysis tasks without accessing or testing any live systems.

1. Locate the entries for A03:2021-Injection and A07:2021-Identification and Authentication Failures. For each entry, record: the rank and name, a one-sentence description of the vulnerability class, and the two most important prevention techniques listed by OWASP. Then explain, in your own words, why parameterized queries prevent SQL injection but input filtering alone does not.
2. A developer argues that deploying a WAF is sufficient protection against all OWASP Top 10 injection risks and that fixing the underlying code is optional. Evaluate this argument. Identify two specific injection scenarios from Module 03 where a WAF could be bypassed, and explain the bypass mechanism for each.
3. Review the OWASP entry for A10:2021-Server-Side Request Forgery (SSRF). Describe one cloud-specific SSRF scenario not already covered in the Module 03 reading guide — include the target endpoint, the data exposed, and one defensive control that would block the attack.
4. Select any three OWASP Top 10 2021 entries and for each one: classify the primary CIA Triad property violated, identify the correct CVSS Attack Vector (Network/Adjacent/Local/Physical), and state whether the vulnerability is most effectively addressed by a Technical/Preventive, Technical/Detective, or Administrative/Preventive control. Justify each answer.

### Challenge 2: Secure Code Review — Vulnerability Identification and Remediation

A development team has asked you to review the following three pseudocode snippets for security vulnerabilities. Perform a static analysis of each snippet without executing any code.

**Snippet A — User search function:**

```text
query = "SELECT * FROM users WHERE username = '" + request.getParam("user") + "'"
db.execute(query)
```

**Snippet B — File download handler:**

```text
filename = request.getParam("file")
filepath = "/var/www/downloads/" + filename
return readFile(filepath)
```

**Snippet C — Internal URL fetcher:**

```text
targetUrl = request.getParam("url")
response = httpClient.get(targetUrl)
return response.body
```

1. For each snippet, identify: the vulnerability type (using the correct SY0-701 term), the attack payload an attacker would submit to exploit it, and the CIA Triad property most at risk.
2. Rewrite each snippet in pseudocode with the correct defensive fix applied. For Snippet A use parameterized queries; for Snippet B validate and canonicalize the path; for Snippet C implement an allowlist of permitted domains.
3. For each snippet, classify the appropriate defensive control using both the Category axis (Physical/Technical/Administrative) and the Function axis (Preventive/Detective/Corrective/Deterrent/Compensating/Directive).
4. A security manager asks whether DAST testing would have caught all three vulnerabilities before deployment. For each snippet, explain whether DAST would or would not detect the vulnerability and why, referencing the specific limitation of DAST described in Module 03 Section 6.

### Reflection Questions

1. After completing both challenges, explain why the principle of "defense in depth" requires fixing the root cause vulnerability in application code even when compensating controls like WAFs and input filtering are in place. Use one specific example from Challenge 1 or Challenge 2 to illustrate your argument.
2. In Challenge 2, Snippet B contains a directory traversal vulnerability. A security engineer argues that the fix should be to block requests containing `../` sequences using a blacklist filter. Explain why a blacklist approach is insufficient as the sole defense against directory traversal, and describe what a correct allowlist-based path validation approach looks like in practice.

---

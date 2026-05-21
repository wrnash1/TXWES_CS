# Quiz: Module 05 - Vulnerability Scanning – Nessus and OpenVAS
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is it called when a vulnerability scanner reports a security issue that does not actually exist on the target system?
*   A) False Negative
*   B) False Positive
*   C) True Positive
*   D) Null Match
*   **Correct Answer:** B) False Positives occur when scanning rules mismatch background states and assume a vulnerability is present.
*   **Distractor Analysis:**
    *   *Why correct:* A false positive is a scanner alert for a vulnerability that does not actually exist — often caused by version-string matching without confirming exploitability, or by scanner logic errors on customized systems.
    *   *Why A is incorrect:* A false negative is the opposite — a real vulnerability exists but the scanner fails to detect it. This is equally dangerous but a different problem from reporting non-existent issues.
    *   *Why C is incorrect:* A true positive is a correctly identified, confirmed real vulnerability. This is the desired scanner outcome.
    *   *Why D is incorrect:* "Null match" is not a standard vulnerability scanning term. It has no definition in the context of scanner result classification.

---

**Question 2**
In vulnerability scanning, which of the following best defines **false positives versus false negatives** as scan quality metrics?
*   A) False positives are vulnerabilities a scanner reports that do not exist on the target; false negatives are real vulnerabilities the scanner misses. Both reduce the accuracy and usefulness of the assessment.
*   B) False positives occur when a credentialed scan finds more vulnerabilities than an uncredentialed scan of the same target.
*   C) False negatives are scanner alerts that require manual verification before they can be included in the final report.
*   D) False positives represent Critical-severity findings and false negatives represent Low-severity findings in the CVSS scoring model.
*   **Correct Answer:** A) False positives are vulnerabilities a scanner reports that do not exist on the target; false negatives are real vulnerabilities the scanner misses. Both reduce the accuracy and usefulness of the assessment.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the standard definition used in vulnerability scanning, IDS/IPS, and security assessment contexts. PT0-002 expects testers to understand both concepts and know that professional practice requires manually verifying findings to reduce false positives, and using credentialed scans to reduce false negatives.
    *   *Why B is incorrect:* The difference between credentialed and uncredentialed scan results is a real phenomenon, but it is not the definition of false positives. A credentialed scan finding more issues reflects greater scan depth, not false positives.
    *   *Why C is incorrect:* Scanner alerts requiring manual verification may include false positives, but the act of requiring verification is a workflow step — it is not the definition of a false negative.
    *   *Why D is incorrect:* CVSS severity levels (Critical, High, Medium, Low) are independent of false positive/negative classification. A finding can be a false positive at any severity level.

---

**Question 3**
A penetration tester is reviewing a Nessus scan report and notices a finding rated CVSS 9.8 on a public-facing web server. Which action best reflects professional vulnerability scanning practice?
*   A) Immediately exploit the vulnerability to demonstrate impact before writing it into the report.
*   B) Discard the finding — a CVSS score above 9.0 is likely a false positive since critical vulnerabilities are rare.
*   C) Manually verify the finding by confirming the vulnerable service version and checking whether a working exploit exists, then document it as confirmed or unconfirmed in the report.
*   D) Report the finding as confirmed Critical severity based solely on the scanner output without additional verification.
*   **Correct Answer:** C) Manually verify the finding by confirming the vulnerable service version and checking whether a working exploit exists, then document it as confirmed or unconfirmed in the report.
*   **Distractor Analysis:**
    *   *Why C is correct:* PT0-002 tests that scanners produce findings that require analyst judgment. A CVSS 9.8 finding demands manual verification to confirm exploitability before exploitation or reporting. Documenting the verification status (confirmed vs. potential) is professional practice.
    *   *Why A is incorrect:* Exploiting a vulnerability without verifying it and without authorization for exploitation (if exploitation is out of scope) violates the RoE. Even if exploitation is in scope, verification precedes exploitation.
    *   *Why B is incorrect:* High CVSS scores are not indicators of false positives. Critical vulnerabilities are genuinely common in unpatched systems. Discarding High/Critical findings without verification would be a dangerous oversight.
    *   *Why D is incorrect:* Reporting unverified scanner output as confirmed findings inflates risk assessments and damages credibility. Professional reports distinguish between scanner-identified and manually confirmed vulnerabilities.

---

**Question 4**
A vulnerability scanner is generating excessive false positive alerts on a network where an authorized security team regularly runs administrative tools that trigger IDS rules. What is the most effective action to address this?
*   A) Tune the scanner signatures to add exceptions for authorized administrative tool traffic and internal management IP addresses.
*   B) Switch from Nessus to OpenVAS, which produces fewer false positives by design.
*   C) Reduce the scan intensity from credentialed to uncredentialed mode to generate fewer alerts.
*   D) Reboot the scanning appliance and re-run the scan after clearing cached results.
*   **Correct Answer:** A) Tune the scanner signatures to add exceptions for authorized administrative tool traffic and internal management IP addresses.
*   **Distractor Analysis:**
    *   *Why A is correct:* False positives from known-good administrative activity are a standard scanner configuration challenge. The correct response is to create exception rules or exclusions for authorized traffic sources — this is analogous to IDS signature tuning and is standard scanner administration practice tested on PT0-002.
    *   *Why B is incorrect:* Nessus and OpenVAS do not have systematically different false positive rates by design. Both require configuration and tuning to reduce false positives in any specific environment.
    *   *Why C is incorrect:* Switching to uncredentialed scanning reduces scan depth and increases false negatives — it does not address false positives from administrative traffic detection.
    *   *Why D is incorrect:* Rebooting the scanner and re-running does not change the underlying signature logic that produces false positives. The same traffic will produce the same alerts.

---

**Question 5**
A tester running an uncredentialed vulnerability scan discovers a server that appears to be running an outdated, vulnerable version of Apache based on the HTTP banner. After manual verification, the server is actually running a patched version with the banner intentionally set to an old version string for deception. What type of scanner result is this?
*   A) True Positive — the scanner correctly identified a vulnerable service.
*   B) False Negative — the scanner missed a vulnerability that exists on the system.
*   C) False Positive — the scanner reported a vulnerability that does not actually exist on the target.
*   D) True Negative — the scanner correctly determined the service is not vulnerable.
*   **Correct Answer:** C) False Positive — the scanner reported a vulnerability that does not actually exist on the target.
*   **Distractor Analysis:**
    *   *Why C is correct:* The scanner reported a vulnerability (outdated Apache) based on the banner string, but manual verification confirmed the software is actually patched and not vulnerable. The report of a non-existent vulnerability is the textbook definition of a false positive. This scenario illustrates exactly why manual verification is essential.
    *   *Why A is incorrect:* A true positive requires that the vulnerability actually exist and be confirmed. Since the server is patched, the scanner's alert is incorrect.
    *   *Why B is incorrect:* A false negative would mean the server has a real vulnerability that the scanner failed to detect. In this scenario the server is not actually vulnerable — so this is not a false negative.
    *   *Why D is incorrect:* A true negative would mean the scanner found no vulnerability and the system is genuinely not vulnerable. The scanner did report a finding (incorrectly), so this is not a true negative.

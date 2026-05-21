# Reading Guide: Module 07 - Malware Analysis Fundamentals
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 07 - Malware Analysis Fundamentals**! This module covers how security analysts identify, classify, and analyze malicious software to understand attacker intent, capabilities, and indicators of compromise. You will learn how to perform static and dynamic malware analysis, interpret common malware behaviors, and extract actionable IOCs from samples. These topics are tested under **Domain 1: Security Operations (33%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn how to distinguish malware categories, use sandboxing tools for safe dynamic analysis, and correlate malware behaviors to ATT&CK techniques. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Static vs. Dynamic Malware Analysis**: Static analysis examines a malware sample without executing it — reviewing file headers, strings, imported functions, and code disassembly to understand capabilities without risk of infection. Dynamic analysis executes the malware in a controlled sandbox environment and observes its runtime behavior (registry changes, network connections, file drops). CySA+ exam questions test when each approach is appropriate and what each method can and cannot reveal.
*   **Sandboxing**: A sandboxed environment is an isolated, instrumented virtual machine used to safely execute suspected malware and record its behavior without risking production systems. Sandbox tools (e.g., Cuckoo Sandbox, Any.run) capture process activity, network traffic, file system changes, and API calls during execution. CySA+ tests sandboxing as the primary method for safe dynamic malware analysis.
*   **File Integrity Monitoring (FIM)**: FIM tools establish cryptographic baselines (SHA-256 hashes) of critical system files and alert when a file's hash changes unexpectedly — indicating unauthorized modification or malware-based file tampering. FIM is a key host-based detective control tested on CySA+ in the context of detecting persistence mechanisms and rootkit activity.

---

### 2. Certification Exam Tips
*   **Focus Area – Malware Categories (Domain 1):** CySA+ CS0-003 tests your ability to distinguish malware types by behavior: ransomware (encrypts files and demands payment), RAT (Remote Access Trojan — provides backdoor control), rootkit (hides its presence in the OS), keylogger (captures keystrokes), spyware (exfiltrates user data silently), and botnet agent (executes C2 commands). Know which behaviors are unique to each type.
*   **Scenario Trap – Static vs. Dynamic:** Static analysis is safe but incomplete — packed or obfuscated malware hides its true code until runtime. Dynamic analysis reveals true behavior but requires a sandbox. When a question asks how to analyze a suspicious file safely without executing it on a production system, dynamic analysis in a sandbox is the answer — not static analysis on a live workstation.
*   **Indicator Extraction:** CySA+ scenario questions ask what artifacts a malware analyst would extract from a sample. Know that static analysis produces: file hashes (MD5/SHA-256), embedded strings, import tables, and compiler artifacts. Dynamic analysis produces: C2 IP addresses and domains, registry keys created, files dropped, and mutex names.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist includes malware analysis concepts, sandbox interpretation, and IOC extraction scenarios mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource covers behavioral indicators and how they map to ATT&CK techniques.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Malware Analysis** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details malware categories, analysis methodologies, and IOC extraction techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Malware Analysis Fundamentals** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of sandbox analysis workflows and malware behavior interpretation.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a FIM utility path watchlist**: Using a FIM tool (e.g., Tripwire or AIDE), establish a hash baseline for a set of critical system files in a directory (e.g., `/etc/` on Linux or `C:\Windows\System32\` on Windows), then verify the baseline file is created and review its contents.
*   **Simulate an unauthorized file change in a monitored directory**: Modify a file within the FIM-monitored directory (e.g., append a line to a config file) and re-run the FIM integrity check to observe how the tool detects and reports the hash mismatch.
*   **Verify the alert in FIM logs and extract the IOC**: Review the FIM alert output to identify the affected file path, the original hash, the new hash, and the modification timestamp — document these as indicators of compromise that would be submitted to the SIEM.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Malware Analysis** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Malware Analysis Fundamentals** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the FIM configuration and sandbox analysis steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

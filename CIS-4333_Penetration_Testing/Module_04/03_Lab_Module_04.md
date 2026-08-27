# Lab Activity: Module 04 - Active Reconnaissance (Nmap)
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

## Objective
Configure and verify systems matching the operational parameters of **Active Reconnaissance (Nmap)**.

---

## Prerequisites
*   Ensure you have access to a terminal or a runtime environment matching the course requirements (e.g., Linux, macOS, Windows, or a cloud/web terminal).
*   Ensure you have administrative privileges if required to install packages or configure system services.

---

## Step-by-Step Instructions
1. **Perform a SYN scan: `nmap -sS target_ip`**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
2. **Identify open services and versions: `nmap -sV target_ip`**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
3. **Use basic vulnerability scan script: `nmap --script vuln target_ip`**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.

---

## Troubleshooting Guide
*   *Error:* `Permission Denied`
    * *Fix:* Remember to run administrative command sequences using `sudo` or execute with administrative privileges (e.g., Run as Administrator on Windows).
*   *Error:* `Command Not Found`
    * *Fix:* Verify your environmental path settings, or double-check if the utility package is installed.

---

## Deliverables
1. Document your completed steps with screenshots or terminal output logs showing successful execution.
2. Submit your completion report to your Canvas LMS assignment portal for grading.

---

## Part 9 — Challenge Exercise

### Challenge 1: Scan Comparison Analysis

Run the same authorized lab target using three different Nmap scan types: a SYN scan (`-sS`), a Connect scan (`-sT`), and a version detection scan (`-sV`). Save each output using `-oN` to separate text files. Then write a structured comparison documenting: which ports appeared in each scan, whether the results differed between scan types, how verbose each output was, and which scan type you would choose for a stealth-focused engagement versus a thoroughness-focused engagement. Include your reasoning based on the trade-offs covered in Module 04.

### Challenge 2: NSE Script Documentation Report

Select any two NSE scripts from categories other than `default` — for example one from `vuln` and one from `discovery`. For each script, document: the script name, its category, what it tests or collects, what a positive result indicates, and what a negative or absent result indicates. Then write a one-paragraph justification for when you would include each script in an authorized engagement and what RoE language would need to authorize its use.

### Reflection Questions

1. A colleague argues that `-T5` (Insane timing) should always be used to complete scans as fast as possible, saving engagement time. Using the concepts from Module 04, explain why this reasoning is flawed and describe a scenario where a slower timing template is the professional choice.
2. What is the ethical and legal significance of saving Nmap scan results to a file and storing them on your testing machine after an engagement concludes? Which pre-engagement document governs how long you may retain these results?

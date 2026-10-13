import urllib.request
import urllib.parse
import json
import ssl
import sys

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

COURSE_ID = 13090  # CIS-4328 Information Security
MODULE_ID = 87953  # Module 05: Cryptography and PKI

ctx = ssl.create_default_context()

def api_call(url, data=None, method="GET"):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    if data is not None:
        req.data = json.dumps(data).encode('utf-8')
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            content = resp.read().decode('utf-8')
            return json.loads(content) if content else {}
    except Exception as e:
        print(f"  ❌ API Error ({method} {url}): {e}")
        return None

# ==============================================================================
# HTML BUILDER: LAB 1 - STEGANOGRAPHY
# ==============================================================================
def build_stego_lab_html():
    return """
<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px;">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    <span style="font-size: 24px;">🖼️</span>
    <h2 style="margin: 0; color: #15803d; font-size: 18px;">
      STEGANOGRAPHY LAB QUICK-START &amp; SUBMISSION CHECKLIST
    </h2>
  </div>
  <p style="margin: 0 0 12px 0; font-size: 14px; color: #166534; line-height: 1.6;">
    In this hands-on lab, you will conceal a secret text message inside an image carrier file using steganography techniques. Follow the OS-specific instructions below for your operating system.
  </p>
  <div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; font-size: 13.5px; line-height: 1.7; color: #1e293b;">
    <strong>1. Required Deliverables (MANDATORY):</strong> You must submit at least <strong>THREE (3) files</strong> to this assignment:<br>
    &nbsp;&nbsp;• <strong>File 1: Original Picture</strong> (e.g., <code>original_image.jpg</code> or <code>.png</code>) — The unaltered cover image.<br>
    &nbsp;&nbsp;• <strong>File 2: Stego Picture</strong> (e.g., <code>stego_image.jpg</code> or <code>.png</code>) — The exact same image containing the hidden secret message.<br>
    &nbsp;&nbsp;• <strong>File 3: Lab Analysis Report</strong> (<code>.pdf</code> or <code>.docx</code>) — Containing your terminal/tool screenshots, extracted secret message verification, and answers to the analysis questions.<br>
    <strong>2. Operating Systems Supported:</strong> Step-by-step instructions are provided below for <strong>Windows</strong>, <strong>macOS</strong>, and <strong>Linux</strong>.<br>
    <strong>3. Due Date:</strong> Sunday, October 4, 2026 at 11:59 PM CST • <strong>Points:</strong> 100.0 Points
  </div>
  <div style="font-size: 12.5px; color: #166534;">
    💡 <em>Industry Mapping: CompTIA Security+ (SY0-701) Domain 2.0 (Security Architecture) • ISC2 CC Domain 4.0 (Network Security Obfuscation)</em>
  </div>
</div>

<div style="max-width: 950px; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.65;">

  <div style="background: linear-gradient(135deg, #1b365d 0%, #002855 100%); color: #ffffff; padding: 26px 30px; border-radius: 10px; margin-bottom: 24px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <span style="font-size: 12px; color: #d9a74a;">Texas Wesleyan University • Fall 2026</span>
      <span style="background: rgba(217, 167, 74, 0.2); border: 1px solid #d9a74a; color: #ffffff; padding: 3px 10px; border-radius: 20px; font-size: 11px;">Hands-On Security Lab</span>
    </div>
    <h1 style="color: #ffffff; margin: 0 0 6px 0; font-size: 22px;">Lab: Hands-On Steganography (Image Payload Embedding &amp; Extraction)</h1>
    <div style="font-size: 15px; color: #e2e8f0;">CIS-4328 Information Security • Module 05 Practical Lab</div>
  </div>

  <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 28px 32px; margin-bottom: 24px;">
    <h3 style="color: #1b365d; margin-top: 0;">🎯 Lab Overview &amp; Learning Objectives</h3>
    <p>
      <strong>Steganography</strong> is the practice of concealing a secret message, file, or data stream within another ordinary, non-secret file or medium to hide the fact that communication is taking place. Unlike cryptography (which scrambles data so that unauthorized parties cannot read it), steganography conceals the very existence of the data.
    </p>
    <p>By completing this lab, you will:</p>
    <ul>
      <li>Understand Least Significant Bit (LSB) insertion and file concatenation techniques.</li>
      <li>Conceal an authenticated text payload within a carrier image file.</li>
      <li>Extract and verify the hidden payload from the steganographic medium.</li>
      <li>Perform forensic steganalysis comparing file hashes, binary structures, and visual fidelity.</li>
    </ul>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">📋 Phase 1: Preparation (All Operating Systems)</h3>
    <ol>
      <li>Create a dedicated lab working folder on your machine: <code>stego_lab</code>.</li>
      <li>Find or take a clear photo/image (JPEG or PNG format) and save it in your folder as <code>original_image.jpg</code>. (Make sure this original image is kept unmodified).</li>
      <li>Create a text file named <code>secret.txt</code> containing the following confidential payload:
        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-left: 4px solid #1b365d; padding: 12px 16px; font-family: monospace; font-size: 13px; margin: 10px 0;">
          CONFIDENTIAL SECURITY BRIEFING<br>
          Student Name: [Your Full Name]<br>
          Student ID: [Your Student ID]<br>
          Course: CIS-4328 Information Security<br>
          Flag: TXWES-STEGO-CRYPT-{YourInitials}-2026<br>
          Timestamp: [Current Date and Time]
        </div>
      </li>
    </ol>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">💻 Phase 2: Operating System Instructions</h3>
    <p>Select the instructions corresponding to your computer's operating system below:</p>

    <!-- WINDOWS INSTRUCTIONS -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
      <h4 style="color: #0284c7; margin-top: 0; display: flex; align-items: center; gap: 8px;">
        <span>🪟</span> OPTION A: Windows Instructions
      </h4>
      <p><strong>Method 1: Built-in Command Prompt (Binary File Appending — No Installation Required)</strong></p>
      <ol>
        <li>Open <strong>Command Prompt (cmd.exe)</strong> and navigate to your lab folder:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">cd C:\path\to\stego_lab</pre>
        </li>
        <li>Combine the cover image and secret message into a new stego image using the binary copy command:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">copy /b original_image.jpg + secret.txt stego_image.jpg</pre>
        </li>
        <li><strong>Verification &amp; Extraction:</strong>
          <ul>
            <li>Double-click <code>stego_image.jpg</code>. Notice that Windows Photo Viewer opens and displays the image completely normally with zero visual distortion!</li>
            <li>Right-click <code>stego_image.jpg</code> &rarr; <em>Open with</em> &rarr; <strong>Notepad</strong> (or run <code>type stego_image.jpg | more</code> in CMD). Scroll to the very bottom of the file in Notepad: your plaintext secret message appears preserved after the JPEG End-Of-Image (EOI <code>0xFFD9</code>) marker!</li>
            <li>Take a clear screenshot of the Notepad view displaying the secret message at the end of the image file.</li>
          </ul>
        </li>
      </ol>

      <p><strong>Method 2: OpenStego GUI (Advanced LSB Embedding — Cross-Platform)</strong></p>
      <ol>
        <li>Download the free, open-source tool <strong>OpenStego</strong> (<a href="https://www.openstego.com/" target="_blank" rel="noopener">https://www.openstego.com/</a>) or run <code>openstego.bat</code>.</li>
        <li>Under <strong>Data Hiding</strong>:
          <ul>
            <li><strong>Message File:</strong> Browse and select <code>secret.txt</code>.</li>
            <li><strong>Cover File:</strong> Browse and select <code>original_image.png</code> (or <code>.bmp</code>).</li>
            <li><strong>Output Stego File:</strong> Set destination as <code>stego_image.png</code>.</li>
            <li><strong>Password:</strong> Enter a strong passphrase (e.g., <code>RamSecurity2026!</code>).</li>
          </ul>
        </li>
        <li>Click <strong>Hide Data</strong>. Then switch to the <strong>Extract Data</strong> tab to extract the message using your password to prove non-repudiation.</li>
      </ol>
    </div>

    <!-- MACOS INSTRUCTIONS -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
      <h4 style="color: #64748b; margin-top: 0; display: flex; align-items: center; gap: 8px;">
        <span>🍎</span> OPTION B: macOS Instructions
      </h4>
      <p><strong>Method 1: Native Terminal &amp; String Extraction (No Installation Required)</strong></p>
      <ol>
        <li>Open <strong>Terminal</strong> (Press <code>Cmd + Space</code>, type <code>Terminal</code>, press Enter) and navigate to your lab directory:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">cd ~/Documents/stego_lab</pre>
        </li>
        <li>Concatenate the secret payload to the end of the original image:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">cat original_image.jpg secret.txt &gt; stego_image.jpg</pre>
        </li>
        <li><strong>Verification &amp; Extraction:</strong>
          <ul>
            <li>Open the image in macOS Preview: <code>open stego_image.jpg</code>. The image renders flawlessly without any visual anomalies.</li>
            <li>Extract the concealed message using the native macOS binary strings utility:
              <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">strings stego_image.jpg | tail -n 12</pre>
            </li>
            <li>Observe your confidential briefing and flag displayed directly in the terminal output! Take a screenshot.</li>
          </ul>
        </li>
      </ol>

      <p><strong>Method 2: Steghide or OpenStego (via Homebrew)</strong></p>
      <ol>
        <li>If you have Homebrew installed, install steghide or download OpenStego for macOS:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">brew install steghide</pre>
        </li>
        <li>Embed: <code>steghide embed -cf original_image.jpg -ef secret.txt -sf stego_image.jpg -p "RamSecurity2026!"</code></li>
        <li>Extract: <code>steghide extract -sf stego_image.jpg -p "RamSecurity2026!"</code></li>
      </ol>
    </div>

    <!-- LINUX INSTRUCTIONS -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
      <h4 style="color: #ea580c; margin-top: 0; display: flex; align-items: center; gap: 8px;">
        <span>🐧</span> OPTION C: Linux Instructions (Ubuntu / Debian / Kali)
      </h4>
      <p><strong>Method 1: Steghide (Industry Standard Cybersecurity Tool)</strong></p>
      <ol>
        <li>Open terminal and install steghide:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">sudo apt update &amp;&amp; sudo apt install -y steghide</pre>
        </li>
        <li>Embed the secret message into the cover image with a passphrase:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">steghide embed -cf original_image.jpg -ef secret.txt -sf stego_image.jpg -p "RamSecurity2026!"</pre>
        </li>
        <li>Inspect the stego image info (proving the presence of embedded data):
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">steghide info stego_image.jpg</pre>
        </li>
        <li>Extract the hidden message to a new file:
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">steghide extract -sf stego_image.jpg -p "RamSecurity2026!"</pre>
        </li>
        <li>Verify extracted content: <code>cat secret.txt</code>. Take a screenshot showing embedding, info, and extraction.</li>
      </ol>

      <p><strong>Method 2: Native Linux Coreutils (No Tool Installation)</strong></p>
      <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">cat original_image.jpg secret.txt &gt; stego_image.jpg
strings stego_image.jpg | grep -A 5 "CONFIDENTIAL"</pre>
    </div>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">🔬 Phase 3: Analytical Comparison &amp; Questions</h3>
    <p>In your written report, answer the following security analysis questions:</p>
    <ol>
      <li><strong>File Size Comparison:</strong> Record the exact file size (in bytes) of <code>original_image.jpg</code>, <code>secret.txt</code>, and <code>stego_image.jpg</code>. How does the size of the stego image relate mathematically to the other two files?</li>
      <li><strong>Hash Digest Comparison:</strong> Run a SHA-256 hash on both <code>original_image.jpg</code> and <code>stego_image.jpg</code>. Record both hashes. Did the hash change? Why?</li>
      <li><strong>Visual Fidelity:</strong> Open both images side-by-side. Can you discern any visual difference with the human eye? Why is image compression (e.g. JPEG lossy vs. PNG lossless) critical when designing steganographic channels?</li>
      <li><strong>Steganalysis &amp; Threat Detection:</strong> If you are a SOC Analyst investigating data exfiltration by a malicious insider, what security controls or tools (e.g. DLP, statistical chi-square steganalysis) could detect steganography across network boundaries?</li>
    </ol>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">📤 Submission Checklist</h3>
    <table style="width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13.5px;">
      <thead>
        <tr style="background: #f1f5f9;">
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">File Name</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">Description</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">Points</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><code>original_image.jpg</code></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;">Clean, original unmodified cover photo</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">25 Pts</td>
        </tr>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><code>stego_image.jpg</code></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;">Carrier photo with embedded confidential payload</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">35 Pts</td>
        </tr>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><code>Steganography_Lab_Report.pdf</code></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;">Screenshots of CLI/tool execution, extraction verification, and answers to the 4 analysis questions</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">40 Pts</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# HTML BUILDER: LAB 2 - FILE INTEGRITY & HASH VERIFICATION
# ==============================================================================
def build_hash_lab_html():
    return """
<div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px;">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    <span style="font-size: 24px;">🔐</span>
    <h2 style="margin: 0; color: #1d4ed8; font-size: 18px;">
      FILE HASH VERIFICATION LAB QUICK-START &amp; SUBMISSION CHECKLIST
    </h2>
  </div>
  <p style="margin: 0 0 12px 0; font-size: 14px; color: #1e3a8a; line-height: 1.6;">
    In this hands-on lab, you will generate cryptographic hash marks for a file, modify the file's contents, and recheck the hashes to observe and analyze cryptographic integrity and the <strong>Avalanche Effect</strong>.
  </p>
  <div style="background: white; border: 1px solid #bfdbfe; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; font-size: 13.5px; line-height: 1.7; color: #1e293b;">
    <strong>1. Required Deliverable:</strong> Submit a completed <strong>Lab Analysis Report (.pdf or .docx)</strong> containing your baseline and modified hash comparison table, terminal output screenshots showing commands executed, and security analysis answers.<br>
    <strong>2. Operating Systems Supported:</strong> Step-by-step commands are provided below for <strong>Windows (PowerShell &amp; CMD)</strong>, <strong>macOS (Terminal)</strong>, and <strong>Linux (Bash)</strong>.<br>
    <strong>3. Due Date:</strong> Sunday, October 4, 2026 at 11:59 PM CST • <strong>Points:</strong> 100.0 Points
  </div>
  <div style="font-size: 12.5px; color: #1e3a8a;">
    💡 <em>Industry Mapping: CompTIA Security+ (SY0-701) Domain 2.0 (Cryptographic Solutions) • CompTIA CySA+ (CS0-003) Software Integrity &amp; Digital Forensics • ISC2 CC Domain 4.0</em>
  </div>
</div>

<div style="max-width: 950px; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.65;">

  <div style="background: linear-gradient(135deg, #1b365d 0%, #002855 100%); color: #ffffff; padding: 26px 30px; border-radius: 10px; margin-bottom: 24px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <span style="font-size: 12px; color: #d9a74a;">Texas Wesleyan University • Fall 2026</span>
      <span style="background: rgba(217, 167, 74, 0.2); border: 1px solid #d9a74a; color: #ffffff; padding: 3px 10px; border-radius: 20px; font-size: 11px;">Hands-On Security Lab</span>
    </div>
    <h1 style="color: #ffffff; margin: 0 0 6px 0; font-size: 22px;">Lab: Cryptographic File Integrity &amp; Hash Verification</h1>
    <div style="font-size: 15px; color: #e2e8f0;">CIS-4328 Information Security • Module 05 Practical Lab</div>
  </div>

  <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 28px 32px; margin-bottom: 24px;">
    <h3 style="color: #1b365d; margin-top: 0;">🎯 Lab Overview &amp; Learning Objectives</h3>
    <p>
      A <strong>cryptographic hash function</strong> is a one-way mathematical algorithm that maps variable-length input data into a fixed-length string of hexadecimal characters (the hash digest). Cryptographic hashes are fundamental to information security: they guarantee <strong>integrity</strong> (detecting accidental corruption or malicious tampering) and support digital signatures and non-repudiation.
    </p>
    <p>A key property of cryptographic hashes is the <strong>Avalanche Effect</strong>: if even a single bit in the input file changes, the resulting hash digest changes completely and unpredictably.</p>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">💻 Step-by-Step Instructions by Operating System</h3>

    <!-- WINDOWS POWERSHELL / CMD -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
      <h4 style="color: #0284c7; margin-top: 0; display: flex; align-items: center; gap: 8px;">
        <span>🪟</span> OPTION A: Windows Instructions (PowerShell / Command Prompt)
      </h4>
      <p>Open <strong>Windows PowerShell</strong> and perform the following sequence:</p>
      <ol>
        <li><strong>Step 1: Create the Original File</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">Set-Content -Path integrity_test.txt -Value "Texas Wesleyan University Information Security Department - CIS4328"</pre>
        </li>
        <li><strong>Step 2: Generate Baseline Hashes (SHA-256, MD5, SHA-1)</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">Get-FileHash -Algorithm SHA256 integrity_test.txt | Format-List
Get-FileHash -Algorithm MD5 integrity_test.txt | Format-List
Get-FileHash -Algorithm SHA1 integrity_test.txt | Format-List</pre>
          <em>(Alternative using CMD: <code>certutil -hashfile integrity_test.txt SHA256</code>)</em><br>
          Record these three hashes in your report table and capture a screenshot.
        </li>
        <li><strong>Step 3: Modify the File (Simulate Data Tampering)</strong>
          <p>Add a single period (<code>.</code>) or character to the end of the file:</p>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">Add-Content -Path integrity_test.txt -Value "."</pre>
        </li>
        <li><strong>Step 4: Recheck and Compare Hashes</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">Get-FileHash -Algorithm SHA256 integrity_test.txt | Format-List
Get-FileHash -Algorithm MD5 integrity_test.txt | Format-List</pre>
          Capture a screenshot of the new hashes. Notice that the entire hash digest changed drastically despite only adding one character!
        </li>
      </ol>
    </div>

    <!-- MACOS TERMINAL -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
      <h4 style="color: #64748b; margin-top: 0; display: flex; align-items: center; gap: 8px;">
        <span>🍎</span> OPTION B: macOS Instructions (Terminal)
      </h4>
      <p>Open <strong>Terminal</strong> and execute the following commands:</p>
      <ol>
        <li><strong>Step 1: Create the Original File</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">echo "Texas Wesleyan University Information Security Department - CIS4328" &gt; integrity_test.txt</pre>
        </li>
        <li><strong>Step 2: Generate Baseline Hashes</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">shasum -a 256 integrity_test.txt
md5 integrity_test.txt
shasum -a 1 integrity_test.txt</pre>
          Record the hexadecimal values in your report table and take a screenshot.
        </li>
        <li><strong>Step 3: Modify the File</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">echo "!" &gt;&gt; integrity_test.txt</pre>
        </li>
        <li><strong>Step 4: Recheck Hashes</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">shasum -a 256 integrity_test.txt
md5 integrity_test.txt</pre>
          Take a screenshot of the output. Observe the Avalanche Effect in action.
        </li>
      </ol>
    </div>

    <!-- LINUX TERMINAL -->
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
      <h4 style="color: #ea580c; margin-top: 0; display: flex; align-items: center; gap: 8px;">
        <span>🐧</span> OPTION C: Linux Instructions (Ubuntu / Debian / Kali)
      </h4>
      <p>Open your bash shell and execute:</p>
      <ol>
        <li><strong>Step 1: Create Original File</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">echo "Texas Wesleyan University Information Security Department - CIS4328" &gt; integrity_test.txt</pre>
        </li>
        <li><strong>Step 2: Generate Baseline Hashes &amp; Save Manifest</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">sha256sum integrity_test.txt &gt; baseline_sha256.txt
md5sum integrity_test.txt &gt; baseline_md5.txt
cat baseline_sha256.txt
cat baseline_md5.txt</pre>
        </li>
        <li><strong>Step 3: Verify Integrity with the <code>-c</code> (Check) Flag</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">sha256sum -c baseline_sha256.txt</pre>
          <em>Output will state: <code>integrity_test.txt: OK</code></em>
        </li>
        <li><strong>Step 4: Modify File and Re-verify</strong>
          <pre style="background: #1e293b; color: #f8fafc; padding: 10px 14px; border-radius: 6px; font-family: monospace; font-size: 13px;">echo "Tampered" &gt;&gt; integrity_test.txt
sha256sum -c baseline_sha256.txt</pre>
          <em>Notice that the checksum validation now outputs: <code>integrity_test.txt: FAILED</code> and <code>sha256sum: WARNING: 1 computed checksum did NOT match</code>.</em>
          Take a screenshot of both the OK and FAILED outputs.
        </li>
      </ol>
    </div>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">📊 Phase 2: Hash Comparison Matrix</h3>
    <p>Include the following completed table in your submitted lab report:</p>
    <table style="width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13.5px;">
      <thead>
        <tr style="background: #f1f5f9;">
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">Algorithm</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">Digest Bit Length</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">Original File Hash</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">Modified File Hash</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><strong>MD5</strong></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">128 bits (32 hex chars)</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-family: monospace; font-size: 12px;">[Paste Original MD5]</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-family: monospace; font-size: 12px;">[Paste Modified MD5]</td>
        </tr>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><strong>SHA-1</strong></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">160 bits (40 hex chars)</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-family: monospace; font-size: 12px;">[Paste Original SHA-1]</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-family: monospace; font-size: 12px;">[Paste Modified SHA-1]</td>
        </tr>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><strong>SHA-256</strong></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">256 bits (64 hex chars)</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-family: monospace; font-size: 12px;">[Paste Original SHA-256]</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-family: monospace; font-size: 12px;">[Paste Modified SHA-256]</td>
        </tr>
      </tbody>
    </table>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">🔬 Phase 3: Security Analyst Critical Thinking Questions</h3>
    <ol>
      <li><strong>The Avalanche Effect:</strong> Define the cryptographic concept of the Avalanche Effect. Looking at your SHA-256 output, how many hexadecimal characters remained identical between the original and modified files?</li>
      <li><strong>Collision Vulnerabilities:</strong> Why are MD5 and SHA-1 deprecated for digital certificates and high-security integrity checks? Research and briefly explain what a <em>hash collision attack</em> is (e.g. the SHAttered collision attack on SHA-1).</li>
      <li><strong>Digital Forensics &amp; Chain of Custody:</strong> In a criminal cyber investigation, why does a digital forensics investigator compute the cryptographic hash of a suspect hard drive image immediately upon acquisition? What would happen in court if the hash at trial does not match the acquisition hash?</li>
      <li><strong>Software Supply Chain Security:</strong> When you download an ISO or security tool (like Kali Linux or Wireshark), the vendor publishes a SHA-256 checksum on their website. How does calculating <code>Get-FileHash</code> or <code>sha256sum</code> before running the installer protect you against a Man-in-the-Middle (MitM) attack?</li>
    </ol>

    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;">

    <h3 style="color: #1b365d;">📤 Submission Checklist</h3>
    <table style="width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13.5px;">
      <thead>
        <tr style="background: #f1f5f9;">
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">Section</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;">Requirement</th>
          <th style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">Points</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><strong>Hash Comparison Matrix</strong></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;">Complete table containing MD5, SHA-1, and SHA-256 hashes for both original and modified files</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">30 Pts</td>
        </tr>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><strong>Terminal Screenshots</strong></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;">Clear screenshots showing commands run and output on your operating system (Windows, Mac, or Linux)</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">30 Pts</td>
        </tr>
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;"><strong>Analyst Questions</strong></td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px;">Thorough, professional answers to the 4 critical thinking questions</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; text-align: center;">40 Pts</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

def main():
    print("=" * 80)
    print("DEPLOYING HANDS-ON SECURITY LABS TO CIS-4328")
    print("=" * 80)

    # 1. Fetch Assignment Group for Labs
    groups = api_call(f"{API_BASE}/courses/{COURSE_ID}/assignment_groups")
    lab_group = next((g for g in groups if "lab" in g.get("name", "").lower()), None)
    lab_group_id = lab_group.get("id") if lab_group else None
    print(f"Target Assignment Group: '{lab_group.get('name') if lab_group else 'Default'}' (ID: {lab_group_id})")

    due_date = "2026-10-05T04:59:00Z"  # Sunday Oct 4, 2026 11:59 PM CDT

    # 2. Deploy Lab 1: Steganography
    print("\n--- Deploying Lab: Steganography (Image Payload Embedding & Extraction) ---")
    stego_payload = {
        "assignment": {
            "name": "Lab: Hands-On Steganography (Image Payload Embedding & Extraction)",
            "description": build_stego_lab_html(),
            "points_possible": 100.0,
            "grading_type": "points",
            "submission_types": ["online_upload"],
            "allowed_extensions": ["png", "jpg", "jpeg", "bmp", "pdf", "docx", "zip"],
            "due_at": due_date,
            "assignment_group_id": lab_group_id,
            "published": True
        }
    }
    stego_assign = api_call(f"{API_BASE}/courses/{COURSE_ID}/assignments", data=stego_payload, method="POST")
    stego_id = stego_assign.get("id")
    print(f"  ✅ Created Steganography Assignment (ID: {stego_id})")

    # Link in Module 05
    stego_mod_item = {
        "module_item": {
            "title": "Lab: Hands-On Steganography (Image Payload Embedding & Extraction)",
            "type": "Assignment",
            "content_id": stego_id,
            "position": 5
        }
    }
    api_call(f"{API_BASE}/courses/{COURSE_ID}/modules/{MODULE_ID}/items", data=stego_mod_item, method="POST")
    print(f"  ✅ Linked Steganography Lab in Module {MODULE_ID}")

    # 3. Deploy Lab 2: File Hash Verification
    print("\n--- Deploying Lab: Cryptographic File Integrity & Hash Verification ---")
    hash_payload = {
        "assignment": {
            "name": "Lab: Cryptographic File Integrity & Hash Verification",
            "description": build_hash_lab_html(),
            "points_possible": 100.0,
            "grading_type": "points",
            "submission_types": ["online_upload"],
            "allowed_extensions": ["pdf", "docx"],
            "due_at": due_date,
            "assignment_group_id": lab_group_id,
            "published": True
        }
    }
    hash_assign = api_call(f"{API_BASE}/courses/{COURSE_ID}/assignments", data=hash_payload, method="POST")
    hash_id = hash_assign.get("id")
    print(f"  ✅ Created Hash Verification Assignment (ID: {hash_id})")

    # Link in Module 05
    hash_mod_item = {
        "module_item": {
            "title": "Lab: Cryptographic File Integrity & Hash Verification",
            "type": "Assignment",
            "content_id": hash_id,
            "position": 6
        }
    }
    api_call(f"{API_BASE}/courses/{COURSE_ID}/modules/{MODULE_ID}/items", data=hash_mod_item, method="POST")
    print(f"  ✅ Linked Hash Verification Lab in Module {MODULE_ID}")

    print("\n" + "="*80)
    print("✅ BOTH HANDS-ON LABS SUCCESSFULLY DEPLOYED AND LINKED IN MODULE 05!")
    print("="*80)

if __name__ == "__main__":
    main()

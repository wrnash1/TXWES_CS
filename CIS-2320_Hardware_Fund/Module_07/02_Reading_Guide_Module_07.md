# Reading Guide: Module 07 - Display Technologies and Connectors
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 07 - Display Technologies and Connectors**! This module covers the display panel technologies used in modern monitors and laptops, the video connector standards used to carry signals from GPU to display, and the resolution and refresh rate specifications that define image quality. These topics appear on the **CompTIA A+ Core 1 (220-1101)** exam under hardware and display troubleshooting.

As a technician you must be able to select the right cable for a display connection, identify connector types by appearance, and advise users on resolution and refresh rate settings. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **OLED vs LCD (IPS, TN, VA)**: LCD (Liquid Crystal Display) panels require a backlight and use liquid crystals to control light transmission. IPS (In-Plane Switching) LCDs offer wide viewing angles and accurate color but have slower response times; TN (Twisted Nematic) panels have the fastest response times (~1ms) and are preferred for competitive gaming; VA (Vertical Alignment) panels deliver deep contrast ratios between IPS and TN. OLED (Organic Light-Emitting Diode) displays emit light per-pixel, achieving true blacks, infinite contrast ratios, and fast response times, but are susceptible to burn-in on static content.
*   **HDMI vs DisplayPort vs DVI**: HDMI (High-Definition Multimedia Interface) carries both video and audio over a single cable and is the most common consumer display connector; HDMI 2.1 supports 4K@120Hz and 8K. DisplayPort is preferred for PC monitors, supports higher refresh rates, and uniquely enables daisy-chaining multiple monitors via Multi-Stream Transport (MST). DVI (Digital Visual Interface) is a legacy connector found on older monitors and graphics cards; DVI-D carries digital signal only, DVI-I carries both digital and analog. VGA is fully analog and is largely obsolete.
*   **resolution and refresh rates**: Resolution defines the number of pixels displayed (width × height); common standards are 1920×1080 (1080p/FHD), 2560×1440 (1440p/QHD), and 3840×2160 (4K/UHD). Refresh rate is the number of times per second the display updates its image, measured in Hz; 60Hz is standard, 144Hz and 240Hz are common for gaming. Higher resolution requires more GPU power; higher refresh rate requires more GPU frames-per-second output to be beneficial.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 1.1 and 3.1):** The A+ exam tests display connector identification and compatibility. Know that HDMI and DisplayPort are the two current-standard connectors; DVI and VGA are legacy. A common scenario question describes a new monitor with only DisplayPort input connected to an older GPU with only HDMI output — the answer involves a DisplayPort-to-HDMI adapter or cable.
*   **Scenario Trap:** Watch for questions about display daisy-chaining. Only DisplayPort (via MST) natively supports daisy-chaining multiple monitors from one output port. HDMI does not support daisy-chaining. The exam will offer HDMI as a distractor in daisy-chain scenarios — always select DisplayPort.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers display technologies and connectors with visual connector identification guides. Navigate to the display section: [Professor Messer's CompTIA A+ Core 1 Course — Display Technologies](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Focus on connector comparison and the IPS/TN/VA panel type comparisons.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the display technology and connector sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on display types, video connectors, resolution, and refresh rates.
*   **Required Video:** Watch the video lecture on display technologies and connectors from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on the connector identification segments and panel technology comparisons.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure dual-monitor setup using display settings**: Connect two monitors to a PC using available video outputs. Open Display Settings (Windows) and configure the second monitor as an extended display. Set each monitor's resolution to its native recommended value.
*   **Identify pins and keyings of DisplayPort vs HDMI cables**: Physically examine a DisplayPort cable (20-pin, one angled corner) and an HDMI cable (19-pin, trapezoidal). Note the connector shapes and document which end connects to the GPU and which to the monitor.
*   **Switch display input settings on physical monitor**: Using the monitor's OSD (On-Screen Display) menu buttons, navigate to the Input Source setting and manually switch between HDMI and DisplayPort inputs to confirm both signal sources are detected correctly.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the display technology and connector sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on display technologies and connectors in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the lab configuration steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

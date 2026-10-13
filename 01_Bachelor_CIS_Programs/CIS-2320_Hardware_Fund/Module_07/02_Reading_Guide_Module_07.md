# Reading Guide: Module 07 - Display Technologies and Connectors

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2320 &BULL; HARDWARE FUNDAMENTALS & PC ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Certification Domain:** 1.1 — Install and configure laptop hardware | 3.1 — Install and configure storage devices and display components

---

### Introduction

Welcome to Module 07 — Display Technologies and Connectors. This module covers the display panel technologies used in modern monitors and laptops, the video connector standards used to carry signals from GPU to display, and the resolution and refresh rate specifications that define image quality. These topics appear on the CompTIA A+ Core 1 (220-1101) exam under hardware configuration and troubleshooting scenarios.

As a technician you must be able to identify connector types by physical appearance, explain which cable version supports a given resolution and refresh rate combination, advise users on panel technology trade-offs, and configure multi-monitor setups. Complete the study checklist and review all glossary terms before beginning the lab.

---

### Section 1: High-Yield Glossary

Review these definitions carefully. The certification exam expects you to recognize and apply all of these terms.

**LCD (Liquid Crystal Display):** A flat-panel display technology that modulates a backlight using a layer of liquid crystals to produce an image. The liquid crystals do not emit light — they control how much backlight passes through. Modern LCDs use LED backlighting. The three main LCD subtypes — TN, IPS, and VA — differ in crystal alignment, which affects viewing angles, response time, and color accuracy.

**TN (Twisted Nematic) Panel:** The oldest and fastest LCD panel subtype. TN crystals twist to control light transmission. Advantages: response times as low as 1ms, typically the lowest-cost panel type. Disadvantages: narrow viewing angles (colors and contrast shift noticeably when viewed from the side or top) and less accurate color reproduction. Primarily used in competitive gaming monitors where response time is the dominant requirement.

**IPS (In-Plane Switching) Panel:** An LCD subtype in which liquid crystals align parallel to the display surface. Advantages: wide viewing angles (approximately 178 degrees horizontal and vertical), highly accurate color reproduction (suitable for photo editing and professional work), better color consistency across the viewing angle. Disadvantages: traditionally slower response times (4–8ms) than TN, though modern IPS panels have improved significantly. Slightly higher cost than TN.

**VA (Vertical Alignment) Panel:** An LCD subtype in which crystals align perpendicular to the panel when off, blocking backlight completely to produce deep blacks. Advantages: high native contrast ratios (3,000:1 to 8,000:1), deep blacks, good color for media consumption. Disadvantages: slower pixel response times than TN and some IPS panels, potential for ghosting in fast motion. Viewing angles are better than TN but not as wide as IPS.

**OLED (Organic Light-Emitting Diode):** A display technology in which each pixel is individually self-illuminating — no backlight is needed. An organic compound emits light when current is applied. When a pixel displays black, it is simply turned off, producing true zero-emission black and effectively infinite contrast ratio. Advantages: true black, infinite contrast, very fast response times, wide viewing angles, thin construction. Disadvantages: susceptibility to burn-in (static images can permanently degrade individual pixel compounds over time), higher cost per inch than LCD.

**Burn-in:** A permanent image artifact on an OLED display caused by prolonged display of a static high-brightness element. The organic compounds in overworked pixels degrade faster than neighboring pixels, leaving a faint, permanent ghost of the static image. Common burn-in sources: always-visible taskbars, application menu bars, game HUDs, and channel logos on TVs. OLED burn-in is irreversible; mitigation strategies include using screen savers, enabling pixel-shift features, and reducing peak brightness.

**Refresh Rate:** The number of times per second a display redraws its image, measured in Hz. At 60Hz the display updates 60 times per second; at 144Hz it updates 144 times per second. Higher refresh rates produce smoother motion, particularly in gaming. To achieve the benefit of a high-refresh-rate display, the GPU must output the corresponding number of frames per second. A 144Hz display showing only 60 fps of GPU output will not deliver 144Hz smoothness.

**Resolution:** The number of individual pixels that compose the display image, expressed as width x height. Common standards: 1920x1080 (1080p, FHD — 2.07 million pixels), 2560x1440 (1440p, QHD — 3.69 million pixels), 3840x2160 (4K, UHD — 8.29 million pixels). Higher resolution requires more GPU processing power to render and more cable bandwidth to transmit.

**HDMI (High-Definition Multimedia Interface):** The most widely deployed consumer video and audio connector standard. A full-size HDMI Type A connector has 19 pins and a distinctive trapezoidal shape. HDMI carries both video and audio over a single cable. Key versions: HDMI 1.4 (max 4K@30Hz), HDMI 2.0 (max 4K@60Hz), HDMI 2.1 (max 4K@120Hz, 8K@60Hz). Mini HDMI (Type C) and Micro HDMI (Type D) are smaller variants for tablets and cameras. HDMI does not support MST daisy-chaining.

**DisplayPort:** A digital display connector standard designed for PC monitors. The connector has 20 pins and one distinctively angled corner that prevents incorrect insertion. DisplayPort supports both video and audio. Its key advantage over HDMI for PC use is higher bandwidth and support for Multi-Stream Transport (MST), which allows one DisplayPort output to drive multiple independent displays via daisy-chaining or an MST hub. Key versions: DisplayPort 1.4 (25.92 Gbps, supports 4K@144Hz), DisplayPort 2.0 (77.4 Gbps, supports 4K@240Hz and beyond).

**MST (Multi-Stream Transport):** A DisplayPort feature that allows a single DisplayPort output to carry multiple independent video streams simultaneously. MST enables daisy-chaining — connecting a second monitor to the first monitor's DisplayPort output — or using a dedicated MST hub to split one DP connection into multiple DP outputs. HDMI does not support MST. MST is the correct answer on the A+ exam for any multi-monitor-from-one-port scenario.

**DVI (Digital Visual Interface):** A legacy video connector found on older monitors and graphics cards. DVI carries video only — no audio. Three subtypes: DVI-D (digital signal only; the four-pin analog cross-cluster is absent), DVI-I (digital and analog signals; the four-pin cross-cluster is present), and DVI-A (analog only, rarely encountered). DVI-D can be adapted to HDMI with a passive adapter because both carry digital signals. DVI-I can be adapted to VGA with a passive adapter because DVI-I carries the analog signal VGA requires. DVI-D cannot be passively adapted to VGA.

**VGA (Video Graphics Array):** A legacy 15-pin three-row analog video connector, typically colored blue. VGA carries analog video only — no audio, no digital signal. Because VGA is analog, signal quality degrades with cable length and VGA cannot carry 4K resolutions. Still encountered on projectors, older monitors, and legacy enterprise displays. A VGA signal can be generated from a DVI-I port via a passive adapter but requires an active adapter from a DVI-D or DisplayPort source.

**Native Resolution:** The resolution at which a monitor's pixel grid exactly matches the signal resolution, producing the sharpest possible image with no scaling artifacts. A 1920x1080 monitor's native resolution is 1920x1080. Displaying a non-native resolution requires the monitor's internal scaler to upscale or downscale the image, which introduces softening or distortion.

**Response Time:** The time in milliseconds (ms) it takes a pixel to transition from one color to another. Lower response times reduce motion blur and ghosting in fast-moving content. TN panels typically achieve 1ms; IPS panels 4–8ms (faster panels now reach 1–4ms); VA panels 4–10ms. Response time is a display panel characteristic, not a cable characteristic.

**Adaptive Sync (G-Sync / FreeSync):** A display synchronization technology that dynamically matches the monitor's refresh rate to the GPU's frame output rate, eliminating screen tearing. NVIDIA G-Sync and AMD FreeSync are the two primary implementations. Both require a DisplayPort connection for full functionality on most implementations, though HDMI support has expanded in recent generations.

---

### Section 2: Panel Technology Comparison Table

| Feature | TN | IPS | VA | OLED |
|---|---|---|---|---|
| Response Time | 1ms (fastest) | 4–8ms (improving) | 4–10ms (slowest) | <1ms |
| Viewing Angles | Narrow (~170 degrees) | Wide (~178 degrees) | Medium (~178 degrees) | Wide (~178 degrees) |
| Color Accuracy | Moderate | Excellent | Good | Excellent |
| Contrast Ratio | ~1,000:1 | ~1,000:1 | 3,000–8,000:1 | Infinite (true black) |
| Burn-in Risk | None | None | None | Yes (static images) |
| Relative Cost | Lowest | Medium | Medium | Highest |
| Primary Use Case | Competitive gaming | Professional work, design | Media consumption | Premium gaming, reference |

---

### Section 3: Display Connector Comparison Table

| Feature | HDMI | DisplayPort | DVI-D | DVI-I | VGA |
|---|---|---|---|---|---|
| Pin Count | 19 (Type A) | 20 | 24+1 | 29 | 15 |
| Carries Audio | Yes | Yes (embedded) | No | No | No |
| Signal Type | Digital | Digital | Digital | Digital + Analog | Analog only |
| Max Version Bandwidth | 42.6 Gbps (2.1) | 77.4 Gbps (2.0) | ~3.96 Gbps | ~3.96 Gbps | N/A (analog) |
| Daisy-chain (MST) | No | Yes | No | No | No |
| 4K@60Hz Support | HDMI 2.0+ | DP 1.2+ | No | No | No |
| Adapt to VGA (passive) | No | No | No | Yes | Native |
| Legacy Status | Current | Current | Legacy | Legacy | Legacy |

---

### Section 4: HDMI Version Bandwidth Reference

| HDMI Version | Maximum Bandwidth | Maximum Supported Combination |
|---|---|---|
| HDMI 1.4 | 8.16 Gbps | 4K @ 30Hz |
| HDMI 2.0 | 14.4 Gbps | 4K @ 60Hz |
| HDMI 2.0a/b | 14.4 Gbps | 4K @ 60Hz with HDR |
| HDMI 2.1 | 42.6 Gbps | 4K @ 120Hz, 8K @ 60Hz |

---

### Section 5: DisplayPort Version Bandwidth Reference

| DisplayPort Version | Maximum Bandwidth | Maximum Supported Combination |
|---|---|---|
| DisplayPort 1.2 | 17.28 Gbps | 4K @ 60Hz |
| DisplayPort 1.4 | 25.92 Gbps | 4K @ 144Hz, 8K @ 60Hz |
| DisplayPort 2.0 | 77.4 Gbps | 4K @ 240Hz, 8K @ 85Hz |

---

### Section 6: Certification Exam Tips

**Trap 1 — HDMI does not support daisy-chaining.** Any A+ scenario asking about connecting multiple monitors from a single output must use DisplayPort MST, not HDMI. This is tested directly and frequently.

**Trap 2 — HDMI 1.4 limits 4K to 30Hz.** A technician who connects a 4K monitor with an HDMI 1.4 cable will see either a limited resolution or a 30Hz refresh rate. The fix is replacing the cable with HDMI 2.0 or using a DisplayPort cable. Cable version is the limiting factor, not the monitor or GPU.

**Trap 3 — DVI-D cannot passively adapt to VGA.** DVI-D carries only a digital signal. VGA requires an analog signal. A passive DVI-D to VGA adapter will not work because there is no analog signal to pass. This question appears in the form "a user wants to connect a VGA monitor to a DVI-D port — which adapter do they need?" The answer is an active adapter (digital-to-analog converter), not a passive one.

**Trap 4 — DVI-I can passively adapt to VGA.** DVI-I carries both digital and analog signals. The four-pin cross-cluster on the connector carries the analog signal. A passive DVI-I to VGA adapter works because the analog signal is already present on the DVI-I port.

**Trap 5 — TN vs. IPS for professional use.** The A+ exam will describe a user who needs accurate color for photo editing or video production and ask which panel type to recommend. The correct answer is IPS (or in some contexts OLED). TN panels are recommended only when response time is the primary requirement.

**Trap 6 — Response time is a panel specification, not a cable specification.** Changing a DisplayPort cable to HDMI will not improve or worsen response time. Response time is determined by the panel technology.

**Trap 7 — A 240Hz monitor requires a compatible GPU output rate and cable.** A monitor capable of 240Hz only delivers 240Hz motion smoothness if the GPU is rendering and outputting 240 fps and the cable carries sufficient bandwidth. The monitor spec alone does not guarantee the experience.

**Trap 8 — Mini DisplayPort and Mini HDMI look similar but are different connectors.** Mini DisplayPort has a distinctively shaped connector (smaller version of the angled DP connector). Mini HDMI has a slightly different shape. Both connect to displays with the appropriate full-size adapter.

---

### Section 7: Required Readings and Videos

Complete all of the following before attempting the lab and quiz.

**Required Reading:** Review the display technology and connector sections in Professor Messer's CompTIA A+ Study Notes, available at [https://www.professormesser.com/](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections covering display types (TN/IPS/VA/OLED), video connectors (HDMI/DisplayPort/DVI/VGA), and resolution/refresh rate specifications.

**Required Video:** Watch the display technologies and connectors segments in Professor Messer's free CompTIA A+ Core 1 course at [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Focus on the connector identification segment, the panel type comparison, and the HDMI vs. DisplayPort capability comparison.

**Supplemental Reference:** CompTIA A+ Core 1 exam objectives are available at [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a). Review Domain 1.1 and Domain 3.1 objective lists to confirm coverage of display-related topics.

---

### Section 8: Lab Connection

This module's lab reinforces three skills directly tested on the A+ exam:

1. Connector identification — matching connector names to pin counts, audio capability, signal type, daisy-chain support, and physical description
2. Resolution and refresh rate compatibility — determining whether a cable version supports a given display specification combination and identifying the limiting factor when it does not
3. Signal path tracing — following the signal path from GPU through a specific connector to a display and identifying configuration errors in a multi-monitor diagram

Complete the Reading Guide glossary review before beginning the lab.

---

### Section 9: Study Checklist

- [ ] Name the four LCD subtypes and state the primary advantage and disadvantage of each
- [ ] Describe what makes OLED fundamentally different from LCD and explain burn-in risk
- [ ] Identify each connector (HDMI, DisplayPort, DVI-D, DVI-I, VGA) by its pin count and a physical characteristic
- [ ] State which connectors carry audio and which carry video only
- [ ] Explain MST (Multi-Stream Transport) and which connector supports it
- [ ] State the maximum resolution and refresh rate for HDMI 1.4, HDMI 2.0, and DisplayPort 1.4
- [ ] Explain why a DVI-D port cannot passively adapt to VGA, but a DVI-I port can
- [ ] Describe the scenario in which a 4K monitor displays only 30Hz and explain the cable version fix
- [ ] Read the display technology and connector sections in Professor Messer's CompTIA A+ Study Notes
- [ ] Watch the display technology videos in Professor Messer's free A+ Core 1 course
- [ ] Complete Lab 07 and submit via Canvas before the deadline
- [ ] Post your Discussion 07 initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

1. **Professor Messer — Display Technologies and Connectors (220-1101 Free Video)**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video covering TN/IPS/VA/OLED panel types, HDMI, DisplayPort, DVI, and VGA connector identification — all Module 07 exam objectives.

2. **HDMI Forum — HDMI Specifications (Free Reference)**
   URL: [https://www.hdmi.org/spec/Summary](https://www.hdmi.org/spec/Summary)
   Relevance: Official HDMI specification summaries for 1.4, 2.0, and 2.1. Use to verify bandwidth, resolution, and refresh rate capabilities for each version when answering compatibility questions in the lab and quiz.

3. **VESA — DisplayPort Standard Overview (Free)**
   URL: [https://www.displayport.org/displayport-a-technical-primer/](https://www.displayport.org/displayport-a-technical-primer/)
   Relevance: Official VESA overview of DisplayPort 1.2, 1.4, and 2.0/2.1 bandwidth capabilities, MST support, and comparisons to HDMI. The authoritative source for DisplayPort technical specifications.

4. **Rtings.com — Monitor Panel Type Comparison (Free)**
   URL: [https://www.rtings.com/monitor/learn/ips-vs-va-vs-tn-vs-oled](https://www.rtings.com/monitor/learn/ips-vs-va-vs-tn-vs-oled)
   Relevance: Free side-by-side comparison of TN, IPS, VA, and OLED panel characteristics with measured data. Reinforces the panel type comparison table from the reading guide with real-world test data.

5. **DisplayPort Bandwidth Calculator (Free Tool)**
   URL: [https://www.displayninja.com/displayport-bandwidth-calculator/](https://www.displayninja.com/displayport-bandwidth-calculator/)
   Relevance: Interactive calculator that shows whether a given resolution, refresh rate, and color depth combination fits within a specific DisplayPort or HDMI version's bandwidth. Useful for the lab challenge exercise on bandwidth calculations.

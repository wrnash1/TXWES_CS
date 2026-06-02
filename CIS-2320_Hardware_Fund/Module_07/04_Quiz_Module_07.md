# Quiz: Module 07 - Display Technologies and Connectors

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

Total Questions: 10 | Points: 10 (1 point each)

Certification Domain: 1.1 — Install and configure laptop hardware | 3.1 — Install and configure display components

---

### Question 1

Which display connector supports daisy-chaining multiple monitors together from a single GPU output port?

- A) HDMI
- B) DisplayPort
- C) VGA
- D) DVI

Correct Answer: B — DisplayPort supports Multi-Stream Transport (MST), which allows a single DisplayPort output to carry multiple independent video streams. These streams can be split using an MST hub or by daisy-chaining from one monitor's DisplayPort output to the next.

Distractor Analysis:

- Why A is incorrect: HDMI does not support MST. Each HDMI output on a GPU connects to exactly one display. An HDMI splitter duplicates the same image to multiple screens but cannot create independent extended displays from one port.
- Why C is incorrect: VGA is a legacy analog connector with no digital protocol layer. It does not support any form of multi-stream transport or daisy-chaining.
- Why D is incorrect: DVI (whether DVI-D or DVI-I) does not support MST. DVI connections are single-stream only, carrying one video signal per cable to one display.

---

### Question 2

Which of the following most accurately describes the key differences between HDMI, DisplayPort, and DVI?

- A) Three digital video connector standards where HDMI carries video and audio and is the most common consumer standard; DisplayPort supports higher refresh rates and enables monitor daisy-chaining via MST; DVI is a legacy connector carrying digital-only (DVI-D) or digital-and-analog (DVI-I) video with no audio.
- B) Three audio interface standards that determine whether a monitor's built-in speakers receive digital surround sound, stereo PCM, or analog audio signals from the connected source device.
- C) Three software rendering APIs — HDMI handles 2D acceleration, DisplayPort manages the 3D pipeline, and DVI provides a DirectX compatibility layer for legacy display drivers.
- D) Three monitor backlight technologies — HDMI uses LED edge lighting, DisplayPort uses full-array local dimming, and DVI uses cold-cathode fluorescent backlighting.

Correct Answer: A — This accurately describes the physical connector standards, their signal types, audio capability, and primary use cases as tested on the CompTIA A+ exam.

Distractor Analysis:

- Why B is incorrect: HDMI, DisplayPort, and DVI are video signal interfaces, not audio routing standards. While HDMI does carry audio, all three are classified and tested as display connectors.
- Why C is incorrect: HDMI, DisplayPort, and DVI are hardware connector and signaling standards, not software rendering APIs. Graphics rendering APIs (DirectX, OpenGL, Vulkan) are entirely separate technologies.
- Why D is incorrect: These connectors define how video signals are transmitted between the GPU and monitor. They do not determine the internal backlight technology of the monitor itself.

---

### Question 3

A user connects a new 4K monitor to their PC using an HDMI cable, but the monitor displays at 1080p and the resolution settings show a maximum of 4K@30Hz rather than the monitor's advertised 4K@60Hz. The GPU supports 4K output and the monitor supports 4K@60Hz. What is the most likely cause?

- A) The monitor's internal scaler is set to 1080p and must be changed via the monitor's OSD menu.
- B) The GPU driver needs to be reinstalled before 4K resolution becomes available over any connector.
- C) The HDMI cable is HDMI 1.4, which has insufficient bandwidth to carry a 4K@60Hz signal.
- D) HDMI is fundamentally incapable of carrying 4K at any refresh rate; DisplayPort must be used.

Correct Answer: C — HDMI 1.4 supports a maximum of approximately 8.16 Gbps effective bandwidth, which supports 4K resolution but only at 30Hz. Achieving 4K@60Hz requires HDMI 2.0 (14.4 Gbps) or higher. The cable version is the limiting factor when both the GPU and monitor are otherwise capable.

Distractor Analysis:

- Why A is incorrect: While the OSD setting is worth checking, the operating system-level resolution maximum of 4K@30Hz is a hardware bandwidth limitation imposed by the cable version, not an OSD configuration issue.
- Why B is incorrect: Driver reinstallation addresses software issues. A cable bandwidth constraint is a physical hardware limitation that reinstalling a driver cannot resolve.
- Why D is incorrect: HDMI 2.0 fully supports 4K@60Hz, and HDMI 2.1 supports 4K@120Hz and 8K@60Hz. The limitation is specific to HDMI 1.4, not to the HDMI standard as a whole.

---

### Question 4

A technician needs to connect three monitors to a single DisplayPort output on a GPU. Each monitor has one DisplayPort input and one HDMI input. Which configuration correctly enables all three monitors as independent extended displays from the one GPU port?

- A) Connect the first monitor to DisplayPort, then use the monitor's HDMI output port to chain to the second monitor, and the second's HDMI output to the third.
- B) Use a DisplayPort MST hub to split the single DisplayPort signal into three separate DisplayPort connections, one to each monitor.
- C) Connect the first monitor via DisplayPort and the remaining two via a dual-HDMI splitter cable plugged into the DisplayPort port using a passive adapter.
- D) Run three DisplayPort cables from the GPU's single DisplayPort port to each monitor using a Y-splitter cable.

Correct Answer: B — A DisplayPort MST hub uses the MST protocol to carry multiple independent video streams over one incoming DisplayPort cable, then splits them into separate output connections — one per monitor. This is the correct and designed use case for MST hardware.

Distractor Analysis:

- Why A is incorrect: Consumer monitors have HDMI input ports, not HDMI output ports. Monitors cannot pass-through or chain HDMI signals downstream to additional monitors.
- Why C is incorrect: A passive DisplayPort-to-HDMI adapter carries only a single video stream. It cannot split into two HDMI outputs, and HDMI does not support MST chaining regardless of the adapter used.
- Why D is incorrect: A DisplayPort Y-splitter would at best duplicate the same image to all connected monitors (mirror/clone mode using SST). It cannot create independent extended displays from one port and may not function at all depending on GPU support.

---

### Question 5

A gaming monitor is advertised as supporting 240Hz refresh rate and 1ms response time. What additional requirement must be met to actually benefit from the 240Hz capability?

- A) The GPU must output at least 240 frames per second in the content being played, and the cable must have sufficient bandwidth for the resolution and refresh rate combination.
- B) The monitor must be connected via HDMI because DisplayPort cannot carry refresh rates above 144Hz to any display at any resolution.
- C) The CPU must have a minimum of 8 cores because single-threaded performance alone determines the monitor's maximum achievable refresh rate.
- D) The operating system must be configured with a 240Hz power plan profile in Windows Advanced Display Settings before the monitor can unlock its full refresh rate.

Correct Answer: A — A 240Hz monitor only delivers 240Hz motion smoothness if the GPU is rendering and outputting 240 or more frames per second in the running content. Additionally, the cable connecting GPU to monitor must have sufficient bandwidth to carry that signal at the target resolution (for example, DisplayPort 1.4 for 1440p@240Hz).

Distractor Analysis:

- Why B is incorrect: DisplayPort 1.4 supports 1440p@240Hz, and DisplayPort 2.0 supports 4K@240Hz. DisplayPort is not limited to 144Hz; in most high-refresh-rate scenarios, DisplayPort is the preferred choice over HDMI.
- Why C is incorrect: Core count does not directly determine frame output rate. GPU performance, game engine threading, and clock speeds are the primary frame rate determinants.
- Why D is incorrect: Windows Advanced Display Settings is where the refresh rate is selected, but the OS configuration does not "unlock" hardware capability. The hardware must support the rate, the GPU must output it, and the cable must carry it.

---

### Question 6

A technician has a monitor with only a VGA input and a GPU with only a DVI-D output. A colleague suggests using a passive DVI-D to VGA adapter. Will this work? Why or why not?

- A) Yes — DVI-D and VGA both carry digital signals, so a passive adapter can bridge the two standards with no signal loss.
- B) No — DVI-D carries only a digital signal and VGA requires an analog signal; a passive adapter cannot convert digital to analog, so an active converter is required.
- C) Yes — DVI-D carries both digital and analog signals, and the VGA adapter simply passes the analog portion of the DVI-D signal to the VGA monitor.
- D) No — VGA and DVI-D use incompatible pin voltages; even an active converter will permanently damage the monitor's input stage.

Correct Answer: B — DVI-D is a digital-only interface. VGA is an analog interface. A passive adapter provides only a physical pin connector mapping — it cannot perform the digital-to-analog conversion that VGA requires. An active DVI-D to VGA converter (containing a DAC chip) is necessary.

Distractor Analysis:

- Why A is incorrect: VGA does not carry a digital signal. VGA is fully analog. DVI-D is fully digital. The two are not compatible with a passive adapter because the signals are of fundamentally different types.
- Why C is incorrect: This describes DVI-I, not DVI-D. DVI-I carries both digital and analog signals and can passively adapt to VGA. DVI-D carries digital only and cannot.
- Why D is incorrect: An active DVI-D to VGA converter does work safely; there is no pin voltage incompatibility that would damage hardware. The issue is signal type, not voltage level.

---

### Question 7

A photographer uses a monitor for professional photo editing and color calibration. Which panel technology should a technician recommend, and which panel type should be explicitly avoided for this use case?

- A) Recommend TN; avoid IPS — TN panels have superior color accuracy for professional color work.
- B) Recommend IPS; avoid TN — IPS panels provide wide viewing angles and accurate color reproduction essential for professional imaging work.
- C) Recommend VA; avoid IPS — VA panels have higher contrast ratios, which is the most important factor in professional color calibration.
- D) Recommend TN; avoid OLED — TN panels are immune to burn-in and therefore the safest choice for extended professional use.

Correct Answer: B — IPS panels are the industry standard recommendation for professional color work because they offer wide viewing angles (ensuring color accuracy is consistent regardless of viewing position) and high color accuracy and gamut coverage. TN panels have inferior color accuracy and narrow viewing angles, making them unsuitable for professional imaging.

Distractor Analysis:

- Why A is incorrect: TN panels are specifically noted for inferior color accuracy and narrow viewing angles — the opposite of what professional photo editing requires. TN is the technology to avoid for color work.
- Why C is incorrect: While VA panels do have excellent contrast ratios, IPS panels are more widely used and validated for professional color calibration because of their superior color accuracy and gamut support. Contrast ratio alone is not the primary criterion for color work.
- Why D is incorrect: TN panels are not recommended for professional color work for reasons of accuracy, not burn-in safety. OLED, while it has burn-in risk, can actually be used for professional reference work with proper usage habits. The recommendation should be based on color accuracy, not burn-in avoidance.

---

### Question 8

A user reports that their laptop connects to an external projector via HDMI but the projector only shows a duplicate of the laptop screen. The user wants the projector to display different content as an extended second display. What is the correct way to configure this?

- A) Replace the HDMI cable with a DisplayPort cable because HDMI cannot support extended display mode, only mirror mode.
- B) Access display settings (Windows key + P or Display Settings) on the laptop and select "Extend" instead of "Duplicate" to configure the projector as an independent second display.
- C) Install the GPU manufacturer's driver update, which enables extended display mode over HDMI for the first time.
- D) Connect the projector to a different HDMI port on the laptop because only specific HDMI ports support extended mode.

Correct Answer: B — "Duplicate" (clone) mode and "Extend" mode are operating system display configuration settings, not hardware limitations. The user needs to change the multi-display mode in Windows Display Settings (accessible via Windows key + P for the quick menu) to "Extend" to use the projector as an independent second display.

Distractor Analysis:

- Why A is incorrect: HDMI fully supports extended display mode. The mirror/extend behavior is a software configuration in the operating system, not a hardware or connector limitation.
- Why C is incorrect: The display mode setting is an OS-level configuration, not a driver feature that requires an update to unlock. Extended mode via HDMI has been a standard feature for many years.
- Why D is incorrect: All HDMI ports on a laptop support extended display mode; the behavior does not vary by which specific physical port is used. The issue is the display mode setting, not the port selection.

---

### Question 9

Which of the following display scenarios would most likely result in visible burn-in damage over time?

- A) Using a TN panel at 144Hz for competitive gaming with frequently changing content for 8 hours per day.
- B) Using an IPS panel for 10 hours per day of general web browsing with the browser window frequently moved around the screen.
- C) Using an OLED monitor as a stock trading workstation where the same ticker bar, charts layout, and menu structure remain on screen for 10–14 hours per day.
- D) Using a VA panel at maximum brightness for 6 hours per day of movie watching with variable full-screen content.

Correct Answer: C — OLED panels are susceptible to burn-in when static high-brightness elements remain on screen for extended periods. A stock trading workstation with a fixed ticker bar, fixed chart panels, and fixed UI elements displayed for many hours daily is an archetypal high-risk OLED burn-in scenario. The organic pixel compounds in the always-on areas degrade faster than neighboring pixels.

Distractor Analysis:

- Why A is incorrect: TN panels use inorganic LCD technology and are not susceptible to burn-in. Burn-in is a phenomenon specific to OLED and plasma displays, not LCD panels of any subtype.
- Why B is incorrect: IPS panels are LCD technology and are not susceptible to burn-in. Varying content and a moving browser window represent low static-image exposure even if it were an OLED display.
- Why D is incorrect: VA panels are LCD technology and are not susceptible to burn-in. Full-screen variable movie content is also a low burn-in risk use case for OLED, as the content changes continuously across all pixels.

---

### Question 10

A technician is setting up a new monitor and needs to identify which HDMI version the cable supports. The cable is unlabeled. What is the most reliable method to determine the cable's HDMI version capability without testing equipment?

- A) Examine the cable color — white cables are HDMI 2.0 and black cables are HDMI 1.4 by manufacturer convention.
- B) Check the cable packaging, the cable label printed on the cable body, or the embossed text near the connector for the rated specification.
- C) The physical connector shape changes with each HDMI version, so examining the connector profile will identify the version.
- D) All HDMI cables support the same maximum bandwidth regardless of labeled version; version numbers are only relevant for the ports on devices, not the cable itself.

Correct Answer: B — HDMI cable version is printed on the cable jacket, the cable packaging, or embossed near the connector on higher-quality cables. Checking the labeling is the standard and most reliable method to identify cable version without test equipment.

Distractor Analysis:

- Why A is incorrect: There is no HDMI color-coding standard. Cable color is a manufacturer aesthetic choice and does not indicate HDMI version.
- Why C is incorrect: All HDMI versions use the same physical connector shape for the full-size Type A connector. The connector profile does not change between HDMI 1.4, 2.0, and 2.1.
- Why D is incorrect: Cable construction and certification do vary by HDMI version. An HDMI 1.4 cable physically cannot carry an HDMI 2.1 signal at full bandwidth because the internal wire gauge, shielding, and certification tolerances differ between versions. Version matters for both the device port and the cable.

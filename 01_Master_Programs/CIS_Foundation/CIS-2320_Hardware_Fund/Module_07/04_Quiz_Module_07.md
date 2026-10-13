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

---

### Question 11

A monitor advertised as "144Hz" is connected to a GPU via a DisplayPort 1.2 cable. The monitor supports up to 1440p resolution. What is the maximum resolution and refresh rate this connection can deliver?

- A) 1440p@144Hz — DisplayPort 1.2 supports this combination
- B) 1080p@144Hz — DisplayPort 1.2 cannot carry 1440p at high refresh rates
- C) 1440p@60Hz — DisplayPort 1.2 bandwidth is insufficient for 1440p@144Hz
- D) 4K@60Hz — DisplayPort 1.2 automatically upscales to the maximum supported resolution

Correct Answer: A — DisplayPort 1.2 provides approximately 17.28 Gbps of usable bandwidth, which is sufficient for 1440p@144Hz (requiring approximately 7.9 Gbps uncompressed). Both the resolution and refresh rate are achievable on this connection.

Distractor Analysis:

- Why B is incorrect: DisplayPort 1.2 has ample bandwidth for 1440p@144Hz. The 1080p limitation would apply to much older interfaces like HDMI 1.4 at very high refresh rates.
- Why C is incorrect: 1440p@60Hz requires only ~3.96 Gbps — well within DisplayPort 1.2 capability. Limiting to 60Hz is unnecessary; the bandwidth supports 144Hz at this resolution.
- Why D is incorrect: DisplayPort does not automatically upscale to a resolution the monitor does not natively support. Resolution output is configured by the OS and GPU driver based on the monitor's EDID data.

---

### Question 12

What is Multi-Stream Transport (MST) in the context of DisplayPort, and which older display interface does NOT support it?

- A) MST allows a single DisplayPort output to drive multiple monitors via a daisy-chain or hub; HDMI does not natively support MST
- B) MST is an audio multichannel feature for surround sound over DisplayPort; VGA does not support audio at all
- C) MST enables a monitor to display multiple input sources simultaneously in picture-in-picture mode; DVI does not support this
- D) MST is a refresh rate synchronization protocol that DisplayPort uses to eliminate screen tearing; VGA does not support synchronization

Correct Answer: A — MST (Multi-Stream Transport) is a DisplayPort feature that allows multiple independent video streams to share a single cable or daisy-chained monitor connection. A single DisplayPort 1.2+ output can drive two or more monitors simultaneously. HDMI does not natively support MST; multiple HDMI monitors each require their own dedicated output port.

Distractor Analysis:

- Why B is incorrect: MST refers to multi-monitor video streams, not audio multichannel. While DisplayPort does carry audio, MST specifically describes the multi-monitor capability.
- Why C is incorrect: MST drives multiple independent external monitors, not picture-in-picture on one monitor. PiP is a monitor feature unrelated to DisplayPort MST.
- Why D is incorrect: Screen tearing synchronization is addressed by adaptive sync technologies (AMD FreeSync, NVIDIA G-Sync), not by MST. MST is a multi-monitor connection protocol, not a sync protocol.

---

### Question 13

A DVI-D Single Link port is the only available output on an older GPU. A technician needs to connect a monitor that only has a VGA input. Which adapter will work?

- A) A DVI-D to VGA passive adapter, which converts the digital DVI-D signal to the analog VGA signal
- B) An active DVI-D to VGA adapter with a built-in DAC that converts digital DVI-D to analog VGA
- C) No adapter will work; DVI-D to VGA connection is impossible because digital and analog signals are incompatible
- D) A DVI-I to VGA passive adapter, which adds VGA pins to the DVI connector

Correct Answer: B — DVI-D is a digital-only signal. Converting digital DVI-D to analog VGA requires an active adapter with a Digital-to-Analog Converter (DAC) chip. Passive adapters work only from DVI-I, which carries an analog signal alongside the digital signal in the connector.

Distractor Analysis:

- Why A is incorrect: A passive DVI-D to VGA adapter will not work because DVI-D carries no analog signal. Passive adapters simply reroute the existing pins — they cannot convert digital to analog without active electronics.
- Why C is incorrect: DVI-D to VGA conversion is possible using an active adapter with a DAC chip. The statement that it is impossible is incorrect.
- Why D is incorrect: A DVI-I to VGA passive adapter works from a DVI-I port (which carries the analog signal). However, the scenario specifies a DVI-D port, which lacks the analog pins DVI-I carries. Applying a DVI-I adapter description to a DVI-D port situation is incorrect.

---

### Question 14

A user connects a new 4K OLED monitor to a laptop using HDMI. The monitor displays only at 1080p@60Hz even though the monitor is rated for 4K@120Hz. The HDMI cable is labeled "High Speed HDMI." What should the technician investigate first?

- A) The laptop GPU driver is outdated and limiting the maximum resolution
- B) The HDMI cable may be High Speed (v1.4, 10.2 Gbps) rather than Ultra High Speed (v2.1, 48 Gbps); replacing with an HDMI 2.1 cable is the first step
- C) OLED monitors cannot display 4K through HDMI; a DisplayPort cable is required for 4K OLED
- D) The monitor's EDID data is corrupted and must be reset before 4K output is available

Correct Answer: B — HDMI "High Speed" certification corresponds to HDMI 1.4 (10.2 Gbps) — sufficient for 1080p@60Hz but insufficient for 4K@120Hz (which requires ~42.7 Gbps). "Ultra High Speed HDMI" (HDMI 2.1) is required for 4K@120Hz. Replacing the cable with a certified HDMI 2.1 cable (48 Gbps) is the first diagnostic step.

Distractor Analysis:

- Why A is incorrect: GPU driver updates can affect features and stability but do not fundamentally change which resolutions/refresh rates are supported — that is determined by the GPU hardware's HDMI version. Additionally, the cable is the most likely bottleneck given the "High Speed" label indicating v1.4.
- Why C is incorrect: HDMI can carry 4K signals. The limitation is HDMI version, not the display technology (OLED vs. LCD). Many OLED TVs and monitors operate natively over HDMI.
- Why D is incorrect: EDID corruption can cause resolution misdetection, but it is an uncommon issue. The simpler and more likely explanation given the cable label is an HDMI version mismatch.

---

### Question 15

Which display panel technology offers true infinite contrast ratio (true blacks) because individual pixels can be completely turned off?

- A) TN (Twisted Nematic)
- B) IPS (In-Plane Switching)
- C) VA (Vertical Alignment)
- D) OLED (Organic Light-Emitting Diode)

Correct Answer: D — OLED panels are emissive displays: each pixel is its own light source and can be individually turned off, producing true black (zero light emission). This results in an infinite contrast ratio. LCD subtypes (TN, IPS, VA) all require a backlight that cannot be completely blocked on a per-pixel basis.

Distractor Analysis:

- Why A is incorrect: TN panels use a backlight that cannot be turned off per pixel. Black levels on TN displays are limited by backlight bleed-through, resulting in a grayish black.
- Why B is incorrect: IPS panels have excellent color accuracy and wide viewing angles, but they require a backlight. IPS panels are known for "IPS glow" — light bleed at screen corners — which limits contrast ratio.
- Why C is incorrect: VA panels have the best contrast ratio among LCD subtypes (typically 2,000:1–6,000:1 vs. TN/IPS at ~1,000:1) due to better light blocking in the aligned crystal state. However, they still have a backlight and cannot achieve true black.

---

### Question 16

A graphic designer complains that colors on their new IPS monitor look slightly different than on the older monitor they are replacing. Both monitors are set to the same brightness. What is the MOST appropriate first step to address this issue?

- A) Replace the HDMI cable with a DisplayPort cable, as HDMI compresses color data
- B) Calibrate the new monitor using a hardware colorimeter or the OS color management tool to create a correct ICC profile
- C) Set the monitor's color temperature to "Cool" mode to match the standard color balance
- D) Increase the monitor's contrast setting until the colors match the old monitor visually

Correct Answer: B — Color accuracy differences between monitors are addressed through calibration. A hardware colorimeter measures actual color output and creates an ICC profile that the OS color management system uses to correct colors for that specific monitor. For professional work, hardware calibration tools provide the most accurate result; the OS's built-in color calibration wizard provides a reasonable free alternative.

Distractor Analysis:

- Why A is incorrect: HDMI 2.0 and DisplayPort both support 10-bit color depth and full-range color. The connector type does not cause the color difference described; monitor panel variation and display settings do.
- Why C is incorrect: Setting the color temperature to "Cool" applies a blue-biased color shift that makes the display appear cooler, not more accurate. This is a subjective aesthetic adjustment, not calibration.
- Why D is incorrect: Adjusting contrast to visually match another uncalibrated monitor compounds the problem. Both monitors may be uncalibrated, and visual matching between two incorrect references does not produce accurate color output.

---

### Question 17

Which of the following correctly describes the function of EDID in a monitor connection?

- A) EDID is the encryption protocol that prevents unauthorized copying of HDMI video signals
- B) EDID is a data block stored in the monitor that identifies the monitor's supported resolutions, refresh rates, and color capabilities to the GPU
- C) EDID is the firmware update mechanism that upgrades a monitor's panel firmware over HDMI or DisplayPort
- D) EDID is the synchronization signal embedded in the HDMI stream that prevents screen tearing

Correct Answer: B — EDID (Extended Display Identification Data) is a standardized data block stored in the monitor's ROM. When connected, the GPU reads the EDID over the display cable (using the DDC channel) to learn the monitor's native resolution, maximum refresh rate, supported resolutions, color depth, and audio capabilities. The GPU then offers only compatible modes to the OS.

Distractor Analysis:

- Why A is incorrect: HDCP (High-bandwidth Digital Content Protection) is the copy protection mechanism for HDMI/DisplayPort signals. EDID is entirely separate and has nothing to do with encryption or content protection.
- Why C is incorrect: Monitor firmware updates are typically performed via proprietary tools or USB connections provided by the manufacturer — not through EDID. EDID is a read-only identification data block, not a firmware update channel.
- Why D is incorrect: Screen tearing prevention is addressed by adaptive sync (FreeSync/G-Sync) or VSync in the GPU driver. EDID is identification data, not a synchronization signal.

---

### Question 18

A presentation room has a projector that only accepts VGA input. A presenter's laptop has only HDMI and USB-C outputs. Which solution is MOST appropriate?

- A) Purchase a DVI-D to VGA passive adapter and connect it to the HDMI port
- B) Use an active HDMI-to-VGA adapter with a built-in DAC, connecting HDMI out to the adapter, then VGA cable to the projector
- C) Use a USB-C to VGA direct passive adapter, connecting USB-C out to the adapter, then VGA cable to the projector
- D) Replace the projector because VGA is no longer supported by modern operating systems

Correct Answer: B — HDMI is a digital signal; VGA is an analog signal. Converting HDMI to VGA requires an active adapter with a DAC (Digital-to-Analog Converter) chip. Passive adapters cannot perform digital-to-analog conversion. Active HDMI-to-VGA adapters are widely available and inexpensive.

Distractor Analysis:

- Why A is incorrect: A DVI-D to VGA passive adapter connects to a DVI-D port, not an HDMI port. Additionally, passive DVI-D to VGA adapters still require the DVI-I analog pins — they would not work from a DVI-D port and are entirely wrong for an HDMI port.
- Why C is incorrect: USB-C carries DisplayPort Alt Mode (a digital signal), not native analog VGA. A USB-C to VGA adapter must also be active (containing a DAC); a purely passive USB-C to VGA adapter does not exist because the signal conversion requires active electronics.
- Why D is incorrect: VGA support in operating systems exists for legacy compatibility; Windows supports VGA output through drivers. The projector does not need replacement — a signal converter adapter is the practical solution.

---

### Question 19

A user reports that their display shows a faint "ghost" image of a previous application permanently burned into the screen. The monitor uses OLED technology. What is the correct term for this phenomenon?

- A) Screen flickering
- B) Image persistence (burn-in)
- C) Dead pixel cluster
- D) Backlight bleeding

Correct Answer: B — Image persistence, commonly called burn-in, occurs on OLED displays when static high-brightness elements remain on screen for extended periods. The organic compounds in OLED pixels degrade at different rates depending on usage, causing the over-used pixels to emit less light than surrounding pixels — resulting in a permanent faint ghost image.

Distractor Analysis:

- Why A is incorrect: Screen flickering describes rapid oscillation in display brightness or image stability, often caused by an incorrect refresh rate setting or a failing cable. It is not related to permanent image retention.
- Why C is incorrect: A dead pixel is a pixel that no longer emits any light, appearing as a permanent black or colored dot. A dead pixel cluster is visible at all times, not only when viewing specific content like a ghost of a previous image.
- Why D is incorrect: Backlight bleeding is a physical artifact on LCD displays where the backlight is not fully blocked by the liquid crystal layer, causing bright patches near screen edges in dark scenes. OLED displays have no backlight; this term does not apply.

---

### Question 20

A technician needs to select a display cable for a video production workstation that requires 4K@60Hz output with 10-bit color depth. The GPU has one HDMI 2.0 port and one DisplayPort 1.4 port available. Which cable should be used?

- A) HDMI 2.0 — it supports 4K@60Hz with 10-bit color
- B) DisplayPort 1.4 — it provides more bandwidth and is required for 4K@60Hz with 10-bit color
- C) Either cable works equally well for this specification; choose based on which port the monitor has
- D) DisplayPort 1.2 is required; neither HDMI 2.0 nor DisplayPort 1.4 supports 10-bit color at 4K@60Hz

Correct Answer: C — Both HDMI 2.0 and DisplayPort 1.4 support 4K@60Hz with 10-bit color. HDMI 2.0 provides 18 Gbps, which is sufficient for 4K@60Hz 10-bit HDR. DisplayPort 1.4 provides 25.92 Gbps with additional headroom. Either works for this specification — the practical choice depends on which input the monitor provides.

Distractor Analysis:

- Why A is incorrect: While HDMI 2.0 does support 4K@60Hz with 10-bit color, stating it as the single choice ignores that DisplayPort 1.4 is equally or more capable. The question asks which to choose given both options, and the correct answer is that either works.
- Why B is incorrect: DisplayPort 1.4 is more capable, but HDMI 2.0 is not insufficient for this specification. Claiming DisplayPort 1.4 is "required" is incorrect when HDMI 2.0 meets the stated requirements.
- Why D is incorrect: Both HDMI 2.0 and DisplayPort 1.4 fully support 4K@60Hz with 10-bit color depth. This answer incorrectly states that neither works and introduces DisplayPort 1.2 (which supports 4K@60Hz 8-bit natively, with 10-bit requiring DSC) as the required cable.

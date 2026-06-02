# Video Script: Module 07 - Display Technologies and Connectors

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Estimated Duration:** 22-24 minutes

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 1.1 (Given a scenario, install and configure laptop hardware and components) and Domain 3.1 (Given a scenario, install and configure storage devices and display components)

**Recorded by:** Professor Nash | Texas Wesleyan University

---

### Production Notes

SHOW COMPONENT cues in this script:

- [SHOW COMPONENT: HDMI cable held up — identify the trapezoidal 19-pin connector shape]
- [SHOW COMPONENT: DisplayPort cable held up — identify the 20-pin connector with one angled corner]
- [SHOW COMPONENT: DVI-D connector (digital only, no analog pins in cross-shaped cluster)]
- [SHOW COMPONENT: DVI-I connector (digital + analog, cross-shaped cluster present)]
- [SHOW COMPONENT: VGA connector (15-pin, 3-row, trapezoidal, blue)]
- [SHOW COMPONENT: IPS panel and TN panel side by side — viewing angle comparison]
- [SHOW COMPONENT: Resolution comparison slide — 1080p, 1440p, 4K pixel counts]
- [SHOW COMPONENT: DisplayPort MST hub — one DP input, multiple DP outputs]

Key Exam Traps to call out explicitly:

- "DisplayPort is the only connector that natively supports daisy-chaining (MST). HDMI does not."
- "HDMI 1.4 supports 4K but only at 30Hz. You need HDMI 2.0 for 4K@60Hz."
- "DVI-D is digital only. DVI-I carries both digital and analog. They look almost identical — count the pins."
- "VGA is fully analog. If a monitor shows VGA, the signal quality degrades with cable length."
- "TN panels have the fastest response time but the worst viewing angles. IPS has great color and angles but slower response."

Safety Notes:

- Monitor panels contain high-voltage inverter boards (for CCFL backlit displays) — do not probe inside a monitor without proper training
- LCD panels are fragile — never press on the panel surface or flex the housing
- When connecting cables to a powered monitor, ensure the display is off before seating the connector to avoid static discharge to the panel driver board

---

### [00:00 - 02:30] Section 1: Introduction — Displays Are the User's Window Into the System

[INSTRUCTOR ON CAMERA — title card visible: "Module 07: Display Technologies and Connectors"]

"Welcome back, everyone. I'm Professor Nash. Today we are covering display technologies and connectors — the hardware that translates all of the computing your CPU and GPU do into the image you actually see.

This topic shows up on the CompTIA A+ Core 1 exam in both hardware configuration scenarios and troubleshooting scenarios. You need to know what panel technologies exist and how they differ, which connector to use for which situation, how cable versions affect resolution and refresh rate, and how to set up a multi-monitor environment.

[PAUSE]

Think about what a technician is actually asked to do in the field. A user brings in a new 4K monitor and their old PC does not display at full resolution. A company wants to set up dual monitors on every workstation. A user's laptop is connected to a projector but gets no image. All of these situations require you to understand what signal is coming out of the GPU, what signal the display expects, which connector or adapter bridges the two, and whether the cable version supports the resolution and refresh rate the user needs.

By the end of this module you will be able to identify HDMI, DisplayPort, DVI, and VGA connectors by sight, explain the capabilities of each, describe the differences between IPS, TN, VA, and OLED panel technologies, and calculate whether a given cable version supports a target resolution and refresh rate. Let's get into it.

Exam Tip: The A+ Core 1 exam tests connector identification, display technology differences, and cable version limitations. Expect both identification questions and scenario questions that ask which cable or adapter to use."

---

### [02:30 - 09:00] Section 2: Display Panel Technologies

[SLIDE: "Panel Technologies — What's Inside the Screen?"]

"Before we talk about connectors, let's understand what kind of panel is behind the glass.

#### LCD — Liquid Crystal Display

[SHOW COMPONENT: IPS panel and TN panel side by side — viewing angle comparison]

LCD stands for Liquid Crystal Display. It is the dominant display technology in monitors and laptops today. An LCD panel uses a backlight (LED in modern displays) and a layer of liquid crystals that can be electrically rotated to control how much light passes through. The liquid crystals themselves do not emit light — they modulate the backlight.

There are three main LCD panel subtypes:

TN — Twisted Nematic. The original and still the fastest LCD panel type. TN panels can achieve response times as low as 1 millisecond, making them popular for competitive gaming where motion blur matters most. The drawback: narrow viewing angles (colors shift noticeably when you look from the side or top) and less accurate color reproduction compared to other types.

IPS — In-Plane Switching. IPS panels align liquid crystals parallel to the screen surface instead of perpendicular. This gives them excellent viewing angles — close to 178 degrees horizontally and vertically — and significantly more accurate color reproduction. These are the panels you will see recommended for photo editing, graphic design, and professional work. The traditional drawback was slower response times (4–8ms), though modern IPS panels have closed that gap considerably.

VA — Vertical Alignment. VA panels sit between TN and IPS in terms of viewing angles and response time. Their standout characteristic is contrast ratio — VA panels can achieve native contrast ratios of 3000:1 to 6000:1, compared to 1000:1 for typical IPS panels. This produces deeper blacks and better shadow detail. VA panels are popular for media consumption and mixed-use monitors.

[PAUSE]

#### OLED — Organic Light-Emitting Diode

OLED panels are fundamentally different from LCD. Each individual pixel in an OLED display is its own light source — it emits light directly when an electrical current passes through the organic compound. This means each pixel can be turned completely off, producing true black with effectively infinite contrast ratio.

Advantages: perfect blacks, incredibly fast response times (fractions of a millisecond), wide viewing angles comparable to IPS, and thinner panel construction since no backlight layer is needed.

Disadvantages: OLED is susceptible to burn-in — if a static image (like a Windows taskbar or a HUD element in a game) remains on screen for extended periods, the organic compounds in those pixels can degrade faster than neighboring pixels, leaving a faint permanent ghost of the image. OLED monitors are also significantly more expensive per inch than LCD.

[PAUSE — exam tip]

Exam Tip: On the A+ exam, TN = fastest response, worst viewing angles. IPS = best color and viewing angles. VA = best contrast ratio. OLED = true black, infinite contrast, burn-in risk. These are the four associations you need to memorize for panel type questions."

---

### [09:00 - 16:00] Section 3: Display Connectors — HDMI, DisplayPort, DVI, VGA

[SLIDE: "Connectors — Matching Signal to Display"]

"Now let's cover the connector types. This is where a significant number of A+ exam questions originate.

#### HDMI — High-Definition Multimedia Interface

[SHOW COMPONENT: HDMI cable held up — identify the trapezoidal 19-pin connector shape]

HDMI is the most widely used consumer display connector in the world. You will find it on TVs, monitors, projectors, laptops, gaming consoles, and set-top boxes. The full-size HDMI connector (Type A) has 19 pins and a distinctive trapezoidal shape with the wider end at the top. Smaller variants include Mini HDMI (Type C) and Micro HDMI (Type D), commonly found on cameras and tablets.

Key capability: HDMI carries both video and audio on a single cable. For most consumer setups this is a significant convenience — one cable from the GPU to the monitor or TV handles both signal types.

Version matters:

- HDMI 1.4: Supports 4K at 30Hz. Common in older TVs and monitors.
- HDMI 2.0: Supports 4K at 60Hz. The current standard for most modern monitors and consoles.
- HDMI 2.1: Supports 4K at 120Hz and 8K at 60Hz. Found in high-end gaming monitors and current-generation consoles.

[PAUSE — exam trap]

HDMI does not natively support daisy-chaining multiple monitors. Each HDMI output on your GPU connects to exactly one display.

#### DisplayPort

[SHOW COMPONENT: DisplayPort cable held up — identify the 20-pin connector with one angled corner]

DisplayPort is the preferred connector for PC monitors. It is used on graphics cards, desktop monitors, and some laptops. The connector has 20 pins and one distinctively angled corner that prevents incorrect insertion. Mini DisplayPort is a smaller variant used on older Apple hardware and some laptops.

DisplayPort's key advantage over HDMI is bandwidth and multi-monitor support. DisplayPort 1.4 supports 8K at 60Hz or 4K at 144Hz. DisplayPort 2.0 dramatically increases bandwidth further. DisplayPort also supports Multi-Stream Transport (MST), which allows a single DisplayPort output to drive multiple independent monitors — either via a daisy-chain (monitor to monitor) or via an MST hub (one port in, multiple ports out).

[PAUSE — exam trap]

DisplayPort is the only standard connector that supports MST daisy-chaining. This is a heavily tested A+ exam point. If a scenario asks about connecting three monitors to one output, the answer is DisplayPort with an MST hub.

#### DVI — Digital Visual Interface

[SHOW COMPONENT: DVI-D connector (digital only) and DVI-I connector (digital + analog)]

DVI is a legacy connector found on older monitors and graphics cards. It carries video only — no audio. There are two variants you must know:

DVI-D (Digital only): Carries only a digital signal. You can identify it by the absence of the four analog pins arranged in a cross-shaped cluster around the flat blade.

DVI-I (Digital and Analog Integrated): Carries both digital and analog signals. You can identify it by the presence of the four analog pins in the cross-shaped cluster around the flat blade.

DVI-A (Analog only): Carries only analog video. Rarely seen; most legacy analog needs are handled by VGA.

A DVI-to-HDMI adapter or cable works because both carry digital signals. A DVI-I port can connect to a VGA monitor using a DVI-to-VGA adapter because the DVI-I connector carries the analog signal needed for VGA.

A DVI-D port cannot connect to a VGA monitor through a simple passive adapter — there is no analog signal on a DVI-D connector to pass to the VGA display.

#### VGA — Video Graphics Array

[SHOW COMPONENT: VGA connector — 15-pin, 3-row, trapezoidal, blue]

VGA is the oldest surviving display connector standard. It is a 15-pin, three-row, trapezoidal analog connector — typically colored blue. VGA carries only analog video and no audio. Because it is analog, signal quality degrades with cable length, and VGA cannot natively carry 4K signals at any refresh rate.

VGA is largely obsolete for new equipment. However, it is still found on projectors, older monitors, and some enterprise displays in legacy environments. A technician working in an organization with aging equipment will encounter VGA.

[PAUSE — summary]

Let me put the connectors side by side for the exam:

- HDMI: 19-pin trapezoidal, video + audio, no daisy-chain, version-dependent bandwidth
- DisplayPort: 20-pin one-angled-corner, video only from connector (audio embedded in signal), MST daisy-chain supported, highest PC monitor bandwidth
- DVI-D: digital only, no audio, legacy, can adapt to HDMI
- DVI-I: digital + analog, no audio, legacy, can adapt to VGA with passive adapter
- VGA: 15-pin three-row analog, video only, no audio, fully legacy

Exam Tip: When you see a scenario about connecting multiple monitors to a single port, always select DisplayPort as the answer. HDMI, DVI, and VGA do not support MST."

---

### [16:00 - 19:30] Section 4: Resolution, Refresh Rate, and Cable Bandwidth

[SLIDE: "Resolution and Refresh Rate — The Numbers That Matter"]

"A display connector is only useful if it can carry the signal your monitor needs. Let's connect the physical connector to the performance specifications.

[SHOW COMPONENT: Resolution comparison slide — 1080p, 1440p, 4K pixel counts]

#### Resolution

Resolution is measured in pixels — the total number of picture elements arranged in a grid. The common standard resolutions are:

- 1920 x 1080 (1080p / FHD): 2,073,600 pixels per frame
- 2560 x 1440 (1440p / QHD): 3,686,400 pixels per frame
- 3840 x 2160 (4K / UHD): 8,294,400 pixels per frame

Moving from 1080p to 4K multiplies the pixel count by four. That increases the data the cable must carry with every frame.

#### Refresh Rate

Refresh rate is measured in Hz — the number of times per second the display updates its image. At 60Hz the display draws 60 frames per second. At 144Hz it draws 144 frames per second. Higher refresh rates produce smoother motion.

The relationship between resolution and refresh rate determines the bandwidth requirement. A 4K signal at 144Hz requires approximately 44 Gbps of bandwidth — significantly more than a 1080p signal at 60Hz (approximately 4.5 Gbps).

#### Matching Cable Version to Requirements

This is where cable version becomes critical:

- HDMI 1.4: approximately 8.16 Gbps effective bandwidth — supports 4K only at 30Hz
- HDMI 2.0: approximately 14.4 Gbps — supports 4K at 60Hz
- HDMI 2.1: approximately 42.6 Gbps — supports 4K at 120Hz, 8K at 60Hz
- DisplayPort 1.4: approximately 25.92 Gbps — supports 4K at 144Hz, 8K at 60Hz
- DisplayPort 2.0: approximately 77.4 Gbps — supports 4K at 240Hz and beyond

[PAUSE — exam trap]

A user connects a 4K monitor using an HDMI cable but the display is stuck at 1080p or 4K at 30Hz. The most likely cause is an HDMI 1.4 cable that cannot carry the required bandwidth for 4K at 60Hz. The fix is replacing the cable with an HDMI 2.0 or DisplayPort cable.

Exam Tip: The A+ exam will present a scenario where a monitor is not displaying at its advertised resolution and refresh rate, and the correct answer involves identifying the cable version as the limiting factor."

---

### [19:30 - 22:30] Section 5: Lab Preview and Exam Wrap-Up

[SLIDE: "Module 07 Lab Overview"]

"For this week's lab, you are going to do three things.

First, a connector identification exercise. You will be given descriptions and connector characteristics and must match them to the correct connector name, pin count, whether they carry audio, and whether daisy-chaining is supported. This mirrors A+ performance-based question format exactly.

Second, a resolution and refresh rate compatibility table. Given a set of scenarios — a monitor specification paired with a cable version — you will determine whether the combination will display at the advertised settings, and if not, identify the limiting factor and suggest the correct cable.

Third, a signal path tracing exercise. Given a multi-monitor setup diagram, you will trace the signal path from GPU to each display, identify which connectors are in use, and identify one configuration error.

[PAUSE]

Key takeaways for the exam:

One — HDMI carries video and audio. DisplayPort carries video only from the connector standpoint (audio is embedded in the DP signal), but importantly it supports MST for daisy-chaining. HDMI does not.

Two — DVI-D is digital only. DVI-I is digital and analog. The difference is the four analog pins in the cross-cluster. This distinction comes up in adapter questions.

Three — VGA is fully analog. DVI-D cannot adapt to VGA passively. DVI-I can, because DVI-I carries an analog signal.

Four — Cable version determines bandwidth. HDMI 1.4 limits 4K to 30Hz. HDMI 2.0 supports 4K at 60Hz. DisplayPort 1.4 supports 4K at 144Hz.

Five — For multi-monitor from one port: DisplayPort MST, not HDMI.

[OUTRO — instructor on camera]

That covers Module 07. Complete the reading guide and lab before attempting the quiz. Post your discussion by Wednesday night. Good luck, and I'll see you in the next module."

---

### End Card

- Complete the Reading Guide before the lab
- Submit Lab 07 via Canvas by the posted deadline
- Initial Discussion Post due Wednesday at 11:59 PM
- Quiz 07 available after the lab submission window closes
- Office hours: see Canvas for current schedule

---

### Additional Resources

- Professor Messer CompTIA A+ Core 1 Free Course (Display Technologies): [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- Professor Messer CompTIA A+ Study Notes (220-1101): [https://www.professormesser.com/](https://www.professormesser.com/)
- CompTIA A+ Exam Objectives (220-1101): [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)

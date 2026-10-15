# Video Script: Module 13 - Laptop Components and Disassembly

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course &bull; Module 13</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH" title="Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 1.3: Given a scenario, install or replace laptop components
**Estimated Duration:** 20-24 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1 — Introduction and Safety Foundation

<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Laptop Internal Architecture &amp; Safe Field Disassembly Protocol</text>

  <!-- Laptop Base Schematic -->
  <g transform="translate(40, 95)">
    <rect width="480" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="240" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Laptop Chassis Under-Panel Component Map</text>

    <!-- Battery -->
    <rect x="30" y="45" width="420" height="75" fill="#0f172a" stroke="#d9a74a" stroke-width="1.5" rx="4"/>
    <text x="240" y="75" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">Lithium-Ion / Li-Polymer Battery Pack</text>
    <text x="240" y="95" fill="#fca5a5" font-size="10" text-anchor="middle">⚠️ STEP 1: Disconnect Battery Connector Before Touching Any Internal Circuits!</text>
    <text x="240" y="110" fill="#94a3b8" font-size="9" text-anchor="middle">Inspect for swelling / pouch distension — replace immediately if deformed</text>

    <!-- Motherboard internals -->
    <g transform="translate(30, 130)">
      <!-- CPU & Heatpipe -->
      <rect x="0" y="0" width="130" height="90" fill="#0f172a" stroke="#ef4444" rx="4"/>
      <text x="65" y="25" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">BGA CPU &amp; Heatpipe</text>
      <line x1="20" y1="45" x2="110" y2="45" stroke="#d9a74a" stroke-width="4"/>
      <text x="65" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">Copper heatpipe to blower fan</text>

      <!-- SO-DIMM Slots -->
      <rect x="145" y="0" width="130" height="90" fill="#0f172a" stroke="#10b981" rx="4"/>
      <text x="210" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">SO-DIMM RAM</text>
      <rect x="160" y="38" width="100" height="15" fill="#334155" rx="2"/>
      <rect x="160" y="58" width="100" height="15" fill="#334155" rx="2"/>
      <text x="210" y="84" fill="#94a3b8" font-size="8" text-anchor="middle">Spring clips at 45° angle</text>

      <!-- M.2 SSD & Wi-Fi -->
      <rect x="290" y="0" width="130" height="90" fill="#0f172a" stroke="#38bdf8" rx="4"/>
      <text x="355" y="20" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">M.2 NVMe SSD (2280/2230)</text>
      <rect x="305" y="28" width="100" height="22" fill="#1e293b" rx="2"/>
      <text x="355" y="65" fill="#a855f7" font-size="10" font-weight="bold" text-anchor="middle">M.2 Wi-Fi / Bluetooth Card</text>
      <text x="355" y="80" fill="#cbd5e1" font-size="8" text-anchor="middle">Main (White) &amp; Aux (Black) Antennas</text>
    </g>

    <!-- Connectors -->
    <g transform="translate(30, 235)">
      <rect x="0" y="0" width="420" height="75" fill="#0f172a" rx="4"/>
      <text x="210" y="20" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">Flat Ribbon Cables &amp; ZIF (Zero Insertion Force) Sockets</text>
      <text x="20" y="42" fill="#94a3b8" font-size="10">• <b>ZIF Connectors:</b> Flip locking bail up gently; never pull cable with bail locked.</text>
      <text x="20" y="60" fill="#94a3b8" font-size="10">• <b>Wi-Fi Antennas:</b> Snap onto micro-coaxial U.FL/MHF4 connectors with spudger.</text>
    </g>
  </g>

  <!-- Disassembly Best Practices Checklist -->
  <g transform="translate(540, 95)">
    <rect width="270" height="325" fill="#1e293b" stroke="#cbd5e1" stroke-width="1.5" rx="6"/>
    <text x="135" y="25" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Field Disassembly Protocol</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="240" height="45" fill="#0f172a" rx="3"/>
      <text x="10" y="18" fill="#38bdf8" font-size="10" font-weight="bold">1. Screw Organization Tray</text>
      <text x="10" y="34" fill="#94a3b8" font-size="9">Label screw lengths and locations.</text>

      <rect x="0" y="52" width="240" height="45" fill="#0f172a" rx="3"/>
      <text x="10" y="70" fill="#10b981" font-size="10" font-weight="bold">2. Anti-Static Wrist Strap</text>
      <text x="10" y="86" fill="#94a3b8" font-size="9">Attach to grounded work mat.</text>

      <rect x="0" y="104" width="240" height="45" fill="#0f172a" rx="3"/>
      <text x="10" y="122" fill="#d9a74a" font-size="10" font-weight="bold">3. Plastic Spudger / Pry Tool</text>
      <text x="10" y="138" fill="#94a3b8" font-size="9">Never use metal tools on plastic tabs.</text>

      <rect x="0" y="156" width="240" height="45" fill="#0f172a" rx="3"/>
      <text x="10" y="174" fill="#ef4444" font-size="10" font-weight="bold">4. Battery Isolation First</text>
      <text x="10" y="190" fill="#94a3b8" font-size="9">Disconnect battery before cables.</text>

      <rect x="0" y="208" width="240" height="50" fill="#0f172a" rx="3"/>
      <text x="10" y="226" fill="#a855f7" font-size="10" font-weight="bold">5. Antenna Route Tracking</text>
      <text x="10" y="244" fill="#94a3b8" font-size="9">Route wires in chassis grooves.</text>
    </g>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ A+ Exam Warning: Mixing screw lengths during reassembly can puncture motherboards or crack palm rests!</text>
</svg>
</div>

**[SHOW COMPONENT: Title slide — "Module 13: Laptop Components and Disassembly"]**

Welcome to Module 13 of CIS-2320 Hardware Fundamentals. I am Professor Nash. Today we go inside the laptop — one of the most interesting and challenging areas of A+ hardware service. Laptops are different from desktops in one critical way: everything is smaller, more tightly integrated, and more fragile. The same upgrade or repair that takes five minutes on a desktop can take thirty minutes on a laptop because of the proprietary design, the miniaturized connectors, and the very specific order of operations required to disassemble without breaking anything.

Before we look at any component, I want to establish the one rule that governs all laptop service work.

**[PAUSE — display on full slide, large font: "STEP ONE: REMOVE THE BATTERY"]**

Before you touch anything inside a laptop — keyboard, RAM, Wi-Fi card, display, anything — you must remove or disconnect the battery first. Always. No exceptions. And before removing the battery, unplug the AC adapter. The battery is the last power source still connected to the system after you unplug from the wall, and if you short any circuit while the battery is connected, you can permanently damage the motherboard, injure yourself, or in a worst case, cause a lithium battery fire.

The CompTIA A+ exam tests this rule directly. If a scenario question asks what the first step is before replacing a laptop keyboard, the answer is not "remove the keyboard screws" — it is "disconnect the battery." Memorize this.

**[PAUSE — transition to section overview slide]**

---

## Section 2 — Laptop Battery Types and Removal Procedures

**[SHOW COMPONENT: Laptop underside — removable battery with sliding latch visible]**

There are two main laptop battery configurations you need to know: removable (user-accessible) and integrated (internal).

A removable battery sits in a bay on the underside of the laptop and is secured by a sliding latch or two latches. To remove it: close the laptop and flip it over. Locate the battery latch — often marked with a lock/unlock icon. Slide the latch to the release position and the battery pops out or can be lifted free. This design is common on older consumer laptops, corporate business laptops, and ruggedized laptops. No tools are required.

**[SHOW COMPONENT: Laptop with bottom panel removed — integrated battery connector visible on motherboard]**

An integrated battery is mounted internally, typically beneath the bottom panel, and does not have an external release. To disconnect it: power off the laptop completely and unplug the AC adapter. Remove the bottom panel screws — typically Phillips or Torx head. Lift the panel using a spudger or plastic pry tool starting at a corner. Once the panel is off, locate the battery connector. It is a small multi-wire JST-style connector seated in a socket on the motherboard. Insert a spudger or your fingernail under the connector and pry it straight up. Do not pull on the wires.

**[PAUSE — exam tip slide: "Removable: slide latch. Integrated: remove bottom panel, disconnect connector with spudger."]**

After disconnecting the battery, confirm the system is fully de-energized: press and hold the power button for five seconds to discharge any residual capacitor energy in the circuit. Now you can safely work on internal components.

---

## Section 3 — Wi-Fi Card, RAM, and M.2 Storage

**[SHOW COMPONENT: Interior of laptop — Wi-Fi card visible with two antenna cables]**

The laptop Wi-Fi card is typically a half-mini PCIe card in an older laptop or an M.2 form factor card in a modern laptop. The card seats in a dedicated slot on the motherboard and is retained by one small Phillips screw. What makes Wi-Fi card replacement unique compared to any other laptop component is the antenna cables.

**[SHOW COMPONENT: Close-up of MHF4 antenna connector on Wi-Fi card — snap-on style]**

The laptop has two or three thin coaxial antenna cables that run from the Wi-Fi card, through the hinge assembly, and up into the LCD lid where they connect to printed antenna traces or films embedded in the display bezel. These cables use MHF4 snap-on connectors — small circular connectors about 1.5 mm in diameter that press onto corresponding pins on the Wi-Fi card.

Here is the critical procedure: to remove an MHF4 antenna connector, place the tip of a non-conductive spudger or your fingernail under the connector body and pry it straight up off the pin. Do not grab the cable and pull. The cable is extremely thin coaxial — the outer shielding and inner conductor will separate from the connector if you pull the cable. If you break the connector, you are looking at routing a new antenna cable all the way through the hinge and lid assembly — a two-hour job on many laptops.

**[PAUSE — exam tip slide: "Antenna connectors: pry the connector body, NEVER pull the cable."]**

After disconnecting both antenna cables, remove the retaining screw. The card lifts out at an angle — the same angle at which it was seated in the slot. To install a replacement card, insert it at the same angle until it seats, secure the screw, then reconnect the antenna cables by pressing each connector firmly straight down onto its pin until you feel and hear a faint click.

**[SHOW COMPONENT: Laptop RAM slot — SO-DIMM module visible]**

Laptop RAM uses the SO-DIMM form factor — Small Outline Dual Inline Memory Module. SO-DIMMs are approximately half the length of desktop DDR4 or DDR5 DIMMs. They seat at an angle and are retained by two spring clips on the sides of the slot. To remove a SO-DIMM, press both spring clips outward simultaneously — the module pops up to about a 30-degree angle, then slide it straight out. Installation is the reverse: insert at the angle, press down until the clips lock.

Modern laptops increasingly use soldered RAM on the motherboard, which is not user-replaceable. Before ordering RAM for a customer's laptop, verify the service manual to confirm whether the RAM is socketed or soldered.

**[SHOW COMPONENT: M.2 slot — M.2 SSD card visible next to Wi-Fi card in same area]**

M.2 storage in a laptop uses the same removal procedure as a Wi-Fi card: one retaining screw, angled insertion. M.2 SSDs can be SATA or NVMe (PCIe) depending on the slot type. The slot keying (B key, M key, or B+M key) and the motherboard's supported protocols determine which M.2 drives are compatible. Always check the service manual before purchasing a replacement drive.

---

## Section 4 — LCD Display Replacement and DC Power Jack

**[SHOW COMPONENT: Laptop lid — bezel visible with rubber plug covering a screw hole]**

LCD display replacement is one of the more involved laptop repairs, but it follows a consistent process across most models. The display assembly consists of the LCD panel, backlight, the display bezel (the plastic frame around the screen), and the hinges that attach the lid to the palm rest.

Older displays used CCFL (Cold Cathode Fluorescent Lamp) backlighting. Everything made in the last decade uses LED backlighting, which is thinner, more power-efficient, and more reliable. The A+ exam references both, so know the distinction: CCFL = older, fluorescent, requires an inverter board; LED = modern, direct or edge-lit.

**[PAUSE — slide: "CCFL backlight = old, needs inverter. LED backlight = modern, no inverter."]**

The display panel connects to the motherboard via the video cable. Older laptops used LVDS (Low Voltage Differential Signaling) flat ribbon cables. Modern laptops use eDP (embedded DisplayPort) cables. Both cable types route from the motherboard, through the hinge assembly, and connect to the back of the LCD panel. The cable connector is typically a thin ZIF-style flat flex connector on the panel side.

**[SHOW COMPONENT: Display bezel removal — showing corner screw plug being lifted with spudger]**

To replace the display panel: begin by removing the rubber plugs covering the bezel screws — typically four to six screws around the perimeter of the bezel. Remove the screws. Use a spudger to pry the bezel away from the lid, starting at a corner and working around the perimeter — the bezel is held by plastic clips that release with gentle prying. Once the bezel is off, locate the retaining screws securing the panel to the lid frame (usually two to four screws, one per bracket). Disconnect the video cable from the back of the panel. On touchscreen models, also disconnect the digitizer flex cable. Lift the panel out.

Reverse the procedure for installation. Before reinstalling the bezel, power on the laptop with the new panel connected and verify the display works — it is far easier to re-seat a connector now than after the bezel is clipped back in place.

**[SHOW COMPONENT: DC power jack — functional vs damaged side-by-side illustration]**

The DC power jack — the barrel connector where the AC adapter plugs in — is the component that fails most often due to physical stress. Every time a user plugs in or unplugs the charger, or when the laptop is moved with the charger attached, the jack experiences mechanical stress. Over time the solder joints crack or the jack itself loosens.

The classic symptom is intermittent charging that changes depending on the angle the charger cable is held. If the laptop charges only when the cable is held in a specific position, or charges sometimes but not others, the DC power jack is the most likely culprit. Consistent no-charging regardless of angle points toward the AC adapter or the battery. Positional intermittent failure is the DC jack.

**[PAUSE — exam tip slide: "Charges only at certain angles = DC power jack failure, NOT battery failure."]**

DC power jack replacement requires either soldering (if the jack is directly mounted to the motherboard) or connector swapping (if the jack is on a daughter board connected by a small cable). Either way it requires more advanced disassembly than the components we covered earlier.

---

## Section 5 — ZIF Connectors, Keyboard Replacement, and Lab Preparation

**[SHOW COMPONENT: ZIF connector on motherboard — locking tab visible in closed and open position]**

ZIF connectors — Zero Insertion Force connectors — appear throughout laptops wherever flat flex cables connect to the motherboard or a sub-board. The keyboard, touchpad, and various sensor ribbons all use ZIF connectors. The connector has a small plastic locking bar that flips up 90 degrees to release the cable, and flips back down to lock it. When the bar is up, you can slide the ribbon cable out with essentially no force. When the bar is down, the cable is clamped firmly.

The most common technician error with ZIF connectors is trying to pull the cable while the lock bar is still down, which tears the cable or breaks the lock bar off the connector body. Before removing any flex cable, always verify the lock bar is in the open position.

**[SHOW COMPONENT: Laptop keyboard removal — retention clips along top edge being released]**

Keyboard replacement depends on the laptop model but follows one of two approaches. In older consumer designs, the keyboard is accessible from the top: a row of retention clips along the top edge of the keyboard release when you press them with a spudger, and the keyboard lifts slightly to reveal the ZIF connector on the motherboard. In most modern business and consumer designs, the keyboard is held by screws accessible from the bottom panel. Remove the bottom panel, remove the keyboard screws, re-seat the bottom panel temporarily, flip the laptop over, and the keyboard can be lifted from the top.

In either case: unlock the ZIF bar, slide the flex cable out, remove the old keyboard, insert the new keyboard's flex cable, lock the ZIF bar, and verify the keyboard works before fully reassembling.

**[PAUSE — slide: "Lab 13 preview — component identification, disassembly order, scenario analysis"]**

For this week's lab you will be identifying laptop components from diagrams, documenting the correct disassembly order for a given repair scenario, and analyzing real-world symptom scenarios to identify the failing component. Read through all three lab parts before starting.

---

## [21:30 - End] End Card

Thank you for watching Module 13. Before our next session:

Read the Reading Guide for Module 13 — it covers ESD protection, SO-DIMM vs DIMM, M.2 keying, and the full disassembly order table in more detail than we covered here.

Complete Lab 13 and submit to Canvas.

Take Quiz 13.

Post your initial Discussion 13 response by Wednesday at 11:59 PM and respond to two classmates by Sunday.

**[PAUSE — slide: "Module 13 Resources"]**

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 Study Notes — Laptop Hardware section: professormesser.com
- CompTIA A+ Exam Objectives (220-1101) — Domain 1.3: comptia.org
- Manufacturer service manuals — available through the laptop manufacturer's support site (search "[model] service manual PDF")

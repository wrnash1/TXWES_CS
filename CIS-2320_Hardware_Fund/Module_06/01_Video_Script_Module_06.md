# Video Script: Module 06 - Power Supplies and System Cooling

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Estimated Duration:** 22-24 minutes

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5 (Given a scenario, install and configure motherboards, CPUs, and add-on cards) and Domain 5.2 (Given a scenario, troubleshoot problems related to motherboards, RAM, CPUs, and power)

**Recorded by:** Professor Nash | Texas Wesleyan University

---

### Production Notes

SHOW COMPONENT cues in this script:

- [SHOW COMPONENT: ATX PSU held up to camera — label 80 Plus Gold sticker, modular cable ports, fan grill]
- [SHOW COMPONENT: 24-pin ATX motherboard power connector and matching motherboard header side-by-side]
- [SHOW COMPONENT: 4-pin and 8-pin EPS CPU power connectors labeled]
- [SHOW COMPONENT: 6-pin and 8-pin PCIe power connectors labeled]
- [SHOW COMPONENT: SATA power connector (15-pin) and 4-pin Molex connector side-by-side]
- [SHOW COMPONENT: Case airflow diagram slide — front intake, rear exhaust, top exhaust arrows]
- [SHOW COMPONENT: Fan label showing airflow arrow and rotation arrow directions]

Key Exam Traps to call out explicitly:

- "The 80 Plus rating affects how much power is drawn from the wall — it does NOT change the DC output to components."
- "A 500W PSU and a 600W PSU of the same efficiency both deliver their rated wattage to the system — bigger PSU does not mean more power is pushed to components."
- "The 24-pin ATX connector powers the motherboard. The 4/8-pin EPS connector powers the CPU. These are different connectors — mixing them up is a real field mistake."
- "Fan orientation matters — a fan installed backwards acts as exhaust when it should be intake."

Safety Notes:

- PSUs retain lethal capacitor charge for several minutes after being unplugged — never open a PSU
- Always power off and unplug the system before connecting or disconnecting any PSU cable
- Touch a grounded metal surface or use an antistatic wrist strap before handling the motherboard or RAM
- Do not operate a system with the side panel removed in a dusty environment for extended periods

---

### [00:00 - 02:30] Section 1: Introduction — Why Power and Cooling Are Critical

[INSTRUCTOR ON CAMERA — title card visible: "Module 06: Power Supplies and System Cooling"]

"Welcome back, everyone. I'm Professor Nash, and today's module covers two topics that are absolutely foundational to every PC build and troubleshooting scenario: power supplies and system cooling.

Here is a perspective I want you to carry through this whole lesson. Every single component in a PC — the CPU, the GPU, the RAM, the drives, the motherboard logic — runs on DC power converted from the AC power coming from the wall. If that conversion is done wrong, or if the power delivery is inadequate, nothing in the system works reliably. And once those components are running, they generate heat — and if that heat is not removed efficiently, those same components will throttle, fail, or catch fire.

[PAUSE]

Power and cooling are not glamorous topics. But they are the reason a system runs stably for five years or dies after six months. A good technician takes these seriously on every build.

By the end of this module you will be able to calculate an appropriate PSU wattage for a given system, identify all major PSU connectors and what they power, explain 80 Plus efficiency ratings, distinguish modular from non-modular PSUs, and describe a correct case airflow strategy. Let's get into it.

Exam Tip: Domain 3.5 and Domain 5.2 both reference PSU connectors and power-related troubleshooting. Connector identification — knowing which cable goes to which component — is a core A+ performance-based question skill."

---

### [02:30 - 08:30] Section 2: PSU Wattage and Efficiency

[SLIDE: "Choosing the Right PSU"]

"Let's start with wattage, because choosing the correct PSU capacity is the first decision in any build.

#### Wattage — How Much Power Does Your System Need?

Every component in a PC draws a certain amount of power, measured in watts. The CPU and GPU are the biggest consumers. A mid-range gaming CPU might draw 65-125W; a high-end CPU can draw 150-250W under full load. A mid-range GPU draws 150-200W; a high-end gaming GPU can draw 300-450W. RAM, storage, and fans add a modest amount — typically 20-50W total for a full system.

[SHOW COMPONENT: ATX PSU held up to camera — label 80 Plus Gold sticker, modular cable ports, fan grill]

The standard practice is to add up the Thermal Design Power (TDP) ratings for all components, then add a 20 to 30 percent headroom buffer. That buffer ensures the PSU never operates near its maximum rated capacity, which would reduce its efficiency and lifespan. For example, a system with an estimated 420W total draw should have at least a 550-600W PSU.

[PAUSE]

Why not just buy a 1000W PSU for everything? Because a PSU operates most efficiently — and most quietly — when loaded to about 50-80% of its rated capacity. A massively oversized PSU running at 20% load actually operates less efficiently than a correctly sized one. It also wastes money on a component you do not need.

#### 80 Plus Efficiency Ratings

The 80 Plus certification program tests PSU efficiency at 20%, 50%, and 100% of rated load. A PSU that is not 80 Plus certified may convert only 70-75% of AC input to usable DC output — the rest is lost as heat inside the PSU itself.

The tiers are: 80 Plus (80% efficient), Bronze (82-85%), Silver (85-88%), Gold (87-90%), Platinum (89-92%), and Titanium (94%+). Higher efficiency means lower electricity costs, less heat generated inside the PSU, and quieter fan operation because the PSU fan does not have to work as hard.

[PAUSE — exam trap]

Here is the key exam trap. A 500W 80 Plus Gold PSU and a 500W 80 Plus Bronze PSU both deliver exactly 500W of DC output to the system components. The efficiency rating only affects how much AC power is drawn from the wall outlet. It does not make one PSU 'more powerful' than the other for the system. Both deliver 500W. The gold one just wastes less electricity getting there.

Exam Tip: The A+ exam will describe an efficiency rating and ask what it means. The correct answer always involves how much AC power is drawn from the wall — not how much DC power is delivered to the system."

---

### [08:30 - 13:30] Section 3: PSU Types and Connectors

[SLIDE: "PSU Connectors — Know Every One"]

"Let's go through the connector types. This is where the exam points live.

#### Modular vs. Non-Modular PSUs

A non-modular PSU has all cables permanently attached. The cable bundle can be large and unwieldy, and unused cables must be tucked away inside the case whether you need them or not.

A semi-modular PSU has the essential cables — the 24-pin ATX and CPU power connector — permanently attached. All other cables (PCIe, SATA, Molex) are detachable. This is a reasonable compromise for most builds.

A fully modular PSU has every cable detachable. You install only the cables your system actually needs, which dramatically improves cable management and airflow inside the case. Fully modular PSUs are more expensive but are the preferred choice for visible or performance-focused builds.

[PAUSE]

#### The 24-pin ATX Connector

[SHOW COMPONENT: 24-pin ATX motherboard power connector and matching motherboard header side-by-side]

The 24-pin ATX connector is the main motherboard power connector. It is the large, wide connector that plugs into a matching 24-pin header on the motherboard. It supplies the 3.3V, 5V, 12V, and standby power rails that run the motherboard logic, PCIe slots, USB headers, and other integrated circuits. This is always the first cable you connect in a build.

Some older motherboards used a 20-pin ATX connector. Modern 24-pin connectors are typically designed so the last 4 pins are detachable, making them backward-compatible with older 20-pin boards.

#### The 4/8-pin EPS CPU Power Connector

[SHOW COMPONENT: 4-pin and 8-pin EPS CPU power connectors labeled]

The CPU requires dedicated power delivered through a separate connector near the top-left corner of the motherboard — not through the 24-pin connector. This is the EPS connector, also called the CPU power connector or ATX12V connector. It provides 12V power directly to the CPU voltage regulator modules on the motherboard.

Budget and mainstream boards use a 4-pin CPU connector. High-end and overclocking boards use an 8-pin (or dual 8-pin) connector. Missing this connector is one of the most common mistakes in new builds — the system will not POST if the CPU power connector is not seated.

[PAUSE — exam point]

This is a real field error I have seen. Technicians plug in the 24-pin and wonder why the system will not turn on. They forgot the 4 or 8-pin CPU connector. Know where this connector goes.

#### The 6/8-pin PCIe Power Connector

[SHOW COMPONENT: 6-pin and 8-pin PCIe power connectors labeled]

The PCIe slot on the motherboard can only supply 75W to a graphics card through the slot itself. Any GPU that requires more than 75W needs one or more dedicated PCIe power connectors from the PSU. Entry-level GPUs may require one 6-pin (75W) or one 8-pin (150W) connector. High-end GPUs may require two 8-pin connectors or a proprietary 16-pin connector.

#### SATA Power and Molex

[SHOW COMPONENT: SATA power connector (15-pin) and 4-pin Molex connector side-by-side]

The 15-pin SATA power connector supplies power to all SATA drives — hard drives and SATA SSDs. The 4-pin Molex connector is a legacy connector from the IDE era, still found on some case fans, optical drives in older systems, and LED controllers. You will not connect Molex to any modern drive, but the A+ exam still expects you to recognize it.

Exam Tip: On the A+ exam, connector identification questions will describe a component and ask which PSU cable it requires. Memorize this: 24-pin for motherboard, 4/8-pin EPS for CPU, 6/8-pin PCIe for GPU, 15-pin SATA for drives, 4-pin Molex for legacy accessories."

---

### [13:30 - 19:00] Section 4: Case Airflow and Thermal Management

[SLIDE: "Cooling — Keep the Heat Moving"]

"Now let's talk about case airflow. Thermal management is the difference between a system that runs stably for years and one that throttles under load or dies from heat stress.

#### The Airflow Principle

[SHOW COMPONENT: Case airflow diagram slide — front intake, rear exhaust, top exhaust arrows]

Heat rises. Cool air is denser and sinks. A properly designed case leverages both of these facts. The goal is to create a directional airflow path that moves cool air from outside the case, across the heat-generating components (CPU, GPU, RAM, VRMs), and out of the case as warm air.

The standard airflow path in an ATX case is front-to-back and bottom-to-top:

- Front fans: intake (drawing cool air in from the front panel mesh)
- Bottom fans: intake (drawing cool air up from below)
- Rear fans: exhaust (pushing warm air out directly behind the motherboard)
- Top fans: exhaust (warm air rises and exits through the top vents)

#### Fan Orientation

[SHOW COMPONENT: Fan label showing airflow arrow and rotation arrow directions]

Every case fan has a label on one side showing two arrows. One arrow indicates the direction of airflow; the other indicates the direction of blade rotation. The side the airflow arrow points away from is the intake side — that is the side that should face the source of cool air. The side the arrow points toward is where warm air exits.

When you install a fan, you need to know which direction the air moves so you can mount it correctly. A front intake fan should have its airflow arrow pointing into the case. A rear exhaust fan should have its airflow arrow pointing out of the case. Reversing a fan turns an intake into an exhaust and disrupts the entire thermal path.

[PAUSE]

#### Positive vs. Negative Pressure

If a case has more intake fan area than exhaust fan area, it runs positive pressure — air is forced in faster than it exits, which means air exits only through filtered vents and not through random gaps. This reduces dust accumulation inside the case.

If a case has more exhaust than intake, it runs negative pressure — air is pulled in through any unfiltered gap or seam in the case, which accelerates dust buildup on components.

Balanced airflow — equal intake and exhaust — is a common recommendation, but slight positive pressure is generally preferred in environments where dust management is important.

#### CPU Coolers and Thermal Paste

The CPU heatsink and fan (air cooler) or all-in-one liquid cooler (AIO) sits directly on the CPU and transfers heat away from the processor die. Thermal paste fills the microscopic air gaps between the CPU heat spreader and the cooler base, dramatically improving heat transfer. Most stock coolers come with pre-applied thermal paste. Aftermarket coolers require application of thermal paste before installation.

Exam Tip: The A+ exam may describe a system that runs hot with all fans spinning normally. One common cause is incorrect fan orientation — an intake fan installed backwards. Another is a clogged air filter blocking the front intake. Both are scenario questions that require understanding of airflow direction."

---

### [19:00 - 22:30] Section 5: Lab Preview and Exam Wrap-Up

[SLIDE: "Module 06 Lab Overview"]

"For this week's lab, you are going to do three things.

First, you will complete a PSU connector identification table, matching connector names to their pin counts, voltage rails, and the components they power. This mirrors the performance-based question format on the A+ exam.

Second, you will work through a wattage calculation exercise. I give you the TDP specifications for a CPU, GPU, and peripherals, and you calculate the minimum recommended PSU wattage including a 25% headroom buffer. This is a skill every technician uses in real builds.

Third, you will analyze a case airflow diagram with intentional errors — fans installed in the wrong orientation — and identify what the correct configuration should be, then explain the thermal consequence of each error.

[PAUSE]

Let me leave you with the key takeaways for the exam.

One — wattage headroom. Size your PSU at 125-130% of your estimated system load, not at the exact load.

Two — efficiency ratings affect AC input, not DC output to components. Do not confuse them.

Three — know your connectors: 24-pin for motherboard, 4/8-pin EPS for CPU, 6/8-pin PCIe for GPU, 15-pin SATA for drives.

Four — missing the CPU power connector is one of the most common build errors. If a system won't POST after a fresh build, check the CPU power cable first.

Five — fan orientation determines airflow direction. Use the label arrows to verify intake versus exhaust before mounting.

[OUTRO — instructor on camera]

That covers Module 06. Complete the reading guide and lab before attempting the quiz. Post your discussion response by Wednesday night. Take care, everyone."

---

### End Card

- Complete the Reading Guide before the lab
- Submit Lab 06 via Canvas by the posted deadline
- Initial Discussion Post due Wednesday at 11:59 PM
- Quiz 06 available after the lab submission window closes
- Office hours: see Canvas for current schedule

---

### Additional Resources

- Professor Messer CompTIA A+ Core 1 Free Course (Power Supplies): [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- Professor Messer CompTIA A+ Study Notes (220-1101): [https://www.professormesser.com/](https://www.professormesser.com/)
- CompTIA A+ Exam Objectives (220-1101): [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)

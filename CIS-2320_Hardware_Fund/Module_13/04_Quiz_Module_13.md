# Quiz: Module 13 - Laptop Components and Disassembly
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Why must you carefully disconnect laptop antenna wires when swapping a Wi-Fi card?
*   A) The card will catch fire if wires cross
*   B) They supply power to the LCD backlight
*   C) They are fragile coax connections required for wireless reception
*   D) Wires are soldered and cannot be removed
*   **Correct Answer:** C) Antenna wires carry the radio signals from the LCD bezel and are attached via tiny, fragile snap-on connector pins.
*   **Distractor Analysis:**
    *   *Why correct:* Antenna wires carry the radio signals from the LCD bezel and are attached via tiny, fragile snap-on connector pins.
    *   Antenna wires carry RF signals, not electrical power, and do not pose fire hazards.

---

**Question 2**
In the context of laptop hardware, which of the following most accurately describes **LCD screen replacement**?
*   A) A repair procedure requiring removal of the display bezel, disconnection of the LVDS or eDP video cable (and digitizer flex cable on touchscreen models), and separation of the panel from the lid assembly — all hinges, bezel clips, and flex cables must be handled carefully to avoid cracking the panel or damaging connectors.
*   B) A repair that requires only removing the single retaining screw on the back of the display lid and sliding the LCD panel out of the chassis, as all laptop displays use a universal HDMI connector that unplugs with no additional cable routing.
*   C) A procedure exclusive to CCFL-backlit displays manufactured before 2012; modern LED-backlit laptop displays are fused to the chassis and cannot be replaced — the entire laptop must be replaced when the display fails.
*   D) A straightforward swap identical to replacing a desktop monitor, where the display detaches via a standard DisplayPort cable and requires no disassembly of the lid assembly or bezel.
*   **Correct Answer:** A) A repair procedure requiring removal of the display bezel, disconnection of the LVDS or eDP video cable (and digitizer flex cable on touchscreen models), and separation of the panel from the lid assembly — all hinges, bezel clips, and flex cables must be handled carefully to avoid cracking the panel or damaging connectors.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the complexity of laptop LCD replacement — bezel removal, video cable disconnection, and careful handling of flex cables and hinges are all required steps tested in A+ laptop hardware scenarios.
    * *Why B is incorrect:* Laptop displays do not use HDMI connectors internally; they use LVDS (older) or eDP (modern) video cables, which are proprietary flat flex cables routed through the hinge and require full bezel disassembly to access.
    * *Why C is incorrect:* LED-backlit laptop displays are absolutely replaceable; most modern laptop display panels can be sourced and swapped by a technician, and the A+ exam specifically tests this repair procedure.
    * *Why D is incorrect:* Laptop displays are integrated into the lid assembly and are not comparable to external desktop monitors; disassembly of the bezel and lid is always required, and the internal connection is not a standard DisplayPort cable.


---

**Question 3**
A technician needs to replace a laptop's internal Wi-Fi card. After removing the battery and back panel, the technician finds two thin cables attached to the card labeled "Main" and "Aux." What are these cables, and what is the correct procedure for removing them?
*   A) These are the SATA data cables for the internal SSD; they should be unplugged by gripping the cable firmly and pulling straight back with moderate force
*   B) These are the wireless antenna coaxial cables routed from the LCD bezel; they should be disconnected by gently prying each snap-on connector off the card using a non-conductive spudger, not by pulling the cable itself
*   C) These are the display backlight power cables; they must be cut with scissors and resoldered to the replacement card because they are permanently fused to the Wi-Fi module
*   D) These are USB data cables connecting the Wi-Fi card to the motherboard's USB controller; they unplug by pressing the release tab on each connector and pulling straight up
*   **Correct Answer:** B) These are the wireless antenna coaxial cables routed from the LCD bezel; they should be disconnected by gently prying each snap-on connector off the card using a non-conductive spudger, not by pulling the cable itself
*   **Distractor Analysis:**
    * *Why B is correct:* Laptop Wi-Fi cards use MHF4 snap-on coaxial connectors for the antenna leads; pulling the cable instead of prying the connector body risks tearing the antenna trace or breaking the connector, which would require replacing the entire antenna assembly routed through the lid.
    * *Why A is incorrect:* SATA data cables use a different connector type entirely and are not present on a Wi-Fi card; Wi-Fi cards use Mini-PCIe or M.2 slots, not SATA.
    * *Why C is incorrect:* Antenna cables are separate from the backlight circuit and are never cut during a Wi-Fi card swap; they are reusable and transfer to the replacement card by snapping the connectors onto the new card's antenna ports.
    * *Why D is incorrect:* Laptop Wi-Fi antenna connectors are coaxial RF connections, not USB connectors; they have no release tab and are removed by careful prying of the connector body.


---

**Question 4**
A user reports that their laptop charges intermittently — sometimes charging normally, sometimes showing no charge even with the AC adapter plugged in. The issue seems related to the angle of the power cable. Which component is most likely failing?
*   A) The laptop battery — lithium-ion batteries develop internal cell failures that cause them to accept charge only when held at specific orientations
*   B) The DC power jack — a damaged or loose power jack creates an intermittent electrical connection that breaks when the connector shifts, causing inconsistent charging
*   C) The AC adapter — the adapter's internal transformer overheats and throttles power output based on the cable routing angle to prevent damage
*   D) The voltage regulator on the motherboard — regulators fail progressively and accept input power only within a narrow voltage range that varies depending on connector position
*   **Correct Answer:** B) The DC power jack — a damaged or loose power jack creates an intermittent electrical connection that breaks when the connector shifts, causing inconsistent charging
*   **Distractor Analysis:**
    * *Why B is correct:* The symptom of charging only at certain angles is the classic presentation of a physically damaged or loose DC power jack; the barrel connector makes intermittent contact inside a cracked or worn jack, and the charging state changes as the connector moves.
    * *Why A is incorrect:* Battery cell failures cause capacity loss, rapid discharge, or failure to hold a charge — not positional charging behavior. Batteries do not respond to physical orientation in the manner described.
    * *Why C is incorrect:* AC adapters deliver a fixed voltage regardless of cable routing angle; thermal throttling is not a feature of AC adapters and would result in consistent reduced output, not positional intermittent failure.
    * *Why D is incorrect:* A failing voltage regulator would cause consistent power delivery issues or system instability, not a symptom that varies with cable angle at the input connector.


---

**Question 5**
Before performing any internal service on a laptop — including replacing the keyboard, Wi-Fi card, or RAM — what is the mandatory first step a technician must always perform?
*   A) Update the BIOS/UEFI firmware to the latest version to ensure the replacement component is recognized correctly after reinstallation
*   B) Disconnect or remove the battery (and unplug the AC adapter) to eliminate all power from the system before touching any internal components
*   C) Run a full virus scan on the laptop to ensure no malware interferes with hardware detection after the repair is complete
*   D) Connect the laptop to an ESD mat but leave the battery installed so the mat has a complete ground path through the system's power circuit
*   **Correct Answer:** B) Disconnect or remove the battery (and unplug the AC adapter) to eliminate all power from the system before touching any internal components
*   **Distractor Analysis:**
    * *Why B is correct:* Disconnecting the battery is the first and most critical step in all laptop internal service — it removes residual power that could cause short circuits, damage components, or injure the technician. The AC adapter must also be unplugged before battery removal.
    * *Why A is incorrect:* BIOS firmware updates are performed as a software maintenance step, not as a prerequisite to physical hardware service; updating firmware before repair is not required and is unrelated to safe disassembly procedure.
    * *Why C is incorrect:* A virus scan is a software security procedure with no relevance to safe physical disassembly; malware does not affect hardware recognition in the manner implied and is never a step in a hardware repair workflow.
    * *Why D is incorrect:* The battery should never remain installed during internal service; leaving the battery connected defeats the purpose of ESD protection because powered components can still be damaged by electrical discharge or accidental short circuits regardless of the ESD mat connection.

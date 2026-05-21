# Quiz: Module 07 - Display Technologies and Connectors
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which display connector supports daisy-chaining multiple monitors together from a single source output?
*   A) HDMI
*   B) DisplayPort
*   C) VGA
*   D) DVI
*   **Correct Answer:** B) DisplayPort supports Multi-Stream Transport (MST), enabling monitor daisy-chaining.
*   **Distractor Analysis:**
    *   *Why correct:* DisplayPort supports Multi-Stream Transport (MST), enabling monitor daisy-chaining.
    *   HDMI does not natively support daisy-chaining. VGA and DVI are legacy interfaces.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes **HDMI vs DisplayPort vs DVI**?
*   A) Three digital video connector standards where HDMI carries both video and audio over a single cable and is the most common consumer standard; DisplayPort supports higher refresh rates and enables monitor daisy-chaining via MST; and DVI is a legacy digital-only (DVI-D) or digital-and-analog (DVI-I) connector found on older hardware.
*   B) Three audio interface standards that determine whether a monitor's built-in speakers receive digital surround sound, stereo PCM, or analog audio signals from the connected source device.
*   C) Three software rendering APIs — HDMI handles hardware-accelerated 2D graphics, DisplayPort manages 3D pipeline shaders, and DVI provides the legacy DirectX compatibility layer for older display drivers.
*   D) Three types of monitor backlight technologies — HDMI uses LED edge lighting, DisplayPort uses full-array local dimming, and DVI uses cold-cathode fluorescent (CCFL) backlighting.
*   **Correct Answer:** A) Three digital video connector standards where HDMI carries both video and audio over a single cable and is the most common consumer standard; DisplayPort supports higher refresh rates and enables monitor daisy-chaining via MST; and DVI is a legacy digital-only (DVI-D) or digital-and-analog (DVI-I) connector found on older hardware.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the physical connector standards, their signal types, and their primary use cases as tested on the CompTIA A+ exam.
    * *Why B is incorrect:* HDMI, DisplayPort, and DVI are video signal interfaces, not audio routing standards; while HDMI does carry audio, all three are categorized as display connectors.
    * *Why C is incorrect:* HDMI, DisplayPort, and DVI are hardware connector standards, not software rendering APIs; graphics APIs are separate technologies (DirectX, OpenGL, Vulkan).
    * *Why D is incorrect:* These connectors define how signals are transmitted between GPU and monitor, not how the monitor's backlight is constructed internally.


---

**Question 3**
A user connects a new 4K monitor to their PC using an HDMI cable but the monitor displays only 1080p at 60Hz. The monitor supports 4K@60Hz and the GPU supports 4K output. What is the most likely cause?
*   A) The monitor's internal scaler is set to 1080p mode and must be changed via the monitor's OSD menu
*   B) The PC's graphics driver needs to be reinstalled before 4K resolution becomes available over any connector
*   C) The HDMI cable is HDMI 1.4, which is limited to 4K@30Hz; a 4K@60Hz signal requires HDMI 2.0 or newer
*   D) DisplayPort can carry 4K@60Hz but HDMI is fundamentally incapable of supporting 4K at any refresh rate
*   **Correct Answer:** C) The HDMI cable is HDMI 1.4, which is limited to 4K@30Hz; a 4K@60Hz signal requires HDMI 2.0 or newer
*   **Distractor Analysis:**
    * *Why C is correct:* HDMI 1.4 supports 4K resolution but only at 30Hz; achieving 4K@60Hz requires an HDMI 2.0 cable and port, which provides the necessary 18 Gbps bandwidth.
    * *Why A is incorrect:* While monitor OSD settings can affect displayed resolution, a cable bandwidth limitation is the more likely technical bottleneck when the system is limited to exactly 1080p@60Hz.
    * *Why B is incorrect:* Driver reinstallation would not resolve a hardware bandwidth limitation imposed by the cable version; the cable is the constraining factor.
    * *Why D is incorrect:* HDMI 2.0 and HDMI 2.1 fully support 4K; HDMI 2.1 supports up to 4K@120Hz and 8K. The limitation is version-specific, not connector-type inherent.


---

**Question 4**
A technician needs to connect three monitors to a single DisplayPort output on a GPU. The monitors each have one DisplayPort input and one HDMI input. Which configuration correctly enables all three monitors from the one DisplayPort output?
*   A) Connect the first monitor to DisplayPort, then use the monitor's HDMI output port to chain to the second monitor, and the second's HDMI output to chain to the third
*   B) Use a DisplayPort MST hub to split the single DisplayPort signal into three separate DisplayPort connections, one to each monitor
*   C) Connect the first monitor via DisplayPort and the remaining two via a dual-HDMI splitter cable plugged into the DisplayPort port using a passive adapter
*   D) Run three separate DisplayPort cables from the GPU's single DisplayPort port to each monitor using a Y-splitter cable
*   **Correct Answer:** B) Use a DisplayPort MST hub to split the single DisplayPort signal into three separate DisplayPort connections, one to each monitor
*   **Distractor Analysis:**
    * *Why B is correct:* A DisplayPort MST (Multi-Stream Transport) hub uses the MST protocol to send multiple independent video streams over one cable, then splits them to separate monitor outputs — the correct solution for multi-monitor from one DP port.
    * *Why A is incorrect:* Consumer monitors have HDMI input ports, not HDMI output ports; monitors cannot pass-through or chain HDMI signals to other monitors.
    * *Why C is incorrect:* A passive DisplayPort-to-HDMI adapter carries only a single video signal; it cannot split into two HDMI outputs, and HDMI does not support MST chaining.
    * *Why D is incorrect:* A DisplayPort port outputs one signal stream; a Y-splitter would duplicate the same image to all monitors (mirror only) using SST, not extend independently, and may not function at all depending on GPU support.


---

**Question 5**
A gaming monitor is advertised as supporting 240Hz refresh rate and 1ms response time. A technician advises the buyer that achieving the full 240Hz benefit requires more than just the monitor. What additional requirement must be met?
*   A) The GPU must output at least 240 frames per second in the game being played, and the cable must support the bandwidth required for the resolution and refresh rate combination
*   B) The monitor must be connected via HDMI because DisplayPort cannot carry refresh rates above 144Hz to any display at any resolution
*   C) The CPU must have a minimum of 8 cores because single-threaded performance alone determines the monitor's maximum achievable refresh rate
*   D) The operating system must be set to a 240Hz power plan profile in Windows Advanced Display Settings before the monitor can unlock its full refresh rate
*   **Correct Answer:** A) The GPU must output at least 240 frames per second in the game being played, and the cable must support the bandwidth required for the resolution and refresh rate combination
*   **Distractor Analysis:**
    * *Why A is correct:* A 240Hz monitor only delivers 240 unique frames per second if the GPU is actually rendering and outputting 240 fps; additionally, a cable with sufficient bandwidth (e.g., DisplayPort 1.4 or HDMI 2.1) is required to carry that signal at the target resolution.
    * *Why B is incorrect:* DisplayPort supports significantly higher refresh rates than HDMI in most versions; DisplayPort 1.4 supports 1440p@240Hz, and HDMI 2.1 also supports high refresh rates — neither is universally limited to 144Hz.
    * *Why C is incorrect:* Core count does not directly determine frame output rate; GPU performance and game engine optimization are the primary frame rate determinants, not CPU core count alone.
    * *Why D is incorrect:* Windows Advanced Display Settings is where the refresh rate is selected, but the operating system setting does not "unlock" the monitor's capability — the hardware must support the rate and the GPU must output it.


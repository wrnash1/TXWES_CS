# Reading Guide: Module 09 - Peripheral Devices and Interfaces
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 09 - Peripheral Devices and Interfaces**! This module covers the external connectivity standards used to attach input devices, storage, displays, and security hardware to a PC. You will learn the USB version hierarchy, the Thunderbolt interface, KVM switches for multi-system desk setups, and authentication peripherals such as smart card readers and biometric scanners. These topics appear on the **CompTIA A+ Core 1 (220-1101)** exam under hardware and connectivity domains.

As a technician, you must be able to identify USB connector types by appearance, explain speed differences between USB versions, and advise users on the correct cable or adapter for a given peripheral. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **USB standards (2.0, 3.0, Type-C)**: USB 2.0 (Hi-Speed) transfers data at up to 480 Mbps and uses Type-A, Type-B, Mini, or Micro connectors. USB 3.0 (SuperSpeed) transfers at up to 5 Gbps and is identified by blue-colored ports and connectors; USB 3.1 Gen 2 doubles this to 10 Gbps. USB Type-C is a reversible connector form factor (not a speed standard) that can carry USB 2.0, USB 3.x, or Thunderbolt signals depending on the host port and cable — the connector shape alone does not guarantee high speed.
*   **Thunderbolt**: Thunderbolt is a high-speed interface developed by Intel that uses the USB Type-C physical connector on Thunderbolt 3 and 4. Thunderbolt 3 and 4 support up to 40 Gbps data transfer, can carry DisplayPort video, USB data, and PCIe signals simultaneously over a single cable, and can supply up to 100W of power for laptop charging. Thunderbolt ports are identified by a lightning bolt icon. Thunderbolt cables are not interchangeable with standard USB-C cables for high-speed Thunderbolt features, though a Thunderbolt port will accept standard USB-C devices at USB speeds.
*   **KVM switches**: A KVM (Keyboard, Video, Mouse) switch allows a single keyboard, monitor, and mouse to control two or more computers by physically switching the USB and video connections between systems. KVM switches eliminate the need for duplicate peripherals when working with multiple machines on one desk. Enterprise KVM switches can manage dozens of servers from a single console; consumer models typically handle two to four systems and include a button or hotkey combination to toggle between connected computers.
*   **smart card readers and biometric scanners**: A smart card reader is a peripheral that authenticates users by reading a chip embedded in a physical card — common in government and enterprise environments for multi-factor authentication (something you have). A biometric scanner authenticates users based on physical characteristics: fingerprint scanners, iris scanners, and facial recognition cameras are the most common types. Both devices require driver installation and integrate with the operating system's authentication framework (Windows Hello, PIV/CAC card authentication). Both represent "something you have" or "something you are" authentication factors.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.2):** The A+ exam tests USB speed identification. Memorize: USB 2.0 = 480 Mbps, USB 3.0 = 5 Gbps (blue ports), USB 3.1 Gen 2 = 10 Gbps, Thunderbolt 3/4 = 40 Gbps. Scenario questions commonly describe a peripheral performing slower than expected and ask you to identify the bottleneck — always check whether the cable or port matches the required USB generation.
*   **Scenario Trap:** A common A+ distractor uses a USB Type-C connector to imply Thunderbolt or USB 3.x speeds. Remember: Type-C is a connector shape, not a speed standard. A USB Type-C port may deliver USB 2.0 speeds (480 Mbps) if that is what the host controller supports. Read the scenario carefully for the actual USB generation, not just the connector type.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers USB standards, Thunderbolt, and peripheral devices with connector identification visuals. Navigate to the peripheral devices section for USB speed comparison charts and connector diagrams: [Professor Messer's CompTIA A+ Core 1 Course — Peripheral Devices](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Pay close attention to the USB version comparison table.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the peripheral devices and interfaces section in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on USB standards, Thunderbolt, KVM switches, and authentication peripherals.
*   **Required Video:** Watch the video lecture on peripheral devices and interfaces from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering USB connector identification, speed differences between versions, and Thunderbolt capabilities.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a USB 3.0 external drive for fast transfer rates**: Connect a USB 3.0 external drive to both a USB 2.0 port and a USB 3.0 (blue) port. Observe the transfer speed difference in each connection. Confirm the drive is recognized at SuperSpeed (5 Gbps) when connected to the correct port using Device Manager.
*   **Set up a KVM switch to share one monitor/keyboard between two machines**: Connect two computers to a KVM switch using the appropriate video (HDMI or DisplayPort) and USB cables. Verify that pressing the KVM toggle button switches both keyboard/mouse input and monitor signal to the second computer. Confirm both computers remain powered on during the switch.
*   **Install drivers for a biometric login scanner**: Connect a USB fingerprint reader to a Windows PC. Allow Windows to automatically detect and install drivers. Navigate to Settings > Accounts > Sign-in options and configure Windows Hello fingerprint authentication. Verify that a registered fingerprint successfully unlocks the device.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the peripheral devices and interfaces sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on peripheral devices and interfaces in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the connectivity steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

# Quiz: Module 09 - Peripheral Devices and Interfaces
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What is the maximum data transfer speed of USB 3.0 (SuperSpeed)?
*   A) 480 Mbps
*   B) 5 Gbps
*   C) 10 Gbps
*   D) 40 Gbps
*   **Correct Answer:** B) USB 3.0 operates at a maximum of 5 Gbps.
*   **Distractor Analysis:**
    *   *Why correct:* USB 3.0 operates at a maximum of 5 Gbps.
    *   480 Mbps is USB 2.0. 10 Gbps is USB 3.1 Gen 2. 40 Gbps is Thunderbolt 3/4.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes **USB Type-C**?
*   A) A reversible connector form factor used with USB 3.x, USB 2.0, Thunderbolt 3/4, and DisplayPort signals — the connector shape does not by itself indicate transfer speed; the host port's supported protocol determines actual performance.
*   B) A dedicated high-speed connector standard that always guarantees 40 Gbps transfer rates, making it interchangeable with Thunderbolt 3 cables for all use cases.
*   C) A connector type exclusive to mobile device charging that carries only power delivery and cannot transmit data or video signals.
*   D) A legacy connector standard superseded by USB Type-A, used only on older laptops and tablets manufactured before 2015.
*   **Correct Answer:** A) A reversible connector form factor used with USB 3.x, USB 2.0, Thunderbolt 3/4, and DisplayPort signals — the connector shape does not by itself indicate transfer speed; the host port's supported protocol determines actual performance.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes USB Type-C as a physical form factor that supports multiple protocols at varying speeds; the A+ exam specifically tests whether students understand that Type-C is a connector shape, not a speed guarantee.
    * *Why B is incorrect:* USB Type-C does not guarantee 40 Gbps; a Type-C port may support only USB 2.0 (480 Mbps) depending on the host controller, and standard USB-C cables cannot carry Thunderbolt speeds.
    * *Why C is incorrect:* USB Type-C carries both power and data; it is used for data transfer, video output (DisplayPort Alt Mode), and charging across laptops, phones, and peripherals.
    * *Why D is incorrect:* USB Type-C is a current-generation connector standard introduced around 2014–2015 and is still the dominant connector on modern devices; it is not legacy.


---

**Question 3**
A user plugs a USB 3.0 external hard drive into their laptop and notices file transfers are completing at approximately 30 MB/s instead of the expected 300+ MB/s. The drive works correctly on another laptop at full speed. What is the most likely cause on this laptop?
*   A) The external drive's firmware is incompatible with this laptop's operating system version and requires a firmware update
*   B) The laptop port the drive is connected to is a USB 2.0 port, limiting the connection to 480 Mbps (approximately 60 MB/s theoretical, ~30 MB/s real-world)
*   C) The USB cable provided with the drive is a charging-only cable that does not include the data pins required for SuperSpeed transfer
*   D) The drive is formatted with NTFS and must be reformatted to exFAT before USB 3.0 speeds are available on a Windows laptop
*   **Correct Answer:** B) The laptop port the drive is connected to is a USB 2.0 port, limiting the connection to 480 Mbps (approximately 60 MB/s theoretical, ~30 MB/s real-world)
*   **Distractor Analysis:**
    * *Why B is correct:* USB 2.0 ports are limited to 480 Mbps theoretical bandwidth; real-world sustained transfer rates are typically 25–40 MB/s, which matches the observed symptom. The drive works at full speed elsewhere, ruling out a drive or cable fault.
    * *Why A is incorrect:* Firmware incompatibility would typically cause the drive to be unrecognized entirely, not throttle to exactly USB 2.0 speeds; the consistent USB 2.0-equivalent rate points to an interface speed mismatch, not firmware.
    * *Why C is incorrect:* A charging-only USB-C cable missing data pins would result in the drive not being detected at all, not a partial speed reduction; this scenario uses a standard USB drive that is functional.
    * *Why D is incorrect:* File system format (NTFS vs. exFAT) does not affect the USB interface transfer rate; both formats operate at the same speed over USB.


---

**Question 4**
A technician sets up a KVM switch so that one monitor, keyboard, and mouse can control two desktop PCs. After configuration, switching to the second PC results in a blank monitor screen, though the keyboard and mouse switch correctly. What is the most likely cause?
*   A) The KVM switch requires identical operating systems on both connected computers before video output is supported
*   B) The video cable connecting the second PC to the KVM switch is unplugged or connected to the wrong port on the switch
*   C) The monitor must be powered off and on again after every KVM switch because it cannot detect hot-plug video signal changes
*   D) The keyboard and mouse switching to the second PC consumes all available USB bandwidth, leaving no bandwidth for the video signal
*   **Correct Answer:** B) The video cable connecting the second PC to the KVM switch is unplugged or connected to the wrong port on the switch
*   **Distractor Analysis:**
    * *Why B is correct:* When keyboard/mouse switch correctly but video does not, the KVM switch itself is functional; the most likely physical cause is a missing or mis-seated video cable between the second PC and the KVM switch's video input.
    * *Why A is incorrect:* KVM switches are OS-agnostic hardware devices; they pass video signals regardless of what operating system is running on the connected computers.
    * *Why C is incorrect:* Modern monitors support hot-plug detection (HPD) and automatically re-sync when a new video signal is presented; a brief blank screen during switching is normal but a persistent blank screen indicates a missing signal, not a monitor limitation.
    * *Why D is incorrect:* USB and video signals in a KVM switch travel over separate, independent physical cables; USB bandwidth has no effect on video signal transmission.


---

**Question 5**
A company requires employees to authenticate to their workstations using both a password and a physical card issued by the IT department. The card contains an embedded chip that stores cryptographic credentials. Which peripheral device reads this card, and which authentication factor category does it represent?
*   A) A barcode scanner reads the card; it represents the "something you know" authentication factor because the barcode encodes the user's password
*   B) A smart card reader reads the card; it represents the "something you have" authentication factor because possession of the physical card is required
*   C) A biometric scanner reads the card; it represents the "something you are" authentication factor because the chip stores the user's fingerprint template
*   D) An NFC tap reader reads the card; it is not an authentication factor because proximity cards are used only for physical door access, not computer login
*   **Correct Answer:** B) A smart card reader reads the card; it represents the "something you have" authentication factor because possession of the physical card is required
*   **Distractor Analysis:**
    * *Why B is correct:* A smart card (PIV/CAC card) contains an embedded cryptographic chip read by a smart card reader attached to the workstation; requiring physical possession of the card is the definition of the "something you have" multi-factor authentication category.
    * *Why A is incorrect:* The described card contains an embedded chip, not a barcode; barcode scanners read printed optical patterns and are not used for cryptographic workstation authentication.
    * *Why C is incorrect:* A biometric scanner reads physical characteristics of the user (fingerprint, iris, face) — the "something you are" factor; it does not read a physical card's chip.
    * *Why D is incorrect:* Smart cards and NFC-based authentication cards are widely used for computer login (Windows Smart Card logon, PIV authentication); physical access and computer authentication are distinct use cases and both are valid "something you have" factors.

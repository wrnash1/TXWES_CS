# Quiz: Module 09 - Peripheral Devices and Interfaces

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.2 and Domain 1.2
**Total Questions:** 10 | **Points:** 10 (1 point each)

---

### Question 1

What is the maximum data transfer speed of USB 3.0 (SuperSpeed)?

- A) 480 Mbps
- B) 5 Gbps
- C) 10 Gbps
- D) 40 Gbps

**Correct Answer:** B — USB 3.0 (also called USB 3.1 Gen 1 and USB 3.2 Gen 1x1) operates at a maximum of 5 Gbps. Its blue port color is the standard field identification indicator.

**Distractor Analysis:**

- *Why A is incorrect:* 480 Mbps is the maximum speed of USB 2.0 (Hi-Speed USB). A port achieving only 480 Mbps despite a USB 3.0 drive being connected is either a USB 2.0 port or using a USB 2.0 cable.
- *Why C is incorrect:* 10 Gbps is the speed of USB 3.1 Gen 2 (SuperSpeed USB 10Gbps), one full generation faster than USB 3.0.
- *Why D is incorrect:* 40 Gbps is the speed of Thunderbolt 3 and Thunderbolt 4, not USB 3.0.

---

### Question 2

In the context of PC hardware, which of the following most accurately describes USB Type-C?

- A) A reversible connector form factor used with USB 3.x, USB 2.0, Thunderbolt 3/4, and DisplayPort signals — the connector shape does not by itself indicate transfer speed; the host port's supported protocol determines actual performance.
- B) A dedicated high-speed connector standard that always guarantees 40 Gbps transfer rates, making it interchangeable with Thunderbolt 3 cables for all use cases.
- C) A connector type exclusive to mobile device charging that carries only power delivery and cannot transmit data or video signals.
- D) A legacy connector standard superseded by USB Type-A, used only on older laptops and tablets manufactured before 2015.

**Correct Answer:** A — USB Type-C is a physical form factor that supports multiple protocols at varying speeds. The A+ exam specifically tests whether students understand that Type-C is a connector shape, not a speed guarantee.

**Distractor Analysis:**

- *Why B is incorrect:* USB Type-C does not guarantee 40 Gbps. A Type-C port may support only USB 2.0 (480 Mbps) depending on the host controller. Standard USB-C cables cannot carry Thunderbolt speeds — both the port and cable must be Thunderbolt-rated.
- *Why C is incorrect:* USB Type-C carries both power and data. It supports data transfer, DisplayPort Alt Mode video output, and charging across laptops, phones, and peripherals.
- *Why D is incorrect:* USB Type-C is a current-generation connector introduced around 2014-2015 and remains the dominant connector on modern devices. It is not legacy and was not superseded by Type-A.

---

### Question 3

A user plugs a USB 3.0 external hard drive into their laptop and notices file transfers are completing at approximately 30 MB/s instead of the expected 300+ MB/s. The drive works correctly on another laptop at full speed. What is the most likely cause on this laptop?

- A) The external drive's firmware is incompatible with this laptop's operating system version and requires a firmware update
- B) The laptop port the drive is connected to is a USB 2.0 port, limiting the connection to 480 Mbps (approximately 60 MB/s theoretical, approximately 30 MB/s real-world)
- C) The USB cable provided with the drive is a charging-only cable that does not include the data pins required for SuperSpeed transfer
- D) The drive is formatted with NTFS and must be reformatted to exFAT before USB 3.0 speeds are available on a Windows laptop

**Correct Answer:** B — USB 2.0 ports are limited to 480 Mbps theoretical bandwidth; real-world sustained transfer rates are typically 25-40 MB/s, which matches the observed symptom. The drive works at full speed elsewhere, ruling out a drive or cable fault.

**Distractor Analysis:**

- *Why A is incorrect:* Firmware incompatibility would typically cause the drive to be unrecognized entirely, not throttle to exactly USB 2.0 speeds. The consistent USB 2.0-equivalent rate points to an interface speed mismatch, not firmware.
- *Why C is incorrect:* A charging-only USB-C cable missing data pins would result in the drive not being detected at all, not a partial speed reduction. This scenario uses a standard USB drive that is functional.
- *Why D is incorrect:* File system format (NTFS vs. exFAT) does not affect the USB interface transfer rate. Both formats operate at the same speed over USB.

---

### Question 4

A technician sets up a KVM switch so that one monitor, keyboard, and mouse can control two desktop PCs. After configuration, switching to the second PC results in a blank monitor screen, though the keyboard and mouse switch correctly. What is the most likely cause?

- A) The KVM switch requires identical operating systems on both connected computers before video output is supported
- B) The video cable connecting the second PC to the KVM switch is unplugged or connected to the wrong port on the switch
- C) The monitor must be powered off and on again after every KVM switch because it cannot detect hot-plug video signal changes
- D) The keyboard and mouse switching to the second PC consumes all available USB bandwidth, leaving no bandwidth for the video signal

**Correct Answer:** B — When keyboard/mouse switch correctly but video does not, the KVM switch itself is functional. The most likely physical cause is a missing or mis-seated video cable between the second PC and the KVM switch's video input port.

**Distractor Analysis:**

- *Why A is incorrect:* KVM switches are OS-agnostic hardware signal-switching devices. They pass video signals regardless of what operating system is running on the connected computers.
- *Why C is incorrect:* Modern monitors support hot-plug detection (HPD) and automatically re-sync when a new video signal is presented. A persistent blank screen indicates a missing signal, not a monitor detection limitation.
- *Why D is incorrect:* USB and video signals in a KVM switch travel over separate, independent physical cables. USB bandwidth has no effect on video signal transmission.

---

### Question 5

A company requires employees to authenticate to their workstations using both a password and a physical card issued by the IT department. The card contains an embedded chip that stores cryptographic credentials. Which peripheral device reads this card, and which authentication factor category does it represent?

- A) A barcode scanner reads the card; it represents the "something you know" authentication factor because the barcode encodes the user's password
- B) A smart card reader reads the card; it represents the "something you have" authentication factor because possession of the physical card is required
- C) A biometric scanner reads the card; it represents the "something you are" authentication factor because the chip stores the user's fingerprint template
- D) An NFC tap reader reads the card; it is not an authentication factor because proximity cards are used only for physical door access, not computer login

**Correct Answer:** B — A smart card (PIV/CAC card) contains an embedded cryptographic chip read by a smart card reader. Requiring physical possession of the card is the definition of the "something you have" multi-factor authentication category.

**Distractor Analysis:**

- *Why A is incorrect:* The described card contains an embedded chip, not a barcode. Barcode scanners read printed optical patterns and are not used for cryptographic workstation authentication.
- *Why C is incorrect:* A biometric scanner reads physical characteristics of the user (fingerprint, iris, face) — the "something you are" factor. It does not read a physical card's chip.
- *Why D is incorrect:* Smart cards and NFC-based authentication cards are widely used for computer login (Windows Smart Card logon, PIV authentication). Both represent valid "something you have" factors.

---

### Question 6

A technician connects a Thunderbolt 4 laptop to a Thunderbolt 4 dock using a standard USB-C charging cable (not a Thunderbolt cable). The user reports that the dock's USB ports and connected monitor do not work, but the laptop charges correctly. What is the most likely cause?

- A) The Thunderbolt 4 dock requires a firmware update before it is compatible with standard USB-C charging cables
- B) The standard USB-C cable supports power delivery but does not carry the Thunderbolt data protocol required for the dock's USB ports and video output
- C) Thunderbolt 4 ports are not backwards compatible with USB-C charging cables, so the charging itself indicates a different fault
- D) The laptop's Thunderbolt 4 port is defective because a functional port would operate all dock features over any USB-C cable

**Correct Answer:** B — A standard USB-C charging cable carries USB Power Delivery and USB data at USB speeds but lacks the signaling required for Thunderbolt 3/4 features. Thunderbolt features require a Thunderbolt-rated cable.

**Distractor Analysis:**

- *Why A is incorrect:* Thunderbolt 4 docks do not require firmware updates to recognize cable type. The dock correctly provides power from any USB-C cable; the limitation is the cable's inability to carry Thunderbolt protocol.
- *Why C is incorrect:* Thunderbolt 4 ports are fully backwards compatible with USB-C charging cables for the USB Power Delivery function. Charging working correctly via a USB-C cable is expected and normal behavior.
- *Why D is incorrect:* The Thunderbolt port is functioning correctly — it is delivering power via USB PD as designed. The cable, not the port, is the limiting factor for Thunderbolt data features.

---

### Question 7

Which USB connector type is described as: small, asymmetric, 5-pin, with one beveled edge; commonly used on Android smartphones manufactured between approximately 2010 and 2018?

- A) USB Type-C
- B) USB Mini-B
- C) USB Micro-B
- D) USB Type-B

**Correct Answer:** C — USB Micro-B is the small asymmetric 5-pin connector with a distinctive beveled edge that was the dominant smartphone charging and data connector from approximately 2010 to 2018, when USB-C began replacing it.

**Distractor Analysis:**

- *Why A is incorrect:* USB Type-C is a small oval reversible connector introduced around 2014-2015 that has no asymmetric beveled edge. It can be inserted either way without orientation.
- *Why B is incorrect:* USB Mini-B is a slightly larger trapezoidal connector used on older cameras and MP3 players predating the Micro-B era. It is distinctly larger than Micro-B.
- *Why D is incorrect:* USB Type-B is the square connector with beveled top corners used on printers and scanners — a device-side connector for larger peripherals, not smartphones.

---

### Question 8

An employee in a high-security government facility must unlock their workstation. The security policy requires the "something you are" authentication factor only — no password or card. The employee is wearing protective gloves that prevent fingerprint scanning. Which biometric option is most appropriate?

- A) Smart card reader, because government facilities standardize on CAC cards for all authentication
- B) Iris scanner, because iris recognition does not require physical contact and works regardless of whether the employee is wearing gloves
- C) USB fingerprint reader with a stylus adapter that allows gloved fingerprint capture
- D) Password entry, because if biometric options are unavailable the fallback must always be a password

**Correct Answer:** B — An iris scanner captures the iris pattern using an infrared camera with no physical contact required. It is unaffected by gloves and fulfills the "something you are" factor requirement.

**Distractor Analysis:**

- *Why A is incorrect:* A smart card (CAC) represents "something you have" — a possession-based factor. The scenario requires "something you are" (biometric) authentication specifically.
- *Why C is incorrect:* Fingerprint scanners require skin contact with the sensor surface to capture the ridge pattern. A glove prevents the sensor from reading the actual fingerprint regardless of any adapter.
- *Why D is incorrect:* A password represents "something you know," not "something you are." Falling back to a password would violate the stated security policy requiring a biometric factor.

---

### Question 9

A user connects a USB 3.0 hub to their laptop's blue USB 3.0 port. They then connect a USB 2.0 keyboard, a USB 3.0 flash drive, and a USB 2.0 webcam to the hub. At what speed will the USB 3.0 flash drive transfer data through this configuration?

- A) 5 Gbps — the flash drive and hub are both USB 3.0, and the laptop port is USB 3.0, so the full speed is available
- B) 480 Mbps — the hub operates at the speed of its slowest connected device, dropping the entire hub to USB 2.0 speeds
- C) 5 Gbps for the flash drive and 480 Mbps simultaneously for the keyboard and webcam, because a USB 3.0 hub maintains separate speed lanes for each device
- D) 1.5 Mbps — connecting any USB 1.1-capable device to the hub forces all ports to the slowest supported speed

**Correct Answer:** C — A USB 3.0 hub includes both a USB 3.0 controller and a USB 2.0 transaction translator. USB 3.0 devices communicate through the high-speed controller while USB 2.0 devices use the transaction translator simultaneously. The hub does not throttle the USB 3.0 device to USB 2.0 speed.

**Distractor Analysis:**

- *Why A is incorrect:* While the flash drive can achieve USB 3.0 speeds, this answer fails to address the simultaneous operation of the USB 2.0 devices at their correct speed. Answer C is more complete and accurate.
- *Why B is incorrect:* This describes the behavior of a USB 2.0 hub. USB 3.0 hubs include a transaction translator chip specifically to avoid throttling high-speed devices to the lowest-speed device's rate.
- *Why D is incorrect:* USB 3.0 hubs do not reduce all devices to USB 1.1 speeds. USB 1.1 Low Speed (1.5 Mbps) is a legacy mode for certain devices; a hub does not force this rate on all ports.

---

### Question 10

Which of the following correctly describes the difference between Thunderbolt 3 and Thunderbolt 4 in terms of data speed and capabilities?

- A) Thunderbolt 4 doubles the data speed of Thunderbolt 3 from 20 Gbps to 40 Gbps, and both versions use the USB-C physical connector
- B) Thunderbolt 4 offers the same 40 Gbps maximum speed as Thunderbolt 3 but enforces stricter minimum capability requirements, including mandatory support for two 4K displays and PCIe tunneling at higher minimums
- C) Thunderbolt 4 increases the maximum speed to 80 Gbps by bonding two Thunderbolt 3 connections through a single USB-C port using channel aggregation
- D) Thunderbolt 4 replaces the USB-C connector with a new proprietary oval connector that is not compatible with standard USB-C devices

**Correct Answer:** B — Thunderbolt 3 and Thunderbolt 4 both operate at a maximum of 40 Gbps. Thunderbolt 4 is a stricter certification that mandates minimum performance requirements (40 Gbps on all certified ports, dual 4K display support, PCIe at 32 Gbps minimum) that were optional or variable under Thunderbolt 3.

**Distractor Analysis:**

- *Why A is incorrect:* Thunderbolt 3 already operates at 40 Gbps, not 20 Gbps. Thunderbolt 2 operates at 20 Gbps. Thunderbolt 4 does not double the speed; it standardizes the minimum feature set.
- *Why C is incorrect:* Thunderbolt 4 does not use channel aggregation to reach 80 Gbps. Future Thunderbolt 5 targets higher speeds, but Thunderbolt 4 is capped at 40 Gbps.
- *Why D is incorrect:* Thunderbolt 4 continues to use the USB Type-C physical connector, exactly as Thunderbolt 3 does. There is no proprietary connector associated with Thunderbolt 4.

---

### Question 11

A user plugs a USB 3.2 Gen 2x2 device into a blue USB Type-A port on their desktop. The device performs at only 5 Gbps instead of the expected 20 Gbps. What is the MOST likely explanation?

- A) The USB cable is defective and limits speed to 5 Gbps
- B) The blue Type-A port supports USB 3.0 (5 Gbps); USB 3.2 Gen 2x2 requires a USB Type-C port with the appropriate host controller
- C) The device needs a driver update to unlock 20 Gbps operation
- D) USB 3.2 Gen 2x2 is only supported on Thunderbolt 4 ports

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* USB 3.2 Gen 2x2 (20 Gbps) uses dual-lane signaling and is only available on USB Type-C ports with a compatible host controller. The blue USB Type-A connector is limited to single-lane USB 3.0/3.1 speeds (5 Gbps or 10 Gbps). Achieving 20 Gbps requires a Type-C host port with Gen 2x2 controller support.
- *Why A is incorrect:* While a damaged cable could limit speed, the more fundamental issue is the port type. Type-A physically cannot carry the dual-lane signal required for USB 3.2 Gen 2x2 regardless of cable quality.
- *Why C is incorrect:* Driver updates can fix recognition or stability issues but cannot change the physical capability of a port. A USB 3.0 Type-A port cannot be upgraded to 20 Gbps via software.
- *Why D is incorrect:* USB 3.2 Gen 2x2 is a USB specification and does not require Thunderbolt 4. It requires a compatible USB Type-C host controller, not a Thunderbolt controller.

---

### Question 12

A technician needs to connect a USB 2.0 printer to a workstation. The only available port on the back of the PC is a USB 3.0 (blue) Type-A port. What will happen?

- A) The printer will not be detected because USB 2.0 devices are not backward compatible with USB 3.0 ports
- B) The printer will function normally at USB 2.0 speeds; USB 3.0 ports are backward compatible with USB 2.0 devices
- C) The printer will operate at USB 3.0 speeds (5 Gbps) automatically when connected to the blue port
- D) A USB 2.0 hub must be used between the port and the printer to ensure compatibility

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* USB is backward compatible across generations. A USB 2.0 device connected to a USB 3.0 port negotiates to USB 2.0 speed (480 Mbps). The printer will be detected and operate normally — it just will not benefit from the higher-speed port. No hub or adapter is required.
- *Why A is incorrect:* USB is specifically designed for backward compatibility. This is a core design principle of the USB specification and is tested repeatedly on the A+ exam.
- *Why C is incorrect:* The printer's internal controller determines the maximum speed, not the port it is connected to. A USB 2.0 printer communicates at USB 2.0 speeds regardless of which USB generation port it uses.
- *Why D is incorrect:* A USB 2.0 hub is unnecessary. Direct connection to the USB 3.0 port with a standard USB cable will work correctly at USB 2.0 speeds.

---

### Question 13

Which of the following correctly identifies the PS/2 connector and its modern replacement?

- A) PS/2 is a 6-pin mini-DIN connector used for keyboard and mouse; it has been largely replaced by USB
- B) PS/2 is a 9-pin serial DB-9 connector used for legacy mice; it has been replaced by Bluetooth
- C) PS/2 is a 15-pin VGA-style connector used for keyboard connection; it has been replaced by HDMI
- D) PS/2 is a 25-pin parallel port connector used for printers; it has been replaced by USB Type-B

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* PS/2 connectors are 6-pin mini-DIN connectors that connect keyboard and mouse to older motherboards. Color coding distinguishes them: purple for keyboard, green for mouse. PS/2 is not hot-pluggable (devices must be connected before boot). USB replaced PS/2 as the standard keyboard and mouse interface.
- *Why B is incorrect:* A 9-pin serial DB-9 connector is a legacy COM port (RS-232 serial), not a PS/2 connector. DB-9 was used for serial mice and modems, not the PS/2 protocol.
- *Why C is incorrect:* A 15-pin connector associated with displays describes VGA (HD-15). PS/2 has nothing to do with video output.
- *Why D is incorrect:* A 25-pin parallel port (Centronics/DB-25) was used for legacy printers. It is an entirely different connector type from PS/2 and was replaced by USB Type-B for printers.

---

### Question 14

A company policy requires two-factor authentication using "something you know" and "something you have." A user currently authenticates with a password only. Which addition satisfies the policy?

- A) A longer, more complex password
- B) A fingerprint scanner
- C) A hardware TOTP token that generates a new 6-digit code every 30 seconds
- D) A second password stored on a separate login screen

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* A TOTP (Time-based One-Time Password) hardware token is a physical device that generates a time-synchronized code. It represents "something you have" (physical possession of the token). Combined with the existing password ("something you know"), this creates true two-factor authentication with two different factor categories.
- *Why A is incorrect:* A longer password is still only "something you know." Increasing password complexity adds strength within a single factor but does not add a second factor from a different category.
- *Why B is incorrect:* A fingerprint scanner adds "something you are" (biometric) — not "something you have." This satisfies a different two-factor combination (know + are) but is not "something you have" as the policy may specifically require.
- *Why D is incorrect:* A second password is still "something you know." Two passwords are two instances of the same factor category, not two-factor authentication.

---

### Question 15

A user plugs a device into their laptop's USB-C port and it charges the laptop's battery. What USB capability enables this behavior?

- A) USB Alt Mode — the USB-C port is operating in alternate mode to deliver power in reverse
- B) USB Power Delivery (USB PD) — a negotiated power protocol over USB-C that can deliver up to 100W (PD 3.0) or 240W (PD 3.1) in either direction
- C) Thunderbolt 4 — all USB-C charging is performed through the Thunderbolt 4 controller
- D) USB 3.2 Gen 2 — the 10 Gbps data rate automatically converts to 20W of charging power at half speed

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* USB Power Delivery (USB PD) is a separate USB standard that allows USB-C connections to negotiate variable power levels. USB PD 3.0 supports up to 100W; USB PD 3.1 supports up to 240W. Critically, power delivery can flow in either direction — a peripheral, dock, or wall adapter can charge the laptop through the same port that delivers data. This is not tied to USB speed generation.
- *Why A is incorrect:* USB Alt Mode allows the USB-C port to carry non-USB signals (DisplayPort, Thunderbolt, HDMI). It does not describe the power delivery function.
- *Why C is incorrect:* USB-C charging via USB PD does not require Thunderbolt 4. Any USB-C port with USB PD support can charge the host device regardless of whether it has a Thunderbolt controller.
- *Why D is incorrect:* USB data speed (3.2 Gen 2 = 10 Gbps) and charging power are entirely independent specifications. A USB 3.2 Gen 2 speed rating has no relationship to how much power the port delivers.

---

### Question 16

A KVM switch has four PC input ports and one set of outputs (monitor, keyboard, mouse). A technician wants to control all four PCs. Which statement about OS compatibility is correct?

- A) All four PCs must run the same operating system for the KVM switch to function correctly
- B) The KVM switch operates at the hardware signal level and is OS-agnostic; PCs running different OSes can all be controlled through the same KVM
- C) The KVM switch requires a USB driver installed on each connected PC before it will recognize keyboard and mouse input
- D) The KVM switch's monitor output only supports Windows-native display resolutions; Linux and macOS may show incorrect resolutions

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* KVM switches operate below the OS layer — they route physical electrical signals (USB HID for keyboard/mouse, video signal for the monitor). The OS receives standard USB keyboard and mouse input and a standard monitor signal. No driver, no OS configuration, and no OS compatibility check is involved. A KVM switch works equally well with Windows, Linux, macOS, and any other OS.
- *Why A is incorrect:* This is a classic A+ exam trap. KVM switches have no OS awareness. Different OSes on different connected PCs are fully supported.
- *Why C is incorrect:* The connected PCs see standard USB HID keyboard and mouse devices — the same devices they would see if directly connected without a KVM. No additional KVM-specific driver is required.
- *Why D is incorrect:* The KVM switch passes the video signal transparently. Resolution is determined by the GPU, the monitor's EDID, and the OS display driver — not by the KVM switch's OS compatibility.

---

### Question 17

A technician sets up a workstation for a security researcher who needs to run a USB device identification utility. The utility scans all USB devices connected to the system and reports their device class, vendor ID, and product ID. Where does this information originate?

- A) The USB device reports its vendor ID, product ID, and device class in a USB descriptor transmitted to the host during the device enumeration process
- B) The information is looked up in a local database file installed by the USB driver during device setup
- C) Windows Device Manager generates these IDs randomly during initial USB device recognition
- D) The information is stored on the USB cable's internal memory chip and reported at connection time

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* USB device enumeration is the process where the USB host controller requests descriptor packets from a newly connected device. The device's firmware responds with standard USB descriptors containing the Vendor ID (VID), Product ID (PID), device class code, manufacturer string, and product string. This happens automatically over the USB protocol before any OS driver is loaded.
- *Why B is incorrect:* While Windows does maintain a device database for driver matching, the vendor ID and product ID originate from the device itself via descriptors — not from the driver database. The database is consulted to find the appropriate driver after the IDs are read.
- *Why C is incorrect:* Device IDs are not randomly generated. They are fixed identifiers assigned by the USB Implementers Forum (USB-IF) to device manufacturers and hard-coded in the device firmware.
- *Why D is incorrect:* USB cables do not contain memory chips or identification data (with the exception of active optical cables and some proprietary smart cables, which is a narrow special case). The device itself — not the cable — transmits descriptor information.

---

### Question 18

A user connects a USB keyboard and mouse to a KVM switch. After switching to a second PC, the keyboard is recognized but the mouse appears to disconnect and reconnect repeatedly. What is the MOST likely cause?

- A) The second PC's USB drivers are corrupted and need reinstallation
- B) The KVM switch's USB hub protocol is incompatible with the mouse, or the mouse cable has a marginal connection at the KVM
- C) The mouse requires Thunderbolt 4 to maintain a stable connection during KVM switching
- D) The second PC's BIOS does not have USB legacy mode enabled, preventing mouse detection after POST

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* When a KVM switch changes input, it re-enumerates the USB devices on the new port. Some mice (particularly those with custom HID firmware or very fast polling rates) are sensitive to re-enumeration timing and may disconnect/reconnect repeatedly if the KVM's USB hub has compatibility issues or if the cable connection is marginal. Testing with a different mouse or a different KVM port isolates the cause.
- *Why A is incorrect:* Corrupted USB drivers would affect all USB devices on that PC, not just the mouse through a KVM. The fact that the keyboard works normally rules out a systemic USB driver issue.
- *Why C is incorrect:* Mice do not require Thunderbolt 4 — they are low-bandwidth USB HID devices that operate at USB 1.1 Low Speed (1.5 Mbps). Thunderbolt has no relevance to mouse connectivity.
- *Why D is incorrect:* USB legacy mode in BIOS enables USB devices during POST (before the OS loads). If the PC has already booted and the keyboard is recognized, the BIOS USB settings are not the issue — the OS USB stack is active and functional.

---

### Question 19

Which USB connector type is specifically designed to be reversible (insertable in either orientation)?

- A) USB Type-A
- B) USB Type-B
- C) USB Micro-B
- D) USB Type-C

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* USB Type-C is the only standard USB connector designed to be symmetrical and reversible — it can be inserted either way without needing to orient the connector. This was one of the primary design goals of the USB Type-C specification, addressing the user frustration of the directional Type-A connector.
- *Why A is incorrect:* USB Type-A has an asymmetric design and is directional. The flat rectangular connector has a specific top and bottom and can only be inserted one way. It is famously non-reversible (the origin of many jokes about USB orientation).
- *Why B is incorrect:* USB Type-B is a square-profile directional connector used on printers, scanners, and audio interfaces. It is not reversible.
- *Why C is incorrect:* USB Micro-B is a small asymmetric connector with a distinctive beveled shape. It is directional and not reversible.

---

### Question 20

A technician is troubleshooting a workstation where a USB device is detected but identified as an "Unknown Device" in Device Manager with a yellow warning triangle. What is the MOST likely cause?

- A) The USB port hardware is physically damaged and cannot supply sufficient power
- B) The device driver for the USB device is missing, corrupted, or incompatible with the installed OS version
- C) The USB cable is too long and the signal has degraded below the threshold for device identification
- D) The device's USB descriptor has been corrupted and the device must be replaced

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* "Unknown Device" with a yellow warning triangle in Device Manager means Windows successfully detected the device via USB enumeration (it can read the VID and PID) but failed to load or find an appropriate driver. The fix is to install the correct driver — from Windows Update, the device manufacturer's website, or a driver package on physical media.
- *Why A is incorrect:* Physical port damage or insufficient power typically results in the device not being detected at all, or causes intermittent disconnection. It does not produce the specific "Unknown Device" entry that appears when the device is successfully enumerated but undriven.
- *Why C is incorrect:* A cable that is too long causes signal degradation that prevents detection entirely — the device would not appear in Device Manager at all. An "Unknown Device" entry requires successful USB enumeration, which means the signal was adequate.
- *Why D is incorrect:* While a corrupted USB descriptor is theoretically possible, it is an extremely rare hardware failure. The overwhelmingly more common cause of "Unknown Device" is a missing or failed driver installation — the standard first step in troubleshooting this specific Device Manager state.

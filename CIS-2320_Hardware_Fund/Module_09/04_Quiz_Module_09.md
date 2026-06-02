# Quiz: Module 09 - Peripheral Devices and Interfaces

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.2 and Domain 1.2
**Total Questions:** 10 | **Points:** 10 (1 point each)

---

**Question 1**

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

**Question 2**

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

**Question 3**

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

**Question 4**

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

**Question 5**

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

**Question 6**

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

**Question 7**

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

**Question 8**

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

**Question 9**

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

**Question 10**

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

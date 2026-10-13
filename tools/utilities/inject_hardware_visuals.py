#!/usr/bin/env python3
"""
Texas Wesleyan University - Curriculum Visual Media Injection Engine
Replaces visual placeholder cues ([SHOW COMPONENT: ...]) across CIS-2320
with responsive, publication-quality technical SVG illustrations in university branding.
"""

import os
import re

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/01_Bachelor_CIS_Programs/CIS-2320_Hardware_Fund"

# 1. Module 01: PC Architecture Overview SVG
M01_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Core Internal PC Components Anatomy &amp; Interconnections</text>

  <!-- Chassis Outline -->
  <rect x="40" y="95" width="770" height="330" fill="#1e293b" stroke="#334155" stroke-width="2" rx="8"/>
  <text x="55" y="115" fill="#64748b" font-size="11" font-weight="bold">DESKTOP CHASSIS (INTERIOR LAYOUT)</text>

  <!-- PSU -->
  <rect x="60" y="130" width="180" height="130" fill="#0f172a" stroke="#d9a74a" stroke-width="1.5" rx="6"/>
  <text x="150" y="160" fill="#d9a74a" font-size="14" font-weight="bold" text-anchor="middle">POWER SUPPLY (PSU)</text>
  <text x="150" y="180" fill="#94a3b8" font-size="11" text-anchor="middle">120V AC → +12V, +5V, +3.3V DC</text>
  <rect x="80" y="200" width="140" height="20" fill="#1e293b" rx="3"/>
  <text x="150" y="214" fill="#38bdf8" font-size="10" text-anchor="middle">24-pin ATX / 8-pin EPS / PCIe</text>
  <rect x="80" y="225" width="140" height="20" fill="#1e293b" rx="3"/>
  <text x="150" y="239" fill="#10b981" font-size="10" text-anchor="middle">80 PLUS Certified Efficiency</text>

  <!-- Drive Bays -->
  <rect x="60" y="280" width="180" height="125" fill="#0f172a" stroke="#64748b" stroke-width="1.5" rx="6"/>
  <text x="150" y="305" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">STORAGE DRIVE BAYS</text>
  <rect x="75" y="320" width="150" height="35" fill="#1e293b" stroke="#0284c7" rx="4"/>
  <text x="150" y="342" fill="#38bdf8" font-size="11" text-anchor="middle">3.5" HDD / 2.5" SATA SSD</text>
  <rect x="75" y="365" width="150" height="25" fill="#1e293b" stroke="#334155" rx="4"/>
  <text x="150" y="382" fill="#94a3b8" font-size="10" text-anchor="middle">SATA 7-pin Data + 15-pin Pwr</text>

  <!-- Motherboard Area -->
  <rect x="270" y="130" width="520" height="275" fill="#0f172a" stroke="#38bdf8" stroke-width="2" rx="6"/>
  <text x="530" y="152" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">SYSTEM MOTHERBOARD (ATX)</text>

  <!-- CPU Socket & Cooler -->
  <rect x="290" y="170" width="115" height="115" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="6"/>
  <rect x="315" y="185" width="65" height="65" fill="#334155" rx="4"/>
  <text x="347" y="215" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">CPU</text>
  <text x="347" y="232" fill="#fca5a5" font-size="9" text-anchor="middle">(LGA / PGA)</text>
  <text x="347" y="272" fill="#cbd5e1" font-size="9" text-anchor="middle">Heatsink + Fan (4-pin)</text>

  <!-- RAM Slots -->
  <g transform="translate(425, 170)">
    <rect x="0" y="0" width="15" height="115" fill="#1e293b" stroke="#3b82f6" rx="2"/>
    <rect x="22" y="0" width="15" height="115" fill="#1e293b" stroke="#10b981" rx="2"/>
    <rect x="44" y="0" width="15" height="115" fill="#1e293b" stroke="#3b82f6" rx="2"/>
    <rect x="66" y="0" width="15" height="115" fill="#1e293b" stroke="#10b981" rx="2"/>
    <text x="40" y="132" fill="#cbd5e1" font-size="10" text-anchor="middle">DIMM Slots (DDR4/DDR5)</text>
    <text x="40" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Dual-Channel Pairs</text>
  </g>

  <!-- M.2 NVMe Slot -->
  <rect x="530" y="175" width="110" height="28" fill="#1e293b" stroke="#d9a74a" rx="4"/>
  <text x="585" y="193" fill="#d9a74a" font-size="10" font-weight="bold" text-anchor="middle">M.2 NVMe SSD (PCIe x4)</text>

  <!-- Expansion Slots -->
  <g transform="translate(290, 305)">
    <rect x="0" y="0" width="230" height="16" fill="#0284c7" rx="3"/>
    <text x="115" y="12" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">PCIe 5.0 ×16 Slot (Discrete GPU / Graphics Card)</text>
    <rect x="0" y="22" width="70" height="12" fill="#64748b" rx="2"/>
    <text x="35" y="31" fill="#ffffff" font-size="8" text-anchor="middle">PCIe ×1</text>
    <rect x="0" y="39" width="140" height="14" fill="#0284c7" rx="2"/>
    <text x="70" y="50" fill="#ffffff" font-size="9" text-anchor="middle">PCIe ×4 Expansion</text>
    <rect x="0" y="58" width="230" height="16" fill="#0284c7" rx="3"/>
    <text x="115" y="70" fill="#ffffff" font-size="10" text-anchor="middle">PCIe ×16 Secondary Slot</text>
  </g>

  <!-- Rear I/O Panel -->
  <rect x="665" y="170" width="110" height="210" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <text x="720" y="190" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">REAR I/O PANEL</text>
  <rect x="680" y="205" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="219" fill="#38bdf8" font-size="9" text-anchor="middle">USB 3.2 Ports</text>
  <rect x="680" y="235" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="249" fill="#10b981" font-size="9" text-anchor="middle">2.5GbE RJ-45 LAN</text>
  <rect x="680" y="265" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="279" fill="#d9a74a" font-size="9" text-anchor="middle">HDMI / DisplayPort</text>
  <rect x="680" y="295" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="309" fill="#f43f5e" font-size="9" text-anchor="middle">HD Audio Jacks</text>

  <!-- Footer Banner -->
  <rect x="40" y="435" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="457" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ CompTIA A+ Blueprint: Identify all 7 primary internal components on sight and know their physical interconnects.</text>
</svg>
</div>'''

# 2. Module 03: CPU Socket Types LGA vs PGA vs BGA SVG
M03_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">CPU Socket Architecture Comparison: LGA vs. PGA vs. BGA</text>

  <!-- LGA Panel -->
  <g transform="translate(40, 95)">
    <rect width="235" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <rect width="235" height="32" fill="#0284c7" rx="8"/>
    <rect width="235" height="10" y="22" fill="#0284c7"/>
    <text x="117" y="21" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">LGA (Land Grid Array)</text>
    
    <!-- Socket Visual -->
    <rect x="42" y="45" width="150" height="110" fill="#0f172a" stroke="#cbd5e1" rx="4"/>
    <circle cx="65" cy="70" r="2.5" fill="#d9a74a"/><circle cx="85" cy="70" r="2.5" fill="#d9a74a"/><circle cx="105" cy="70" r="2.5" fill="#d9a74a"/><circle cx="125" cy="70" r="2.5" fill="#d9a74a"/><circle cx="145" cy="70" r="2.5" fill="#d9a74a"/><circle cx="165" cy="70" r="2.5" fill="#d9a74a"/>
    <circle cx="65" cy="90" r="2.5" fill="#d9a74a"/><circle cx="85" cy="90" r="2.5" fill="#d9a74a"/><circle cx="105" cy="90" r="2.5" fill="#d9a74a"/><circle cx="125" cy="90" r="2.5" fill="#d9a74a"/><circle cx="145" cy="90" r="2.5" fill="#d9a74a"/><circle cx="165" cy="90" r="2.5" fill="#d9a74a"/>
    <circle cx="65" cy="110" r="2.5" fill="#d9a74a"/><circle cx="85" cy="110" r="2.5" fill="#d9a74a"/><circle cx="105" cy="110" r="2.5" fill="#d9a74a"/><circle cx="125" cy="110" r="2.5" fill="#d9a74a"/><circle cx="145" cy="110" r="2.5" fill="#d9a74a"/><circle cx="165" cy="110" r="2.5" fill="#d9a74a"/>
    <circle cx="65" cy="130" r="2.5" fill="#d9a74a"/><circle cx="85" cy="130" r="2.5" fill="#d9a74a"/><circle cx="105" cy="130" r="2.5" fill="#d9a74a"/><circle cx="125" cy="130" r="2.5" fill="#d9a74a"/><circle cx="145" cy="130" r="2.5" fill="#d9a74a"/><circle cx="165" cy="130" r="2.5" fill="#d9a74a"/>
    <text x="117" y="172" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Pins on Motherboard Socket</text>
    
    <rect x="15" y="185" width="205" height="125" fill="#0f172a" rx="4"/>
    <text x="25" y="205" fill="#f8fafc" font-size="11"><b>CPU Underside:</b> Flat gold pads</text>
    <text x="25" y="225" fill="#f8fafc" font-size="11"><b>Primary Vendors:</b> Intel, AMD AM5</text>
    <text x="25" y="245" fill="#f8fafc" font-size="11"><b>Key Examples:</b> LGA1700, LGA1200</text>
    <text x="25" y="268" fill="#fca5a5" font-size="10">⚠️ <b>Risk:</b> Bent socket pins</text>
    <text x="25" y="283" fill="#fca5a5" font-size="10">destroys the entire motherboard.</text>
    <text x="25" y="300" fill="#38bdf8" font-size="10">Retained via load lever &amp; bracket.</text>
  </g>

  <!-- PGA Panel -->
  <g transform="translate(305, 95)">
    <rect width="235" height="325" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
    <rect width="235" height="32" fill="#059669" rx="8"/>
    <rect width="235" height="10" y="22" fill="#059669"/>
    <text x="117" y="21" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">PGA (Pin Grid Array)</text>
    
    <!-- CPU Underside Visual -->
    <rect x="42" y="45" width="150" height="110" fill="#0f172a" stroke="#cbd5e1" rx="4"/>
    <!-- Pins extending -->
    <line x1="65" y1="65" x2="65" y2="78" stroke="#d9a74a" stroke-width="3"/>
    <line x1="85" y1="65" x2="85" y2="78" stroke="#d9a74a" stroke-width="3"/>
    <line x1="105" y1="65" x2="105" y2="78" stroke="#d9a74a" stroke-width="3"/>
    <line x1="125" y1="65" x2="125" y2="78" stroke="#d9a74a" stroke-width="3"/>
    <line x1="145" y1="65" x2="145" y2="78" stroke="#d9a74a" stroke-width="3"/>
    <line x1="165" y1="65" x2="165" y2="78" stroke="#d9a74a" stroke-width="3"/>
    <line x1="65" y1="95" x2="65" y2="108" stroke="#d9a74a" stroke-width="3"/>
    <line x1="85" y1="95" x2="85" y2="108" stroke="#d9a74a" stroke-width="3"/>
    <line x1="105" y1="95" x2="105" y2="108" stroke="#d9a74a" stroke-width="3"/>
    <line x1="125" y1="95" x2="125" y2="108" stroke="#d9a74a" stroke-width="3"/>
    <line x1="145" y1="95" x2="145" y2="108" stroke="#d9a74a" stroke-width="3"/>
    <line x1="165" y1="95" x2="165" y2="108" stroke="#d9a74a" stroke-width="3"/>
    <text x="117" y="172" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Pins on CPU Package Underside</text>
    
    <rect x="15" y="185" width="205" height="125" fill="#0f172a" rx="4"/>
    <text x="25" y="205" fill="#f8fafc" font-size="11"><b>Socket:</b> Receptacle pin holes</text>
    <text x="25" y="225" fill="#f8fafc" font-size="11"><b>Primary Vendors:</b> Legacy AMD (AM4)</text>
    <text x="25" y="245" fill="#f8fafc" font-size="11"><b>Insertion:</b> Zero Insertion Force (ZIF)</text>
    <text x="25" y="268" fill="#fef08a" font-size="10">⚠️ <b>Risk:</b> Dropping CPU bends pins.</text>
    <text x="25" y="283" fill="#fef08a" font-size="10">Pins can be straightened gently.</text>
    <text x="25" y="300" fill="#10b981" font-size="10">Locked into socket with ZIF arm.</text>
  </g>

  <!-- BGA Panel -->
  <g transform="translate(570, 95)">
    <rect width="240" height="325" fill="#1e293b" stroke="#a855f7" stroke-width="2" rx="8"/>
    <rect width="240" height="32" fill="#7e22ce" rx="8"/>
    <rect width="240" height="10" y="22" fill="#7e22ce"/>
    <text x="120" y="21" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">BGA (Ball Grid Array)</text>
    
    <!-- Solder Ball Visual -->
    <rect x="45" y="45" width="150" height="110" fill="#0f172a" stroke="#cbd5e1" rx="4"/>
    <circle cx="70" cy="75" r="4.5" fill="#cbd5e1"/><circle cx="95" cy="75" r="4.5" fill="#cbd5e1"/><circle cx="120" cy="75" r="4.5" fill="#cbd5e1"/><circle cx="145" cy="75" r="4.5" fill="#cbd5e1"/><circle cx="170" cy="75" r="4.5" fill="#cbd5e1"/>
    <circle cx="70" cy="105" r="4.5" fill="#cbd5e1"/><circle cx="95" cy="105" r="4.5" fill="#cbd5e1"/><circle cx="120" cy="105" r="4.5" fill="#cbd5e1"/><circle cx="145" cy="105" r="4.5" fill="#cbd5e1"/><circle cx="170" cy="105" r="4.5" fill="#cbd5e1"/>
    <circle cx="70" cy="135" r="4.5" fill="#cbd5e1"/><circle cx="95" cy="135" r="4.5" fill="#cbd5e1"/><circle cx="120" cy="135" r="4.5" fill="#cbd5e1"/><circle cx="145" cy="135" r="4.5" fill="#cbd5e1"/><circle cx="170" cy="135" r="4.5" fill="#cbd5e1"/>
    <text x="120" y="172" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Solder Balls Bonded to Board</text>
    
    <rect x="15" y="185" width="210" height="125" fill="#0f172a" rx="4"/>
    <text x="25" y="205" fill="#f8fafc" font-size="11"><b>Socket:</b> NONE (Surface Mount)</text>
    <text x="25" y="225" fill="#f8fafc" font-size="11"><b>Target Devices:</b> Laptops, Tablets, IoT</text>
    <text x="25" y="245" fill="#f8fafc" font-size="11"><b>Serviceability:</b> Non-removable</text>
    <text x="25" y="268" fill="#e9d5ff" font-size="10">⚡ <b>Exam Fact:</b> CPU failure requires</text>
    <text x="25" y="283" fill="#e9d5ff" font-size="10">complete motherboard replacement.</text>
    <text x="25" y="300" fill="#a855f7" font-size="10">Zero field swappability.</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="435" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="457" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ A+ Rule of Thumb: LGA = Pins in Socket | PGA = Pins on Processor | BGA = Bonded by Solder Ball</text>
</svg>
</div>'''

# 3. Module 04: RAM Form Factors DDR4 vs DDR5 DIMM vs SODIMM SVG
M04_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">RAM Architecture: DDR4 vs. DDR5 &amp; DIMM vs. SO-DIMM</text>

  <!-- Desktop DDR4 DIMM -->
  <g transform="translate(50, 95)">
    <rect width="750" height="85" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
    <text x="20" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Standard Desktop DDR4 DIMM (288 Pins • 1.2V • 133.35 mm)</text>
    <!-- DRAM Chips -->
    <rect x="40" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="100" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="160" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="220" y="35" width="45" height="35" fill="#0f172a" rx="2"/>
    <!-- Key Notch -->
    <rect x="360" y="70" width="16" height="15" fill="#0f172a"/>
    <text x="368" y="65" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">DDR4 Notch</text>
    <rect x="460" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="520" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="580" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="640" y="35" width="45" height="35" fill="#0f172a" rx="2"/>
  </g>

  <!-- Desktop DDR5 DIMM -->
  <g transform="translate(50, 200)">
    <rect width="750" height="85" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="4"/>
    <text x="20" y="25" fill="#10b981" font-size="13" font-weight="bold">Standard Desktop DDR5 DIMM (288 Pins • 1.1V • On-Die ECC • PMIC Onboard)</text>
    <!-- DRAM Chips -->
    <rect x="40" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="100" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="160" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="220" y="35" width="45" height="35" fill="#0f172a" rx="2"/>
    <!-- Centered Key Notch -->
    <rect x="375" y="70" width="16" height="15" fill="#0f172a"/>
    <text x="383" y="65" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">DDR5 Notch (Shifted)</text>
    <!-- PMIC Chip -->
    <rect x="300" y="38" width="30" height="25" fill="#d9a74a" rx="2"/>
    <text x="315" y="54" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">PMIC</text>
    <rect x="460" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="520" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="580" y="35" width="45" height="35" fill="#0f172a" rx="2"/><rect x="640" y="35" width="45" height="35" fill="#0f172a" rx="2"/>
  </g>

  <!-- Laptop SO-DIMM -->
  <g transform="translate(50, 305)">
    <rect width="400" height="110" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="4"/>
    <text x="20" y="24" fill="#f59e0b" font-size="12" font-weight="bold">Laptop SO-DIMM (Small Outline DIMM • 67.6 mm)</text>
    <rect x="30" y="40" width="40" height="40" fill="#0f172a" rx="2"/><rect x="85" y="40" width="40" height="40" fill="#0f172a" rx="2"/>
    <rect x="140" y="40" width="40" height="40" fill="#0f172a" rx="2"/>
    <!-- Notch -->
    <rect x="210" y="85" width="12" height="25" fill="#0f172a"/>
    <rect x="250" y="40" width="40" height="40" fill="#0f172a" rx="2"/><rect x="305" y="40" width="40" height="40" fill="#0f172a" rx="2"/>
    <text x="200" y="103" fill="#cbd5e1" font-size="10" text-anchor="middle">DDR4: 260 Pins | DDR5: 262 Pins</text>
  </g>

  <!-- Dual Channel Explanation -->
  <g transform="translate(470, 305)">
    <rect width="330" height="110" fill="#1e293b" stroke="#cbd5e1" stroke-width="1.5" rx="4"/>
    <text x="20" y="24" fill="#ffffff" font-size="12" font-weight="bold">Dual-Channel Installation Best Practice</text>
    <text x="20" y="48" fill="#94a3b8" font-size="11">• Matching pairs must go into <b>identical color slots</b>.</text>
    <text x="20" y="68" fill="#94a3b8" font-size="11">• Slots 1 &amp; 3 (Channel A) / Slots 2 &amp; 4 (Channel B).</text>
    <text x="20" y="88" fill="#38bdf8" font-size="11">• Doubles memory bus width from <b>64-bit to 128-bit</b>.</text>
    <text x="20" y="103" fill="#10b981" font-size="10" font-weight="bold">• Never mix speeds or latencies between channels.</text>
  </g>

  <!-- Footer Banner -->
  <rect x="50" y="430" width="750" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Critical A+ Rule: DDR4 and DDR5 DIMMs both have 288 pins, but incompatible notch alignments prevent cross-insertion.</text>
</svg>
</div>'''

# 4. Module 05: Storage Devices HDD vs SATA SSD vs M.2 NVMe & RAID SVG
M05_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 500" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Storage Technology Tiers &amp; RAID Levels Architecture</text>

  <!-- Drive Comparisons -->
  <g transform="translate(40, 95)">
    <!-- 3.5" HDD -->
    <rect x="0" y="0" width="235" height="175" fill="#1e293b" stroke="#64748b" stroke-width="1.5" rx="6"/>
    <text x="117" y="22" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">3.5-inch Mechanical HDD</text>
    <circle cx="117" cy="80" r="35" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="117" cy="80" r="10" fill="#475569"/>
    <line x1="117" y1="80" x2="145" y2="60" stroke="#d9a74a" stroke-width="2"/>
    <text x="117" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle">Spinning Platters • 7,200 RPM</text>
    <text x="117" y="152" fill="#94a3b8" font-size="10" text-anchor="middle">SATA III: ~150 - 200 MB/s</text>
    <text x="117" y="167" fill="#38bdf8" font-size="9" text-anchor="middle">Best $/TB for Bulk Storage</text>

    <!-- 2.5" SATA SSD -->
    <rect x="255" y="0" width="235" height="175" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" rx="6"/>
    <text x="372" y="22" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">2.5-inch SATA SSD</text>
    <rect x="290" y="45" width="165" height="70" fill="#0f172a" rx="4"/>
    <rect x="305" y="55" width="30" height="25" fill="#334155" rx="2"/><rect x="345" y="55" width="30" height="25" fill="#334155" rx="2"/><rect x="385" y="55" width="30" height="25" fill="#334155" rx="2"/>
    <rect x="305" y="85" width="30" height="25" fill="#334155" rx="2"/><rect x="345" y="85" width="30" height="25" fill="#334155" rx="2"/><rect x="385" y="85" width="30" height="25" fill="#334155" rx="2"/>
    <text x="372" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle">NAND Flash • No Moving Parts</text>
    <text x="372" y="152" fill="#94a3b8" font-size="10" text-anchor="middle">SATA III: Max ~550 MB/s (Capped)</text>
    <text x="372" y="167" fill="#10b981" font-size="9" text-anchor="middle">Drop-in replacement for HDDs</text>

    <!-- M.2 NVMe SSD -->
    <rect x="510" y="0" width="260" height="175" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="640" y="22" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">M.2 2280 NVMe SSD</text>
    <rect x="535" y="55" width="210" height="50" fill="#0f172a" stroke="#d9a74a" rx="3"/>
    <rect x="550" y="65" width="35" height="30" fill="#334155" rx="2"/><rect x="600" y="65" width="35" height="30" fill="#334155" rx="2"/><rect x="650" y="65" width="35" height="30" fill="#334155" rx="2"/>
    <rect x="735" y="75" width="10" height="10" fill="#0f172a"/>
    <text x="640" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle">PCIe Gen 4/5 x4 Bus Architecture</text>
    <text x="640" y="152" fill="#d9a74a" font-size="10" font-weight="bold" text-anchor="middle">Speeds: 3,500 – 7,500+ MB/s</text>
    <text x="640" y="167" fill="#38bdf8" font-size="9" text-anchor="middle">Direct Motherboard Screw Mount</text>
  </g>

  <!-- RAID Levels Breakdown -->
  <g transform="translate(40, 290)">
    <rect width="770" height="150" fill="#1e293b" stroke="#334155" stroke-width="1.5" rx="6"/>
    <text x="385" y="24" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">CompTIA A+ RAID Level Reference</text>

    <!-- RAID 0 -->
    <rect x="15" y="38" width="170" height="100" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="100" y="58" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">RAID 0 (Striping)</text>
    <text x="100" y="78" fill="#cbd5e1" font-size="10" text-anchor="middle">Min Drives: 2</text>
    <text x="100" y="96" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Fault Tolerance: ZERO</text>
    <text x="100" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">High Performance Only</text>
    <text x="100" y="128" fill="#64748b" font-size="9" text-anchor="middle">1 Drive Lost = All Lost</text>

    <!-- RAID 1 -->
    <rect x="200" y="38" width="170" height="100" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="285" y="58" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">RAID 1 (Mirroring)</text>
    <text x="285" y="78" fill="#cbd5e1" font-size="10" text-anchor="middle">Min Drives: 2</text>
    <text x="285" y="96" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Fault Tolerance: 1 Drive</text>
    <text x="285" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">50% Usable Capacity</text>
    <text x="285" y="128" fill="#64748b" font-size="9" text-anchor="middle">Duplicate Exact Copy</text>

    <!-- RAID 5 -->
    <rect x="385" y="38" width="180" height="100" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="475" y="58" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">RAID 5 (Parity)</text>
    <text x="475" y="78" fill="#cbd5e1" font-size="10" text-anchor="middle">Min Drives: 3</text>
    <text x="475" y="96" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Fault Tolerance: 1 Drive</text>
    <text x="475" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">Capacity: (N-1) Drives</text>
    <text x="475" y="128" fill="#64748b" font-size="9" text-anchor="middle">Distributed Parity Blocks</text>

    <!-- RAID 10 -->
    <rect x="580" y="38" width="175" height="100" fill="#0f172a" stroke="#d9a74a" rx="4"/>
    <text x="667" y="58" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">RAID 10 (1+0 Striped Mirrors)</text>
    <text x="667" y="78" fill="#cbd5e1" font-size="10" text-anchor="middle">Min Drives: 4</text>
    <text x="667" y="96" fill="#d9a74a" font-size="10" font-weight="bold" text-anchor="middle">Fault Tolerance: 1 Per Pair</text>
    <text x="667" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">Capacity: 50% Total</text>
    <text x="667" y="128" fill="#64748b" font-size="9" text-anchor="middle">High Speed + Redundancy</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="455" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="477" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ A+ Blueprint Trap: M.2 is a physical form factor — always verify if the motherboard M.2 slot supports NVMe (PCIe) or SATA!</text>
</svg>
</div>'''

# 5. Module 06: Power Supply Connectors & Airflow SVG
M06_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Power Supply Connectors &amp; PC Chassis Airflow Dynamics</text>

  <!-- PSU Connectors -->
  <g transform="translate(40, 95)">
    <rect width="380" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="190" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Essential PSU Power Connectors</text>

    <!-- 24-Pin ATX -->
    <rect x="20" y="40" width="340" height="48" fill="#0f172a" rx="4"/>
    <text x="35" y="60" fill="#f8fafc" font-size="11" font-weight="bold">24-Pin ATX Main Power</text>
    <text x="35" y="78" fill="#94a3b8" font-size="10">Powers motherboard chipset, PCIe slots, logic (3.3V, 5V, 12V)</text>

    <!-- 4/8-Pin EPS -->
    <rect x="20" y="98" width="340" height="48" fill="#0f172a" rx="4"/>
    <text x="35" y="118" fill="#f8fafc" font-size="11" font-weight="bold">4-Pin / 8-Pin (4+4) EPS 12V CPU</text>
    <text x="35" y="136" fill="#94a3b8" font-size="10">Dedicated power directly to the CPU socket power regulation</text>

    <!-- 6/8-Pin PCIe -->
    <rect x="20" y="156" width="340" height="48" fill="#0f172a" rx="4"/>
    <text x="35" y="176" fill="#f8fafc" font-size="11" font-weight="bold">6-Pin (75W) &amp; 8-Pin (150W) PCIe</text>
    <text x="35" y="194" fill="#94a3b8" font-size="10">Dedicated supplemental 12V power for discrete graphics cards</text>

    <!-- 15-Pin SATA -->
    <rect x="20" y="214" width="340" height="48" fill="#0f172a" rx="4"/>
    <text x="35" y="234" fill="#f8fafc" font-size="11" font-weight="bold">15-Pin SATA Power (L-Shaped)</text>
    <text x="35" y="252" fill="#94a3b8" font-size="10">Supplies 3.3V, 5V, and 12V to SATA SSDs, HDDs, and RGB hubs</text>

    <!-- 4-Pin Molex -->
    <rect x="20" y="272" width="340" height="42" fill="#0f172a" rx="4"/>
    <text x="35" y="290" fill="#f8fafc" font-size="11" font-weight="bold">4-Pin Molex Legacy Connector</text>
    <text x="35" y="306" fill="#94a3b8" font-size="10">Legacy drives, case fans, water cooling pumps (5V &amp; 12V)</text>
  </g>

  <!-- Airflow & Thermal Dynamics -->
  <g transform="translate(440, 95)">
    <rect width="370" height="325" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="185" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Chassis Airflow &amp; Pressure Profiles</text>

    <!-- Chassis Case Schematic -->
    <rect x="25" y="45" width="320" height="175" fill="#0f172a" stroke="#64748b" rx="4"/>
    
    <!-- Front Intake Fans -->
    <rect x="35" y="65" width="20" height="50" fill="#0284c7" rx="2"/>
    <rect x="35" y="125" width="20" height="50" fill="#0284c7" rx="2"/>
    <text x="45" y="195" fill="#38bdf8" font-size="9" text-anchor="middle">Front Intake</text>
    <path d="M 65 90 L 130 90" stroke="#38bdf8" stroke-width="2" marker-end="url(#arr)"/>
    <path d="M 65 150 L 130 150" stroke="#38bdf8" stroke-width="2"/>

    <!-- CPU Cooler Center -->
    <rect x="150" y="90" width="60" height="60" fill="#334155" stroke="#ef4444" rx="4"/>
    <text x="180" y="125" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">CPU HSF</text>

    <!-- Rear Exhaust -->
    <rect x="315" y="80" width="20" height="50" fill="#ef4444" rx="2"/>
    <text x="325" y="150" fill="#fca5a5" font-size="9" text-anchor="middle">Rear Exhaust</text>
    <path d="M 220 105 L 305 105" stroke="#ef4444" stroke-width="2"/>

    <!-- Pressure Types -->
    <rect x="25" y="230" width="320" height="80" fill="#0f172a" rx="4"/>
    <text x="35" y="248" fill="#10b981" font-size="11" font-weight="bold">Positive Pressure (Recommended):</text>
    <text x="35" y="265" fill="#cbd5e1" font-size="10">Intake CFM &gt; Exhaust CFM. Forces air out cracks,</text>
    <text x="35" y="280" fill="#cbd5e1" font-size="10">preventing unfiltered dust accumulation.</text>
    <text x="35" y="298" fill="#fca5a5" font-size="10"><b>Negative Pressure:</b> Exhaust &gt; Intake (draws dust in).</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Technician Safety Warning: Never open a PSU chassis. High-voltage capacitors store lethal charges for days.</text>
</svg>
</div>'''

# 6. Module 07: Display & Peripheral Connectors Comparison SVG
M07_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Video Display Interfaces &amp; Connector Form Factors</text>

  <!-- Connectors Grid -->
  <g transform="translate(40, 95)">
    <!-- HDMI -->
    <rect x="0" y="0" width="180" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="90" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">HDMI</text>
    <rect x="30" y="45" width="120" height="55" fill="#0f172a" stroke="#cbd5e1" rx="4"/>
    <text x="90" y="78" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">19-Pin Trapezoid</text>
    <text x="90" y="125" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Audio + Video</text>
    <text x="90" y="145" fill="#94a3b8" font-size="10" text-anchor="middle">HDMI 2.0 / 2.1</text>
    <text x="90" y="165" fill="#cbd5e1" font-size="10" text-anchor="middle">4K @ 120Hz / 8K @ 60Hz</text>
    <rect x="15" y="195" width="150" height="110" fill="#0f172a" rx="4"/>
    <text x="25" y="215" fill="#cbd5e1" font-size="9">• Consumer standard</text>
    <text x="25" y="235" fill="#cbd5e1" font-size="9">• TVs &amp; PC Monitors</text>
    <text x="25" y="255" fill="#cbd5e1" font-size="9">• CEC &amp; eARC support</text>
    <text x="25" y="275" fill="#cbd5e1" font-size="9">• Length: up to 15m</text>
    <text x="25" y="295" fill="#38bdf8" font-size="9">Friction-fit retention</text>

    <!-- DisplayPort -->
    <rect x="200" y="0" width="180" height="325" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="290" y="25" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">DisplayPort (DP)</text>
    <rect x="230" y="45" width="120" height="55" fill="#0f172a" stroke="#cbd5e1" rx="4"/>
    <text x="290" y="78" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">20-Pin (1 Angled Corner)</text>
    <text x="290" y="125" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Audio + Video + MST</text>
    <text x="290" y="145" fill="#94a3b8" font-size="10" text-anchor="middle">DP 1.4 / 2.0</text>
    <text x="290" y="165" fill="#cbd5e1" font-size="10" text-anchor="middle">Daisy-Chaining (MST)</text>
    <rect x="215" y="195" width="150" height="110" fill="#0f172a" rx="4"/>
    <text x="225" y="215" fill="#cbd5e1" font-size="9">• PC / Workstation standard</text>
    <text x="225" y="235" fill="#cbd5e1" font-size="9">• Mechanical locking latch</text>
    <text x="225" y="255" fill="#cbd5e1" font-size="9">• Multi-Stream Transport</text>
    <text x="225" y="275" fill="#cbd5e1" font-size="9">• High refresh rates</text>
    <text x="225" y="295" fill="#10b981" font-size="9">Preferred for PC gaming</text>

    <!-- DVI -->
    <rect x="400" y="0" width="180" height="325" fill="#1e293b" stroke="#a855f7" stroke-width="2" rx="6"/>
    <text x="490" y="25" fill="#a855f7" font-size="13" font-weight="bold" text-anchor="middle">DVI-D / DVI-I</text>
    <rect x="430" y="45" width="120" height="55" fill="#0f172a" stroke="#cbd5e1" rx="4"/>
    <text x="490" y="78" fill="#a855f7" font-size="11" font-weight="bold" text-anchor="middle">24-Pin Dual-Link Grid</text>
    <text x="490" y="125" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Video Only (No Audio)</text>
    <text x="490" y="145" fill="#94a3b8" font-size="10" text-anchor="middle">Dual-Link: 2560×1600</text>
    <text x="490" y="165" fill="#cbd5e1" font-size="10" text-anchor="middle">Single-Link: 1920×1200</text>
    <rect x="415" y="195" width="150" height="110" fill="#0f172a" rx="4"/>
    <text x="425" y="215" fill="#cbd5e1" font-size="9">• DVI-D: Digital only</text>
    <text x="425" y="235" fill="#cbd5e1" font-size="9">• DVI-I: Digital + Analog</text>
    <text x="425" y="255" fill="#cbd5e1" font-size="9">• Screw-post retention</text>
    <text x="425" y="275" fill="#cbd5e1" font-size="9">• Legacy transition standard</text>
    <text x="425" y="295" fill="#a855f7" font-size="9">Replaced by DP &amp; HDMI</text>

    <!-- VGA -->
    <rect x="600" y="0" width="170" height="325" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="6"/>
    <text x="685" y="25" fill="#94a3b8" font-size="13" font-weight="bold" text-anchor="middle">VGA (DE-15)</text>
    <rect x="625" y="45" width="120" height="55" fill="#0284c7" rx="4"/>
    <text x="685" y="78" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">15-Pin (3 Rows of 5)</text>
    <text x="685" y="125" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Analog Video Only</text>
    <text x="685" y="145" fill="#94a3b8" font-size="10" text-anchor="middle">Max: 2048×1536</text>
    <text x="685" y="165" fill="#cbd5e1" font-size="10" text-anchor="middle">Susceptible to Interference</text>
    <rect x="615" y="195" width="140" height="110" fill="#0f172a" rx="4"/>
    <text x="625" y="215" fill="#cbd5e1" font-size="9">• Traditional blue plug</text>
    <text x="625" y="235" fill="#cbd5e1" font-size="9">• Analog RGB signaling</text>
    <text x="625" y="255" fill="#cbd5e1" font-size="9">• Screw-in fasteners</text>
    <text x="625" y="275" fill="#cbd5e1" font-size="9">• Legacy projectors / PCs</text>
    <text x="625" y="295" fill="#ef4444" font-size="9">Requires D/A converter</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ CompTIA A+ Identification Tip: DisplayPort has ONE angled corner with latch; HDMI has TWO symmetric angled corners.</text>
</svg>
</div>'''

# 7. Module 11: Network Cabling Cat5e/6/6a & T568A/B SVG
M11_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Ethernet Cable Categories &amp; T568A vs. T568B Color Wiring Standards</text>

  <!-- Wiring Diagrams (T568A vs T568B) -->
  <g transform="translate(40, 95)">
    <!-- T568A -->
    <rect x="0" y="0" width="375" height="325" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="187" y="25" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">T568A Pinout Standard (Residential / Gov)</text>
    
    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="16" fill="#86efac" font-size="10">Pin 1: White / Green</text>
      <rect x="0" y="28" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="44" fill="#22c55e" font-size="10">Pin 2: Green</text>
      <rect x="0" y="56" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="72" fill="#fdba74" font-size="10">Pin 3: White / Orange</text>
      <rect x="0" y="84" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="100" fill="#3b82f6" font-size="10">Pin 4: Blue</text>
      <rect x="0" y="112" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="128" fill="#93c5fd" font-size="10">Pin 5: White / Blue</text>
      <rect x="0" y="140" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="156" fill="#f97316" font-size="10">Pin 6: Orange</text>
      <rect x="0" y="168" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="184" fill="#d6d3d1" font-size="10">Pin 7: White / Brown</text>
      <rect x="0" y="196" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="212" fill="#a8a29e" font-size="10">Pin 8: Brown</text>
    </g>
    <text x="187" y="300" fill="#cbd5e1" font-size="10" text-anchor="middle">Used primarily in federal installations &amp; residential telecom</text>
  </g>

  <!-- T568B -->
  <g transform="translate(435, 95)">
    <rect x="0" y="0" width="375" height="325" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <text x="187" y="25" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">T568B Pinout Standard (Commercial Default)</text>
    
    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="16" fill="#fdba74" font-size="10">Pin 1: White / Orange</text>
      <rect x="0" y="28" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="44" fill="#f97316" font-size="10">Pin 2: Orange</text>
      <rect x="0" y="56" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="72" fill="#86efac" font-size="10">Pin 3: White / Green</text>
      <rect x="0" y="84" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="100" fill="#3b82f6" font-size="10">Pin 4: Blue</text>
      <rect x="0" y="112" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="128" fill="#93c5fd" font-size="10">Pin 5: White / Blue</text>
      <rect x="0" y="140" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="156" fill="#22c55e" font-size="10">Pin 6: Green</text>
      <rect x="0" y="168" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="184" fill="#d6d3d1" font-size="10">Pin 7: White / Brown</text>
      <rect x="0" y="196" width="325" height="24" fill="#0f172a" rx="3"/><text x="10" y="212" fill="#a8a29e" font-size="10">Pin 8: Brown</text>
    </g>
    <text x="187" y="300" fill="#cbd5e1" font-size="10" text-anchor="middle">De facto commercial standard across modern enterprise networks</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Cable Rule: Straight-through = Same on both ends | Crossover = T568A on one end, T568B on the other.</text>
</svg>
</div>'''

# 8. Module 12: Network Devices Hub vs Switch vs Router & Rack Layout SVG
M12_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Network Infrastructure Devices &amp; Standard 19" Rack Architecture</text>

  <!-- OSI Device Hierarchy -->
  <g transform="translate(40, 95)">
    <rect width="420" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="210" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">OSI Device Layer Assignments</text>

    <!-- Layer 3 Router -->
    <rect x="20" y="40" width="380" height="80" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="35" y="60" fill="#ef4444" font-size="12" font-weight="bold">Layer 3: Network Layer Router / Firewall</text>
    <text x="35" y="78" fill="#f8fafc" font-size="10">• Addresses: Logical IP Addresses (IPv4/IPv6)</text>
    <text x="35" y="94" fill="#cbd5e1" font-size="10">• Function: Connects disparate networks; breaks broadcast domains</text>
    <text x="35" y="108" fill="#94a3b8" font-size="9">PDU: Packet | Protocol: OSPF, BGP, NAT</text>

    <!-- Layer 2 Switch -->
    <rect x="20" y="130" width="380" height="85" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="35" y="150" fill="#10b981" font-size="12" font-weight="bold">Layer 2: Data Link Layer Switch / WAP / Bridge</text>
    <text x="35" y="168" fill="#f8fafc" font-size="10">• Addresses: Physical MAC Addresses (48-bit EUI-48)</text>
    <text x="35" y="184" fill="#cbd5e1" font-size="10">• Function: Forwards frames via MAC Address Table; separates collision domains</text>
    <text x="35" y="200" fill="#94a3b8" font-size="9">PDU: Frame | Features: VLANs (802.1Q), PoE (802.3af/at/bt)</text>

    <!-- Layer 1 Hub -->
    <rect x="20" y="225" width="380" height="85" fill="#0f172a" stroke="#64748b" rx="4"/>
    <text x="35" y="245" fill="#94a3b8" font-size="12" font-weight="bold">Layer 1: Physical Layer Hub / Repeater / Patch Panel</text>
    <text x="35" y="263" fill="#f8fafc" font-size="10">• Signals: Electrical, Optical, or RF Bits</text>
    <text x="35" y="279" fill="#cbd5e1" font-size="10">• Function: Multi-port repeater; single collision &amp; broadcast domain</text>
    <text x="35" y="295" fill="#fca5a5" font-size="9">Legacy device — high collision rates. Replaced by switches.</text>
  </g>

  <!-- 19-inch Equipment Rack Layout -->
  <g transform="translate(480, 95)">
    <rect width="330" height="325" fill="#1e293b" stroke="#d9a74a" stroke-width="1.5" rx="6"/>
    <text x="165" y="24" fill="#d9a74a" font-size="13" font-weight="bold" text-anchor="middle">Standard 19" Rack Elevation (Top to Bottom)</text>

    <!-- Rack Posts -->
    <line x1="20" y1="40" x2="20" y2="310" stroke="#475569" stroke-width="4"/>
    <line x1="310" y1="40" x2="310" y2="310" stroke="#475569" stroke-width="4"/>

    <!-- Patch Panel -->
    <rect x="30" y="45" width="270" height="35" fill="#0f172a" stroke="#94a3b8" rx="2"/>
    <text x="165" y="67" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1U 24-Port Patch Panel (Structured Cable Punchdown)</text>

    <!-- Switch -->
    <rect x="30" y="90" width="270" height="35" fill="#0f172a" stroke="#10b981" rx="2"/>
    <text x="165" y="112" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">1U Managed Gigabit PoE+ Switch</text>

    <!-- Router / Firewall -->
    <rect x="30" y="135" width="270" height="35" fill="#0f172a" stroke="#ef4444" rx="2"/>
    <text x="165" y="157" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">1U Enterprise Next-Gen Firewall / Edge Router</text>

    <!-- Server -->
    <rect x="30" y="180" width="270" height="50" fill="#0f172a" stroke="#38bdf8" rx="2"/>
    <text x="165" y="210" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">2U Rackmount Server (Host / SAN)</text>

    <!-- UPS -->
    <rect x="30" y="240" width="270" height="60" fill="#0f172a" stroke="#f59e0b" rx="2"/>
    <text x="165" y="268" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">2U / 3U UPS Battery Backup</text>
    <text x="165" y="285" fill="#94a3b8" font-size="9" text-anchor="middle">Placed at lowest U for center of gravity stability</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ CompTIA A+ Key Principle: Always mount heavy UPS units at the rack bottom to prevent tipping hazards.</text>
</svg>
</div>'''

# 9. Module 13: Laptop Disassembly & Mobile Architecture SVG
M13_SVG = '''<div style="text-align: center; margin: 24px 0;">
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
</div>'''

MODULE_MAP = {
    "Module_01": M01_SVG,
    "Module_03": M03_SVG,
    "Module_04": M04_SVG,
    "Module_05": M05_SVG,
    "Module_06": M06_SVG,
    "Module_07": M07_SVG,
    "Module_11": M11_SVG,
    "Module_12": M12_SVG,
    "Module_13": M13_SVG,
}

def inject_visuals():
    print("Beginning systematic SVG injection across CIS-2320 Hardware Fundamentals...")
    for mod_name, svg_content in MODULE_MAP.items():
        mod_dir = os.path.join(BASE_DIR, mod_name)
        if not os.path.exists(mod_dir):
            continue
        
        # Inject into Video Script
        vs_files = [f for f in os.listdir(mod_dir) if f.startswith("01_Video_Script")]
        if vs_files:
            vs_path = os.path.join(mod_dir, vs_files[0])
            with open(vs_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find the first major SHOW COMPONENT cue in body and prepend/replace with SVG
            if "<svg" not in content:
                # Replace the first SHOW COMPONENT cue
                m = re.search(r'(\*\*?\[SHOW COMPONENT:[^\]]+\]\*\*?)', content)
                if m:
                    cue_matched = m.group(1)
                    new_content = content.replace(cue_matched, f"{svg_content}\n\n{cue_matched}", 1)
                    with open(vs_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"  ✓ Injected technical SVG into Video Script: {mod_name}/{vs_files[0]}")
                else:
                    print(f"  - No cue found in Video Script {mod_name}")
            else:
                print(f"  - Video Script already has SVG: {mod_name}")

        # Inject into Reading Guide
        rg_files = [f for f in os.listdir(mod_dir) if "Reading_Guide" in f]
        if rg_files:
            rg_path = os.path.join(mod_dir, rg_files[0])
            with open(rg_path, "r", encoding="utf-8") as f:
                rg_content = f.read()
            
            # Check if specialized topic SVG already present (besides the generic workflow banner)
            if "TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS" not in rg_content:
                # Insert after the video embed or at beginning of section 1
                if "## 1." in rg_content:
                    parts = rg_content.split("## 1.", 1)
                    new_rg = parts[0] + f"{svg_content}\n\n## 1." + parts[1]
                elif "### 1." in rg_content:
                    parts = rg_content.split("### 1.", 1)
                    new_rg = parts[0] + f"{svg_content}\n\n### 1." + parts[1]
                else:
                    # After end of video embed
                    if "<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->" in rg_content:
                        parts = rg_content.split("<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->", 1)
                        new_rg = parts[0] + "<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->\n\n" + svg_content + parts[1]
                    else:
                        new_rg = svg_content + "\n\n" + rg_content
                
                with open(rg_path, "w", encoding="utf-8") as f:
                    f.write(new_rg)
                print(f"  ✓ Injected technical SVG into Reading Guide: {mod_name}/{rg_files[0]}")
            else:
                print(f"  - Reading Guide already has topic SVG: {mod_name}")

    print("\nInjection complete.")

if __name__ == "__main__":
    inject_visuals()

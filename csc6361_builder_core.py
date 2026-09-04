# -*- coding: utf-8 -*-
"""
CSC-6361 Course Builder for Canvas LMS
Course: CSC-6361-33: Computer Networks
Term: 2026 Fall 7-WEEK 2 Session (10/19/2026 - 12/11/2026)
Course ID: 12666
"""

import os, re, json, time, sys, urllib.request, urllib.parse, urllib.error
from pathlib import Path

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
COURSE_ID  = 12666
BASE_DIR   = Path(__file__).parent / "CSC-6361_Computer_Networks"

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

def api_call(method: str, path: str, data: dict = None) -> dict | list:
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            res = r.read()
            return json.loads(res) if res else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read()[:300].decode('utf-8', errors='replace')
        print(f"    [{method} ERROR] {path}: {e.code} -> {err_msg}")
        return {}
    except Exception as ex:
        print(f"    [{method} EXCEPTION] {path}: {ex}")
        return {}

def api_get(path): return api_call('GET', path)
def api_post(path, data): return api_call('POST', path, data)
def api_put(path, data): return api_call('PUT', path, data)
def api_delete(path): return api_call('DELETE', path)

# ─── MARKDOWN PARSER ──────────────────────────────────────────────────────────
def md2html(text: str) -> str:
    if not text:
        return ""
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    code_blocks = []
    def _store_code(m):
        lang = m.group(1) or ""
        code = m.group(2).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        idx = len(code_blocks)
        lc = f' class="language-{lang}"' if lang else ''
        code_blocks.append(
            f'<pre style="background:#1e1e1e;color:#d4d4d4;padding:16px;border-radius:6px;'
            f'overflow-x:auto;font-family:Consolas,monospace;font-size:13px;line-height:1.5;">'
            f'<code{lc}>{code}</code></pre>'
        )
        return f'__CODE_{idx}__'

    text = re.sub(r'```(\w*)\n(.*?)```', _store_code, text, flags=re.DOTALL)

    def _inline(s):
        s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'__(.+?)__', r'<strong>\1</strong>', s)
        s = re.sub(r'\*([^*\n]+?)\*', r'<em>\1</em>', s)
        s = re.sub(r'_([^_\n]+?)_', r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+?)`', r'<code style="background:#f4f4f4;color:#c7254e;padding:2px 6px;border-radius:3px;font-family:Consolas,monospace;font-size:90%;">\1</code>', s)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" style="color:#8b0000;text-decoration:underline;">\1</a>', s)
        return s

    lines = text.split('\n')
    out = []
    in_list = None
    in_bq = False
    in_table = False
    t_headers = []
    t_rows = []

    def flush_list():
        nonlocal in_list
        if in_list:
            out.append(f'</{in_list}>')
            in_list = None

    def flush_bq():
        nonlocal in_bq
        if in_bq:
            out.append('</blockquote>')
            in_bq = False

    def flush_table():
        nonlocal in_table, t_headers, t_rows
        if in_table:
            rows_html = ''
            if t_headers:
                rows_html += '<thead><tr>'
                for h in t_headers:
                    rows_html += f'<th style="padding:10px 14px;background:#8b0000;color:#fff;text-align:left;border:1px solid #700000;font-size:14px;">{_inline(h.strip())}</th>'
                rows_html += '</tr></thead>'
            if t_rows:
                rows_html += '<tbody>'
                for i, row in enumerate(t_rows):
                    bg = '#ffffff' if i % 2 == 0 else '#f9f9f9'
                    rows_html += f'<tr style="background:{bg};">'
                    for td in row:
                        rows_html += f'<td style="padding:8px 12px;border:1px solid #ddd;font-size:13px;line-height:1.5;">{_inline(td.strip())}</td>'
                    rows_html += '</tr>'
                rows_html += '</tbody>'
            out.append(f'<div style="overflow-x:auto;margin:18px 0;"><table style="border-collapse:collapse;width:100%;">{rows_html}</table></div>')
            in_table = False
            t_headers.clear()
            t_rows.clear()

    for line in lines:
        raw = line.strip()

        if raw.startswith('__CODE_') and raw.endswith('__'):
            flush_list(); flush_bq(); flush_table()
            out.append(code_blocks[int(raw[7:-2])])
            continue

        if re.match(r'^(-{3,}|\*{3,}|_{3,})\s*$', raw):
            flush_list(); flush_bq(); flush_table()
            out.append('<hr style="border:none;border-top:2px solid #8b0000;margin:24px 0;">')
            continue

        hm = re.match(r'^(#{1,6})\s+(.+)$', raw)
        if hm:
            flush_list(); flush_bq(); flush_table()
            lvl = len(hm.group(1))
            sizes = {1:'26px', 2:'21px', 3:'17px', 4:'15px', 5:'14px', 6:'13px'}
            color = '#8b0000' if lvl <= 2 else '#333333'
            bb = 'border-bottom:2px solid #b22222;padding-bottom:6px;' if lvl <= 2 else ''
            out.append(f'<h{lvl} style="font-size:{sizes[lvl]};color:{color};margin:20px 0 10px;font-weight:bold;{bb}">{_inline(hm.group(2))}</h{lvl}>')
            continue

        if raw.startswith('|') and raw.endswith('|'):
            flush_list(); flush_bq()
            cells = raw.split('|')[1:-1]
            if all(re.match(r'^\s*:?-+:?\s*$', c) for c in cells):
                continue
            if not in_table:
                in_table = True
                t_headers = cells
            else:
                t_rows.append(cells)
            continue
        else:
            flush_table()

        if raw.startswith('>'):
            flush_list(); flush_table()
            bq_text = _inline(re.sub(r'^>\s*', '', raw))
            if not in_bq:
                out.append('<blockquote style="border-left:4px solid #b22222;margin:16px 0;padding:12px 18px;background:#fff8f8;color:#444;font-style:italic;">')
                in_bq = True
            out.append(f'<p style="margin:4px 0;line-height:1.6;">{bq_text}</p>')
            continue
        else:
            flush_bq()

        ul_m = re.match(r'^[-*+]\s+(.+)$', raw)
        if ul_m:
            flush_bq(); flush_table()
            if in_list != 'ul':
                flush_list()
                out.append('<ul style="margin:8px 0;padding-left:24px;line-height:1.7;">')
                in_list = 'ul'
            out.append(f'<li style="margin:4px 0;">{_inline(ul_m.group(1))}</li>')
            continue

        ol_m = re.match(r'^\d+\.\s+(.+)$', raw)
        if ol_m:
            flush_bq(); flush_table()
            if in_list != 'ol':
                flush_list()
                out.append('<ol style="margin:8px 0;padding-left:24px;line-height:1.7;">')
                in_list = 'ol'
            out.append(f'<li style="margin:4px 0;">{_inline(ol_m.group(1))}</li>')
            continue

        if not raw:
            flush_list(); flush_bq(); flush_table()
            continue

        flush_list(); flush_bq(); flush_table()
        out.append(f'<p style="margin:8px 0;line-height:1.75;font-size:14.5px;color:#2c3e50;">{_inline(raw)}</p>')

    flush_list(); flush_bq(); flush_table()
    return '\n'.join(out)


# ─── QUIZ PARSER ──────────────────────────────────────────────────────────────
def parse_quiz(md_text: str) -> list:
    questions = []
    SPLIT = re.compile(
        r'(\n(?:#{2,3}\s+Question\s*\d+|####\s+Q\d+(?=\n)|\*\*Question\s+\d+[^*\n]*\*\*)[^\n]*\n)',
        re.IGNORECASE
    )
    parts = SPLIT.split(md_text)
    pairs = []
    i = 1
    while i + 1 < len(parts):
        pairs.append((parts[i], parts[i+1]))
        i += 2

    for header, block in pairs:
        ha = re.search(r'Answer\s*:\s*([A-D])', header, re.I)
        header_ans = ha.group(1).upper() if ha else None

        opt_start = re.search(r'\n\s*[-*]?\s*[A-D][.):]\s', block)
        if not opt_start:
            continue
        stem = block[:opt_start.start()].strip()
        stem = re.sub(r'^(?:\*\*[^*]+\*\*\s*\n)+', '', stem).strip()
        if not stem:
            continue

        options = {}
        for m in re.finditer(
            r'(?:^|\n)\s*[-*]?\s*([A-D])[.):]\s+(.*?)'
            r'(?=\n\s*[-*]?\s*[A-D][.):]\s|\n\n(?:Correct|\*\*Correct|Distractor|---|\Z)|\Z)',
            block, re.DOTALL
        ):
            lbl  = m.group(1).upper()
            text = re.sub(r'\n+', ' ', m.group(2).strip())
            text = re.sub(r'\*\*', '', text).strip()
            text = re.split(r'\s+—\s+|\s*---\s*', text)[0].strip()
            text = re.split(r'\*?Correct\s+Answer', text, flags=re.I)[0].strip()
            options[lbl] = text

        if len(options) < 2:
            continue

        if header_ans and header_ans in options:
            correct = header_ans
        else:
            ca = re.search(r'(?:Correct\s+)?Answer[:\s*\d]*[:\s*]+\**\s*([A-D])', block, re.I)
            if not ca:
                continue
            correct = ca.group(1).upper()
            if correct not in options:
                continue

        questions.append({'stem': stem, 'options': options, 'correct': correct})

    return questions


# ─── DETAILED SVG DIAGRAM GENERATOR ──────────────────────────────────────────
def get_csc6361_diagram(mod_num: int) -> str:
    """Returns high-resolution, informative inline SVG diagrams for each module."""
    if mod_num == 1:
        # Multi-Area OSPF & EIGRP Architecture
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">Enterprise Multi-Area OSPF &amp; EIGRP Redistribution Architecture</text>
  
  <!-- Area 1 Box -->
  <rect x="25" y="60" width="180" height="230" rx="8" fill="#e8f4fc" stroke="#2a7ab5" stroke-width="2" stroke-dasharray="4"/>
  <text x="115" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a5a8a" font-family="Arial">Area 1 (Stub / Standard)</text>
  <text x="115" y="103" text-anchor="middle" font-size="11" fill="#555" font-family="Arial">Internal Subnets: 10.1.0.0/16</text>
  
  <!-- Router 1 -->
  <rect x="55" y="130" width="120" height="50" rx="6" fill="#2a7ab5"/>
  <text x="115" y="153" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">R1 (Internal)</text>
  <text x="115" y="169" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">RID: 10.1.99.1</text>
  
  <!-- Area 0 Backbone Box -->
  <rect x="220" y="60" width="240" height="230" rx="8" fill="#fff5f5" stroke="#b22222" stroke-width="2"/>
  <text x="340" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#8b0000" font-family="Arial">Area 0 (Backbone Core)</text>
  <text x="340" y="103" text-anchor="middle" font-size="11" fill="#666" font-family="Arial">Transit Core: 10.0.0.0/16</text>

  <!-- Router 3 ABR -->
  <rect x="235" y="130" width="100" height="50" rx="6" fill="#b22222"/>
  <text x="285" y="153" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">R3 (ABR)</text>
  <text x="285" y="169" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">Type 3 LSA Summary</text>

  <!-- Router 2 Core -->
  <rect x="350" y="130" width="95" height="50" rx="6" fill="#8b0000"/>
  <text x="397" y="153" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">R2 (Core)</text>
  <text x="397" y="169" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">RID: 10.0.99.1</text>

  <!-- EIGRP Domain Box -->
  <rect x="475" y="60" width="180" height="230" rx="8" fill="#fef8e7" stroke="#d4780a" stroke-width="2" stroke-dasharray="4"/>
  <text x="565" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#995000" font-family="Arial">EIGRP AS 100</text>
  <text x="565" y="103" text-anchor="middle" font-size="11" fill="#555" font-family="Arial">Acquired Entity: 10.100.0.0/16</text>

  <!-- Router 4 ASBR -->
  <rect x="485" y="130" width="90" height="50" rx="6" fill="#d4780a"/>
  <text x="530" y="153" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">R4 (ASBR)</text>
  <text x="530" y="169" text-anchor="middle" fill="#fff3d9" font-size="10" font-family="Arial">Type 5 / Ext Metric</text>

  <!-- Router 5 EIGRP -->
  <rect x="585" y="130" width="60" height="50" rx="6" fill="#b35f00"/>
  <text x="615" y="153" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">R5</text>
  <text x="615" y="169" text-anchor="middle" fill="#fff3d9" font-size="10" font-family="Arial">AS 100</text>

  <!-- Connecting Lines -->
  <line x1="175" y1="155" x2="235" y2="155" stroke="#333" stroke-width="2"/>
  <line x1="335" y1="155" x2="350" y2="155" stroke="#333" stroke-width="2"/>
  <line x1="445" y1="155" x2="485" y2="155" stroke="#333" stroke-width="2"/>
  <line x1="575" y1="155" x2="585" y2="155" stroke="#333" stroke-width="2"/>

  <!-- Protocol summary banner at bottom -->
  <rect x="25" y="305" width="630" height="60" rx="6" fill="#ffffff" stroke="#ddd" stroke-width="1"/>
  <text x="45" y="327" font-size="12" font-weight="bold" fill="#8b0000" font-family="Arial">Key Protocol Rules &amp; Operations:</text>
  <text x="45" y="347" font-size="11" fill="#333" font-family="Arial">• <strong>ABR (R3)</strong> summarizes Type 1/2 LSAs into Type 3 Summary LSAs to insulate Area 0 from Area 1 link flaps.</text>
  <text x="45" y="361" font-size="11" fill="#333" font-family="Arial">• <strong>ASBR (R4)</strong> injects EIGRP routes as Type 5 External LSAs. Route-tagging prevents mutual redistribution loops.</text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 1.1: CCNP Enterprise Multi-Area OSPF Architecture with Boundary Routers (ABR/ASBR)</em></p>
</div>'''

    elif mod_num == 2:
        # Campus Hierarchical Model (Core, Dist, Access)
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">Cisco 3-Tier Hierarchical Campus Switching Architecture</text>
  
  <!-- CORE LAYER -->
  <rect x="190" y="55" width="300" height="50" rx="6" fill="#8b0000"/>
  <text x="340" y="78" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold" font-family="Arial">CORE LAYER (High-Speed Packet Switching)</text>
  <text x="340" y="94" text-anchor="middle" fill="#ffcccc" font-size="11" font-family="Arial">No packet filtering • 40G/100G Links • Redundant Core-1 &amp; Core-2</text>

  <!-- DISTRIBUTION LAYER -->
  <rect x="70" y="150" width="240" height="55" rx="6" fill="#b22222"/>
  <text x="190" y="174" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">DISTRIBUTION SWITCH 1</text>
  <text x="190" y="191" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">Primary Root for VLANs 10, 20 • HSRP VIP</text>

  <rect x="370" y="150" width="240" height="55" rx="6" fill="#b22222"/>
  <text x="490" y="174" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">DISTRIBUTION SWITCH 2</text>
  <text x="490" y="191" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">Primary Root for VLANs 30, 40 • HSRP VIP</text>

  <!-- EtherChannel between Dist 1 and 2 -->
  <line x1="310" y1="177" x2="370" y2="177" stroke="#d4780a" stroke-width="4"/>
  <text x="340" y="172" text-anchor="middle" font-size="10" font-weight="bold" fill="#d4780a" font-family="Arial">LACP Trunk</text>

  <!-- Inter-tier lines -->
  <line x1="250" y1="105" x2="190" y2="150" stroke="#555" stroke-width="2"/>
  <line x1="430" y1="105" x2="490" y2="150" stroke="#555" stroke-width="2"/>
  <line x1="250" y1="105" x2="490" y2="150" stroke="#555" stroke-width="1" stroke-dasharray="3"/>
  <line x1="430" y1="105" x2="190" y2="150" stroke="#555" stroke-width="1" stroke-dasharray="3"/>

  <!-- ACCESS LAYER -->
  <rect x="50" y="260" width="160" height="45" rx="6" fill="#2a7ab5"/>
  <text x="130" y="281" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold" font-family="Arial">Access Switch A</text>
  <text x="130" y="295" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">PortFast + BPDU Guard</text>

  <rect x="260" y="260" width="160" height="45" rx="6" fill="#2a7ab5"/>
  <text x="340" y="281" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold" font-family="Arial">Access Switch B</text>
  <text x="340" y="295" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">802.1Q Trunks / Voice VLAN</text>

  <rect x="470" y="260" width="160" height="45" rx="6" fill="#2a7ab5"/>
  <text x="550" y="281" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold" font-family="Arial">Access Switch C</text>
  <text x="550" y="295" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">DHCP Snooping + DAI</text>

  <!-- Dist to Access lines -->
  <line x1="150" y1="205" x2="130" y2="260" stroke="#555" stroke-width="1.5"/>
  <line x1="230" y1="205" x2="340" y2="260" stroke="#555" stroke-width="1.5"/>
  <line x1="450" y1="205" x2="340" y2="260" stroke="#555" stroke-width="1.5"/>
  <line x1="530" y1="205" x2="550" y2="260" stroke="#555" stroke-width="1.5"/>

  <!-- Footer box -->
  <rect x="25" y="325" width="630" height="45" rx="6" fill="#ffffff" stroke="#ddd"/>
  <text x="45" y="344" font-size="11" fill="#333" font-family="Arial"><strong>Spanning Tree Tuning:</strong> Rapid PVST+ with root bridges deterministically placed at Distribution Layer.</text>
  <text x="45" y="359" font-size="11" fill="#333" font-family="Arial"><strong>Port Security:</strong> Edge ports configured with <code>spanning-tree portfast bpduguard enable</code> to block rogue switches.</text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 2.1: Campus Hierarchical Design with Layer 2/3 Boundary and Spanning Tree Root Placement</em></p>
</div>'''

    elif mod_num == 3:
        # MPLS & SD-WAN
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">MPLS Label-Switched Path (LSP) &amp; SD-WAN Overlay Architecture</text>

  <!-- Customer Edge Ingress -->
  <rect x="25" y="70" width="110" height="60" rx="6" fill="#2a7ab5"/>
  <text x="80" y="96" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">Customer Edge</text>
  <text x="80" y="113" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">CE-1 (IP Packet)</text>

  <!-- Provider Edge Ingress (LER) -->
  <rect x="175" y="70" width="130" height="60" rx="6" fill="#b22222"/>
  <text x="240" y="94" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">Ingress LER (PE-1)</text>
  <text x="240" y="111" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">PUSH Label: 1042</text>

  <!-- Provider Core Router (LSR) -->
  <rect x="345" y="70" width="120" height="60" rx="6" fill="#8b0000"/>
  <text x="405" y="94" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">Provider (P-1)</text>
  <text x="405" y="111" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">SWAP: 1042 → 2088</text>

  <!-- Provider Edge Egress (LER) -->
  <rect x="505" y="70" width="130" height="60" rx="6" fill="#b22222"/>
  <text x="570" y="94" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold" font-family="Arial">Egress LER (PE-2)</text>
  <text x="570" y="111" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">POP Label / PHP</text>

  <!-- Connecting arrows -->
  <line x1="135" y1="100" x2="175" y2="100" stroke="#333" stroke-width="3"/>
  <line x1="305" y1="100" x2="345" y2="100" stroke="#8b0000" stroke-width="3"/>
  <line x1="465" y1="100" x2="505" y2="100" stroke="#8b0000" stroke-width="3"/>

  <!-- SD-WAN Overlay Plane below -->
  <rect x="25" y="165" width="630" height="120" rx="8" fill="#f0f7fc" stroke="#2a7ab5" stroke-width="2"/>
  <text x="45" y="190" font-size="13" font-weight="bold" fill="#1a5a8a" font-family="Arial">Cisco SD-WAN Architecture Planes:</text>
  
  <rect x="45" y="205" width="130" height="65" rx="5" fill="#2a7ab5"/>
  <text x="110" y="230" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">vManage</text>
  <text x="110" y="246" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">Management Plane</text>
  <text x="110" y="260" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">GUI, Policies, APIs</text>

  <rect x="195" y="205" width="130" height="65" rx="5" fill="#d4780a"/>
  <text x="260" y="230" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">vSmart</text>
  <text x="260" y="246" text-anchor="middle" fill="#fff3d9" font-size="10" font-family="Arial">Control Plane</text>
  <text x="260" y="260" text-anchor="middle" fill="#fff3d9" font-size="9" font-family="Arial">OMP Protocol, Routes</text>

  <rect x="345" y="205" width="130" height="65" rx="5" fill="#b22222"/>
  <text x="410" y="230" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">vBond</text>
  <text x="410" y="246" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">Orchestration Plane</text>
  <text x="410" y="260" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">NAT Traversal, ZTP</text>

  <rect x="495" y="205" width="145" height="65" rx="5" fill="#1a5a8a"/>
  <text x="567" y="230" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">vEdge / cEdge</text>
  <text x="567" y="246" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">Data Plane</text>
  <text x="567" y="260" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">IPsec Overlay Tunnels</text>

  <!-- Bottom details -->
  <rect x="25" y="300" width="630" height="65" rx="6" fill="#ffffff" stroke="#ddd"/>
  <text x="45" y="322" font-size="11" fill="#333" font-family="Arial"><strong>MPLS 32-bit Header:</strong> 20-bit Label | 3-bit Traffic Class (QoS) | 1-bit Bottom-of-Stack (S) | 8-bit TTL</text>
  <text x="45" y="339" font-size="11" fill="#333" font-family="Arial"><strong>PHP (Penultimate Hop Popping):</strong> The router before the egress PE pops the label to prevent double-lookup.</text>
  <text x="45" y="355" font-size="11" fill="#333" font-family="Arial"><strong>SD-WAN Overlay:</strong> Encapsulates client traffic in dynamic IPsec tunnels over MPLS, broadband, and 5G.</text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 3.1: MPLS Label Switching Operations and Cisco SD-WAN Multi-Plane Architecture</em></p>
</div>'''

    elif mod_num == 4:
        # Enterprise Security & Hardening
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">Enterprise Defense-in-Depth &amp; Layer 2 Hardening Architecture</text>

  <!-- 802.1X Flow -->
  <rect x="30" y="60" width="620" height="95" rx="8" fill="#fff9f5" stroke="#d4780a" stroke-width="2"/>
  <text x="50" y="85" font-size="13" font-weight="bold" fill="#884400" font-family="Arial">IEEE 802.1X Port-Based Network Access Control (PNAC)</text>
  
  <rect x="50" y="98" width="130" height="42" rx="5" fill="#2a7ab5"/>
  <text x="115" y="118" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">Supplicant</text>
  <text x="115" y="132" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">Client PC / EAPoL</text>

  <line x1="180" y1="119" x2="270" y2="119" stroke="#555" stroke-width="2"/>
  <text x="225" y="113" text-anchor="middle" font-size="9" fill="#555" font-family="Arial">EAPoL</text>

  <rect x="270" y="98" width="150" height="42" rx="5" fill="#b22222"/>
  <text x="345" y="118" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">Authenticator (Switch)</text>
  <text x="345" y="132" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">Blocks Unauthorized Port</text>

  <line x1="420" y1="119" x2="500" y2="119" stroke="#555" stroke-width="2"/>
  <text x="460" y="113" text-anchor="middle" font-size="9" fill="#555" font-family="Arial">RADIUS</text>

  <rect x="500" y="98" width="135" height="42" rx="5" fill="#8b0000"/>
  <text x="567" y="118" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">Auth Server (ISE)</text>
  <text x="567" y="132" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">Validates Credentials</text>

  <!-- 4 Pillars of L2 Security -->
  <rect x="30" y="170" width="140" height="100" rx="6" fill="#ffffff" stroke="#b22222" stroke-width="2"/>
  <text x="100" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#b22222" font-family="Arial">DHCP Snooping</text>
  <text x="100" y="215" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Blocks rogue servers</text>
  <text x="100" y="230" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Builds binding table</text>
  <text x="100" y="250" text-anchor="middle" font-size="9" fill="#666" font-family="Arial">Trust vs Untrusted ports</text>

  <rect x="190" y="170" width="140" height="100" rx="6" fill="#ffffff" stroke="#2a7ab5" stroke-width="2"/>
  <text x="260" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#2a7ab5" font-family="Arial">Dynamic ARP (DAI)</text>
  <text x="260" y="215" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Stops ARP poisoning</text>
  <text x="260" y="230" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Validates MAC/IP pairs</text>
  <text x="260" y="250" text-anchor="middle" font-size="9" fill="#666" font-family="Arial">Uses DHCP Snoop DB</text>

  <rect x="350" y="170" width="140" height="100" rx="6" fill="#ffffff" stroke="#d4780a" stroke-width="2"/>
  <text x="420" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#d4780a" font-family="Arial">IP Source Guard</text>
  <text x="420" y="215" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Prevents IP spoofing</text>
  <text x="420" y="230" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Installs port ACLs</text>
  <text x="420" y="250" text-anchor="middle" font-size="9" fill="#666" font-family="Arial">Requires DHCP Snoop</text>

  <rect x="510" y="170" width="140" height="100" rx="6" fill="#ffffff" stroke="#1a5a8a" stroke-width="2"/>
  <text x="580" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a5a8a" font-family="Arial">CoPP &amp; Control Plane</text>
  <text x="580" y="215" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Protects router CPU</text>
  <text x="580" y="230" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">Rate-limits BGP/OSPF</text>
  <text x="580" y="250" text-anchor="middle" font-size="9" fill="#666" font-family="Arial">Prevents DoS on CPU</text>

  <!-- Footer box -->
  <rect x="30" y="285" width="620" height="80" rx="6" fill="#ffffff" stroke="#ddd"/>
  <text x="50" y="307" font-size="11" font-weight="bold" fill="#8b0000" font-family="Arial">Enterprise Implementation Strategy:</text>
  <text x="50" y="324" font-size="11" fill="#333" font-family="Arial">1. Always enable <strong>DHCP Snooping</strong> first. It is the foundation for both Dynamic ARP Inspection and IP Source Guard.</text>
  <text x="50" y="340" font-size="11" fill="#333" font-family="Arial">2. Restrict management traffic to an out-of-band (OOB) VRF using SSHv2 and TACACS+ AAA authentication.</text>
  <text x="50" y="356" font-size="11" fill="#333" font-family="Arial">3. Implement <strong>Control Plane Policing (CoPP)</strong> to safeguard route engine processors against volumetric transit floods.</text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 4.1: Multi-Layer Enterprise Security Architecture — Port Authentication &amp; Layer 2 Threat Defense</em></p>
</div>'''

    elif mod_num == 5:
        # QoS & High Availability
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">Quality of Service (QoS) &amp; High Availability (HSRP/VRRP) Pipeline</text>

  <!-- HSRP Section -->
  <rect x="25" y="55" width="630" height="110" rx="8" fill="#f8fafd" stroke="#2a7ab5" stroke-width="2"/>
  <text x="45" y="78" font-size="13" font-weight="bold" fill="#1a5a8a" font-family="Arial">First Hop Redundancy (HSRP / VRRP Virtual IP Gateway)</text>
  
  <rect x="50" y="90" width="160" height="60" rx="5" fill="#2a7ab5"/>
  <text x="130" y="113" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Router 1 (ACTIVE)</text>
  <text x="130" y="129" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">Priority: 110 (Preempt)</text>
  <text x="130" y="142" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">Physical IP: 10.1.1.2</text>

  <rect x="255" y="95" width="170" height="50" rx="6" fill="#8b0000"/>
  <text x="340" y="118" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Virtual Gateway (VIP)</text>
  <text x="340" y="133" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">IP: 10.1.1.1 | VMAC</text>

  <rect x="470" y="90" width="165" height="60" rx="5" fill="#d4780a"/>
  <text x="552" y="113" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Router 2 (STANDBY)</text>
  <text x="552" y="129" text-anchor="middle" fill="#fff3d9" font-size="10" font-family="Arial">Priority: 100 (Default)</text>
  <text x="552" y="142" text-anchor="middle" fill="#fff3d9" font-size="9" font-family="Arial">Physical IP: 10.1.1.3</text>

  <!-- QoS 3-Stage Pipeline -->
  <rect x="25" y="180" width="630" height="110" rx="8" fill="#fffdfa" stroke="#d4780a" stroke-width="2"/>
  <text x="45" y="203" font-size="13" font-weight="bold" fill="#884400" font-family="Arial">QoS MQC 3-Stage Processing Pipeline (Modular QoS CLI)</text>

  <rect x="45" y="215" width="180" height="60" rx="5" fill="#b22222"/>
  <text x="135" y="238" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">1. Classification &amp; Marking</text>
  <text x="135" y="253" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">DSCP EF (46) = Voice</text>
  <text x="135" y="267" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">DSCP AF41/31 = Video/Data</text>

  <rect x="250" y="215" width="180" height="60" rx="5" fill="#d4780a"/>
  <text x="340" y="238" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">2. Queuing &amp; Policing</text>
  <text x="340" y="253" text-anchor="middle" fill="#fff3d9" font-size="10" font-family="Arial">LLQ (Priority Queue)</text>
  <text x="340" y="267" text-anchor="middle" fill="#fff3d9" font-size="9" font-family="Arial">CBWFQ for Data Streams</text>

  <rect x="455" y="215" width="180" height="60" rx="5" fill="#2a7ab5"/>
  <text x="545" y="238" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">3. Scheduling &amp; Shaping</text>
  <text x="545" y="253" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">WRED (Avoid Congestion)</text>
  <text x="545" y="267" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">Traffic Shaping to Rate</text>

  <!-- Automation snippet -->
  <rect x="25" y="305" width="630" height="65" rx="6" fill="#ffffff" stroke="#ddd"/>
  <text x="45" y="325" font-size="11" fill="#333" font-family="Arial"><strong>Model-Driven Programmability:</strong> YANG Data Models + NETCONF (Port 830 XML) / RESTCONF (Port 443 JSON).</text>
  <text x="45" y="342" font-size="11" fill="#333" font-family="Arial"><strong>Python Automation:</strong> Use <code>netmiko</code> for CLI scraping and <code>requests</code> / <code>ncclient</code> for structured API interactions.</text>
  <text x="45" y="358" font-size="11" fill="#333" font-family="Arial"><strong>HSRP Tracking:</strong> Configure <code>track interface</code> on R1 to decrement priority upon WAN failure and trigger failover.</text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 5.1: High Availability Gateway Failover and MQC Quality of Service Pipeline</em></p>
</div>'''

    elif mod_num == 6:
        # Cloud Networking & Hybrid Architecture
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">Enterprise Hybrid Cloud Networking &amp; Transit Gateway Architecture</text>

  <!-- On-Premises Data Center -->
  <rect x="25" y="60" width="185" height="225" rx="8" fill="#f4f6f8" stroke="#555" stroke-width="2"/>
  <text x="117" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50" font-family="Arial">On-Premises Data Center</text>
  <text x="117" y="103" text-anchor="middle" font-size="10" fill="#7f8c8d" font-family="Arial">Corporate ASN: 65000</text>

  <rect x="45" y="125" width="145" height="45" rx="5" fill="#2a7ab5"/>
  <text x="117" y="147" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">Core Enterprise Router</text>
  <text x="117" y="161" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">BGP eBGP Peering</text>

  <rect x="45" y="195" width="145" height="45" rx="5" fill="#1a5a8a"/>
  <text x="117" y="217" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">Internal Workloads</text>
  <text x="117" y="231" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">Subnets: 10.10.0.0/16</text>

  <!-- WAN Interconnects -->
  <line x1="190" y1="140" x2="310" y2="140" stroke="#8b0000" stroke-width="4"/>
  <text x="250" y="133" text-anchor="middle" font-size="10" font-weight="bold" fill="#8b0000" font-family="Arial">Direct Connect (10G)</text>

  <line x1="190" y1="165" x2="310" y2="165" stroke="#d4780a" stroke-width="2" stroke-dasharray="4"/>
  <text x="250" y="180" text-anchor="middle" font-size="10" font-weight="bold" fill="#d4780a" font-family="Arial">Backup IPsec VPN</text>

  <!-- Cloud Transit Hub -->
  <rect x="310" y="60" width="150" height="225" rx="8" fill="#fff5f5" stroke="#8b0000" stroke-width="2"/>
  <text x="385" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="#8b0000" font-family="Arial">Cloud Transit Hub</text>
  <text x="385" y="103" text-anchor="middle" font-size="10" fill="#777" font-family="Arial">Transit Gateway (TGW)</text>

  <rect x="325" y="130" width="120" height="60" rx="5" fill="#8b0000"/>
  <text x="385" y="153" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold" font-family="Arial">AWS TGW / vWAN</text>
  <text x="385" y="169" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">Cloud ASN: 64512</text>
  <text x="385" y="181" text-anchor="middle" fill="#ffe0e0" font-size="8" font-family="Arial">Route Table Propagation</text>

  <!-- Spoke VPCs -->
  <rect x="490" y="60" width="165" height="105" rx="8" fill="#eef7fc" stroke="#2a7ab5" stroke-width="1.5"/>
  <text x="572" y="82" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a5a8a" font-family="Arial">Production VPC</text>
  <text x="572" y="97" text-anchor="middle" font-size="9" fill="#555" font-family="Arial">172.16.0.0/16 • Multi-AZ</text>
  <rect x="505" y="107" width="135" height="40" rx="4" fill="#2a7ab5"/>
  <text x="572" y="127" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold" font-family="Arial">App &amp; DB Subnets</text>
  <text x="572" y="140" text-anchor="middle" fill="#e0f0ff" font-size="8" font-family="Arial">Private Route Tables</text>

  <rect x="490" y="180" width="165" height="105" rx="8" fill="#fef8e7" stroke="#d4780a" stroke-width="1.5"/>
  <text x="572" y="202" text-anchor="middle" font-size="11" font-weight="bold" fill="#995000" font-family="Arial">Shared Services VPC</text>
  <text x="572" y="217" text-anchor="middle" font-size="9" fill="#555" font-family="Arial">172.20.0.0/16 • Inspection</text>
  <rect x="505" y="227" width="135" height="40" rx="4" fill="#d4780a"/>
  <text x="572" y="247" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold" font-family="Arial">Firewall / DNS Proxy</text>
  <text x="572" y="260" text-anchor="middle" fill="#fff3d9" font-size="8" font-family="Arial">Egress NAT Gateway</text>

  <!-- TGW Attachments -->
  <line x1="445" y1="150" x2="490" y2="115" stroke="#333" stroke-width="2"/>
  <line x1="445" y1="170" x2="490" y2="230" stroke="#333" stroke-width="2"/>

  <!-- Footer box -->
  <rect x="25" y="300" width="630" height="65" rx="6" fill="#ffffff" stroke="#ddd"/>
  <text x="45" y="322" font-size="11" fill="#333" font-family="Arial"><strong>Transit Gateway (TGW) Hub-and-Spoke:</strong> Replaces N×(N-1)/2 complex VPC peering meshes with centralized routing.</text>
  <text x="45" y="339" font-size="11" fill="#333" font-family="Arial"><strong>BGP Over Direct Connect:</strong> Dynamic BGP route exchange advertises enterprise prefixes to cloud and propagates VPC CIDRs.</text>
  <text x="45" y="355" font-size="11" fill="#333" font-family="Arial"><strong>Security Groups vs NACLs:</strong> Security Groups are stateful (instance level); Network ACLs are stateless (subnet level).</text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 6.1: Enterprise Hybrid Cloud Architecture with AWS Transit Gateway and Dedicated WAN Interconnect</em></p>
</div>'''

    elif mod_num == 7:
        # Troubleshooting & Capstone Methodology
        return '''<div style="text-align:center;margin:28px 0;">
<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #dcdcdc;border-radius:10px;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <rect width="680" height="380" fill="#fafbfc"/>
  <rect x="0" y="0" width="680" height="42" fill="#8b0000"/>
  <text x="340" y="27" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff" font-family="Arial, sans-serif">CCNP Enterprise Systematic Network Troubleshooting Methodology</text>

  <!-- Step 1 -->
  <rect x="40" y="65" width="170" height="75" rx="6" fill="#2a7ab5"/>
  <text x="125" y="90" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Step 1: Define Problem</text>
  <text x="125" y="107" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">Scope, Impact, Symptoms</text>
  <text x="125" y="122" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">Talk to users, check alerts</text>

  <line x1="210" y1="102" x2="255" y2="102" stroke="#555" stroke-width="3" marker-end="url(#arr)"/>

  <!-- Step 2 -->
  <rect x="255" y="65" width="170" height="75" rx="6" fill="#b22222"/>
  <text x="340" y="90" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Step 2: Gather Facts</text>
  <text x="340" y="107" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">show ip route / show lldp</text>
  <text x="340" y="122" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">Isolate Layer 1 through 7</text>

  <line x1="425" y1="102" x2="470" y2="102" stroke="#555" stroke-width="3"/>

  <!-- Step 3 -->
  <rect x="470" y="65" width="170" height="75" rx="6" fill="#8b0000"/>
  <text x="555" y="90" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Step 3: Analyze &amp; Hypothesize</text>
  <text x="555" y="107" text-anchor="middle" fill="#ffe0e0" font-size="10" font-family="Arial">Identify Root Cause</text>
  <text x="555" y="122" text-anchor="middle" fill="#ffe0e0" font-size="9" font-family="Arial">Eliminate possibilities</text>

  <line x1="555" y1="140" x2="555" y2="175" stroke="#555" stroke-width="3"/>

  <!-- Step 4 -->
  <rect x="470" y="175" width="170" height="75" rx="6" fill="#d4780a"/>
  <text x="555" y="200" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Step 4: Action Plan</text>
  <text x="555" y="217" text-anchor="middle" fill="#fff3d9" font-size="10" font-family="Arial">Design Change &amp; Rollback</text>
  <text x="555" y="232" text-anchor="middle" fill="#fff3d9" font-size="9" font-family="Arial">Assess collateral risk</text>

  <line x1="470" y1="212" x2="425" y2="212" stroke="#555" stroke-width="3"/>

  <!-- Step 5 -->
  <rect x="255" y="175" width="170" height="75" rx="6" fill="#1a5a8a"/>
  <text x="340" y="200" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Step 5: Test &amp; Verify</text>
  <text x="340" y="217" text-anchor="middle" fill="#e0f0ff" font-size="10" font-family="Arial">Execute change in change window</text>
  <text x="340" y="232" text-anchor="middle" fill="#e0f0ff" font-size="9" font-family="Arial">Verify end-to-end telemetry</text>

  <line x1="255" y1="212" x2="210" y2="212" stroke="#555" stroke-width="3"/>

  <!-- Step 6 -->
  <rect x="40" y="175" width="170" height="75" rx="6" fill="#2e7d32"/>
  <text x="125" y="200" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold" font-family="Arial">Step 6: Document &amp; Root-Cause</text>
  <text x="125" y="217" text-anchor="middle" fill="#e8f5e9" font-size="10" font-family="Arial">Update Network Topology Maps</text>
  <text x="125" y="232" text-anchor="middle" fill="#e8f5e9" font-size="9" font-family="Arial">Post-mortem review</text>

  <!-- Footer box -->
  <rect x="40" y="275" width="600" height="85" rx="6" fill="#ffffff" stroke="#ddd"/>
  <text x="60" y="297" font-size="11" font-weight="bold" fill="#8b0000" font-family="Arial">Critical Command Toolkit for Capstone Lab:</text>
  <text x="60" y="315" font-size="11" fill="#333" font-family="Arial">• <strong>OSPF / Routing:</strong> <code>show ip ospf neighbor</code> | <code>show ip route ospf</code> | <code>show ip ospf database</code></text>
  <text x="60" y="331" font-size="11" fill="#333" font-family="Arial">• <strong>Switching / Trunks:</strong> <code>show interfaces trunk</code> | <code>show spanning-tree root</code> | <code>show etherchannel summary</code></text>
  <text x="60" y="347" font-size="11" fill="#333" font-family="Arial">• <strong>Security &amp; Gateways:</strong> <code>show standby brief</code> | <code>show ip dhcp snooping binding</code> | <code>show ip arp inspection</code></text>
</svg>
<p style="font-size:12px;color:#666;margin-top:6px;"><em>Figure 7.1: Structured Diagnostic Methodology &amp; Command Verification Sequence for Network Engineers</em></p>
</div>'''

    return ""


# ─── RICH READING GUIDE BUILDER ──────────────────────────────────────────────
def build_rich_reading_guide(mod_num: int, title: str, md_content: str) -> str:
    body = md2html(md_content)
    diagram = get_csc6361_diagram(mod_num)

    return f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<!-- BRANDED HEADER BANNER -->
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">🎓 Texas Wesleyan University · Department of Computer Science &amp; IT · CSC-6361 Advanced Computer Networks</p>
</div>

<!-- LEARNING OBJECTIVES CALLOUT -->
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 GRADUATE &amp; CCNP ENTERPRISE LEARNING OBJECTIVES</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13.5px;line-height:1.6;">After completing this module reading guide and the accompanying hands-on lab, you will be able to analyze enterprise protocol behaviors, evaluate architectural design trade-offs, and implement production-ready configurations matching Cisco CCNP Enterprise standards.</p>
</div>

<!-- CUSTOM ARCHITECTURE DIAGRAM -->
{diagram}

<!-- MAIN READING CONTENT -->
<div style="background:white;padding:10px 0;line-height:1.8;color:#2c3e50;font-size:15px;">
{body}
</div>

<!-- STUDY & LAB SUCCESS TIP BOX -->
<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 PROFESSOR NASH'S LAB &amp; QUIZ SUCCESS STRATEGY</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13.5px;line-height:1.6;">Before attempting the quiz or submitting your lab report, verify each routing table entry using the diagnostic commands shown above. In your written lab report, do not simply provide raw terminal output — explain <em>why</em> each command proves the design requirements have been met.</p>
</div>

<!-- KEY TERMS & STANDARDS BOX -->
<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 STANDARDS &amp; PROTOCOL SPECIFICATIONS TO CITE</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13.5px;line-height:1.6;">For your weekly graduate discussion post, you are required to cite at least one external credible source (IETF RFC, IEEE standard, or official Cisco configuration guide). Scan this guide for protocol numbers and standard RFC references to incorporate into your analysis.</p>
</div>

<!-- CAREER CONNECTION -->
<div style="background:#fce4ec;border-left:5px solid #e91e63;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#880e4f;">🏆 INDUSTRY CERTIFICATION &amp; SENIOR ARCHITECT CAREER IMPACT</p>
  <p style="margin:6px 0 0;color:#880e4f;font-size:13.5px;line-height:1.6;">The topics in this module map directly to the <strong>Cisco CCNP Enterprise Core (350-401 ENCOR)</strong> examination blueprint and senior infrastructure engineering interviews. Developing mastery of these protocols positions you for roles such as Senior Network Architect, Cloud Infrastructure Engineer, and Principal Systems Integrator.</p>
</div>

</div>'''

print("CSC-6361 builder library loaded successfully.")

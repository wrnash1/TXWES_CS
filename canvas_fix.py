# -*- coding: utf-8 -*-
"""
TXWES Canvas Live Course Fixer
Fixes live courses on txwes.instructure.com:
  1. Pushes quiz questions from local Markdown to Canvas
  2. Expands and publishes reading guide pages with rich content + SVG diagrams
  3. Verifies/fixes discussions

Usage:
  python3 canvas_fix.py
"""

import os, re, json, time, sys, urllib.request, urllib.parse, urllib.error
from pathlib import Path

# ─── CONFIG ───────────────────────────────────────────────────────────────────
CANVAS_URL   = "https://txwes.instructure.com"
TOKEN        = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
BASE_DIR     = Path(__file__).parent

COURSES = [
    {
        'id':       13089,
        'code':     'CIS-3321',
        'name':     'Network Administration',
        'dir':      'CIS-3321_Network_Admin',
        'quiz_ids': {
            1:  75363, 2:  75364, 3:  75365, 4:  75366,
            5:  75367, 6:  75368, 7:  75369, 8:  75370,
            9:  75371, 10: 75372, 11: 75373, 12: 75374,
            13: 75375, 14: 75376, 15: 75377, 16: 75378,
        },
    },
    {
        'id':       13090,
        'code':     'CIS-4328',
        'name':     'Fund Informa Systems Security',
        'dir':      'CIS-4328_Information_Security',
        'quiz_ids': {
            1:  75380, 2:  75381, 3:  75382, 4:  75383,
            5:  75384, 6:  75385, 7:  75386, 8:  75387,
            9:  75388, 10: 75389, 11: 75390, 12: 75391,
            13: 75392, 14: 75393, 15: 75394, 16: 75395,
        },
    },
]

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

# ─── HTTP HELPERS ─────────────────────────────────────────────────────────────
def api_get(path: str) -> dict | list:
    url = f"{CANVAS_URL}/api/v1{path}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"    [GET ERROR] {path}: {e.code} {e.read()[:200]}")
        return {}

def api_post(path: str, data: dict) -> dict:
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode()
    req  = urllib.request.Request(url, data=body, headers=HEADERS, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body_err = e.read()[:300]
        print(f"    [POST ERROR] {path}: {e.code} {body_err}")
        return {}

def api_put(path: str, data: dict) -> dict:
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode()
    req  = urllib.request.Request(url, data=body, headers=HEADERS, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"    [PUT ERROR] {path}: {e.code} {e.read()[:300]}")
        return {}

def api_delete(path: str) -> bool:
    url = f"{CANVAS_URL}/api/v1{path}"
    req = urllib.request.Request(url, headers=HEADERS, method='DELETE')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True
    except urllib.error.HTTPError as e:
        print(f"    [DELETE ERROR] {path}: {e.code}")
        return False

# ─── MARKDOWN PARSER ──────────────────────────────────────────────────────────
def md2html(text: str) -> str:
    if not text:
        return ""
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    code_blocks = []
    def _store_code(m):
        lang = m.group(1) or ""
        code = m.group(2)
        # Escape HTML entities
        code_esc = code.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        idx = len(code_blocks)
        lang_cls = f' class="language-{lang}"' if lang else ''
        code_blocks.append(f'<pre style="background:#1e1e1e;color:#d4d4d4;padding:16px;border-radius:6px;overflow-x:auto;font-family:monospace;font-size:14px;line-height:1.5;"><code{lang_cls}>{code_esc}</code></pre>')
        return f'__CODE_{idx}__'

    text = re.sub(r'```(\w*)\n(.*?)```', _store_code, text, flags=re.DOTALL)

    def _inline(s):
        s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'__(.+?)__', r'<strong>\1</strong>', s)
        s = re.sub(r'\*([^*\n]+?)\*', r'<em>\1</em>', s)
        s = re.sub(r'_([^_\n]+?)_', r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+?)`', r'<code style="background:#f0f0f0;padding:2px 6px;border-radius:3px;font-family:monospace;">\1</code>', s)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', s)
        return s

    lines = text.split('\n')
    out = []
    in_list = None
    in_bq    = False
    in_table = False
    t_headers = []
    t_rows    = []

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
                    rows_html += f'<th style="padding:10px;background:#8b0000;color:#fff;text-align:left;">{_inline(h.strip())}</th>'
                rows_html += '</tr></thead>'
            if t_rows:
                rows_html += '<tbody>'
                for i,row in enumerate(t_rows):
                    bg = '#fff' if i%2==0 else '#f9f9f9'
                    rows_html += f'<tr style="background:{bg};">'
                    for td in row:
                        rows_html += f'<td style="padding:8px;border:1px solid #ddd;">{_inline(td.strip())}</td>'
                    rows_html += '</tr>'
                rows_html += '</tbody>'
            out.append(f'<table style="border-collapse:collapse;width:100%;margin:16px 0;">{rows_html}</table>')
            in_table = False
            t_headers.clear()
            t_rows.clear()

    for line in lines:
        raw = line.strip()

        if raw.startswith('__CODE_') and raw.endswith('__'):
            flush_list(); flush_bq(); flush_table()
            idx = int(raw[7:-2])
            out.append(code_blocks[idx])
            continue

        if re.match(r'^(-{3,}|\*{3,}|_{3,})\s*$', raw):
            flush_list(); flush_bq(); flush_table()
            out.append('<hr style="border:none;border-top:2px solid #8b0000;margin:24px 0;">')
            continue

        hm = re.match(r'^(#{1,6})\s+(.+)$', raw)
        if hm:
            flush_list(); flush_bq(); flush_table()
            lvl = len(hm.group(1))
            sizes = {1:'28px',2:'22px',3:'18px',4:'16px',5:'14px',6:'13px'}
            color = '#8b0000' if lvl <= 3 else '#333'
            margin = '24px 0 12px' if lvl == 1 else '20px 0 8px'
            out.append(f'<h{lvl} style="font-size:{sizes[lvl]};color:{color};margin:{margin};font-weight:bold;border-bottom:{"2px solid #b22222" if lvl==2 else "none"};padding-bottom:{"6px" if lvl==2 else "0"};">{_inline(hm.group(2))}</h{lvl}>')
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
                out.append('<blockquote style="border-left:4px solid #b22222;margin:16px 0;padding:12px 16px;background:#fff8f8;color:#555;">')
                in_bq = True
            out.append(f'<p style="margin:4px 0;">{bq_text}</p>')
            continue
        else:
            flush_bq()

        ul_m = re.match(r'^[-*+]\s+(.+)$', raw)
        if ul_m:
            flush_bq(); flush_table()
            if in_list != 'ul':
                flush_list()
                out.append('<ul style="margin:8px 0;padding-left:24px;">')
                in_list = 'ul'
            out.append(f'<li style="margin:4px 0;">{_inline(ul_m.group(1))}</li>')
            continue

        ol_m = re.match(r'^\d+\.\s+(.+)$', raw)
        if ol_m:
            flush_bq(); flush_table()
            if in_list != 'ol':
                flush_list()
                out.append('<ol style="margin:8px 0;padding-left:24px;">')
                in_list = 'ol'
            out.append(f'<li style="margin:4px 0;">{_inline(ol_m.group(1))}</li>')
            continue

        if not raw:
            flush_list(); flush_bq(); flush_table()
            continue

        flush_list(); flush_bq(); flush_table()
        out.append(f'<p style="margin:8px 0;line-height:1.7;">{_inline(raw)}</p>')

    flush_list(); flush_bq(); flush_table()
    return '\n'.join(out)


# ─── QUIZ PARSER ─────────────────────────────────────────────────────────────
def parse_quiz(md_text: str) -> list:
    questions = []
    QUESTION_SPLIT = re.compile(
        r'(\n(?:#{2,3}\s+Question\s*\d+|####\s+Q\d+(?=\n)|\*\*Question\s+\d+[^*\n]*\*\*)[^\n]*\n)',
        re.IGNORECASE
    )
    parts = QUESTION_SPLIT.split(md_text)
    pairs = []
    i = 1
    while i + 1 < len(parts):
        pairs.append((parts[i], parts[i+1]))
        i += 2

    for header, block in pairs:
        header_answer = None
        ha = re.search(r'Answer\s*:\s*([A-D])', header, re.IGNORECASE)
        if ha:
            header_answer = ha.group(1).upper()

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
            label = m.group(1).upper()
            text  = re.sub(r'\n+', ' ', m.group(2).strip())
            text  = re.sub(r'\*\*', '', text).strip()
            text  = re.split(r'\s+—\s+|\s*---\s*', text)[0].strip()
            text  = re.split(r'\*?Correct\s+Answer', text, flags=re.I)[0].strip()
            options[label] = text

        if len(options) < 2:
            continue

        if header_answer and header_answer in options:
            correct = header_answer
        else:
            ca = re.search(r'(?:Correct\s+)?Answer[:\s*\d]*[:\s*]+\**\s*([A-D])', block, re.IGNORECASE)
            if not ca:
                continue
            correct = ca.group(1).upper()
            if correct not in options:
                continue

        questions.append({'stem': stem, 'options': options, 'correct': correct})

    return questions


# ─── RICH CONTENT WRAPPER ─────────────────────────────────────────────────────
# SVG diagram library: returns topic-appropriate diagrams
def get_topic_svg(title: str) -> str:
    """Return an inline SVG diagram relevant to the topic."""
    t = title.lower()

    # OSI / Networking Fundamentals
    if any(k in t for k in ['osi', 'network fundamental', 'networking fund']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="420" viewBox="0 0 560 420" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="420" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">OSI Model — 7 Layers</text>
  <!-- Layers -->
  <g font-family="Arial" font-size="13">
    <rect x="40" y="45" width="200" height="40" rx="6" fill="#b22222"/><text x="140" y="70" text-anchor="middle" fill="white" font-weight="bold">Layer 7 — Application</text>
    <rect x="40" y="95" width="200" height="40" rx="6" fill="#cc3333"/><text x="140" y="120" text-anchor="middle" fill="white" font-weight="bold">Layer 6 — Presentation</text>
    <rect x="40" y="145" width="200" height="40" rx="6" fill="#dd4444"/><text x="140" y="170" text-anchor="middle" fill="white" font-weight="bold">Layer 5 — Session</text>
    <rect x="40" y="195" width="200" height="40" rx="6" fill="#e85c1a"/><text x="140" y="220" text-anchor="middle" fill="white" font-weight="bold">Layer 4 — Transport</text>
    <rect x="40" y="245" width="200" height="40" rx="6" fill="#d4780a"/><text x="140" y="270" text-anchor="middle" fill="white" font-weight="bold">Layer 3 — Network</text>
    <rect x="40" y="295" width="200" height="40" rx="6" fill="#2a7ab5"/><text x="140" y="320" text-anchor="middle" fill="white" font-weight="bold">Layer 2 — Data Link</text>
    <rect x="40" y="345" width="200" height="40" rx="6" fill="#1a5a8a"/><text x="140" y="370" text-anchor="middle" fill="white" font-weight="bold">Layer 1 — Physical</text>
    <!-- Examples -->
    <text x="270" y="72" fill="#333">HTTP, FTP, DNS, SMTP</text>
    <text x="270" y="122" fill="#333">SSL/TLS, JPEG, ASCII</text>
    <text x="270" y="172" fill="#333">NetBIOS, SQL sessions</text>
    <text x="270" y="222" fill="#333">TCP (reliable) / UDP (fast)</text>
    <text x="270" y="272" fill="#333">IP Addressing, Routing</text>
    <text x="270" y="322" fill="#333">MAC Addresses, Ethernet</text>
    <text x="270" y="372" fill="#333">Cables, Hubs, Signals</text>
  </g>
  <!-- Arrow -->
  <line x1="250" y1="55" x2="250" y2="375" stroke="#999" stroke-width="1" stroke-dasharray="4"/>
  <text x="28" y="215" font-size="11" fill="#777" transform="rotate(-90,28,215)">DATA FLOW ▼</text>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: The OSI 7-Layer Reference Model</em></p>
</div>'''

    # TCP/IP
    elif any(k in t for k in ['tcp/ip', 'tcp ip', 'protocol', 'network protocol']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="520" height="340" viewBox="0 0 520 340" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="520" height="340" fill="#f8f9fa"/>
  <text x="260" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">TCP/IP vs OSI Model</text>
  <g font-family="Arial" font-size="13">
    <!-- TCP/IP -->
    <text x="110" y="55" text-anchor="middle" fill="#8b0000" font-weight="bold">TCP/IP Model</text>
    <rect x="20" y="65" width="180" height="45" rx="6" fill="#b22222"/><text x="110" y="93" text-anchor="middle" fill="white" font-weight="bold">Application</text>
    <rect x="20" y="118" width="180" height="45" rx="6" fill="#e85c1a"/><text x="110" y="146" text-anchor="middle" fill="white" font-weight="bold">Transport</text>
    <rect x="20" y="171" width="180" height="45" rx="6" fill="#d4780a"/><text x="110" y="199" text-anchor="middle" fill="white" font-weight="bold">Internet</text>
    <rect x="20" y="224" width="180" height="45" rx="6" fill="#2a7ab5"/><text x="110" y="252" text-anchor="middle" fill="white" font-weight="bold">Network Access</text>
    <!-- OSI -->
    <text x="400" y="55" text-anchor="middle" fill="#8b0000" font-weight="bold">OSI Model</text>
    <rect x="310" y="65" width="180" height="25" rx="4" fill="#b22222"/><text x="400" y="83" text-anchor="middle" fill="white" font-size="12">Application (7)</text>
    <rect x="310" y="95" width="180" height="25" rx="4" fill="#cc3333"/><text x="400" y="113" text-anchor="middle" fill="white" font-size="12">Presentation (6)</text>
    <rect x="310" y="125" width="180" height="25" rx="4" fill="#dd4444"/><text x="400" y="143" text-anchor="middle" fill="white" font-size="12">Session (5)</text>
    <rect x="310" y="160" width="180" height="45" rx="4" fill="#e85c1a"/><text x="400" y="188" text-anchor="middle" fill="white" font-size="12">Transport (4)</text>
    <rect x="310" y="210" width="180" height="45" rx="4" fill="#d4780a"/><text x="400" y="238" text-anchor="middle" fill="white" font-size="12">Network (3)</text>
    <rect x="310" y="260" width="180" height="25" rx="4" fill="#2a7ab5"/><text x="400" y="278" text-anchor="middle" fill="white" font-size="12">Data Link (2)</text>
    <rect x="310" y="288" width="180" height="25" rx="4" fill="#1a5a8a"/><text x="400" y="306" text-anchor="middle" fill="white" font-size="12">Physical (1)</text>
    <!-- connecting lines -->
    <line x1="200" y1="87" x2="310" y2="80" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
    <line x1="200" y1="87" x2="310" y2="107" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
    <line x1="200" y1="87" x2="310" y2="137" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
    <line x1="200" y1="140" x2="310" y2="180" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
    <line x1="200" y1="193" x2="310" y2="228" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
    <line x1="200" y1="246" x2="310" y2="270" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
    <line x1="200" y1="246" x2="310" y2="298" stroke="#ccc" stroke-dasharray="4" stroke-width="1"/>
  </g>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: TCP/IP 4-Layer Model mapped to the OSI 7-Layer Model</em></p>
</div>'''

    # IP Addressing / Subnetting
    elif any(k in t for k in ['ip address', 'subnet', 'cidr', 'ipv4']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="300" viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="300" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">IPv4 Address Structure &amp; Subnetting</text>
  <g font-family="monospace" font-size="14">
    <!-- IP Octets -->
    <rect x="30" y="50" width="100" height="45" rx="4" fill="#b22222"/><text x="80" y="78" text-anchor="middle" fill="white">192</text>
    <rect x="140" y="50" width="100" height="45" rx="4" fill="#b22222"/><text x="190" y="78" text-anchor="middle" fill="white">168</text>
    <rect x="250" y="50" width="100" height="45" rx="4" fill="#2a7ab5"/><text x="300" y="78" text-anchor="middle" fill="white">1</text>
    <rect x="360" y="50" width="100" height="45" rx="4" fill="#2a7ab5"/><text x="410" y="78" text-anchor="middle" fill="white">100</text>
    <text x="130" y="80" fill="#555" font-size="18" font-family="Arial">.</text>
    <text x="240" y="80" fill="#555" font-size="18" font-family="Arial">.</text>
    <text x="350" y="80" fill="#555" font-size="18" font-family="Arial">.</text>
    <text x="80" y="115" text-anchor="middle" fill="#b22222" font-family="Arial" font-size="11" font-weight="bold">Network</text>
    <text x="190" y="115" text-anchor="middle" fill="#b22222" font-family="Arial" font-size="11" font-weight="bold">Network</text>
    <text x="300" y="115" text-anchor="middle" fill="#2a7ab5" font-family="Arial" font-size="11" font-weight="bold">Subnet</text>
    <text x="410" y="115" text-anchor="middle" fill="#2a7ab5" font-family="Arial" font-size="11" font-weight="bold">Host</text>
  </g>
  <!-- CIDR table -->
  <g font-family="Arial" font-size="12">
    <text x="30" y="150" fill="#333" font-weight="bold">Common CIDR Notations:</text>
    <rect x="30" y="160" width="490" height="25" rx="3" fill="#b22222"/>
    <text x="80" y="177" fill="white" font-weight="bold">CIDR</text>
    <text x="180" y="177" fill="white" font-weight="bold">Subnet Mask</text>
    <text x="320" y="177" fill="white" font-weight="bold">Total Hosts</text>
    <text x="430" y="177" fill="white" font-weight="bold">Usable Hosts</text>
    <rect x="30" y="185" width="490" height="22" fill="#fff"/><text x="80" y="200" fill="#333">/24</text><text x="180" y="200" fill="#333">255.255.255.0</text><text x="320" y="200" fill="#333">256</text><text x="430" y="200" fill="#333">254</text>
    <rect x="30" y="207" width="490" height="22" fill="#f0f0f0"/><text x="80" y="222" fill="#333">/25</text><text x="180" y="222" fill="#333">255.255.255.128</text><text x="320" y="222" fill="#333">128</text><text x="430" y="222" fill="#333">126</text>
    <rect x="30" y="229" width="490" height="22" fill="#fff"/><text x="80" y="244" fill="#333">/26</text><text x="180" y="244" fill="#333">255.255.255.192</text><text x="320" y="244" fill="#333">64</text><text x="430" y="244" fill="#333">62</text>
    <rect x="30" y="251" width="490" height="22" fill="#f0f0f0"/><text x="80" y="266" fill="#333">/27</text><text x="180" y="266" fill="#333">255.255.255.224</text><text x="320" y="266" fill="#333">32</text><text x="430" y="266" fill="#333">30</text>
    <rect x="30" y="273" width="490" height="22" fill="#fff"/><text x="80" y="288" fill="#333">/30</text><text x="180" y="288" fill="#333">255.255.255.252</text><text x="320" y="288" fill="#333">4</text><text x="430" y="288" fill="#333">2</text>
  </g>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: IPv4 Address Structure and CIDR Subnetting Reference</em></p>
</div>'''

    # IPv6
    elif 'ipv6' in t:
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="280" viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="280" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">IPv6 Address Structure</text>
  <g font-family="Arial" font-size="13">
    <text x="30" y="60" fill="#333">Full IPv6: <tspan font-family="monospace" fill="#b22222">2001:0db8:85a3:0000:0000:8a2e:0370:7334</tspan></text>
    <text x="30" y="85" fill="#333">Compressed: <tspan font-family="monospace" fill="#2a7ab5">2001:db8:85a3::8a2e:370:7334</tspan></text>
    <!-- 8 groups visual -->
    <rect x="30" y="105" width="60" height="35" rx="4" fill="#b22222"/><text x="60" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">2001</text>
    <rect x="98" y="105" width="60" height="35" rx="4" fill="#b22222"/><text x="128" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">0db8</text>
    <rect x="166" y="105" width="60" height="35" rx="4" fill="#cc3333"/><text x="196" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">85a3</text>
    <rect x="234" y="105" width="60" height="35" rx="4" fill="#cc3333"/><text x="264" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">0000</text>
    <rect x="302" y="105" width="60" height="35" rx="4" fill="#2a7ab5"/><text x="332" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">0000</text>
    <rect x="370" y="105" width="60" height="35" rx="4" fill="#2a7ab5"/><text x="400" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">8a2e</text>
    <rect x="438" y="105" width="50" height="35" rx="4" fill="#1a5a8a"/><text x="463" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">0370</text>
    <rect x="496" y="105" width="50" height="35" rx="4" fill="#1a5a8a"/><text x="521" y="127" text-anchor="middle" fill="white" font-family="monospace" font-size="12">7334</text>
    <text x="60" y="158" text-anchor="middle" fill="#b22222" font-size="11">Global</text>
    <text x="128" y="158" text-anchor="middle" fill="#b22222" font-size="11">Prefix</text>
    <text x="196" y="158" text-anchor="middle" fill="#cc3333" font-size="11">Subnet</text>
    <text x="264" y="158" text-anchor="middle" fill="#cc3333" font-size="11">Subnet</text>
    <text x="332" y="158" text-anchor="middle" fill="#2a7ab5" font-size="11">Interface</text>
    <text x="400" y="158" text-anchor="middle" fill="#2a7ab5" font-size="11">Interface</text>
    <text x="463" y="158" text-anchor="middle" fill="#1a5a8a" font-size="11">Interface</text>
    <text x="521" y="158" text-anchor="middle" fill="#1a5a8a" font-size="11">Interface</text>
    <!-- IPv4 vs IPv6 comparison -->
    <text x="30" y="190" fill="#333" font-weight="bold" font-size="13">IPv4 vs IPv6 at a Glance:</text>
    <rect x="30" y="200" width="490" height="22" rx="3" fill="#b22222"/>
    <text x="100" y="215" fill="white" font-weight="bold">Feature</text><text x="300" y="215" fill="white" font-weight="bold">IPv4</text><text x="430" y="215" fill="white" font-weight="bold">IPv6</text>
    <rect x="30" y="222" width="490" height="20" fill="#fff"/><text x="100" y="236" fill="#333">Address Size</text><text x="300" y="236" fill="#333">32-bit</text><text x="430" y="236" fill="#333">128-bit</text>
    <rect x="30" y="242" width="490" height="20" fill="#f0f0f0"/><text x="100" y="256" fill="#333">Total Addresses</text><text x="300" y="256" fill="#333">~4.3 billion</text><text x="430" y="256" fill="#333">340 undecillion</text>
    <rect x="30" y="262" width="490" height="18" fill="#fff"/><text x="100" y="275" fill="#333">Config</text><text x="300" y="275" fill="#333">Manual/DHCP</text><text x="430" y="275" fill="#333">SLAAC/DHCPv6</text>
  </g>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: IPv6 Address Structure — 8 groups of 16-bit hexadecimal</em></p>
</div>'''

    # Security / CIA / Threats
    elif any(k in t for k in ['security', 'threat', 'attack', 'vulnerab', 'cia', 'cryptograph', 'encryption', 'malware', 'phish', 'forensic', 'incident', 'risk', 'compliance', 'governance', 'endpoint']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="300" viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="300" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">CIA Triad &amp; Security Principles</text>
  <!-- CIA Triangle -->
  <polygon points="280,55 140,240 420,240" fill="none" stroke="#8b0000" stroke-width="3"/>
  <circle cx="280" cy="55" r="40" fill="#b22222"/>
  <text x="280" y="50" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">CONFI-</text>
  <text x="280" y="67" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">DENTIALITY</text>
  <circle cx="140" cy="240" r="40" fill="#2a7ab5"/>
  <text x="140" y="235" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">INTEG-</text>
  <text x="140" y="252" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">RITY</text>
  <circle cx="420" cy="240" r="40" fill="#d4780a"/>
  <text x="420" y="235" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">AVAIL-</text>
  <text x="420" y="252" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">ABILITY</text>
  <!-- Labels -->
  <text x="475" y="60" fill="#333" font-family="Arial" font-size="11">🔐 Only authorized</text>
  <text x="475" y="74" fill="#333" font-family="Arial" font-size="11">users can access</text>
  <text x="475" y="100" fill="#333" font-family="Arial" font-size="11">data (encryption,</text>
  <text x="475" y="114" fill="#333" font-family="Arial" font-size="11">access controls)</text>
  <text x="30" y="185" fill="#333" font-family="Arial" font-size="11">✅ Data is accurate</text>
  <text x="30" y="199" fill="#333" font-family="Arial" font-size="11">and unaltered</text>
  <text x="30" y="213" fill="#333" font-family="Arial" font-size="11">(hashing, checksums)</text>
  <text x="455" y="185" fill="#333" font-family="Arial" font-size="11">⚡ Systems are</text>
  <text x="455" y="199" fill="#333" font-family="Arial" font-size="11">accessible when</text>
  <text x="455" y="213" fill="#333" font-family="Arial" font-size="11">needed (uptime,</text>
  <text x="455" y="227" fill="#333" font-family="Arial" font-size="11">redundancy)</text>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: The CIA Triad — Foundation of Information Security</em></p>
</div>'''

    # Default: generic network topology
    else:
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="520" height="260" viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="520" height="260" fill="#f8f9fa"/>
  <text x="260" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">Network Topology Overview</text>
  <!-- Internet Cloud -->
  <ellipse cx="260" cy="100" rx="55" ry="35" fill="#d4e8f7" stroke="#2a7ab5" stroke-width="2"/>
  <text x="260" y="96" text-anchor="middle" fill="#2a7ab5" font-family="Arial" font-size="12" font-weight="bold">INTERNET</text>
  <text x="260" y="111" text-anchor="middle" fill="#2a7ab5" font-family="Arial" font-size="10">☁ Cloud</text>
  <!-- Router -->
  <rect x="218" y="155" width="84" height="35" rx="6" fill="#b22222"/>
  <text x="260" y="177" text-anchor="middle" fill="white" font-family="Arial" font-size="12">Router/Firewall</text>
  <line x1="260" y1="135" x2="260" y2="155" stroke="#555" stroke-width="2"/>
  <!-- Switch -->
  <rect x="218" y="205" width="84" height="30" rx="6" fill="#d4780a"/>
  <text x="260" y="225" text-anchor="middle" fill="white" font-family="Arial" font-size="12">Switch (L2/L3)</text>
  <line x1="260" y1="190" x2="260" y2="205" stroke="#555" stroke-width="2"/>
  <!-- Hosts -->
  <rect x="80" y="205" width="70" height="30" rx="6" fill="#2a7ab5"/><text x="115" y="225" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Host A</text>
  <rect x="160" y="235" width="70" height="25" rx="6" fill="#2a7ab5"/><text x="195" y="252" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Host B</text>
  <rect x="300" y="235" width="70" height="25" rx="6" fill="#2a7ab5"/><text x="335" y="252" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Host C</text>
  <rect x="370" y="205" width="70" height="30" rx="6" fill="#2a7ab5"/><text x="405" y="225" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Server</text>
  <line x1="230" y1="220" x2="150" y2="220" stroke="#555" stroke-width="2"/>
  <line x1="230" y1="220" x2="195" y2="235" stroke="#555" stroke-width="2"/>
  <line x1="290" y1="220" x2="335" y2="235" stroke="#555" stroke-width="2"/>
  <line x1="290" y1="220" x2="370" y2="220" stroke="#555" stroke-width="2"/>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: Typical Enterprise Network Architecture</em></p>
</div>'''


def build_rich_page_html(title: str, md_content: str) -> str:
    """Build richly styled Canvas page with expanded content and SVG diagram."""
    base_html = md2html(md_content)
    diagram   = get_topic_svg(title)

    return f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<!-- HEADER BANNER -->
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">📚 Texas Wesleyan University · CIS/CSC Program · University 3.0</p>
</div>

<!-- LEARNING OBJECTIVES CALLOUT -->
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 LEARNING OBJECTIVES</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13px;">After completing this reading guide, you will be able to explain the core concepts, identify real-world applications, and apply this knowledge in the weekly quiz and lab assignment.</p>
</div>

<!-- TOPIC DIAGRAM -->
{diagram}

<!-- MAIN CONTENT -->
<div style="background:white;padding:8px 0;line-height:1.8;color:#333;font-size:15px;">
{base_html}
</div>

<!-- STUDY TIP BOX -->
<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 STUDY TIP — Before the Quiz</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13px;">Review each heading above and try to explain it out loud without looking. If you get stuck, reread that section. The quiz questions are drawn directly from the concepts in this reading guide.</p>
</div>

<!-- KEY TERMS BOX -->
<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 KEY TERMS TO KNOW</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13px;">Scan this guide and write down every term in <strong>bold</strong>. Define each one in your own words — this is the most effective way to prepare for both the quiz and the certification exam.</p>
</div>

<!-- CAREER CONNECTION -->
<div style="background:#fce4ec;border-left:5px solid #e91e63;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#880e4f;">🏆 WHY THIS MATTERS IN YOUR CAREER</p>
  <p style="margin:6px 0 0;color:#880e4f;font-size:13px;">These concepts appear on industry certifications (CompTIA Network+, Security+, CySA+) and are tested in IT job interviews. Mastering this module directly builds marketable skills employers look for in network administrators and security analysts.</p>
</div>

</div>'''


# ─── PHASE 1: PUSH QUIZ QUESTIONS ─────────────────────────────────────────────
def fix_quiz(course_id: int, quiz_id: int, md_path: Path, mod_num: int):
    if not md_path.exists():
        print(f"    ⚠ Quiz file not found: {md_path}")
        return

    md_text   = md_path.read_text(encoding='utf-8')
    questions = parse_quiz(md_text)

    if not questions:
        print(f"    ⚠ No questions parsed from {md_path.name}")
        return

    # Delete any existing questions first
    existing = api_get(f'/courses/{course_id}/quizzes/{quiz_id}/questions?per_page=50')
    if isinstance(existing, list):
        for eq in existing:
            api_delete(f'/courses/{course_id}/quizzes/{quiz_id}/questions/{eq["id"]}')
            time.sleep(0.15)

    pts_each = round(100.0 / len(questions), 1)
    pushed = 0
    for q in questions:
        # Build Canvas answer list
        answers = []
        for lbl in sorted(q['options'].keys()):
            answers.append({
                'answer_text':   q['options'][lbl],
                'answer_weight': 100 if lbl == q['correct'] else 0,
                'answer_html':   '',
            })

        payload = {
            'question': {
                'question_name':  f'Question {pushed+1}',
                'question_text':  q['stem'],
                'question_type':  'multiple_choice_question',
                'points_possible': pts_each,
                'answers':         answers,
            }
        }
        res = api_post(f'/courses/{course_id}/quizzes/{quiz_id}/questions', payload)
        if res.get('id'):
            pushed += 1
        time.sleep(0.3)

    print(f"    ✅ Pushed {pushed}/{len(questions)} questions → Quiz {quiz_id}")


# ─── PHASE 2: PUSH READING GUIDE PAGES ───────────────────────────────────────
def fix_page(course_id: int, page_url: str, page_title: str, md_path: Path):
    if not md_path.exists():
        print(f"    ⚠ Reading guide not found: {md_path}")
        return

    md_text  = md_path.read_text(encoding='utf-8')
    rich_html = build_rich_page_html(page_title, md_text)

    payload = {
        'wiki_page': {
            'body':           rich_html,
            'published':      True,
            'notify_of_update': False,
        }
    }
    res = api_put(f'/courses/{course_id}/pages/{page_url}', payload)
    if res.get('url'):
        print(f"    ✅ Updated page → {page_title[:70]}")
    else:
        print(f"    ⚠ Page update uncertain for {page_url}")


# ─── PHASE 3: FIX DISCUSSIONS ────────────────────────────────────────────────
def fix_discussions(course_id: int, course_dir: Path):
    topics = api_get(f'/courses/{course_id}/discussion_topics?per_page=50')
    if not isinstance(topics, list):
        return
    for topic in topics:
        # Check if body is missing or too short
        msg = topic.get('message') or ''
        if len(msg.strip()) < 50:
            # Try to find matching discussion md file
            title = topic.get('title','')
            mod_m = re.search(r'M(\d+)', title)
            if not mod_m:
                continue
            mod_num = int(mod_m.group(1))
            disc_file = sorted((course_dir / f'Module_{mod_num:02d}').glob('*Discussion*.md'))
            if not disc_file:
                continue
            disc_md = disc_file[0].read_text(encoding='utf-8')
            rich_html = md2html(disc_md)
            payload = {
                'title':                topic['title'],
                'message':              rich_html,
                'discussion_type':      'threaded',
                'require_initial_post': True,
                'published':            True,
            }
            res = api_put(f'/courses/{course_id}/discussion_topics/{topic["id"]}', payload)
            if res.get('id'):
                print(f"    ✅ Fixed discussion → {topic['title'][:60]}")
            time.sleep(0.4)


# ─── MAIN ─────────────────────────────────────────────────────────────────────
PAGE_MAP_3321 = {
    1:  'reading-guide-m01-networking-fundamentals-and-the-osi-model',
    2:  'reading-guide-m02-tcp-slash-ip-model-and-network-protocols',
    3:  'reading-guide-m03-ip-addressing-ipv4-subnetting-cidr',
    4:  'reading-guide-m04-ipv6-addressing-and-transition-technologies',
    5:  'reading-guide-m05-network-infrastructure-cables-switches-routers',
    6:  'reading-guide-m06-wireless-networking-802-dot-11-standards-and-security',
    7:  'reading-guide-m07-network-monitoring-and-troubleshooting-tools',
    8:  'reading-guide-m08-network-security-concepts',
    9:  'reading-guide-m09-network-services-dns-dhcp-and-ntp',
    10: 'reading-guide-m10-routing-protocols-static-ospf-and-bgp',
    11: 'reading-guide-m11-switching-vlans-stp-and-etherchannel',
    12: 'reading-guide-m12-wide-area-networks',
    13: 'reading-guide-m13-unified-communications-and-collaboration',
    14: 'reading-guide-m14-network-troubleshooting-methodology',
    15: 'reading-guide-m15-network-documentation-and-policies',
    16: 'reading-guide-m16-network-exam-preparation',
}

PAGE_MAP_4328 = {
    1:  'reading-guide-m01-threats-attacks-and-vulnerabilities',
    2:  'reading-guide-m02-social-engineering-and-phishing',
    3:  'reading-guide-m03-application-attacks-and-software-vulnerabilities',
    4:  'reading-guide-m04-malware-social-engineering-and-indicators-of-compromise',
    5:  'reading-guide-m05-cryptography-and-pki',
    6:  'reading-guide-m06-identity-and-access-management',
    7:  'reading-guide-m07-network-security-architecture',
    8:  'reading-guide-m08-endpoint-security',
    9:  'reading-guide-m09-cloud-security',
    10: 'reading-guide-m10-application-security',
    11: 'reading-guide-m11-incident-response',
    12: 'reading-guide-m12-digital-forensics',
    13: 'reading-guide-m13-risk-management',
    14: 'reading-guide-m14-governance-compliance-and-regulatory-frameworks',
    15: 'reading-guide-m15-security-operations',
    16: 'reading-guide-m16-security-exam-preparation-and-capstone',
}

PAGE_MAPS = {
    13089: PAGE_MAP_3321,
    13090: PAGE_MAP_4328,
}

if __name__ == '__main__':
    for course in COURSES:
        cid      = course['id']
        cdir     = BASE_DIR / course['dir']
        page_map = PAGE_MAPS[cid]

        print(f"\n{'='*60}")
        print(f"COURSE {cid}: {course['name']} ({course['code']})")
        print(f"{'='*60}")

        for mod_num in range(1, 17):
            mod_dir = cdir / f'Module_{mod_num:02d}'
            print(f"\n  Module {mod_num:02d}:")

            # ── Quiz questions ────────────────────────────────────────────────
            quiz_id   = course['quiz_ids'].get(mod_num)
            quiz_file = None
            if mod_dir.exists():
                matches = sorted(mod_dir.glob('04_Quiz_*.md'))
                if not matches:
                    matches = sorted(mod_dir.glob('*Quiz*.md'))
                if matches:
                    quiz_file = matches[0]

            if quiz_id and quiz_file:
                print(f"    [QUIZ] Pushing questions to quiz {quiz_id}...")
                fix_quiz(cid, quiz_id, quiz_file, mod_num)
            elif quiz_id:
                print(f"    ⚠ Quiz file missing for module {mod_num}")

            # ── Reading Guide page ────────────────────────────────────────────
            page_url = page_map.get(mod_num)
            rg_file  = None
            if mod_dir.exists():
                matches = sorted(mod_dir.glob('02_Reading_Guide_*.md'))
                if not matches:
                    matches = sorted(mod_dir.glob('*Reading_Guide*.md'))
                if matches:
                    rg_file = matches[0]

            if page_url and rg_file:
                # Build page title from file
                rg_text   = rg_file.read_text(encoding='utf-8')
                title_m   = re.search(r'^#\s+(.+)$', rg_text, re.M)
                page_title = re.sub(r'[*_`]', '', title_m.group(1)).strip() if title_m else f'Reading Guide Module {mod_num:02d}'
                print(f"    [PAGE] Updating reading guide page...")
                fix_page(cid, page_url, page_title, rg_file)
            elif page_url:
                print(f"    ⚠ Reading guide MD missing for module {mod_num}")

            time.sleep(0.5)

        # ── Fix discussions ───────────────────────────────────────────────────
        print(f"\n  [DISCUSSIONS] Checking discussions for course {cid}...")
        fix_discussions(cid, cdir)

    print(f"\n{'='*60}")
    print("✅ ALL DONE — Both courses updated in Canvas")
    print("='*60")

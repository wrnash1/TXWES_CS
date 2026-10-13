# -*- coding: utf-8 -*-
"""
TXWES Canvas Spring 2026 Course Fixer
Fixes Spring 2026 live courses on txwes.instructure.com:
  - CIS-4327 Database Administration (Course #11713)
  - CIS-3326 Windows Server Admin   (Course #11709)

Populates:
  1. Reading Guide / Lesson Content pages (blank → rich HTML + SVG diagrams)
  2. Discussion topics (verify content)
  3. Quizzes that have 0 questions (adds from local Markdown)
"""

import os, re, json, time, sys, urllib.request, urllib.parse, urllib.error
from pathlib import Path

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
BASE_DIR   = Path(__file__).parent

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

# ─── HTTP HELPERS ─────────────────────────────────────────────────────────────
def api_get(path):
    url = f"{CANVAS_URL}/api/v1{path}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"    [GET ERROR] {path}: {e.code} {e.read()[:200]}")
        return {}

def api_post(path, data):
    url  = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode()
    req  = urllib.request.Request(url, data=body, headers=HEADERS, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"    [POST ERROR] {path}: {e.code} {e.read()[:300]}")
        return {}

def api_put(path, data):
    url  = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode()
    req  = urllib.request.Request(url, data=body, headers=HEADERS, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"    [PUT ERROR] {path}: {e.code} {e.read()[:300]}")
        return {}

def api_delete(path):
    url = f"{CANVAS_URL}/api/v1{path}"
    req = urllib.request.Request(url, headers=HEADERS, method='DELETE')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True
    except urllib.error.HTTPError:
        return False

# ─── MARKDOWN → HTML ──────────────────────────────────────────────────────────
def md2html(text):
    if not text:
        return ""
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    code_blocks = []
    def _store_code(m):
        lang = m.group(1) or ""
        code = m.group(2).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        idx  = len(code_blocks)
        lc   = f' class="language-{lang}"' if lang else ''
        code_blocks.append(
            f'<pre style="background:#1e1e1e;color:#d4d4d4;padding:16px;border-radius:6px;'
            f'overflow-x:auto;font-family:monospace;font-size:14px;line-height:1.5;">'
            f'<code{lc}>{code}</code></pre>')
        return f'__CODE_{idx}__'
    text = re.sub(r'```(\w*)\n(.*?)```', _store_code, text, flags=re.DOTALL)

    def _inline(s):
        s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        s = re.sub(r'\*\*(.+?)\*\*',     r'<strong>\1</strong>', s)
        s = re.sub(r'__(.+?)__',         r'<strong>\1</strong>', s)
        s = re.sub(r'\*([^*\n]+?)\*',    r'<em>\1</em>', s)
        s = re.sub(r'_([^_\n]+?)_',      r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+?)`',
                   r'<code style="background:#f0f0f0;padding:2px 6px;border-radius:3px;font-family:monospace;">\1</code>', s)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', s)
        return s

    lines  = text.split('\n')
    out    = []
    in_list= None
    in_bq  = False
    in_tbl = False
    t_hdrs = []
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
        nonlocal in_tbl, t_hdrs, t_rows
        if not in_tbl:
            return
        rows_html = ''
        if t_hdrs:
            rows_html += '<thead><tr>'
            for h in t_hdrs:
                rows_html += f'<th style="padding:10px;background:#8b0000;color:#fff;text-align:left;">{_inline(h.strip())}</th>'
            rows_html += '</tr></thead>'
        if t_rows:
            rows_html += '<tbody>'
            for i, row in enumerate(t_rows):
                bg = '#fff' if i % 2 == 0 else '#f9f9f9'
                rows_html += f'<tr style="background:{bg};">'
                for td in row:
                    rows_html += f'<td style="padding:8px;border:1px solid #ddd;">{_inline(td.strip())}</td>'
                rows_html += '</tr>'
            rows_html += '</tbody>'
        out.append(f'<table style="border-collapse:collapse;width:100%;margin:16px 0;">{rows_html}</table>')
        in_tbl = False
        t_hdrs.clear()
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
            lvl   = len(hm.group(1))
            sizes = {1:'28px',2:'22px',3:'18px',4:'16px',5:'14px',6:'13px'}
            color = '#8b0000' if lvl <= 3 else '#333'
            bb    = 'border-bottom:2px solid #b22222;padding-bottom:6px;' if lvl == 2 else ''
            out.append(f'<h{lvl} style="font-size:{sizes[lvl]};color:{color};margin:20px 0 8px;font-weight:bold;{bb}">'
                       f'{_inline(hm.group(2))}</h{lvl}>')
            continue

        if raw.startswith('|') and raw.endswith('|'):
            flush_list(); flush_bq()
            cells = raw.split('|')[1:-1]
            if all(re.match(r'^\s*:?-+:?\s*$', c) for c in cells):
                continue
            if not in_tbl:
                in_tbl = True
                t_hdrs[:] = cells
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


# ─── QUIZ PARSER ──────────────────────────────────────────────────────────────
def parse_quiz(md_text):
    questions = []
    SPLIT = re.compile(
        r'(\n(?:#{2,3}\s+Question\s*\d+|####\s+Q\d+(?=\n)|\*\*Question\s+\d+[^*\n]*\*\*)[^\n]*\n)',
        re.IGNORECASE)
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


# ─── SVG DIAGRAMS ─────────────────────────────────────────────────────────────
def get_topic_svg(title):
    t = title.lower()

    if any(k in t for k in ['database', 'sql', 'relational', 'mysql', 'nosql', 'bigquery', 'spanner', 'firestore']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="320" viewBox="0 0 560 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="320" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">Relational Database Architecture</text>
  <!-- Application Layer -->
  <rect x="180" y="45" width="200" height="40" rx="6" fill="#b22222"/>
  <text x="280" y="70" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">Application / Client</text>
  <line x1="280" y1="85" x2="280" y2="105" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <!-- SQL Layer -->
  <rect x="155" y="105" width="250" height="40" rx="6" fill="#cc3333"/>
  <text x="280" y="130" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">SQL Query Engine</text>
  <line x1="280" y1="145" x2="280" y2="165" stroke="#555" stroke-width="2"/>
  <!-- Tables -->
  <rect x="40" y="165" width="140" height="50" rx="6" fill="#2a7ab5"/>
  <text x="110" y="188" text-anchor="middle" fill="white" font-family="Arial" font-size="12" font-weight="bold">Table: Users</text>
  <text x="110" y="205" text-anchor="middle" fill="white" font-family="Arial" font-size="11">id | name | email</text>
  <rect x="210" y="165" width="140" height="50" rx="6" fill="#2a7ab5"/>
  <text x="280" y="188" text-anchor="middle" fill="white" font-family="Arial" font-size="12" font-weight="bold">Table: Orders</text>
  <text x="280" y="205" text-anchor="middle" fill="white" font-family="Arial" font-size="11">id | user_id | total</text>
  <rect x="380" y="165" width="140" height="50" rx="6" fill="#2a7ab5"/>
  <text x="450" y="188" text-anchor="middle" fill="white" font-family="Arial" font-size="12" font-weight="bold">Table: Products</text>
  <text x="450" y="205" text-anchor="middle" fill="white" font-family="Arial" font-size="11">id | name | price</text>
  <!-- FK arrows -->
  <line x1="210" y1="190" x2="183" y2="190" stroke="#f90" stroke-width="2" stroke-dasharray="4"/>
  <line x1="380" y1="190" x2="352" y2="190" stroke="#f90" stroke-width="2" stroke-dasharray="4"/>
  <text x="196" y="185" font-family="Arial" font-size="10" fill="#f90">FK</text>
  <text x="360" y="185" font-family="Arial" font-size="10" fill="#f90">FK</text>
  <!-- Storage -->
  <rect x="155" y="240" width="250" height="40" rx="6" fill="#1a5a8a"/>
  <text x="280" y="265" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">💾 Persistent Storage (Disk / Cloud)</text>
  <line x1="110" y1="215" x2="110" y2="250" stroke="#555" stroke-width="1" stroke-dasharray="3"/>
  <line x1="110" y1="250" x2="155" y2="260" stroke="#555" stroke-width="1" stroke-dasharray="3"/>
  <line x1="280" y1="215" x2="280" y2="240" stroke="#555" stroke-width="2"/>
  <line x1="450" y1="215" x2="450" y2="250" stroke="#555" stroke-width="1" stroke-dasharray="3"/>
  <line x1="450" y1="250" x2="405" y2="260" stroke="#555" stroke-width="1" stroke-dasharray="3"/>
  <!-- SQL example -->
  <rect x="30" y="290" width="500" height="22" rx="4" fill="#eee"/>
  <text x="40" y="306" font-family="monospace" font-size="11" fill="#333">SELECT u.name, o.total FROM Users u JOIN Orders o ON u.id = o.user_id;</text>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: Relational Database — Tables, Foreign Keys, and SQL Query Flow</em></p>
</div>'''

    elif any(k in t for k in ['windows server', 'active directory', 'server admin', 'server 2019', 'server 2022', 'powershell', 'group policy', 'dns', 'dhcp', 'iis', 'hyper-v']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="320" viewBox="0 0 560 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="320" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">Windows Server Infrastructure</text>
  <!-- Domain Controller -->
  <rect x="190" y="45" width="180" height="50" rx="6" fill="#b22222"/>
  <text x="280" y="67" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">Domain Controller</text>
  <text x="280" y="84" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Active Directory / DNS / DHCP</text>
  <!-- Services -->
  <line x1="180" y1="95" x2="120" y2="140" stroke="#555" stroke-width="2"/>
  <line x1="280" y1="95" x2="280" y2="140" stroke="#555" stroke-width="2"/>
  <line x1="380" y1="95" x2="440" y2="140" stroke="#555" stroke-width="2"/>
  <rect x="50" y="140" width="140" height="45" rx="6" fill="#2a7ab5"/>
  <text x="120" y="161" text-anchor="middle" fill="white" font-family="Arial" font-size="12" font-weight="bold">File Server</text>
  <text x="120" y="177" text-anchor="middle" fill="white" font-family="Arial" font-size="11">NTFS / DFS / SMB</text>
  <rect x="210" y="140" width="140" height="45" rx="6" fill="#2a7ab5"/>
  <text x="280" y="161" text-anchor="middle" fill="white" font-family="Arial" font-size="12" font-weight="bold">Web Server (IIS)</text>
  <text x="280" y="177" text-anchor="middle" fill="white" font-family="Arial" font-size="11">HTTP/HTTPS / ASP.NET</text>
  <rect x="370" y="140" width="140" height="45" rx="6" fill="#2a7ab5"/>
  <text x="440" y="161" text-anchor="middle" fill="white" font-family="Arial" font-size="12" font-weight="bold">Hyper-V</text>
  <text x="440" y="177" text-anchor="middle" fill="white" font-family="Arial" font-size="11">VM Host / Snapshots</text>
  <!-- Clients -->
  <line x1="120" y1="185" x2="120" y2="225" stroke="#555" stroke-width="1" stroke-dasharray="4"/>
  <line x1="280" y1="185" x2="280" y2="225" stroke="#555" stroke-width="1" stroke-dasharray="4"/>
  <line x1="440" y1="185" x2="440" y2="225" stroke="#555" stroke-width="1" stroke-dasharray="4"/>
  <rect x="40" y="225" width="100" height="35" rx="5" fill="#d4780a"/>
  <text x="90" y="247" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Client PC 1</text>
  <rect x="155" y="225" width="100" height="35" rx="5" fill="#d4780a"/>
  <text x="205" y="247" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Client PC 2</text>
  <rect x="275" y="225" width="100" height="35" rx="5" fill="#d4780a"/>
  <text x="325" y="247" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Client PC 3</text>
  <rect x="395" y="225" width="120" height="35" rx="5" fill="#d4780a"/>
  <text x="455" y="247" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Virtual Machine</text>
  <!-- Group Policy note -->
  <rect x="30" y="278" width="500" height="30" rx="5" fill="#fff3cd" stroke="#f0ad4e" stroke-width="1"/>
  <text x="280" y="298" text-anchor="middle" font-family="Arial" font-size="12" fill="#856404">🔑 Group Policy Objects (GPOs) enforce security settings across all clients via AD</text>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: Windows Server Domain Infrastructure Overview</em></p>
</div>'''

    elif any(k in t for k in ['security', 'threat', 'attack', 'cia', 'cryptograph', 'encryption', 'malware', 'phish', 'forensic', 'incident', 'risk', 'compliance', 'endpoint', 'cloud security', 'identity', 'access']):
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="560" height="300" viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="560" height="300" fill="#f8f9fa"/>
  <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">CIA Triad &amp; Security Principles</text>
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
  <text x="475" y="60" fill="#333" font-family="Arial" font-size="11">🔐 Encryption,</text>
  <text x="475" y="74" fill="#333" font-family="Arial" font-size="11">access controls</text>
  <text x="30" y="199" fill="#333" font-family="Arial" font-size="11">✅ Hashing,</text>
  <text x="30" y="213" fill="#333" font-family="Arial" font-size="11">checksums</text>
  <text x="455" y="199" fill="#333" font-family="Arial" font-size="11">⚡ Uptime,</text>
  <text x="455" y="213" fill="#333" font-family="Arial" font-size="11">redundancy</text>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: The CIA Triad — Foundation of Information Security</em></p>
</div>'''

    else:
        return '''<div style="text-align:center;margin:24px 0;">
<svg width="520" height="200" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:1px solid #ddd;border-radius:8px;">
  <rect width="520" height="200" fill="#f8f9fa"/>
  <text x="260" y="30" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b0000" font-family="Arial">Key Concept Overview</text>
  <rect x="40" y="55" width="130" height="55" rx="8" fill="#b22222"/>
  <text x="105" y="80" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">Understand</text>
  <text x="105" y="98" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Learn the concepts</text>
  <rect x="195" y="55" width="130" height="55" rx="8" fill="#d4780a"/>
  <text x="260" y="80" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">Apply</text>
  <text x="260" y="98" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Practice with labs</text>
  <rect x="350" y="55" width="130" height="55" rx="8" fill="#2a7ab5"/>
  <text x="415" y="80" text-anchor="middle" fill="white" font-family="Arial" font-size="13" font-weight="bold">Evaluate</text>
  <text x="415" y="98" text-anchor="middle" fill="white" font-family="Arial" font-size="11">Quiz &amp; discussion</text>
  <line x1="170" y1="82" x2="195" y2="82" stroke="#555" stroke-width="2" marker-end="url(#a)"/>
  <line x1="325" y1="82" x2="350" y2="82" stroke="#555" stroke-width="2" marker-end="url(#a)"/>
  <text x="260" y="155" text-anchor="middle" font-family="Arial" font-size="12" fill="#555">📌 Read → Practice → Demonstrate Mastery</text>
</svg>
<p style="font-size:12px;color:#777;margin-top:4px;"><em>Figure 1: Learning Cycle for this Module</em></p>
</div>'''


def build_rich_page_html(title, md_content):
    body    = md2html(md_content)
    diagram = get_topic_svg(title)
    return f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">📚 Texas Wesleyan University · CIS/CSC Program · University 3.0</p>
</div>

<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 LEARNING OBJECTIVES</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13px;">After completing this reading, you will be able to explain core concepts, identify real-world applications, and apply this knowledge in the weekly quiz, lab, and discussion assignments.</p>
</div>

{diagram}

<div style="background:white;padding:8px 0;line-height:1.8;color:#333;font-size:15px;">
{body}
</div>

<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 STUDY TIP — Before the Quiz</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13px;">Review each heading above and try to explain it out loud without looking. If you get stuck, reread that section. Quiz questions are drawn directly from concepts in this reading.</p>
</div>

<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 KEY TERMS TO KNOW</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13px;">Find every term in <strong>bold</strong> in this guide and define it in your own words. This is the most effective exam preparation strategy.</p>
</div>

<div style="background:#fce4ec;border-left:5px solid #e91e63;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#880e4f;">🏆 WHY THIS MATTERS IN YOUR CAREER</p>
  <p style="margin:6px 0 0;color:#880e4f;font-size:13px;">These concepts appear on industry certifications (CompTIA, Google Cloud, Microsoft) and are tested in IT job interviews. Mastering this module builds real, marketable skills employers look for.</p>
</div>

</div>'''


# ─── PAGE UPDATER ─────────────────────────────────────────────────────────────
def fix_page(course_id, page_url, page_title, md_path):
    if not md_path.exists():
        print(f"    ⚠ File not found: {md_path}")
        return False
    md_text   = md_path.read_text(encoding='utf-8')
    rich_html = build_rich_page_html(page_title, md_text)
    payload   = {'wiki_page': {'body': rich_html, 'published': True, 'notify_of_update': False}}
    res       = api_put(f'/courses/{course_id}/pages/{page_url}', payload)
    if res.get('url'):
        print(f"    ✅ Updated page → {page_title[:70]}")
        return True
    print(f"    ⚠ Page update may have failed: {page_url}")
    return False


# ─── QUIZ FIXER ───────────────────────────────────────────────────────────────
def fix_quiz(course_id, quiz_id, md_path):
    if not md_path.exists():
        print(f"    ⚠ Quiz file not found: {md_path}")
        return
    md_text   = md_path.read_text(encoding='utf-8')
    questions = parse_quiz(md_text)
    if not questions:
        print(f"    ⚠ No questions parsed from {md_path.name}")
        return
    existing = api_get(f'/courses/{course_id}/quizzes/{quiz_id}/questions?per_page=50')
    if isinstance(existing, list):
        for eq in existing:
            api_delete(f'/courses/{course_id}/quizzes/{quiz_id}/questions/{eq["id"]}')
            time.sleep(0.15)
    pts_each = round(100.0 / len(questions), 1)
    pushed   = 0
    for q in questions:
        answers = [{'answer_text': q['options'][l], 'answer_weight': 100 if l == q['correct'] else 0}
                   for l in sorted(q['options'])]
        res = api_post(f'/courses/{course_id}/quizzes/{quiz_id}/questions', {
            'question': {
                'question_name':   f'Question {pushed+1}',
                'question_text':   q['stem'],
                'question_type':   'multiple_choice_question',
                'points_possible': pts_each,
                'answers':         answers,
            }
        })
        if res.get('id'):
            pushed += 1
        time.sleep(0.3)
    print(f"    ✅ Pushed {pushed}/{len(questions)} questions → Quiz {quiz_id}")


# ─── DISCUSSION FIXER ─────────────────────────────────────────────────────────
def fix_discussions(course_id, course_dir):
    topics = api_get(f'/courses/{course_id}/discussion_topics?per_page=50')
    if not isinstance(topics, list):
        return
    fixed = 0
    for topic in topics:
        msg   = topic.get('message') or ''
        if len(msg.strip()) >= 50:
            continue
        title = topic.get('title', '')
        mod_m = re.search(r'[Mm](\d+)', title)
        if not mod_m:
            continue
        mod_num  = int(mod_m.group(1))
        mod_dir  = course_dir / f'Module_{mod_num:02d}'
        disc_files = sorted(mod_dir.glob('*Discussion*.md')) if mod_dir.exists() else []
        if not disc_files:
            continue
        disc_html = md2html(disc_files[0].read_text(encoding='utf-8'))
        res = api_put(f'/courses/{course_id}/discussion_topics/{topic["id"]}', {
            'title': title, 'message': disc_html,
            'discussion_type': 'threaded', 'require_initial_post': True, 'published': True,
        })
        if res.get('id'):
            print(f"    ✅ Fixed discussion → {title[:60]}")
            fixed += 1
        time.sleep(0.4)
    if fixed == 0:
        print(f"    ℹ  All discussions already have content.")


# ─── COURSE DEFINITIONS ───────────────────────────────────────────────────────
# CIS-4327 Database Admin — lesson-content-mX pages, chapter quizzes already have Qs
# CIS-3326 Windows Server — lesson-content-mX pages, module quizzes already have Qs

DB_PAGE_MAP = {
    1:  ('lesson-content-m1-introduction-to-database-administration-and-google-cloud',  'M01: Introduction to Database Administration & Google Cloud'),
    2:  ('lesson-content-m2-sql-fundamentals-and-relational-database-concepts',         'M02: SQL Fundamentals & Relational Database Concepts'),
    3:  ('lesson-content-m3-sql-investigation-and-database-security-fundamentals',      'M03: SQL Investigation & Database Security Fundamentals'),
    4:  ('lesson-content-m4-implementing-and-managing-google-cloud-sql',                'M04: Implementing & Managing Google Cloud SQL'),
    5:  ('lesson-content-m5-implementing-and-managing-google-cloud-spanner',            'M05: Implementing & Managing Google Cloud Spanner'),
    6:  ('lesson-content-m6-nosql-solutions-with-firestore-and-bigtable',               'M06: NoSQL Solutions with Firestore & Bigtable'),
    7:  ('lesson-content-m7-migrating-databases-to-google-cloud',                       'M07: Migrating Databases to Google Cloud'),
    8:  ('lesson-content-m8-ensuring-database-reliability-and-business-continuity',     'M08: Ensuring Database Reliability & Business Continuity'),
    9:  ('lesson-content-m9-monitoring-alerting-and-performance-tuning',                'M09: Monitoring, Alerting & Performance Tuning'),
    10: ('lesson-content-m10-automating-database-operations-on-google-cloud',           'M10: Automating Database Operations on Google Cloud'),
    11: ('lesson-content-m11-securing-google-cloud-database-services',                  'M11: Securing Google Cloud Database Services'),
    12: ('lesson-content-m12-data-analytics-with-google-bigquery',                      'M12: Data Analytics with Google BigQuery'),
    13: ('lesson-content-m13-database-reliability-engineering-practices',               'M13: Database Reliability Engineering Practices'),
    14: ('lesson-content-m14-google-cloud-database-engineer-certification-preparation', 'M14: Google Cloud Database Engineer Certification Prep'),
    15: ('lesson-content-m15-google-cloud-database-engineer-certification-exam',        'M15: Google Cloud Database Engineer Certification Exam'),
}

WIN_PAGE_MAP = {
    1:  ('lesson-content-m1',  'M01: Introduction to Windows Server Administration'),
    2:  ('lesson-content-m2',  'M02: Active Directory Domain Services'),
    3:  ('lesson-content-m3',  'M03: DNS and DHCP Configuration'),
    4:  ('lesson-content-m4',  'M04: File Services and Storage Solutions'),
    5:  ('lesson-content-m5',  'M05: Group Policy and Security Settings'),
    6:  ('lesson-content-m6',  'M06: Remote Desktop and Remote Management'),
    7:  ('lesson-content-m7',  'M07: Hyper-V and Virtualization'),
    8:  ('lesson-content-m8',  'M08: Windows Server Monitoring and Performance'),
    9:  ('lesson-content-m9',  'M09: Network Policy and Access Services'),
    10: ('lesson-content-m10', 'M10: IIS and Web Server Configuration'),
    11: ('lesson-content-m11', 'M11: PowerShell Automation'),
    12: ('lesson-content-m12', 'M12: Backup and Disaster Recovery'),
    13: ('lesson-content-m13', 'M13: Windows Server Security Hardening'),
    14: ('lesson-content-m14', 'M14: Patch Management and Updates'),
    15: ('lesson-content-m15', 'M15: Windows Server Exam Preparation'),
    16: ('lesson-content-m16', 'M16: Windows Server Capstone Review'),
}

COURSES = [
    {'id': 11713, 'code': 'CIS-4327', 'name': 'Database Administration',
     'dir': 'CIS-4327_Database_Admin', 'page_map': DB_PAGE_MAP, 'modules': 15},
    {'id': 11709, 'code': 'CIS-3326', 'name': 'Windows Server Admin',
     'dir': 'CIS-3326_Windows_Server_Admin', 'page_map': WIN_PAGE_MAP, 'modules': 16},
]

# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    for course in COURSES:
        cid      = course['id']
        cdir     = BASE_DIR / course['dir']
        page_map = course['page_map']
        mods     = course['modules']

        print(f"\n{'='*60}")
        print(f"COURSE {cid}: {course['name']} ({course['code']})")
        print(f"{'='*60}")

        for mod_num in range(1, mods + 1):
            mod_dir = cdir / f'Module_{mod_num:02d}'
            print(f"\n  Module {mod_num:02d}:")

            # Reading Guide page
            if mod_num in page_map:
                page_url, page_title = page_map[mod_num]
                rg_files = sorted(mod_dir.glob('02_Reading_Guide_*.md')) if mod_dir.exists() else []
                if not rg_files:
                    rg_files = sorted(mod_dir.glob('*Reading_Guide*.md')) if mod_dir.exists() else []
                if rg_files:
                    rg_md = rg_files[0].read_text(encoding='utf-8')
                    title_m = re.search(r'^#\s+(.+)$', rg_md, re.M)
                    if title_m:
                        page_title = re.sub(r'[*_`]', '', title_m.group(1)).strip()
                    print(f"    [PAGE] Updating lesson content page...")
                    fix_page(cid, page_url, page_title, rg_files[0])
                else:
                    print(f"    ⚠ No reading guide MD for module {mod_num}")

            time.sleep(0.5)

        # Discussions
        print(f"\n  [DISCUSSIONS] Checking discussions for course {cid}...")
        fix_discussions(cid, cdir)

    print(f"\n{'='*60}")
    print("✅ ALL DONE — Spring 2026 courses updated in Canvas")
    print(f"{'='*60}")

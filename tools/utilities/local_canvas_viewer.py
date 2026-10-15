#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Texas Wesleyan University - Local Canvas LMS Course Simulator & Viewer
Provides a local web interface to test, preview, and review all 48 courses,
their 16 modules, syllabi, interactive quizzes, reading guides, and labs.

Usage:
  python3 local_canvas_viewer.py [--port 8080]
"""

import os
import sys
import json
import re
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS"

# Markdown to HTML basic parser
def md_to_html(md_text):
    if not md_text:
        return ""
    # SVGs preservation
    svg_blocks = []
    def save_svg(match):
        svg_blocks.append(match.group(0))
        return f"<!--SVG_BLOCK_{len(svg_blocks)-1}-->"
    
    html = re.sub(r'<svg[\s\S]*?</svg>', save_svg, md_text, flags=re.IGNORECASE)

    # Escape basic HTML entities outside tags/blocks if needed, but preserve existing tags
    # Code blocks
    def code_block(match):
        lang = match.group(1) or ""
        code = match.group(2).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return f'<pre><code class="language-{lang}">{code}</code></pre>'
    html = re.sub(r'```([a-zA-Z0-9_-]*)\n([\s\S]*?)```', code_block, html)

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Tables
    def parse_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 2: return match.group(0)
        table_html = '<div class="table-container"><table class="table">'
        headers = [c.strip() for c in lines[0].split('|')[1:-1]]
        table_html += '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr></thead><tbody>'
        for line in lines[2:]:
            cols = [c.strip() for c in line.split('|')[1:-1]]
            table_html += '<tr>' + ''.join(f'<td>{c}</td>' for c in cols) + '</tr>'
        table_html += '</tbody></table></div>'
        return table_html
    html = re.sub(r'(\|[^\n]+\|\n\|[-:| ]+\|\n(\|[^\n]+\|\n?)+)', parse_table, html)

    # Headers
    html = re.sub(r'^###### (.*?)$', r'<h6>\1</h6>', html, flags=re.M)
    html = re.sub(r'^##### (.*?)$', r'<h5>\1</h5>', html, flags=re.M)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.M)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.M)

    # Bold and Italic
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Blockquotes / Alerts
    html = re.sub(r'^> \[\!NOTE\]\s*(.*?)$', r'<div class="alert alert-info">ℹ️ <strong>Note:</strong> \1</div>', html, flags=re.M)
    html = re.sub(r'^> \[\!TIP\]\s*(.*?)$', r'<div class="alert alert-success">💡 <strong>Tip:</strong> \1</div>', html, flags=re.M)
    html = re.sub(r'^> \[\!IMPORTANT\]\s*(.*?)$', r'<div class="alert alert-warning">⚠️ <strong>Important:</strong> \1</div>', html, flags=re.M)
    html = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.M)

    # Horizontal Rule
    html = re.sub(r'^(?:---|\*\*\*|___)\s*$', r'<hr/>', html, flags=re.M)

    # Lists
    lines = html.split('\n')
    in_ul = False
    in_ol = False
    new_lines = []
    for line in lines:
        ul_match = re.match(r'^\s*[-*+]\s+(.*)$', line)
        ol_match = re.match(r'^\s*(\d+)\.\s+(.*)$', line)
        if ul_match:
            if not in_ul:
                new_lines.append('<ul>')
                in_ul = True
            new_lines.append(f'<li>{ul_match.group(1)}</li>')
        elif ol_match:
            if not in_ol:
                new_lines.append('<ol>')
                in_ol = True
            new_lines.append(f'<li>{ol_match.group(2)}</li>')
        else:
            if in_ul:
                new_lines.append('</ul>')
                in_ul = False
            if in_ol:
                new_lines.append('</ol>')
                in_ol = False
            new_lines.append(line)
    if in_ul: new_lines.append('</ul>')
    if in_ol: new_lines.append('</ol>')
    html = '\n'.join(new_lines)

    # Paragraphs
    parts = re.split(r'\n{2,}', html)
    p_parts = []
    for part in parts:
        part_strip = part.strip()
        if not part_strip: continue
        if part_strip.startswith(('<h', '<ul', '<ol', '<pre', '<div', '<blockquote', '<table', '<hr', '<p', '<!--SVG')):
            p_parts.append(part_strip)
        else:
            p_parts.append(f'<p>{part_strip}</p>')
    html = '\n'.join(p_parts)

    # Restore SVGs
    for idx, svg in enumerate(svg_blocks):
        html = html.replace(f"<!--SVG_BLOCK_{idx}-->", svg)

    return html

def get_all_courses():
    courses = []
    tiers = [
        ("01_Bachelor_CIS_Programs", "Bachelor of Science in CIS (Undergraduate)"),
        ("02_Master_MCS_Program", "Master of Science in Computer Science (Graduate)"),
        ("03_Doctoral_DIT_Program", "Doctor of Information Technology (Doctoral)"),
    ]
    for tier_folder, tier_name in tiers:
        tier_path = os.path.join(BASE_DIR, tier_folder)
        if not os.path.exists(tier_path): continue
        for root, dirs, files in os.walk(tier_path):
            mods = sorted([d for d in dirs if d.startswith("Module_")])
            if mods:
                code_match = re.search(r'([A-Z]{3,4}-[0-9]{4}[A-Z]?)', os.path.basename(root))
                code = code_match.group(1) if code_match else os.path.basename(root).split('_')[0]
                rel_path = os.path.relpath(root, BASE_DIR)
                courses.append({
                    "code": code,
                    "title": os.path.basename(root).replace('_', ' '),
                    "tier": tier_name,
                    "tier_folder": tier_folder,
                    "rel_path": rel_path,
                    "module_count": len(mods),
                    "has_pptx": os.path.exists(os.path.join(root, "PowerPoints")),
                    "has_syllabus": any('syllabus' in f.lower() for f in os.listdir(root) + (os.listdir(os.path.join(root, "00_Course_Information")) if os.path.exists(os.path.join(root, "00_Course_Information")) else []))
                })
    return sorted(courses, key=lambda x: (x["tier_folder"], x["code"]))


def sanitize_for_students(text):
    if not text:
        return ""
    # 1. Blockquote production notes (e.g. > **PRODUCTION NOTES FOR INSTRUCTOR:**)
    text = re.sub(
        r'>\s*\*\*PRODUCTION\s+NOTES[^\*]*\*\*[\s\S]*?(?=\n\s*\n[^\>]|\n\s*---\s*\n|\n\s*##|\Z)',
        '',
        text,
        flags=re.IGNORECASE
    )
    # 2. Section header production notes (e.g. ## Production Notes, ## Pre-Production Notes)
    text = re.sub(
        r'(?:\n|^)#{2,4}\s+(?:Pre-)?Production\s+Notes[\s\S]*?(?=\n\s*#{1,4}\s+|\n\s*---\s*\n|\Z)',
        '',
        text,
        flags=re.IGNORECASE
    )
    # 3. Inline italicized production notes (e.g. *Production notes: ...*)
    text = re.sub(
        r'\*Production\s+notes:[^\*]*\*',
        '',
        text,
        flags=re.IGNORECASE
    )
    # 4. Teleprompter, camera, and slide cues
    cues = [
        r'\*\*\[INSTRUCTOR ON CAMERA[^\n\]]*\]\*\*',
        r'\[INSTRUCTOR ON CAMERA[^\n\]]*\]',
        r'\*\*\[ON CAMERA[^\n\]]*\]\*\*',
        r'\[ON CAMERA[^\n\]]*\]',
        r'\*\*\[SHOW SLIDE:[^\n\]]*\]\*\*',
        r'\[SHOW SLIDE:[^\n\]]*\]',
        r'\*\*\[SHOW SLIDE[^\n\]]*\]\*\*',
        r'\[SHOW SLIDE[^\n\]]*\]',
        r'\*\*\[PAUSE\]\*\*',
        r'\[PAUSE\]',
        r'\*\*\[SHOW DIAGRAM[^\n\]]*\]\*\*',
        r'\[SHOW DIAGRAM[^\n\]]*\]',
        r'\*\*\[TRANSITION[^\n\]]*\]\*\*',
        r'\[TRANSITION[^\n\]]*\]',
        r'\*\*\[DEMO[^\n\]]*\]\*\*',
        r'\[DEMO[^\n\]]*\]',
        r'\*\*\[CUT TO[^\n\]]*\]\*\*',
        r'\[CUT TO[^\n\]]*\]',
        r'\*\*\[DIRECTOR[^\n\]]*\]\*\*',
        r'\[DIRECTOR[^\n\]]*\]',
        r'\[Title card:[^\n\]]*\]',
        r'\*\*\[Title card:[^\n\]]*\]\*\*',
    ]
    for c in cues:
        text = re.sub(c, '', text, flags=re.IGNORECASE)
    # Clean section header timestamps e.g. ## [00:00 - 01:00] Title -> ## Title
    text = re.sub(r'^(#{2,4})\s*\[[0-9]{2}:[0-9]{2}\s*[\u2013-]\s*[0-9]{2}:[0-9]{2}\]\s*(.*)$', r'\1 \2', text, flags=re.MULTILINE)
    text = re.sub(r'^(#{2,4})\s*(.*?)\s*\[[0-9]{2}:[0-9]{2}\s*[\u2013-]\s*[0-9]{2}:[0-9]{2}\]\s*$', r'\1 \2', text, flags=re.MULTILINE)
    # 5. Clean up any leftover duplicate divider rules or multiple blank lines
    text = re.sub(r'---\s*\n\s*---', '---', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_slides_for_item(course_path, item_rel, content):
    slides = []
    course_name = os.path.basename(course_path).replace('_', ' ')
    
    # Check if item is a lecture, script, or reading guide
    item_l = item_rel.lower()
    is_lecture = any(k in item_l for k in ['video', 'reading', 'lecture', 'script', 'notes'])
    if not is_lecture:
        return []

    # 1. Cleaned Lecture Notes / Video Scripts: extract conceptual headings (## Section Title)
    sections = re.findall(r'(##\s+([^#\n]+)\n([\s\S]*?)(?=\n##\s+[^#\n]+|\Z))', content)
    if sections:
        doc_title_m = re.search(r'#\s+(.*?)\n(?:##\s+(.*?)\n)?', content)
        t1 = doc_title_m.group(1).strip() if doc_title_m else "Lecture Presentation"
        t2 = doc_title_m.group(2).strip() if (doc_title_m and doc_title_m.group(2)) else course_name
        slides.append({
            "title": t2,
            "subtitle": f"{t1} • Texas Wesleyan University",
            "bullets": [
                "Texas Wesleyan University — Department of Computer Science & Information Technology",
                "Master Interactive Presentation & Slide Deck Viewer",
                "Use the [◀ Previous] and [Next ▶] buttons or keyboard Arrow Left / Right keys to navigate.",
                "Synchronized with module video lecture, lab benchmarks, and certification blueprints."
            ]
        })
        for full_sec, sec_title, sec_body in sections:
            clean_sec_title = re.sub(r'\[.*?\]', '', sec_title).strip()
            if not clean_sec_title or clean_sec_title.lower().startswith('production'):
                continue
            
            raw_paras = [p.strip() for p in sec_body.split('\n\n') if p.strip()]
            bullets = []
            for p in raw_paras:
                if p.startswith('>') or p.startswith('---') or p.startswith('```') or p.startswith('<') or (p.startswith('**[') and p.endswith(']**')):
                    continue
                clean = re.sub(r'[\*\`\#]', '', p).strip('" ')
                clean = re.sub(r'\[.*?\]', '', clean).strip()
                sents = re.split(r'(?<=[.!?])\s+', clean)
                for s in sents:
                    s = s.strip()
                    if len(s) > 25 and not s.startswith('<'):
                        bullets.append(s[:150] + ('...' if len(s) > 150 else ''))
                        if len(bullets) >= 4:
                            break
                if len(bullets) >= 4:
                    break
            if not bullets:
                bullets = ["Core technical principles, theoretical framework, and laboratory mastery."]
            slides.append({
                "title": clean_sec_title,
                "subtitle": f"{course_name} • Key Concepts",
                "bullets": bullets
            })
        return slides

    # 2. Reading Guides: extract conceptual headings
    rg_sections = re.findall(r'(##\s+([0-9]+\.\s+.*?|[A-Z].*?)\n([\s\S]*?)(?=\n##\s+|\Z))', content)
    if rg_sections:
        doc_title_m = re.search(r'#\s+(.*?)\n', content)
        t1 = doc_title_m.group(1).strip() if doc_title_m else "Module Reading Guide"
        slides.append({
            "title": t1,
            "subtitle": f"{course_name} • Texas Wesleyan University",
            "bullets": [
                "Texas Wesleyan University — Department of Computer Science & Information Technology",
                "Module Core Architecture & Theoretical Slide Summary",
                "Use the [◀ Previous] and [Next ▶] buttons or keyboard Arrow Left / Right keys to navigate.",
                "Mastery review companion for textbook readings and laboratory applications."
            ]
        })
        for full_sec, sec_title, sec_body in rg_sections[:12]:
            clean_title = re.sub(r'^[0-9]+\.\s*', '', sec_title).strip()
            raw_paras = [p.strip() for p in sec_body.split('\n\n') if p.strip()]
            bullets = []
            for p in raw_paras:
                if p.startswith('>') or p.startswith('---') or p.startswith('```') or p.startswith('<'):
                    continue
                clean = re.sub(r'[\*\`\#\|]', '', p).strip('" ')
                sents = re.split(r'(?<=[.!?])\s+', clean)
                for s in sents:
                    s = s.strip()
                    if len(s) > 25 and not s.startswith('<'):
                        bullets.append(s[:150] + ('...' if len(s) > 150 else ''))
                        if len(bullets) >= 4:
                            break
                if len(bullets) >= 4:
                    break
            if bullets:
                slides.append({
                    "title": clean_title,
                    "subtitle": f"Domain Blueprint • {sec_title}",
                    "bullets": bullets
                })
        if len(slides) > 1:
            return slides

    # 3. Fallback: Parse Course Master PPTX
    import zipfile
    import xml.etree.ElementTree as ET
    pptx_dir = os.path.join(course_path, 'PowerPoints')
    if os.path.exists(pptx_dir):
        pptx_files = [os.path.join(pptx_dir, f) for f in os.listdir(pptx_dir) if f.endswith('.pptx')]
        if pptx_files:
            try:
                with zipfile.ZipFile(pptx_files[0], 'r') as z:
                    slide_names = [n for n in z.namelist() if re.match(r'^ppt/slides/slide\d+\.xml$', n)]
                    slide_names.sort(key=lambda s: int(re.search(r'\d+', s).group(0)))
                    for sname in slide_names:
                        tree = ET.fromstring(z.read(sname))
                        paras = []
                        for p in tree.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
                            t = ''.join([elem.text for elem in p.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if elem.text])
                            if t.strip():
                                paras.append(t.strip())
                        if paras:
                            slides.append({
                                "title": paras[0],
                                "subtitle": "Master Course Presentation Deck",
                                "bullets": paras[1:] if len(paras) > 1 else ["Course syllabus and curriculum alignment."]
                            })
            except Exception as e:
                pass
    return slides


class CanvasViewerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_parts = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(url_parts.path)
        query = urllib.parse.parse_qs(url_parts.query)

        if path == "/" or path == "/index.html":
            self.render_dashboard()
        elif path == "/course":
            course_rel = query.get("p", [""])[0]
            self.render_course(course_rel)
        elif path == "/item":
            course_rel = query.get("p", [""])[0]
            item_rel = query.get("item", [""])[0]
            self.render_item(course_rel, item_rel)
        elif path == "/syllabus":
            course_rel = query.get("p", [""])[0]
            self.render_syllabus(course_rel)
        elif path.endswith(".pptx"):
            self.serve_file(path)
        else:
            self.send_error(404, "Page Not Found")

    def serve_file(self, req_path):
        clean_path = req_path.lstrip('/')
        full_path = os.path.join(BASE_DIR, clean_path)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            self.send_response(200)
            self.send_header("Content-Type", "application/vnd.openxmlformats-officedocument.presentationml.presentation")
            self.send_header("Content-Disposition", f'attachment; filename="{os.path.basename(full_path)}"')
            self.send_header("Content-Length", str(os.path.getsize(full_path)))
            self.end_headers()
            with open(full_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File not found")

    def render_dashboard(self):
        courses = get_all_courses()
        total_courses = len(courses)
        ug_courses = sum(1 for c in courses if "Bachelor" in c["tier"])
        ms_courses = sum(1 for c in courses if "Master" in c["tier"])
        doc_courses = sum(1 for c in courses if "Doctoral" in c["tier"])

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Texas Wesleyan University - Canvas Course Simulator</title>
<style>
  :root {{
    --txwes-navy: #1B365D;
    --txwes-gold: #D9A74A;
    --txwes-slate: #0F172A;
    --canvas-bg: #F5F7FA;
    --card-bg: #FFFFFF;
    --text-primary: #1E293B;
    --text-muted: #64748B;
    --border-color: #E2E8F0;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: var(--canvas-bg); color: var(--text-primary); line-height: 1.5; }}
  
  .canvas-layout {{ display: flex; min-height: 100vh; }}
  .global-nav {{ width: 84px; background: var(--txwes-navy); display: flex; flex-direction: column; align-items: center; padding: 16px 0; color: #fff; flex-shrink: 0; }}
  .global-nav .brand-logo {{ font-size: 26px; margin-bottom: 24px; color: var(--txwes-gold); }}
  .global-nav a {{ color: #cbd5e1; text-decoration: none; font-size: 11px; display: flex; flex-direction: column; align-items: center; margin-bottom: 20px; font-weight: 500; }}
  .global-nav a:hover, .global-nav a.active {{ color: var(--txwes-gold); }}
  .global-nav .nav-icon {{ font-size: 20px; margin-bottom: 4px; }}
  
  .main-content {{ flex: 1; padding: 32px 48px; max-width: 1400px; }}
  .header-banner {{ background: linear-gradient(135deg, var(--txwes-navy) 0%, #0f2444 100%); color: white; padding: 28px 36px; border-radius: 12px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.15); }}
  .header-banner h1 {{ font-size: 28px; font-weight: 700; margin-bottom: 8px; }}
  .header-banner p {{ color: #cbd5e1; font-size: 15px; }}
  .stats-row {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 32px; }}
  .stat-card {{ background: var(--card-bg); padding: 20px; border-radius: 10px; border: 1px solid var(--border-color); box-shadow: 0 2px 4px rgba(0,0,0,0.02); }}
  .stat-card .num {{ font-size: 28px; font-weight: 800; color: var(--txwes-navy); }}
  .stat-card .label {{ font-size: 13px; color: var(--text-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
  
  .tier-section {{ margin-bottom: 40px; }}
  .tier-title {{ font-size: 20px; font-weight: 700; color: var(--txwes-navy); margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid var(--txwes-gold); display: flex; justify-content: space-between; align-items: center; }}
  .tier-badge {{ font-size: 12px; background: #e2e8f0; color: var(--txwes-navy); padding: 4px 12px; border-radius: 20px; font-weight: 600; }}
  
  .course-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 20px; }}
  .course-card {{ background: var(--card-bg); border-radius: 10px; border: 1px solid var(--border-color); overflow: hidden; transition: transform 0.15s ease, box-shadow 0.15s ease; text-decoration: none; color: inherit; display: flex; flex-direction: column; }}
  .course-card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 16px rgba(0,0,0,0.08); border-color: var(--txwes-gold); }}
  .card-top {{ height: 100px; background: var(--txwes-navy); position: relative; padding: 16px; display: flex; flex-direction: column; justify-content: flex-end; }}
  .card-top.grad {{ background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); }}
  .card-top.doc {{ background: linear-gradient(135deg, #431407 0%, #1e1b4b 100%); }}
  .course-code {{ background: var(--txwes-gold); color: #000; padding: 3px 8px; border-radius: 4px; font-weight: 800; font-size: 12px; align-self: flex-start; }}
  .card-body {{ padding: 18px; flex: 1; display: flex; flex-direction: column; justify-content: space-between; }}
  .course-name {{ font-size: 16px; font-weight: 700; color: var(--text-primary); margin-bottom: 12px; }}
  .card-meta {{ display: flex; gap: 8px; font-size: 12px; color: var(--text-muted); flex-wrap: wrap; }}
  .badge-tag {{ background: #f1f5f9; padding: 4px 8px; border-radius: 4px; font-weight: 600; }}
  .badge-tag.ready {{ background: #ecfdf5; color: #047857; }}
</style>
</head>
<body>
<div class="canvas-layout">
  <div class="global-nav">
    <div class="brand-logo">🏛️</div>
    <a href="/" class="active"><div class="nav-icon">📊</div>Dashboard</a>
    <a href="/"><div class="nav-icon">📚</div>Courses</a>
  </div>
  <div class="main-content">
    <div class="header-banner">
      <h1>Texas Wesleyan University — Canvas Course Simulator</h1>
      <p>Local offline course preview and review testing environment for university computing programs.</p>
    </div>
    
    <div class="stats-row">
      <div class="stat-card"><div class="num">{total_courses}</div><div class="label">Total Courses</div></div>
      <div class="stat-card"><div class="num">{ug_courses}</div><div class="label">Undergraduate (BS CIS)</div></div>
      <div class="stat-card"><div class="num">{ms_courses}</div><div class="label">Graduate (MCS)</div></div>
      <div class="stat-card"><div class="num">{doc_courses}</div><div class="label">Doctoral (DIT)</div></div>
    </div>
"""
        current_tier = ""
        for c in courses:
            if c["tier"] != current_tier:
                if current_tier != "":
                    html += "</div></div>"
                current_tier = c["tier"]
                tier_badge = "16-Week Format" if "Bachelor" in current_tier else "Graduate Level"
                html += f"""
    <div class="tier-section">
      <div class="tier-title">
        <span>{current_tier}</span>
        <span class="tier-badge">{tier_badge}</span>
      </div>
      <div class="course-grid">
"""
            card_class = "doc" if "Doctoral" in c["tier"] else ("grad" if "Master" in c["tier"] else "")
            html += f"""
        <a href="/course?p={urllib.parse.quote(c['rel_path'])}" class="course-card">
          <div class="card-top {card_class}">
            <span class="course-code">{c['code']}</span>
          </div>
          <div class="card-body">
            <div class="course-name">{c['title']}</div>
            <div class="card-meta">
              <span class="badge-tag ready">✓ {c['module_count']} Modules</span>
              <span class="badge-tag">3.0 SCH</span>
              {'<span class="badge-tag">📊 PPTX Ready</span>' if c['has_pptx'] else ''}
              {'<span class="badge-tag">📜 Syllabus</span>' if c['has_syllabus'] else ''}
            </div>
          </div>
        </a>
"""
        html += """
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def render_course(self, course_rel):
        course_path = os.path.join(BASE_DIR, course_rel)
        if not os.path.exists(course_path):
            self.send_error(404, "Course path not found")
            return

        course_title = os.path.basename(course_path).replace('_', ' ')
        modules = sorted([d for d in os.listdir(course_path) if d.startswith("Module_")])

        # PPTX files
        pptx_files = []
        pp_dir = os.path.join(course_path, "PowerPoints")
        if os.path.exists(pp_dir):
            pptx_files = [f for f in os.listdir(pp_dir) if f.endswith('.pptx')]

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{course_title} - Canvas Course Shell</title>
<style>
  :root {{
    --txwes-navy: #1B365D;
    --txwes-gold: #D9A74A;
    --canvas-bg: #F5F7FA;
    --border-color: #E2E8F0;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background: #fff; color: #1E293B; }}
  .app-layout {{ display: flex; min-height: 100vh; }}
  
  .global-nav {{ width: 84px; background: var(--txwes-navy); display: flex; flex-direction: column; align-items: center; padding: 16px 0; color: #fff; flex-shrink: 0; }}
  .global-nav a {{ color: #cbd5e1; text-decoration: none; font-size: 11px; display: flex; flex-direction: column; align-items: center; margin-bottom: 20px; }}
  .global-nav a:hover {{ color: var(--txwes-gold); }}
  
  .course-nav {{ width: 220px; border-right: 1px solid var(--border-color); padding: 24px 16px; background: #f8fafc; flex-shrink: 0; }}
  .course-nav h2 {{ font-size: 13px; text-transform: uppercase; color: #64748B; margin-bottom: 16px; letter-spacing: 0.5px; }}
  .course-nav ul {{ list-style: none; }}
  .course-nav li {{ margin-bottom: 6px; }}
  .course-nav a {{ display: block; padding: 8px 12px; border-radius: 6px; text-decoration: none; color: #334155; font-size: 14px; font-weight: 500; }}
  .course-nav a.active, .course-nav a:hover {{ background: #e2e8f0; color: var(--txwes-navy); font-weight: 600; }}

  .course-main {{ flex: 1; padding: 32px 48px; max-width: 1100px; }}
  .course-header {{ border-bottom: 2px solid var(--txwes-navy); padding-bottom: 16px; margin-bottom: 28px; display: flex; justify-content: space-between; align-items: flex-end; }}
  .course-header h1 {{ font-size: 24px; color: var(--txwes-navy); }}
  .btn-group {{ display: flex; gap: 10px; }}
  .btn {{ padding: 8px 16px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; cursor: pointer; }}
  .btn-primary {{ background: var(--txwes-navy); color: #fff; }}
  .btn-gold {{ background: var(--txwes-gold); color: #000; }}

  .module-card {{ border: 1px solid var(--border-color); border-radius: 8px; margin-bottom: 16px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }}
  .module-header {{ background: #f8fafc; padding: 14px 20px; font-weight: 700; color: var(--txwes-navy); border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center; }}
  .module-items {{ list-style: none; }}
  .module-item {{ padding: 12px 20px; border-bottom: 1px solid #f1f5f9; display: flex; align-items: center; justify-content: space-between; }}
  .module-item:last-child {{ border-bottom: none; }}
  .module-item a {{ text-decoration: none; color: #1e293b; font-size: 14px; font-weight: 500; display: flex; align-items: center; gap: 10px; }}
  .module-item a:hover {{ color: #2563eb; }}
  .item-badge {{ font-size: 11px; padding: 2px 8px; border-radius: 12px; background: #e2e8f0; color: #475569; font-weight: 600; }}
  .badge-reading {{ background: #e0f2fe; color: #0369a1; }}
  .badge-lab {{ background: #fef3c7; color: #92400e; }}
  .badge-quiz {{ background: #fce7f3; color: #9d174d; }}
  .badge-disc {{ background: #f0fdf4; color: #15803d; }}
</style>
</head>
<body>
<div class="app-layout">
  <div class="global-nav">
    <div style="font-size:24px; margin-bottom:24px; color:#D9A74A;">🏛️</div>
    <a href="/"><div style="font-size:20px;">📊</div>Dashboard</a>
    <a href="/" class="active"><div style="font-size:20px;">📚</div>Courses</a>
  </div>
  
  <div class="course-nav">
    <h2>Course Navigation</h2>
    <ul>
      <li><a href="/course?p={urllib.parse.quote(course_rel)}" class="active">Modules</a></li>
      <li><a href="/syllabus?p={urllib.parse.quote(course_rel)}">Syllabus</a></li>
      <li><a href="/">All Courses</a></li>
    </ul>
    {f'''<div style="margin-top:24px;">
      <h2 style="margin-bottom:8px;">Lecture Decks</h2>
      {"".join(f'<a href="/{urllib.parse.quote(course_rel)}/PowerPoints/{f}" class="btn btn-gold" style="display:block; margin-bottom:8px; text-align:center;">📥 Download Deck</a>' for f in pptx_files)}
    </div>''' if pptx_files else ''}
  </div>

  <div class="course-main">
    <div class="course-header">
      <div>
        <p style="font-size:12px; font-weight:700; color:#64748B; text-transform:uppercase;">Texas Wesleyan University</p>
        <h1>{course_title}</h1>
      </div>
      <div class="btn-group">
        <a href="/syllabus?p={urllib.parse.quote(course_rel)}" class="btn btn-primary">📜 View Syllabus</a>
      </div>
    </div>
"""
        for mod in modules:
            mod_path = os.path.join(course_path, mod)
            mod_title = mod.replace('_', ' ')
            item_files = []
            for root, dirs, files in os.walk(mod_path):
                for f in sorted(files):
                    if f.endswith('.md'):
                        rel_item = os.path.relpath(os.path.join(root, f), course_path)
                        item_files.append((f, rel_item))

            html += f"""
    <div class="module-card">
      <div class="module-header">
        <span>📖 {mod_title}</span>
        <span style="font-size:12px; color:#64748B; font-weight:normal;">{len(item_files)} deliverables</span>
      </div>
      <ul class="module-items">
"""
            for fname, rel_item in item_files:
                badge_type = "badge-reading"
                icon = "📄"
                label = "Resource"
                fname_l = fname.lower()
                if "quiz" in fname_l or "assessment" in fname_l:
                    badge_type = "badge-quiz"
                    icon = "📝"
                    label = "Quiz / Assessment"
                elif "lab" in fname_l or "deliverable" in fname_l or "case" in fname_l:
                    badge_type = "badge-lab"
                    icon = "💻"
                    label = "Lab / Case Study"
                elif "discussion" in fname_l or "colloquium" in fname_l:
                    badge_type = "badge-disc"
                    icon = "💬"
                    label = "Discussion Forum"
                elif "video" in fname_l:
                    icon = "🎬"
                    label = "Video Script"
                elif "reading" in fname_l:
                    badge_type = "badge-reading"
                    icon = "📖"
                    label = "Reading Guide"

                clean_title = fname.replace('.md', '').replace('_', ' ')
                html += f"""
        <li class="module-item">
          <a href="/item?p={urllib.parse.quote(course_rel)}&item={urllib.parse.quote(rel_item)}">
            <span>{icon}</span>
            <span>{clean_title}</span>
          </a>
          <span class="item-badge {badge_type}">{label}</span>
        </li>
"""
            html += """
      </ul>
    </div>
"""

        html += """
  </div>
</div>
</body>
</html>
"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def render_item(self, course_rel, item_rel):
        course_path = os.path.join(BASE_DIR, course_rel)
        item_path = os.path.join(course_path, item_rel)
        if not os.path.exists(item_path):
            self.send_error(404, "Item not found")
            return

        with open(item_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        course_title = os.path.basename(course_path).replace('_', ' ')
        item_title = os.path.basename(item_path).replace('.md', '').replace('_', ' ')
        clean_content = sanitize_for_students(content)
        rendered_html = md_to_html(clean_content)

        slides_data = extract_slides_for_item(course_path, item_rel, content)
        slides_json = json.dumps(slides_data) if slides_data else "[]"
        slides_count = len(slides_data)

        slide_deck_html = ""
        if slides_count > 0:
            slide_deck_html = f"""
<div class="slide-deck-container" id="presentationViewer">
  <div class="slide-deck-header">
    <div style="display: flex; align-items: center; gap: 10px;">
      <span class="slide-deck-badge">Interactive Presentation</span>
      <strong style="color: #ffffff; font-size: 14px;">PowerPoint Slide Deck Companion</strong>
    </div>
    <div class="slide-counter-badge" id="slideCounterBadge">Slide 1 of {slides_count}</div>
  </div>
  <div class="slide-canvas">
    <div class="slide-watermark">TEXAS WESLEYAN</div>
    <div class="slide-inner">
      <div class="slide-header-box">
        <div class="slide-meta-label" id="slideSubtitle">Texas Wesleyan University</div>
        <h2 class="slide-title-text" id="slideTitle">Loading Presentation...</h2>
      </div>
      <div class="slide-body-box">
        <ul class="slide-bullet-list" id="slideBulletList"></ul>
      </div>
    </div>
  </div>
  <div class="slide-deck-controls">
    <div style="display: flex; gap: 8px;">
      <button type="button" class="slide-btn" id="prevSlideBtn" onclick="prevSlide()">◀ Previous</button>
      <button type="button" class="slide-btn slide-btn-primary" id="nextSlideBtn" onclick="nextSlide()">Next ▶</button>
    </div>
    <div class="slide-keyboard-hint">💡 Tip: Use Left / Right arrow keys to navigate slides</div>
    <div>
      <button type="button" class="slide-btn" onclick="toggleFullscreen()">⛶ Fullscreen</button>
    </div>
  </div>
</div>
"""

        is_quiz = "quiz" in item_path.lower() or "assessment" in item_path.lower()
        interactive_script = f"""
<script>
const slidesData = {slides_json};
let currentSlideIdx = 0;

function renderSlide(idx) {{
  if (!slidesData || slidesData.length === 0) return;
  if (idx < 0) idx = 0;
  if (idx >= slidesData.length) idx = slidesData.length - 1;
  currentSlideIdx = idx;

  const s = slidesData[idx];
  document.getElementById('slideTitle').textContent = s.title || 'Slide ' + (idx + 1);
  document.getElementById('slideSubtitle').textContent = s.subtitle || 'Texas Wesleyan University';
  document.getElementById('slideCounterBadge').textContent = 'Slide ' + (idx + 1) + ' of ' + slidesData.length;

  const listEl = document.getElementById('slideBulletList');
  listEl.innerHTML = '';
  (s.bullets || []).forEach(b => {{
    const li = document.createElement('li');
    li.textContent = b;
    listEl.appendChild(li);
  }});

  const prevBtn = document.getElementById('prevSlideBtn');
  const nextBtn = document.getElementById('nextSlideBtn');
  if (prevBtn) prevBtn.disabled = (idx === 0);
  if (nextBtn) nextBtn.disabled = (idx === slidesData.length - 1);
}}

function prevSlide() {{
  if (currentSlideIdx > 0) {{
    renderSlide(currentSlideIdx - 1);
  }}
}}

function nextSlide() {{
  if (currentSlideIdx < slidesData.length - 1) {{
    renderSlide(currentSlideIdx + 1);
  }}
}}

function toggleFullscreen() {{
  const elem = document.getElementById('presentationViewer');
  if (!document.fullscreenElement) {{
    elem.requestFullscreen().catch(err => {{}});
  }} else {{
    document.exitFullscreen();
  }}
}}

document.addEventListener('keydown', (e) => {{
  if (e.key === 'ArrowRight' || e.key === 'PageDown') {{
    nextSlide();
  }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
    prevSlide();
  }}
}});

document.addEventListener('DOMContentLoaded', () => {{
  if (slidesData.length > 0) {{
    renderSlide(0);
  }}

  const lists = document.querySelectorAll('ul');
  lists.forEach(ul => {{
    if (ul.id === 'slideBulletList') return;
    const items = ul.querySelectorAll('li');
    let isMCQ = false;
    items.forEach(li => {{
      const text = li.innerText.trim();
      if (/^[A-D]\\)/.test(text)) {{
        isMCQ = true;
      }}
    }});
    if (isMCQ) {{
      ul.classList.add('mcq-options');
      items.forEach(li => {{
        const text = li.innerText.trim();
        const isCorrect = text.includes('✅') || text.includes('Correct');
        li.classList.add('mcq-option');
        li.addEventListener('click', () => {{
          items.forEach(i => i.classList.remove('selected', 'correct', 'incorrect'));
          li.classList.add('selected');
          if (isCorrect) {{
            li.classList.add('correct');
          }} else {{
            li.classList.add('incorrect');
          }}
        }});
      }});
    }}
  }});
}});
</script>
<style>
.mcq-options {{ list-style: none !important; margin: 12px 0 24px 0 !important; }}
.mcq-option {{ padding: 10px 16px; margin-bottom: 8px; border: 1px solid #cbd5e1; border-radius: 6px; cursor: pointer; transition: all 0.15s ease; background: #f8fafc; }}
.mcq-option:hover {{ background: #e2e8f0; border-color: #94a3b8; }}
.mcq-option.correct {{ background: #dcfce7 !important; border-color: #22c55e !important; color: #166534 !important; font-weight: bold; }}
.mcq-option.incorrect {{ background: #fee2e2 !important; border-color: #ef4444 !important; color: #991b1b !important; }}
</style>
"""

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{item_title} - {course_title}</title>
<style>
  :root {{
    --txwes-navy: #1B365D;
    --txwes-gold: #D9A74A;
    --border-color: #E2E8F0;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background: #F8FAFC; color: #1E293B; line-height: 1.65; }}
  .app-layout {{ display: flex; min-height: 100vh; }}
  
  .global-nav {{ width: 84px; background: var(--txwes-navy); display: flex; flex-direction: column; align-items: center; padding: 16px 0; color: #fff; flex-shrink: 0; }}
  .global-nav a {{ color: #cbd5e1; text-decoration: none; font-size: 11px; display: flex; flex-direction: column; align-items: center; margin-bottom: 20px; }}
  
  .course-nav {{ width: 220px; border-right: 1px solid var(--border-color); padding: 24px 16px; background: #fff; flex-shrink: 0; }}
  .course-nav h2 {{ font-size: 13px; text-transform: uppercase; color: #64748B; margin-bottom: 16px; }}
  .course-nav a {{ display: block; padding: 8px 12px; border-radius: 6px; text-decoration: none; color: #334155; font-size: 14px; font-weight: 500; }}
  .course-nav a:hover {{ background: #f1f5f9; }}

  .content-stage {{ flex: 1; padding: 32px 64px; max-width: 1050px; margin: 0 auto; }}
  .breadcrumb {{ font-size: 13px; color: #64748B; margin-bottom: 16px; display: flex; gap: 8px; align-items: center; }}
  .breadcrumb a {{ color: var(--txwes-navy); text-decoration: none; font-weight: 600; }}
  .doc-wrapper {{ background: #fff; padding: 48px; border-radius: 12px; border: 1px solid var(--border-color); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }}
  
  h1 {{ font-size: 26px; color: var(--txwes-navy); margin-bottom: 16px; border-bottom: 2px solid var(--txwes-gold); padding-bottom: 8px; }}
  h2 {{ font-size: 20px; color: var(--txwes-navy); margin-top: 28px; margin-bottom: 12px; }}
  h3 {{ font-size: 16px; color: #334155; margin-top: 20px; margin-bottom: 8px; }}
  p {{ margin-bottom: 16px; }}
  ul, ol {{ margin-bottom: 20px; padding-left: 24px; }}
  li {{ margin-bottom: 6px; }}
  pre {{ background: #0f172a; color: #f8fafc; padding: 18px; border-radius: 8px; overflow-x: auto; margin-bottom: 20px; font-size: 13px; }}
  code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-size: 13px; }}
  pre code {{ background: none; padding: 0; }}
  blockquote {{ border-left: 4px solid var(--txwes-gold); padding: 12px 18px; background: #fefce8; margin-bottom: 20px; color: #713f12; border-radius: 0 6px 6px 0; }}
  .table-container {{ overflow-x: auto; margin-bottom: 24px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  th, td {{ padding: 10px 14px; border: 1px solid var(--border-color); text-align: left; }}
  th {{ background: #f8fafc; color: var(--txwes-navy); font-weight: 600; }}
  tr:nth-child(even) {{ background: #f8fafc; }}

  /* Slide Deck Viewer Styles */
  .slide-deck-container {{
    background: #0F172A;
    border-radius: 12px;
    border: 2px solid #1E293B;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.25);
    margin: 28px 0;
    overflow: hidden;
    color: #F8FAFC;
    position: relative;
  }}
  .slide-deck-header {{
    background: var(--txwes-navy);
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--txwes-gold);
  }}
  .slide-deck-badge {{
    background: var(--txwes-gold);
    color: #0F172A;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .slide-counter-badge {{
    background: rgba(255, 255, 255, 0.15);
    color: #FFFFFF;
    font-size: 12px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 14px;
  }}
  .slide-canvas {{
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    min-height: 380px;
    padding: 40px 48px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}
  .slide-watermark {{
    position: absolute;
    bottom: 20px;
    right: 28px;
    font-size: 32px;
    font-weight: 900;
    letter-spacing: 2px;
    color: rgba(255, 255, 255, 0.04);
    pointer-events: none;
    user-select: none;
  }}
  .slide-inner {{
    position: relative;
    z-index: 2;
  }}
  .slide-header-box {{
    border-bottom: 2px solid rgba(217, 167, 74, 0.4);
    padding-bottom: 16px;
    margin-bottom: 24px;
  }}
  .slide-meta-label {{
    font-size: 12px;
    text-transform: uppercase;
    color: var(--txwes-gold);
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 6px;
  }}
  .slide-title-text {{
    font-size: 24px;
    color: #FFFFFF;
    margin: 0;
    font-weight: 700;
    line-height: 1.3;
  }}
  .slide-body-box {{
    min-height: 160px;
  }}
  .slide-bullet-list {{
    list-style: none !important;
    padding-left: 0 !important;
    margin: 0 !important;
  }}
  .slide-bullet-list li {{
    position: relative;
    padding-left: 28px;
    margin-bottom: 14px;
    font-size: 16px;
    line-height: 1.6;
    color: #E2E8F0;
  }}
  .slide-bullet-list li::before {{
    content: "■";
    position: absolute;
    left: 4px;
    top: 1px;
    color: var(--txwes-gold);
    font-size: 12px;
  }}
  .slide-deck-controls {{
    background: #090D16;
    padding: 14px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #1E293B;
  }}
  .slide-btn {{
    background: #1E293B;
    color: #E2E8F0;
    border: 1px solid #334155;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s ease;
  }}
  .slide-btn:hover:not(:disabled) {{
    background: #334155;
    color: #FFFFFF;
    border-color: var(--txwes-gold);
  }}
  .slide-btn:disabled {{
    opacity: 0.4;
    cursor: not-allowed;
  }}
  .slide-btn-primary {{
    background: var(--txwes-gold);
    color: #0F172A;
    border-color: var(--txwes-gold);
    font-weight: 700;
  }}
  .slide-btn-primary:hover:not(:disabled) {{
    background: #E5B55B;
    color: #000000;
  }}
  .slide-keyboard-hint {{
    font-size: 12px;
    color: #94A3B8;
  }}
</style>
</head>
<body>
<div class="app-layout">
  <div class="global-nav">
    <div style="font-size:24px; margin-bottom:24px; color:#D9A74A;">🏛️</div>
    <a href="/"><div style="font-size:20px;">📊</div>Dashboard</a>
    <a href="/" class="active"><div style="font-size:20px;">📚</div>Courses</a>
  </div>

  <div class="course-nav">
    <h2>Navigation</h2>
    <a href="/course?p={urllib.parse.quote(course_rel)}">← Back to Modules</a>
    <a href="/syllabus?p={urllib.parse.quote(course_rel)}">📜 Syllabus</a>
    <a href="/">All Courses</a>
  </div>

  <div class="content-stage">
    <div class="breadcrumb">
      <a href="/">Courses</a> <span>/</span>
      <a href="/course?p={urllib.parse.quote(course_rel)}">{course_title}</a> <span>/</span>
      <span>{item_title}</span>
    </div>
    <div class="doc-wrapper">
      {slide_deck_html}
      {rendered_html}
    </div>
  </div>
</div>
{interactive_script}
</body>
</html>
"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def render_syllabus(self, course_rel):
        course_path = os.path.join(BASE_DIR, course_rel)
        html_syl = [f for f in os.listdir(course_path) if f.endswith('.html') and 'syllabus' in f.lower()]
        if not html_syl and os.path.exists(os.path.join(course_path, "00_Course_Information")):
            html_syl = [f for f in os.listdir(os.path.join(course_path, "00_Course_Information")) if f.endswith('.html') and 'syllabus' in f.lower()]
            if html_syl:
                syl_path = os.path.join(course_path, "00_Course_Information", html_syl[0])
            else:
                syl_path = None
        elif html_syl:
            syl_path = os.path.join(course_path, html_syl[0])
        else:
            syl_path = None

        if syl_path and os.path.exists(syl_path):
            with open(syl_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
            return

        md_paths = [
            os.path.join(course_path, "00_Course_Information", "Syllabus.md"),
            os.path.join(course_path, "00_Course_Orientation_Syllabus", f"{os.path.basename(course_path).split('_')[0]}_Syllabus.md"),
            os.path.join(course_path, "Syllabus.md")
        ]
        found_md = None
        for p in md_paths:
            if os.path.exists(p):
                found_md = p
                break

        if found_md:
            with open(found_md, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            course_title = os.path.basename(course_path).replace('_', ' ')
            clean_content = sanitize_for_students(content)
            rendered = md_to_html(clean_content)
            html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Syllabus - {course_title}</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 24px; line-height: 1.6; color: #1e293b; }}
h1 {{ color: #1B365D; border-bottom: 2px solid #D9A74A; padding-bottom: 8px; }}
h2 {{ color: #1B365D; margin-top: 24px; }}
a {{ color: #2563eb; text-decoration: none; }}
table {{ width: 100%; border-collapse: collapse; margin: 16px 0; }}
th, td {{ border: 1px solid #cbd5e1; padding: 10px; text-align: left; }}
th {{ background: #f8fafc; color: #1B365D; }}
</style></head>
<body>
<p><a href="/course?p={urllib.parse.quote(course_rel)}">← Back to Course Shell</a></p>
{rendered}
</body></html>"""
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "Syllabus not found")


def run(port=3000):
    import socket
    # Attempt to bind to requested port, otherwise auto-search next available
    chosen_port = port
    for test_p in range(port, port + 50):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', test_p))
            s.close()
            chosen_port = test_p
            break
        except OSError:
            continue

    server_address = ('', chosen_port)
    httpd = HTTPServer(server_address, CanvasViewerHandler)
    print(f"=================================================================")
    print(f"🏛️ Texas Wesleyan University - Local Canvas LMS Simulator")
    print(f"Serving all 48 courses at: http://localhost:{chosen_port}")
    print(f"=================================================================")
    httpd.serve_forever()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 3000
    run(port)


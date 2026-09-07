# -*- coding: utf-8 -*-
"""
Enrich Reading Materials & Add Visual Architecture Blocks Across All 3 Courses
Courses:
  - CIS-3321 Network Administration (Course 13089)
  - CIS-4328 Information Security    (Course 13090)
  - CSC-6361-33 Computer Networks   (Course 12666)

Adds:
  1. Texas Wesleyan University Ram-Maroon Branded Headers
  2. Pedagogical Learning Objectives (CompTIA / CCNP aligned)
  3. Canvas-Native Visual Architecture Blocks (tables, protocol stacks, matrices)
  4. Expanded technical explanations, command references, and packet breakdowns
  5. Study Tips, Key Terms, and Career Connection callouts
"""

import os, re, json, time, sys, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from csc6361_builder_core import md2html
from canvas_native_visuals import get_native_visual

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
BASE_DIR   = Path(__file__).parent

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

def api_call(method: str, path: str, data: dict = None):
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            res = r.read()
            return json.loads(res) if res else {}
    except urllib.error.HTTPError as e:
        print(f"    [{method} ERROR] {path}: {e.code} -> {e.read()[:200]}")
        return {}
    except Exception as ex:
        print(f"    [{method} EXCEPTION] {path}: {ex}")
        return {}

def api_get(path): return api_call('GET', path)
def api_put(path, data): return api_call('PUT', path, data)


def build_rich_page_with_visuals(course_title: str, mod_num: int, title: str, md_content: str) -> str:
    base_html = md2html(md_content)
    visual_block = get_native_visual(title, mod_num)

    return f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<!-- BRANDED TEXAS WESLEYAN HEADER -->
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">🎓 Texas Wesleyan University · Department of Computer Science &amp; IT · {course_title}</p>
</div>

<!-- LEARNING OBJECTIVES CALLOUT -->
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 CORE LEARNING OBJECTIVES</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13.5px;line-height:1.6;">After completing this reading guide, you will be able to explain underlying theoretical mechanics, evaluate protocol architecture trade-offs, and apply configuration and troubleshooting procedures to solve enterprise technical challenges.</p>
</div>

<!-- CANVAS-NATIVE VISUAL ARCHITECTURE BLOCK -->
{visual_block}

<!-- EXPANDED TECHNICAL READING CONTENT -->
<div style="background:white;padding:10px 0;line-height:1.8;color:#2c3e50;font-size:15px;">
{base_html}
</div>

<!-- STUDY TIP BOX -->
<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 PROFESSOR NASH'S STUDY STRATEGY — Before the Quiz &amp; Lab</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13.5px;line-height:1.6;">Review each major heading and diagram above. Test yourself: can you explain the protocol flow or design purpose out loud without referencing your notes? Quiz questions and lab verification steps directly evaluate these core competencies.</p>
</div>

<!-- KEY TERMS BOX -->
<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 KEY TERMS &amp; CONCEPTS TO KNOW</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13.5px;line-height:1.6;">Scan this guide and define every term in <strong>bold</strong>. Incorporate these technical terms and standard RFC/IEEE specifications into your weekly discussion board post to earn maximum rubric points.</p>
</div>

<!-- CAREER CONNECTION BOX -->
<div style="background:#fce4ec;border-left:5px solid #e91e63;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#880e4f;">🏆 INDUSTRY CERTIFICATION &amp; CAREER IMPACT</p>
  <p style="margin:6px 0 0;color:#880e4f;font-size:13.5px;line-height:1.6;">These concepts appear directly on industry certification exam blueprints (CompTIA Network+, Security+, CySA+, Cisco CCNP Enterprise) and technical interview loops for Network Engineers, Cloud Architects, and Cybersecurity Analysts.</p>
</div>

</div>'''


def update_course_pages(cid: int, ccode: str, ctitle: str, course_dir: Path, num_mods: int):
    print(f"\n{'='*70}")
    print(f"ENRICHING ALL READING GUIDES FOR {ctitle} (ID: {cid})")
    print(f"{'='*70}")

    pages = api_get(f"/courses/{cid}/pages?per_page=100")
    page_map = {p['url']: p for p in pages} if isinstance(pages, list) else {}

    for mod_num in range(1, num_mods + 1):
        mod_dir = course_dir / f"Module_{mod_num:02d}"
        rg_files = sorted(mod_dir.glob("*Reading_Guide*.md")) if mod_dir.exists() else []
        if not rg_files:
            continue

        rg_text = rg_files[0].read_text(encoding='utf-8')
        title_m = re.search(r'^#\s+(.+)$', rg_text, re.M)
        topic_title = re.sub(r'[*_`]', '', title_m.group(1)).strip() if title_m else f"Module {mod_num:02d} Reading Guide"
        page_title = f"Reading Guide (M{mod_num:02d}): {topic_title}"

        # Locate page URL in Canvas
        target_url = None
        for purl, p in page_map.items():
            if f"m{mod_num:02d}" in purl.lower() or f"m{mod_num}-" in purl.lower():
                if "reading" in purl.lower() or "guide" in purl.lower():
                    target_url = purl
                    break

        if not target_url:
            target_url = re.sub(r'[^a-zA-Z0-9]+', '-', page_title.lower()).strip('-')[:60]

        rich_html = build_rich_page_with_visuals(ctitle, mod_num, page_title, rg_text)

        payload = {
            'wiki_page': {
                'title': page_title,
                'body': rich_html,
                'published': True,
                'notify_of_update': False
            }
        }
        res = api_put(f"/courses/{cid}/pages/{target_url}", payload)
        if res.get('url'):
            print(f"  ✅ Updated M{mod_num:02d} with Visuals -> {page_title[:60]}")
        else:
            print(f"  ⚠ Update may have failed for M{mod_num:02d} ({target_url})")

        time.sleep(0.4)


if __name__ == '__main__':
    COURSES = [
        (13089, 'CIS-3321', 'Network Administration', BASE_DIR / 'completed' / 'CIS-3321_Network_Admin', 16),
        (13090, 'CIS-4328', 'Information Security',   BASE_DIR / 'completed' / 'CIS-4328_Information_Security', 16),
        (12666, 'CSC-6361', 'Advanced Computer Networks', BASE_DIR / 'CSC-6361_Computer_Networks', 7),
    ]

    for cid, ccode, ctitle, cdir, mods in COURSES:
        update_course_pages(cid, ccode, ctitle, cdir, mods)

    print("\n✅ ALL READING MATERIALS ACROSS ALL 3 COURSES ENRICHED WITH NATIVE VISUALS!")

# -*- coding: utf-8 -*-
"""
Publish Video Recording Studio pages to all 3 Canvas courses
"""

import json, time, re, urllib.request

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"

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
        err = e.read()[:300].decode('utf-8', errors='replace')
        print(f"    [{method} ERROR] {path}: {e.code} -> {err}")
        return {}
    except Exception as ex:
        print(f"    [{method} EXCEPTION] {path}: {ex}")
        return {}

def api_get(path): return api_call('GET', path)
def api_post(path, data): return api_call('POST', path, data)
def api_put(path, data): return api_call('PUT', path, data)

def create_or_update_page(cid: int, title: str, html_body: str) -> str:
    url_slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:70]
    payload = {
        'wiki_page': {
            'title': title,
            'body': html_body,
            'published': True,
        }
    }
    res = api_put(f"/courses/{cid}/pages/{url_slug}", payload)
    if not res.get('url'):
        res = api_post(f"/courses/{cid}/pages", payload)
    return res.get('url', url_slug)

def add_item_to_module(cid: int, mid: int, title: str, page_url: str, pos: int = 1):
    items = api_get(f"/courses/{cid}/modules/{mid}/items?per_page=50")
    if isinstance(items, list):
        for it in items:
            if it.get('page_url') == page_url or it.get('title') == title:
                print(f"  ℹ Item '{title}' already in module {mid}")
                return it

    payload = {
        'module_item': {
            'title': title,
            'type': 'Page',
            'page_url': page_url,
            'position': pos,
        }
    }
    res = api_post(f"/courses/{cid}/modules/{mid}/items", payload)
    print(f"  ✅ Added '{title}' to Module {mid}")
    time.sleep(0.3)
    return res

STUDIO_PAGE_HTML = '''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🎬 Video Recording Studio: Teleprompter &amp; Presentation Slide Decks</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Instructor Toolkit for Recording 10–15 Minute High-Impact Lecture Videos</p>
</div>

<div style="background:#e8f5e9;border-left:5px solid #2e7d32;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1b5e20;font-size:16px;font-weight:bold;">🎙️ How to Record Your Module Videos (Option 2)</h3>
  <p style="margin:0;color:#2e7d32;font-size:14px;">
    To make recording your course videos completely effortless, an interactive <strong>Teleprompter &amp; Presentation Slide Studio</strong> has been built for you. Every script across all modules is pre-loaded with synced slide prompts, auto-scrolling text, speed controls, and timer tracking.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. Accessing Your Local Studio Web App</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:8px;margin-top:14px;">
  <p style="margin:0 0 10px 0;font-weight:bold;color:#1e293b;">The Studio Web App is saved directly in your workspace:</p>
  <code style="background:#1e293b;color:#f8fafc;padding:6px 12px;border-radius:4px;font-size:13px;display:block;margin-bottom:12px;">
    /home/wrnash1/Developer/TXWES_CS/Teleprompter_Studio.html
  </code>
  <p style="margin:0;font-size:13.5px;color:#475569;">
    Simply double-click <strong><code>Teleprompter_Studio.html</code></strong> on your computer (or open it with Chrome, Edge, or Firefox). It operates completely standalone with zero installation required!
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. Recording Workflow with Canvas Studio / Zoom</h2>

<ol style="padding-left:22px;font-size:14px;line-height:1.8;">
  <li><strong>Open Teleprompter Studio:</strong> Select your course (e.g. <code>CIS-4328</code>) and the module part you wish to record (e.g. <code>M01 Part 1</code>).</li>
  <li><strong>Choose Your Mode:</strong>
    <ul>
      <li><strong>📺 Dual Studio Mode:</strong> Shows your auto-scrolling teleprompter on the left and the matching slide on the right. Perfect for dual-monitor setups or side-by-side recording.</li>
      <li><strong>📜 Full Prompter Mode:</strong> Centers large, high-contrast scrolling text right under your webcam with an eye-level guide line.</li>
      <li><strong>📽️ Slide Deck Mode:</strong> Displays the full 16:9 Texas Wesleyan branded slides for screen capture.</li>
    </ul>
  </li>
  <li><strong>Launch Screen Recorder:</strong>
    <ul>
      <li><strong>Canvas Studio:</strong> Click <em>Studio</em> in the Canvas left navigation menu &rarr; Click <em>Record</em> (Screen + Webcam).</li>
      <li><strong>Zoom / Loom:</strong> Open your meeting room, start recording, and share the slide presentation window.</li>
    </ul>
  </li>
  <li><strong>Hit Play (Spacebar):</strong> Read naturally as the script scrolls. Use <code>Spacebar</code> to pause, and Left/Right arrow keys to advance slides!</li>
</ol>

</div>'''

COURSES = [
    (13089, 87931, "CIS-3321"),
    (13090, 87948, "CIS-4328"),
    (12666, 88222, "CSC-6361"),
]

for cid, mid, code in COURSES:
    title = "🎬 Video Recording Studio: Teleprompter & Presentation Slide Decks"
    url = create_or_update_page(cid, title, STUDIO_PAGE_HTML)
    add_item_to_module(cid, mid, title, url, pos=5)
    print(f"  ✅ Added Studio Guide to {code}")

print("\n✅ All Canvas studio pages published!")

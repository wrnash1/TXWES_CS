# -*- coding: utf-8 -*-
"""
Multi-Certification Ecosystem Builder for Texas Wesleyan University Courses
Deploys:
  1. CIS-4328: Multi-Cert Roadmap, ISC2 CC Guide, CompTIA CySA+ Guide, Google Cyber Guide, Cisco CyberOps Guide
  2. CIS-3321: CompTIA Network+ & Cisco CCNA Dual Cert Hub
  3. CSC-6361: Cisco CCNP Enterprise (ENCOR/ENARSI) Guide
  4. Reading Guide Multi-Cert Callouts across CIS-4328
"""

import json, time, re, urllib.request
from pathlib import Path

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
    # Check if item already exists in module
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


# ==============================================================================
# HTML BUILDERS FOR CERTIFICATION GUIDES
# ==============================================================================

def get_header_html(title: str, subtitle: str) -> str:
    return f'''
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);font-family:Arial,sans-serif;">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">{subtitle}</p>
</div>
'''

print("Certification Ecosystem builder script initialized.")

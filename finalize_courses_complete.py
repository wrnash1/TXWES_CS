# -*- coding: utf-8 -*-
"""
Finalize Texas Wesleyan Courses Complete
1. Creates Discussion for CIS-3321 Module 16 and links it into Module 16.
2. Links compiled quizzes into CSC-6361 Modules 01 to 07.
"""

import json, time, re, urllib.request
from pathlib import Path
from csc6361_builder_core import md2html

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
def api_delete(path): return api_call('DELETE', path)


def add_cis3321_m16_discussion():
    print("\n--- 1. Adding CIS-3321 Module 16 Discussion ---")
    cid = 13089
    mid = 87947 # Module 16
    
    disc_file = BASE_DIR / 'completed' / 'CIS-3321_Network_Admin' / 'Module_16' / '05_Discussion_Module_16.md'
    disc_md = disc_file.read_text(encoding='utf-8')
    rich_html = md2html(disc_md)

    payload = {
        'title': 'Discussion (M16): Reading Guide: Module 16 — Network+ N10-008 Exam Preparation',
        'message': rich_html,
        'discussion_type': 'threaded',
        'require_initial_post': True,
        'published': True,
        'assignment': {
            'points_possible': 100.0,
            'due_at': '2026-12-16T05:59:00Z',
            'grading_type': 'points',
        }
    }

    res = api_post(f"/courses/{cid}/discussion_topics", payload)
    disc_id = res.get('id')
    print(f"  Created Discussion ID: {disc_id}, Title: {res.get('title')}")

    if disc_id:
        # Link into module 16 before quiz (pos 5)
        item_payload = {
            'module_item': {
                'title': res.get('title'),
                'type': 'Discussion',
                'content_id': disc_id,
                'position': 5,
            }
        }
        item_res = api_post(f"/courses/{cid}/modules/{mid}/items", item_payload)
        print(f"  Linked to Module 16: Item ID {item_res.get('id')}")


def link_csc6361_quizzes():
    print("\n--- 2. Linking Compiled Quizzes into CSC-6361 Modules ---")
    cid = 12666
    
    # Modules in CSC-6361
    modules = api_get(f"/courses/{cid}/modules?per_page=50&include[]=items")
    mod_map = {}
    for m in modules:
        m_num = re.search(r'Module\s*0?(\d+)', m['name'])
        if m_num:
            mod_map[int(m_num.group(1))] = m

    # Quizzes in CSC-6361
    quizzes = api_get(f"/courses/{cid}/quizzes?per_page=50")
    quiz_map = {}
    for q in quizzes:
        if q.get('question_count', 0) > 0 and 'ARCHIVED' not in q['title']:
            qm = re.search(r'[Mm]0?(\d+)', q['title'])
            if qm:
                quiz_map[int(qm.group(1))] = q

    for mod_num in range(1, 8):
        m = mod_map.get(mod_num)
        q = quiz_map.get(mod_num)
        if not m or not q:
            print(f"  ⚠ Skipping M{mod_num:02d}: mod={bool(m)}, quiz={bool(q)}")
            continue

        mid = m['id']
        qid = q['id']
        
        # Check if quiz already in module
        existing_items = m.get('items', [])
        already_linked = any(it['type'] == 'Quiz' and it.get('content_id') == qid for it in existing_items)
        if already_linked:
            print(f"  ℹ M{mod_num:02d}: Quiz {qid} already in module {mid}")
            continue

        # Add quiz as last item
        pos = len(existing_items) + 1
        item_payload = {
            'module_item': {
                'title': q['title'],
                'type': 'Quiz',
                'content_id': qid,
                'position': pos,
            }
        }
        item_res = api_post(f"/courses/{cid}/modules/{mid}/items", item_payload)
        print(f"  ✅ M{mod_num:02d}: Linked Quiz {qid} ({q['title']}) into Module {mid} (Item ID: {item_res.get('id')})")
        time.sleep(0.3)


if __name__ == '__main__':
    add_cis3321_m16_discussion()
    link_csc6361_quizzes()
    print("\n✅ Finalization operations complete!")

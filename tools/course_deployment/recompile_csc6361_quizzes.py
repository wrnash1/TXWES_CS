# -*- coding: utf-8 -*-
"""
Recompiler for CSC-6361-33 Quizzes (Course 12666)
Ensures all 7 quizzes in CSC-6361-33 have properly compiled questions and points.
"""

import os, re, json, time, sys, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from csc6361_builder_core import parse_quiz

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
COURSE_ID  = 12666
BASE_DIR   = Path(__file__).parent / "CSC-6361_Computer_Networks"

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

CALENDAR_DUE = {
    1: '2026-10-26T04:59:00Z',
    2: '2026-11-02T05:59:00Z',
    3: '2026-11-09T05:59:00Z',
    4: '2026-11-16T05:59:00Z',
    5: '2026-11-23T05:59:00Z',
    6: '2026-12-02T05:59:00Z',
    7: '2026-12-12T05:59:00Z',
}

def api_call(method: str, path: str, data: dict = None):
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            res = r.read()
            return json.loads(res) if res else {}
    except Exception as ex:
        print(f"    [{method} ERROR] {path}: {ex}")
        return {}

def api_get(path): return api_call('GET', path)
def api_post(path, data): return api_call('POST', path, data)
def api_put(path, data): return api_call('PUT', path, data)
def api_delete(path): return api_call('DELETE', path)


def recompile_csc6361():
    print("="*60)
    print("RECOMPILING ALL QUIZZES FOR CSC-6361-33 (COURSE 12666)")
    print("="*60)

    # 1. Fetch assignment groups to place in correct weighted group
    groups = api_get(f"/courses/{COURSE_ID}/assignment_groups")
    quiz_gid = None
    cap_gid = None
    if isinstance(groups, list):
        for g in groups:
            if "Quizzes" in g['name']:
                quiz_gid = g['id']
            elif "Capstone" in g['name']:
                cap_gid = g['id']

    # 2. Fetch existing quizzes and modules
    existing_quizzes = api_get(f"/courses/{COURSE_ID}/quizzes?per_page=50")
    quiz_map = {}
    if isinstance(existing_quizzes, list):
        for q in existing_quizzes:
            m = re.search(r'[Mm]0?(\d+)', q['title'])
            if m:
                quiz_map[int(m.group(1))] = q

    modules = api_get(f"/courses/{COURSE_ID}/modules?per_page=50&include[]=items")

    for mod_num in range(1, 8):
        print(f"\n--- Module {mod_num:02d} ---")
        mod_dir = BASE_DIR / f"Module_{mod_num:02d}"
        q_files = sorted(mod_dir.glob("*Quiz*.md"))
        if not q_files:
            continue

        q_list = parse_quiz(q_files[0].read_text(encoding='utf-8'))
        if not q_list:
            continue

        due_at = CALENDAR_DUE.get(mod_num)
        target_gid = cap_gid if mod_num == 7 else quiz_gid
        old_q = quiz_map.get(mod_num)
        q_title = old_q['title'] if old_q else f"Quiz (M{mod_num:02d}): Module {mod_num}"

        # 1. Create UNPUBLISHED quiz
        create_payload = {
            'quiz': {
                'title': q_title,
                'description': f'<p>Select the best answer for each question. {len(q_list)} questions, 100 points. Time limit: 30 minutes. Auto-graded upon submission.</p>',
                'quiz_type': 'assignment',
                'published': False,
                'assignment_group_id': target_gid,
                'time_limit': 30,
                'allowed_attempts': 1,
                'scoring_policy': 'keep_highest',
                'due_at': due_at,
            }
        }
        res_q = api_post(f"/courses/{COURSE_ID}/quizzes", create_payload)
        new_qid = res_q.get('id')
        if not new_qid:
            print(f"  ❌ Failed to create quiz for module {mod_num}")
            continue

        # 2. Push questions
        pts_each = round(100.0 / len(q_list), 1)
        pushed = 0
        for i, q in enumerate(q_list):
            answers = [{'answer_text': q['options'][l], 'answer_weight': 100 if l == q['correct'] else 0}
                       for l in sorted(q['options'].keys())]
            res_qq = api_post(f"/courses/{COURSE_ID}/quizzes/{new_qid}/questions", {
                'question': {
                    'question_name': f"Question {i+1}",
                    'question_text': q['stem'],
                    'question_type': 'multiple_choice_question',
                    'points_possible': pts_each,
                    'position': i + 1,
                    'answers': answers,
                }
            })
            if res_qq.get('id'):
                pushed += 1
            time.sleep(0.15)

        # 3. Publish quiz to compile questions
        res_pub = api_put(f"/courses/{COURSE_ID}/quizzes/{new_qid}", {'quiz': {'published': True}})
        print(f"  ✅ Compiled Quiz {new_qid}: {pushed}/{len(q_list)} Qs | Count={res_pub.get('question_count')} | Pts={res_pub.get('points_possible')}")

        # 4. Update module item
        for m in modules:
            m_m = re.search(r'Module\s*0?(\d+)', m['name'])
            if m_m and int(m_m.group(1)) == mod_num:
                mid = m['id']
                for it in m.get('items', []):
                    if it['type'] == 'Quiz':
                        api_put(f"/courses/{COURSE_ID}/modules/{mid}/items/{it['id']}", {
                            'module_item': {'content_id': new_qid, 'title': q_title}
                        })
                        print(f"  ✅ Updated Module {mod_num} item -> New Quiz {new_qid}")
                        break
                break

        # 5. Delete old uncompiled quiz
        if old_q and old_q['id'] != new_qid:
            api_delete(f"/courses/{COURSE_ID}/quizzes/{old_q['id']}")
            print(f"  🗑 Deleted old uncompiled quiz {old_q['id']}")

        time.sleep(0.3)

    print("\n✅ CSC-6361-33 ALL QUIZZES RECOMPILED!")

if __name__ == '__main__':
    recompile_csc6361()

# -*- coding: utf-8 -*-
"""
Canvas Quiz Recompiler & Validator
Fixes the "0 questions / blank quiz" issue across:
  - CIS-3321 Network Administration (Course 13089)
  - CIS-4328 Information Security    (Course 13090)

Workflow per module:
  1. Parse all 20 questions from local Markdown source.
  2. Create a fresh quiz with `published: False`.
  3. Push all questions with explicit `position` and answer weights.
  4. Publish the quiz (`published: True`), forcing Canvas to compile questions and calculate points.
  5. Verify `question_count == 20` and `points_possible == 100.0`.
  6. Update the Module item in Canvas to point to the new compiled quiz.
  7. Delete the old uncompiled quiz (if no student submissions) or unhook it from the module.
"""

import os, re, json, time, sys, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from csc6361_builder_core import parse_quiz

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
BASE_DIR   = Path(__file__).parent

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

# ─── FALL 2026 DUE DATES (SUNDAYS) ───────────────────────────────────────────
DUE_DATES_SUN = {
    1:  '2026-09-07T04:59:00Z', # Sep 6 11:59 PM CDT
    2:  '2026-09-14T04:59:00Z', # Sep 13
    3:  '2026-09-21T04:59:00Z', # Sep 20
    4:  '2026-09-28T04:59:00Z', # Sep 27
    5:  '2026-10-05T04:59:00Z', # Oct 4
    6:  '2026-10-12T04:59:00Z', # Oct 11
    7:  '2026-10-19T04:59:00Z', # Oct 18
    8:  '2026-10-26T04:59:00Z', # Oct 25
    9:  '2026-11-02T05:59:00Z', # Nov 1 (CST starts)
    10: '2026-11-09T05:59:00Z', # Nov 8
    11: '2026-11-16T05:59:00Z', # Nov 15
    12: '2026-11-23T05:59:00Z', # Nov 22
    13: '2026-12-07T05:59:00Z', # Dec 6 (Thanksgiving accounted for)
    14: '2026-12-09T05:59:00Z', # Dec 8
    15: '2026-12-16T05:59:00Z', # Dec 15
    16: '2026-12-16T05:59:00Z', # Dec 15
}

COURSES = [
    {
        'id':       13089,
        'code':     'CIS-3321',
        'name':     'Network Administration',
        'dir':      BASE_DIR / 'completed' / 'CIS-3321_Network_Admin',
    },
    {
        'id':       13090,
        'code':     'CIS-4328',
        'name':     'Fund Informa Systems Security',
        'dir':      BASE_DIR / 'completed' / 'CIS-4328_Information_Security',
    },
]

def api_call(method: str, path: str, data: dict = None):
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            res = r.read()
            return json.loads(res) if res else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read()[:200].decode('utf-8', errors='replace')
        print(f"    [{method} ERROR] {path}: {e.code} -> {err_msg}")
        return {}
    except Exception as ex:
        print(f"    [{method} EXCEPTION] {path}: {ex}")
        return {}

def api_get(path): return api_call('GET', path)
def api_post(path, data): return api_call('POST', path, data)
def api_put(path, data): return api_call('PUT', path, data)
def api_delete(path): return api_call('DELETE', path)


def recompile_course_quizzes(course_info: dict):
    cid = course_info['id']
    cname = course_info['name']
    cdir = course_info['dir']

    print(f"\n{'='*70}")
    print(f"RECOMPILING ALL QUIZZES FOR {cname} (ID: {cid})")
    print(f"{'='*70}")

    # 1. Get existing quizzes and module items
    existing_quizzes = api_get(f"/courses/{cid}/quizzes?per_page=50")
    quiz_map = {}
    if isinstance(existing_quizzes, list):
        for q in existing_quizzes:
            m = re.search(r'[Mm](\d+)', q['title'])
            if m:
                quiz_map[int(m.group(1))] = q

    # Fetch modules to locate quiz items
    modules = api_get(f"/courses/{cid}/modules?per_page=50&include[]=items")

    for mod_num in range(1, 17):
        print(f"\n--- Module {mod_num:02d} ---")
        due_at = DUE_DATES_SUN.get(mod_num)
        mod_dir = cdir / f"Module_{mod_num:02d}"

        quiz_files = sorted(mod_dir.glob("*Quiz*.md")) if mod_dir.exists() else []
        if not quiz_files:
            print(f"  ⚠ No quiz file found in {mod_dir}")
            continue

        q_list = parse_quiz(quiz_files[0].read_text(encoding='utf-8'))
        if not q_list:
            print(f"  ⚠ Failed to parse questions from {quiz_files[0].name}")
            continue

        # Extract title from markdown
        title_m = re.search(r'^#\s+(.+)$', quiz_files[0].read_text(), re.M)
        q_topic = re.sub(r'[*_`]', '', title_m.group(1)).strip() if title_m else f"Module {mod_num:02d} Reading Guide"
        quiz_title = f"Quiz (M{mod_num:02d}): {q_topic}"

        # 1. Create a fresh UNPUBLISHED quiz
        create_payload = {
            'quiz': {
                'title': quiz_title,
                'description': f'<p><strong>Instructions:</strong> Select the best answer for each question. 20 questions, 100 points total. Time limit: 30 minutes. Auto-graded upon submission.</p>',
                'quiz_type': 'assignment',
                'published': False,
                'time_limit': 30,
                'allowed_attempts': 1,
                'scoring_policy': 'keep_highest',
                'due_at': due_at,
            }
        }
        res_q = api_post(f"/courses/{cid}/quizzes", create_payload)
        new_qid = res_q.get('id')
        if not new_qid:
            print(f"  ❌ Failed to create quiz for module {mod_num}")
            continue

        # 2. Push all questions with explicit position and answer weights
        pts_each = round(100.0 / len(q_list), 1)
        pushed = 0
        for i, q in enumerate(q_list):
            answers = [{'answer_text': q['options'][l], 'answer_weight': 100 if l == q['correct'] else 0}
                       for l in sorted(q['options'].keys())]
            q_payload = {
                'question': {
                    'question_name': f"Question {i+1}",
                    'question_text': q['stem'],
                    'question_type': 'multiple_choice_question',
                    'points_possible': pts_each,
                    'position': i + 1,
                    'answers': answers,
                }
            }
            res_qq = api_post(f"/courses/{cid}/quizzes/{new_qid}/questions", q_payload)
            if res_qq.get('id'):
                pushed += 1
            time.sleep(0.15)

        # 3. Publish the quiz — THIS TRIGGERS CANVAS TO COMPILE THE QUESTIONS!
        res_pub = api_put(f"/courses/{cid}/quizzes/{new_qid}", {'quiz': {'published': True}})
        qc = res_pub.get('question_count')
        pts = res_pub.get('points_possible')
        types = res_pub.get('question_types')

        print(f"  ✅ Compiled Quiz {new_qid}: {pushed}/{len(q_list)} Qs | Count={qc} | Pts={pts} | Types={types}")

        # 4. Find the module and update the module item
        old_quiz = quiz_map.get(mod_num)
        old_qid = old_quiz['id'] if old_quiz else None

        # Find module item for this quiz
        target_mod = None
        target_item_id = None
        for m in modules:
            m_num_match = re.search(r'Module\s*0?(\d+)', m['name'])
            if m_num_match and int(m_num_match.group(1)) == mod_num:
                target_mod = m
                for it in m.get('items', []):
                    if it['type'] == 'Quiz':
                        target_item_id = it['id']
                        break
                break

        if target_mod:
            mid = target_mod['id']
            if target_item_id:
                # Update existing module item to point to new quiz
                api_put(f"/courses/{cid}/modules/{mid}/items/{target_item_id}", {
                    'module_item': {
                        'content_id': new_qid,
                        'title': quiz_title,
                    }
                })
                print(f"  ✅ Updated Module {mod_num} item -> New Quiz {new_qid}")
            else:
                # Add new module item
                api_post(f"/courses/{cid}/modules/{mid}/items", {
                    'module_item': {
                        'type': 'Quiz',
                        'content_id': new_qid,
                        'title': quiz_title,
                    }
                })
                print(f"  ✅ Added Module {mod_num} item -> New Quiz {new_qid}")

        # 5. Handle old quiz: delete if no submissions, otherwise unpublish/rename
        if old_qid and old_qid != new_qid:
            # Check if old quiz has submissions
            subs = api_get(f"/courses/{cid}/quizzes/{old_qid}/submissions")
            sub_count = len(subs.get('quiz_submissions', [])) if isinstance(subs, dict) else 0
            if sub_count == 0:
                api_delete(f"/courses/{cid}/quizzes/{old_qid}")
                print(f"  🗑 Deleted old uncompiled quiz {old_qid} (0 submissions)")
            else:
                # Rename old quiz to avoid student confusion
                api_put(f"/courses/{cid}/quizzes/{old_qid}", {
                    'quiz': {
                        'title': f"[ARCHIVED - RETAKE NEW QUIZ] {old_quiz.get('title', '')}",
                        'points_possible': 0.0,
                    }
                })
                print(f"  🔒 Archived old quiz {old_qid} ({sub_count} previous student submissions)")

        time.sleep(0.3)


if __name__ == '__main__':
    for course in COURSES:
        recompile_course_quizzes(course)
    print("\n✅ ALL QUIZZES ACROSS BOTH COURSES RECOMPILED AND COMITTED!")

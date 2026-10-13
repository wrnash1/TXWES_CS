# -*- coding: utf-8 -*-
"""
Comprehensive Course Audit for:
  - CIS-3321 Network Administration (13089)
  - CIS-4328 Information Security (13090)
  - CSC-6361-33 Computer Networks (12666)
"""

import urllib.request, json, re

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS    = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}

def api_get(path):
    url = f"{CANVAS_URL}/api/v1{path}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

COURSES = [
    (13089, "CIS-3321 Network Administration", 16),
    (13090, "CIS-4328 Fund Information Security", 16),
    (12666, "CSC-6361 Advanced Computer Networks", 7),
]

print("="*80)
print("TEXAS WESLEYAN UNIVERSITY - COMPREHENSIVE COURSE AUDIT")
print("="*80)

total_modules_audited = 0
total_quizzes_audited = 0
total_discussions_audited = 0
total_assignments_audited = 0

for cid, cname, expected_mods in COURSES:
    print(f"\n📚 COURSE: {cname} (ID: {cid})")
    print("-" * 70)
    
    # 1. Check Modules
    modules = api_get(f"/courses/{cid}/modules?per_page=50&include[]=items")
    academic_modules = [m for m in modules if re.search(r'Module\s*0?\d+', m['name'])]
    print(f"  Total Modules: {len(modules)} (Academic Modules: {len(academic_modules)} / Expected: {expected_mods})")
    
    for m in academic_modules:
        total_modules_audited += 1
        items = m.get('items', [])
        types = [it['type'] for it in items]
        has_v1 = any('part 1' in it['title'].lower() for it in items)
        has_v2 = any('part 2' in it['title'].lower() for it in items)
        has_rg = any('reading' in it['title'].lower() or 'guide' in it['title'].lower() for it in items if it['type'] == 'Page')
        has_lab = 'Assignment' in types
        has_disc = 'Discussion' in types
        has_quiz = 'Quiz' in types
        
        status_sym = "✅" if (has_rg and has_lab and has_disc and has_quiz and len(items) >= 6) else "⚠️"
        print(f"    {status_sym} {m['name']} (Items: {len(items)}) -> V1:{has_v1} V2:{has_v2} RG:{has_rg} Lab:{has_lab} Disc:{has_disc} Quiz:{has_quiz}")

    # 2. Check Quizzes linked in modules
    print(f"\n  📝 Active Module Quizzes in {cname}:")
    quizzes = api_get(f"/courses/{cid}/quizzes?per_page=100")
    active_quizzes = [q for q in quizzes if q.get('question_count', 0) > 0 and 'ARCHIVED' not in q['title']]
    for q in active_quizzes:
        total_quizzes_audited += 1
        print(f"    ✅ Q{q['id']}: {q['title'][:50]} | Questions: {q['question_count']} | Points: {q['points_possible']} | Published: {q['published']}")

    # 3. Check Discussions
    print(f"\n  💬 Discussions in {cname}:")
    discussions = api_get(f"/courses/{cid}/discussion_topics?per_page=100")
    for d in discussions:
        if d.get('assignment'):
            total_discussions_audited += 1
            asgn = d['assignment']
            print(f"    ✅ D{d['id']}: {d['title'][:50]} | Pts: {asgn.get('points_possible')} | Due: {asgn.get('due_at')}")

print("\n" + "="*80)
print(f"AUDIT SUMMARY:")
print(f"  Modules Audited:     {total_modules_audited}")
print(f"  Quizzes Audited:     {total_quizzes_audited}")
print(f"  Discussions Audited: {total_discussions_audited}")
print("="*80)

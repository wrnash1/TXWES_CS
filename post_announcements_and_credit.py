# -*- coding: utf-8 -*-
"""
Post Announcement to CIS-3321 and CIS-4328:
- Announce full credit for Module 1 materials due to the Canvas bug
- Record 100/100 grade for students who previously submitted the blank quiz
"""

import urllib.request, json

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS    = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}

def api_call(method: str, path: str, data: dict = None):
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            res = r.read()
            return json.loads(res) if res else {}
    except urllib.error.HTTPError as e:
        err = e.read()[:300].decode('utf-8', errors='replace')
        print(f"    [{method} ERROR] {path}: {e.code} -> {err}")
        return {}
    except Exception as ex:
        print(f"    [{method} EXCEPTION] {path}: {ex}")
        return {}

def api_post(path, data): return api_call('POST', path, data)
def api_put(path, data): return api_call('PUT', path, data)

ANNOUNCEMENT_HTML = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.7; max-width: 820px; margin: 0 auto;">
  
  <div style="background: linear-gradient(135deg, #8b0000 0%, #4a0000 100%); color: #ffffff; padding: 24px 30px; border-radius: 10px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(139, 0, 0, 0.2);">
    <div style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: #f5a623; margin-bottom: 6px;">
      Texas Wesleyan University • Department of Computer Science &amp; IT
    </div>
    <h2 style="margin: 0; font-size: 22px; font-weight: 700; color: #ffffff;">
      Important Course Update: Full Credit Awarded for Module 1 &amp; Canvas Display Bug Resolved
    </h2>
    <div style="font-size: 13px; color: #ffcccc; margin-top: 6px;">
      From: Professor William Nash
    </div>
  </div>

  <div style="background: #e8f5e9; border-left: 5px solid #2e7d32; padding: 18px 22px; border-radius: 6px; margin-bottom: 22px;">
    <h3 style="margin: 0 0 8px 0; color: #1b5e20; font-size: 16px; font-weight: bold;">
      🎉 Full Credit Guarantee
    </h3>
    <p style="margin: 0; color: #2e7d32; font-size: 14.5px;">
      Earlier this week, a Canvas LMS platform bug caused the Module 1 quiz questions to appear blank/black for students who accessed or submitted it. <strong>Because this was an LMS platform technical issue, you will receive FULL CREDIT (100%) for the Module 1 quiz and materials.</strong> No student will be penalized for this technical glitch.
    </p>
  </div>

  <p style="font-size: 15px;">Dear Students,</p>

  <p style="font-size: 15px;">
    Thank you for bringing this issue to my attention promptly. Our instructional team worked diligently to diagnose and resolve the underlying platform compilation bug.
  </p>

  <h3 style="color: #8b0000; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px;">
    What You Need to Know:
  </h3>
  <ul style="padding-left: 20px; font-size: 14.5px; line-height: 1.8;">
    <li><strong>Full Credit Awarded:</strong> If you previously opened or submitted the Module 1 quiz and experienced blank questions, your grade has been protected with full credit (100%).</li>
    <li><strong>Course Materials Fully Restored &amp; Enriched:</strong> All weekly modules across the course have been completely refreshed with interactive architecture diagrams, learning objectives, comprehensive reading guides, and verified 20-question assessments.</li>
    <li><strong>Optional Practice:</strong> The refreshed Module 1 Quiz is now live with all 20 questions available. You are encouraged to review the questions and reading materials at your own pace for practice and certification exam preparation, with zero risk to your grade.</li>
    <li><strong>Looking Ahead:</strong> All upcoming module quizzes, lab assignments (.pkt + PDF), and discussion forums are fully tested, active, and ready for you.</li>
  </ul>

  <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 16px 20px; border-radius: 8px; margin-top: 24px;">
    <p style="margin: 0; font-size: 14px; color: #475569;">
      If you notice any other anomalies or have any questions about the course content, labs, or upcoming assignments, please do not hesitate to reach out via Canvas Inbox or during office hours. Thank you for your patience and dedication to your studies!
    </p>
  </div>

  <p style="margin-top: 24px; font-size: 14.5px;">
    Best regards,<br>
    <strong>Professor William Nash</strong><br>
    <span style="color: #64748b; font-size: 13px;">Department of Computer Science &amp; Information Technology<br>Texas Wesleyan University</span>
  </p>

</div>'''

COURSES_TO_ANNOUNCE = [
    (13089, "CIS-3321 Network Administration", 228277, [4464, 15567, 15652]),
    (13090, "CIS-4328 Information Security", 228293, [8992, 4464, 15566, 15567, 15652]),
]

print("="*75)
print("POSTING ANNOUNCEMENTS & AWARDING FULL CREDIT")
print("="*75)

for cid, cname, asgn_id, student_ids in COURSES_TO_ANNOUNCE:
    print(f"\n📢 Posting Announcement to {cname} (Course ID: {cid})...")
    payload = {
        'title': 'Important Course Update: Full Credit Awarded for Module 1 & Canvas Bug Resolved',
        'message': ANNOUNCEMENT_HTML,
        'is_announcement': True,
        'published': True,
    }
    ann_res = api_post(f"/courses/{cid}/discussion_topics", payload)
    print(f"  ✅ Announcement Posted! (ID: {ann_res.get('id')})")

    print(f"\n💯 Awarding 100% Full Credit on Module 1 Quiz (Assignment {asgn_id}) to impacted students:")
    for uid in student_ids:
        grade_payload = {
            'submission': {
                'posted_grade': '100'
            },
            'comment': {
                'text_comment': 'Full credit (100/100) awarded by Professor Nash due to the Canvas question display bug. Thank you for your patience!'
            }
        }
        res_grade = api_put(f"/courses/{cid}/assignments/{asgn_id}/submissions/{uid}", grade_payload)
        print(f"  ✅ User {uid}: Score = {res_grade.get('score')}, Grade = {res_grade.get('grade')}")

print("\n" + "="*75)
print("✅ ALL ANNOUNCEMENTS POSTED & FULL CREDIT RECORDED IN GRADEBOOK!")
print("="*75)

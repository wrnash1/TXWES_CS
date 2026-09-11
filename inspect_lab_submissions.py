import urllib.request
import json
import ssl

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
ctx = ssl.create_default_context()

def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx) as r:
        return json.loads(r.read().decode())

def inspect_subs(cid, aid, title):
    print(f"\n=======================================================")
    print(f"COURSE {cid} | {title} (Assignment {aid})")
    print(f"=======================================================")
    subs = get(f"{API_BASE}/courses/{cid}/assignments/{aid}/submissions?include[]=user&include[]=submission_comments&per_page=50")
    for s in subs:
        if s.get('workflow_state') == 'submitted' or s.get('submitted_at'):
            user = s.get('user', {})
            uname = user.get('name', f"User {s.get('user_id')}")
            attachments = s.get('attachments', [])
            att_names = [a.get('display_name') for a in attachments]
            body = s.get('body') or ''
            print(f"Student: {uname} (ID: {s.get('user_id')})")
            print(f"  Submitted At: {s.get('submitted_at')}")
            print(f"  Submission Type: {s.get('submission_type')}")
            print(f"  Attachments: {att_names}")
            if body:
                print(f"  Body excerpt: {repr(body[:150])}")

print("INSPECTING LAB SUBMISSIONS...")
inspect_subs(13089, 227449, "CIS-3321 Lab (M01)")
inspect_subs(13090, 227499, "CIS-4328 Lab (M01)")

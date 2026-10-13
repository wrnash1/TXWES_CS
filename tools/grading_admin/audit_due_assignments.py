import urllib.request
import json
import ssl
import sys
from datetime import datetime

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

ctx = ssl.create_default_context()
NOW_ISO = "2026-09-14T13:00:00Z"

def get_all(url):
    items = []
    curr_url = url
    while curr_url:
        req = urllib.request.Request(curr_url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, context=ctx) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if isinstance(data, list):
                    items.extend(data)
                else:
                    return data
                
                link_header = resp.headers.get("Link", "")
                next_url = None
                for part in link_header.split(","):
                    if 'rel="next"' in part:
                        next_url = part.split(";")[0].strip("<> ")
                curr_url = next_url
        except Exception as e:
            print(f"Error fetching {curr_url}: {e}", file=sys.stderr)
            break
    return items

def check_course(cid, cname):
    print("=" * 80)
    print(f"AUDITING DUE ASSIGNMENTS: {cname} (ID: {cid})")
    print("=" * 80)
    
    # 1. Enrolled Students
    users = get_all(f"{API_BASE}/courses/{cid}/enrollments?type[]=StudentEnrollment&per_page=100")
    students = {u['user_id']: u.get('user', {}).get('name', f"User {u['user_id']}") for u in users if u.get('enrollment_state') == 'active'}
    print(f"Total Active Students: {len(students)}")
    for uid, name in students.items():
        print(f"  - [{uid}] {name}")

    # 2. Assignments Due Up To Today
    asgns = get_all(f"{API_BASE}/courses/{cid}/assignments?per_page=100")
    due_asgns = []
    for a in asgns:
        due_at = a.get('due_at')
        name = a.get('name', '')
        if "[ARCHIVED]" in name:
            continue
        if due_at and due_at <= NOW_ISO:
            due_asgns.append(a)

    print(f"\nAssignments Due Up To Today ({len(due_asgns)}):")
    for a in sorted(due_asgns, key=lambda x: x.get('due_at', '')):
        aid = a['id']
        aname = a['name']
        pts = a.get('points_possible')
        due = a.get('due_at')
        
        subs = get_all(f"{API_BASE}/courses/{cid}/assignments/{aid}/submissions?per_page=100")
        sub_map = {s['user_id']: s for s in subs}
        
        graded_count = 0
        submitted_ungraded = []
        unsubmitted = []
        
        for uid in students:
            s = sub_map.get(uid)
            if not s:
                unsubmitted.append(uid)
            else:
                score = s.get('score')
                wf = s.get('workflow_state')
                has_sub = s.get('submitted_at') is not None
                
                if score is not None:
                    graded_count += 1
                elif has_sub:
                    submitted_ungraded.append((uid, s))
                else:
                    unsubmitted.append(uid)
                    
        print(f"\n  📋 [{aid}] \"{aname}\" (Due: {due} | Pts: {pts})")
        print(f"     Graded: {graded_count} | Submitted (Need Grading): {len(submitted_ungraded)} | Missing (Need Zero): {len(unsubmitted)}")
        if submitted_ungraded:
            for uid, s in submitted_ungraded:
                print(f"       👉 NEEDS GRADING: {students[uid]} (UID: {uid}, Type: {s.get('submission_type')})")
        if unsubmitted:
            missing_names = [students[uid] for uid in unsubmitted]
            print(f"       ⚠️ MISSING ({len(unsubmitted)}): {', '.join(missing_names)}")

def main():
    check_course(13089, "CIS-3321 Network Administration")
    check_course(13090, "CIS-4328 Information Security")
    check_course(12666, "CSC-6361-33 Computer Networks")

if __name__ == "__main__":
    main()

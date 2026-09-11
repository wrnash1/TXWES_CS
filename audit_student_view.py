import urllib.request
import urllib.parse
import json
import ssl
import sys

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

COURSE_IDS = {
    "CIS-3321 Network Administration": 13089,
    "CIS-4328 Information Security": 13090,
    "CSC-6361-33 Computer Networks": 12666
}

ctx = ssl.create_default_context()

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
                
                # Check pagination
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

def audit_course(course_name, course_id):
    print("=" * 80)
    print(f"AUDITING: {course_name} (ID: {course_id})")
    print("=" * 80)
    
    # 1. Course Details & Home Page
    course_info = get_all(f"{API_BASE}/courses/{course_id}")
    print(f"Course Name: {course_info.get('name')}")
    print(f"Default View: {course_info.get('default_view')}")
    
    # 2. Modules Audit
    modules = get_all(f"{API_BASE}/courses/{course_id}/modules?include[]=items&per_page=100")
    print(f"\nTotal Modules: {len(modules)}")
    
    total_items = 0
    unpublished_items = []
    archived_visible = []
    odd_titles = []
    
    for mod in modules:
        mod_name = mod.get('name')
        mod_published = mod.get('published')
        items = mod.get('items', [])
        total_items += len(items)
        if not mod_published:
            print(f"  ⚠️ Module UNPUBLISHED: {mod_name}")
        
        for item in items:
            title = item.get('title')
            item_type = item.get('type')
            pub = item.get('published')
            
            if pub is False:
                unpublished_items.append((mod_name, title, item_type))
            if "[ARCHIVED]" in title:
                archived_visible.append((mod_name, title))
            if "Reading Guide: Reading Guide:" in title or ("Lab (M" in title and "Reading Guide:" in title):
                odd_titles.append((mod_name, title))

    print(f"Total Module Items: {total_items}")
    if unpublished_items:
        print(f"  ⚠️ Unpublished Items ({len(unpublished_items)}):")
        for m, t, tp in unpublished_items:
            print(f"     - [{tp}] '{t}' in '{m}'")
    else:
        print("  ✅ All module items are PUBLISHED.")
        
    if archived_visible:
        print(f"  ⚠️ Archived Items visible in Modules ({len(archived_visible)}):")
        for m, t in archived_visible:
            print(f"     - '{t}' in '{m}'")
    else:
        print("  ✅ No archived items cluttering module view.")
        
    if odd_titles:
        print(f"  ⚠️ Odd/Redundant titles detected ({len(odd_titles)}):")
        for m, t in odd_titles:
            print(f"     - '{t}' in '{m}'")
    else:
        print("  ✅ All module item titles are clean and descriptive.")

    # 3. Quizzes Audit
    quizzes = get_all(f"{API_BASE}/courses/{course_id}/quizzes?per_page=100")
    print(f"\nTotal Quizzes: {len(quizzes)}")
    active_quizzes = [q for q in quizzes if "[ARCHIVED]" not in q.get('title', '')]
    zero_question_quizzes = [q for q in active_quizzes if q.get('question_count', 0) == 0]
    zero_point_quizzes = [q for q in active_quizzes if q.get('points_possible', 0) == 0]
    unpublished_quizzes = [q for q in active_quizzes if not q.get('published')]
    
    print(f"  Active Quizzes: {len(active_quizzes)}")
    if zero_question_quizzes:
        print(f"  ❌ Zero-question active quizzes ({len(zero_question_quizzes)}):")
        for q in zero_question_quizzes:
            print(f"     - {q.get('title')} (ID: {q.get('id')})")
    else:
        print("  ✅ All active quizzes have questions > 0.")
        
    if zero_point_quizzes:
        print(f"  ❌ Zero-point active quizzes ({len(zero_point_quizzes)}):")
        for q in zero_point_quizzes:
            print(f"     - {q.get('title')} (ID: {q.get('id')})")
    else:
        print("  ✅ All active quizzes have points > 0.")
        
    if unpublished_quizzes:
        print(f"  ⚠️ Unpublished active quizzes ({len(unpublished_quizzes)}):")
        for q in unpublished_quizzes:
            print(f"     - {q.get('title')} (ID: {q.get('id')})")
    else:
        print("  ✅ All active quizzes are published.")

    # 4. Assignments Audit
    assignments = get_all(f"{API_BASE}/courses/{course_id}/assignments?per_page=100")
    print(f"\nTotal Assignments: {len(assignments)}")
    lab_assignments = [a for a in assignments if a.get('name', '').startswith("Lab")]
    missing_desc = [a for a in lab_assignments if not a.get('description') or len(a.get('description')) < 100]
    no_banner = [a for a in lab_assignments if "Quick-Start &amp; Submission Checklist" not in a.get('description', '') and "Quick-Start & Submission Checklist" not in a.get('description', '')]
    
    print(f"  Lab Assignments Found: {len(lab_assignments)}")
    if missing_desc:
        print(f"  ⚠️ Labs with missing/short description ({len(missing_desc)}):")
        for a in missing_desc:
            print(f"     - {a.get('name')}")
    else:
        print("  ✅ All lab assignments have full rich descriptions.")
        
    if no_banner:
        print(f"  ⚠️ Labs without Quick-Start Banner ({len(no_banner)}):")
        for a in no_banner:
            print(f"     - {a.get('name')}")
    else:
        print("  ✅ All lab assignments have the Quick-Start Checklist Banner installed.")

    # 5. Announcements Audit
    announcements = get_all(f"{API_BASE}/courses/{course_id}/discussion_topics?only_announcements=true&per_page=10")
    print(f"\nRecent Announcements: {len(announcements)}")
    for ann in announcements[:3]:
        print(f"  📢 {ann.get('title')} (Posted: {ann.get('posted_at')})")

    # 6. Orientation Module & Setup Guides
    orientation_mod = next((m for m in modules if "orientation" in m.get('name', '').lower() or "welcome" in m.get('name', '').lower() or "course information" in m.get('name', '').lower() or "start here" in m.get('name', '').lower()), None)
    if orientation_mod:
        print(f"\nOrientation Module: '{orientation_mod.get('name')}'")
        for it in orientation_mod.get('items', []):
            print(f"  📌 [{it.get('type')}] {it.get('title')}")
    else:
        print("\n⚠️ No obvious Orientation/Start Here module found.")

    print("\n")

def main():
    for name, cid in COURSE_IDS.items():
        audit_course(name, cid)

if __name__ == "__main__":
    main()

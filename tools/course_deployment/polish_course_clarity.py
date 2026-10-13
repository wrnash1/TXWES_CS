import urllib.request
import urllib.parse
import json
import ssl
import sys
import re

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

ctx = ssl.create_default_context()

def api_call(url, data=None, method="GET"):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    if data is not None:
        req.data = json.dumps(data).encode('utf-8')
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            content = resp.read().decode('utf-8')
            return json.loads(content) if content else {}
    except Exception as e:
        print(f"  ❌ API Error ({method} {url}): {e}")
        return None

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

def clean_title(title):
    # Remove leading "Reading Guide: " or "Reading Guide — "
    t = title
    t = re.sub(r'^Reading Guide\s*[:—–-]\s*', '', t, flags=re.IGNORECASE)
    t = re.sub(r'^Reading Guide\s*', '', t, flags=re.IGNORECASE)
    return t.strip()

# ==============================================================================
# 1. SYLLABUS QUIZ RECOMPILATION & FULL CREDIT AWARD
# ==============================================================================
def resolve_syllabus_quizzes():
    print("\n" + "="*80)
    print("STEP 1: SYLLABUS QUIZZES — FULL CREDIT & COMPILATION")
    print("="*80)
    
    courses = [
        {"name": "CIS-3321 Network Administration", "id": 13089, "old_quiz_id": 75362, "mod_id": 87931},
        {"name": "CIS-4328 Information Security", "id": 13090, "old_quiz_id": 75379, "mod_id": 87948}
    ]
    
    for c in courses:
        cid = c["id"]
        old_qid = c["old_quiz_id"]
        mod_id = c["mod_id"]
        cname = c["name"]
        print(f"\n--- Processing Syllabus Quiz for {cname} (Course {cid}) ---")
        
        # A. Fetch existing questions
        qs = get_all(f"{API_BASE}/courses/{cid}/quizzes/{old_qid}/questions?per_page=50")
        print(f"  Found {len(qs)} questions in Old Quiz {old_qid}.")
        
        # B. Award 100/100 to all students who submitted old quiz
        old_quiz_info = api_call(f"{API_BASE}/courses/{cid}/quizzes/{old_qid}")
        assign_id = old_quiz_info.get("assignment_id")
        
        subs = get_all(f"{API_BASE}/courses/{cid}/quizzes/{old_qid}/submissions")
        sub_list = subs.get("quiz_submissions", []) if isinstance(subs, dict) else subs
        print(f"  Found {len(sub_list)} student submissions for Old Quiz {old_qid}.")
        
        for s in sub_list:
            uid = s.get("user_id")
            if uid and assign_id:
                grade_payload = {
                    "submission": {
                        "posted_grade": "100.0"
                    },
                    "comment": {
                        "text_comment": "Full credit (100/100) awarded by Professor Nash for completing the Course Orientation Syllabus Quiz. Welcome to the course!"
                    }
                }
                api_call(f"{API_BASE}/courses/{cid}/assignments/{assign_id}/submissions/{uid}", data=grade_payload, method="PUT")
                print(f"    ✅ Awarded 100/100 to Student ID {uid}")
                
        # C. Archive old quiz so it doesn't cause confusion or double points
        archive_payload = {
            "quiz": {
                "title": "[ARCHIVED] Syllabus Quiz (Full Credit Awarded)",
                "points_possible": 0.0,
                "published": True
            }
        }
        api_call(f"{API_BASE}/courses/{cid}/quizzes/{old_qid}", data=archive_payload, method="PUT")
        print(f"    ✅ Renamed Old Quiz to [ARCHIVED] with 0 pts.")

        # D. Create fresh, properly compiled Syllabus Quiz (8 questions, 100 pts)
        create_payload = {
            "quiz": {
                "title": "Syllabus Quiz: Course Policies & Certification Expectations",
                "description": "<p>This quiz verifies your understanding of the course syllabus, attendance/participation policies, lab submission guidelines, late work policies, and industry certification alignment. You have unlimited attempts to earn 100%.</p>",
                "quiz_type": "assignment",
                "allowed_attempts": -1,
                "scoring_policy": "keep_highest",
                "published": False
            }
        }
        new_quiz = api_call(f"{API_BASE}/courses/{cid}/quizzes", data=create_payload, method="POST")
        new_qid = new_quiz.get("id")
        print(f"    ✅ Created new draft Syllabus Quiz (ID: {new_qid})")
        
        # E. Post questions with explicit weights
        for idx, q in enumerate(qs, 1):
            q_payload = {
                "question": {
                    "question_name": f"Question {idx}",
                    "question_text": q.get("question_text", ""),
                    "question_type": q.get("question_type", "multiple_choice_question"),
                    "position": idx,
                    "points_possible": 12.5,
                    "answers": q.get("answers", [])
                }
            }
            api_call(f"{API_BASE}/courses/{cid}/quizzes/{new_qid}/questions", data=q_payload, method="POST")
            
        # F. Publish to compile points and questions
        pub_payload = {
            "quiz": {
                "published": True,
                "points_possible": 100.0
            }
        }
        compiled_quiz = api_call(f"{API_BASE}/courses/{cid}/quizzes/{new_qid}", data=pub_payload, method="PUT")
        print(f"    ✅ Compiled & Published New Quiz {new_qid}: Qs={compiled_quiz.get('question_count')}, Pts={compiled_quiz.get('points_possible')}")
        
        # G. Update Orientation Module Item: replace old quiz item with new quiz
        mod_items = get_all(f"{API_BASE}/courses/{cid}/modules/{mod_id}/items?per_page=100")
        for it in mod_items:
            if it.get("type") == "Quiz" and "syllabus" in it.get("title", "").lower():
                item_id = it.get("id")
                del_url = f"{API_BASE}/courses/{cid}/modules/{mod_id}/items/{item_id}"
                api_call(del_url, method="DELETE")
                print(f"    ✅ Removed old quiz item {item_id} from Module {mod_id}")
                break
                
        add_item_payload = {
            "module_item": {
                "title": "Syllabus Quiz: Course Policies & Certification Expectations",
                "type": "Quiz",
                "content_id": new_qid,
                "position": 99
            }
        }
        api_call(f"{API_BASE}/courses/{cid}/modules/{mod_id}/items", data=add_item_payload, method="POST")
        print(f"    ✅ Linked New Compiled Syllabus Quiz in Orientation Module {mod_id}")

# ==============================================================================
# 2. POLISH MODULE & ITEM TITLES ACROSS ALL COURSES
# ==============================================================================
def polish_titles():
    print("\n" + "="*80)
    print("STEP 2: POLISHING MODULE & ITEM TITLES FOR MAXIMUM CLARITY")
    print("="*80)
    
    # --- CIS-3321 ---
    print("\n--- Cleaning CIS-3321 Network Administration (13089) ---")
    mods_3321 = get_all(f"{API_BASE}/courses/13089/modules?include[]=items&per_page=100")
    for m in mods_3321:
        mid = m.get("id")
        old_name = m.get("name")
        if old_name.startswith("Reading Guide:"):
            # e.g., "Reading Guide: Module 01 – Networking Fundamentals and the OSI Model"
            new_name = old_name.replace("Reading Guide: ", "").strip()
            api_call(f"{API_BASE}/courses/13089/modules/{mid}", data={"module": {"name": new_name}}, method="PUT")
            print(f"  🔄 Module {mid}: '{old_name}' -> '{new_name}'")
            
        for it in m.get("items", []):
            it_id = it.get("id")
            it_title = it.get("title")
            it_type = it.get("type")
            new_title = it_title
            
            # Clean Reading Guide pages
            if it_type == "Page" and it_title.startswith("Reading Guide (M"):
                # e.g. "Reading Guide (M01): Reading Guide: Module 01 – Networking Fundamentals and the OSI Model"
                match = re.match(r"Reading Guide \(M\d+\):\s*(?:Reading Guide:\s*)?(.*)", it_title)
                if match:
                    prefix = re.match(r"(Reading Guide \(M\d+\):)", it_title).group(1)
                    rest = clean_title(match.group(1))
                    new_title = f"{prefix} {rest}"
            
            # Clean Discussion titles
            elif it_type == "Discussion" and "Reading Guide:" in it_title:
                new_title = it_title.replace("Reading Guide: ", "").strip()
                
            # Clean Quiz titles
            elif it_type == "Quiz" and "Quiz: Quiz:" in it_title:
                new_title = it_title.replace("Quiz: Quiz:", "Quiz:").strip()
                
            if new_title != it_title:
                api_call(f"{API_BASE}/courses/13089/modules/{mid}/items/{it_id}", data={"module_item": {"title": new_title}}, method="PUT")
                print(f"    🔄 [{it_type}] '{it_title}' -> '{new_title}'")

    # --- CIS-4328 ---
    print("\n--- Cleaning CIS-4328 Information Security (13090) ---")
    mods_4328 = get_all(f"{API_BASE}/courses/13090/modules?include[]=items&per_page=100")
    for m in mods_4328:
        mid = m.get("id")
        old_name = m.get("name")
        if "Reading Guide" in old_name:
            # e.g., "Reading Guide — Module 01: Threats, Attacks, and Vulnerabilities"
            new_name = re.sub(r"^Reading Guide\s*[:—–-]\s*", "", old_name, flags=re.IGNORECASE).strip()
            api_call(f"{API_BASE}/courses/13090/modules/{mid}", data={"module": {"name": new_name}}, method="PUT")
            print(f"  🔄 Module {mid}: '{old_name}' -> '{new_name}'")
            
        for it in m.get("items", []):
            it_id = it.get("id")
            it_title = it.get("title")
            it_type = it.get("type")
            new_title = it_title
            
            if it_type == "Page" and it_title.startswith("Reading Guide (M"):
                new_title = re.sub(r"Reading Guide \(M(\d+)\):\s*(?:Reading Guide\s*[:—–-]\s*)?", r"Reading Guide (M\1): ", it_title)
            elif it_type == "Discussion" and ("Reading Guide —" in it_title or "Reading Guide:" in it_title):
                new_title = re.sub(r"Discussion \(M(\d+)\):\s*(?:Reading Guide\s*[:—–-]\s*)?", r"Discussion (M\1): ", it_title)
            elif it_type == "Quiz" and ("Quiz —" in it_title or "Quiz: Quiz:" in it_title or "Quiz: Quiz —" in it_title):
                new_title = re.sub(r"Quiz \(M(\d+)\):\s*(?:Quiz\s*[:—–-]\s*)?", r"Quiz (M\1): ", it_title)
                
            if new_title != it_title:
                api_call(f"{API_BASE}/courses/13090/modules/{mid}/items/{it_id}", data={"module_item": {"title": new_title}}, method="PUT")
                print(f"    🔄 [{it_type}] '{it_title}' -> '{new_title}'")

    # --- CSC-6361 ---
    print("\n--- Cleaning CSC-6361 Computer Networks (12666) ---")
    mods_6361 = get_all(f"{API_BASE}/courses/12666/modules?include[]=items&per_page=100")
    for m in mods_6361:
        mid = m.get("id")
        for it in m.get("items", []):
            it_id = it.get("id")
            it_title = it.get("title")
            it_type = it.get("type")
            cid = it.get("content_id")
            new_title = it_title
            
            # Fix Module 05 Discussion
            if it_type == "Discussion" and "M05" in it_title and "Lab" in it_title:
                new_title = "Discussion (M05): QoS, High Availability & Network Automation"
                # also update topic itself
                if cid:
                    api_call(f"{API_BASE}/courses/12666/discussion_topics/{cid}", data={"title": new_title}, method="PUT")
            
            # Fix Module 07 Quiz
            elif it_type == "Quiz" and "M07" in it_title and "Lab" in it_title:
                new_title = "Quiz (M07): Comprehensive Final Exam & Troubleshooting Review"
                if cid:
                    api_call(f"{API_BASE}/courses/12666/quizzes/{cid}", data={"quiz": {"title": new_title}}, method="PUT")
            
            # Clean Reading Guide
            elif it_type == "Page" and it_title.startswith("Reading Guide (M"):
                new_title = re.sub(r"Reading Guide \(M(\d+)\):\s*Reading Guide:\s*", r"Reading Guide (M\1): ", it_title)
                
            if new_title != it_title:
                api_call(f"{API_BASE}/courses/12666/modules/{mid}/items/{it_id}", data={"module_item": {"title": new_title}}, method="PUT")
                print(f"    🔄 [{it_type}] '{it_title}' -> '{new_title}'")

def main():
    resolve_syllabus_quizzes()
    polish_titles()
    print("\n" + "="*80)
    print("✅ COMPREHENSIVE COURSE CLARITY & POLISH COMPLETE!")
    print("="*80)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Full Live Course Deployer for CSC-6361-33: Computer Networks
Course ID: 12666
Texas Wesleyan University Canvas LMS
"""

import os, re, json, time, sys
from pathlib import Path
import urllib.request, urllib.parse, urllib.error
from csc6361_builder_core import (
    api_get, api_post, api_put, api_delete,
    md2html, parse_quiz, build_rich_reading_guide,
    CANVAS_URL, TOKEN, COURSE_ID
)

BASE_DIR = Path(__file__).parent / "CSC-6361_Computer_Networks"

# ─── ACADEMIC CALENDAR (FALL 2026 7-WEEK 2 SESSION) ─────────────────────────
# Session: Oct 19, 2026 – Dec 11, 2026
# CDT is UTC-5 through Saturday, Oct 31, 2026
# CST is UTC-6 starting Sunday, Nov 1, 2026 at 2:00 AM
CALENDAR = {
    1: {
        'name': 'Module 01: Advanced IP Routing: OSPF Multi-Area & EIGRP',
        'dates': 'Oct 19 – Oct 25',
        'unlock_at': '2026-10-19T05:00:00Z',
        'wed_due':   '2026-10-22T04:59:00Z', # Oct 21 11:59 PM CDT
        'sun_due':   '2026-10-26T04:59:00Z', # Oct 25 11:59 PM CDT
    },
    2: {
        'name': 'Module 02: Campus Network Design: VLANs, STP & EtherChannel',
        'dates': 'Oct 26 – Nov 1',
        'unlock_at': '2026-10-26T05:00:00Z',
        'wed_due':   '2026-10-29T04:59:00Z', # Oct 28 11:59 PM CDT
        'sun_due':   '2026-11-02T05:59:00Z', # Nov 1 11:59 PM CST
    },
    3: {
        'name': 'Module 03: WAN Technologies: MPLS, SD-WAN & VPNs',
        'dates': 'Nov 2 – Nov 8',
        'unlock_at': '2026-11-02T06:00:00Z',
        'wed_due':   '2026-11-05T05:59:00Z', # Nov 4 11:59 PM CST
        'sun_due':   '2026-11-09T05:59:00Z', # Nov 8 11:59 PM CST
    },
    4: {
        'name': 'Module 04: Enterprise Security & Infrastructure Hardening',
        'dates': 'Nov 9 – Nov 15',
        'unlock_at': '2026-11-09T06:00:00Z',
        'wed_due':   '2026-11-12T05:59:00Z', # Nov 11 11:59 PM CST
        'sun_due':   '2026-11-16T05:59:00Z', # Nov 15 11:59 PM CST
    },
    5: {
        'name': 'Module 05: QoS, High Availability & Network Automation',
        'dates': 'Nov 16 – Nov 22',
        'unlock_at': '2026-11-16T06:00:00Z',
        'wed_due':   '2026-11-19T05:59:00Z', # Nov 18 11:59 PM CST
        'sun_due':   '2026-11-23T05:59:00Z', # Nov 22 11:59 PM CST
    },
    6: {
        'name': 'Module 06: Cloud Networking & Hybrid Architectures + Research Paper',
        'dates': 'Nov 23 – Dec 1 (Extended)',
        'unlock_at': '2026-11-23T06:00:00Z',
        'wed_due':   '2026-11-26T05:59:00Z', # Nov 25 11:59 PM CST
        'sun_due':   '2026-12-02T05:59:00Z', # Dec 1 11:59 PM CST (Thanksgiving extension)
    },
    7: {
        'name': 'Module 07: Troubleshooting, Capstone Lab & Final Exam',
        'dates': 'Nov 30 – Dec 11',
        'unlock_at': '2026-11-30T06:00:00Z',
        'wed_due':   '2026-12-03T05:59:00Z', # Dec 2 11:59 PM CST
        'sun_due':   '2026-12-12T05:59:00Z', # Dec 11 11:59 PM CST (Term end)
    },
}

def setup_course_overview():
    print("\n[STEP 1] Updating Course Metadata & Syllabus Body...")
    syl_path = BASE_DIR / "00_Course_Information" / "Syllabus.md"
    syl_text = syl_path.read_text(encoding='utf-8') if syl_path.exists() else ""
    syl_html = md2html(syl_text)

    course_payload = {
        'course': {
            'name': 'CSC-6361-33: Computer Networks',
            'course_code': 'CSC-6361-33',
            'default_view': 'modules',
            'syllabus_body': syl_html,
            'apply_assignment_group_weights': True,
        }
    }
    api_put(f"/courses/{COURSE_ID}", course_payload)
    print("  ✅ Course metadata & syllabus updated.")


def setup_assignment_groups():
    print("\n[STEP 2] Setting Up Weighted Gradebook Assignment Groups...")
    existing = api_get(f"/courses/{COURSE_ID}/assignment_groups")
    existing_map = {g['name']: g['id'] for g in existing} if isinstance(existing, list) else {}

    groups = [
        ("Weekly Lab Assignments (Modules 01–06)", 30.0),
        ("Weekly Quizzes (Modules 01–06)",         20.0),
        ("Graduate Discussion Boards (Modules 01–06)", 20.0),
        ("Graduate Research Paper (Module 06)",    10.0),
        ("Final Capstone Lab & Exam (Module 07)",  20.0),
    ]

    group_ids = {}
    for name, weight in groups:
        if name in existing_map:
            gid = existing_map[name]
            api_put(f"/courses/{COURSE_ID}/assignment_groups/{gid}", {'group_weight': weight})
            group_ids[name] = gid
            print(f"  ✅ Updated group: {name} ({weight}%)")
        else:
            res = api_post(f"/courses/{COURSE_ID}/assignment_groups", {
                'name': name,
                'group_weight': weight
            })
            if res.get('id'):
                group_ids[name] = res['id']
                print(f"  ✅ Created group: {name} ({weight}%)")
            time.sleep(0.3)

    return group_ids


def create_page(title: str, body_html: str) -> str:
    url_slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:60]
    payload = {
        'wiki_page': {
            'title': title,
            'body': body_html,
            'published': True,
        }
    }
    res = api_put(f"/courses/{COURSE_ID}/pages/{url_slug}", payload)
    if not res.get('url'):
        res = api_post(f"/courses/{COURSE_ID}/pages", payload)
    return res.get('url', url_slug)


def add_module_item(module_id: int, item_type: str, content_id: int | str = None, page_url: str = None, title: str = None):
    payload = {
        'module_item': {
            'type': item_type,
        }
    }
    if item_type == 'Page' and page_url:
        payload['module_item']['page_url'] = page_url
    elif content_id:
        payload['module_item']['content_id'] = content_id
    if title:
        payload['module_item']['title'] = title

    res = api_post(f"/courses/{COURSE_ID}/modules/{module_id}/items", payload)
    time.sleep(0.2)
    return res


def build_module_00(mod0_id: int):
    print("\n[STEP 3] Populating Course Information & Resources (Module 00)...")
    info_dir = BASE_DIR / "00_Course_Information"

    pages_to_create = [
        ("Welcome to CSC-6361: Advanced Computer Networks", info_dir / "Course_Administration_Pack.md"),
        ("Course Syllabus & Graduate Policies",             info_dir / "Syllabus.md"),
        ("Online Course Map & 7-Week Schedule",            info_dir / "Online_Course_Map.md"),
        ("Graduate Student Success Guide",                 info_dir / "STUDENT_GUIDE.md"),
        ("Zero Textbook Cost (ZTC) & Free OER Resources",  BASE_DIR / "ZTC_OER_Reading_Materials.md"),
    ]

    for title, ppath in pages_to_create:
        if ppath.exists():
            html_body = md2html(ppath.read_text(encoding='utf-8'))
            url = create_page(title, html_body)
            add_module_item(mod0_id, 'Page', page_url=url, title=title)
            print(f"  ✅ Added page: {title}")
        time.sleep(0.3)


def build_modules(group_ids: dict):
    print("\n[STEP 4] Building All 7 Academic Modules...")

    lab_gid   = group_ids.get("Weekly Lab Assignments (Modules 01–06)")
    quiz_gid  = group_ids.get("Weekly Quizzes (Modules 01–06)")
    disc_gid  = group_ids.get("Graduate Discussion Boards (Modules 01–06)")
    paper_gid = group_ids.get("Graduate Research Paper (Module 06)")
    cap_gid   = group_ids.get("Final Capstone Lab & Exam (Module 07)")

    # Fetch existing modules
    existing_mods = api_get(f"/courses/{COURSE_ID}/modules?per_page=50")
    mod_map = {m['name']: m['id'] for m in existing_mods} if isinstance(existing_mods, list) else {}

    for mod_num in range(1, 8):
        cal = CALENDAR[mod_num]
        mod_name = cal['name']
        mod_dir = BASE_DIR / f"Module_{mod_num:02d}"

        print(f"\n{'='*60}")
        print(f"MODULE {mod_num:02d}: {mod_name}")
        print(f"{'='*60}")

        # Get or create module
        if mod_name in mod_map:
            mod_id = mod_map[mod_name]
        else:
            res_m = api_post(f"/courses/{COURSE_ID}/modules", {
                'module': {
                    'name': mod_name,
                    'position': mod_num + 1,
                    'unlock_at': cal['unlock_at'],
                }
            })
            mod_id = res_m.get('id')
            api_put(f"/courses/{COURSE_ID}/modules/{mod_id}", {'module': {'published': True}})
            time.sleep(0.3)

        print(f"  Using Module ID: {mod_id}")

        # 1. Video Scripts Part 1 & 2
        for part in (1, 2):
            vs_files = sorted(mod_dir.glob(f"*Video_Script*_Part_{part}.md"))
            if vs_files:
                vs_text = vs_files[0].read_text(encoding='utf-8')
                vs_title = f"Lecture Video Script (M{mod_num:02d} Part {part})"
                vs_html = f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:20px 28px;border-radius:8px;margin-bottom:20px;">
  <h1 style="color:white;margin:0;font-size:22px;font-weight:bold;">📺 {vs_title}</h1>
  <p style="color:#ffcccc;margin:6px 0 0;font-size:13px;">CSC-6361: Advanced Computer Networks · Professor Nash</p>
</div>
{md2html(vs_text)}
</div>'''
                url = create_page(vs_title, vs_html)
                add_module_item(mod_id, 'Page', page_url=url, title=vs_title)
                print(f"  ✅ Added Video Script Part {part}")
                time.sleep(0.3)

        # 2. Enriched Reading Guide with SVG Diagram
        rg_files = sorted(mod_dir.glob("*Reading_Guide*.md"))
        if rg_files:
            rg_text = rg_files[0].read_text(encoding='utf-8')
            tm = re.search(r'^#\s+(.+)$', rg_text, re.M)
            rg_topic = re.sub(r'[*_`]', '', tm.group(1)).strip() if tm else f"Module {mod_num:02d} Reading Guide"
            rg_title = f"Reading Guide (M{mod_num:02d}): {rg_topic}"
            rg_html = build_rich_reading_guide(mod_num, rg_title, rg_text)
            url = create_page(rg_title, rg_html)
            add_module_item(mod_id, 'Page', page_url=url, title=rg_title)
            print(f"  ✅ Added Enriched Reading Guide (with Architecture Diagram)")
            time.sleep(0.3)

        # 3. Graduate Discussion Board
        disc_files = sorted(mod_dir.glob("*Discussion*.md"))
        if disc_files:
            disc_text = disc_files[0].read_text(encoding='utf-8')
            dtm = re.search(r'^#\s+(.+)$', disc_text, re.M)
            d_topic = re.sub(r'[*_`]', '', dtm.group(1)).strip() if dtm else f"Module {mod_num:02d} Discussion"
            d_title = f"Discussion (M{mod_num:02d}): {d_topic}"
            disc_html = f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:14px 18px;border-radius:0 8px 8px 0;margin-bottom:18px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:13.5px;">⏰ DISCUSSION DUE DATES</p>
  <p style="margin:4px 0 0;color:#7a5800;font-size:13px;">Initial Substantive Post (400+ words, 1+ citation) due <strong>Wednesday at 11:59 PM</strong>. Peer Responses (2+ classmates) due <strong>Sunday at 11:59 PM</strong>.</p>
</div>
{md2html(disc_text)}
</div>'''
            disc_payload = {
                'title': d_title,
                'message': disc_html,
                'discussion_type': 'threaded',
                'published': True,
                'require_initial_post': True,
                'assignment': {
                    'points_possible': 100.0,
                    'due_at': cal['sun_due'],
                    'assignment_group_id': disc_gid,
                }
            }
            res_d = api_post(f"/courses/{COURSE_ID}/discussion_topics", disc_payload)
            if res_d.get('id'):
                add_module_item(mod_id, 'Discussion', content_id=res_d['id'], title=d_title)
                print(f"  ✅ Added Graded Discussion Board ({d_title[:50]}...)")
            time.sleep(0.3)

        # 4. Weekly Quiz
        quiz_files = sorted(mod_dir.glob("*Quiz*.md"))
        if quiz_files:
            quiz_text = quiz_files[0].read_text(encoding='utf-8')
            q_list = parse_quiz(quiz_text)
            q_title = f"Quiz (M{mod_num:02d}): {cal['name'].split(': ')[1]}"
            q_target_gid = cap_gid if mod_num == 7 else quiz_gid

            quiz_payload = {
                'quiz': {
                    'title': q_title,
                    'description': f'<p>This quiz assesses your comprehension of Module {mod_num:02d} reading, lectures, and lab concepts. 1 attempt, 30-minute time limit.</p>',
                    'quiz_type': 'assignment',
                    'assignment_group_id': q_target_gid,
                    'time_limit': 30,
                    'allowed_attempts': 1,
                    'scoring_policy': 'keep_highest',
                    'due_at': cal['sun_due'],
                    'published': True,
                }
            }
            res_q = api_post(f"/courses/{COURSE_ID}/quizzes", quiz_payload)
            if res_q.get('id'):
                qid = res_q['id']
                # Upload all parsed questions
                pts_each = round(100.0 / max(len(q_list), 1), 1)
                pushed = 0
                for q in q_list:
                    answers = [{'answer_text': q['options'][l], 'answer_weight': 100 if l == q['correct'] else 0}
                               for l in sorted(q['options'].keys())]
                    res_qq = api_post(f"/courses/{COURSE_ID}/quizzes/{qid}/questions", {
                        'question': {
                            'question_name': f"Question {pushed+1}",
                            'question_text': q['stem'],
                            'question_type': 'multiple_choice_question',
                            'points_possible': pts_each,
                            'answers': answers,
                        }
                    })
                    if res_qq.get('id'):
                        pushed += 1
                    time.sleep(0.25)

                api_put(f"/courses/{COURSE_ID}/quizzes/{qid}", {'quiz': {'published': True}})
                add_module_item(mod_id, 'Quiz', content_id=qid, title=q_title)
                print(f"  ✅ Added Quiz with {pushed}/{len(q_list)} Questions ({q_title[:50]}...)")
            time.sleep(0.3)

        # 5. Hands-on Lab Assignment
        lab_files = sorted(mod_dir.glob("*Lab*.md"))
        if lab_files:
            lab_text = lab_files[0].read_text(encoding='utf-8')
            ltm = re.search(r'^#\s+(.+)$', lab_text, re.M)
            l_topic = re.sub(r'[*_`]', '', ltm.group(1)).strip() if ltm else f"Module {mod_num:02d} Lab"
            is_capstone = (mod_num == 7)
            l_title = f"Capstone Enterprise Lab (M07)" if is_capstone else f"Lab (M{mod_num:02d}): {l_topic}"
            l_target_gid = cap_gid if is_capstone else lab_gid

            lab_html = f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">
<div style="background:#e8f4fc;border-left:5px solid #2a7ab5;padding:14px 18px;border-radius:0 8px 8px 0;margin-bottom:18px;">
  <p style="margin:0;font-weight:bold;color:#1a5a8a;font-size:13.5px;">📋 LAB SUBMISSION REQUIREMENTS</p>
  <p style="margin:4px 0 0;color:#1a5a8a;font-size:13px;">Submit two deliverables: (1) Completed <strong>.pkt</strong> Cisco Packet Tracer topology file, and (2) Professional <strong>PDF</strong> Lab Report with screenshots and analytical commentary.</p>
</div>
{md2html(lab_text)}
</div>'''
            lab_payload = {
                'assignment': {
                    'name': l_title,
                    'description': lab_html,
                    'points_possible': 100.0,
                    'due_at': cal['sun_due'],
                    'assignment_group_id': l_target_gid,
                    'submission_types': ['online_upload'],
                    'allowed_extensions': ['pkt', 'pdf', 'zip'],
                    'published': True,
                }
            }
            res_l = api_post(f"/courses/{COURSE_ID}/assignments", lab_payload)
            if res_l.get('id'):
                add_module_item(mod_id, 'Assignment', content_id=res_l['id'], title=l_title)
                print(f"  ✅ Added Lab Assignment ({l_title[:50]}...)")
            time.sleep(0.3)

        # 6. Special Case: Module 06 Graduate Research Paper
        if mod_num == 6:
            paper_title = "Graduate Research Paper: Advanced Enterprise Networking"
            paper_desc = '''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:20px 28px;border-radius:8px;margin-bottom:20px;">
  <h1 style="color:white;margin:0;font-size:22px;font-weight:bold;">📄 Graduate Research Paper</h1>
  <p style="color:#ffcccc;margin:6px 0 0;font-size:13px;">CSC-6361: Advanced Computer Networks · 10% of Final Grade</p>
</div>
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:14px 18px;border-radius:0 8px 8px 0;margin-bottom:20px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;">⏰ EXTENDED SUBMISSION DEADLINE: Tuesday, December 1, 2026 at 11:59 PM CST</p>
  <p style="margin:4px 0 0;color:#7a5800;font-size:13px;">Extended due to Thanksgiving Break. Submit your paper as a PDF document.</p>
</div>
<h3>Paper Requirements</h3>
<ul>
  <li><strong>Length:</strong> 5–7 pages (double-spaced, 12pt font, standard 1-inch margins, excluding title page and references).</li>
  <li><strong>Format:</strong> APA 7th Edition or IEEE style.</li>
  <li><strong>References:</strong> Minimum of 5 credible technical sources (RFCs, IEEE Xplore, ACM Digital Library, or official vendor whitepapers).</li>
  <li><strong>Topic Options:</strong>
    <ul>
      <li>SD-WAN Migration Strategies and Architectural Trade-offs in Multi-Cloud Enterprises</li>
      <li>BGP Security: RPKI Route Origin Authorization, BGPsec, and Path Validation</li>
      <li>Zero Trust Network Architecture (ZTNA) and Micro-segmentation in Campus Infrastructures</li>
      <li>Network Automation at Scale: Model-Driven Telemetry, gNMI, and Infrastructure as Code</li>
      <li>IPv6-Only Transition in Modern Data Centers: Operational Realities and Performance Analysis</li>
    </ul>
  </li>
</ul>
<h3>Grading Rubric (100 Points)</h3>
<ul>
  <li><strong>Technical Accuracy &amp; Depth (35 pts):</strong> Demonstrates graduate-level understanding aligned with CCNP standards.</li>
  <li><strong>Research Quality &amp; Citations (25 pts):</strong> Minimum 5 credible sources properly integrated.</li>
  <li><strong>Writing Quality &amp; Organization (25 pts):</strong> Clear, professional structure, logical argument progression.</li>
  <li><strong>Original Analysis &amp; Recommendations (15 pts):</strong> Synthesizes unique insights rather than merely summarizing sources.</li>
</ul>
</div>'''
            paper_payload = {
                'assignment': {
                    'name': paper_title,
                    'description': paper_desc,
                    'points_possible': 100.0,
                    'due_at': cal['sun_due'],
                    'assignment_group_id': paper_gid,
                    'submission_types': ['online_upload'],
                    'allowed_extensions': ['pdf'],
                    'published': True,
                }
            }
            res_p = api_post(f"/courses/{COURSE_ID}/assignments", paper_payload)
            if res_p.get('id'):
                add_module_item(mod_id, 'Assignment', content_id=res_p['id'], title=paper_title)
                print(f"  ✅ Added Graduate Research Paper Assignment")
            time.sleep(0.3)

    print(f"\n{'='*60}")
    print("✅ CSC-6361-33: COMPUTER NETWORKS FULLY DEPLOYED TO CANVAS!")
    print(f"{'='*60}")


if __name__ == '__main__':
    setup_course_overview()
    group_ids = setup_assignment_groups()

    # Create/check Module 00
    existing_mods = api_get(f"/courses/{COURSE_ID}/modules?per_page=50")
    mod0_name = "Course Information & Resources"
    mod0_id = None
    if isinstance(existing_mods, list):
        for m in existing_mods:
            if m['name'] == mod0_name:
                mod0_id = m['id']
                break
    if not mod0_id:
        res0 = api_post(f"/courses/{COURSE_ID}/modules", {'module': {'name': mod0_name, 'position': 1}})
        mod0_id = res0.get('id')
    
    api_put(f"/courses/{COURSE_ID}/modules/{mod0_id}", {'module': {'published': True}})
    build_module_00(mod0_id)
    build_modules(group_ids)

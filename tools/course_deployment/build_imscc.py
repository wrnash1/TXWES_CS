# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
TXWES Course Builder — IMS Common Cartridge v1.1 Package Generator
Converts Markdown course content to Canvas/Blackboard .imscc format.

Usage:
  python3 build_imscc.py CIS-1310_Intro_to_Python
  python3 build_imscc.py CIS-1310_Intro_to_Python --section 40
  python3 build_imscc.py --all                        # builds every course in CWD

Output: dist/CIS-XXXX_CourseName_Fall2026.imscc
"""

import os, re, sys, uuid, zipfile, argparse
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

# ── Pure-Python Markdown → HTML Engine ───────────────────────────────────────
def md2html(text: str) -> str:
    """
    Comprehensive zero-dependency Markdown-to-HTML converter.
    Handles code blocks, headers, hr, blockquotes, lists, tables, inline formatting.
    """
    if not text:
        return ""

    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Code blocks (fenced)
    code_blocks = []
    def _store_code_block(m):
        lang = m.group(1) or ""
        code = m.group(2)
        code_escaped = xml_escape(code)
        idx = len(code_blocks)
        code_blocks.append(f'<pre><code>{code_escaped}</code></pre>')
        return f'__CODE_BLOCK_{idx}__'

    text = re.sub(r'```(\w*)\n(.*?)```', _store_code_block, text, flags=re.DOTALL)

    lines = text.split('\n')
    html_lines = []
    in_list = None  # 'ul' or 'ol'
    in_blockquote = False
    in_table = False
    table_headers = []
    table_rows = []

    def _flush_list():
        nonlocal in_list
        if in_list:
            html_lines.append(f'</{in_list}>')
            in_list = None

    def _flush_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            html_lines.append('</blockquote>')
            in_blockquote = False

    def _flush_table():
        nonlocal in_table, table_headers, table_rows
        if in_table:
            out = ['<table>']
            if table_headers:
                out.append('  <thead><tr>')
                for th in table_headers:
                    out.append(f'    <th>{_inline_md(th.strip())}</th>')
                out.append('  </tr></thead>')
            if table_rows:
                out.append('  <tbody>')
                for row in table_rows:
                    out.append('    <tr>')
                    for td in row:
                        out.append(f'      <td>{_inline_md(td.strip())}</td>')
                    out.append('    </tr>')
                out.append('  </tbody>')
            out.append('</table>')
            html_lines.append('\n'.join(out))
            in_table = False
            table_headers = []
            table_rows = []

    def _inline_md(s: str) -> str:
        # Bold + Italic
        s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        # Bold
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'__(.+?)__', r'<strong>\1</strong>', s)
        # Italic
        s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
        s = re.sub(r'_(.+?)_', r'<em>\1</em>', s)
        # Inline code
        s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
        # Links
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
        return s

    for line in lines:
        raw = line.strip()

        # Check code block placeholder
        if raw.startswith('__CODE_BLOCK_') and raw.endswith('__'):
            _flush_list()
            _flush_blockquote()
            _flush_table()
            idx = int(raw.replace('__CODE_BLOCK_', '').replace('__', ''))
            html_lines.append(code_blocks[idx])
            continue

        # Horizontal Rule
        if re.match(r'^(?:---|\*\*\*|___)\s*$', raw):
            _flush_list()
            _flush_blockquote()
            _flush_table()
            html_lines.append('<hr />')
            continue

        # Headings
        hm = re.match(r'^(#{1,6})\s+(.+)$', raw)
        if hm:
            _flush_list()
            _flush_blockquote()
            _flush_table()
            level = len(hm.group(1))
            h_text = _inline_md(hm.group(2))
            html_lines.append(f'<h{level}>{h_text}</h{level}>')
            continue

        # Table rows (| col1 | col2 |)
        if raw.startswith('|') and raw.endswith('|'):
            _flush_list()
            _flush_blockquote()
            cells = [c for c in raw.split('|')[1:-1]]
            # Check if separator row (|---|---|)
            if all(re.match(r'^\s*:?-+:?\s*$', c) for c in cells):
                continue
            if not in_table:
                in_table = True
                table_headers = cells
            else:
                table_rows.append(cells)
            continue
        else:
            _flush_table()

        # Blockquote
        if raw.startswith('>'):
            _flush_list()
            _flush_table()
            bq_text = _inline_md(re.sub(r'^>\s*', '', raw))
            if not in_blockquote:
                html_lines.append('<blockquote>')
                in_blockquote = True
            html_lines.append(f'  <p>{bq_text}</p>')
            continue
        else:
            _flush_blockquote()

        # Unordered List
        ul_m = re.match(r'^[-*+]\s+(.+)$', raw)
        if ul_m:
            _flush_blockquote()
            _flush_table()
            item_text = _inline_md(ul_m.group(1))
            if in_list != 'ul':
                _flush_list()
                html_lines.append('<ul>')
                in_list = 'ul'
            html_lines.append(f'  <li>{item_text}</li>')
            continue

        # Ordered List
        ol_m = re.match(r'^\d+\.\s+(.+)$', raw)
        if ol_m:
            _flush_blockquote()
            _flush_table()
            item_text = _inline_md(ol_m.group(1))
            if in_list != 'ol':
                _flush_list()
                html_lines.append('<ol>')
                in_list = 'ol'
            html_lines.append(f'  <li>{item_text}</li>')
            continue

        # Empty line
        if not raw:
            _flush_list()
            _flush_blockquote()
            _flush_table()
            continue

        # Normal Paragraph
        _flush_list()
        _flush_blockquote()
        _flush_table()
        p_text = _inline_md(raw)
        html_lines.append(f'<p>{p_text}</p>')

    _flush_list()
    _flush_blockquote()
    _flush_table()

    return '\n'.join(html_lines)


# ── Fall 2026 Academic Calendar ───────────────────────────────────────────────
# Sunday 11:59 PM CDT = Monday 04:59:00 UTC (Labs, Quizzes, Peer Responses)
# Wednesday 11:59 PM CDT = Thursday 04:59:00 UTC (Initial Discussion Posts)
DUE_DATES_SUN = {
    1:  "2026-08-31T04:59:00Z",
    2:  "2026-09-07T04:59:00Z",
    3:  "2026-09-14T04:59:00Z",
    4:  "2026-09-21T04:59:00Z",
    5:  "2026-09-28T04:59:00Z",
    6:  "2026-10-05T04:59:00Z",
    7:  "2026-10-12T04:59:00Z",
    8:  "2026-10-19T04:59:00Z",
    9:  "2026-10-26T04:59:00Z",
    10: "2026-11-02T04:59:00Z",
    11: "2026-11-09T04:59:00Z",
    12: "2026-11-16T04:59:00Z",
    13: "2026-11-23T04:59:00Z",  # Sunday before Thanksgiving
    14: "2026-11-30T04:59:00Z",  # Sunday back from Thanksgiving
    15: "2026-12-07T04:59:00Z",
    16: "2026-12-14T04:59:00Z",  # Finals
}

DUE_DATES_WED = {
    1:  "2026-08-27T04:59:00Z",
    2:  "2026-09-03T04:59:00Z",
    3:  "2026-09-10T04:59:00Z",
    4:  "2026-09-17T04:59:00Z",
    5:  "2026-09-24T04:59:00Z",
    6:  "2026-10-01T04:59:00Z",
    7:  "2026-10-08T04:59:00Z",
    8:  "2026-10-15T04:59:00Z",
    9:  "2026-10-22T04:59:00Z",
    10: "2026-10-29T04:59:00Z",
    11: "2026-11-05T04:59:00Z",
    12: "2026-11-12T04:59:00Z",
    13: "2026-11-19T04:59:00Z",
    14: "2026-11-26T04:59:00Z",
    15: "2026-12-03T04:59:00Z",
    16: "2026-12-10T04:59:00Z",
}

# ── Helpers ───────────────────────────────────────────────────────────────────
def new_id() -> str:
    return uuid.uuid4().hex

def xe(s: str) -> str:
    """XML-escape a string."""
    return xml_escape(str(s))

def read(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except Exception:
        return ''

def find_file(module_dir: Path, pattern: str) -> Path | None:
    """Return first file in module_dir whose name matches glob pattern."""
    matches = sorted(module_dir.glob(pattern))
    return matches[0] if matches else None

def extract_title_from_md(md_text: str, fallback: str = '') -> str:
    """Pull the first # heading from Markdown as a plain-text title."""
    m = re.search(r'^#\s+(.+)$', md_text, re.M)
    if m:
        t = re.sub(r'[*_`]', '', m.group(1))
        return t.strip()
    return fallback

# ── Quiz Parser ───────────────────────────────────────────────────────────────
def parse_quiz(md_text: str) -> list[dict]:
    """
    Parse quiz Markdown into question dicts.
    Returns list of {'stem', 'options': {A..D}, 'correct', 'points'}
    """
    questions = []

    QUESTION_SPLIT = re.compile(
        r'(\n(?:#{2,3}\s+Question\s*\d+|####\s+Q\d+(?=\n)|\*\*Question\s+\d+[^*\n]*\*\*)[^\n]*\n)',
        re.IGNORECASE
    )
    parts = QUESTION_SPLIT.split(md_text)
    pairs = []
    i = 1
    while i + 1 < len(parts):
        pairs.append((parts[i], parts[i + 1]))
        i += 2

    for header, block in pairs:
        header_answer = None
        ha = re.search(r'Answer\s*:\s*([A-D])', header, re.IGNORECASE)
        if ha:
            header_answer = ha.group(1).upper()

        opt_start = re.search(r'\n\s*[-*]?\s*[A-D][.):]\s', block)
        if not opt_start:
            continue
        stem = block[:opt_start.start()].strip()
        stem = re.sub(r'^(?:\*\*[^*]+\*\*\s*\n)+', '', stem).strip()
        if not stem:
            continue

        options = {}
        for m in re.finditer(
            r'(?:^|\n)\s*[-*]?\s*([A-D])[.):]\s+(.*?)'
            r'(?=\n\s*[-*]?\s*[A-D][.):]\s'
            r'|\n\n(?:Correct|\*\*Correct|Distractor|\*\*Answer|Answer\s*\d|---)'
            r'|\Z)',
            block, re.DOTALL
        ):
            label = m.group(1).upper()
            text  = m.group(2).strip()
            text  = re.sub(r'\n+', ' ', text)
            text  = re.sub(r'\*\*', '', text).strip()
            text  = re.split(r'\s+\u2014\s+|\s*---\s*', text)[0].strip()
            text  = re.split(r'\*?Correct\s+Answer', text, flags=re.I)[0].strip()
            options[label] = text

        if len(options) < 2:
            continue

        if header_answer and header_answer in options:
            correct = header_answer
        else:
            ca = re.search(
                r'(?:Correct\s+)?Answer[:\s*\d]*[:\s*]+\**\s*([A-D])',
                block, re.IGNORECASE
            )
            if not ca:
                continue
            correct = ca.group(1).upper()
            if correct not in options:
                continue

        pts_m = re.search(r'\((\d+)\s*points?\)', block)
        points = float(pts_m.group(1)) if pts_m else 10.0

        questions.append({
            'stem':    stem,
            'options': options,
            'correct': correct,
            'points':  points,
        })

    return questions

# ── QTI & Assessment XML Builders ──────────────────────────────────────────
def build_qti(quiz_id: str, title: str, questions: list[dict]) -> str:
    """Generate Canvas-compliant IMS QTI v1.2 XML for a quiz."""
    total_pts = sum(q['points'] for q in questions)

    items_xml = ''
    for i, q in enumerate(questions, 1):
        item_id = new_id()
        pts = q['points']
        stem_html = md2html(q['stem'])

        # Option ident mapping
        opt_idents = {lbl: f"opt_{lbl}_{new_id()[:6]}" for lbl in q['options'].keys()}

        labels_xml = ''
        for lbl, text in sorted(q['options'].items()):
            opt_id = opt_idents[lbl]
            t_html = md2html(text)
            labels_xml += f'''
              <response_label ident="{opt_id}">
                <material><mattext texttype="text/html">{xe(t_html)}</mattext></material>
              </response_label>'''

        correct_opt_id = opt_idents[q['correct']]

        items_xml += f'''
      <item ident="{item_id}" title="Question {i}">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>cc_profile</fieldlabel>
              <fieldentry>cc.multiple_choice.v0p1</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>{pts:.1f}</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">{xe(stem_html)}</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice shuffle="No">{labels_xml}
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">{correct_opt_id}</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>'''

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_qtiasiv1p2p1_v1p0.xsd">
  <assessment ident="{quiz_id}" title="{xe(title)}">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_profile</fieldlabel>
        <fieldentry>cc.exam.v0p1</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_assessmenttype</fieldlabel>
        <fieldentry>Examination</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_scoretype</fieldlabel>
        <fieldentry>Percentage</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>1</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
      {items_xml}
    </section>
  </assessment>
</questestinterop>'''

def build_assessment_meta(quiz_id: str, assign_id: str, group_id: str,
                           title: str, due_at: str, total_pts: float,
                           mod_num: int) -> str:
    """Generate Canvas quiz metadata XML."""
    all_day_date = due_at[:10] if due_at else ''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<quiz identifier="{quiz_id}"
  xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{xe(title)}</title>
  <description></description>
  <shuffle_answers>false</shuffle_answers>
  <scoring_policy>keep_highest</scoring_policy>
  <hide_results></hide_results>
  <quiz_type>assignment</quiz_type>
  <points_possible>{total_pts:.1f}</points_possible>
  <allowed_attempts>1</allowed_attempts>
  <one_question_at_a_time>false</one_question_at_a_time>
  <cant_go_back>false</cant_go_back>
  <available>true</available>
  <unlock_at></unlock_at>
  <due_at>{xe(due_at)}</due_at>
  <show_correct_answers>true</show_correct_answers>
  <anonymous_submissions>false</anonymous_submissions>
  <could_be_locked>false</could_be_locked>
  <time_limit>30</time_limit>
  <ip_filter></ip_filter>
  <workflow_state>published</workflow_state>
  <assignment identifier="{assign_id}">
    <title>{xe(title)}</title>
    <due_at>{xe(due_at)}</due_at>
    <lock_at></lock_at>
    <unlock_at></unlock_at>
    <module_locked>false</module_locked>
    <all_day_date>{all_day_date}</all_day_date>
    <has_overrides>false</has_overrides>
    <could_be_locked>false</could_be_locked>
    <submission_types>online_quiz</submission_types>
    <assignment_group_identifierref>{group_id}</assignment_group_identifierref>
    <workflow_state>published</workflow_state>
    <quiz_identifierref>{quiz_id}</quiz_identifierref>
    <rubric_use_for_grading>false</rubric_use_for_grading>
    <rubric_hide_score_total>false</rubric_hide_score_total>
    <has_group_category>false</has_group_category>
    <points_possible>{total_pts:.1f}</points_possible>
    <grading_type>points</grading_type>
    <all_day>false</all_day>
    <position>4</position>
  </assignment>
  <assignment_group_identifierref>{group_id}</assignment_group_identifierref>
</quiz>'''

# ── Assignment (Lab) Builders ─────────────────────────────────────────────────
def build_assignment_settings(assign_id: str, rubric_id: str, group_id: str,
                               title: str, due_at: str, mod_num: int) -> str:
    all_day_date = due_at[:10] if due_at else ''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<assignment identifier="{assign_id}"
  xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{xe(title)}</title>
  <due_at>{xe(due_at)}</due_at>
  <lock_at></lock_at>
  <unlock_at></unlock_at>
  <all_day_date>{all_day_date}</all_day_date>
  <has_overrides>false</has_overrides>
  <could_be_locked>false</could_be_locked>
  <submission_types>online_upload,online_text_entry</submission_types>
  <assignment_group_identifierref>{group_id}</assignment_group_identifierref>
  <grading_type>points</grading_type>
  <points_possible>20.0</points_possible>
  <all_day>false</all_day>
  <position>2</position>
  <rubric_identifierref>{rubric_id}</rubric_identifierref>
  <rubric_use_for_grading>true</rubric_use_for_grading>
  <rubric_hide_score_total>false</rubric_hide_score_total>
  <has_group_category>false</has_group_category>
  <workflow_state>published</workflow_state>
  <external_tool_tag/>
</assignment>'''

# ── Discussion XML Builders ───────────────────────────────────────────────────
def build_discussion(title: str, html_body: str) -> str:
    """IMS Common Cartridge Discussion Topic XML."""
    escaped_body = xe(html_body)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<topic xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imsdt_v1p1.xsd">
  <title>{xe(title)}</title>
  <text texttype="text/html">{escaped_body}</text>
</topic>'''

def build_discussion_meta(disc_meta_id: str, disc_topic_id: str, disc_asgn_id: str,
                            group_id: str, rubric_id: str, title: str,
                            due_at_sun: str) -> str:
    """Canvas Discussion Topic Metadata XML (topicMeta)."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<topicMeta identifier="{disc_meta_id}"
  xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <topic_id>{disc_topic_id}</topic_id>
  <title>{xe(title)}</title>
  <position>3</position>
  <type>topic</type>
  <discussion_type>threaded</discussion_type>
  <require_initial_post>true</require_initial_post>
  <has_group_category>false</has_group_category>
  <workflow_state>active</workflow_state>
  <module_locked>false</module_locked>
  <allow_rating>false</allow_rating>
  <only_graders_can_rate>false</only_graders_can_rate>
  <sort_by_rating>false</sort_by_rating>
  <assignment identifier="{disc_asgn_id}">
    <title>{xe(title)}</title>
    <due_at>{xe(due_at_sun)}</due_at>
    <lock_at/>
    <unlock_at/>
    <module_locked>false</module_locked>
    <assignment_group_identifierref>{group_id}</assignment_group_identifierref>
    <workflow_state>published</workflow_state>
    <rubric_identifierref>{rubric_id}</rubric_identifierref>
    <rubric_use_for_grading>true</rubric_use_for_grading>
    <rubric_hide_score_total>false</rubric_hide_score_total>
    <has_group_category>false</has_group_category>
    <points_possible>10.0</points_possible>
    <grading_type>points</grading_type>
    <all_day>false</all_day>
    <submission_types>discussion_topic</submission_types>
    <position>3</position>
  </assignment>
  <reply_to_entry_required_count>2</reply_to_entry_required_count>
</topicMeta>'''

# ── Course Settings XML Builders ──────────────────────────────────────────────
def build_course_settings(course_id: str, title: str, code: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<course identifier="{course_id}"
  xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{xe(title)}</title>
  <course_code>{xe(code)}</course_code>
  <is_public>false</is_public>
  <public_syllabus>false</public_syllabus>
  <public_syllabus_to_auth>false</public_syllabus_to_auth>
  <default_view>modules</default_view>
  <open_enrollment>false</open_enrollment>
  <self_enrollment>false</self_enrollment>
  <license>private</license>
  <indexed>false</indexed>
  <hide_final_grade>false</hide_final_grade>
  <hide_distribution_graphs>false</hide_distribution_graphs>
  <allow_student_discussion_editing>true</allow_student_discussion_editing>
  <allow_student_forum_attachments>false</allow_student_forum_attachments>
  <allow_student_discussion_reporting>true</allow_student_discussion_reporting>
  <restrict_student_past_view>false</restrict_student_past_view>
  <restrict_student_future_view>false</restrict_student_future_view>
  <show_announcements_on_home_page>false</show_announcements_on_home_page>
  <home_page_announcement_limit>3</home_page_announcement_limit>
  <grading_standard_enabled>false</grading_standard_enabled>
  <syllabus_course_summary>true</syllabus_course_summary>
  <lock_all_announcements>false</lock_all_announcements>
  <usage_rights_required>false</usage_rights_required>
  <homeroom_course>false</homeroom_course>
</course>'''

def build_assignment_groups(groups: list[dict]) -> str:
    items = ''
    for g in groups:
        items += f'''
  <assignment_group identifier="{g['id']}">
    <title>{xe(g['name'])}</title>
    <position>{g['position']}</position>
    <group_weight>{g['weight']:.1f}</group_weight>
  </assignment_group>'''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<assignmentGroups xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  {items}
</assignmentGroups>'''

def build_rubrics_xml(lab_rubric_id: str, disc_rubric_id: str) -> str:
    """Rubrics for lab assignments (20 pts) and discussions (10 pts)."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<rubrics xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">

  <rubric identifier="{lab_rubric_id}">
    <title>Lab Assignment Rubric</title>
    <reusable>false</reusable>
    <public>false</public>
    <hide_score_total>false</hide_score_total>
    <free_form_criterion_comments>false</free_form_criterion_comments>
    <criteria>
      <criterion>
        <description>Technical Accuracy &amp; Completeness</description>
        <points>8</points>
        <ratings>
          <rating><description>Excellent</description><points>8</points></rating>
          <rating><description>Proficient</description><points>6</points></rating>
          <rating><description>Developing</description><points>4</points></rating>
          <rating><description>Beginning</description><points>0</points></rating>
        </ratings>
      </criterion>
      <criterion>
        <description>Screenshots / Deliverables Submitted</description>
        <points>7</points>
        <ratings>
          <rating><description>All required</description><points>7</points></rating>
          <rating><description>Most present</description><points>5</points></rating>
          <rating><description>Some missing</description><points>3</points></rating>
          <rating><description>None submitted</description><points>0</points></rating>
        </ratings>
      </criterion>
      <criterion>
        <description>Reflection / Write-Up Quality</description>
        <points>5</points>
        <ratings>
          <rating><description>Thorough analysis</description><points>5</points></rating>
          <rating><description>Adequate</description><points>3</points></rating>
          <rating><description>Minimal</description><points>1</points></rating>
          <rating><description>Not submitted</description><points>0</points></rating>
        </ratings>
      </criterion>
    </criteria>
  </rubric>

  <rubric identifier="{disc_rubric_id}">
    <title>Discussion Board Rubric</title>
    <reusable>false</reusable>
    <public>false</public>
    <hide_score_total>false</hide_score_total>
    <free_form_criterion_comments>false</free_form_criterion_comments>
    <criteria>
      <criterion>
        <description>Initial Post — Content &amp; Technical Accuracy</description>
        <points>6</points>
        <ratings>
          <rating><description>Addresses all prompt parts with technical accuracy</description><points>6</points></rating>
          <rating><description>Addresses most parts, minor gaps</description><points>4</points></rating>
          <rating><description>Partial response</description><points>2</points></rating>
          <rating><description>No post</description><points>0</points></rating>
        </ratings>
      </criterion>
      <criterion>
        <description>Peer Responses (2 required, 60+ words each)</description>
        <points>4</points>
        <ratings>
          <rating><description>Both responses substantive and 60+ words</description><points>4</points></rating>
          <rating><description>One response, or both superficial</description><points>2</points></rating>
          <rating><description>No peer responses</description><points>0</points></rating>
        </ratings>
      </criterion>
    </criteria>
  </rubric>

</rubrics>'''

def build_module_meta(modules_data: list[dict]) -> str:
    mods_xml = ''
    for mod in modules_data:
        items_xml = ''
        for pos, item in enumerate(mod['items'], 1):
            items_xml += f'''
      <item identifier="{item['item_id']}">
        <content_type>{xe(item['content_type'])}</content_type>
        <workflow_state>active</workflow_state>
        <title>{xe(item['title'])}</title>
        <identifierref>{xe(item['res_id'])}</identifierref>
        <position>{pos}</position>
        <new_tab>false</new_tab>
        <indent>0</indent>
      </item>'''
        mods_xml += f'''
  <module identifier="{mod['id']}">
    <title>{xe(mod['title'])}</title>
    <workflow_state>active</workflow_state>
    <position>{mod['position']}</position>
    <require_sequential_progress>false</require_sequential_progress>
    <locked>false</locked>
    <items>{items_xml}
    </items>
  </module>'''

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  {mods_xml}
</modules>'''

def build_context_xml(course_id: str, title: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<course_export xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{xe(title)}</title>
  <identifier>{course_id}</identifier>
</course_export>'''

def build_files_meta() -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<fileMeta xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
</fileMeta>'''

def build_late_policy() -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<latePolicy xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <missing_submission_deduction_enabled>false</missing_submission_deduction_enabled>
  <late_submission_deduction_enabled>false</late_submission_deduction_enabled>
  <late_submission_minimum_percent_enabled>false</late_submission_minimum_percent_enabled>
</latePolicy>'''

def build_media_tracks() -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<media_tracks xmlns="http://canvas.instructure.com/xsd/cccv1p0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
</media_tracks>'''

# ── Manifest Builder ──────────────────────────────────────────────────────────
def build_manifest(manifest_id: str, course_title: str, resources: list[dict]) -> str:
    """
    resources: list of {'id', 'type', 'href', 'files': [str], 'deps': [str]}
    """
    res_xml = ''
    for r in resources:
        files_xml = ''.join(f'\n      <file href="{xe(f)}"/>' for f in r.get('files', []))
        deps_xml = ''.join(
            f'\n      <dependency identifierref="{xe(d)}"/>' for d in r.get('deps', [])
        )
        href_attr = f' href="{xe(r["href"])}"' if r.get('href') else ''
        res_xml += f'''
  <resource identifier="{r['id']}" type="{xe(r['type'])}"{href_attr}>{files_xml}{deps_xml}
  </resource>'''

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{manifest_id}"
  xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"
  xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.1.0</schemaversion>
    <lomimscc:lom>
      <lomimscc:general>
        <lomimscc:title>
          <lomimscc:string language="en-US">{xe(course_title)}</lomimscc:string>
        </lomimscc:title>
      </lomimscc:general>
    </lomimscc:lom>
  </metadata>
  <organizations>
    <organization identifier="org_1" structure="rooted-hierarchy">
      <item identifier="LearningModules">
        <!-- module structure defined in course_settings/module_meta.xml -->
      </item>
    </organization>
  </organizations>
  <resources>{res_xml}
  </resources>
</manifest>'''

# ── Syllabus HTML ─────────────────────────────────────────────────────────────
def build_syllabus_html(course_code: str, section: str, title: str,
                        syllabus_md: str) -> str:
    body = md2html(syllabus_md) if syllabus_md else f'<h1>{xe(title)}</h1>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>{xe(title)} — Syllabus</title>
<style>
  body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; }}
  h1 {{ color: #b22222; }} h2 {{ color: #8b0000; border-bottom: 1px solid #ccc; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; }}
  th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
  th {{ background: #f0f0f0; }}
  code {{ background: #f8f8f8; padding: 2px 4px; border-radius: 3px; }}
</style>
</head>
<body>
{body}
</body>
</html>'''

# ── Page HTML Wrapper ─────────────────────────────────────────────────────────
def page_html(title: str, body_html: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>{xe(title)}</title>
<style>
  body {{ font-family: Arial, sans-serif; max-width: 960px; margin: 0 auto; padding: 20px; }}
  h1, h2, h3 {{ color: #8b0000; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; }}
  th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
  th {{ background: #f0f0f0; }}
  pre, code {{ background: #f8f8f8; padding: 2px 6px; border-radius: 3px; font-family: monospace; }}
  pre {{ padding: 12px; overflow-x: auto; }}
  blockquote {{ border-left: 4px solid #b22222; margin: 0; padding-left: 12px; color: #555; }}
</style>
</head>
<body>
{body_html}
</body>
</html>'''

# ── Main Course Builder ───────────────────────────────────────────────────────
def build_course(course_dir: Path, section: str = '40', output_dir: Path = None) -> Path:
    """
    Build an .imscc package from a course directory.
    Returns the path to the generated .imscc file.
    """
    if output_dir is None:
        output_dir = course_dir.parent / 'dist'
    output_dir.mkdir(parents=True, exist_ok=True)

    course_folder = course_dir.name  # e.g. "CIS-1310_Intro_to_Python"
    parts = course_folder.split('_', 1)
    course_code = parts[0]            # e.g. "CIS-1310"
    course_slug = parts[1] if len(parts) > 1 else course_folder  # e.g. "Intro_to_Python"
    course_slug_clean = course_slug.replace('_', ' ')  # e.g. "Intro to Python"

    syllabus_md = ''
    for syl_path in [
        course_dir / '00_Course_Information' / 'Syllabus.md',
        course_dir / 'Syllabus.md',
    ]:
        if syl_path.exists():
            syllabus_md = read(syl_path)
            break

    title_m = re.search(r'###\s+Course Syllabus:\s*(.+?)\s+-\s+', syllabus_md)
    if title_m:
        raw_title = title_m.group(1).strip()
        full_title = re.sub(r'^[A-Z]+-\d+[_\s]+', '', raw_title).replace('_', ' ').strip()
        if not full_title:
            full_title = course_slug_clean
    else:
        full_title = course_slug_clean

    canvas_title = f'{course_code}-{section}: {full_title}'
    print(f'\nBuilding: {canvas_title}')

    manifest_id   = new_id()
    course_id     = new_id()
    lab_rubric_id = new_id()
    disc_rubric_id = new_id()

    grp_quizzes   = {'id': new_id(), 'name': 'Weekly Quizzes',   'weight': 20.0, 'position': 1}
    grp_discuss   = {'id': new_id(), 'name': 'Discussions',       'weight': 20.0, 'position': 2}
    grp_labs      = {'id': new_id(), 'name': 'Lab Assignments',   'weight': 30.0, 'position': 3}
    grp_final     = {'id': new_id(), 'name': 'Final Exam',        'weight': 30.0, 'position': 4}
    groups = [grp_quizzes, grp_discuss, grp_labs, grp_final]

    module_dirs = sorted(
        [d for d in course_dir.iterdir() if d.is_dir() and re.match(r'Module_\d+', d.name)],
        key=lambda d: int(re.search(r'\d+', d.name).group())
    )
    print(f'  Found {len(module_dirs)} modules')

    zip_entries = {}       # path_in_zip -> bytes/str content
    resources   = []       # for imsmanifest.xml
    modules_data = []      # for module_meta.xml

    resources.append({'id': course_id, 'type': 'associatedcontent/imscc_xmlv1p1/learning-application-resource',
                       'href': 'course_settings/course_settings.xml',
                       'files': ['course_settings/course_settings.xml',
                                 'course_settings/module_meta.xml',
                                 'course_settings/assignment_groups.xml',
                                 'course_settings/context.xml',
                                 'course_settings/files_meta.xml',
                                 'course_settings/late_policy.xml',
                                 'course_settings/rubrics.xml',
                                 'course_settings/syllabus.html',
                                 'course_settings/media_tracks.xml',
                                 'course_settings/canvas_export.txt']})

    for mod_dir in module_dirs:
        mod_num_m = re.search(r'\d+', mod_dir.name)
        if not mod_num_m:
            continue
        mod_num = int(mod_num_m.group())
        due_at_sun = DUE_DATES_SUN.get(mod_num, DUE_DATES_SUN[16])
        due_at_wed = DUE_DATES_WED.get(mod_num, DUE_DATES_WED[16])
        print(f'  Processing Module {mod_num:02d}...', end=' ')

        # ── Reading Guide ──────────────────────────────────────────────────────
        rg_file = find_file(mod_dir, '02_Reading_Guide_*.md')
        if not rg_file:
            rg_file = find_file(mod_dir, '*Reading_Guide*.md')

        rg_md   = read(rg_file) if rg_file else f'# Module {mod_num:02d}\n\nReading guide coming soon.'
        rg_title_md = extract_title_from_md(rg_md, f'Reading Guide (M{mod_num:02d})')
        mod_topic = re.sub(r'^Reading Guide\s*[:\-—]+\s*', '', rg_title_md).strip()
        rg_canvas_title = f'Reading Guide (M{mod_num:02d}): {mod_topic}'

        rg_id   = new_id()
        rg_href = f'wiki_content/reading-guide-m{mod_num:02d}.html'
        rg_html_body = md2html(rg_md)
        rg_html_full = page_html(rg_canvas_title, rg_html_body)
        zip_entries[rg_href] = rg_html_full
        resources.append({
            'id': rg_id, 'type': 'webcontent',
            'href': rg_href, 'files': [rg_href]
        })

        # ── Lab Assignment ─────────────────────────────────────────────────────
        lab_file = find_file(mod_dir, '03_Lab_*.md')
        if not lab_file:
            lab_file = find_file(mod_dir, '*Lab*.md')

        lab_md   = read(lab_file) if lab_file else f'# Lab (M{mod_num:02d})\n\nLab instructions coming soon.'
        lab_canvas_title = f'Lab (M{mod_num:02d}): {mod_topic}'

        lab_res_id  = new_id()
        lab_asgn_id = new_id()
        lab_folder  = f'g{new_id()}'
        lab_href    = f'{lab_folder}/assignment-m{mod_num:02d}.html'
        lab_set_href = f'{lab_folder}/assignment_settings.xml'

        lab_html_body = md2html(lab_md)
        lab_html_full = page_html(lab_canvas_title, lab_html_body)
        zip_entries[lab_href]     = lab_html_full
        zip_entries[lab_set_href] = build_assignment_settings(
            lab_asgn_id, lab_rubric_id, grp_labs['id'],
            lab_canvas_title, due_at_sun, mod_num
        )
        resources.append({
            'id': lab_res_id,
            'type': 'associatedcontent/imscc_xmlv1p1/learning-application-resource',
            'href': lab_href,
            'files': [lab_href, lab_set_href]
        })

        # ── Discussion ─────────────────────────────────────────────────────────
        disc_file = find_file(mod_dir, '05_Discussion_*.md')
        if not disc_file:
            disc_file = find_file(mod_dir, '*Discussion*.md')

        disc_md   = read(disc_file) if disc_file else f'# Discussion (M{mod_num:02d})\n\nDiscussion prompt coming soon.'
        disc_canvas_title = f'Discussion (M{mod_num:02d}): {mod_topic}'

        disc_topic_id = new_id()
        disc_meta_id  = new_id()
        disc_asgn_id  = new_id()

        disc_xml_path = f'{disc_topic_id}.xml'
        disc_meta_path = f'{disc_meta_id}.xml'

        disc_html_body = md2html(disc_md)
        zip_entries[disc_xml_path] = build_discussion(disc_canvas_title, disc_html_body)
        zip_entries[disc_meta_path] = build_discussion_meta(
            disc_meta_id, disc_topic_id, disc_asgn_id,
            grp_discuss['id'], disc_rubric_id, disc_canvas_title, due_at_sun
        )

        resources.append({
            'id': disc_topic_id,
            'type': 'imsdt_xmlv1p1',
            'href': disc_xml_path,
            'files': [disc_xml_path],
            'deps': [disc_meta_id]
        })
        resources.append({
            'id': disc_meta_id,
            'type': 'associatedcontent/imscc_xmlv1p1/learning-application-resource',
            'href': disc_meta_path,
            'files': [disc_meta_path]
        })

        # ── Quiz ───────────────────────────────────────────────────────────────
        quiz_file = find_file(mod_dir, '04_Quiz_*.md')
        if not quiz_file:
            quiz_file = find_file(mod_dir, '*Quiz*.md')

        quiz_md = read(quiz_file) if quiz_file else ''
        quiz_questions = parse_quiz(quiz_md) if quiz_md else []
        quiz_canvas_title = f'Quiz (M{mod_num:02d}): {mod_topic}'

        if quiz_questions:
            pts_each = round(100.0 / len(quiz_questions), 2)
            for q in quiz_questions:
                q['points'] = pts_each
            total_pts = sum(q['points'] for q in quiz_questions)
        else:
            total_pts = 100.0

        quiz_res_id  = new_id()
        quiz_meta_res_id = new_id()
        quiz_id      = new_id()
        quiz_asgn_id = new_id()
        quiz_folder  = f'g{new_id()}'
        qti_href     = f'{quiz_folder}/assessment_qti.xml'
        qmeta_href   = f'{quiz_folder}/assessment_meta.xml'
        ncc_href     = f'non_cc_assessments/{quiz_res_id}.xml.qti'

        if quiz_questions:
            qti_xml = build_qti(quiz_id, quiz_canvas_title, quiz_questions)
        else:
            qti_xml = build_qti(quiz_id, quiz_canvas_title, [{
                'stem': f'This quiz for Module {mod_num:02d} will be added by the instructor.',
                'options': {'A': 'True', 'B': 'False', 'C': 'N/A', 'D': 'Other'},
                'correct': 'A',
                'points': 100.0,
            }])

        zip_entries[qti_href]   = qti_xml
        zip_entries[ncc_href]   = qti_xml
        zip_entries[qmeta_href] = build_assessment_meta(
            quiz_id, quiz_asgn_id, grp_quizzes['id'],
            quiz_canvas_title, due_at_sun, total_pts, mod_num
        )

        resources.append({
            'id': quiz_res_id,
            'type': 'imsqti_xmlv1p2/imscc_xmlv1p1/assessment',
            'href': qti_href,
            'files': [qti_href],
            'deps': [quiz_meta_res_id]
        })
        resources.append({
            'id': quiz_meta_res_id,
            'type': 'associatedcontent/imscc_xmlv1p1/learning-application-resource',
            'href': qmeta_href,
            'files': [qmeta_href, ncc_href]
        })

        # ── Module Meta entry ──────────────────────────────────────────────────
        mod_meta_title = f'Module {mod_num:02d}: {mod_topic}'
        modules_data.append({
            'id':       new_id(),
            'title':    mod_meta_title,
            'position': mod_num,
            'items': [
                {'item_id': new_id(), 'content_type': 'WikiPage',
                 'title': rg_canvas_title, 'res_id': rg_id},
                {'item_id': new_id(), 'content_type': 'Assignment',
                 'title': lab_canvas_title, 'res_id': lab_res_id},
                {'item_id': new_id(), 'content_type': 'DiscussionTopic',
                 'title': disc_canvas_title, 'res_id': disc_topic_id},
                {'item_id': new_id(), 'content_type': 'Quizzes::Quiz',
                 'title': quiz_canvas_title, 'res_id': quiz_res_id},
            ]
        })

        q_count = len(quiz_questions)
        print(f'  done (quiz: {q_count}q)')

    # ── Course Settings Files ──────────────────────────────────────────────────
    syllabus_html = build_syllabus_html(course_code, section, canvas_title, syllabus_md)
    zip_entries['course_settings/course_settings.xml']  = build_course_settings(course_id, canvas_title, f'{course_code}-{section}')
    zip_entries['course_settings/module_meta.xml']       = build_module_meta(modules_data)
    zip_entries['course_settings/assignment_groups.xml'] = build_assignment_groups(groups)
    zip_entries['course_settings/context.xml']           = build_context_xml(course_id, canvas_title)
    zip_entries['course_settings/files_meta.xml']        = build_files_meta()
    zip_entries['course_settings/late_policy.xml']       = build_late_policy()
    zip_entries['course_settings/rubrics.xml']           = build_rubrics_xml(lab_rubric_id, disc_rubric_id)
    zip_entries['course_settings/syllabus.html']         = syllabus_html
    zip_entries['course_settings/media_tracks.xml']      = build_media_tracks()
    zip_entries['course_settings/canvas_export.txt']     = f'course_id: {course_id}\n'
    zip_entries['imsmanifest.xml']                       = build_manifest(manifest_id, canvas_title, resources)

    # ── Write .imscc ZIP ───────────────────────────────────────────────────────
    safe_name = re.sub(r'[^\w\-]', '_', f'{course_code}_{course_slug}')
    out_path  = output_dir / f'{safe_name}_Fall2026.imscc'

    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for zpath, content in zip_entries.items():
            if isinstance(content, str):
                zf.writestr(zpath, content.encode('utf-8'))
            else:
                zf.writestr(zpath, content)

    size_kb = out_path.stat().st_size // 1024
    print(f'  >> {out_path.name} ({size_kb} KB, {len(zip_entries)} files)')
    return out_path


# ── CLI ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description='Build IMS Common Cartridge (.imscc) packages from TXWES course Markdown.'
    )
    parser.add_argument('course', nargs='?', help='Course folder name (e.g. CIS-1310_Intro_to_Python)')
    parser.add_argument('--section', default='40', help='Section number (default: 40)')
    parser.add_argument('--all', action='store_true', help='Build all courses in current directory')
    parser.add_argument('--outdir', default='dist', help='Output directory (default: dist/)')
    args = parser.parse_args()

    base_dir   = Path(__file__).parent
    output_dir = base_dir / args.outdir

    if args.all:
        course_dirs = sorted([
            d for d in base_dir.iterdir()
            if d.is_dir() and re.match(r'(?:CIS|CSC)-\d+', d.name)
        ])
        print(f'Found {len(course_dirs)} courses to build.\n')
        built = []
        failed = []
        for cd in course_dirs:
            try:
                out = build_course(cd, section=args.section, output_dir=output_dir)
                built.append(out.name)
            except Exception as e:
                failed.append((cd.name, str(e)))
                print(f'  ERROR: {e}')
        print(f'\n{"="*60}')
        print(f'Built: {len(built)}/{len(course_dirs)} courses -> {output_dir}/')
        if failed:
            print('FAILED:')
            for name, err in failed:
                print(f'  {name}: {err}')
    elif args.course:
        course_dir = base_dir / args.course
        if not course_dir.is_dir():
            matches = [d for d in base_dir.iterdir()
                       if d.is_dir() and args.course.lower() in d.name.lower()]
            if len(matches) == 1:
                course_dir = matches[0]
            elif len(matches) > 1:
                print(f'Ambiguous: {[d.name for d in matches]}')
                sys.exit(1)
            else:
                print(f'Course directory not found: {args.course}')
                sys.exit(1)
        build_course(course_dir, section=args.section, output_dir=output_dir)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()

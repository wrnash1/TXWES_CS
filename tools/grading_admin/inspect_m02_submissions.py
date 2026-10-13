import urllib.request
import json
import ssl
import re

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
ctx = ssl.create_default_context()

def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx) as r:
        return json.loads(r.read().decode())

def clean_html(raw_html):
    return re.sub(r'<.*?>', '', raw_html).strip() if raw_html else ''

print("=== CIS-3321 LAB M02 (ID: 227452) ===")
subs = get(f"{API_BASE}/courses/13089/assignments/227452/submissions?include[]=user&per_page=50")
for s in subs:
    if s.get('submitted_at'):
        uname = s.get('user', {}).get('name')
        atts = [a['display_name'] for a in s.get('attachments', [])]
        print(f"  Student: {uname} (ID: {s.get('user_id')}) | Atts: {atts} | Body: {repr(clean_html(s.get('body', ''))[:100])}")

print("\n=== CIS-4328 LAB M02 (ID: 227502) ===")
subs = get(f"{API_BASE}/courses/13090/assignments/227502/submissions?include[]=user&per_page=50")
for s in subs:
    if s.get('submitted_at'):
        uname = s.get('user', {}).get('name')
        atts = [a['display_name'] for a in s.get('attachments', [])]
        print(f"  Student: {uname} (ID: {s.get('user_id')}) | Atts: {atts}")

print("\n=== CIS-3321 DISCUSSION M02 (Topic ID: 139133) ===")
view = get(f"{API_BASE}/courses/13089/discussion_topics/139133/view")
parts = {p['id']: p.get('display_name') for p in view.get('participants', [])}
for e in view.get('view', []):
    uname = parts.get(e.get('user_id'))
    print(f"  Entry {e.get('id')} | {uname}: {clean_html(e.get('message', ''))[:150]}...")

print("\n=== CIS-4328 DISCUSSION M02 (Topic ID: 139149) ===")
view = get(f"{API_BASE}/courses/13090/discussion_topics/139149/view")
parts = {p['id']: p.get('display_name') for p in view.get('participants', [])}
for e in view.get('view', []):
    uname = parts.get(e.get('user_id'))
    print(f"  Entry {e.get('id')} | {uname}: {clean_html(e.get('message', ''))[:150]}...")

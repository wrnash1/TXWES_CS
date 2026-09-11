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
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html).strip()

def dump_topic(cid, tid, name):
    print(f"\n==================================================")
    print(f"DUMPING TOPIC: {name} (ID: {tid})")
    print(f"==================================================")
    view = get(f"{API_BASE}/courses/{cid}/discussion_topics/{tid}/view")
    participants = {p['id']: p.get('display_name') for p in view.get('participants', [])}
    for e in view.get('view', []):
        uid = e.get('user_id')
        eid = e.get('id')
        uname = participants.get(uid, f"User {uid}")
        msg = clean_html(e.get('message', ''))
        replies = e.get('replies', [])
        print(f"Entry ID: {eid} | Student: {uname} (UID: {uid}) | Replies: {len(replies)}")
        print(f"  Content: {msg[:250]}...\n")

dump_topic(13089, 139131, "Introduce Yourself")
dump_topic(13089, 139132, "Discussion M01")
dump_topic(13089, 139133, "Discussion M02")

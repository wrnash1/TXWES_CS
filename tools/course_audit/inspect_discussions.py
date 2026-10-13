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

def inspect_discussions(cid, cname):
    print(f"\n=======================================================")
    print(f"DISCUSSIONS IN {cname} (Course {cid})")
    print(f"=======================================================")
    topics = get(f"{API_BASE}/courses/{cid}/discussion_topics?per_page=50")
    for t in topics:
        title = t.get('title')
        tid = t.get('id')
        msg_count = t.get('discussion_subentry_count', 0)
        # Check if there are posts
        if msg_count > 0 or 'Introduce' in title or 'M01' in title or 'M02' in title:
            print(f"\nTopic: '{title}' (ID: {tid}) | Messages: {msg_count}")
            # get view
            view = get(f"{API_BASE}/courses/{cid}/discussion_topics/{tid}/view")
            participants = {p['id']: p.get('display_name') for p in view.get('participants', [])}
            entries = view.get('view', [])
            print(f"  Total Top-Level Posts: {len(entries)}")
            for e in entries[:4]:
                user_name = participants.get(e.get('user_id'), f"User {e.get('user_id')}")
                msg = e.get('message', '')
                print(f"    - [{user_name}]: {repr(msg[:100])}...")

inspect_discussions(13089, "CIS-3321")
inspect_discussions(13090, "CIS-4328")

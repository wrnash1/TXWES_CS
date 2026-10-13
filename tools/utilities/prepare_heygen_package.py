# -*- coding: utf-8 -*-
"""
Prepares HeyGen-ready speech files for all 78 video lectures across all 3 courses.
Outputs to: /home/wrnash1/Developer/TXWES_CS/HeyGen_Uploads/
  - Pure speech .txt files with stage directions & markdown stripped
  - Scene-by-scene .json files for HeyGen multi-scene projects
  - Quick-start guide for HeyGen video generation
"""

import json, re, os
from pathlib import Path

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "HeyGen_Uploads"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

COURSES = [
    {
        "id": "CIS-3321",
        "folder": "CIS-3321_Network_Admin",
        "name": "CIS-3321 Network Administration",
        "dir": BASE_DIR / "completed" / "CIS-3321_Network_Admin"
    },
    {
        "id": "CIS-4328",
        "folder": "CIS-4328_Information_Security",
        "name": "CIS-4328 Information Security",
        "dir": BASE_DIR / "completed" / "CIS-4328_Information_Security"
    },
    {
        "id": "CSC-6361",
        "folder": "CSC-6361_Computer_Networks",
        "name": "CSC-6361 Advanced Computer Networks",
        "dir": BASE_DIR / "CSC-6361_Computer_Networks"
    }
]

def clean_speech_text(raw_text: str) -> str:
    t = raw_text
    # Remove stage directions, slide cues, diagram descriptions, alt-text
    t = re.sub(r'\[SHOW.*?\]', '', t, flags=re.DOTALL | re.IGNORECASE)
    t = re.sub(r'\[Alt-text:.*?\]', '', t, flags=re.DOTALL | re.IGNORECASE)
    t = re.sub(r'\[Diagram:.*?\]', '', t, flags=re.DOTALL | re.IGNORECASE)
    t = re.sub(r'\[Table:.*?\]', '', t, flags=re.DOTALL | re.IGNORECASE)
    t = re.sub(r'\[Illustration:.*?\]', '', t, flags=re.DOTALL | re.IGNORECASE)
    t = re.sub(r'\[.*?ON CAMERA.*?\]', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\[VOICEOVER.*?\]', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\[DEMONSTRATION.*?\]', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\[TRANSITION.*?\]', '', t, flags=re.IGNORECASE)
    # Remove timestamps like [00:00 – 01:30]
    t = re.sub(r'\[\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2}\]', '', t)
    # Remove markdown headers and horizontal rules
    t = re.sub(r'^#+.*$', '', t, flags=re.M)
    t = re.sub(r'---+', '', t)
    # Remove markdown bold/italics symbols
    t = re.sub(r'\*{1,3}', '', t)
    t = re.sub(r'_{1,3}', '', t)
    t = re.sub(r'`{1,3}', '', t)
    # Clean links [text](url) -> text
    t = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', t)
    # Remove table formatting pipes
    t = re.sub(r'\|', ' ', t)
    # Normalize spacing and paragraphs
    paras = [p.strip() for p in t.split('\n\n') if p.strip()]
    # Filter out empty or header-only leftovers
    clean_paras = []
    for p in paras:
        # Avoid lines like "Section 1: Welcome"
        if re.match(r'^(Section \d+:|Pre-Roll Slide|Estimated Duration|Recorded by:)', p, re.I):
            continue
        clean_paras.append(p)
    return '\n\n'.join(clean_paras)

def parse_scenes(raw_text: str):
    sections = re.split(r'\n(?=###?\s+)', raw_text)
    scenes = []
    for sec in sections:
        sec = sec.strip()
        if not sec: continue
        heading_m = re.search(r'^###?\s+(.+)$', sec, re.M)
        title = heading_m.group(1).strip() if heading_m else "Scene"
        
        slide_m = re.search(r'\[SHOW SLIDE:\s*(.+?)\]', sec, re.DOTALL)
        slide_prompt = slide_m.group(1).replace('\n', ' ').strip() if slide_m else f"Topic: {title}"
        
        speech = clean_speech_text(sec)
        if speech:
            scenes.append({
                "scene_title": title,
                "slide_background_prompt": slide_prompt,
                "speech_script": speech
            })
    return scenes

total_files_generated = 0

for c in COURSES:
    course_out = OUTPUT_DIR / c["folder"]
    course_out.mkdir(parents=True, exist_ok=True)
    
    scripts = sorted(c["dir"].glob("Module_*/01_Video_Script*.md"))
    print(f"Processing {c['name']} ({len(scripts)} scripts)...")
    
    for sfile in scripts:
        mod_m = re.search(r'Module_(\d+)', sfile.parent.name)
        if not mod_m: continue
        mod_num = int(mod_m.group(1))
        part = 1 if "Part_1" in sfile.name or "part1" in sfile.name.lower() else 2
        
        raw_text = sfile.read_text(encoding='utf-8')
        speech = clean_speech_text(raw_text)
        scenes = parse_scenes(raw_text)
        
        prefix = f"M{mod_num:02d}_Part_{part}"
        
        # 1. Save Full Speech Text File
        txt_path = course_out / f"{prefix}_HeyGen_Speech.txt"
        txt_path.write_text(speech, encoding='utf-8')
        
        # 2. Save Scene-by-Scene JSON File
        json_path = course_out / f"{prefix}_Scenes.json"
        json_path.write_text(json.dumps(scenes, indent=2), encoding='utf-8')
        
        total_files_generated += 2

# Write a HeyGen Step-by-Step Readme
readme_path = OUTPUT_DIR / "README_HeyGen_Instructions.md"
readme_path.write_text('''# 🎬 HeyGen Video Generation Quick-Start Guide for Professor Nash

These files have been generated and pre-cleaned specifically for uploading into **[HeyGen.com](https://www.heygen.com)** to create your course videos with your photo avatar.

---

## 📁 What is Inside These Folders:
For every module in **CIS-3321**, **CIS-4328**, and **CSC-6361**:
1. **`*_HeyGen_Speech.txt`**: The complete spoken text for that lecture. All stage cues, timestamps, and markdown formatting have been stripped out so the AI voice reads it with 100% natural pronunciation without saying "bracket" or "slide".
2. **`*_Scenes.json`**: Scene-by-scene breakdown indicating the slide visual prompt and matching dialogue for multi-scene video projects.

---

## 🚀 3-Step HeyGen Video Creation Flow:

### Step 1: Set Up Your TalkingPhoto & Voice (One-time setup)
1. Log in to [HeyGen.com](https://www.heygen.com).
2. Go to **Avatars &rarr; Photo Avatar** &rarr; Upload a high-resolution professional headshot of yourself.
3. Go to **Voices &rarr; Clone Voice** &rarr; Record 1–2 minutes reading any paragraph from these scripts. HeyGen will clone your real voice!

### Step 2: Create the Lecture Video
1. Click **Create Video &rarr; 16:9 Landscape**.
2. Select your custom **Photo Avatar** and place it in the bottom-right corner.
3. Open the corresponding `.txt` file (e.g. `M01_Part_1_HeyGen_Speech.txt`) and paste the text into the HeyGen script box.
4. (Optional) Set the background to match the slide prompt in `*_Scenes.json` or use Texas Wesleyan maroon branding.

### Step 3: Export & Add to Canvas
1. Click **Generate** in HeyGen.
2. Download the resulting `.mp4` video.
3. Upload the video to **Canvas Studio** (or YouTube) and embed it directly onto the module's lecture video page in Canvas!
''', encoding='utf-8')

print(f"\n✅ SUCCESS: Generated {total_files_generated} HeyGen-ready files in:")
print(f"   {OUTPUT_DIR}")

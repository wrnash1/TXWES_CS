# -*- coding: utf-8 -*-
"""
Builds the Standalone Teleprompter & Slide Deck Studio Web App
Aggregates all 83 video scripts from CIS-3321, CIS-4328, and CSC-6361.
Outputs:
  - /home/wrnash1/Developer/TXWES_CS/Teleprompter_Studio.html
  - /home/wrnash1/.gemini/antigravity/brain/c1239228-60f2-4111-9f86-91a2627ea801/teleprompter_studio.html
"""

import json, re, os
from pathlib import Path

BASE_DIR = Path(__file__).parent
BRAIN_DIR = Path("/home/wrnash1/.gemini/antigravity/brain/c1239228-60f2-4111-9f86-91a2627ea801")

COURSES_CONFIG = [
    {
        "id": "CIS-3321",
        "name": "CIS-3321: Network Administration",
        "dir": BASE_DIR / "completed" / "CIS-3321_Network_Admin",
        "badge": "CompTIA Network+ & CCNA"
    },
    {
        "id": "CIS-4328",
        "name": "CIS-4328: Information Security",
        "dir": BASE_DIR / "completed" / "CIS-4328_Information_Security",
        "badge": "Security+ & ISC2 CC"
    },
    {
        "id": "CSC-6361",
        "name": "CSC-6361: Advanced Computer Networks",
        "dir": BASE_DIR / "CSC-6361_Computer_Networks",
        "badge": "Cisco CCNP Enterprise"
    }
]

def parse_markdown_script(file_path: Path):
    text = file_path.read_text(encoding="utf-8")
    
    # Extract title
    title_m = re.search(r"^#\s+(.+)$", text, re.M)
    title = title_m.group(1).strip() if title_m else file_path.stem
    
    # Extract duration
    dur_m = re.search(r"Duration:\s*([^\n\r]+)", text, re.I)
    duration = dur_m.group(1).strip() if dur_m else "12–15 minutes"
    
    # Split by headings
    raw_sections = re.split(r"\n(?=###?\s+)", text)
    sections = []
    
    for raw in raw_sections:
        raw = raw.strip()
        if not raw:
            continue
            
        heading_m = re.search(r"^###?\s+(.+)$", raw, re.M)
        sec_title = heading_m.group(1).strip() if heading_m else "Introduction"
        
        # Avoid pre-roll or empty
        time_m = re.search(r"\[(\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2})\]", raw)
        timestamp = time_m.group(1) if time_m else ""
        
        slide_m = re.search(r"\[SHOW SLIDE:\s*(.+?)\]", raw, re.DOTALL)
        slide_prompt = slide_m.group(1).replace("\n", " ").strip() if slide_m else ""
        
        # Clean speech text
        clean = re.sub(r"\[SHOW SLIDE:.*?\]", "", raw, flags=re.DOTALL)
        clean = re.sub(r"\[\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2}\]", "", clean)
        clean = re.sub(r"^###?.*$", "", clean, flags=re.M)
        clean = re.sub(r"---+", "", clean)
        clean_paras = [p.strip() for p in clean.split("\n\n") if p.strip()]
        
        if clean_paras or slide_prompt:
            sections.append({
                "title": sec_title,
                "timestamp": timestamp,
                "slide_prompt": slide_prompt or f"Discussion: {sec_title}",
                "paragraphs": clean_paras
            })
            
    return {
        "title": title,
        "duration": duration,
        "sections": sections
    }

def gather_all_data():
    database = {}
    
    for conf in COURSES_CONFIG:
        cid = conf["id"]
        cname = conf["name"]
        cdir = conf["dir"]
        database[cid] = {
            "name": cname,
            "badge": conf["badge"],
            "modules": {}
        }
        
        mod_dirs = sorted([d for d in cdir.iterdir() if d.is_dir() and d.name.startswith("Module_")])
        for mdir in mod_dirs:
            m_num_m = re.search(r"Module_(\d+)", mdir.name)
            if not m_num_m: continue
            mod_num = int(m_num_m.group(1))
            
            scripts = sorted(mdir.glob("*Video_Script*.md"))
            for sfile in scripts:
                part = 1 if "Part_1" in sfile.name or "part1" in sfile.name.lower() else 2
                key = f"M{mod_num:02d}_P{part}"
                parsed = parse_markdown_script(sfile)
                parsed["module"] = mod_num
                parsed["part"] = part
                database[cid]["modules"][key] = parsed

    return database

def build_html_app(data):
    json_data = json.dumps(data)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Texas Wesleyan Video Recording Studio &amp; Teleprompter</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    /* Custom Scrollbar for Teleprompter */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: #0f172a; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #475569; }}
    
    .mirrored {{
      transform: scaleX(-1);
    }}
    
    .eye-line {{
      position: absolute;
      top: 38%;
      left: 0;
      right: 0;
      height: 2px;
      background: rgba(239, 68, 68, 0.4);
      pointer-events: none;
      z-index: 20;
    }}
    .eye-line::after {{
      content: "👁️ CAMERA EYE-LEVEL GUIDE";
      position: absolute;
      right: 20px;
      top: -10px;
      font-size: 10px;
      font-weight: bold;
      color: rgba(239, 68, 68, 0.8);
      background: #0f172a;
      padding: 0 6px;
      border-radius: 4px;
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans select-none">

  <!-- TOP HEADER & CONTROLS -->
  <header class="bg-slate-900 border-b border-slate-800 px-6 py-3 flex flex-wrap items-center justify-between gap-4 sticky top-0 z-50">
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-lg bg-red-800 flex items-center justify-center font-bold text-white shadow">
        TW
      </div>
      <div>
        <h1 class="text-base font-bold text-white flex items-center gap-2">
          Professor Nash Lecture Studio
          <span class="text-xs bg-red-900 text-red-200 px-2 py-0.5 rounded border border-red-700">Teleprompter &amp; Slides</span>
        </h1>
        <p class="text-xs text-slate-400">Texas Wesleyan University · Computer Science &amp; IT</p>
      </div>
    </div>

    <!-- SELECTORS -->
    <div class="flex items-center gap-2">
      <!-- Course Selector -->
      <select id="courseSelect" class="bg-slate-800 border border-slate-700 text-sm rounded-lg px-3 py-1.5 text-slate-200 focus:ring-2 focus:ring-red-600 focus:outline-none">
        <option value="CIS-3321">CIS-3321: Network Administration</option>
        <option value="CIS-4328" selected>CIS-4328: Information Security</option>
        <option value="CSC-6361">CSC-6361: Advanced Computer Networks</option>
      </select>

      <!-- Module & Part Selector -->
      <select id="lectureSelect" class="bg-slate-800 border border-slate-700 text-sm rounded-lg px-3 py-1.5 text-slate-200 focus:ring-2 focus:ring-red-600 focus:outline-none max-w-xs truncate">
      </select>
    </div>

    <!-- VIEW MODE TABS -->
    <div class="flex bg-slate-800 p-1 rounded-lg border border-slate-700 text-xs">
      <button id="modeStudioBtn" onclick="setMode('studio')" class="px-3 py-1.5 rounded-md font-medium bg-red-800 text-white shadow">
        📺 Dual Studio
      </button>
      <button id="modePrompterBtn" onclick="setMode('prompter')" class="px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-white">
        📜 Full Prompter
      </button>
      <button id="modeSlidesBtn" onclick="setMode('slides')" class="px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-white">
        📽️ Slide Deck
      </button>
    </div>
  </header>

  <!-- TELEPROMPTER FLOATING TOOLBAR -->
  <div class="bg-slate-900/95 backdrop-blur border-b border-slate-800 px-6 py-2 flex flex-wrap items-center justify-between gap-4 text-xs text-slate-300">
    <!-- Playback -->
    <div class="flex items-center gap-2">
      <button id="playPauseBtn" onclick="toggleScroll()" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-1.5 rounded flex items-center gap-1.5 shadow transition">
        <span id="playIcon">▶</span> <span id="playText">Start (Space)</span>
      </button>
      <button onclick="resetScroll()" class="bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1.5 rounded border border-slate-700 transition">
        ⏮ Reset
      </button>
    </div>

    <!-- Speed Slider -->
    <div class="flex items-center gap-2">
      <span class="text-slate-400">Scroll Speed:</span>
      <input type="range" id="speedSlider" min="1" max="10" value="3" class="w-24 accent-red-600 cursor-pointer">
      <span id="speedVal" class="font-mono bg-slate-800 px-1.5 py-0.5 rounded text-amber-400">3x</span>
    </div>

    <!-- Font Size Slider -->
    <div class="flex items-center gap-2">
      <span class="text-slate-400">Font Size:</span>
      <input type="range" id="fontSlider" min="20" max="64" value="34" class="w-24 accent-red-600 cursor-pointer">
      <span id="fontVal" class="font-mono bg-slate-800 px-1.5 py-0.5 rounded text-amber-400">34px</span>
    </div>

    <!-- Mirror Mode & Timer -->
    <div class="flex items-center gap-4">
      <label class="flex items-center gap-1.5 cursor-pointer">
        <input type="checkbox" id="mirrorCheckbox" onchange="toggleMirror()" class="rounded accent-red-600">
        <span>Mirror Glass</span>
      </label>

      <div class="font-mono bg-slate-950 px-2.5 py-1 rounded border border-slate-800 text-amber-400 flex items-center gap-2">
        <span>⏱️</span>
        <span id="timerText">00:00</span>
        <span class="text-slate-500 text-[10px]" id="targetDuration">/ 15:00</span>
      </div>
    </div>
  </div>

  <!-- MAIN WORKSPACE -->
  <main class="flex-1 flex overflow-hidden relative" id="workspace">

    <!-- LEFT PANE: TELEPROMPTER -->
    <section id="prompterPane" class="flex-1 relative bg-black flex flex-col overflow-hidden transition-all duration-300 border-r border-slate-800">
      <div class="eye-line"></div>
      
      <!-- Scrolling Text Container -->
      <div id="prompterScrollArea" class="flex-1 overflow-y-auto px-12 py-32 scroll-smooth text-slate-100" style="font-size: 34px; line-height: 1.75;">
        <div id="prompterContent" class="max-w-3xl mx-auto space-y-10">
          <!-- Populated by JS -->
        </div>
      </div>
    </section>

    <!-- RIGHT PANE: PRESENTATION SLIDE DECK -->
    <section id="slidesPane" class="w-1/2 bg-slate-900 flex flex-col overflow-hidden transition-all duration-300">
      
      <!-- Slide Presentation Canvas -->
      <div class="flex-1 p-6 flex flex-col justify-center items-center overflow-auto">
        <div id="slideCard" class="w-full max-w-2xl aspect-[16/9] bg-gradient-to-br from-red-950 via-slate-900 to-slate-950 border-2 border-red-800 rounded-2xl shadow-2xl p-8 flex flex-col justify-between relative overflow-hidden">
          
          <!-- Slide Watermark Background -->
          <div class="absolute -right-10 -bottom-10 opacity-5 pointer-events-none text-9xl font-black text-white">
            TWU
          </div>

          <!-- Slide Header -->
          <div class="flex justify-between items-start border-b border-red-800/40 pb-3">
            <div>
              <span id="slideBadge" class="text-xs font-bold text-amber-400 uppercase tracking-widest">TEXAS WESLEYAN UNIVERSITY</span>
              <h2 id="slideCourseName" class="text-sm font-semibold text-slate-300">Information Security</h2>
            </div>
            <div class="text-right">
              <span id="slideTime" class="text-xs font-mono bg-red-900/60 text-red-200 px-2 py-0.5 rounded border border-red-700">00:00</span>
            </div>
          </div>

          <!-- Slide Main Content Area -->
          <div class="my-auto py-4">
            <h3 id="slideTitle" class="text-2xl font-black text-white mb-3 tracking-tight">
              Slide Title
            </h3>
            <div id="slideVisualBox" class="bg-slate-950/80 border border-red-900/40 rounded-xl p-4 text-sm text-slate-200 shadow-inner">
              <p id="slidePromptText" class="leading-relaxed text-amber-200 font-medium">
                [Slide Visual Prompt]
              </p>
            </div>
          </div>

          <!-- Slide Footer -->
          <div class="flex justify-between items-center border-t border-red-800/40 pt-3 text-xs text-slate-400">
            <span>Professor William Nash</span>
            <span id="slideCounter" class="font-mono text-amber-400 font-bold">Slide 1 of 5</span>
          </div>

        </div>
      </div>

      <!-- Slide Navigation Controls Bar -->
      <div class="bg-slate-950 border-t border-slate-800 px-6 py-3 flex items-center justify-between">
        <button onclick="prevSlide()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 px-4 py-2 rounded text-xs font-semibold flex items-center gap-1 transition">
          ◀ Previous Slide
        </button>
        <span class="text-xs text-slate-400">Navigate: Arrow Keys (← / →)</span>
        <button onclick="nextSlide()" class="bg-red-800 hover:bg-red-700 text-white px-4 py-2 rounded text-xs font-semibold flex items-center gap-1 transition shadow">
          Next Slide ▶
        </button>
      </div>

    </section>

  </main>

  <!-- DATABASE SCRIPT -->
  <script>
    const COURSE_DB = {json_data};

    let currentCourse = "CIS-4328";
    let currentLectureKey = "";
    let currentLectureData = null;
    let currentSlideIndex = 0;
    
    let isScrolling = false;
    let scrollInterval = null;
    let scrollSpeed = 3;
    let timerSeconds = 0;
    let timerInterval = null;

    // Elements
    const courseSelect = document.getElementById("courseSelect");
    const lectureSelect = document.getElementById("lectureSelect");
    const prompterScrollArea = document.getElementById("prompterScrollArea");
    const prompterContent = document.getElementById("prompterContent");
    const speedSlider = document.getElementById("speedSlider");
    const speedVal = document.getElementById("speedVal");
    const fontSlider = document.getElementById("fontSlider");
    const fontVal = document.getElementById("fontVal");
    const mirrorCheckbox = document.getElementById("mirrorCheckbox");
    const timerText = document.getElementById("timerText");
    const targetDuration = document.getElementById("targetDuration");
    const playPauseBtn = document.getElementById("playPauseBtn");
    const playIcon = document.getElementById("playIcon");
    const playText = document.getElementById("playText");

    // Slide Elements
    const slideCourseName = document.getElementById("slideCourseName");
    const slideTime = document.getElementById("slideTime");
    const slideTitle = document.getElementById("slideTitle");
    const slidePromptText = document.getElementById("slidePromptText");
    const slideCounter = document.getElementById("slideCounter");

    // Initialization
    window.addEventListener("DOMContentLoaded", () => {{
      populateLectureSelect();
      loadCurrentLecture();
      
      // Event Listeners
      courseSelect.addEventListener("change", (e) => {{
        currentCourse = e.target.value;
        populateLectureSelect();
        loadCurrentLecture();
      }});

      lectureSelect.addEventListener("change", (e) => {{
        currentLectureKey = e.target.value;
        loadCurrentLecture();
      }});

      speedSlider.addEventListener("input", (e) => {{
        scrollSpeed = parseInt(e.target.value);
        speedVal.innerText = scrollSpeed + "x";
      }});

      fontSlider.addEventListener("input", (e) => {{
        const size = e.target.value;
        prompterScrollArea.style.fontSize = size + "px";
        fontVal.innerText = size + "px";
      }});

      // Keyboard Shortcuts
      window.addEventListener("keydown", (e) => {{
        if (e.code === "Space") {{
          e.preventDefault();
          toggleScroll();
        }} else if (e.code === "ArrowRight") {{
          nextSlide();
        }} else if (e.code === "ArrowLeft") {{
          prevSlide();
        }} else if (e.code === "KeyR") {{
          resetScroll();
        }}
      }});
    }});

    function populateLectureSelect() {{
      const course = COURSE_DB[currentCourse];
      if (!course) return;
      
      lectureSelect.innerHTML = "";
      const keys = Object.keys(course.modules).sort();
      keys.forEach((k) => {{
        const lec = course.modules[k];
        const opt = document.createElement("option");
        opt.value = k;
        opt.innerText = `M${{lec.module < 10 ? '0' + lec.module : lec.module}} Part ${{lec.part}}: ${{lec.title.substring(0, 45)}}...`;
        lectureSelect.appendChild(opt);
      }});
      currentLectureKey = keys[0];
    }}

    function loadCurrentLecture() {{
      resetScroll();
      const course = COURSE_DB[currentCourse];
      currentLectureData = course.modules[currentLectureKey];
      if (!currentLectureData) return;

      targetDuration.innerText = `/ ${{currentLectureData.duration}}`;
      renderPrompterText();
      currentSlideIndex = 0;
      updateSlideDisplay();
    }}

    function renderPrompterText() {{
      prompterContent.innerHTML = "";
      
      currentLectureData.sections.forEach((sec, idx) => {{
        const secDiv = document.createElement("div");
        secDiv.className = "mb-14 border-b border-slate-800/80 pb-8";
        
        const header = document.createElement("div");
        header.className = "flex items-center justify-between text-base font-bold text-red-400 mb-4 tracking-wide uppercase";
        header.innerHTML = `<span>SECTION ${{idx + 1}}: ${{sec.title}}</span><span class="font-mono bg-red-950 px-2 py-0.5 rounded text-amber-300">${{sec.timestamp || ''}}</span>`;
        secDiv.appendChild(header);

        if (sec.slide_prompt) {{
          const cue = document.createElement("div");
          cue.className = "text-xs font-semibold text-amber-300 bg-amber-950/40 border-l-4 border-amber-500 px-3 py-2 rounded mb-6";
          cue.innerText = `📺 SLIDE CUE: ${{sec.slide_prompt}}`;
          secDiv.appendChild(cue);
        }}

        sec.paragraphs.forEach((para) => {{
          const p = document.createElement("p");
          p.className = "mb-6 text-slate-200 leading-relaxed font-medium";
          p.innerText = para;
          secDiv.appendChild(p);
        }});

        prompterContent.appendChild(secDiv);
      }});
    }}

    function updateSlideDisplay() {{
      if (!currentLectureData || !currentLectureData.sections.length) return;
      const sec = currentLectureData.sections[currentSlideIndex];
      const total = currentLectureData.sections.length;

      slideCourseName.innerText = COURSE_DB[currentCourse].name;
      slideTime.innerText = sec.timestamp || "00:00";
      slideTitle.innerText = sec.title;
      slidePromptText.innerText = sec.slide_prompt || "Discussion & Demonstration: " + sec.title;
      slideCounter.innerText = `Slide ${{currentSlideIndex + 1}} of ${{total}}`;
    }}

    function nextSlide() {{
      if (!currentLectureData) return;
      if (currentSlideIndex < currentLectureData.sections.length - 1) {{
        currentSlideIndex++;
        updateSlideDisplay();
      }}
    }}

    function prevSlide() {{
      if (currentSlideIndex > 0) {{
        currentSlideIndex--;
        updateSlideDisplay();
      }}
    }}

    function toggleScroll() {{
      isScrolling = !isScrolling;
      if (isScrolling) {{
        playPauseBtn.className = "bg-amber-600 hover:bg-amber-500 text-white font-semibold px-4 py-1.5 rounded flex items-center gap-1.5 shadow transition";
        playIcon.innerText = "⏸";
        playText.innerText = "Pause (Space)";
        
        scrollInterval = setInterval(() => {{
          prompterScrollArea.scrollTop += (scrollSpeed * 0.85);
        }}, 30);

        if (!timerInterval) {{
          timerInterval = setInterval(() => {{
            timerSeconds++;
            const mins = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
            const secs = String(timerSeconds % 60).padStart(2, '0');
            timerText.innerText = `${{mins}}:${{secs}}`;
          }}, 1000);
        }}
      }} else {{
        playPauseBtn.className = "bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-1.5 rounded flex items-center gap-1.5 shadow transition";
        playIcon.innerText = "▶";
        playText.innerText = "Start (Space)";
        clearInterval(scrollInterval);
      }}
    }}

    function resetScroll() {{
      isScrolling = false;
      clearInterval(scrollInterval);
      clearInterval(timerInterval);
      timerInterval = null;
      timerSeconds = 0;
      timerText.innerText = "00:00";
      playPauseBtn.className = "bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-1.5 rounded flex items-center gap-1.5 shadow transition";
      playIcon.innerText = "▶";
      playText.innerText = "Start (Space)";
      prompterScrollArea.scrollTop = 0;
    }}

    function toggleMirror() {{
      if (mirrorCheckbox.checked) {{
        prompterScrollArea.classList.add("mirrored");
      }} else {{
        prompterScrollArea.classList.remove("mirrored");
      }}
    }}

    function setMode(mode) {{
      const prompterPane = document.getElementById("prompterPane");
      const slidesPane = document.getElementById("slidesPane");
      const modeStudioBtn = document.getElementById("modeStudioBtn");
      const modePrompterBtn = document.getElementById("modePrompterBtn");
      const modeSlidesBtn = document.getElementById("modeSlidesBtn");

      // Reset tabs
      [modeStudioBtn, modePrompterBtn, modeSlidesBtn].forEach(b => {{
        b.className = "px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-white";
      }});

      if (mode === "studio") {{
        modeStudioBtn.className = "px-3 py-1.5 rounded-md font-medium bg-red-800 text-white shadow";
        prompterPane.style.display = "flex";
        prompterPane.className = "flex-1 relative bg-black flex flex-col overflow-hidden border-r border-slate-800";
        slidesPane.style.display = "flex";
        slidesPane.className = "w-1/2 bg-slate-900 flex flex-col overflow-hidden";
      }} else if (mode === "prompter") {{
        modePrompterBtn.className = "px-3 py-1.5 rounded-md font-medium bg-red-800 text-white shadow";
        prompterPane.style.display = "flex";
        prompterPane.className = "w-full relative bg-black flex flex-col overflow-hidden";
        slidesPane.style.display = "none";
      }} else if (mode === "slides") {{
        modeSlidesBtn.className = "px-3 py-1.5 rounded-md font-medium bg-red-800 text-white shadow";
        prompterPane.style.display = "none";
        slidesPane.style.display = "flex";
        slidesPane.className = "w-full bg-slate-900 flex flex-col overflow-hidden";
      }}
    }}
  </script>
</body>
</html>
'''
    return html

def main():
    print("Gathering script data from courses...")
    data = gather_all_data()
    print(f"Loaded courses: {list(data.keys())}")
    for k, v in data.items():
        print(f"  - {k}: {len(v['modules'])} lecture scripts loaded.")
        
    html = build_html_app(data)
    
    # Save local copy
    local_path = BASE_DIR / "Teleprompter_Studio.html"
    local_path.write_text(html, encoding="utf-8")
    print(f"✅ Saved local studio app: {local_path}")
    
    # Save artifact copy
    artifact_path = BRAIN_DIR / "teleprompter_studio.html"
    artifact_path.write_text(html, encoding="utf-8")
    print(f"✅ Saved artifact studio app: {artifact_path}")

if __name__ == "__main__":
    main()

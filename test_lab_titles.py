from pathlib import Path
import re

base = Path("/home/wrnash1/Developer/TXWES_CS")

def get_lab_titles(cdir):
    titles = {}
    for mdir in sorted(cdir.glob("Module_*")):
        m_num = int(re.search(r"Module_(\d+)", mdir.name).group(1))
        labs = list(mdir.glob("03_Lab*.md"))
        if labs:
            txt = labs[0].read_text(encoding="utf-8")
            tm = re.search(r"Lab Title:\*?\*?\s*(.+)", txt)
            h1 = re.search(r"^#\s+(.+)", txt, re.M)
            t = tm.group(1).strip() if tm else (h1.group(1).strip() if h1 else f"Module {m_num:02d} Lab")
            t = re.sub(r"[*_`#]", "", t).strip()
            # Clean leading prefixes like "Lab Activity — Module 01: "
            t = re.sub(r"^(Lab Activity\s*[-—:]*\s*Module\s*\d+\s*[-—:]*\s*)", "", t, flags=re.I)
            t = re.sub(r"^(Lab Assignment\s*[-—:]*\s*Module\s*\d+\s*[-—:]*\s*)", "", t, flags=re.I)
            t = re.sub(r"^(Lab:\s*Module\s*\d+\s*[-—:]*\s*)", "", t, flags=re.I)
            titles[m_num] = t.strip()
    return titles

t3321 = get_lab_titles(base / "completed" / "CIS-3321_Network_Admin")
t4328 = get_lab_titles(base / "completed" / "CIS-4328_Information_Security")
t6361 = get_lab_titles(base / "CSC-6361_Computer_Networks")

print("CIS-3321 Lab Titles:")
for k, v in sorted(t3321.items()):
    print(f"  M{k:02d}: {v}")

print("\nCIS-4328 Lab Titles:")
for k, v in sorted(t4328.items()):
    print(f"  M{k:02d}: {v}")

print("\nCSC-6361 Lab Titles:")
for k, v in sorted(t6361.items()):
    print(f"  M{k:02d}: {v}")

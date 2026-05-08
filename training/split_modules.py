import os
import glob
import re

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
content_files = glob.glob(os.path.join(base_dir, "CIS-*", "Module_*", "Module_*_Content.md"))

for filepath in content_files:
    mod_dir = os.path.dirname(filepath)
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    parts = re.split(r'\n### ', content)
    if len(parts) <= 1:
        continue # Doesn't match expected format
        
    # parts[0] is the header
    header = parts[0].strip()
    
    # Create subdirectories if they don't exist
    os.makedirs(os.path.join(mod_dir, "01_Video_Scripts"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "02_Reading_Guides"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "03_Activities"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "Assessments"), exist_ok=True)
    
    for part in parts[1:]:
        lines = part.strip().split('\n')
        title_line = lines[0]
        
        # Clean title for filename
        clean_title = re.sub(r'[^\w\s-]', '', title_line).strip().replace(' ', '_')
        
        target_dir = None
        if "Video" in title_line or "Script" in title_line:
            target_dir = "01_Video_Scripts"
        elif "Reading" in title_line or "Guide" in title_line:
            target_dir = "02_Reading_Guides"
        elif "Lab" in title_line or "Activity" in title_line:
            target_dir = "03_Activities"
        elif "Quiz" in title_line or "Assessment" in title_line:
            target_dir = "Assessments"
        else:
            target_dir = "03_Activities" # default fallback
            
        out_path = os.path.join(mod_dir, target_dir, f"{clean_title}.md")
        with open(out_path, 'w') as out_f:
            out_f.write(f"### {part.strip()}\n")
            
    # Remove original monolithic file
    os.remove(filepath)
    
print("Splitting complete.")

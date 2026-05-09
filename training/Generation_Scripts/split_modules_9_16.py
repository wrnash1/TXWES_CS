import os
import glob
import re

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
content_files = glob.glob(os.path.join(base_dir, "CIS-*", "Module_1*", "Module_*_Content.md")) + glob.glob(os.path.join(base_dir, "CIS-*", "Module_09", "Module_*_Content.md"))

for filepath in content_files:
    mod_dir = os.path.dirname(filepath)
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    os.makedirs(os.path.join(mod_dir, "01_Video_Scripts"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "02_Reading_Guides"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "03_Activities"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "Assessments"), exist_ok=True)

    current_file = None
    current_content = []
    
    for line in lines:
        if line.startswith("**Video Script") or line.startswith("**Reading"):
            if current_file and current_content:
                with open(current_file, 'w') as out_f:
                    out_f.write("".join(current_content))
            
            clean_title = re.sub(r'[^\w\s-]', '', line).strip().replace(' ', '_')
            target_dir = "01_Video_Scripts" if "Video" in line else "02_Reading_Guides"
            current_file = os.path.join(mod_dir, target_dir, f"{clean_title}.md")
            current_content = [line]
            
        elif line.startswith("**Lab"):
            if current_file and current_content:
                with open(current_file, 'w') as out_f:
                    out_f.write("".join(current_content))
                    
            clean_title = re.sub(r'[^\w\s-]', '', line).strip().replace(' ', '_')
            current_file = os.path.join(mod_dir, "03_Activities", f"{clean_title}.md")
            current_content = [line]
            
        elif line.startswith("**Quiz"):
            if current_file and current_content:
                with open(current_file, 'w') as out_f:
                    out_f.write("".join(current_content))
                    
            clean_title = re.sub(r'[^\w\s-]', '', line).strip().replace(' ', '_')
            current_file = os.path.join(mod_dir, "Assessments", f"{clean_title}.md")
            current_content = [line]
        else:
            if current_file:
                current_content.append(line)
                
    if current_file and current_content:
        with open(current_file, 'w') as out_f:
            out_f.write("".join(current_content))

    os.remove(filepath)
    
print("Splitting 9-16 complete.")

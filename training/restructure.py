import os
import glob
import re

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
courses = glob.glob(os.path.join(base_dir, "CIS-*"))

for course in courses:
    # Handle Modules 5-8
    file_5_8 = os.path.join(course, "Modules_05_to_08_Content.md")
    if os.path.exists(file_5_8):
        with open(file_5_8, 'r') as f:
            content = f.read()
        
        # Split by "## Module "
        parts = re.split(r'\n## Module (\d+):[^\n]*\n', content)
        
        # parts[0] is header, parts[1] is '5', parts[2] is content, parts[3] is '6', parts[4] is content, etc.
        header = parts[0]
        for i in range(1, len(parts), 2):
            mod_num = int(parts[i])
            mod_content = parts[i+1]
            
            mod_dir = os.path.join(course, f"Module_{mod_num:02d}")
            os.makedirs(mod_dir, exist_ok=True)
            
            with open(os.path.join(mod_dir, f"Module_{mod_num:02d}_Content.md"), 'w') as out_f:
                out_f.write(header + f"\n## Module {mod_num}\n" + mod_content.strip() + "\n")
                
        os.remove(file_5_8)
        
    # Handle Modules 9-16
    file_9_16 = os.path.join(course, "Modules_09_to_16_Content.md")
    if os.path.exists(file_9_16):
        with open(file_9_16, 'r') as f:
            content = f.read()
        
        parts = re.split(r'\n## Module (\d+):[^\n]*\n', content)
        
        header = parts[0]
        for i in range(1, len(parts), 2):
            mod_num = int(parts[i])
            mod_content = parts[i+1]
            
            mod_dir = os.path.join(course, f"Module_{mod_num:02d}")
            os.makedirs(mod_dir, exist_ok=True)
            
            with open(os.path.join(mod_dir, f"Module_{mod_num:02d}_Content.md"), 'w') as out_f:
                out_f.write(header + f"\n## Module {mod_num}\n" + mod_content.strip() + "\n")
                
        os.remove(file_9_16)

print("Restructuring complete.")

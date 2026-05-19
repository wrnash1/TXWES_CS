#!/usr/bin/env python3
import os
import re
import sys
import shutil
import glob

# Constants
BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
CATEGORIES = {
    1: ("01", "Video_Script"),
    2: ("02", "Reading_Guide"),
    3: ("03", "Lab"),
    4: ("04", "Quiz")
}

def clean_original_filename(filename):
    """
    Remove leading digits, spaces, and separators from the filename.
    e.g., "1_Video_Script.md" -> "Video_Script.md"
          "5_Quiz_Module_01.md" -> "Quiz_Module_01.md"
    """
    # Pattern to match leading digits followed by underscores, spaces, or dashes
    cleaned = re.sub(r'^\d+[\s_-]*', '', filename)
    return cleaned

def classify_file(filepath):
    """
    Determine the category of a file based on its name, parent folder, and content.
    Returns (category_id, category_name)
    """
    filename = os.path.basename(filepath).lower()
    parent_dir = os.path.basename(os.path.dirname(filepath)).lower()
    
    # Check explicit keywords in filename first to correct misplaced files
    if 'reading' in filename or 'guide' in filename or 'ztc_oer' in filename:
        return 2, 'Reading_Guide'
    if 'quiz' in filename or 'assessment' in filename or 'question_bank' in filename or 'distractor' in filename:
        return 4, 'Quiz'
    if 'lab' in filename or 'activity' in filename or 'submission' in filename or 'applied' in filename:
        return 3, 'Lab'
    if 'video' in filename or 'script' in filename:
        return 1, 'Video_Script'
        
    # Fallback to parent directory
    if 'video' in parent_dir:
        return 1, 'Video_Script'
    if 'reading' in parent_dir:
        return 2, 'Reading_Guide'
    if 'activit' in parent_dir:
        return 3, 'Lab'
    if 'assess' in parent_dir:
        return 4, 'Quiz'
        
    # Fallback to content check
    try:
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read(2048) # Read first 2KB
            content_lower = content.lower()
            if '### video script' in content_lower or 'video script:' in content_lower:
                return 1, 'Video_Script'
            if '### reading guide' in content_lower or 'reading guide:' in content_lower:
                return 2, 'Reading_Guide'
            if '### lab' in content_lower or 'lab activity' in content_lower or 'applied skills' in content_lower:
                return 3, 'Lab'
            if '### quiz' in content_lower or 'question bank' in content_lower or 'correct answer:' in content_lower:
                return 4, 'Quiz'
    except Exception:
        pass
        
    # Default fallback to Lab
    return 3, 'Lab'

def get_root_quizzes(course_path):
    """
    Scan root-level Assessments directory (e.g. in Network Admin) and map quizzes to modules.
    Returns a dict mapping module_num (int) -> list of file paths.
    """
    root_quizzes = {}
    assessments_dir = os.path.join(course_path, "Assessments")
    if os.path.exists(assessments_dir):
        for root, _, files in os.walk(assessments_dir):
            for file in files:
                if file.endswith('.md'):
                    fpath = os.path.join(root, file)
                    # Try to extract module number from filename
                    # e.g., Quiz_1_Domain_1.md -> Module 1
                    match = re.search(r'Quiz_(\d+)', file, re.IGNORECASE)
                    if match:
                        mod_num = int(match.group(1))
                        root_quizzes.setdefault(mod_num, []).append(fpath)
    return root_quizzes

def main():
    dry_run = "--execute" not in sys.argv
    if dry_run:
        print("=== DRY RUN MODE: No files will be moved or deleted. Run with '--execute' to perform changes. ===")
    else:
        print("=== EXECUTION MODE: Performing directory flattening and restructuring. ===")

    courses = sorted(glob.glob(os.path.join(BASE_DIR, "CIS-*")))
    
    total_files_moved = 0
    total_files_skipped = 0
    moves_planned = []
    
    for course_path in courses:
        course_name = os.path.basename(course_path)
        print(f"\nProcessing Course: {course_name}")
        
        # 1. Identify any root-level quizzes
        root_quizzes = get_root_quizzes(course_path)
        
        # Keep track of destinations to prevent name collisions
        planned_destinations = set()
        
        # 2. Reorganize Modules 01 to 16
        for mod_idx in range(1, 17):
            mod_dir_name = f"Module_{mod_idx:02d}"
            mod_path = os.path.join(course_path, mod_dir_name)
            
            if not os.path.exists(mod_path):
                continue
                
            # Collect all files that should end up in this module folder
            files_to_process = []
            
            # Walk current module folder
            for root, dirs, files in os.walk(mod_path):
                for file in files:
                    filepath = os.path.join(root, file)
                    files_to_process.append(filepath)
            
            # Add any root-level quizzes mapped to this module
            if mod_idx in root_quizzes:
                for qpath in root_quizzes[mod_idx]:
                    files_to_process.append(qpath)
                    print(f"  Found root quiz for {mod_dir_name}: {os.path.basename(qpath)}")
            
            # Plan restructuring for files in this module
            for src_path in sorted(files_to_process):
                # Don't process files that are already outside Modules or at course level
                # (e.g. ZTC_OER_Reading_Materials.md at course root - wait, walk inside Module folder will not include it anyway,
                # but root-level quizzes will be included).
                
                cat_id, cat_name = classify_file(src_path)
                prefix = CATEGORIES[cat_id][0]
                
                orig_filename = os.path.basename(src_path)
                cleaned_name = clean_original_filename(orig_filename)
                new_filename = f"{prefix}_{cleaned_name}"
                
                # Check for duplicate destinations within this module
                dest_path = os.path.join(mod_path, new_filename)
                if dest_path in planned_destinations:
                    base, ext = os.path.splitext(new_filename)
                    counter = 2
                    while True:
                        alt_filename = f"{base}_{counter}{ext}"
                        alt_dest_path = os.path.join(mod_path, alt_filename)
                        if alt_dest_path not in planned_destinations:
                            new_filename = alt_filename
                            dest_path = alt_dest_path
                            break
                        counter += 1
                
                planned_destinations.add(dest_path)
                
                if src_path == dest_path:
                    total_files_skipped += 1
                else:
                    moves_planned.append((src_path, dest_path))
                    total_files_moved += 1

    # Print summary of planned moves
    print(f"\nTotal moves planned: {total_files_moved}")
    print(f"Total files already in correct position: {total_files_skipped}")
    
    if dry_run:
        # Print a sample of moves
        print("\nSample of planned file moves:")
        for src, dest in moves_planned[:20]:
            print(f"  [MOVE] {os.path.relpath(src, BASE_DIR)} \n      -> {os.path.relpath(dest, BASE_DIR)}")
        if len(moves_planned) > 20:
            print(f"  ... and {len(moves_planned) - 20} more moves.")
    else:
        # Execute the moves
        print("\nExecuting moves...")
        for src, dest in moves_planned:
            # Ensure dest dir exists (in case we are moving root-level quizzes)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            # Move the file
            shutil.move(src, dest)
            print(f"  Moved: {os.path.basename(src)} -> {os.path.relpath(dest, BASE_DIR)}")
            
        # Clean up empty directories bottom-up
        print("\nCleaning up empty directories...")
        for course_path in courses:
            for root, dirs, files in os.walk(course_path, topdown=False):
                for d in dirs:
                    dir_path = os.path.join(root, d)
                    # Don't delete Course Info or Modules even if empty (though they shouldn't be empty)
                    if d == "00_Course_Information" or d.startswith("Module_"):
                        continue
                    try:
                        if not os.listdir(dir_path):
                            os.rmdir(dir_path)
                            print(f"  Removed empty directory: {os.path.relpath(dir_path, BASE_DIR)}")
                    except Exception as e:
                        print(f"  Error removing directory {dir_path}: {e}")
                        
            # Specifically check and delete root Assessments if empty
            root_assess = os.path.join(course_path, "Assessments")
            if os.path.exists(root_assess):
                try:
                    for root, dirs, files in os.walk(root_assess, topdown=False):
                        for d in dirs:
                            os.rmdir(os.path.join(root, d))
                    os.rmdir(root_assess)
                    print(f"  Removed empty root Assessments folder for {os.path.basename(course_path)}")
                except Exception:
                    pass

        print("\n=== Restructuring Complete ===")

if __name__ == "__main__":
    main()

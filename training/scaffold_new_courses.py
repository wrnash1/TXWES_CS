import os

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
new_courses = ["CIS-4330_Intro_to_AI", "CIS-4331_Azure_Cloud"]

for course in new_courses:
    course_path = os.path.join(base_dir, course)
    os.makedirs(os.path.join(course_path, "00_Course_Information"), exist_ok=True)
    
    for i in range(1, 17):
        mod_dir = os.path.join(course_path, f"Module_{i:02d}")
        if i < 16:
            os.makedirs(os.path.join(mod_dir, "01_Video_Scripts"), exist_ok=True)
            os.makedirs(os.path.join(mod_dir, "Assessments"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "02_Reading_Guides"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "03_Activities"), exist_ok=True)

print("Scaffolded new courses.")

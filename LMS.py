SYSTEM_INFO=("LMS Students portal","v1.0","2025","edify university")
ADMIN_INFO=("admin@edify.ai","9550739077","200")
print("="*50)
print(f"welcome to {SYSTEM_INFO[0]}")
print(f"developed by {SYSTEM_INFO[3]}")
print("="*50)
students={}
#start with option selection
while True:
    print("Choose an option from (1-5): ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List All Students")
    print("5 - Exit System")
    
    choice = input("Enter Your Choice: ")
    
    if choice == "1":
        print("Performing Operation 1")
        student_id = input("Enter Student ID: ")
        # student exists
        if student_id in students:
            print("Student Already with this ID exists in system!")
        else:
            name = input("Enter Student Name: ").title()
            # store multiple scores
            scores = []
            while True:
                score_input = input("Enter a score or type done: ")
                # validate if input is number or done
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Score should be between 0-100")
                else:
                   print("Score should be Number Only") 
        
            # store multiple unique skills
            skills = set()
            while True:
                skill_input = input("Enter a skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title())
            
            # save student details received so far
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Added Successfully!")
            
            # For Verification print student
            print(students)
                       
    elif choice == "2":
        print("Performing Operation 2")
        student_id = input("Enter Student ID To Modify: ")
        if student_id in students:
            new_name = input("Enter New Name To Update: ").title()
            students[student_id]["name"] = new_name
            print("Student Updated Successfully!")
        else:
            print("Student ID Doesn't Exist!")
        print(students)
        
    elif choice == "3":
        print("Performing Operation 3")
        student_id = input("Enter Student ID To Delete: ")
        removed = students.pop(student_id,None)
        if removed:
            print("Student Removed Successfully!")
        else:
            print("Student ID Doesn't Exist!")
        print(students)
        
    elif choice == "4":
        print("Performing Operation 4")
    elif choice == "5":
        print("Performing Operation 5")
        break
    else:
       print("Invalid Choice Only (1-5) available") 




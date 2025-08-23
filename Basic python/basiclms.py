student_ID_valid=False 
while not student_ID_valid:
    student_ID = input("Enter student ID: ")
    if student_ID.isdigit() :
        student_ID = int(student_ID)
        if student_ID > 0:
            student_ID_valid = True
        else:
            print("plese input non-zero values")
    else:
        print("enter only numbers")
#formating ID
formatted_student_ID ="STU" + str(student_ID).zfill(5)
print(f"Formatted Student ID: {formatted_student_ID}")

#validate student name
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter student name: ")
    student_name=student_name.strip().title()   #strip will remove front and back spaces
  #check name should have only alphabets
    name_check = student_name.replace(" ","")
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print(name_check)
    else:
        print("Please enter a valid name with at least 3 characters and only alphabets.")
#email generation
name_part=student_name.split()
first_name=name_part[0].lower()
student_email = first_name + "."+ str(student_ID) + "@school.com"
print(f"Generated Student Email: {student_email}")

#discount calculation
base_course_fee_valid= False
while not base_course_fee_valid:
    base_course_fee= input("Enter base course fee: ")
    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("Please enter a non-zero value for the base course fee.")
    else:
        print("Please enter a valid number for the base course fee.")
discount = 0
description=input("Enter discount description: ")
if description.lower().find("reference")!= -1:
    discount +=5000
if "scholarship" in description:
    discount += 7000
if "promo" in description:
    discount += 3000
final_course_fee = base_course_fee - discount
print(f"Base Course Fee: {base_course_fee}")
print(f"Discount Applied: {discount}")
print(f"Final Course Fee: {final_course_fee}")



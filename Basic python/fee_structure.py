student_name = (input("enter student name: "))
student_grade = int(input("enter student grade level :"))
academic_toppers_status = (input("Academic Status: "))
base_tuition_fee = int(input("Base tuition fee: "))
discount_percentage = 0
if  student_grade >= 1 and student_grade <=12:
       print("Valid student grade")
else :
        print("student grades are invalid")
if  student_grade >= 9 and student_grade <=12:
       if academic_toppers_status == "yes" :
              discount_percentage = 20
       else:       
             discount_percentage = 10
if  student_grade >= 6 and student_grade <=8 :
       discount_percentage = 5
elif student_grade <6:
       add_discount = 0
elif student_grade == 10:
       add_discount = 3
elif student_grade == 12:
       add_discount = 5
else:
       add_discount = 0
total_discount = discount_percentage + add_discount
discount_amount = base_tuition_fee * (total_discount / 100)
final_fee = base_tuition_fee - discount_amount
academic_toppers_status = "yes" if academic_toppers_status == "yes" else "no"
print(f"Student Name: {student_name}")
print(f"Student Grade: {student_grade}")
print(f"Academic Toppers Status: {academic_toppers_status}")
print(f"Base Tuition Fee: {base_tuition_fee}")
print(f"Total Discount: {total_discount}%")
print(f"Final Tuition Fee: {final_fee}")
print(f"{total_discount}%")
print(f"{discount_amount}")
print(f"{final_fee}")


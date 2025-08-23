student_ID=100
student_Name="Syam"
student_Age=25
Quiz_score=75
assignment_score=85
Exam_score=80
student_attendance=65
total_score=Quiz_score+assignment_score+Exam_score
average_score=total_score/3  #or we can write 3 also as static
#student passed
student_passed=average_score>=75
#student attendance
student_attendance +=1
#award eligibility
award_eligibility = student_attendance >= 90 and student_passed
# Print student details
print(f"Student Name: {student_Name}")
print(f"total score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Student Passed: {student_passed}")
print(f"Student Attendance: {student_attendance}")
print(f"Award Eligibility: {award_eligibility}")
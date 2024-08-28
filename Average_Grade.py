student_grades = {
  'Alice': (50,35,64),
  'Bob': (70,22,40), 
  'Charlie': (31, 21,10),
  'David': (80,85,90)
  }

def average_grade(student_dictionary):
  for student, grade in student_dictionary.items():
     average = sum(grade) // len(grade)
     print(f"Average Grade for {student}: {average}")


average_grade(student_grades)
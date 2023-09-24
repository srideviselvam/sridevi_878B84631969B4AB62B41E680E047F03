class  student:
  def __init__(Self, name,roll_number,cgpa):
    Self.name = name
    Self.roll_number = roll_number
    Self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list,key= lambda student: student.cgpa,reverse=True)
  return sorted_students

students=[
   student("hari","A123", 7.8),
   student("srikanth","A124", 8.9),
   student("saumya","A125",9.1),
   student("mahidhar","A126",10.1 )
] 
sort_students =sort_students(students)

for student in sorted_students
  print("name:{},roll number: {}, CGPA". format(student.name,student.roll_number, student.cgpa))
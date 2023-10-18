class Student:

  def__init__(self,name, roll_number,cgpa):
  self.name = NameError
  self.roll_number=roll_number
self.cgpa=cgpa


def sort_students(Student_list):
  #sort tha list of students  descending order of CGPA
  sorted_students=sorted(student_list,key=lambda student:student.  
cgpa,
                         reverse =True)
  #Syntax_lambda arg :exp
  return  sorted_students 


#Example  usage 
students = [
  Student ("Hari",""A123",7.8),
  Student ("Srikanth","A124",8.9),
  Student (Saumya","A125",9.1),
  Student ("Mahidhar",A126",9.9),
 ]
 
 sorted_students=sort_students(students)
 
 #Print the sorted list of students
 for student in sorted_students
 print("Name:{},Roll Number:{},CGPA:{}".format (student.name,:  student  roll_number,
        student.cgpa))"

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

#instances
student1 = Student("S001", "A")
student2 = Student("S002", "B")
student3 = Student("S003", "C")
student4 = Student("S004", "D")
student5 = Student("S005", "E")

teacher1 = Teacher("T001", "อ.อรฉัตร")
teacher2 = Teacher("T002", "อ.ธนา")
teacher3 = Teacher("T003", "อ.ศักดิ์ชัย")

subject1 = Subject("OOP16", "OOP1", "Section 1", 3)
subject2 = Subject("OOP17", "OOP2", "Section 2", 3)
subject3 = Subject("CAL17", "CAL", "Section 1", 3)

subject1.student = [student1, student2, student3]
subject2.student = [student3, student4, student5]
subject3.student = [student1, student2, student3, student4]

subject1.teacher = teacher1
subject2.teacher = teacher2
subject3.teacher = teacher3

def find_student_by_teacher(teacher_id):
    student_list = []
    for subject in [subject1, subject2, subject3]:
        if subject.teacher.teacher_id == teacher_id:
            return [student.student_name for student in subject.student]

def find_subject_by_student(student_id):
    subject_list = []
    for subject in [subject1, subject2, subject3]:
        if student_id in [student.student_id for student in subject.student]:
            subject_list.append(subject.subject_name)
    return subject_list

#print("------------------------------")
#print(subject3.teacher.teacher_name)
print("------------------------------")
print(find_student_by_teacher("T002"))
print("------------------------------")
print(find_subject_by_student("S001"))
print("------------------------------")



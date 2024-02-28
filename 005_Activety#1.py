class Student:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name

    def get_student_id(self):
        return self.__student_id

    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, value):
        if value.isalpha():
            self.__student_name = value
        else:
            print("Invalid name. Please enter an English alphabetic name.")

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__section = section
        self.__credit = credit

    def get_subject_id(self):
        return self.__subject_id

    def get_subject_name(self):
        return self.__subject_name

    def get_section(self):
        return self.__section

    def get_credit(self):
        return self.__credit

    def student(self):
        return self.__student

    def set_student(self, students):
        self.__student = students

    def get_teacher(self):
        return self.__teacher

    def set_teacher(self, teacher):
        self.__teacher = teacher

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name

    def get_teacher_id(self):
        return self.__teacher_id

    def get_teacher_name(self):
        return self.__teacher_name

    def set_teacher_name(self, value):
        if value.isalpha():
            self.__teacher_name = value
        else:
            print("Invalid name. Please enter an English alphabetic name.")

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



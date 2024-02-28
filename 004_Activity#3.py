class Student:

    def __init__(self, student_id, student_name, student_year):
        self.student_id = student_id
        self.student_name = student_name
        self.student_year = student_year
        self.student_menter = None

    def menter(self):
        return self.student_menter

#instances
student1 = Student("66000000", "A", 1)
student2 = Student("65000000", "B", 2)
student3 = Student("64000000", "C", 3)
student4 = Student("63000000", "D", 4)
#student5 = Student("00000000", "E", 0)

student1.student_menter = student2
student2.student_menter = student3
student3.student_menter = student4

student_list = [student1, student2, student3, student4]

def find_student_menter(student_id):
    student_list = [student1, student2, student3, student4]
    menter_list = []

    for student in student_list:
        if student.student_id == student_id:
            menter = student.student_menter
            while menter:
                menter_list.append((menter.student_id, menter.student_name))
                menter = menter.student_menter
            return menter_list
    return None

def true_false_menter(student_x, student_y):
    for student in student_list:
        while student_x.menter and student_y.menter:
            if student_x.student_id == student_y.student_id:
                return True
            student_y = student_x.student_menter
            student_x = student_y.student_menter
        return False


student_id = "66000000"
student_menter = find_student_menter(student_id)
print(student_menter)

result = true_false_menter(student1, student2)
print(result)



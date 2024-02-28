# สร้าง Class Student ที่ Attribute ทุกตัวเป็น private
class Student:
    # มี parameter student_id, student_name
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name

    # สร้าง getter ของ student_id และ student_name
    @property
    def student_id(self) :
        return self.__student_id  

    @property
    def student_name(self):
        return self.__student_name

# สร้าง Class Subject ที่ Attribute ทุกตัวเป็น private
class Subject:
    # มี parameter subject_id, subject_name, credit
    def __init__(self, subject_id, subject_name, credit):
        self.__subject_id = subject_id      
        self.__subject_name = subject_name
        self.__credit = credit

    # สร้าง getter id, name, credit, assign_teacher, teacher
    def get_subject_id(self):
        return self.__subject_id

    def get_subject_name(self):
        return self.__subject_name

    def get_credit(self):
        return self.__credit

    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

    subject_id = property(get_subject_id)
    subject_name = property(get_subject_name)
    credit = property(get_credit)
    teacher = property(get_teacher)

# สร้าง Class Teacher ที่ Attribute ทุกตัวเป็น private
class Teacher:
    # มี parameter teacher_id, teacher_name
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name

    # สร้าง getter ของ teacher_name(มีที่จำเป็นอันเดียว)
    @property
    def teacher_name(self):
        return self.__teacher_name

#สร้าง Class Enrollment ที่มี attribute ทุกตัวเป็นแบบ private
class Enrollment:
    # มี parameter student, subject กำหนด grade เป็น None
    def __init__(self, student, subject):
        self.__student = student
        self.__subject = subject
        self.__grade = None

    # สร้าง getter ของ student, subject, grade   
    @property
    def student(self):
        return self.__student
    
    @property
    def subject(self):
        return self.__subject
    
    @property
    def grade(self):
        return self.__grade
    
    # function set_grade โดยมีการตรวจสอบว่าเกรดเป็นตัวอักษรภาษาอังกฤษหรือไม่ และเกรดใช่ a หรือ b หรือ c หรือ d หรือ f
    @grade.setter
    def grade(self, student_grade):
        if student_grade.isalpha() and (student_grade in {'A','B','C','D','F'}) :
            self.__grade = student_grade
        else :
            raise ValueError("Invalid Grade")

# สร้าง List ว่าง ดังนี้
student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id):
    # วน loop ใน subject_list เพื่อหาวิชาที่มีรหัสวิชาตรงกันของรหัสปัจจุบันกับรหัสที่ระบุ
    for subject in subject_list:
        if subject.subject_id == subject_id:
            #ถ้ารหัสวิชาตรงกันให้ return วิชานั้นออกมา
            return subject 
    #ถ้าไม่ตรงให้ return None
    return None

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    #วน loop ใน student_list เพื่อหานักเรียนที่มีรหัสตรงกันขังรหัสปัจจุบันกับรหัสที่ระบุ
    for student in student_list:
        if student.student_id == student_id:
            #ถ้ารหัสตรงกันให้ return นักเรียนคนนั้นออกมา
            return student
    #ถ้าไม่ตรงให้ return None
    return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student, subject):
    if isinstance(student, Student) and isinstance(subject, Subject):
        # วน loop ใน enrollment_list เพื่อตรวจสอบว่านักเรียนลงทะเบียนในรายวิชานั้นแล้วยัง
        for enrollment in enrollment_list:
            if student == enrollment.student and subject == enrollment.subject:
                # ถ้าลงแล้วให้ return ดังนี้
                return "Already Enrolled"
        # ถ้ายังให้เพิ่ม object เข้าไป
        enrollment_list.append(Enrollment(student, subject))
        # เพิ่มเสร็จเรียบร้อย return Done
        return "Done"
    else:
        # ถ้าไม่ได้รับ Instance ของ student และ subject ให้ return Error
        return "Error"

# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject):
    #ถ้า student และ subject ไม่เป็น instance ให้คืนค่า 'Error'
    if not isinstance(student, Student) or not isinstance(subject,Subject):
        return 'Error'
    #ถ้า student และ subject เป็น instance ให้ลูป object ใน enrollment_list
    for enrollment in enrollment_list:
        #ถ้ามี object student และ subject ในลิสให้ลบออก
        if student == enrollment.student and subject == enrollment.subject:
            enrollment_list.remove(enrollment)
    #ถ้าไม่มีให้คืนค่า 'Not Found'
    return 'Not Found'

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student):
    #ลูปในลิสลงทะเบียนแล้วตรวจหาวิชาที่ตรงกับที่ต้องการแล้วคืนค่า instance ของ Enroll นั้น ถ้าไม่มีอันที่ตรงกันจะคืนค่า 'Not found'
    for enrollment in enrollment_list:
        if enrollment.subject == subject and enrollment.student == student:
            return enrollment
    return 'Not Found'

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject):
    #สร้างลิสต์เพื่อเก็บ instance ของ Enroll ที่ต้องการ
    enrollment_student = []
    # ลูป enrollment_list ตรวจว่านักศึกษาลงทะเบียนในรายวิชาที่กำหนดไหม ถ้ามีให้เพิ่ม instance ลงในลิสต์ enrollment_student
    for enrollment in enrollment_list:
        if enrollment.subject == subject:
            enrollment_student.append(enrollment)
    # return List ของ instance
    return enrollment_student

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student):
    # สร้างลิสเพื่อเก็บ instance ของ Enroll ที่ต้องการ
    enrollment_subject = []
    # ลูป enrollment_list ตรวจว่านักศึกษาที่ลงทะเบียนวิชานี้ตรงกับนักศึกษาที่ต้องการหาไหม ถ้าตรงให้เพิ่ม instance ลงในลิสต์ enrollment_student
    for enrollment in enrollment_list:
        if enrollment.student == student:
            enrollment_subject.append(enrollment)
    # คืนค่าเป็นลิส enrollment_subject
    return enrollment_subject 

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    # ลูปใน enrollment_list
    for enrollment in enrollment_list:
        # ตรวจว่านักศึกษาและรายวิชาตรงกับที่กำลังค้นหาไหม ถ้าตรงให้กำหนดเกรดให้นักศึกษาแล้วคือค่า 'Done' ถ้าไม่ตรงเงื่อนไขคืนค่า 'Not Found'
        if enrollment.student == student and enrollment.subject == subject:
            enrollment.grade = grade
            return 'Done'
    return 'Not Found'

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search):
    # วน loop ใน subject_list เพื่อหาอาจารย์ที่สอนในรายวิชานั้น
    for subject in subject_list:
        if subject == subject_search: 
            # ถ้ามีให้ส่งค่าคืนเป็น instance ของอาจารย์ที่สอนวิชานั้น
            return subject.teacher
    # ไม่เจอให้คืนค่า Not Found
    return 'Not Found'

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject):
    return len(search_student_enroll_in_subject(subject))

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student):
    # สร้างตัวแปร student_data เป็น dict เก็บข้อมูลการลงทะเบียนและผลการเรียนของนักศึกษา
    student_data = {}
    # ลูปใน enrollment_list
    for enrollment in enrollment_list:
        # ตรวจสอบว่านักศึกษาตรงกับที่กำลังค้นหาไหม ถ้าตรงเพิ่มข้อมูลการลงทะเบียนและผลการเรียนของนักศึกษาใน student_data
        if enrollment.student == student:
            student_data[enrollment.subject.subject_id] = enrollment.subject.subject_name, enrollment.grade
    # คืนค่า student_data
    return student_data

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    # กำหนดตัวแปร
    total_credits = 0
    total_grade_points = 0

    # วน loop ใน enrollment_list
    # ถ้านักเรียนตรงกับที่กำหนดไว้และมีเกรด จะคำนวน total_grade_points total_credits
    for enrollment in enrollment_list:
        if enrollment.student == student and enrollment.grade is not None:
            total_grade_points += grade_to_count(enrollment.grade) * enrollment.subject.credit
            total_credits += enrollment.subject.credit

    if total_credits == 0:
        return 0
    else:
        return total_grade_points / total_credits

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    # ค้นหาวิชาจากรหัสวิชา
    subject = search_subject_by_id(subject_id)
    # ถ้า ไม่มีวิชา ให้ return Subject not found
    if subject is None:
        return "Subject not found"
    # สร้างตัวแปร filter_student_list เป็นการค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    # วน loop enrollment ใน filter_student_list
    for enrollment in filter_student_list:
        # สร้าง dict ที่มีชื่อ : รหัส
        student_dict[enrollment.student.student_id] = enrollment.student.student_name
    # return dict ที่สร้างไว้
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = self.search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.subject.subject_id] = enrollment.subject.subject_name
    return subject_dict

#######################################################################################

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 4))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()

# ### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

# ### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

# ### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

# ### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

# ### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].subject_id))
print("")

# ### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.student.student_id for i in lst])
print("")

# ### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.subject.subject_id for i in lst])
print("")

# ### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).teacher_name)
print("")

# ### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.subject.subject_id,enroll.student.student_id)
print("")

# ### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

# ### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1]))
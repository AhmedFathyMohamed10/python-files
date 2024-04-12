class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"Courses enrolled by {self.name}:")
        for course in self.courses:
            print(course)

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"{self.course_id}: {self.name}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student_id, course_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            student.enroll(course)
            print(f"{student.name} has been enrolled in {course.name}.")
        else:
            print("Student or course not found.")

    def display_student_courses(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.display_courses()
        else:
            print("Student not found.")


# Usage example:
# Create students
student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

# Create courses
course1 = Course(101, "Math")
course2 = Course(102, "Science")
course3 = Course(103, "Computer Science")

# Create student management system
sms = StudentManagementSystem()

# Add students and courses to the system
sms.add_student(student1)
sms.add_student(student2)
sms.add_course(course1)
sms.add_course(course2)
sms.add_course(course3)

# Enroll students in courses
sms.enroll_student(1, 101)
sms.enroll_student(1, 102)
sms.enroll_student(1, 103)
sms.enroll_student(2, 102)
sms.enroll_student(2, 103)

# Display courses for a student
sms.display_student_courses(1)
sms.display_student_courses(2)
sms.display_student_courses(6) #Student not found.

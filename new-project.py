class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.age}, {self.address}"

class Teacher(Person):
    def __init__(self, name, age, address, department, subjects):
        super().__init__(name, age, address)
        self.department = department
        self.subjects = subjects

    def teach(self, subject):
        return f"{self.name} is teaching {subject}"

class Student(Person):
    def __init__(self, name, age, address, course, semester):
        super().__init__(name, age, address)
        self.course = course
        self.semester = semester
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.code}), {self.credits} credits"

class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.courses = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []
        self.teachers = []

    def add_department(self, department):
        self.departments.append(department)

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

# Example usage:

university = University("National textile university")

department_TE = Department("Textile Engineering")
university.add_department(department_TE)

teacher_Dr_kashif = Teacher("Dr kashif", 45, "123 Main St", department_TE.name, ["Engineering", "Textile processing"])
department_TE.add_teacher(teacher_Dr_kashif)
university.add_teacher(teacher_Dr_kashif)

course_Engineering = Course("Engineering", "TE 101", 3)
department_TE.add_course(course_Engineering)

student_Faisal = Student("Faisal", 25, "125-c Faisalabad ", course_Engineering.name, 2)
university.add_student(student_Faisal)
student_Faisal.add_grade("Engineering", 90)

print(university.name)
print(department_TE.name)
print(teacher_Dr_kashif.teach("Engineering"))
print(student_Faisal)
print(student_Faisal.get_average_grade())
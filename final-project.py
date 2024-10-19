# University class
class University:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)
        print(f"Faculty '{faculty.name}' has been added to the university.")

    def display_faculties(self):
        print(f"Faculties in {self.name}:")
        for faculty in self.faculties:
            print(f"- {faculty.name}")

    def __str__(self):
        return f"University: {self.name}, : {self.place}"

# Define the Faculty class
class Faculty:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' has been added to the faculty '{self.name}'.")

    def display_students(self):
        print(f"Students in the faculty of {self.name}:")
        for student in self.students:
            print(f"- {student.name}")

    def _str_(self):
        return f"Faculty: {self.name}, Department: {self.department}"

# Define the Student class
class Student:
    def __init__(self, name, student_id, year):
        self.name = name
        self.student_id = student_id
        self.year = year

    def _str_(self):
        return f"Student: {self.name}, ID: {self.student_id}, Year: {self.year}"

# Main program to demonstrate the system
def main():
    # Create a university
    university = University("National Textile University ", "Faisalabad")

    # Create some faculties
    faculty1 = Faculty("Engineering", "Computer Science")
    faculty2 = Faculty("Business", "Finance")

    # Add faculties to the university
    university.add_faculty(faculty1)
    university.add_faculty(faculty2)

    # Create some students
    student1 = Student("Maryam", "67895", 2)
    student2 = Student("Marie", "57221", 1)
    student3 = Student("Meem", "12345", 3)

    # Add students to faculties
    faculty1.add_student(student1)
    faculty1.add_student(student2)
    faculty2.add_student(student3)

    # Display university details
    print(university)
    university.display_faculties()

    # Display faculty details
    print("\nFaculty Details:")
    faculty1.display_students()
    faculty2.display_students()

# Run the main function
if __name__ == "__main__":
    main()
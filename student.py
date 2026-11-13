from dataclasses import dataclass

@dataclass
class Student:
    name: str
    section: str


print("Student Management System")

def print_name(name: str):
    print("Student name:", name)

def print_section(section: str):
    print("Student section:", section)

_student = Student("Inu Chetry", "3B")
print_name(_student.name)
print_section(_student.section)

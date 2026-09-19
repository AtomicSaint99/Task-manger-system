# Student Marks Management System

students = {}

# Add student
def add_student(name, marks):
    students[name] = marks
    print(f"{name} added successfully!")
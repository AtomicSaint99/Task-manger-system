# Student Marks Management System

students = {}

# Add student
def add_student(name, marks):
    students[name] = marks
    print(f"{name} added successfully!")

# View all students
def view_students():
    if not students:
        print("No records found.")
    else:
        print("\nStudent Records:")
        for name, marks in students.items():
            print(f"{name}: {marks}")
# Update marks
def update_marks(name, new_marks):
    if name in students:
        students[name] = new_marks
        print(f"{name}'s marks updated!")
    else:
        print("Student not found.")
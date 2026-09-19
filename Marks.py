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

# Delete student
def delete_student(name):
    if name in students:
        del students[name]
        print(f"{name} deleted successfully!")
    else:
        print("Student not found.")

# Main menu
while True:
    print("\n--- Student Marks Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter student name: ")
        new_marks = int(input("Enter new marks: "))
        update_marks(name, new_marks)

    elif choice == "4":
        name = input("Enter student name: ")
        delete_student(name)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
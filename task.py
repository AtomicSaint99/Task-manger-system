tasks = []

def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added")

def view_tasks():
    for task in tasks:
        print(task)

class Task:
    def __init__(self, name, description, priority, due_date):
        self.name = name
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

# Create an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (high, medium, low): ")
    due_date = input("Enter task due date: (yyyy-mm-dd)")
    task = Task(name, description, priority, due_date)
    tasks.append(task)

# Function to remove a task
def remove_task():
    name = input("Enter task name to remove: ")
    for task in tasks:
        if task.name == name:
            tasks.remove(task)
            break

# Function to mark a task as completed
def mark_completed():
    name = input("Enter task name to mark as completed: ")
    for task in tasks:
        if task.name == name:
            task.completed = True
            break

# Function to display tasks
def display_tasks():
    for task in tasks:
        print(f"Task: {task.name}")
        print(f"Description: {task.description}")
        print(f"Priority: {task.priority}")
        print(f"Due Date: {task.due_date}")
        print(f"Completed: {task.completed}")
        print()

# Main loop
while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

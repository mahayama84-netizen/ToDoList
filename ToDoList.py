import json
import os

FILE_NAME = "tasks.json"

# ------------------ Load Tasks ------------------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# ------------------ Save Tasks ------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ------------------ View Tasks ------------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\n------ YOUR TASKS ------")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "❌ Pending"
        print(f"{i}. {task['title']}  --> {status}")
    print()

# ------------------ Add Task ------------------
def add_task(tasks):
    title = input("Enter task name: ")
    tasks.append({"title": title.strip(), "completed": False})
    print("Task added successfully!")

# ------------------ Update Task ------------------
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to update: "))
        tasks[task_no - 1]["title"] = input("Enter new task name: ")
        print("Task updated successfully!")
    except:
        print("Invalid task number!")

# ------------------ Mark Complete ------------------
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark completed: "))
        tasks[task_no - 1]["completed"] = True
        print("Task marked as completed!")
    except:
        print("Invalid task number!")

# ------------------ Delete Task ------------------
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        print("Task deleted successfully!")
    except:
        print("Invalid task number!")

# ------------------ Main Program ------------------
def main():
    tasks = load_tasks()

    while True:
        print("""
====== TO-DO LIST MENU ======
1. View Tasks
2. Add Task
3. Update Task
4. Mark Task Completed
5. Delete Task
6. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved! Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

        save_tasks(tasks)

if __name__ == "__main__":
    main()

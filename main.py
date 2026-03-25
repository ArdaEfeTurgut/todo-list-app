tasks = []


# Load tasks from file when program starts
def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []


# Save tasks to file after every change
def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


# Shows the menu options
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


# Adds a new task to the list
def add_task():
    task = input("Enter a new task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append("[ ] " + task)
        save_tasks()
        print("Task added successfully.")


# Displays all tasks in the list
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Marks a task as completed
def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        else:
            if tasks[task_number - 1].startswith("[✓] "):
                print("This task is already completed.")
            else:
                if tasks[task_number - 1].startswith("[ ] "):
                    tasks[task_number - 1] = tasks[task_number - 1].replace("[ ] ", "[✓] ", 1)
                else:
                    tasks[task_number - 1] = "[✓] " + tasks[task_number - 1]

                save_tasks()
                print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")


# Deletes a task from the list
def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        else:
            tasks.pop(task_number - 1)
            save_tasks()
            print("Task deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
tasks = []


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
    # Ask the user to enter a task
    task = input("Enter a new task: ")

    # Check if the task is empty
    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        # Add the task to the tasks list
        tasks.append(task)

        # Show a success message
        print("Task added successfully.")


# Displays all tasks in the list
def view_tasks():
    # Check if the list is empty
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        # Print all tasks with numbers
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Marks a task as completed
def complete_task():
    # Show current tasks first
    view_tasks()

    # If there are no tasks, stop the function
    if len(tasks) == 0:
        return

    # Ask the user which task is completed
    task_number = int(input("Enter task number to mark as completed: "))

    # Check if the task number is valid
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
    else:
        # Check if the task is already completed
        if tasks[task_number - 1].startswith("[✓] "):
            print("This task is already completed.")
        else:
            # Mark the selected task as completed
            tasks[task_number - 1] = "[✓] " + tasks[task_number - 1]

            # Show a success message
            print("Task marked as completed.")


# Deletes a task from the list
def delete_task():
    # Show current tasks first
    view_tasks()

    # If there are no tasks, stop the function
    if len(tasks) == 0:
        return

    # Ask the user which task should be deleted
    task_number = int(input("Enter task number to delete: "))

    # Check if the task number is valid
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
    else:
        # Remove the selected task from the list
        tasks.pop(task_number - 1)

        # Show a success message
        print("Task deleted successfully.")


def main():
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
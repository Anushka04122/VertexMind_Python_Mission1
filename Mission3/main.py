from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# List to store tasks
tasks = []


def add_task():
    """
    Adds a new task to the task list.
    """

    task_name = input(Fore.YELLOW + "\nEnter task name: ")

    task = {
        "task": task_name,
        "status": "Pending"
    }

    tasks.append(task)

    print(Fore.GREEN + "Task added successfully!")


def view_tasks():
    """
    Displays all tasks.
    """

    if len(tasks) == 0:

        print(Fore.RED + "\nNo tasks available.")

    else:

        print(Fore.CYAN + "\n========== TASK LIST ==========")

        for index, task in enumerate(tasks, start=1):

            print(
                Fore.WHITE +
                f"{index}. {task['task']} - {task['status']}"
            )


def complete_task():
    """
    Marks a task as completed.
    """

    view_tasks()

    try:

        task_number = int(
            input(Fore.YELLOW + "\nEnter task number to mark as completed: ")
        )

        tasks[task_number - 1]["status"] = "Completed"

        print(Fore.GREEN + "Task marked as completed!")

    except ValueError:

        print(Fore.RED + "Please enter a valid number.")

    except IndexError:

        print(Fore.RED + "Task number does not exist.")


def remove_task():
    """
    Removes a task from the list.
    """

    view_tasks()

    try:

        task_number = int(
            input(Fore.YELLOW + "\nEnter task number to remove: ")
        )

        removed_task = tasks.pop(task_number - 1)

        print(
            Fore.GREEN +
            f"Removed task: {removed_task['task']}"
        )

    except ValueError:

        print(Fore.RED + "Please enter a valid number.")

    except IndexError:

        print(Fore.RED + "Task number does not exist.")


# Main Program Loop
while True:

    print(Fore.CYAN + "\n========== STUDENT TASK MANAGER ==========")

    print(Fore.WHITE + "1. Add Task")
    print(Fore.WHITE + "2. View Tasks")
    print(Fore.WHITE + "3. Complete Task")
    print(Fore.WHITE + "4. Remove Task")
    print(Fore.WHITE + "5. Exit")

    choice = input(Fore.YELLOW + "\nEnter your choice: ")


    if choice == "1":

        add_task()


    elif choice == "2":

        view_tasks()


    elif choice == "3":

        complete_task()


    elif choice == "4":

        remove_task()


    elif choice == "5":

        print(Fore.GREEN + "\nExiting application...")

        break


    else:

        print(Fore.RED + "\nInvalid choice. Please try again.")
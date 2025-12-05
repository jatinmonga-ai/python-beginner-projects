tasks = []

while True:
    print(" TO-DO LIST : ")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add a task
    if choice == "1":
        task = input("Type your task: ")
        tasks.append(task)
        print("Task added!")

    # View all tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    # Delete a task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            delete_number = input("Enter task number to delete: ")

            if delete_number.isdigit():  # checks if input is a number
                delete_number = int(delete_number)
                if 1 <= delete_number <= len(tasks):
                    deleted = tasks.pop(delete_number - 1)
                    print(f"Deleted: {deleted}")
                else:
                    print("Invalid task number!")
            else:
                print("Please enter a valid number!")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again!")

print("Press Enter to exit")        








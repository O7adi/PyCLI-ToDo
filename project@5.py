# this is my 5 project

tasks = []

while True:
    print("\nTO DO LIST")
    print("1. ADD TASK")
    print("2. VIEW TASKS")
    print("3. REMOVE TASK")
    print("4. EXIT")

    choice = input("CHOOSE NO: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("TASK ADDED !!!")
    elif choice == "2":
        print("YOUR TASKS:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("NO TASKS FOUND !!!")
    elif choice == "3":
        task = input("Enter Task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("TASK REMOVED !!!")
        else:
            print("TASK NOT FOUND !!!")
    elif choice == "4":
        print("BYE !!!")
        break
    else:
        print("INVALID NO !!!")
        
import threading

tasks = []
lock = threading.Lock()

def add_task(task):
    with lock:
        tasks.append(task)
        print(f"Task added: {task}")

def delete_task(index):
    with lock:
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task removed: {removed}")
        else:
            print("Invalid index.")

def list_tasks():
    with lock:
        if tasks:
            print("Task List:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        else:
            print("No tasks available.")

def main():
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. List Tasks\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            task = input("Enter task: ")
            threading.Thread(target=add_task, args=(task,)).start()
        elif choice == '2':
            index = int(input("Enter task index to delete: ")) - 1
            threading.Thread(target=delete_task, args=(index,)).start()
        elif choice == '3':
            threading.Thread(target=list_tasks).start()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main()

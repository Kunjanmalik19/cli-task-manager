import json
import os
from task import Task

DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return[]
    with open(DATA_FILE,'r') as file:
        try:
            data_list = json.load(file)
            return[Task.from_dict(task) for task in data_list]
        except json.JSONDecodeError:
            return[]
        
def save_tasks(tasks):
    with open(DATA_FILE,"w") as file:
        json.dump([task.to_dict() for task in tasks],file, indent=4)

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            if not tasks:
                print("\nNo tasks found!")
            else:
                for index,task in enumerate(tasks,start=1):
                    print(f"{index}.[{task.status}] {task.title} - {task.description}")

        elif choice == '2':
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            new_task=Task(title,description,"Pending")
            tasks.append(new_task)
            save_tasks(tasks)
            print("\nTask added successfully!") 

        elif choice == '3':
            if not tasks:
                print("\nNo tasks found!")
                continue
            for index,task in enumerate(tasks,start=1):
                print(f"{index}.[{task.status}] {task.title} - {task.description}")
            try:
                task_index = int(input("Enter task number to mark as completed: ").strip()) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index].status = "Completed"
                    save_tasks(tasks)
                    print("\nTask marked as completed!")
                else:
                    print("\nInvalid task number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        elif choice == '4':
            if not tasks:
                print("\nNo tasks found!")
                continue
            for index,task in enumerate(tasks,start=1):
                print(f"{index}.[{task.status}] {task.title} - {task.description}")
            try:
                task_index = int(input("Enter task number to delete: ").strip()) - 1
                if 0 <= task_index < len(tasks):
                    del tasks[task_index]
                    save_tasks(tasks)
                    print("\nTask deleted successfully!")
                else:
                    print("\nInvalid task number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        elif choice == '5':
            print("\nExiting Task Manager. Goodbye!")
            break

if __name__=="__main__":
    main()

    
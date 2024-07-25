import json
import os

FILE_NAME = 'tasks.json'


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)


def view_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Pending"
        print(f"{i + 1}. {task['task']} - {status}")


def mark_task_completed(tasks):
    task_id = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)


def delete_task(tasks):
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)


def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()


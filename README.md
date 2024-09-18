# Task Management System

This is a simple Python-based task management system that allows you to create, modify, delete, and track tasks. Each task has a name and a completion status (done or not done), and the tasks are stored in a JSON file to persist data.

## Features

- **Create Tasks**: Add new tasks with a unique ID and a status.
- **Modify Tasks**: Update the task name and automatically reflect changes in the JSON file.
- **Mark Tasks as Done**: Toggle the completion status of a task and update the JSON file.
- **Delete Tasks**: Remove a task from the list and the JSON file.
- **List Tasks**: List all tasks, done tasks, and tasks that are still in progress.
- **Persistent Storage**: Tasks are saved in a JSON file, making them persistent between program executions.

## JSON Structure

The tasks are stored in a `json/task.json` file in the following format:

```json
{
    "task1": {
        "task": "Fight",
        "done": false
    },
    "task2": {
        "task": "Swim",
        "done": true
    }
}
```

Each task is represented as a dictionary entry with a key like `task1`, `task2`, etc. The value is another dictionary containing the task name and the status (`done`).

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed on your machine.
3. No external dependencies are required.

## Usage

### 1. Running the Program

You can run the main program that demonstrates the task management functionality. The `main()` function will create tasks, modify them, and delete them to show how the system works:

```bash
python your_script.py
```
### 2. How to Add Tasks

Tasks are added by creating instances of the `Task` class. Each task must have a unique name. For example:

```python
task1 = Task('Run')
```
### 3. Modifying Tasks

You can modify the name of a task using the `task_name` property. For example:

```python
task1.task_name = 'Jog'
```
### 4. Deleting Tasks

To delete a task, use the `del` keyword to remove the task's name. For example:

```python
del task1.task_name
```
### 5. Marking a Task as Done

To toggle the completion status of a task, use the `change_mark_task` method:

```python
task1.change_mark_task()
```
### 6. Listing Tasks

You can list all tasks, done tasks, or tasks that are in progress using the following methods:

- **List all tasks:**

  ```python
  Task.lists_all_tasks()
  ```
- **List completed tasks:**

```python
Task.lists_all_done_tasks()
```
- **List tasks still in progress:**

```python
Task.lists_all_not_done_tasks()
```
### 7. File Structure

- `your_script.py`: Main Python file containing the `Task` class and task management logic.
- `json/task.json`: JSON file where tasks are stored persistently.

### 8. Example

Here is an example of using the system:

```python
def main():
    # Creating tasks
    task1 = Task('Run')
    task2 = Task('Jump')
    task3 = Task('Swim')

    # Modifying tasks
    task1.task_name = 'Fight'
    
    # Deleting a task
    del task2.task_name
    
    # Marking task3 as done
    task3.change_mark_task()

    # Listing all tasks
    Task.lists_all_tasks()

if __name__ == "__main__":
    main()
```
This will:

- Create three tasks (`Run`, `Jump`, `Swim`).
- Modify the name of the first task to `Fight`.
- Delete the second task.
- Mark the third task (`Swim`) as done.
- Finally, list all tasks.



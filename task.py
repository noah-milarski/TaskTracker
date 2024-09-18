import json
import os

class Task:
    """
    Represents a task with a name and a completion status.
    """

    task_counter = 0
    list_of_all_tasks = []
    file_path = 'json/task.json'

    def __init__(self, name):
        """
        Initializes a new Task instance.

        :param name: The name of the task.
        :type name: str
        """
        if not name:
            raise ValueError("Task name cannot be empty.")

        self.name = name
        self.is_done = False
        self.id = Task.task_counter + 1
        Task.task_counter += 1
        Task.list_of_all_tasks.append(self)

        self._write_task_to_json()

    def _write_task_to_json(self):
        """
        Helper method to write all tasks to the JSON file.
        Saves tasks in the format of a dictionary where the keys are task IDs.
        """
        tasks = {f"task{task.id}": {"task": task.name, "done": task.is_done} for task in Task.list_of_all_tasks if task.name is not None}

        with open(Task.file_path, "w") as json_file:
            json.dump(tasks, json_file, indent=4)

    def __str__(self):
        """
        Returns a string representation of the Task instance.

        :return: A string representing the task.
        :rtype: str
        """
        status = '☑ (Done)' if self.is_done else '☐ (In Progress)'
        return f'{self.id} - {self.name} - {status}' if self.name is not None else 'Task was deleted'

    @property
    def task_name(self):
        """
        Gets the name of the task.

        :return: The name of the task.
        :rtype: str
        """
        return self.name

    @task_name.setter
    def task_name(self, name):
        """
        Sets the name of the task if the new name is different from the current one and is not empty.

        :param name: The new name for the task.
        :type name: str
        """
        if not name:
            raise ValueError("The task name cannot be an empty string.")
        if self.name == name:
            print('You typed the same task.')
        else:
            self.name = name
            self._write_task_to_json()  # Update JSON after changing task name

    @task_name.deleter
    def task_name(self):
        """
        Marks the task as deleted by setting the name to None, removing it from the list of all tasks, and reassigning IDs.
        """
        self.name = None
        if self in Task.list_of_all_tasks:
            Task.list_of_all_tasks.remove(self)
            Task.reassign_ids()
            self._write_task_to_json()  # Update JSON after deleting a task

    @classmethod
    def reassign_ids(cls):
        """
        Reassigns IDs to tasks to maintain a continuous sequence.
        """
        for index, task in enumerate(cls.list_of_all_tasks):
            task.id = index + 1

    @classmethod
    def lists_all_tasks(cls):
        """
        Prints all created tasks.
        """
        for task in cls.list_of_all_tasks:
            print(task)

    @classmethod
    def lists_all_done_tasks(cls):
        """
        Prints all done tasks.
        """
        for task in cls.list_of_all_tasks:
            if task.is_done:
                print(task)

    @classmethod
    def lists_all_not_done_tasks(cls):
        """
        Prints all not done tasks.
        """
        for task in cls.list_of_all_tasks:
            if not task.is_done:
                print(task)

    def change_mark_task(self):
        """
        Toggles the completion status of the task.
        """
        self.is_done = not self.is_done if self.name is not None else print("This task was deleted.")
        self._write_task_to_json()
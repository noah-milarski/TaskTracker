class Task:
    """
    Represents a task with a name and a completion status.

    Attributes:
        task_counter (int): A class-level counter for generating unique task IDs.
        list_of_all_tasks (list): A class-level list that stores all created tasks.
        name (str): The name of the task.
        is_done (bool): The completion status of the task.
        id (int): A unique identifier for the task.

    Methods:
        __init__(name):
            Initializes a new task with a given name, sets the completion status to False, and assigns a unique ID.

        __str__():
            Returns a string representation of the task including its ID, name, and status (Done or In Progress).

        task_name:
            Property to get and set the task's name. Includes validation to ensure the name is not empty.

        delete_task():
            Marks the task as deleted by setting its name to None, removing it from the class-level list, and reassigning IDs.

        reassign_ids():
            Reassigns IDs to tasks to maintain a continuous sequence.

        lists_all_tasks():
            Prints all created tasks.

        lists_all_done_tasks():
            Prints all done tasks.

        lists_all_not_done_tasks():
            Prints all not done tasks.

        change_mark_task():
            Toggles the completion status of the task.
    """

    task_counter = 0
    list_of_all_tasks = []

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

    @task_name.deleter
    def task_name(self):
        """
        Marks the task as deleted by setting the name to None, removing it from the list of all tasks, and reassigning IDs.
        """
        self.name = None
        if self in Task.list_of_all_tasks:
            Task.list_of_all_tasks.remove(self)
            Task.reassign_ids()

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

from uaclient.api.u.pro.packages.updates.v1 import updates


class Task:
    count = 0

    def __init__(self, name):
        self.name = name
        self.is_done = False
        self.id = Task.count + 1
        Task.count += 1

    def __str__(self):
        if self.is_done == False:
            msg = 'Not Done'
        else:
            msg = 'Done'
        if self.name is not None:
            return f'{self.id} - {self.name} - {msg}'
        else:
            return f'Task was deleted'

    def update_task_name(self, name):
        if self.name == name:
            print('You typed the same task')
        else:
            self.name = name

    def delete_task(self):
        self.name = None

    def list_all_tasks(self):
        pass



task1 = Task('Run')
task2 = Task('Jump')
task3 = Task('Swim')

print(task1)
print(task2)
print(task3)
print()

task1.update_task_name('Fight')

task1.delete_task()

task2.update_task_name('Fight')

print(task1)
print(task2)
print(task3)


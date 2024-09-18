from task import Task

def main():
    task1 = Task('Run')
    task2 = Task('Jump')
    task3 = Task('Swim')

    # Task.lists_all_tasks()
    # print()
    #
    task1.task_name = 'Fight'
    del task2.task_name
    task3.change_mark_task()
    #
    # Task.lists_all_done_tasks()
    # print()
    # Task.lists_all_not_done_tasks()




if __name__ == '__main__':
    main()


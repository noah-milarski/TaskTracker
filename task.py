class Task:
    def __init__(self, name):
        self.name = name
        self.is_done = False

    def __str__(self):
        if self.is_done == False:
            msg = 'Not Done'
        else:
            msg = 'Done'
        return f'{self.name} {msg}'
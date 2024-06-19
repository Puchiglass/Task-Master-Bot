import random


class TaskManager:
    def __init__(self):
        self.tasks = ['Go kiss your honey', 'Go dish wash']

    def get_task(self) -> str:
        i = random.randint(0, len(self.tasks) - 1)
        return self.tasks[i]

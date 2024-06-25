import csv
import random


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def get_task(self) -> str:
        i = random.randint(0, len(self.tasks) - 1)
        return self.tasks[str(i)]

    def load_tasks(self):
        activities = {}
        with open('tasks.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                id, activity = row
                activities[id] = activity
        return activities
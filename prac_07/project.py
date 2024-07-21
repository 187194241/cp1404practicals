from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, new_completion_percentage=None, new_priority=None):
        if new_completion_percentage is not None:
            self.completion_percentage = new_completion_percentage
        if new_priority is not None:
            self.priority = new_priority

    def from_string(string):
        parts = string.strip().split('\t')
        return Project(*parts)

    def to_string(self):
        return f"{self.name}\t{self.start_date.strftime("%d/%m/%Y")}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

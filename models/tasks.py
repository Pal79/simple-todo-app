from datetime import datetime

class Tasks:
    def __init__(self, id, task_name, description, deadline, status):
        self.id = id
        self.task_name = task_name
        self.description = description
        self.deadline = deadline
        self.status = status
    
    @property
    def deadline_date(self):
        return datetime.strptime(self.deadline, '%Y-%m-%d')
    
    @property
    def dom(self):
        return self.deadline_date.day
    
    @property
    def year(self):
        return self.deadline_date.year
    
    @property
    def month(self):
        return self.deadline_date.month

    def __repr__(self):
        return f'<Task {self.id}: {self.task_name} ({self.deadline})'

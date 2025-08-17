class Task:
    def __init__(self, id, description, completed):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True
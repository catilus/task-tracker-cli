from task import Task

class Task_manager:
    tasks = []
    
    @classmethod # if method works only on the class itself
    def add_task(cls, description):
        task_id = len(cls.tasks) + 1
        task = Task(task_id, description, False)
        cls.tasks.append(task)
    
    @classmethod
    def list_tasks(cls):
        for task in cls.tasks:
            print(task.id)
            print(task.description)
            print(task.completed)
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
        print('List of tasks: ')
        for task in cls.tasks:
            if task.completed == True:
                print(str(task.id) + ' - ' + task.description + '. Completed: Yes')
            else:
                print(str(task.id) + ' - ' + task.description + '. Completed: No')
import sys
from task_manager import Task_manager
from task import Task
# Main program

# Display menu until user chooses or exits program
while True:
    print('1. Add task')
    print('2. List tasks')
    print('3. Quit')

    menu_choice = input('Enter 1, 2, 3 > ')

    if menu_choice == '1':
        print("Enter a description for your task:")
        description = input('> ')
        Task_manager.add_task(description)
    elif menu_choice == '2':
        Task_manager.list_tasks()
    elif menu_choice == '3':
        sys.exit()
    else:
        continue
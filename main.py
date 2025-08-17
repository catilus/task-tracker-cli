import sys
# Main program

# Display menu until user chooses or exits program
while True:
    print('1. Add task')
    print('2. List tasks')
    print('3. Quit')

    menu_choice = input('Enter 1, 2, 3 > ')

    if menu_choice == '1':
        break
    elif menu_choice == '2':
        break
    elif menu_choice == '3':
        sys.exit()
    else:
        continue
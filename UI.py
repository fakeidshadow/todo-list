from User import User

PROJECT_IDX = -1

def print_main_menu():
    print('- '*10)
    print('1  -> add project')
    print('2  -> edit project tasks')
    print('3  -> edit project name')
    print('4  -> edit project description')
    print('5  -> delete project')
    print('6  -> show projects')
    print('-1 -> exit')

def start():
    user = User()
    command = ''
    while command != '-1':
        print_main_menu()
        command = input()
        if command == '1':
            name = input('Enter your project name')
            description = input('Enter your project description')
            user.add_project(name, description)
        elif command == '2':
            edit_project_tasks(user)
        elif command == '3':
            name = input('Enter your project name')
            new_name = input('Enter your project new name')
            user.edit_project_name(name, new_name)
        elif command == '4':
            name = input('Enter your project name')
            new_description = input('Enter your project new description')
            user.edit_project_description(name, new_description)
        elif command == '5':
            name = input('Enter your project name')
            user.del_project(name)
        elif command == '6':
            user.show_projects()
        elif command != '-1':
            print('choose between options')

def print_edit_tasks_menu():
    print('- '*10)
    print('1  -> add task')
    print('2  -> edit task name')
    print('3  -> edit task description')
    print('4  -> edit task status')
    print('5  -> edit task deadline')
    print('6  -> delete task')
    print('7  -> show tasks')
    print('-1 -> exit')

def edit_project_tasks(user:User):
    global PROJECT_IDX
    name = input('Enter your project name')
    PROJECT_IDX = user.index(name)
    if PROJECT_IDX == -1:
        print('project doesnt exist')
    else:
         command = ''
    while command != '-1':
        print_edit_tasks_menu()
        command = input()
        if command == '1':
            name = input('Enter your task neme')
            description = input('Enter your task description')
            status = input('Enter your task status')
            deadline = input('Enter your task deadline')
            user._projects[PROJECT_IDX].add_task(name, description, status, deadline)
        elif command == '2':
            name = input('Enter your task name')
            new_name = input('Enter your task new name')
            user._projects[PROJECT_IDX].edit_task_name(name, new_name)
        elif command == '3':
            name = input('Enter your task name')
            new_description = input('Enter your task new description')
            user._projects[PROJECT_IDX].edit_rask_description(name, new_description)
        elif command == '4':
            name = input('Enter your task name')
            new_status = input('Enter your task new status')
            user._projects[PROJECT_IDX].edit_rask_status(name, new_status)
        elif command == '5':
            name = input('Enter your task name')
            new_deadline = input('Enter your task new deadline')
            user._projects[PROJECT_IDX].edit_rask_deadline(name, new_deadline)
        elif command == '6':
            name = input('Enter your task name')
            user._projects[PROJECT_IDX].del_task(name)
        elif command == '7':
            user._projects[PROJECT_IDX].show_tasks()
        elif command != '-1':
            print('choose between options')
            


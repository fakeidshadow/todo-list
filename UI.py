from custum_exception import CustomError
import models
from datetime import datetime
import pytz
import schedule
import scheduler

schedule.every().day.at("00:00", "Asia/Tehran").do(scheduler.end_tasks())

tz = pytz.timezone('Asia/Tehran')

PROJECT_IDX = -1

def print_main_menu():
    print('- '*20)
    print('1  -> add project')
    print('2  -> edit project tasks')
    print('3  -> edit project name')
    print('4  -> edit project description')
    print('5  -> delete project')
    print('6  -> show projects')
    print('-1 -> exit')

def start():
    command = ''
    while command != '-1':
        schedule.run_pending()
        print_main_menu()
        command = input()
        try:
            if command == '1':
                name = input('Enter your project name: ')
                description = input('Enter your project description: ')
                models.add_project(name, description)
            elif command == '2':
                edit_project_tasks()
            elif command == '3':
                name = input('Enter your project name: ')
                new_name = input('Enter your project new name: ')
                models.edit_project(name, name=new_name)
            elif command == '4':
                name = input('Enter your project name: ')
                new_description = input('Enter your project new description: ')
                models.edit_project(name, description=new_description)
            elif command == '5':
                name = input('Enter your project name: ')
                models.del_project(name)
            elif command == '6':
                for project in models.get_all_projects():
                    print(f'name: {project.name}\ndescription: {project.description}\nnumber of tasks: {len(models.get_all_tasks(project.name))}')
            elif command != '-1':
                print('choose between options')
        except CustomError as e:
            print(e)

def print_edit_tasks_menu():
    print('- '*20)
    print('1  -> add task')
    print('2  -> edit task name')
    print('3  -> edit task description')
    print('4  -> edit task status')
    print('5  -> edit task deadline')
    print('6  -> delete task')
    print('7  -> show tasks')
    print('-1 -> exit')

def edit_project_tasks():
    project_name = input('Enter project_name: ')
    if not models.get_project(project_name):
        print('Project doesnt exists')
        return
    command = ''
    while command != '-1':
        print_edit_tasks_menu()
        command = input()
        try:
            if command == '1':
                name = input('Enter your task name: ')
                description = input('Enter your task description: ')
                status = input('Enter your task status(0:todo, 1:doing, 2:done): ')
                if status == '':
                    status = '0'
                if not status in ['0', '1', '2']:
                    raise CustomError('Enter valid status')
                deadline = input('Enter your task deadline: ')
                models.add_task(project_name=project_name, name=name, description=description, status=int(status), deadline=deadline, closed_at='')
            elif command == '2':
                name = input('Enter your task name: ')
                new_name = input('Enter your task new name: ')
                models.edit_task(name, name=new_name)
            elif command == '3':
                name = input('Enter your task name: ')
                new_description = input('Enter your task new description: ')
                models.edit_task(name, name=new_description)
            elif command == '4':
                name = input('Enter your task name: ')
                new_status = input('Enter your task new status: ')
                if not new_status in ['0', '1', '2']:
                    raise CustomError('Enter valid status')
                models.edit_task(name, status=new_status)
                if new_status == '2':
                    ct = datetime.now(tz)
                    models.edit_task(name, closed_at=str(ct))
            elif command == '5':
                name = input('Enter your task name: ')
                new_deadline = input('Enter your task new deadline: ')
                models.edit_task(name, status=new_deadline)
            elif command == '6':
                name = input('Enter your task name: ')
                models.del_task(name)
            elif command == '7':
                for task in models.get_all_tasks(project_name):
                    print(f'name: {task.name}\ndescription: {task.description}\nstatus: {task.status}\ndeadline: {task.deadline}, closed at: {task.closed_at}')

            elif command != '-1':
                print('choose between options')
        except CustomError as e:
            print(e)



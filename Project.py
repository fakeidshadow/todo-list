from Task import Task
from custum_exception import CustomError
from dotenv import load_dotenv
import os

load_dotenv()

MAX_NUMBER_OF_TASK = int(os.getenv('MAX_NUMBER_OF_TASK'))

class Project:
    def __init__(self, name:str, description:str):
        self.name = name
        self.description= description
        self._tasks = []
    
    @property
    def name(self)->str:
        return self._name
    
    @property
    def description(self)->str:
        return self._description
    

    @name.setter
    def name(self, name:str)->None:
        if len(name.split()) > 30:
            raise CustomError('len name must be le 30 words')
        if not name:
            raise CustomError('name cant be empty')
        self._name = name

    @description.setter
    def description(self, description:str)->None:
        if len(description.split()) > 150:
            raise CustomError('len name must be le 30 words')
        self._description=description

    def index(self, name:str):
        for i in range(len(self._tasks)):
            if self._tasks[i] == name:
                return i
        return -1

    def add_task(self, name:str, description:str, status:int=0, deadline:str=''):
        t = Task(name, description, status, deadline)
        if self.index(name) != -1:
            print(self.index(name))
            raise CustomError('its already exists')
        elif len(self._tasks) >= MAX_NUMBER_OF_TASK:
            raise CustomError('MAX number of tasks')
        else:
            self._tasks.append(t)
            print('task added successfuly')

    
    def del_task(self, name:str):
        idx = self.index(name)
        if idx == -1:
            raise CustomError('task doesnt exist')
        else:
            self._tasks.pop(idx)
            print('task deleted successfuly')
    
    def edit_task_name(self, name:str, new_name:str):
        idx = self.index(name)
        idx_new = self.index(new_name)
        if idx == -1:
            raise CustomError('task doesnt exist')
        elif idx_new != -1 and idx_new != idx:
            raise CustomError('task exist with this name')
        else:
            self._tasks[idx].name = new_name
            print('task name edited successfuly')


    def edit_task_status(self, name:str, new_status:int):
        idx = self.index(name)
        self._tasks[idx].status = new_status
        print('task status edited successfuly')


    
    def edit_task_description(self, name:str, new_description:str):
        idx = self.index(name)
        self._tasks[idx].descriptin = new_description
        print('task description edited successfuly')


    def edit_task_deadline(self, name:str, new_deadline:str):
        idx = self.index(name)
        self._tasks[idx].deadline = new_deadline
        print('task deadline edited successfuly')



    def show_tasks(self):
        if not self._tasks:
            print('There is no task')
        else:
            for t in self._tasks:
                status = 'todo'
                if t.status == 1:
                    status = 'doing'
                if t.status == 2:
                    status = 'done'
                print(f'name: {t.name}')    
                print(f'description: {t.description}')    
                print(f'status: {status}')  
                if t.deadline != '':  
                    print(f'deadline: {t.deadline}')    
        
    def __eq__(self, name:str):
        if self.name == name:
            return True
        else:
            return False
        
        

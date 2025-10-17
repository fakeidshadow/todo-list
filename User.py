from Project import Project
from custum_exception import CustomError
from dotenv import load_dotenv
import os

load_dotenv()

MAX_NUMBER_OF_PROJECT = int(os.getenv('MAX_NUMBER_OF_PROJECT'))

class User:
    def __init__(self):
        self._projects = []

    def index(self, name:str):
        for i in range(len(self._projects)):
            if self._projects[i] == name:
                return i
        return -1
    
    def add_project(self, name:str, description:str):
        p = Project(name, description)        
        if self.index(name) != -1:
            print(self.index(name))
            raise CustomError('its already exists')
        elif len(self._projects) >= MAX_NUMBER_OF_PROJECT:
            raise CustomError('MAX number of projects')
        else:
            self._projects.append(p)
            print('task added successfuly')
    
    def del_project(self, name:str):
        idx = self.index(name)
        if idx == -1:
            raise CustomError('task doesnt exist')
        else:
            self._projects.pop(idx)
            print('task deleted successfuly')
    
    def edit_project_name(self, name:str, new_name:str):
        idx = self.index(name)
        idx_new = self.index(new_name)
        if idx == -1:
            raise CustomError('task doesnt exist')
        elif idx_new != -1 and idx_new != idx:
            raise CustomError('task exist with this name')
        else:
            self._projects[idx].name = new_name
            print('project name edited successfuly')


    def edit_project_description(self, name:str, new_description:str):
        idx = self.index(name)
        self._projects[idx].description = new_description
        print('project description edited successfuly')


    def show_projects(self):
        if not self._projects:
            print('There is no project')
        else:
            for p in self._projects:
                print(f'name: {p.name}')    
                print(f'description: {p.description}')    
                print(f'NO. tasks: {len(p._tasks)}')


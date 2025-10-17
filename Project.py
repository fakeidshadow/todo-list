from Task import Task

class Project:
    def __init__(self, name:str, description:str):
        self.name(name)
        self.description(description)
        self._tasks = []
    
    @property
    def name(self)->str:
        return self._name
    
    @property
    def description(self)->str:
        return self._deadline
    

    @name.setter
    def name(self, name:str)->None:
        if len(name.split()) > 30:
            print('len name must be le 30 words')
        self._name = name

    @description.setter
    def status(self, description:str)->None:
        if len(description.split()) > 150:
            print('len name must be le 30 words')
        self._description=description


    def index(self, name:str):
        for i in range(len(self._tasks)):
            if self._tasks[i] == name:
                return i
            return -1

    def add_task(self, name:str, description:str, status:int=0, deadline:str=''):
        t = Task(name, description, status, deadline)
        if self.index(name) != -1:
            print('its already exists')
        else:
            self._tasks.append(t)
            print('task added successfuly')

    
    def del_task(self, name:str):
        idx = self.index(name)
        if idx == -1:
            print('task doesnt exist')
        else:
            self._tasks.pop(idx)
            print('task deleted successfuly')
    
    def edit_task_name(self, name:str, new_name:str):
        idx = self.index(name)
        idx_new = self.index(new_name)
        if idx == -1:
            print('task doesnt exist')
        elif idx_new != -1 and idx_new != idx:
            print('task exist with this name')
        else:
            self._tasks[idx].name = new_name

    def edit_rask_status(self, name:str, new_status:int):
        idx = self.index(name)
        self._tasks[idx].status = new_status

    
    def edit_rask_description(self, name:str, new_description:str):
        idx = self.index(name)
        self._tasks[idx].descriptin = new_description

    def edit_rask_deadline(self, name:str, new_deadline:str):
        idx = self.index(name)
        self._tasks[idx].status = new_deadline


    def show_tasks(self):
        for t in self._tasks:
            status = 'todo'
            if t.status == 1:
                status = 'doing'
            if t.status == 2:
                t.status = 'done'
            print(f'name: {t.name}')    
            print(f'description: {t.description}')    
            print(f'status: {status}')  
            if t.deadline != '':  
                print(f'deadline: {t.deadline}')    
        

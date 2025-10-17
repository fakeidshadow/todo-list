from Project import Project

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
            print('its already exists')
        else:
            self._projects.append(p)
            print('task added successfuly')
    
    def del_project(self, name:str):
        idx = self.index(name)
        if idx == -1:
            print('task doesnt exist')
        else:
            self._projects.pop(idx)
            print('task deleted successfuly')
    
    def edit_project_name(self, name:str, new_name:str):
        idx = self.index(name)
        idx_new = self.index(new_name)
        if idx == -1:
            print('task doesnt exist')
        elif idx_new != -1 and idx_new != idx:
            print('task exist with this name')
        else:
            self._projects[idx].name = new_name

    def edit_project_description(self, name:str, new_description:str):
        idx = self.index(name)
        self._projects[idx].descriptin = new_description


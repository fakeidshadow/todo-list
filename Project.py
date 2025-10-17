from Task import Task

class Project:
    def __init__(self, name:str, description:str):
        self.name(name)
        self.description(description)
        list[Task]: self._tasks = []
    
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


    



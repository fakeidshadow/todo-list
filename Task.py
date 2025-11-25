from datetime import datetime

class Task:
    def __init__(self, name:str, description:str, status:int=0, deadline:str=''):
        self.name = name
        self.status = status
        self.deadline = deadline
        self.description = description
        self.closed_at = ""
    
    @property
    def name(self)->str:
        return self._name
    
    @property
    def status(self)->int:
        return self._status
    
    @property
    def deadline(self)->str:
        return self._deadline
    
    @property
    def description(self)->str:
        return self.description

    @property
    def closed_at(self) -> str:
        return self.closed_at

    @name.setter
    def name(self, name:str)->None:
        if len(name.split()) > 30:
            print('len name must be le 30 words')
        self._name = name

    @description.setter
    def description(self, description:str)->None:
        if len(description.split()) > 150:
            print('len name must be le 30 words')
        self._description=description

    
    @status.setter
    def status(self, status:int)->None:
        if status > 2 or status < 0:
            print('status only can be 0,1,2')
        self._status = status

    
    @deadline.setter
    def deadline(self, deadline:str)->None:
        if deadline != '':
            try:
                datetime.strptime(deadline, '%Y-%m-%d')
            except ValueError:
                print('deadline is invalid')
            else:
                self._deadline = deadline
        else:
            self._deadline = deadline

    @closed_at.setter
    def closed_at(self, closed_at: str) -> None:
        if closed_at != '':
            try:
                datetime.strptime(closed_at, '%Y-%m-%d')
            except ValueError:
                print('deadline is invalid')
            else:
                self.closed_at = closed_at
        else:
            self.closed_at = closed_at

    def __eq__(self, name:str):
        if self.name == name:
            return True
        else:
            return False


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    projects = relationship('Project', back_populates='user')

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    description = Column(String(150))

    tasks = relationship("Task", back_populates="project")
    owner = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='projects')

class Task(Base):
    __tablename__ = 'task'


    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    status = Column(Integer, default=0)
    deadline = Column(String(20))
    description = Column(String(150))
    closed_at = Column(String(20), default='')

    owner = Column(Integer, ForeignKey('project.id'))

    project = relationship("Project", back_populates="tasks")



from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:sec123@localhost:5432/todo_db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

def add_user(name:str) -> int:
    user = User(name=name)
    session.add(user)
    session.commit()

def add_project(username:str, name:str, description:str) -> int:
    user = get_user(name)
    project = Project(name=name, description=description, owner=user.id)
    session.add(project)
    session.commit()

def add_task(project_name:str, name:str, status:int, deadline:str, description:str, closed_at:str):
    project = get_project(name=project_name)
    task = Task(name=name, status=status, deadline=deadline, description=description, closed_at=closed_at, owner=project.id)
    session.add(task)
    session.commit()

def get_user(name:str) -> User:
    pass

def get_project(name:str) -> Project:
    pass

def get_task(name:str) -> Task:
    pass
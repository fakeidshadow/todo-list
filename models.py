
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
    return user.id

def add_project(username:str, name:str, description:str) -> int:
    user = get_user(name)
    project = Project(name=name, description=description, owner=user.id)
    session.add(project)
    session.commit()
    return project.id

def add_task(project_name:str, name:str, status:int, deadline:str, description:str, closed_at:str):
    project = get_project(name=project_name)
    task = Task(name=name, status=status, deadline=deadline, description=description, closed_at=closed_at, owner=project.id)
    session.add(task)
    session.commit()
    return task.id

def get_user(name:str) -> User:
    return session.query(User).filter_by(name=name).one_or_none()

def get_project(name:str) -> Project:
    return session.query(Project).filter_by(name=name).one_or_none()

def get_task(name:str) -> Task:
    return session.query(Task).filter_by(name=name).one_or_none()

def gat_all_project(name:str):
    return session.query(Project).filter_by(owner=get_user(name=name).id).all()

def gat_all_tasks(name:str):
    return session.query(Task).filter_by(owner=get_project(name=name).id).all()


def edit_user(name, **kwargs):
    user = get_user(name)
    if 'name' in kwargs:
        user.name = kwargs['name']
    session.commit()


def edit_project(name, **kwargs):
    project = get_project(name)
    if 'name' in kwargs:
        project.name = kwargs['name']
    elif 'description' in kwargs:
        project.description = kwargs['description']
    session.commit()


def edit_task(name, **kwargs):
    task = get_task(name)
    if 'name' in kwargs:
        task.name = kwargs['name']
    elif 'description' in kwargs:
        task.description = kwargs['description']
    elif 'status' in kwargs:
        task.status = kwargs['status']
    elif 'deadline' in kwargs:
        task.deadline = kwargs['deadline']
    elif 'closed_at' in kwargs:
        task.closed_at = kwargs['closed_at']
    session.commit()



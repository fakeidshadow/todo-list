
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
    name = Column(String(30))
    description = Column(String(150))

    tasks = relationship("Task", back_populates="project")
    owner = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='projects')

class Task(Base):
    __tablename__ = 'task'


    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    status = Column(Integer, default=0)
    deadline = Column(String(20))
    description = Column(String(150))
    closed_at = Column(String(20), default='')

    owner = Column(Integer, ForeignKey('project.id'))

    project = relationship("Project", back_populates="tasks")

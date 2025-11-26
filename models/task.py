from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    status = Column(Integer, default=0)
    deadline = Column(String(20))
    description = Column(String(150))
    closed_at = Column(String(20), default='')

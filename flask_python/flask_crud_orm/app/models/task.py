from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from config import *

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state = Column(Boolean)

    def __init__(self, name, state):
        self.name = name
        self.state = state
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, status: {self.state}"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state
        }



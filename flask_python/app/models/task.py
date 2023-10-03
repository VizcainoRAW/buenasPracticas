from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state = Column(Boolean())

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state
        }

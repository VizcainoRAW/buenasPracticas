from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    description = Column(String(256))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

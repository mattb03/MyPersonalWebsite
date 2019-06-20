from sqlalchemy import Column, Integer, String
from database import Base

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(50), unique=False)
    message = Column(String(250), unique=False)

    def __init__(self, name=None, email=None, message=None):
        self.name = name
        self.email = email
        self.message = message

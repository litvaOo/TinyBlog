import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'
    title = Column(
    String(150), nullable=False)
    id = Column(
    Integer, primary_key=True)
    post_text = Column(
    Text, nullable=False)
    likes_number = Column(
    Integer, nullable=False)

    def __init__(self, title, post_text, likes_number = 0):
        self.title = title
        self.post_text = post_text
        self.likes_number = likes_number

class Users(Base):
    __tablename__ = 'users'
    name = Column(
    String(32), nullable=False)
    id = Column(
    Integer, primary_key=True)
    login = Column(
    String(32), nullable=False)
    password = Column(
    String(64), nullable=False)
    isadmin = Column(
    Boolean, nullable=False)

engine = create_engine ("postgresql://postgres:litva@127.0.0.1:5432/postgres")

Base.metadata.create_all(engine)

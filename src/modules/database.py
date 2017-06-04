import sys
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from modules import config
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
    post_date = Column(
    TIMESTAMP, nullable=False)

    def __init__(self, title, post_text, likes_number = 0):
        self.title = title
        self.post_text = post_text
        self.likes_number = likes_number
        self.post_date = datetime.now()

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

class Comments(Base):
    __tablename__ = 'comments'
    id = Column (
    Integer, primary_key=True)
    post_id = Column (
    Integer, nullable=False)
    text = Column (
    Text, nullable=False)
    carma = Column (
    Integer, nullable=False)

    def __init__(self, post_id, text):
        self.post_id = post_id
        self.text = text
        self.carma = 0


engine = create_engine (config.Config.buildConnectionString())

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session_db = DBSession()

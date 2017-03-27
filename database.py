import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
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

engine = create_engine ()

Base.metadata.create_all(engine)

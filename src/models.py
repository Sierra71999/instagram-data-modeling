import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), ForeignKey('user.id'))

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("user.id"))
class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    comment_text = Column(Integer, ForeignKey("user.id"))
    comment_id = Column(Integer, ForeignKey("post.id"))

class Follower(Base):
    __tablename__ ='follower'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    comment_id = Column(Integer, ForeignKey("user.id"))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    media_id = Column(Integer, ForeignKey("post.id"))

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

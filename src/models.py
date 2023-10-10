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
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password =Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey ('user.id'))
    user = relationship(User)

class Characters(Base):
    __tablename__ = 'characters' 
    id = Column (Integer, primary_key=True)
    name= Column (String (50))
    height= Column (Integer)
    mass= Column (Integer)
    birth_year= Column (String(50))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column (Integer, primary_key=True)
    name= Column (String(50))
    diameter= Column (Integer)
    rotation_period= Column (Integer)
    orbital_period= Column (Integer)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column (Integer, primary_key=True)
    name= Column (String(100))
    starship_class= Column (String(100))
    model= Column (String(100))
    length= Column (Integer)

class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user = relationship(User)
    characters = relationship(Characters)
    
class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))    
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    planets = relationship(Planets)

class Favorites_starships(Base):
    __tablename__ = 'favorites_starships'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    starships_id =Column(Integer, ForeignKey('starships.id'))  
    user = relationship(User)
    starships = relationship(Starships)    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
engine = create_engine('sqlite:///workspaces/exercise-starwars-data-modeling-MarthaK')
render_er(Base, 'diagram.png')

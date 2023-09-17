#!/usr/bin/python3
"""contains the class definition of a City"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    cities table class:
        id: primary key
        name: name of the state
        state_id: state id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

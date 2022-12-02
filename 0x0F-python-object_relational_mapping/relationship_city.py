#!/usr/bin/python3
"""City_State Relationship"""
from sqlalchemy.orm import relationship
from model_state import Base, State
from model_city import City

City.state = relationship("State", back_populates="cities")

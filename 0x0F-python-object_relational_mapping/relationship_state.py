#!/usr/bin/python3
"""State_City Relationship"""
from sqlalchemy.orm import relationship
from model_state import Base, State
from model_city import City

State.cities = relationship("City", order_by=City.id, back_populates="state",
                            cascade="all, delete, delete-orphan")

#!/usr/bin/python3
"""City Driver module"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base
from model_city import City
from relationship_state import State
from relationship_city import City


def main():
    """City Driver."""

    DB_USER = argv[1]
    DB_PASS = argv[2]
    DB_NAME = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()


if __name__ == "__main__":
    main()

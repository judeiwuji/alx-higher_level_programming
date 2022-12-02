#!/usr/bin/python3
"""City Driver module"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City


def main():
    """City Driver."""

    DB_USER = argv[1]
    DB_PASS = argv[2]
    DB_NAME = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))
    Session = sessionmaker(bind=engine)
    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for i, city in enumerate(cities):
        print("{}: ({:d}) {}".format(city.state.name, i+1, city.name))


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""City Driver module"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base
from relationship_state import State
from relationship_city import City


def main():
    """City Driver."""

    DB_USER = argv[1]
    DB_PASS = argv[2]
    DB_NAME = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id)

    for city in cities:
        print("{:d}: {} -> {}".format(city.id, city.name, city.state.name))


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""Select state with a given name."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


def main():
    """Select state with a given name."""
    DB_USER = argv[1]
    DB_PASS = argv[2]
    DB_NAME = argv[3]
    SEARCH = argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == SEARCH).first()

    if state is not None:
        print("{:d}".format(state.id))
    else:
        print("Not found")


if __name__ == '__main__':
    main()

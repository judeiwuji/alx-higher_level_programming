#!/usr/bin/python3
"""Select all first states."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


def main():
    """Selects all states."""
    DB_USER = argv[1]
    DB_PASS = argv[2]
    DB_NAME = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))
    Session = sessionmaker()
    session = Session(bind=engine)
    state = session.query(State).first()

    if state is not None:
        print("{:d}: {}".format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == '__main__':
    main()

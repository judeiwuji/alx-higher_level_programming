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

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
    session.commit()


if __name__ == '__main__':
    main()

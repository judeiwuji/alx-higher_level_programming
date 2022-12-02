#!/usr/bin/python3
"""Delete all states that contain letter 'a'."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


def main():
    """Delete all states that contain letter 'a'."""
    DB_USER = argv[1]
    DB_PASS = argv[2]
    DB_NAME = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(DB_PASS, DB_USER, DB_NAME))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.ilike('%%a%%'))\
                    .all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == '__main__':
    main()

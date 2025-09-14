#!/usr/bin/python3
"""
List all State objects that contain the letter 'a' from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing 'a', ordered by id
    states = session.query(State).filter(State.name.like("%a%")).order_by(
        State.id
    ).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> "
              "<password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    # Create engine and session
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)

    # Query cities joined with states
    cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

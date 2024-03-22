#!/usr/bin/python3

"""Script prints the first State object from the
`hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def get_first_state(username: str, password: str, database: str) -> None:
    """Lists the first State object in a database

    Args:
        username (str): username for the connection.
        password (str): password of the user.
        database (str): database to connect to.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        firstState = session.query(State).order_by(State.id).first()

        if firstState:
            print(f"{firstState.id}: {firstState.name}")
        else:
            print("Nothing")


if __name__ == "__main__":
    try:
        get_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <database_name>\n"
        )
        sys.exit(1)

#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, database_name):
    """Changes the name of a State object with id=2 to 'New Mexico'.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database_name (str): The name of the database.
    """

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    try:
        # Retrieve the State object with id=2
        state_to_update = session.query(State).filter_by(id=2).one()

        # Modify its name
        state_to_update.name = "New Mexico"

        # Commit the change to the database
        session.commit()

        print("State name updated successfully!")
    except Exception as e:
        print(f"Error updating state: {e}")
    finally:
        session.close()

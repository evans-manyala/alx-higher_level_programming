from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database_name):
    """Adds the state "Louisiana" to the database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database_name (str): The name of the database.
    """

    # Create the SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
    )

    # Create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Print the new state's ID
    print(f"New state ID: {new_state.id}")

    # Close the session
    session.close()

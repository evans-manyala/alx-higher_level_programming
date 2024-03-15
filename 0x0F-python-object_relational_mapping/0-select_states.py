#!/usr/bin/python3

"""This script lists all states from the database `hbtn_0e_0_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database_name = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        db=database_name,
        port=3306,
    )

    cursor = db.cursor()
    cursor.execute(
        """
        SELECT * FROM states ORDER BY states.id;
        """
    )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

#!/usr/bin/python3

"""Script displays all values in the `states`
table of the database `hbtn_0e_0_usa` where the `name` matches the argument."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database_name, states = sys.argv[1:]

    myDB = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database_name,
        port=3306,
    )

    cursor = myDB.cursor()

    cursor.execute(
        """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY states.id;
        """,
        (states,),
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    myDB.close()
#!/usr/bin/python3

"""Sript displays all values in the `states`
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

    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id;
    """.format(states)

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    myDB.close()

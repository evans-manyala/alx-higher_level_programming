#!/usr/bin/python3

"""Script that lists all cities found in the database `hbtn_0e_4_usa`"""

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
        SELECT cities.name
        FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
        ORDER BY cities.id;
        """,
        (states,),
    )

    results = cursor.fetchall()

    print(", ".join(row[0] for row in results))

    cursor.close()
    myDB.close()

#!/usr/bin/python3

"""Script that lists all cities found in the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database_name = sys.argv[1:]

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
        SELECT cities.id, cities.name, states.name
        FROM cities
            JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
        """
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    myDB.close()

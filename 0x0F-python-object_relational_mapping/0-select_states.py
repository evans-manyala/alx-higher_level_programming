#!/usr/bin/python3
"""This script lists all states from the database `hbtn_0e_0_usa`"""

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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    myDB.close()

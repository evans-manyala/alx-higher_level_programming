#!/usr/bin/python3
"""python script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        db=database_name,
        port=3306
    )
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
states = cursor.fetchall()

for state in states:
    print(state)
cursor.close()
db.close()

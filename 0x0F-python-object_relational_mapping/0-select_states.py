#!/usr/bin/python3

import sys
import MySQLdb


def list_states(username, password, database):
        try:
                db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
                cursor = db.cursor()
        except MySQLdb.Error as e:
                print("Error connecting to MySQL:", e)
                sys.exit(1)
        
        try:
                cursor.execute("SELECT * FROM states ORDER BY id")
                states = cursor.fetchall()
        except MySQLdb.error as e:
                print("Error executing query:", e)
                cursor.close()
                db.close()
                sys.exit(1)
        
        for state in states
                print(state)
        
        cursor.close()
        db.close()

if __name__ == "__main__":
        if len(sys.argv) != 4:
                print("Usage: python list_states.py <username> <password> <database>")
                sys.exit(1)
        
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        
        list_states(username, password, database)

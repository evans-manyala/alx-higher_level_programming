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
                print ("Error executing query:", e)
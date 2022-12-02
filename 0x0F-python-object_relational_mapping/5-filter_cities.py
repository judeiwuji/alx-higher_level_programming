#!/usr/bin/python3
"""Executes a SELECT statement using MySQLdb module."""
import MySQLdb
import sys


def main():
    """Entry point"""
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASSWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    DB_PORT = 3306
    SEARCH = sys.argv[4]

    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD,
                         db=DB_NAME, port=DB_PORT)
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN states ON\
           states.id=cities.state_id WHERE states.name=%s\
           ORDER BY cities.id ASC"
    cur.execute(sql, (SEARCH, ))
    rows = cur.fetchall()

    i = 0
    for row in rows:
        if i != 0:
            print(end=", ")
        for col in row:
            print(col, end="")
        i += 1
    print()


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""Executes a SELECT statement using MySQLdb module.
Selecting only states that start with N
"""
import MySQLdb
import sys


def main():
    """Entry point"""

    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASSWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    SEARCH = sys.argv[4]
    DB_PORT = 3306

    try:
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD,
                             db=DB_NAME, port=DB_PORT)
        cur = db.cursor()
        sql = "SELECT id, name FROM states WHERE name= BINARY '{}' \
            ORDER BY id ASC".format(SEARCH)
        cur.execute(sql)
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
    except Exception:
        pass


if __name__ == '__main__':
    main()

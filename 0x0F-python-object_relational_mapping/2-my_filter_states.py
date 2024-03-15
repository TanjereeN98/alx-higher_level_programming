#!/usr/bin/python3
"""list all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    db_conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                              passwd=args[2], db=args[3])
    cur = db_conn.cursor()
    cur.execute("SELECT * From states where BINARY name = %s", (args[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()

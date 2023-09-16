#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c
                 JOIN states AS s ON s.id = c.state_id
                 ORDER BY c.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

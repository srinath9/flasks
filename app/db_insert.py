import sqlite3 as lite
import MySQLdb as db

conn = db.connect (host = "localhost", user = "root", passwd = "zophop", db="twent")
cursor = conn.cursor()

con = lite.connect("events.sqlite")
cur = con.cursor()
query = "SELECT * FROM events"
cur.execute(query)
rows = cur.fetchall()

for row in rows:
	print row
	if row[5]=="true":
		featured = 1
	else:
		featured = 0
	if row[6]=="true":
		popular = 1
	else:
		popular = 0
	query = "INSERT INTO events VALUES (\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{featured}\',\'{popular}\',\'{5}\')".format(row[0],row[1],row[2],row[3],row[4],row[7],featured=featured,popular=popular)
	cursor.execute(query)

conn.commit()
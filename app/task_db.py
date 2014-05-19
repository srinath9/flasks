import MySQLdb as db
import json
from datetime import datetime

conn = db.connect (host = "localhost", user = "root", passwd = "srinath", db="twent")
cursor = conn.cursor()

def fetch_all_tasks():
	query = "SELECT * FROM events"
	cursor.execute(query)
	rows = cursor.fetchall()
	events = []
	for row in rows:
		data = row
		print row[7]
		data[7] = datetime.strftime(row[7],"YYYY-MM-DD")
		events.append(data)
		print data[7]
	return events

def fetch_task(id):
	query = "SELECT * FROM events where id=\'{0}\'".format(id)
	cursor.execute(query)
	rows = cursor.fetchone()
	return rows
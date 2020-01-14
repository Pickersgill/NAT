import sqlite3

connection = sqlite3.connect("notes.db")
c = connection.cursor();

c.execute("SELECT * FROM courses;")
rows = c.fetchall()

for row in rows:
	print(row)


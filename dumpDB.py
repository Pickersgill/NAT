import sqlite3

connection = sqlite3.connect("notes.db")
c = connection.cursor();

print("\n\ncourses:")
c.execute("SELECT * FROM courses;")
rows = c.fetchall()

for row in rows:
	print(row)

print("\n\nnotes:")
c.execute("SELECT * FROM notes;")
rows = c.fetchall()

for row in rows:
	print(row)

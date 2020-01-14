import sqlite3

conn = sqlite3.connect("notes.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS notes;")
c.execute("DROP TABLE IF EXISTS courses;")

c.execute('''CREATE TABLE courses(
				id INTEGER PRIMARY KEY,
				code text NOT NULL,
				title text	
			);''')

c.execute('''CREATE TABLE notes(
				note_id INTEGER PRIMARY KEY,
				course_id INTEGER REFERENCES courses(id) NOT NULL,
				location text NOT NULL,
				description text,
				created date NOT NULL,
				modified date
			);''')

import sqlite3

conn = sqlite3.connect("notes.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS notes;")
c.execute("DROP TABLE IF EXISTS courses;")

c.execute('''CREATE TABLE courses(
				int id PRIMARY KEY NOT NULL,
				code text NOT NULL,
				title text	
			);''')

c.execute('''CREATE TABLE notes(
				note_id PRIMARY KEY NOT NULL,
				course_id int REFERENCES courses(id) NOT NULL,
				location text NOT NULL,
				created date NOT NULL,
				modified date
			);''')

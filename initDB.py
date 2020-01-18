import sqlite3

conn = sqlite3.connect("notes.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS notes;")
c.execute("DROP TABLE IF EXISTS courses;")
c.execute("DROP TABLE IF EXISTS words;")
c.execute("DROP TABLE IF EXISTS indexing;")

c.execute('''CREATE TABLE courses(
				code text PRIMARY KEY NOT NULL,
				title text	
			);''')

c.execute('''CREATE TABLE notes(
				note_id INTEGER PRIMARY KEY,
				course_code text REFERENCES courses(code) NOT NULL,
				location text UNIQUE NOT NULL,
				description text,
				created date NOT NULL,
				modified date
			);''')

c.execute('''CREATE TABLE words(
				word_id INTEGER PRIMARY KEY NOT NULL,	
				word text NOT NULL
			);''')	

c.execute('''CREATE TABLE indexing(
				word_id INTEGER REFERENCES words(word_id) NOT NULL,
				note_id INTEGER REFERENCES notes(note_id) NOT NULL,
				count INTEGER NOT NULL, 
				PRIMARY KEY (word_id, note_id)
			);''')

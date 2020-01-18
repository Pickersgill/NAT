import sqlite3
import re
import datetime
import config
import os

def get_root_dir():
	return config.get("root")

def wait_key():
	input("Press any key to continue: ")

def open_note(location):
	editor = config.get("default_editor")
	os.system(editor + " " + location)

def add_course(cursor, code, title):
	cursor.execute("INSERT INTO courses VALUES(?, ?)", (code, title))

def remove_course(cursor, course_code):
	cursor.execute("DELETE FROM courses WHERE code=?", (course_code,))
	cursor.execute("SELECT note_id FROM notes WHERE course_code=?", (course_code,))
	result = cursor.fetchall()
	for r in result:
		curr_note_id = r[0]
		remove_note(cursor, curr_note_id)

def remove_note(cursor, note_id):
	cursor.execute("SELECT location FROM notes WHERE note_id = ?;", (note_id,))
	result = cursor.fetchone()
	if len(result) == 0:
		print("Given note_id does not exist.")
		return False
	else:
		location = result[0]
	
	os.remove(location)
	cursor.execute("DELETE FROM notes WHERE note_id = ?", (note_id,))
	cursor.execute("UPDATE indexing SET count = count - 1 WHERE note_id=?", (note_id,))
	cursor.execute("DELETE FROM indexing WHERE count = 0")
	print("Note: " + location + " succesfully removed.")
	return True

def add_note(cursor, course_code, location, description, created):
	sql = "INSERT INTO notes(course_code, location, description, created) VALUES(?, ?, ?, ?)"
	cursor.execute(sql, (course_code, location, description, created))
	cursor.execute("SELECT title FROM courses WHERE code=?", (course_code,))
	course_title = cursor.fetchone()[0]
	new_note = open(location, "w")
	new_note.write(course_code + " " + course_title +  "\t\t\t\t" + created.replace("_", " ") + "\n\n")
	new_note.close()

def get_date():
	date = datetime.datetime.today().strftime("%d-%m-%Y_%H:%M:%-S")
	print(date)
	return date

def print_notes(cursor, course_code):	
	sql = '''SELECT note_id, description, created
				FROM notes 
				WHERE course_code = ? 
				ORDER BY created;'''
	cursor.execute(sql, (course_code,))
	result = cursor.fetchall()
	for r in result:
		print(str(r[0]) + ":\t" + r[1] + ", " + r[2])

def finish_modifying(cursor, location):
	cursor.execute("UPDATE notes SET modified=? WHERE location=?", (get_date(), location,))	
	reverse_index(cursor, location)
	
def reverse_index(cursor, location):
	
	cursor.execute("SELECT note_id FROM notes WHERE location=?", (location,))
	note_id = cursor.fetchone()[0]
	
	f = open(location)

	for line in f:
		line = re.sub(r"[\t\n]", " ",line)
		words = line.split(" ")
		print(words)
		for w in words:
			add_count(cursor, w, note_id)

def add_count(cursor, word, note_id):

	if len(word) < 1:
		return

	cursor.execute("SELECT word_id FROM words WHERE word=?", (word,))
	result = cursor.fetchone()
	if result != None:	
		word_id = result[0]
		cursor.execute('''UPDATE indexing SET count = count + 1 
						WHERE word_id=? AND note_id=?''', (word_id, note_id,))
	else:
		cursor.execute("INSERT INTO words(word) VALUES (?)", (word,))
		cursor.execute("SELECT word_id FROM words WHERE word=?", (word,))
		word_id = cursor.fetchone()[0]
		cursor.execute("INSERT INTO indexing VALUES (?, ?, 1)", (word_id, note_id))

def print_courses(cursor):
	cursor.execute("SELECT code, title FROM courses;")
	courses = cursor.fetchall()
	for course in courses:
		print(str(course[0]) + ": " + course[1])

def valid_course_code(cursor, course_code):
	cursor.execute("SELECT * FROM courses WHERE code=?", (course_code,))
	result = cursor.fetchone()
	return result != None

def valid_note_id(cursor, note_id):
	cursor.execute("SELECT * FROM notes WHERE note_id=?", (note_id,))
	result = cursor.fetchone()
	return result != None


import sqlite3
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
	cursor.execute("DELETE FROM courses WHERE id=?", (course_code,))

def remove_note(cursor, note_id):
	cursor.execute("SELECT location FROM notes WHERE note_id = ?;", (note_id,))
	location = cursor.fetchone()[0]
	os.remove(location)
	cursor.execute("DELETE FROM notes WHERE note_id = ?", (note_id,))
	print("Note: " + location + " succesfully removed.")

def add_note(cursor, course_code, location, description, created):
	sql = "INSERT INTO notes(course_code, location, description, created) VALUES(?, ?, ?, ?)"
	cursor.execute(sql, (course_code, location, description, created))
	cursor.execute("SELECT title FROM courses WHERE code=?", (course_code,))
	course_title = cursor.fetchone()[0]
	new_note = open(location, "w")
	new_note.write(course_code + " " + course_title +  "\t\t\t\t" + created.replace("_", " ") + "\n\n")
	new_note.close()

def get_date():
	date = datetime.datetime.today().strftime("%d-%m-%Y_%H:%M")
	print(date)
	return date

def print_notes(cursor, course_code):	
	sql = '''SELECT note_id, location, description 
				FROM notes 
				WHERE course_code = ? 
				ORDER BY created;'''
	cursor.execute(sql, (course_code,))
	result = cursor.fetchall()
	for r in result:
		print(str(r[0]) + ":\t" + r[1] + ", " + r[2])

def print_courses(cursor):
	cursor.execute("SELECT code, title FROM courses;")
	courses = cursor.fetchall()
	for course in courses:
		print(str(course[0]) + ": " + course[1])

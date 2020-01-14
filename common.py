import sqlite3
import datetime
import config
import os

def get_root_dir():
	return config.get("root")

def wait_key():
	input("Press any key to continue: ")

def add_course(cursor, code, title):
	cursor.execute("INSERT INTO courses(code, title) VALUES(?, ?)", (code, title))

def remove_course(cursor, course_id):
	cursor.execute("DELETE FROM courses WHERE id=?", (course_id,))

def add_note(cursor, course_id, location, description, created):
	sql = "INSERT INTO notes(course_id, location, description, created) VALUES(?, ?, ?, ?)"
	cursor.execute(sql, (course_id, location, description, created))
	
	cursor.execute("SELECT title FROM courses WHERE id=?", (course_id,))
	course_title = cursor.fetchone()[0]
	new_note = open(location, "a")
	new_note.write(course_title +  "\t\t\t\t" + created.replace("_", " ") + "\n\n")
	new_note.close()

def get_date():
	date = datetime.datetime.today().strftime("%d-%m-%Y_%H:%M")
	print(date)
	return date

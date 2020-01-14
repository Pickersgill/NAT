import sqlite3
import datetime

def wait_key():
	input("Press any key to continue: ")

def add_course(cursor, code, title):
	cursor.execute("INSERT INTO courses(code, title) VALUES(?, ?)", (code, title))

def remove_course(cursor, course_id):
	cursor.execute("DELETE FROM courses WHERE id=?", (course_id,))

def add_note(cursor, course_id, location):
	created = datetime.datetime.today().strftime('%d%m%Y')
	sql = "INSERT INTO notes(course_id, location, created) VALUES(?, ?, ?)"
	cursor.execute(sql, (course_id, location, created))


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
	os.system("touch " + location)

def get_date():
	date = datetime.datetime.today().strftime("%d-%m-%Y")
	print(date)
	return date

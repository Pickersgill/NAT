import common

def new_note(cursor):
	print("Which course is this note for? \n")
	cursor.execute("SELECT code, title FROM courses;")
	courses = cursor.fetchall()
	for course in courses:
		print(str(course[0]) + ": " + course[1])
	code = input("Enter course code: ").replace("\n", "")

	# Fetching course id data
	cursor.execute("SELECT id FROM courses WHERE code=?", (code,))
	course_id = cursor.fetchone()[0]

	# Fetching creation time data
	created = common.get_date()
	created.replace(" ", "_")

	# Fetching file location data
	location = common.get_root_dir() + "/" + code + "." + created + ".note"
	location.replace(" ", "_")

	# Fetching description data
	desc = input("Add a description for your note (e.g. Vectors and Scalars):\n\t")
	if len(desc) == 0:
		desc = "untitled"
	
	common.add_note(cursor, course_id, location, desc, created)
	
	common.wait_key()
	return 

def new_subject(cursor):
	print("Adding a new subject:\n")
	code = input("Please give a subject code:\t")
	title = input("Please give a name for the subject:\t")
	cursor.execute('SELECT * FROM courses WHERE (code=? OR title=?)', (code, title))
	result = cursor.fetchall()

	if len(result) == 0:
		common.add_course(cursor, code, title)
		print("Successfully inserted " + title + "with course code: " + code)
	else:
		print("This course title or code is already in use in the following course(s):\n")
		for row in result:
			temp_str = "Entry: "
			for col in row:
				temp_str += str(col) + "\n"
			print(temp_str)
		if(input("would you like to delete the existing courses?\n y - yes\n n - no\n") == "y"):
			for row in result:
				common.remove_course(cursor, row[0])
			print("Entries removed, adding new course...")
			common.add_course(cursor, code, title)
			print("Success!")

	return()

def change_recent_note(cursor):
	print("Change most recent note:")
	return()

def change_note(cursor):
	print("Change a note:")
	return()

def get_notes(cursor):
	print("Retrieve a note:")
	return()

def quit(cursor):
	print("Quitting...")
	exit(1)

class Option:
	def __init__(self, name, function):
		self.name = name
		self.function = function
	
	def get_name(self):
		return self.name
	
	def get_function(self):
		return self.function


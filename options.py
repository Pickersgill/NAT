import common

def new_note(cursor):
	# Fetching course code data
	print("Which course is this note for? \n")
	common.print_courses(cursor)
	code = input("Enter course code: ").replace("\n", "")

	# Fetching creation time data
	created = common.get_date()
	created.replace(" ", "_")

	# Fetching file location data
	location = common.get_root_dir() + "/" + code + "." + created + ".note"
	location = location.replace(" ", "_")

	# Fetching description data
	desc = input("Add a description for your note (e.g. Vectors and Scalars):\n\t")
	if len(desc) == 0:
		desc = "untitled"
	
	common.add_note(cursor, code, location, desc, created)

	if(input("Note creation was successful, to open the note now, enter 'o'").lower() == "o"):
		common.open_note(location)
	else:
		print("Okay, returning to menu")
	
	cursor.execute("UPDATE notes SET modified=? WHERE location=?;", (common.get_date(), location,))

	common.wait_key()

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

def remove_note(cursor):
	print("For which course would you like to remove a note?")
	print("Which note would you like to remove?")	
	common.print_courses(cursor)
	course = input("Enter course code: ")
	
	if not common.valid_course_code(cursor, course):
		print("Given course code does not exist, returning to menu.")
		common.wait_key()
		return
	
	print("Okay, fetching notes for that course...")
	common.print_notes(cursor, course)
	note_id = input("Which note would you like to delete?")

	if not common.valid_note_id(cursor, note_id):
		print("Given note id does not exist, returning to menu.")
		common.wait_key()
		return

	common.remove_note(cursor, note_id)

def change_recent_note(cursor):
	print("Change most recent note:")

def change_note(cursor):
	print("Which course would you like to change notes for?")
	common.print_courses(cursor)
	course_code = input("Enter course code: ")

	if not common.valid_course_code(cursor, course_code):
		print("Given course code does not exist, returning to menu.")
		common.wait_key()
		return
	 
	print("Okay, fetching notes for that course...")
	common.print_notes(cursor, course_code)
	note_id = input("Which note would you like to change?")

	if not common.valid_note_id(cursor, note_id):
		print("Given note id does not exist, returning to menu.")
		common.wait_key()
		return

	cursor.execute("SELECT location FROM notes WHERE note_id=?", (note_id,))
	result = cursor.fetchone()
	
	common.open_note(result[0])
	common.wait_key()

def get_notes(cursor):
	print("Retrieve a note:")

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


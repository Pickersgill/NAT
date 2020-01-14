
def new_note(cursor):
	print("Add new note:")
	return 

def new_subject(cursor):
	print("Adding a new subject:\n")
	code = input("Please give a subject code:\t")
	name = input("Please give a name for the subject:\t")
	cursor.execute("INSERT INTO courses (code, title) VALUES(?, ?)", (code, name))
	print("Successfully inserted " + name + "with course code: " + code)
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


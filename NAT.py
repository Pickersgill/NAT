import sqlite3
import options

optionChars = {
				"s" : "NEW SUBJECT",
				"n" : "NEW NOTE",
				"c" : "CHANGE NOTE",
				"cr" : "CHANGE RECENT_NOTE",
				"g" : "GET NOTES",
				"q" : "QUIT"
			}

def start():
	connection = sqlite3.connect("notes.db")
	cursor = connection.cursor()
	
	menu(cursor)

	connection.commit()
	connection.close()

def menu(cursor):
	print("Welcome to the Note Assistance Tool (NAT):\n")
	options.setCursor(cursor)
	option = ""
	while option != "q":
		option = getOption()
		if option == "s":
			options.newSubject()
		elif option == "n":
			options.newNote()

def getOption():
	menu_size = 20

	for option in optionChars:
		option_string = optionChars.get(option).rjust(20)
		option_string += " - "
		option_string += option.replace("_", " ").ljust(20)
		print(option_string)

	return(input("\nInput option: "))		


def createNote(subject, tags):
	assert type(subject) is StringType, "Subject given is not string: %r" % subject
	if(isInstance(tags, list)):
		if tags.size() > 0:
			assert type(tags[0]) is StringType, "tags given are not of type string"
		else:
			warning("It is reccomended that you give a minimum of 1 tag.")
	else:
		print("tags is not of type list")
		exit(1)
	
	
def warning(message):
	assert type(message) is StringType, "message given is not string"
	print("\nWARNING:\t " + message)	

if __name__ == "__main__":
	start()



# python imports:
import sqlite3
import os

# local imports:
import options

Option = options.Option
optionDict = {
				"nc" : Option("NEW COURSE", options.new_course),
				"nn" : Option("NEW NOTE", options.new_note),
				"cn" : Option("CHANGE NOTE", options.change_note),
				"rn" : Option("REMOVE NOTE", options.remove_note),
				"rc" : Option("REMOVE COURSE", options.remove_course), 
				"crn" : Option("CHANGE RECENT_NOTE", options.change_recent_note),
				"gn" : Option("GET NOTES", options.get_notes),
				"q" : Option("QUIT", options.quit),
			}

def start():
	connection = sqlite3.connect("notes.db")
	
	menu(connection)

	connection.commit()
	connection.close()


def menu(connection):
	cursor = connection.cursor()
	print("Welcome to the Note Assistance Tool (NAT):\n")
	while True:
		os.system("clear")
		option = get_option()
		if validOption(option):
			func_to_call = optionDict.get(option).get_function()
			func_to_call(cursor)	
			connection.commit()
		else:
			input("Invalid option: " + option + "\npress any key to continue.")

def validOption(option):
	for o in optionDict:
		if o == option:
			return True
	return False

def get_option():
	#os.system("clear")
	menu_size = 20
	print()
	for option in optionDict:
		option_string = optionDict.get(option).get_name().rjust(20)
		option_string += " - "
		option_string += option.ljust(20)
		print(option_string)
	
	option = input("\nInput option: ").lower().replace(" ", "")

	return(option)		

def create_note(subject, tags):
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


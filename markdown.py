import re


def parse(location, cursor):
	source = open(location)
	for line in source:
		tags = re.findall(r"<.*?>\s*\w*\s", line)
		for tag in tags:
			tag = re.sub("\s*", "", tag)
			tag_type = re.findall(r"\<.*\>", tag)[0]
			tag_type = re.sub(r"[\<\>]", "", tag_type)
			print(tag_type)
			func_to_call = tagDict.get(tag_type)
			func_to_call(tag, cursor)

def acronym(tag, cursor):
	for t in tag.split(">"):
		print(t)

	return

tagDict = {
		"ac" : acronym
	}

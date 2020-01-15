
config = open(".config")

configDict = {}

for l in config:
	pair = l.split(":")
	key = pair[0].replace(" ", "").replace("\n", "")
	value = pair[1].replace(" ", "").replace("\n", "")
	configDict[key] = value

def get(key):
	return configDict[key]


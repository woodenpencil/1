import json
import difflib
from difflib import get_close_matches
data=json.load(open("D:\\newfolder\\py_projects\\data.json","r"))

def get_def(key):
	key=key.lower()
	if (key in data):
		return data[key]
	elif key.title() in data:
		return data[key.title()]
	elif key.upper() in data:
		return data[key.upper()]
	else:
		if len(get_close_matches(key,data.keys()))>0:
			closest=get_close_matches(key,data.keys())[0]
		else:
			return "The word does not exist."
		answer=input("Did you mean %s ? [y/n]" %closest)
		if answer=="y":
			return data[closest]
		elif answer=="n":
			return "The word does not exist, yet."
		else:
			return "Error: incorrect input."

query=input("Enter a word: ")
defin=get_def(query)
if type(defin)==list:
	for i in defin:
		print("- %s" %i)
else:
	print("- %s" %defin)



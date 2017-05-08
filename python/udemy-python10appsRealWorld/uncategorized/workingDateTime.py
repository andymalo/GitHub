import datetime

r"""
This script creates an empty files.
"""

filename = datetime.datetime.now()

#Create empty file
def create_file():
	"""This function creates an empty file"""
	with open(str(filename.strftime("%Y-%m-%d")+ ".txt"), "w") as file:
		file.write("") #Writing an empty string

create_file()
import glob2
import datetime

fileName = datetime.datetime.now()
files = glob2.glob("*.txt")

with open(str(fileName.strftime("%Y-%m-%d")+ ".txt"), "w") as fileNew:
	for file in files :
		tempFile = open(file, "r")
		fileNew.write(tempFile.read() + "\n")
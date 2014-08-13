import os

fileList = os.listdir(os.getcwd())

for fileName in os.listdir(os.getcwd()):
	if(".html" in fileName):
		if(fileName.replace(".html",".pdf") in fileList):
			continue
		print fileName + " is being converted."
		os.system("unoconv -f pdf " + fileName)
		print fileName + " has been converted."



#Git is the control system, while github is a site that allows backing up.sharing of data
#terminal is the software that allows editing and interacting w the command line, commandline is where you type and get results
#local is on the computer, remote is online.
#version control is organizing the different versions of a file
#staging area is where the files go after git add, ready to be committed. 
#adds files to staging area
#commits the files to staging area
#pushes the files to remote repo
#shows status of files on local repo
#pulls files from remote repo to local
#full path name of current directory
#shows files in current directory
#move between files
#text editor
#creates new file
#moves file
#removes file
#displays file contents

#3.2 directory tree
#pwd
#ls
#git pull <repo>
#mv <file> <location>
#cd
#cat homework.py
#git add . git commit -m "message" git push origin main
#git pull .
#git checkout <branch>

#4.1 Data Types
def checkDataType(val):
	return type(val)

checkDataType(3.14)
checkDataType(True)

#4.2 Conditionals
def evenOrOdd(num):
	if num %2 == 0:
		return "Even"
	else:
		return "Odd"
evenOrOdd(7)
evenOrOdd(10)

#5 Loops

numbers = [1,2,3,4,5]

def sumWithLoop(numbers):
	sumz = 0
	for i in numbers:
		sumz += i
	return sumz
sumWithLoop(numbers)

#6.1 Lists

listy = ['a','b','c']
def duplicateList(listy):
	return [i for i in listy for j in range(2)]
duplicateList(listy)

#6.2 Debugging
def square(num):
	return num * num


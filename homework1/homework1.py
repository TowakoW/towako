# File: homework1. py
# --- Variables and Data Types ---
a=10
print(a)
print(type(a)) #a is aninteger, a whole number with no decimals
b=1.5
print(b)
print(type(b)) #b is a floating point number
c=3j
print(c)
print(type(c)) #c is a complex number
d="hello"
print(d)
print(type(d)) #d is a string, or a phrase
e=[1,2,3]
print(e)
print(type(e)) #e is an list
f={"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, a collection of key-value pairs
g=(1,2)
print(g)
print(type(g)) #g is a tuple, ordered, immutable collection of items
h=["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is also a list...?
i=True
print(i)
print(type(i)) #i is considered a bool
j=None
print(j)
print(type(j)) #j is a NoneType, representing the absense of a value
k=[True, "blue", 12]
print(k)
print(type(k)) #k is also a list. There are too many of these, are there not?
l=str(14)
print(l)
print(type(l)) #l is a string data type
m=1e4
print(m)
print(type(m)) #m is a power, and is a floating point number. This is also the last one that I have to do.
# 1. 9 types. Probably.
# 2. integer, float, string, list, nonetype, bool, tuple, dictionary, complex number
# 3. e,h,k are lists. d and l are strings. b and m are floats.
# 4. l is not an integer because str() converts it into a string.
# 5. hopefully, n is a set.
n={1,2,3,4}
print(n)
print(type(n)) 
# --- Booleans ---
print(10>9) #True, 10 is greater than 9
print(10==9) #False, 10 does not equal 9
print(10<=9) #False, 10 is not greater than or equal to 9
print(bool("abc")) #True, any string is true if not empty
print(123) #True, any number is true if not 0
print(bool(["apple", "cherry", "banana"])) #True, lists are true if not empty
print(bool(True)) #True, if not False
print(bool(False)) #False
print(bool(0)) #False, another exception to the "true"s
print(bool("")) #False, it is empty
print(bool(" ")) #True, it is not empty
print(bool(())) #False, it is empty
print(bool([])) #False, it is empty
print(bool({})) #False, it is empty
print(bool(True and False)) #False, only true if both "True" amd "False" are true
print(bool(True and True)) #True, both are true
print(bool(False and False)) #False, both are not True
print(bool(True or False)) #True, will always evaluate to True if it is an option
print(bool(True or True)) #True, both options are true
print(bool(False or False)) #False, no true option
print(bool(not(False))) #True, it's not false
print(bool(not(True))) #False, if it can't be true.
#It defaulted to True unless it was blank, zero, or of False was the only option.
#the print(bool(" ")), I wasn't expecting the space to count as a character.
#print(bool(6)), it is true because it is not left blank
# print(bool(not(True) or False)) there are no true options.
# --- Operators ---
print(10+5) #15, addition
print(10-5) #5, subtraction
print(2*4) #8, multiplication
print(6/3) #2, division
print(5%2) #1, remainder
print(3**2) #9, power
print(15//2) #7, floor devision
print(5==2) #False, 5 does not equal 2
print(10!=10) #False, 10 is equal to 10
print(2<5) #True, 2 is less than 5
print(1>=10) #False, 1 is not greater than or equal to 10

x=5
x += 5
print(x) # new x is 5+5, 10
x -= 4
print(x) #new x is 10-4, is 6
x *= 3
print(x) #new x is 6*3, 18
#1 operator and is true only if both are True. print(bool(True and True)), print(bool(True and False))
#2 operator or selects True, and is false if there is no True. print(bool(True or False)), print(bool(False or False))
#3 operator not is the oposite of the following subject. print(bool(not(False))), print(bool(not(True)))
#1 / is division, while // is floor division, providing the lower rounded solution.
#2 % is the remainder to division, while // is floor division
#3 %. print(7%3)
#4 assigns the value on the right to the name on the left side of the equation sign
# --Strings--
my_string="hello"
print(my_string) #prints hello
print(my_string[0]) #prints the first character
print(my_string[1]) #prints the second character
print(my_string[3]) #prints the third character
print(my_string[4]) #prints the fourth different letter
print(my_string[-1]) #prints the last differing character
print(my_string[1:3]) #prints from the second element to the third, no repeated elements
print(my_string[0:5:2]) #prints the first to fifth element, skipping every other one.
print(len(my_string)) #"hello" is 5 elements long
print(my_string+"goodbye") #adds the elements together
print(my_string*7) #repeats "hello" 7 times
# sclicing takes apart a part of the string, done in #2-9
name="Oski"
print("Hello, my name is", name) #fills in name with previously defined "Oski"
print(f"Hello, my name is {name}") #same results as above.
# ability to incorporate variable in the middle of a sentence/string.
# --Terminal Commands--
#cd
#change directories, moves to folders.
# cd python_decal_fa25
#ls
#list directives, shows contents on file
#ls Users
#ls-a
#Shell command, list directories "all", lists directories including dot-files
#ls-a Users
# mkdir
# make directory, creates new file
# mkdir towako
# cat
# lists contents of files to standard output
# cat towako
# pwd
# print working directory, displays full path
# pwd python_decal_fa25
# cd ..
# windows command prompt to move up directory lvl
# cd .. python_decal_fa25
# cd . 
# stay in current directory
# cd . 
# cd ~
# changes directory to home folder
# cd ~
# cp
# copy files/directories
# cp towako python_decal_fa25
# mv
# move/rename files
# mv towako python_decal_fa25
# rm
# delete files/directories
# rm towako
# clear 
# clear ternimal screen
# clear
# grep
# search for patterns in files/output
# grep "ls" python_decal_fa25
# 1. less, view file contents interactively. rmdir removes empty directories. head displays beginning of a file.
# 2. ls-a lists all files including hidden dot files
# 3. dot file, has a . to hide it from computer system
# 4. ls-l, provides a long listing. -v, used w cp or rm to display detailed output. -r, cp or rm, operate recursively
# this is to debug git
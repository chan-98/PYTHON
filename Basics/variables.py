# variable = a container for any value, of any type. Behaves exactly as the value behaves.
# no keywords necessary

# STRING VARIABLE
name = "Chandini"
# name is a string variable. the value of the string should always be within ""
print(name)
print()
print("Hi "+name)

print("Testing spaces")

print('It seems that even if you leave gap between 2 print statements, they would still print in the successive lines')
print()
print("So if you want space between 2 lines, do print() instead, unless I discover another way")

print()
print("TO CHECK THE TYPE OF THE VARIABLE: print(type(var_name))")
print(type(name))
last_name = "Venkatesan"
full_name = name + " " + last_name
print("Hello! Welcome " + full_name)
print()
print()
print()


# INTEGER VARIABLE
# make sure to not put the int value in " " because then it will be considered as a string
# and it cant be used for any math.
age = 23
str_age = "23"
print(type(age))
print(type(str_age))
print(age)
age += 1
print(age)
# The following is not going to work
# print("Your age is " + age)
# This results in a TypeError since a string literal (the first part of the print statement) can't be combined with an int variable.
# One way to bypass this is by "typecasting"

#The following will work now
print("Your age is " + str(age))
print()
print()
print()


# FLOAT VARIABLE
# floating point number (decimal)
height = 158.31
print(type(height))
print(height)
print("Your height is " + str(height) + "cm")
print()
print()
print()


#BOOLEAN
# where useful in loop statements like if statements while testing conditions
Human = True
print(Human)
print(type(Human))
human = "True"
print(human)
print(type(human))
print("Are you a human: " + str(Human))
print()
print()
print()

#############################################################
print("Now we learn MULTIPLE ASSIGNMENTS")
# MULTIPLE ASSIGNMENTS
# allow us to assign multiple variables at the same time in the same line of code
Name, Age, attractive = "Chan", 23, True
print(Name)
print(Age)
print(attractive)
Bablu = Chandan = Divya = "M Tech Computational Biology"
print(Bablu)
print(Chandan)
print(Divya)
print()
print()
print()

###################################
# STRING FUNCTIONS (STRING METHODS)
print('Now we learn STRING FUNCTIONS')

print(len(name))
print(name.upper())
print(name.lower())
print(name.find('i'))
print(name.capitalize())
print(name.isalpha())
print(name.isdigit())
print(name.count("i"))
print(name.replace("i","a"))
print(name*3)
print()
print()
print()


#######################################
# TYPECASTING
# convert 1 datatype to another
print("We will learn TYPECASTING")
x = 1 #int
y = 2.3 #float
z = "3" #str
print(x+1)
print(y)
print(z*3)
a = str(x)
b = str(y)
c = str(z)
# print(a+1) gives TypeError
print(a)
print(b)
print(c*3)
print()
print()
print()
print()
######################################
######################################
######################################
print("Time to learn how to take USER INPUT!!!")
######### USER INPUT ##########
name2 = str(input("What is your name?: "))
age2 = int(input("How old are you?: "))
height2 = float(input("Enter your height!: "))
print("Hello " + name2)
print("You are "+str(age2)+" years old")
print("You are "+str(height2)+" cm tall")
# Failing to do stringcasting will result in TypeError
print()
print()
print()
print()

############################################################
### MATH FUNCTIONS (METHODS) ###
# located in the math module
# do import math in the beginning of coding
############################################################
import math
print("MATH METHODS! Make sure to <import math> in the top before beginning to write code")
e, f, g = 5, 6.09, 7.2
pi = 3.14
print(max(e,f,g))
print(round(pi))
print(math.sqrt(f))
print(math.ceil(pi))
print(math.floor(pi))
print(math.pow(g,3))
print()
print()
print()
print()

#####################################################
print("Now we learn STRING SLICING")
##### STRING SLICING #####

#slicing = creating a substring by extracting elements from another string

print("This can be done using either of the 2 operators:")
print("<indexing[]>   or    <slice()>")
print("The slice() operator is more complex")
print()
print("Three arguments to provide while using indexing[] operator:")
print(" start:stop:step ")
print()
print("Your full name is "+full_name+". Now let's extract your first name using indexing[].")
first_name1 = full_name[0:7]
print(first_name1)
#The first index (0) is inclusive, the stopping index (7) is exclusive
#WHich means character at 0 will print, but at 7 won't print.
#Will stop before 7.
first_name2 = full_name[:8]
print(first_name2)
last_name1 = full_name[9:19]
print(last_name1)
last_name2 = full_name[9:]
print(last_name2)
### In all these cases, step is 1 by default
# if we set step to 2, it will only extract every 2nd character from the start index
print()
funkyName = full_name[0:19:1]
print(funkyName)
funky2Name = full_name[0:19:2]
print(funky2Name)
funky3name = full_name[::3]
print(funky3name)
print()
print()
print("REVERSING A STRING USING INDEXING[]")
print('In this case, the step value will be -1')
############## PRINTING A STRING IN REVERSE ##############

reversed_name = full_name[::-1]
print(reversed_name)
print()
print()
print("NOW WE WILL USE slice(). Slice objects are reusable.")
print("Three arguments to provide while using indexing[] operator:")
print(" start,stop,step ")
print('Exactly the same as indexing[]')
print("Syntax: slice_object_name = slice(start,stop,step)")
print()
website = "https://www.google.co.in/"

#we want our slice object to begin where the website name starts (g)
#start index will be 12
#stop index is tricky because not all websites have same length
#so we wont be able to use the same one
#therefore we use negative index.
#each element in a string has a positive and negative index
#positive index starts from the left at 0
#negative index starts from the right at -1
#In this case, google.co.in/, I want my substring to stop where the dot is.
#So my stop index will be -7
#Again, start index is inclusive but stop index is exclusive
#Which means character at index 12 (g) will print but the one at -7 (.) wont print

#syntax:
#       strVar = " "
#       sliceObj = slice(start, stop, step)
#       print(strVar[sliceObj])

webpage = slice(12, -7)
print(website)
print(website[webpage])
website2 = "https://www.yahoo.co.in/"
print(website2[webpage])
print("Because we are using negative stop index, as long as the domains are same, the sliceObj can be re-used")
print()
print()
print()
print()
print("THE END OF VARIABLES BASICS")

###############################################################
###############################################################

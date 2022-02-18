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

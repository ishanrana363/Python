# variables rules


# 1. single Quotes or double Quotes
"""game = "cricket"
print(game)
home = 'dinajpur'
print(home)"""

# 2. Case-Sensitive

# name = "ishan"
# print(name)
# Name = "rana"

# 3. A variable name must start with a letter or the underscore character

# age = 20
# print(age)
#
# _district = "Rangpur"
#
# print(_district)

# 4 A variable name cannot start with a number
# 3dogs = "bla bla"  wrong
# print(3dogs)

# 5 A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# _firstName1 = "Ishan"
# print(_firstName1)

# 6 A variable name cannot be any of the Python keywords.
# for = "for"  wrong variables
# print(for)


# Camel Case

# firstName = "Ishan Rana"
# print(firstName)

# Pascal Case

# FirstName = "Ishan Rana"
# print("name is",FirstName)


# Snake Case


# my_variable_name  = "jhone"
#
# print(my_variable_name)


# Many Values to Multiple Variables

# x,y,z = 10,20,30
#
# print(x)
# print(y)
# print(z)

# One Value to Multiple Variables

# x = y = z = "Orange"
#
# print(x)
# print(y)
# print(z)




# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking


# fruits = ["apple","banana","cherry"]
#
# x,y,z = fruits
#
# print(x)
# print(y)
# print(z)


#  Global Variables

# x = "awesome"
#
# def myFun () :
#     print("Python is ",x)
# myFun()

# local variables

x = "fantastic"

def fun () :
    x = "awesome"
    print("Python is ", x)
fun()

print("Python is", x )




















































































































































































































"""
Basic Arithmetic Operations:
    1. Addition
    2. Subtraction
    3. multiplication
    4. Division
    5. Modulus
    6. Squares
"""

# Arithmetic operations on two variables
a = 6
b = 2
print("Addition: {0} + {1} = {2}".format(a, b, a+b))
print("Subtraction: {0} - {1} = {2}".format(a, b, a-b))
print("Multiplication: {0} * {1} = {2}".format(a, b, a*b))
print("Division: {0} / {1} = {2}".format(a, b, a/b))
print("Modulus: {0} % {1} = {2}".format(a, b, a%b))
print("Square: {0} ** {1} = {2}".format(a, b, a**b))
print("")

# Declaring variables and verifying the types
number = 1
string = "String"
ratio = 1.2
boolean = True

print("Type of the following variables\nNumber: {0}\nString: {1}\nFloat: {2}\nBoolean: {3}".format(type(number), type(string), type(ratio), type(boolean)))
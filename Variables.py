"""
Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""
x = 23
y = "Om"
z = True

for i in x, y, z:
    print("Value: {0} and its type: {1}".format(i, type(i)))

# Assign same value to multiple variables
a = b = c = 1
print("values", a, b, c)

# Assign values to multiple variables
a, b, c = 1, 2, 3
print("values", a, b, c)

# Local scope of variable
city = "Pune"


def my_city():
    """
    This is an example of local variable
    :return: None
    """
    city = "Aurangabad"
    print("My city is "+city)


my_city()
print("My city is "+city)


def my_current_city():
    """
    This is an example of Global variable
    :return: None
    """
    global city
    city = "Chennai"
    print("My city is " + city)


my_current_city()
print("My city is "+city)




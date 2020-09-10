"""
Conditionals and Booleans
Booleans are named after the mathematician, George Boole,
who defined an algebraic system for determining the truth value of logical expressions.

We only ever have two Boolean values, and in Python those values are the words True and False.

Truth value
Every value in Python has an associated truth value, which determines whether or not the value is considered
True or False when we test the truthiness of a value. This happens when we use the value as a condition, for example.
"""
print(bool(0))              # False
print(bool(6))              # True

print(bool("Caterpillar"))  # True
print(bool(""))             # False

print(bool([]))             # False
print(bool([0, 1, 2, 3]))   # True

print(bool(True))           # True
print(bool(False))          # False

# Apart from these values, everything else in Python is truthy.

"""
Comparison operators
We have eight comparison operators in total
1. <
2. >
3. <=
4. >=
5. ==
6. !=
7. is
8. is not
"""

# We can use a function called id to find out where something is being stored,
# represented as a long series of numbers.
# This long series of numbers is an address that references a location in memory.
# We can print these memory addresses to verify that the two lists are not in fact the same:

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # 139806639351360
print(id(b))  # 139806638418944

print(a == b)  # True
print(a is b)  # False

# We can make the two lists the same by making a small change.
# Instead of defining this new identical list when assigning to b, let's just refer to the one we assigned to a:

a = [1, 2, 3]
b = a

print(id(a))  # 139685763327296
print(id(b))  # 139685763327296

print(a == b)  # True
print(a is b)  # True

# Now both of our memory addresses are the same, and as a result,
# the is operator yields True when we compare a and b.

"""
Order of operations
Comparison operators are always lower priority than arithmetic operators.
For example, if we write an expression like this:

5 + 4 < 3 * 2

The comparison is effectively:

(5 + 4) < (3 * 2)
"""

"""
Conditional statements
Conditional statements allow us to run some block on code if and only if some condition is met.
We can use this structure to control the flow of our application based on whether or not something is the case.
For example, we might only permit a user to log into a website if they enter the correct credentials.
"""
age = int(input("How old are you? "))

if age < 16:
    print("You are eligible for the child rate of 80p.")
elif age >= 60:
    print("You are eligible for the OAP rate of £1.")
else:
    print("You must pay the standard rate of £1.50.")

name = input("Please enter your name: ")

if name:  # Checks the truth value of name by calling bool
    print(f"You entered {name}")
else:
    print("You didn't type anything")

"""
Exercise
Write a program to determine whether an employee is owed any overtime.
You should ask the user how many hours the employee worked this week,
as well as the hourly wage for this employee.

If the employee worked more than 40 hours,
you should print a message which says the employee is due some additional pay, as well as the amount due.
The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours.
In effect, the employees get paid 110% of their hourly wage for any overtime.
"""
hours_worked = float(input("How many hours worked this week? "))
hourly_wage = float(input("Hourly wage? "))
overtime = 0
payment = hourly_wage * 40

if hours_worked > 40:
    overtime = (hours_worked - 40) * 0.1 * hourly_wage
    print(f"Employee is due some additional pay, The total amount due is ${(payment + overtime):.2f}.")
else:
    print(f"Employee's payment does not include overtime, the total amount due is ${payment:.2f}.")

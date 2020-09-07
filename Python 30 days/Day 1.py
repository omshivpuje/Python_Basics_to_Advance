"""
Integers and floats are basic numerical types in Python.
Integers are used to represent whole numbers, and floats are used for real numbers with some decimal component.
For example, we'd use an integer for the number 3, but a float for 3.141.
"""
print(f'Integer {4}, Float {3.1415}')

"""
expression
What exactly is an expression? We don’t need to get into too much detail,
but we can think of it like this: if something in our code evaluates to a value,
it’s an expression. Bear with me, this is going to make a lot more sense in a moment.
When we do this, the order the expressions are evaluated in corresponds to BODMAS-
(Brackets, Orders of, Division, Multiplication, Addition, Subtraction)
(or PEMDAS, etc., if you learnt a different acronym in school).
"""
print('Without grouping result', 5 * 3 - 6 + 2 / 4)
print('Grouped Result', (5 * 3) - (6 + 2) / 4)

"""
Exercise:
1. Print your age to the console.
2. Calculate and print the number of days, weeks, and months in 27 years.
Don’t worry about leap years!
3. Calculate and print the area of a circle with a radius of 5 units.
You can be as accurate as you like with the value of pi.
"""
years = 27
months = 12
days = 365
weeks = 52

pi = 3.14
r = 5

print(f'1. My Age is {25}')
print(f'2. Days are {years * days}, Weeks are {years * weeks}, Months are {years * months}')
print(f'Area of a circle with radius {r} is {pi * r ** 2}')

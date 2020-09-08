"""
String basics
Strings in Python are ordered sequences of zero or more characters, and we can use them to represent arbitrary collections of symbols. This might be words, whole sentences, or random strings of letters, numerals, and punctuation. Strings are sometimes called "string literals".

In order to create a string, we just need to wrap some series of characters in quotation marks:
"""
print("This is a string!")

"""
Getting values from the user
So far we’ve provided all the values in our Python code, but sometimes we need to get values from the user instead.
For example, maybe we want to get the user’s name and age.

Luckily we don’t have to implement something like this from scratch, because Python comes with another function to do
this exact job. This function is called input.

We call input in exactly the same way as print, we just need to write the function name and put opening and closing 
parentheses directly after:
"""
input("Please enter your name:")

"""
Exercise

1. Ask the user for their name and age, assign theses values to two variables, and then print them.
2. Investigate what happens when you try to assign a value to a variable that you’ve already defined.
Try printing the variable before and after you reuse the name.
3. Below you’ll find some code with a number of errors. Try to go through the program line by line and
fix the issues in the code. I’d encourage you to try running the program while you’re working on it,
as reading the error messages is great practice for debugging your own programs.
hourly_wage = input("Please enter your hourly wage: ')

prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")
"""
name = input("Enter the name: ")
age = int(input("Enter the age: "))
print(f"Name is {name} and age is {age}")

name = "Omi"
print("Assigned new value to already defined variable name", name)

hourly_wage = input("Please enter your hourly wage: ")

print("Hourly wage: ")
print(hourly_wage)

hours_worked = input("How many hours did you work this week? ")
print("Hours worked: ", hours_worked)

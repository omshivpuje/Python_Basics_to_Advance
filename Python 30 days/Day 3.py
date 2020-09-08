"""
Day 3: Formatting Strings and Processing User Input

String concatenation
String concatenation means joining two or more strings together.

Truncation
Truncation is the act of shortening something by removing some part of it.
For example, we can refer to truncating a float, which means that we're removing everything after the decimal point.

String interpolation
String interpolation is the act of inserting some new content into an existing string.
"""
print("{} is {} years old!".format("John", 24))

# Placeholders {}
output = "{} is {} years old, and {} works as a {}."

print(output.format("John", 24, "John", "web developer"))

# Ordered placeholders
output = "{0} is {1} years old, and {0} works as a {2}."

print(output.format("John", 24, "web developer"))

# f-strings
name = "John"
age = 24

print(f"{name} is {age * 12} months old!")

"""
Comments
Using good, descriptive names we can do a lot to make our code self-documenting; however,
sometimes even great code can be hard to reason about. Some things are just complicated, after all.

In instances like this, it can be useful to use comments to explain to readers of our code (which includes us) 
what the code is doing.

In order to write a comment, we just need to put a # directly before the message we want to write.
This is going to tell Python not to treat what follows as code.
"""
# This is a comment!

"""
Basic String Processing
The final thing I want to mention in this post is some common string processing operations,
such as changing the case of the letters, or removing white space (space characters, tabs, newlines, etc.) 
from the ends of strings. This kind of thing happens all the time when we’re dealing with user input.

We have a number of different options for changing the case of letters in a string.
Here we’re going to focus on four important options: lower, upper, capitalize, and title.

lower and upper turn the entire string to lowercase and uppercase, respectively.
Characters which don’t have a case, such a punctuation characters, are ignored.

capitalize is going to turn the first character to uppercase, with the rest being lowercase.
title is going to turn the string to title case, which means every word starts with a capital letter,
and all other letters are turns to lowercase.

In order to use these methods, we just need to use the dot notation again, just like with format.
"""
print("Hello, World!".lower())       # "hello, world!"
print("Hello, World!".upper())       # "HELLO, WORLD!"
print("Hello, World!".capitalize())  # "Hello, world!"
print("hello, world!".title())       # "Hello, World!"
print("  Hello, World!  ".strip())   # Using strip method for "   Hello, World!"

"""
split, join, and Slices
"""
# Join
from typing import List

project_authors = ["Mike", "Sofia", "Helen"]
authors = ", ".join(project_authors)

print(f"The people who worked on this project are: {authors}.")

print(f"The people who worked on this project are: {', '.join(project_authors)}.")

# Split
user_numbers = input("Please enter 5 numbers separated by commas: ")  # 1,2,3,4,5
numbers_list = user_numbers.split(",")

print(numbers_list)  # ['1', '2', '3', '4', '5']

sample_string = "Python"

print(list(sample_string))  # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string))  # ('P', 'y', 't', 'h', 'o', 'n')

"""
Exercises:
    
    1. Ask the user to enter their given name and surname in response to a single prompt.
    Use split to extract the names, and then assign each name to a different variable.
    For this exercise, you can assume that the user has a single given name and a single surname. 
"""
name, surname = input("Enter your name and surname with separated comma and space: ").split(", ")
print(f"The entered name is {name} and surname is {surname}")

# 2. Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method.
# Remember that you can only join collections of strings,
# so you’re going to need to do some initial processing of the list of numbers.
numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(f"{', '.join(stringified_numbers)}")

"""
3. Below you’ll find a short list of quotes:

 quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
 ]
Each quote is a string, but each string actually contains quote characters at the start and end.
Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

You may also want to try a solution using strip.
"""
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
for quote in quotes:
    print(quote[1:-1])

for quote in quotes:
    print(quote.strip("\'"))

"""
4) Ask the user to enter a word, and then print out the length of the word.
You should account for any excess whitespace in the user’s input,
so you’re going to have to process the string before you find its length.

If you want to take this a little bit further, you an ask the user for a long piece of text.
You can then tell them how many characters are in the text overall, and you can also provide them a word count.
"""
words = input('Enter the words here: ').split()
print(f"There are {len(words)} words in {words} in the provided sentence.")

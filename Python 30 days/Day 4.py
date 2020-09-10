"""
Lists
Simply put, lists are containers for other values. Unlike strings, which are collections of just characters,
lists can
store whatever values we like. We can even mix different types of values if we want.

We define a list using square brackets like this:

names = ["John", "Alice", "Sarah", "George"]

Subscription expression
Subscriptions expressions are used for accessing values in many collections.
For sequences, they are used for accessing elements by index.
"""
names = ["John", "Alice", "Sarah", "George"]

print(names[2])  # Sarah
print(names[-1])  # George
"""
Adding items to a list
Extending list by the end can be done by append, extend and + operand
"""
names.append("Simon")
print(names)

# Can add item or items using + operand
names += ['Bob']
print(names)

# Inserting the item at specified index can be done by insert method
names.insert(2, 'Prince')
print(names)

"""
Removing items from a list

    1. remove
    2. pop
    3. del
    4. clear
"""
names.remove('Bob')
print(names)

del names[2]
print(names)

names.pop(1)
print(names)

names.clear()
print(names)

"""
Tuples are very similar to lists in that they're containers for other values,
but there are some important differences that we'll discuss later one.

All we need to define a tuple is a series of comma separated values:

names = "John", "Sarah", "Alice"
"""
names = "John", "Sarah", "Alice"
print(names)

"""
For example, it’s totally legal (and common) to put tuples in a list. Maybe we want to store movie names
and release dates together in a list of movies like this:

"""
movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]
print(movies)

"""
Accessing values in a tuple
Much like with lists, tuples are ordered collections, where each item can be accessed by
index based on their position in the collection.

Tuples vs lists
One of big differences between tuples and lists is that tuples are immutable.
We can’t change them once we define them.
"""

"""
Exercises
1. Create a movies list containing a single tuple. The tuple should contain a movie title,
the director’s name, the release year of the movie, and the movie’s budget.
2. Use the input function to gather information about another movie.
You need a title, director’s name, release year, and budget.
3. Create a new tuple from the values you gathered using input.
Make sure they’re in the same order as the tuple you wrote in the movies list.
4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
5. Add the new movie tuple to the movies collection using append.
6. Print both movies in the movies collection.
7. Remove the first movie from movies. Use any method you like.
"""
movies = [
    ("Batman: The Dark Knight", "Christopher Nolan", 2008, "$185 million")
]

print("Add another movie")
title = input("Please enter the title of the movie: ").strip().title()
director_name = input("Please enter directors name: ").strip().title()
release_year = int(input("Please enter release year: "))
budget = input("Please enter the budget of the movie: ")
movie = (title, director_name, release_year, budget)
print(f"The movie {movie[0]} is released in year {movie[2]}.")

movies.append(movie)
print("The movies available:", movies)

del movies[0]
print("The movies available:", movies)

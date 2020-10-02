"""
Day 9: Unpacking, Enumeration, and the zip Function
Unpacking is generally used to perform several
assignments at once, by extracting the individual values from some iterable. This process is also called
destructuring.
"""
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for title, director, year in movies:
    print(f"{title} ({year}), by {director}")

"""
Enumeration
One common application for unpacking is when using a function called enumerate.
"""

for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")

"""
Zip
"""
movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = list(zip(movie_titles, movie_directors))

for title, director in movies:
    print(f"{title} by {director}.")

movies_list = movies

print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")


print("\n\n")
"""
Exercise:
"""
# 1) Below is some simple data about characters from BoJack Horseman:
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
# The data contains the character name, the voice actor or actress who plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print each tuple in the following format:
# BoJack Horseman is a horse voiced by Will Arnet.

for char_name, voice_actor, species in main_characters:
    print(f"{char_name} is a {species.lower()} voiced by {voice_actor}")

# 2) Unpack the following tuple into 4 variables:
#
# ("John Smith", 11743, ("Computer Science", "Mathematics"))
# The data represents a student's name, their student id number, and their major and minor disciplines in that order.
name, id, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))
print(f"{id}: {name} has major {major} and minor {minor}.")

# 3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list
# containing three items, and a tuples containing four items.
cities = ['Pune', 'Banglore', 'Chennai']
states = ['Maharashtra', 'Karnataka', 'Tamilnadu', 'Delhi']

states_and_cities = zip(states, cities)
for state, city in states_and_cities:
    print(f"{city} is in {state}!")

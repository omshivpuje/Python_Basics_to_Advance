"""
Movie Budget

The brief
Below you'll find a list which contains the relevant data about a selection of movies.
Each item in the list is a tuple containing a movie name and movie budget in that order:

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

For this project, your program should do the following:

1. Calculate the average budget of all movies in the data set.
2. Print out every movie that has a budget higher than the average you calculated.
You should also print out how much higher than the average the movie's budget was.
3. Print out how many movies spent more than the average you calculated.

If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.

You can do this by asking the user how many movies they want to add, which will allow you to use a for loop and range
to repeat some code a given number of times. Inside the for loop, you can write some code that takes in some user
input and appends a movie tuple containing the collected data to the movie list.
"""

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count = int(input("Enter how many new movies you wish to add: "))

for _ in range(new_movie_count):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    new_movie = (name, budget)
    movies.append(new_movie)

total_budget = 0
for movie in movies:
    total_budget += movie[1]


avg_budget = total_budget/len(movies)
high_budget_movies_count = 0
for movie in movies:
    if movie[1] > avg_budget:
        over_average_cost = movie[1] - avg_budget
        print(f"{movie[0]} cost ${movie[1]}: ${over_average_cost} over average.")
        high_budget_movies_count += 1


print(f"There are {high_budget_movies_count} number of movies which has budget more than {avg_budget}.")

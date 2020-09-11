"""
For Loops

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

for movie in movies:
    # Check the title of the current movie is Memento
    if movie[0] == "Memento":
        # If the title is Memento, inform the user that the movie exists and break the loop
        print("Memento is in the movie library!")
        break

"""The range function Python has a built in function called range which is capable of producing a series of integers 
according to some set pattern. For example, we might want to get a series of numbers starting from 1 and ending at 
100, moving in steps of 3. In this case, we'd have 1, 4, 7, 10, 13, 16, 19, etc. """
print(list(range(0, 10, 2)))  # 0, 2, 4, 6, 8
print(list(range(0, 10, 3)))  # 0, 3, 6, 9

"""
Exercise
    1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: 
their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be 
paid at the end of the week in a nice, readable format. 

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
"""
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for name, hours_worked, wage in employees:
    print(f"{name} is due amount {hours_worked * wage}")

total = 0

for employee in employees:
    total += employee[2]

average_wage = total / len(employees)

for employee in employees:
    if employee[2] > average_wage:
        print(f"{employee[0]} earns more than average.")

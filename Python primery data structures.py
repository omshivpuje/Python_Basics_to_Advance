"""
Primary Data structures:
    1. List
    2. Tuple
    3. Dictionary
    4. Sets
"""

# List
# Lists are mutable and ordered. Also can have different, duplicate members. can be declared in [].
ranks = [1, 2, 3, 4, 5]
fruits = ["Orange", "Mango", "Pineapple", "Strawberry"]
print("ranks: {0}, fruits: {1}".format(ranks, fruits))
print("Type of list", type(ranks))
print("")

# Tuple
# Tuples are ordered, immutable and declared in ().
t1 = ("Pune", 1, True)
print("Items in t1", t1)
print("Type of tuple", type(t1))
print("")

# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets {}, and they have keys and values.
my_car = {
    "Brand": "Ford",
    "Make": 2010,
    "Colour": "White",
    "Insurance": True
}

print("My car", my_car)
print("Type of my car object", type(my_car))
print("")

# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
copy = [1, 2, 1, 2, 3, 4, 5, 6, 1, 3, 5, 3]
s1 = set(copy)
print("Copy list", copy)
print("Set is", s1)


# This file contain example of vararg
def details(name, *vararg):
    print("My name is", name)
    for item in vararg:
        print(item)


details("Omi", "ID: 7", "Course: Data Science!")

import re

name = 'My name is Omprakash!'
d = re.search("name is ", name)
print(name[d.end():])
print(name.find("name is "))

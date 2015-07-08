"""
Lists are a datatype you can use to store a collection
of different pieces of information as a sequence
under a single variable name. (Datatypes you've already
learned about include strings, numbers, and booleans.)
"""

suitcase = ["pangolin", "cassowary", "sloth", "tiger"]
suitcase.append("razer")
suitcase.append("plannar")
suitcase.append("book")

list_length = len(suitcase ) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)


# List Slicing

print(suitcase[0:1]) # displays first
print(suitcase[1:3]) # displays second and third
print(suitcase[0:list_length]) # displays all (list_length = 7)
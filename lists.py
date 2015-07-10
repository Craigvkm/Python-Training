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

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end
print("cat = %s" % cat)
print("dog = %s" % dog)
print("frog = %s" % frog)

animals = ["aardvvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Finds the index for duck
animals.insert(duck_index, "Cobra") # Inserts Cobra at that index pushing everything else down
animals.remove("aardvvark") # Removes list item
print(animals)

# Cycling through Lists

numbers = [1, 4, 6, 7, 3, 2]
number_length = len(numbers) # Gets the number of items in list
numbers.insert(number_length, 5)  # Inserts number into list
numbers.sort() # Sorts list alphebetically/numerically

for number in numbers: #Cycle through list based on how many items are in it.
	print(number) 

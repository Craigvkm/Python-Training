# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents['Puffin']) # Prints Puffin's room number


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair

# Add some dish-price pairs to menu!
menu['Fried Eggs'] = 10.50
menu['Pancakes'] = 5.99
menu['Waffles'] = 7.99

# Delete/Modify Entry
menu['Crap'] = 0.99 # Entry Mistake
menu['Crap'] = 0.01 # Change Value
del menu['Crap']    # Delete Entry


print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

print("\n\n Complex List \n\n")

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()
# print(inventory['backpack'][0]) # Prints first item in backpack
print("Inventory:")
for item in inventory['backpack']:
	print(item)

print ("\n\n Final Lesson \n\n")
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['backpack'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50
names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]

for name in names:
	print(name)

# Add Space Temporarily for readability
print("\n\n")

webster = {
	"Aardvark" : "A star of popular children's cartoon show.",
	"Baa" : "The sound a goat makes.",
	"Carpet" : "Goes on the floor.",
	"Dab" : "A small amount"
}

for key in webster:
	print("Key is : %s" % key)
	print("Definition is : %s" % webster[key])

# Add Space Temporarily for readability
print("\n\n")


# Print Even numbers
print("Printing Even numbers")
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
	if number%2 == 0:
		print(number)

# Tests for a object type "list"
atype = str(type(a))
if atype == "<class 'list'>":
	print("Its a list!!!!")
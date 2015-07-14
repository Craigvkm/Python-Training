from math import * # Import all math functions

# Returns True if the users input(test_object)
# matches the input string name (test_object_type)
# of the requested object type.
## Available Tests:
## "str", "int", "float", "list"
### To complete:
###   Tuples
###   Dictionaries
def validate(test_object, test_object_type):
	# types = int, float, string, tuple, list

	# Work around var for lists and so on
	type_tostring = str(type(test_object))


	# Find the Objects Type
	if type(test_object) is str:
		# print("string")
		object_type = "str"
	elif type(test_object) is int:
		# print("int")
		object_type = "int"
	elif type(test_object) is float:
		# print("float")
		object_type = "float"
	#elif type(test_object) is tuple
	#	print("tuple")
	#	object_type = "tuple"
	elif type_tostring == "<class 'list'>":
		# print("list")
		object_type = "list"
	else:
		print("uncoded formatting")
		return False

	# validates type against user desire
	# Return True if they Match, false otherwise
	if test_object_type == object_type:
		return True
	else:
		return False



# Requires: validate()
# Returns list of even numbers unless True is given as second Argument
# if true is given as second arguments, returns all odd numbers.
# Returns false if no even numbers or not a list
def find_even_odd(numbers, get_odd = False):
	# Validate list in case no validation prior (returns false if not list)
	if validate(numbers, "list"):
		# Init return list
		numbers_found = []

		# Cycles through list
		# appending matches
		for number in numbers:
			if get_odd and number%2:
				numbers_found.append(number)
			elif number%2 == 0:
				numbers_found.append(number)

		# Validate at least 1 match found
		if len(numbers_found) > 0:
			return numbers_found
	
	# Fall through if no numbers in list
	# or Validate match fails
	return False

			
#test_int = 222
#test_str = "hello"
#test_float = 44.44
#test_tuple = 1, 4, 5
my_list = [1, 3, 5, 77, 100, 202, 2, 44, 5, 79]

# Requires: find_even_odd(), validate()
# input List to request even or odd return
# Returns False if nothing found or input cancelled
def request_even_odd(test_list = False):
	# Required Variables
	validate_for = ["int", "float", "list"] # acceptable inputs
	is_correct = False # stays False until test_list is validated
	value = False # gets loaded with found matches

	for check in validate_for:
		is_correct = validate(test_list, check)

		# breaks loop if validated, leaving is_correct = True
		if is_correct:
			break



	if is_correct:
		# Requests Even or Odd
		requested_function = input("Do you want even or odd? (even/odd) ")

		#takes action based on even/odd request
		if requested_function == "even":
			value = (find_even_odd(test_list))
		elif requested_function == "odd":
			value = (find_even_odd(test_list, True))
		

		# Last chance code.
		if value == False:
			redo = input("Do you want to try again? (y/n)")
			if redo == "y":
				request_even_odd(test_list)
			else:
				return "function Terminated"

		# returns even/odd list
		if value:
			return value
		# Else if nothing was found
		else:
			return "Valid input, No values found"

	else:
		# returns blank due to is_correct being false
		return


print(request_even_odd(my_list))

def tax(price = False, tip = False):
	bill = price
	tip_percentage = tip
	if price == False:
		print("No price")
		bill = input("how much was your bill? ")

	if tip == False:
		print("No percentage")
		tip_percentage = input(tip)


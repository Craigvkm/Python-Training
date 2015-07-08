#from functions import * # Imports all of my made functions
						# doesnt require functions.func() due to importing all
import math
from distance_from_x import distance_from_zero
import myFunctions

""" 
Uncomment to show
all available functions
"""
# all_functions = dir()
# print(all_functions)

number = int(input("What number do you want to check? "))
print(distance_from_zero(number))
myFunctions.validate(distance_from_zero(number))


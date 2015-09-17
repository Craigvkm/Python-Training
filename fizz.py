test = ["help", "i", "wish", 3, "fizz", "would", "show up", ".... ", "fizz fizz", "fizz"]

def fizz_count(words):
	count = 0
	for word in words:
		if word == "fizz":
			count += 1

	return count

print(fizz_count(test))
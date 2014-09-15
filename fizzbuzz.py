n = raw_input("How high do you want to go? ")
#my_input = raw_input("How high do you want to count?")
#print "Fizz buzz counting up to " + str(n)

fizzbuzz = []

i = 1

while i <= n: 
	div3 = i % 3
	div5 = i % 5
	
	if (div3 == 0) and (div5 == 0):
		value = "fizz buzz"

	elif (div3 == 0) and (div5 != 0): 
		value = "fizz"

	elif (div5 == 0) and (div3 !=0): 
		value = "buzz"
	else: 
		value = i
	fizzbuzz.append(value)
	i = i + 1

print fizzbuzz

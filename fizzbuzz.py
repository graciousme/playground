def fiz_buzz():
	for i in range(1,100):
		if (i % 3 == 0) and (i % 5 == 0):
			print "FizzBuzz"
		elif (i % 3 == 0):
			print "Fizz"
		elif (i % 5 == 0):
			print "Buzz"
		else:
			print i

#fiz_buzz()

#Create a function called sum_nums that takes in a number called num. sum_nums should add up all of the numbers from 0 until 
#(but not including) num. sum_nums should return this sum.
#   	Example: print sum_nums(3)            3
#Modify sum_nums to add up all the numbers from 0 to num, including num.
#    Example: print sum_nums(3)            6

#Write a function called sum_nums2 that checks if the parameter num is negative. If it is, sum_nums2 should add up all of the 
#numbers from 0 to the negative number and return that sum. If the parameter num is positive, sum_nums2 should work the same 
#as sum_nums from #7 part A.
#    Example: print sum_nums2(-3)        -6

def sum_nums(num):
	sum = 0
	for i in range(num + 1):
		sum = i + sum 
	return sum

# print sum_nums(5)

def sum_nums2(num):
	sum = 0
	if num < 0:
		for i in range (0, num - 1, -1):
			sum = i + sum
		return sum
	else:
		for i in range (num + 1):
			sum = i + sum
		return sum

print sum_nums2 (-10)
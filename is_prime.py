
def is_prime(num):
	prime = True
	if num == 2:
		prime = True
	else:
		for i in range (2, num):
			if (num % i == 0):
				prime = False
				break

	if prime: 
		print num, "is a prime number."
	else:
		print num, "is not a prime number."

num = int(raw_input ("Type a number to check whether it is prime. "))
is_prime(num)
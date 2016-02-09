def add_to_list(max):

	i = 0
	numbers = []

	while i < max:
		numbers.append(i)
		i = i + 5

	print "The numbers: "

	for num in numbers:
		print num

add_to_list(21)

def add_to_list_range(max):

	for i in range(1,max):
		print i

add_to_list_range(16)



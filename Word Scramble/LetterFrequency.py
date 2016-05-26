letter_frequencies = {
'a' : 816.7,
'b' : 149.2,
'c' : 278.2,
'd' : 425.3,
'e' : 1270.2,
'f' : 222.8,
'g' : 201.5,
'h' : 609.4,
'i' : 696.6,
'j' : 15.3,
'k' : 77.2,
'l' : 402.5,
'm' : 240.6,
'n' : 674.9,
'o' : 750.7,
'p' : 192.9,
'q' : 9.5,
'r' : 598.7,
's' : 632.7,
't' : 905.6,
'u' : 275.8,
'v' : 97.8,
'w' : 236.1,
'x' : 15,
'y' : 197.4,
'z' : 7.4
}

list_of_letters = []

def create_list_of_letters():
	for key, value in letter_frequencies.items():
		for index in range(int(value)):
			list_of_letters.append(key)

	with open("letter_frequency.txt", "w") as file:
		for item in list_of_letters:
			file.write("%s \n" % item)

create_list_of_letters()

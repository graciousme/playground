# returns dictionary with count of each character in a file, including punctuation and excluding spaces and line breaks
def letter_count(file_name):
	letter_count_dict = {}
	index = 0
	with open (file_name) as letter_count_file:
		letter_count_file = " ".join(letter_count_file)
		for character in letter_count_file:
			if character != "\n" and character != "\x92" and character != " ":
				letter_count_dict[str.upper(character)] = letter_count_file.count(character)
				index  += 1
	print letter_count_dict

letter_count("one_fish.txt")

# returns dictionary with count of each word in a file
# bug is that it returns count of ''
# is there a more efficient way vs. replacing every single special character?

# reads the file as a string
# replaces special characters with spaces
# then splits the string at spaces

def word_count(file_name):
	word_count_dict = {}
	index = 0

	with open (file_name) as word_count_file:
		string = word_count_file.read()
		string = string.replace("\n", " ")
		string = string.replace(".", " ")	
		string = string.replace(",", " ")
		string = string.replace("!", " ")
		string = string.replace("\x92t", "'")
		string = string.replace("  ", " ")	
		string = string.split(" ")

# iterates over every word in the string except for spaces	
		for word in string:
			if word != " ":
				word_count_dict[str.lower(word)] = string.count(word)
				index += 1
	print word_count_dict

word_count("one_fish.txt")

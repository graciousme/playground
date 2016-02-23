# Write a program that counts how many times each letter appears in a file. 
# Return a dictionary. Test your program with this file.
# Write a program that counts how many times each word appears in a file. 
# Return a dictionary. Download this file to test your program. 
# (Hints: Be careful of uppercase and lowercase instances of the same word. 
# Remove punctuation at the end of words.)

# returns dictionary with count of each character in a file, including punctuation and excluding spaces and line breaks
def letter_count(file_name):
	letter_count_dict = {}
	index = 0
	with open (file_name) as letter_count_file:
		letter_count_file = " ".join(letter_count_file)
		for character in letter_count_file:
			if character != "\n" and character != "\x92" and character != " ":
				letter_count_dict[character] = letter_count_file.count(character)
				index  += 1
	print letter_count_dict

#letter_count("one_fish.txt")

# work in progress: working on returning count of each word in a file
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
	
		# clean_file = ((" ".join(word_count_file).strip()).split(" ")
		for word in string:
			if word != " ":
				word_count_dict[str.lower(word)] = string.count(word)
				index += 1
	print word_count_dict

word_count("one_fish.txt")

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

# work in progress: working on returning count of each word in a file
def word_count(file_name):
	word_count_dict = {}
	index = 0
	with open (file_name) as word_count_file:
		for line in word_count_file:
			word_count_dict[line.split(" ")] = 1
			index += 1

		# clean_file = ((" ".join(word_count_file).strip()).split(" ")
		# for word in word_count_file:
		# 	word_count_dict[word] = word_count_file.count(word)
		# 	index += 1
	print word_count_dict


#letter_count("one_fish.txt")
word_count("one_fish.txt")

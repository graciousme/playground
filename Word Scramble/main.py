#TODO
#create validater function that calls Webster API
#create Computer class that guesses all possible words

import random
from Scrambler import *

# check to make sure entered word is made up of available letters
def check_if_valid_letters(new_word, list_of_letters):
	broken_word = []
	broken_word = list(new_word)
	word_is_valid = True
	for letter in broken_word:
		if  broken_word.count(letter) > list_of_letters.count(letter): # if a letter shows up more times in the word than it does in the scramble list... 
			word_is_valid = False
			return False
	
	if word_is_valid:
		return True
#
#
# MAIN
# get user's name
user_name = raw_input("\n\tWelcome to  W O R D  S C R A M B L E!\n\n\tPlease tell me your name: ")

# intro to computer
print "\n\t%s, descramble the letters to form words. When you're out of ideas, type DONEZO." % (user_name)

raw_input("\n\tPress enter to begin.")

# generate word scramble set
new_game = Scrambler() # instantiate Scrambler class

# create new list of random letters
new_game_list = new_game.create_list_of_letters()

# print letters 
new_game.print_letters(new_game_list)

# establish collected words list
collected_words = []

user_score = 0

# main loop
while True:

	# collect a guess if it's valid
	new_word = str.upper(raw_input("\tEnter words that can be made from this list of letters: "))

	if str.upper(new_word) == "DONEZO":
		break

	if check_if_valid_letters(new_word, new_game_list):

		collected_words.append(new_word) # keep track of all valid words
		new_word_points = len(new_word)
		user_score += new_word_points
		print "\n\t+ %i points! Total score: %i" % (new_word_points, user_score), collected_words
 
	else:

		print "\n\tWord is not valid. You can only use the letters given."

	new_game.scramble_list(new_game_list)
	new_game.print_letters(new_game_list)




# creates word scramble set
import random

class Scrambler(object):

	def __init__(self):
		self.list_of_letters = []

	# randomly chooses a letter from letter_frequency.txt
	def get_a_letter(self):
		with open ("letter_frequency.txt") as file:
			letter = random.choice(list(file))
			return letter
	
	# creates list of 7 randomly chosen letters
	def create_list_of_letters(self):
		index = 0
		for index in range(7):
			letter = str.upper(self.get_a_letter())
			letter = str.strip(letter)

			self.list_of_letters.append(letter)
			index += 1

		return self.list_of_letters

	# prints list nicely
	def print_letters(self, list):
		print "\n"
		print "\t"
		for letter in list:
			print " ", letter, " ",
		print "\n"

	# mixes up the order of the letters chosen
	def scramble_list(self, list):
		random.shuffle(list)








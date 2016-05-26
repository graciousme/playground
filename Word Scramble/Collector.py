# collects and validates words that user submits
from Scrambler import *

class Collector(object):

	def __init__(self, word): #, collected_words=[]):
		self.word = word
		self.collected_words = ""

	def collect(self):
		collected_words.append(word)
		print self.collected_words
		return self.collected_words

	def check_if_valid_letters(self):
		broken_word = []
		broken_word = list(self.word)
		print broken_word
		for letter in broken_word:
			if list_of_letters.count(letter) < broken_word.count(letter): # if a letter shows up more times in the word than it does in the scramble list... 
				print "False"
				return False # then it's not valid
			else:
				print "True"
				return True


	# def check_if_valid_word(self, word):

	# def calculate_points(self, word):




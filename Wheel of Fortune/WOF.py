import random

# returns True if user wants to play again, else returns False
def play_again():
	print ("Do you want to play again? (yes or no) ")
	return input().upper().startswith("Y")

# chooses random category from list
def get_category():
	categories = ["AROUND THE HOUSE", "BEFORE AND AFTER", "EVENTS", "FUN & GAMES", "PHRASES", "WHAT ARE YOUR DOING?"]
	category = random.choice(categories)
	print 
	print "Today's category is...", category
	return category

# chooses random board solution from category list
def get_board_solution():
	category = get_category()
	category_files = {"AROUND THE HOUSE": "sol_around_the_house.txt", 
		"BEFORE AND AFTER": "sol_before_and_after.txt", 
		"EVENTS": "sol_event.txt", 
		"FUN & GAMES": "sol_fun_and_games.txt", 
		"PHRASES": "sol_phrase.txt", 
		"WHAT ARE YOUR DOING?": "sol_what_are_you_doing.txt"}
	
	with open(category_files[category]) as file_wanted:
		lines = file_wanted.read().splitlines()
		board_solution = random.choice(lines)
	
	return board_solution

# gets user's action for this turn
def get_user_choice():
	print
	user_choice = raw_input ("\nChoose an action: \n\t1 = Guess a letter and spin the wheel \n\t2 = Buy a vowel for $250 \n\t3 = Solve the puzzle \n")
	return user_choice

# gets the space that user lands on 
def spin_wheel():
	guess = guess_letter()
	with open("wheel_spaces.txt") as file:
		lines = file.read().splitlines()
		landed_space = random.choice(lines)
		print landed_space

# gets consonant that user guesses
# TO DO: handle other non-letters, previously guessed letters
def guess_letter():
	guess = raw_input ("\nGuess a letter as the wheel spins: ")
	if len(guess) > 1:
		print "Sorry, just one letter please: "
		guess = raw_input ("\nGuess a letter as the wheel spins: ")

# gets vowel that user guesses
#def buy_vowel():

# gets solution that user guesses
#def solve():


# plays turn based on user's choice
def play_turn():
	user_choice = get_user_choice()
	
	if user_choice != "1" and user_choice != "2" and user_choice != "3":
		print "Sorry, that's not an option. Try again."
		user_choice = get_user_choice()

	if user_choice == "1":
		spin_wheel()

	if user_choice == "2":
		buy_vowel()

	if user_choice == "3":
		solve()
		

board_solution = get_board_solution()

play_turn()



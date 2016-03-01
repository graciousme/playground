import random

# TO DO: print rules, esp around points

# returns True if user wants to play again, else returns False
# TO DO: integrate this piece
# def play_again():
# 	print ("Do you want to play again? (yes or no) ")
# 	return input().upper().startswith("Y")

# gets users' names
# TO DO: handle invalid input, handle both names being the same
def get_user_names(num_users):
	users = []
	index = 1
	for number in range(num_users):
		user = str.upper(raw_input (("\nPlayer %i, please tell us your name: ") % (index)))
		
		while user in [" ", "", ".", ",", "'"]:
			user = str.upper(raw_input ("Sorry, invalid user name. Please try again: "))
		
		users.append(user)
		index += 1
	
	return users

# gets number of users playing the game, returns as num_users
# keeps asking until valid input received (only 1-3 allowed)

def get_num_users():

	num_users = raw_input ("\n How many contestants will be playing today? ")

	while num_users not in ["1", "2", "3"]:
		num_users = raw_input("\n Sorry, invalid number. Please try again: ")

	num_users = int(num_users)
	
	return num_users

# chooses random category from list and prints
def get_category(): 
	categories = ["AROUND THE HOUSE", "BEFORE AND AFTER", "EVENTS", "FUN & GAMES", "PHRASES", "WHAT ARE YOU DOING?"]
	category = random.choice(categories)
	print 
	print "\tToday's category is...", category
	return category

# chooses random board solution from category file, splits into list of characters, returns as board_solution
def get_board_solution():
	category = get_category()
	category_files = {"AROUND THE HOUSE": "sol_around_the_house.txt", 
		"BEFORE AND AFTER": "sol_before_and_after.txt", 
		"EVENTS": "sol_event.txt", 
		"FUN & GAMES": "sol_fun_and_games.txt", 
		"PHRASES": "sol_phrase.txt", 
		"WHAT ARE YOU DOING?": "sol_what_are_you_doing.txt"}
	
	with open(category_files[category]) as file_wanted:
		lines = file_wanted.read().splitlines()
		board_solution = random.choice(lines)
	
	board_solution = list(str.upper(board_solution))
	return board_solution

# gets user's action for this turn, returns as user_choice
def get_user_choice():
	user_choice = raw_input ("\n\t1 = Guess a letter and spin the wheel \n\t2 = Buy a vowel for $250 \n\t3 = Solve the puzzle \n\n\tChoose an action: ")

	if user_choice != "1" and user_choice != "2" and user_choice != "3":
		user_choice = raw_input("\n\tSorry, that's not an option. Try again: ")

	return user_choice

# gets the space that user lands on, returns as landed_space
# if lands on $1MM, give them 1 in 3 chance of getting it; otherwise Bankrupt
# TO DO: code for non-$ wedges
def spin_wheel():
	with open("wheel_spaces.txt") as file:
		lines = file.read().splitlines()
		
		landed_space = random.choice(lines)

		if landed_space == "ONE MILLION":
			rand_int = random.randint(0, 2)
			if rand_int != 1:
				landed_space = random.choice(lines)
			else:
				landed_space = "$1000000"
				print "\n\t YOU LANDED ON THE $1,000,000 SPACE, CONGRATS! "

	print "\n\tWheel has landed on:", landed_space
	return landed_space
			
# gets consonant that user chooses, returns as guess
# TO DO: handle other non-letters, previously guessed letters
def guess_letter():
	guess = str.upper(raw_input ("\n\tGuess a letter as the wheel spins: "))
	if len(guess) > 1:
		print "\n\tSorry, just one letter please: "
		guess = str.upper(raw_input ("\n\tGuess a letter as the wheel spins: "))
	
	return guess

# gets vowel that user chooses, returns as guess
# TO DO: handle invalid inputs
def buy_vowel():
	guess = str.upper(raw_input ("\n\tWhich vowel would you like to buy? "))
	if guess not in ['A', 'E', 'I', 'O', 'U']:
		guess = str.upper(raw_input ("\n\tSorry, that's an invalid entry. Please try again: "))
	
	return guess

#stores list of all user guesses in game, returns as guesses
def store_guesses(guess, guesses):
	guesses.append(guess)
	return guesses

# iterates over board_solution and prints character if it's been guessed; else prints a blank
def draw_board(guesses, board_solution):
	print "\n\tThe board looks like: \n"
	print "\t",
	for letter in board_solution:
		if letter == " " or letter == "'":
			print letter,
		if letter in guesses:
			print letter,
		else:
			print "__",

# checks if user's guess was correct, returns as is_winning boolean
def check_if_winning(guess, board_solution):
	count_of_letter = board_solution.count(guess)

	if count_of_letter > 0:
		is_winning = True
	else:
		is_winning = False

	return is_winning

# gets score for this turn only
# handles dollar amounts as integers
# TO DO: handle other wedges like Bankrupt, Lose a Turn, Prize, 1/2 Car
def get_turn_score(guess, board_solution, landed_space):	
	count_of_letter = board_solution.count(guess)
	
	if count_of_letter > 0:
		if not landed_space.startswith("$"):
			turn_score = 0

		else:
			landed_space = int(landed_space.replace("$", ""))
			turn_score = landed_space * count_of_letter
			if count_of_letter == 1:
				print "\n\tThere is %i %s on the board! You've earned %i this round." % (count_of_letter, guess, turn_score)
			else:
				print "\n\tThere are %i %ss on the board! You've earned %i in this round." % (count_of_letter, guess, turn_score)

	else:
		turn_score = 0
		print "\n\tThere are no %ss on the board, sorry! Next contestant." % (guess)

	return turn_score

# gets solution that user guesses
# TO DO: code this! 
#def solve():


# plays game while condition is True
# increments score for users
# adds to list of guesses	
def play_game():
	num_users = get_num_users()

	users = get_user_names(num_users)

	guesses = []

	board_solution = get_board_solution()
	
	# *** for testing
	#
	#
	print "\n\tanswer is:", board_solution

	draw_board(guesses, board_solution)

	scores = {}
	for user in users:
		scores[user] = 0

	user_index = 0

	while True:

		current_user = users[user_index]

	 	user_score = scores[current_user]

		print "\n\n\tCurrent score is ", scores
		user_score = scores[current_user]
		print "\n\n %s's turn" % (current_user)
		
		user_choice = get_user_choice()
		
		if user_choice == "1":
			guess = guess_letter()
			
			landed_space = spin_wheel()
			
			raw_input ("\n\tPress enter to see results. ")

			guesses = store_guesses(guess, guesses)

			turn_score = get_turn_score(guess, board_solution, landed_space)

			draw_board(guesses, board_solution)

			scores[current_user] += turn_score

			is_winning = check_if_winning(guess, board_solution)

			if is_winning == False:
				user_index += 1
				user_index %= num_users	

		if user_choice == "2":
			guess = buy_vowel()

			guesses = store_guesses(guess, guesses)

			user_score -= 250

			draw_board(guesses, board_solution)

		if user_choice == "3":
			solve()

play_game()




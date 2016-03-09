import random

# TO DO: print rules, esp around points

# gets users' names, returns in list
# USERS
def get_user_names(num_users):
	users = []
	index = 1
	for number in range(num_users):

		user = str.upper(raw_input (("\n Player %i, please tell us your name: ") % (index)))

		while users.count(user) > 0 or user in [" ", "", ".", ",", "'"]:
			user = str.upper(raw_input (" Sorry, invalid name. Please try again: "))
	
		users.append(user)
		index += 1
	
	return users

# gets number of users playing the game, returns as num_users
# keeps asking until valid input received (only 1-3 allowed)
# NUM_USERS
def get_num_users():

	num_users = raw_input ("\n How many contestants will be playing today? ")

	while num_users not in ["1", "2", "3"]:
		num_users = raw_input("\n Sorry, invalid number. Please try again: ")

	num_users = int(num_users)
	
	return num_users

# chooses random category from list and prints
# CATEGORY
def get_category(): 
	categories = ["AROUND THE HOUSE", "BEFORE AND AFTER", "EVENTS", "FUN & GAMES", "PHRASES", "WHAT ARE YOU DOING?"]
	category = random.choice(categories)
	return category

# chooses random board solution from category file, splits into list of characters, returns as board_solution
# BOARD SOLUTION
def get_board_solution(category):
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
# TO DO: fix bug, combine two while conditions somehow
# USER_CHOICE
def get_user_choice(user_score):
	user_choice = raw_input ("\n\t1 = Spin the wheel and guess a letter \n\t2 = Buy a vowel for $250 \n\t3 = Solve the puzzle \n\t4 = Give up and exit \n\n\tChoose an action: ")

	while user_choice == "2" and user_score < 250:
		user_choice = raw_input("\n\tSorry, you need at least $250 to buy a vowel. Try again: ")

	while user_choice not in ["1", "2", "3", "4"]:
		user_choice = raw_input("\n\tSorry, that's not an option. Try again: ")	

	return user_choice

# gets the space that user lands on, returns as landed_space
# TO DO: code for non-$ wedges
# LANDED_SPACE
def spin_wheel():
	with open("wheel_spaces.txt") as file:
		lines = file.read().splitlines()
		landed_space = random.choice(lines)

	return landed_space

# if lands on $1MM, give them 1 in 3 chance of getting it; otherwise Bankrupt
# TO DO: make sure bankrupt works
def check_if_bankrupt(landed_space):
	rand_int = random.randint(0, 2)
	return landed_space == "BANKRUPT" or (landed_space == "ONE_MILLION" and rand_int > 0)
			
# gets consonant that user chooses, returns as guess
# TO DO: handle other non-letters
# GUESS
def guess_letter(guesses):
	guess = str.upper(raw_input ("\n\tGuess a letter as the wheel spins: "))	

	while guesses.count(guess) > 0 or len(guess) > 1 or guess in ['A', 'E', 'I', 'O', 'U', '.', ',', "", " ", "!"]:
		guess = str.upper(raw_input ("\n\tInvalid guess, please try again: "))		
	
	return guess

# gets vowel that user chooses, returns as guess
# TO DO: handle invalid inputs, users with < $250
# GUESS
def buy_vowel():
	guess = str.upper(raw_input ("\n\tWhich vowel would you like to buy? "))
	
	while guess not in ['A', 'E', 'I', 'O', 'U']:
		guess = str.upper(raw_input ("\n\tSorry, that's an invalid entry. Please try again: "))
	
	return guess

# gets solution that user guesses, returns True if correct
def solve_puzzle(board_solution):
	puzzle_guess = str.upper(raw_input("\n\tImpressive! Please type your guess: "))
	answer = ''.join(board_solution)
	
	if puzzle_guess == answer:
		return True
	
	else:
		return False

#stores list of all user guesses in game, returns as guesses
# TO DO: handle when you guess the last letter
# TO DO: handle letters already guessed (no points)
# GUESSES
def store_guesses(guess, guesses):
	guesses.append(guess)
	return guesses

# iterates over board_solution and prints character if it's been guessed; else prints a blank
def draw_board(guesses, board_solution, category):
	print "\n\tCategory: %s\n\n" % (category) 
	print "\t",
	for letter in board_solution:
		if letter in [" ", "'", "-", "?"]:
			print letter,
		elif letter in guesses:
			print letter,
		else:
			print "__",

# gets score for this turn only
# handles dollar amounts as integers
# TURN_SCORE
def calc_score_wheel(guess, board_solution, landed_space):	
	count_of_letter = board_solution.count(guess)
	
	if count_of_letter > 0:

		landed_space = int(landed_space.replace("$", ""))
		turn_score = landed_space * count_of_letter
		
	else:
		turn_score = 0

	return turn_score

# prints message based on whether letter is in board, returns is_winning = True if letter was correct
# TO DO: message is awkward for vowels ("-250 earned")
# IS_WINNING
def check_letter(guess, board_solution, turn_score):
	count_of_letter = board_solution.count(guess)
	is_losing = True
	if count_of_letter > 0:
		is_losing = False

		if count_of_letter == 1:
			print "\n\t>>> There is %i %s on the board! You've earned $%i this round." % (count_of_letter, guess, turn_score)
			
		else:
			print "\n\t>>> There are %i %ss on the board! You've earned $%i in this round." % (count_of_letter, guess, turn_score)
		
	else:
		print "\n\t>>> There are no %ss on the board, sorry! Next contestant." % (guess)

	return is_losing

# prints all characters in board, with category
def reveal_board(category, board_solution):
	print "\n\tCategory: %s\n\n" % (category) 
	print "\t",
	
	for letter in board_solution:
		print letter,

# prints final score and thanks user for playing
def end_game(scores):

	print "\n\n\tFinal score is ", scores

	print "\n\t>>> Thanks for playing."

# returns True if user wants to play again
def prompt_again():
	
	again = str.upper(raw_input ("\n\tWant to play again? "))
	
	if again.startswith("Y"):
		return True

	else:
		return False

def print_scores(scores):
	print "\n\n\tCurrent score is ", scores

def prompt_user_to_start_turn(current_user):
	raw_input ("\n\tPress 'enter' to start turn ")
	print "\n\n > %s's turn" % (current_user)

# main game function
def play_game():
	
	print " \n\n Welcome to W H E E L  O F  F O R T U N E"

	num_users = get_num_users()

	users = get_user_names(num_users)

	scores = {}
	for user in users:
		scores[user] = 0

	category = get_category()

	board_solution = get_board_solution(category)

	guesses = []

	draw_board(guesses, board_solution, category)

	user_index = 0

	while True:
		current_user = users[user_index]
		current_user_turn_over = False
		print_scores(scores)
		prompt_user_to_start_turn(current_user)

		user_choice = get_user_choice(scores[current_user])
		if user_choice == "1":			
			guess = guess_letter(guesses)
			guesses.append(guess)
			
			landed_space = spin_wheel()

			is_bankrupt = check_if_bankrupt(landed_space)
				## pass through variabe for bankrupt situation?
				## user only wins if they also solve the puzzle

			if is_bankrupt:
				scores[current_user] = 0
				turn_score = 0
				guesses.pop() # don't store guesses for bankrupt turns

				print "\n\t>> So sorry, you've landed on BANKRUPT! Your score is %i, and it's the next contestant's turn." % (scores[current_user])			
			else:

				print "\n\t>> Wheel has landed on: %s" % (landed_space)
			
				raw_input ("\n\tPress 'enter' to see results ")

				turn_score = calc_score_wheel(guess, board_solution, landed_space)
				draw_board(guesses, board_solution, category)
				scores[current_user] += turn_score

			if turn_score <= 0:
				current_user_turn_over = True

		if user_choice == "2":
			guess = buy_vowel()
			guesses.append(guess)

			turn_score = -250
			current_user_turn_over = check_letter(guess, board_solution, turn_score)
			draw_board(guesses, board_solution, category)
			scores[current_user] += turn_score

		if user_choice == "3":
			is_solved = solve_puzzle(board_solution)

			if is_solved:
				print "\n\t>>> Nice work! You solved ths puzzle."

				reveal_board(category, board_solution)
				end_game(scores)
				break
			
			else:
				print "\n\t>>> Sorry, that's not right"
				# TO DO: take away from score
				current_user_turn_over = True

		if user_choice == "4":

			raw_input ("\n\t>> Press enter to reveal the board. ")
			reveal_board(category, board_solution)
			end_game(scores)

			break

		if current_user_turn_over:
			user_index += 1
			user_index %= num_users	
###						
###
###	ACTUAL GAME BELOW
###
###						

active_game = True

while active_game:

	play_game()

	active_game = prompt_again()





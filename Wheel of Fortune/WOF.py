import random

# TO DO: print rules, esp around points

# returns True if user wants to play again, else returns False
# TO DO: integrate this piece
# def play_again():
# 	print ("Do you want to play again? (yes or no) ")
# 	return input().upper().startswith("Y")

# gets users' names
# TO DO: handle invalid input
def get_user_names(user_num):
	users = []
	index = 1
	for number in range(user_num):
		user = str.upper(raw_input (("\nPlayer %i, please tell us your name: ") % (index)))
		if user == " " or user == "":
			user = str.upper(raw_input ("Sorry, invalid user name. Please try again: "))
		else:
			users.append(user)
		index += 1
	return users

def get_user_num():
	user_num = int(raw_input ("\nHow many contestants will be playing today? "))
	if user_num > 4 or user_num < 1:
		user_num = int(raw_input ("\nSorry, not a valid number of players. Please try again: "))
	return user_num

# chooses random category from list
def get_category():
	categories = ["AROUND THE HOUSE", "BEFORE AND AFTER", "EVENTS", "FUN & GAMES", "PHRASES", "WHAT ARE YOU DOING?"]
	category = random.choice(categories)
	print 
	print "\tToday's category is...", category
	return category

# chooses random board solution from category list
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

# gets user's action for this turn
def get_user_choice():
	user_choice = raw_input ("\n\t1 = Guess a letter and spin the wheel \n\t2 = Buy a vowel for $250 \n\t3 = Solve the puzzle \n\n\tChoose an action: ")

	if user_choice != "1" and user_choice != "2" and user_choice != "3":
		user_choice = raw_input("\n\tSorry, that's not an option. Try again: ")

	return user_choice

# gets the space that user lands on
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
			
# gets consonant that user guesses
# TO DO: handle other non-letters, previously guessed letters
def guess_letter():
	guess = str.upper(raw_input ("\n\tGuess a letter as the wheel spins: "))
	if len(guess) > 1:
		print "\n\tSorry, just one letter please: "
		guess = str.upper(raw_input ("\n\tGuess a letter as the wheel spins: "))
	
	return guess

# gets vowel that user guesses
# TO DO: handle invalid inputs
def buy_vowel():
	guess = str.upper(raw_input ("\n\tWhich vowel would you like to buy? "))
	if guess not in ['A', 'E', 'I', 'O', 'U']:
		guess = str.upper(raw_input ("\n\tSorry, that's an invalid entry. Please try again: "))
	
	return guess
	
def store_guesses(guess, guesses):
	guesses.append(guess)
	return guesses

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

def check_if_winning(guess, board_solution):
	count_of_letter = board_solution.count(guess)
	if count_of_letter > 0:
		is_winning = True
	else:
		is_winning = False

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
		print "\n\tThere are no %ss on the board - sorry! Next contestant." % (guess)

	return turn_score

# gets solution that user guesses
#def solve():


# plays game while condition is True; adds points for each user		
def play_game():
	user_num = get_user_num()

	users = get_user_names(user_num)

	board_solution = get_board_solution()
	# *** for testing
	print "\n\tanswer is:", board_solution

	guesses = []

	draw_board(guesses, board_solution)

	scores = {}
	for player in users:
		scores[player] = 0

	index = 0

	for player in users:
		user_turn = player
		is_winning = True

		while user_turn == player:
			print "\n\n\tCurrent score is ", scores
			user_score = scores[player]
			print "\n\nIt's %s's turn." % (user_turn)
			
			user_choice = get_user_choice()
			
			if user_choice == "1":
				guess = guess_letter()
				
				landed_space = spin_wheel()
				
				guesses = store_guesses(guess, guesses)

				turn_score = get_turn_score(guess, board_solution, landed_space)

				draw_board(guesses, board_solution)

				is_winning = check_if_winning(guess, board_solution)

				scores[user_turn] += turn_score

				if is_winning == False:
					index += 1

			if user_choice == "2":
				guess = buy_vowel()

				guesses = store_guesses(guess, guesses)

				user_score -= 250

				draw_board(guesses, board_solution)

			if user_choice == "3":
				solve()

play_game()




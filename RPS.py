import random

def get_user_choice():
	user_choice = str.lower(raw_input("Choose rock, paper, or scissors. "))
	print "You chose %s" % (user_choice)
	return user_choice

def get_computer_choice():
	rand_int = random.randint(0,2)
	if rand_int == 0:
		comp_choice = "rock"
	elif rand_int == 1:
		comp_choice = "paper"
	elif rand_int == 2:
		comp_choice = "scissors"
	print "Computer chose %s" % (comp_choice)
	return comp_choice

def game():
	user_score = 0
	comp_score = 0
	round_number = 0
	while round_number < 3:
		user_choice = get_user_choice()
		comp_choice = get_computer_choice()

		if comp_choice == "paper":
			if user_choice == "rock":
				print "Computer wins! "
				comp_score += 1
			elif user_choice == "paper":
				print "It's a draw! "
			elif user_choice == "scissors":
				print "You win! "
				user_score += 1
		
		elif comp_choice == "scissors":
			if user_choice == "rock":
				print "You win! "
				user_score += 1
			elif user_choice == "paper":
				print "Computer wins! "
				comp_score += 1
			elif user_choice == "scissors":
				print "It's a draw! "
		
		elif comp_choice == "rock":
			if user_choice == "rock":
				print "It's a draw! "
			elif user_choice == "paper":
				print "You win! "
				user_score += 1
			elif user_choice == "scissors":
				print "Computer wins! "
				comp_score += 1

		round_number = round_number + 1
		print
		print "After round %i, the score is User %i, Computer %i" % (round_number, user_score, comp_score)
		print

# print final score
	if user_score > comp_score:
		print
		print "Final Score: Your score is %i and the Computer's score is %i. You win!" % (user_score, comp_score)
		print
	elif comp_score > user_score:
		print
		print "Final Score: Your score is %i and the Computer's score is %i. Computer wins!" % (user_score, comp_score)
		print	
	elif comp_score == user_score:
		print
		print "Final Score: Your score is %i and the Computer's score is %i. It's a draw." % (user_score, comp_score)
		print
game()

# version where I attempt to use global variables

user_name = raw_input("What is your name? ")

print

print "Hello, %s, welcome to the bacon decision engine." % (user_name)

print 

print "We'll be helping you decide whether you should eat that bacon."

print 

# do you want to feel like angels are frolicking on your tastebuds?
def wants_angels(answer1):
	if answer1 == "NO":
		return False
	if answer1 == "YES":
		return True

# but are you afraid that bacon will kill you?
def fears_death(answer2):
	if answer2 == "NO":
		return False
	if answer2 == "YES":
		return True

# well are you a coward?
def is_coward(answer3):
	if answer == "YES":
		return True
	if answer == "NO":
		return False

answer1 = str.upper(raw_input("Do you want to feel like angels are frolicking on your taste buds? "))

if not wants_angels(answer1):
	
	print
	print "You clearly have never tasted bacon before, therefore you should eat the bacon."
	print 

answer2 = str.upper(raw_input("But are you afraid that bacon will kill you? "))

elif fears_death(answer2):

	answer3 = str.upper(raw_input("Well are you a coward? "))

	if is_coward(answer3):

		print
		print "Bacon will turn you into a true warrior."
		print

	else: 

			print
			print "Then eat it, you not-coward!"
			print

else: 

		print
		print "Good, so you can proceed to eat the bacon."
		print











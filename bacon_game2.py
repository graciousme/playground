user_name = raw_input("What is your name? ")

print

print "Hello, %s, welcome to the bacon decision engine." % (user_name)

print 

print "We'll be helping you decide whether you should eat that bacon."

print 

# do you want to feel like angels are frolicking on your tastebuds?
def wants_angels(answer):
	if (answer == "NO"):
		return False
	if (answer == "YES"):
		return True

# but are you afraid that bacon will kill you?
def fears_death(answer):
	if (answer == "NO"):
		return False
	if (answer == "YES"):
		return True

# well are you a coward?
def is_coward(answer):
	if (answer == "YES"):
		return True
	if (answer == "NO"):
		return False

if not wants_angels(str.upper(raw_input("Do you want to feel like angels are frolicking on your taste buds? "))):

	print
	print "You clearly have never tasted bacon before, therefore you should eat the bacon."
	print 

else:

	if fears_death(str.upper(raw_input("But are you afraid that bacon will kill you? "))):

		if is_coward(str.upper(raw_input("Well are you a coward? "))):

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











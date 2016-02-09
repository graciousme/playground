# version with raw inputs built in the functions

user_name = raw_input("What is your name? ")

print

print "Hello, %s, welcome to the bacon decision engine." % (user_name)

print 

print "We'll be helping you decide whether you should eat that bacon."

print 

def wants_angels():
	answer = str.upper(raw_input("Do you want to feel like angels are frolicking on your tastebuds? "))
	if (answer == "NO"):
		return False
	if (answer == "YES"):
		return True

def fears_death():
	answer = str.upper(raw_input("But are you afraid that bacon will kill you? "))
	if (answer == "NO"):
		return False
	if (answer == "YES"):
		return True

def is_coward():
	answer = str.upper(raw_input("Well are you a coward? "))
	if (answer == "YES"):
		return True
	if (answer == "NO"):
		return False

if not wants_angels():

	print
	print "You clearly have never tasted bacon before, therefore you should eat the bacon."
	print 

else:

	if fears_death():

		if is_coward():

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











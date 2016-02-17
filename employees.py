Employee = {"age":40, "name":"Dilbert", "height":62}

def check_for_key(poss_key):
	if poss_key in Employee:
		print poss_key, Employee["poss_key"]
	else: 
		print poss_key, "is not a key. "

#poss_key = str(raw_input ("What key would you like to check for? "))
#check_for_key(poss_key)


for key in Employee.keys():
	print key

print Employee.items()
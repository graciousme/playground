shopping_list = ['eggs', 'milk', 'cheese']

def go_home():
	print_menu()
	selection = raw_input ("Choose a numbered option listed above. ")
	main_menu(selection)

def print_menu():
	print
	print "Main Menu:"
	print "1 - Add an item"
	print "2 - Remove an item"
	print "3 - Replace one item with another"
	print

def main_menu(selection):
	
	if selection == "1":
		item = raw_input ("What would you like to add to your shopping list? ")
		add_item(item)
		print
		print "Your shopping list contains:", shopping_list
		print
		go_home()

	elif selection == "2":
		rm_item = raw_input ("What item would you like to remove from the shopping list? ")
		remove_item(rm_item)
		print
		print "Your shopping list contains:", shopping_list
		print
		go_home()

	elif selection == "3":
		rm_item = raw_input ("What item would you like to remove from the shopping list? ")
		item = raw_input ("What would you like to add to your shopping list? ")
		remove_item(rm_item)
		add_item(item)
		print
		print "Your shopping list contains:", shopping_list
		print
		go_home() 

	else:
		print
		print "Sorry, I don't recognize that selection. Please try again. "
		print 
		go_home()

def add_item(item):
	if shopping_list.count(item) > 0:
		confirm_duplicate = raw_input("You already have %s in your list. Are you sure you want to add it again? (Y/N) " % item)
		if str.upper(confirm_duplicate) == "N":
			print_menu()
		else:
			shopping_list.append(item)
	else:			
		shopping_list.append(item)

def remove_item(rm_item):
	if shopping_list.count(rm_item)<1:
		print
		print "You don't have", rm_item, "on your list."
		print
	elif shopping_list.count(rm_item)>1:
		confirm_rm_duplicate = raw_input ("%s appears more than once on your list. Would you like to remove them all? (Y/N) " % rm_item)
		if str.upper(confirm_rm_duplicate) == "Y":
			count = shopping_list.count(rm_item)
			for i in range (count):
				shopping_list.remove(rm_item)
		else:
			shopping_list.remove(rm_item)
	else:
		shopping_list.remove(rm_item)

print
print "Your shopping list contains:", shopping_list
go_home()



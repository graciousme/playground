def draw_square(side_length):
	height = 0
	while height < side_length:
		for i in range(side_length):
			print "* ",
		height += 1
		print "\n"

side_length = int(raw_input("Type the length/width of the square I should draw. "))
draw_square(side_length)

def draw_checkerboard(checker_side_length):
	height = 0 
	
	while height < checker_side_length:
		if (height % 2) == 0:
			for i in range(checker_side_length):
				if (i % 2) == 0:
					print "o ",
				if (i % 2) > 0:
					print "x ",
			height += 1
			print "\n"
		
		elif (height % 2) > 0:
			for i in range(checker_side_length):
				if (i % 2) == 0:
					print "x ",
				if (i % 2) > 0:
					print "o ",
			height += 1
			print "\n"

checker_side_length = int(raw_input("Type the length/width of the checkerboard I should draw. "))
draw_checkerboard(checker_side_length)


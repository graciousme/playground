# calculates seconds from other units
def convert_to_seconds (hours, minutes, seconds):
	conv_hours = hours * 3600
	conv_minutes = minutes * 60
	converted = conv_hours + conv_minutes + seconds
	print "This time converts to %i seconds. " % converted

# breaks up user input into digestible pieces for converting
time_string = raw_input ("Enter the time to convert in format hh:mm:ss. ")
hours = int(time_string.split(":")[0])
minutes = int(time_string.split(":")[1])
seconds = int(time_string.split(":")[2])

convert_to_seconds (hours, minutes, seconds)

# calculates number of inches from feet
def convert_to_inches (feet, inches):
	conv_feet = feet * 12
	converted = conv_feet + inches
	print "This length converts to %i inches. " % converted

# breaks up user input into digestible pieces for converting
length_string = raw_input ("Enter the length that you wish to convert to inches, for example '5,2' for 5 feet and 2 inches. ")
feet = int(length_string.split(",")[0])
inches = int(length_string.split(",")[1])

convert_to_inches (feet, inches)
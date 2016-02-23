from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
#apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?title=180"

def search_title():
	title = raw_input ("What title would you like to search? ")
	title = title.replace(" ", "-")
	apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?title="+title
	print apiUrl
	response = urlopen(apiUrl)
	json_obj = load(response)
	print json_obj	

#open the apiUrl and assign data to variable
# response = urlopen(apiUrl)

# json_obj = load(response)

# print json_obj

search_title()

#ideas
# how does kanye feel today?
# where should we eat right now? yelp api
# visualization: CEO twitter sentiment analysis * stock price
# codenames player / taboo player
# translation check
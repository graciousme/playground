from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
#apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?title=180"

def search_year():
	apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"
	release_year_wanted = raw_input ("What release year would you like to search? ")
	release_year = "release_year=" + release_year_wanted
	apiUrl += release_year
	print apiUrl

	response = urlopen(apiUrl)
	json_obj = load(response)
	
	film_list = []
	for film in json_obj:
		if film["title"] not in film_list:
			film_list.append(film["title"])

	print film_list

#open the apiUrl and assign data to variable
# response = urlopen(apiUrl)

# json_obj = load(response)

# print json_obj

search_year()

#ideas
# how does kanye feel today?
# where should we eat right now? yelp api
# visualization: CEO twitter sentiment analysis * stock price
# codenames player / taboo player
# translation check
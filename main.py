# ==================================
#      Python Quote Scraper
#
# Team: [Your Team Name]
# Members: [List of team member names]
# ==================================


single_quote = {
  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
  'author': 'Albert Einstein',
}

multi_quote = [
  
	{
	  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
	  'author': 'Albert Einstein',
	},
	{
		'text': 'fail. fail. fail. Wow, I just learned 3 new ways on how not to do something!',
		'author': 'Amaurys Valdez',
	},
	{
		'text': 'I Am Groot',
		'author': 'Groot',
	},
]


# SECTION 1: IMPORTS
# All team members: Add the libraries you need for your function here.
# import requests
# import json
# import random
# from bs4 import BeautifulSoup


# ==================================
# SECTION 2: FUNCTION DEFINITIONS
# ==================================

# --- Function for Student A ---
# TODO: Put your scrape_all_quotes function here.
# This function should scrape all quotes from the website.
# It should return a list of quote dictionaries.


# --- Function for Student B ---
# TODO: Put your save_quotes_to_disk function here.
# This function should take the list of quotes and a filename.
# It should save the quotes to a JSON or CSV file.

from bs4 import BeautifulSoup
import requests 

url = 'https://quotes.toscrape.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

quotes = []

while True:
    # Find all quote blocks on the page
    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').get_text(strip=True)
        author = quote.select_one('small.author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.select('div.tags a.tag')]
        quotes.append({'text': text, 'author': author, 'tags': tags})
    
    # Find the link to the next page, if available
    next_btn = soup.select_one('li.next a')
    if next_btn:
        next_url = url + next_btn['href']
        page = requests.get(next_url)
        soup = BeautifulSoup(page.text, 'html.parser')
    else:
        break




import json

person_JSON = {'text': text, 'author': author, 'tags': tags}
person_JSON = json.dumps(author)

with open('person.json', 'w') as json_file:
	json_file.write(person_JSON)
	print('Saved succesfully!')


#import json
#date_str = input("Please put in the date:")

#def save_quotes_to_disk(quotes, date_str):
    #filename = f"save_quotes_to_disk{date_str}.json"
    #with open(filename, "w", encoding="utf-8") as f:
        #json.dump(quotes, f, indent=4, ensure_ascii=False)
    #print(f"Quotes saved to {filename}")








#from bs4 import JSON

#import request 

#url = https://qprintuotes.toscrape.com/

#file_name = input("Please put in the date:")

#def save_quotes_to_disk_json(list , file_name):
	#with open('save_quotes_to_disk_json', file_name) as f:
		#json.dump(save_quotes_to_disk_json, f)
#save_quotes_to_disk_json(list , file_name)





















# --- Function for Student C ---
# TODO: Put your load_quotes_from_disk function here.
# This function should take a filename.
# If the file exists, it returns the list of quotes from the file.
# If the file does not exist, it returns an empty list [].


# --- Function for Student D ---
# TODO: Put your get_quotes_by_tag function here.
# This function should take the list of quotes.
# It asks the user for a tag and prints any matching quotes.


# --- Function for Student E ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.












# ==================================
# SECTION 3: MAIN PROGRAM
# ==================================


# Team Lead/Integrator: Write the main logic here that calls the functions.


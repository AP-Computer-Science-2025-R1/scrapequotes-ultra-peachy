# ==================================
#      Python Quote Scraper
#
# Team: [Ultra Peachy]
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

import requests
import json
import random
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import date

# Function for Adam and Matthew ---
# TODO: Put your group_introductions() function here.
# This function should introduce the student and function they work on.
 
def group_introductions():
	UNDERLINE = '\033[4m'
	END = '\033[0m'  	
	print("This project aims to create a command line application to scrape quotations from websites and display them in the terminal. \nIt is all about web scraping learning, improving Python programming skills, and team working.")
	print("This project was created by: Adam, TD, Arham, Stephanie, Eduardo, Anthony, and Matthew")
	print("-----------------------------")
	print(UNDERLINE + "Functions Worked On" + END)
	print("TD: Captain")
	print(UNDERLINE + "Adam and Matthew:" + END + " group_introductions --> They are displaying a text that introduces all group members, what they worked on, and the purpose of this project")
	print(UNDERLINE + "Arham:" + END + " scrape_all_quotes --> He is scraping all quotes from every page of the website.")
	print(UNDERLINE + "Stephanie:" + END + " get_random_quote(quotes_list) --> She is displaying a random quote to the user using the website")
	print(UNDERLINE + "Anthony:" + END + " save_quotes_to_disk(quotes_list, date_str) --> He is saving the scrape to the local file.")
	print(UNDERLINE + "Eduardo:" + END + " load_quotes_from_disk(filename) --> He is loading all the quotes from the previously saved file which helps avoid the need to scrape again.")

# --- Function for Arham ---
# TODO: Put your scrape_all_quotes function here.
# This function should scrape all quotes from the website.
# It should return a list of quote dictionaries.

def scrape_all_quotes(base_url='https://quotes.toscrape.com'):
	page = requests.get(base_url)
	soup = BeautifulSoup(page.text, 'html.parser')
	quotes = []

	while True:
		for quote in soup.select('div.quote'):
			text = quote.select_one('span.text').get_text(strip=True)
			author = quote.select_one('small.author').get_text(strip=True)
			tags = [tag.get_text(strip=True) for tag in quote.select('div.tags a.tag')]
			quotes.append({
				'text': text,
				'author': author,
				'tags': tags
			})

		next_btn = soup.select_one('li.next a')
		if next_btn:
			next_url = base_url.rstrip('/') + next_btn['href']
			page = requests.get(next_url)
			soup = BeautifulSoup(page.text, 'html.parser')
		else:
			break

	return quotes

# --- Function for Anthony ---
# TODO: Put your save_quotes_to_disk function here.
# This function should take the list of quotes and a filename.
# It should save the quotes to a JSON or CSV file.

def save_quotes_to_disk(quotes_list):
	with open(str(date.today())+'.json', 'w') as json_file:
		json.dump(quotes_list, json_file, indent=2)
		print('Saved succesfully!')

# --- Function for Eduardo ---
# TODO: Put your load_quotes_from_disk function here.
# This function should take a filename.
# If the file exists, it returns the list of quotes from the file.
# If the file does not exist, it returns an empty list [].


def load_quotes_from_disk(filename):
	try:
		with open(filename, 'r') as qtf:
			jsdat = json.load(qtf)
		return jsdat
	except FileNotFoundError:
		print(f"Error: File '{filename}' not found.")
		return None


# --- Function for Stephanie ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.


def get_random_quote(quotes):
	if not quotes:
		print("No quotes available.")
		return None
	else:
		random_quote = random.choice(quotes)
		print(random_quote)
		return random_quote['text']
group_introductions()
if load_quotes_from_disk(str(date.today())+'.json') is None:
	print("No quotes available. Scraping new quotes...")
	scrape_all_quotes()
	save_quotes_to_disk(scrape_all_quotes())
	quote = get_random_quote(load_quotes_from_disk(str(date.today())+'.json'))
	print("The Random Quote is: ", quote)
else:
	quote = get_random_quote(load_quotes_from_disk(str(date.today())+'.json'))
	print("The Random Quote is: ", quote)

# Team Lead/Integrator: Write the main logic here that calls the functions.
#if __name__ == "__main__":

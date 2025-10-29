from bs4 import BeautifulSoup
import requests 
def scrape_all_quotes():
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

for q in quotes:
    print(q)
 











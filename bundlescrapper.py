import requests
from bs4 import BeautifulSoup

print('Start to scrape')

url = 'https://www.humblebundle.com/books/start-a-startup-books'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)
#print(soup.p)
#print(soup.findAll('.dd-header-headline'))
#print(soup.findAll('h2'))
#testy = soup.findAll('h2')
#print(testy[0])

tier_headlines = soup.select('.dd-header-headline')
print(tier_headlines[0].text.strip())

for tier in tier_headlines:
    print(tier.text.strip())






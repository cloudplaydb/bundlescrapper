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

# Bundle tiers
tier_headlines = soup.select('.dd-header-headline')
print(tier_headlines[0].text.strip())

for tier in tier_headlines:
    print(tier.text.strip())

# Design datastructure - List ?? dictionary ??

tiers = {
    "tier1" :{
        "price" : 500,
        "products" : [
            "name1",
            "name2"
        ]
    },
    "tier2" : {
        "price" : 500,
        "products" : [
            "name1",
            "name2"
        ]
    }
}

print(tiers)

# list of tiers
#print(tiers.keys())
#dict_keys(['tier1'])

#python list comprehensions
print([key.upper() for key in tiers.keys()])

stripped_tiernames = [tier.text.strip() for tier in tier_headlines]
print(stripped_tiernames)




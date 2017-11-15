import requests
from bs4 import BeautifulSoup

url = 'https://www.humblebundle.com/books/start-a-startup-books'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
tier_dict = {}

#Product names
product_names = soup.select(".dd-image-box-caption")
stripped_product_names = [prodname.text.strip() for prodname in product_names]

# Bundle tiers
tiers = soup.select(".dd-game-row")

# Looping through each tier
for tier in tiers:
    # Only for sections that have a headline
    if tier.select(".dd-header-headline"):
        # Grab tiername and price
        tiername = tier.select(".dd-header-headline")[0].text.strip()

        # Grab tier product names
        product_names = tier.select(".dd-image-box-caption")
        product_names = [prodname.text.strip() for prodname in product_names]

        # Add one product tier to our data structure
        tier_dict[tiername] = {"products" : product_names}

# After we build our datastructure ...
for tiername, tierinfo in tier_dict.items():
    print(tiername)
    print("#######################################")
    print("products: ")
    print("\n".join(tierinfo['products']))
    print("\n\n")





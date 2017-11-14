#! /usr/bin/env python3

# webscrapper - https://www.youtube.com/watch?v=7SWVXPYZLJM
# scrap dest - https://www.humblebundle.com/books/sex-science-comics

import sys
import requests
from bs4 import BeautifulSoup

print('Start to scrape')

# setup virtual env
# https://www.youtube.com/watch?v=N5vscPTWKOk

url = 'https://www.humblebundle.com/books/sex-science-comics'

# make an http request to the url and inspect the result of that
# http://docs.python-requests.org/en/master/
# use get HTTP request to get the resource
# add requests to requirements.txt file
# pip install -r requirements.txt

resp = requests.get(url)
print(resp)

# Parsing HTML with BS4 aka Beautiful Soup
# add bs4 to requirements.txt file
# pip install -r requirements.txt
# bs4 doc - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# changed virtualenv in File >> Settings >> Project >> Project Interpreter

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)
#print(soup.p)

# Bundle tiers
# dd-header-headline
#print(soup.findAll('.dd-header-headline'))
#print(soup.findAll('h2'))

#testy = soup.findAll('h2')
#print(testy[0])

testy = soup.select('.dd-header-headline')
print(testy[0].text.strip())






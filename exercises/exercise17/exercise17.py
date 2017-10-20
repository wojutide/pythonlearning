#!/usr/bin/python3.5

import sys
import requests
from bs4 import BeautifulSoup as bs

'''exercise 1
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''

url='https://www.nytimes.com/'

r=requests.get(url)
r_html=r.text

soup=bs(r_html,"html.parser")
#title=soup.find_all('p',"title")
title=soup.find_all(class_='story-heading')
#title=soup.find_all('a','href')

i=1
for dat in title:
    if dat.a:
        print(dat.a.text.replace("\n", " ").strip())
    else:
        print(dat.contents[0].strip())
    old=sys.stdout
    with open('%d.dat' % i,  'w') as f:
        sys.stdout = f
        print(dat) 
        sys.stdout =old
        i+=1

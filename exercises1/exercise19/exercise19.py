#!/usr/bin/python3.5

import sys,re
import requests
from bs4 import BeautifulSoup as bs


'''exercise 1
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
'''

url='https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r_html=requests.get(url).text

soup=bs(r_html,'html.parser')

i=1
for dat in soup.find_all(['p','section'], class_='content-section', attrs={"data-reactid": re.compile(r'\d+')}):
#for dat in soup.find_all(['p','section'], attrs={"data-reactid": re.compile(r'\d+')}):
    print(dat.text.strip())
    old=sys.stdout
    with open('%d.dat' % i,  'w') as f:
        sys.stdout = f
        print(dat.text) 
        sys.stdout =old
    i+=1

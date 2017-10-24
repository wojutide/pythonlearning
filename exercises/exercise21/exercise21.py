#!/usr/bin/python3.5

import sys
import requests
from bs4 import BeautifulSoup as bs 

'''exercise 1
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

    Ask the user to specify the name of the output file that will be saved.
'''

def fopen(url):
    try:
        r=requests.get(url)
        r_html=r.text
        print('Encoding mathod: %s' % r.encoding)
    except:
        print("The url you input is unavaliable!")
        sys.exit()
    return r_html


def fcat(r_html):  # return a dict
    d={}
    soup=bs(r_html,'html.parser')
    title=soup.find_all('title')[0].string
    d['title']=soup.find_all('title')[0].string
    d['Num_of_hyperlink']=len(list(soup.find_all(href=True)))
    return d

def fwrite(d, filename):   # d is a dict
    with open(filename,'w') as f:
        for key in d.keys():
            f.write("The %s of the file is: %s \n" % (key, d[key]))

if __name__=="__main__":
    url=input('please input the url of webset: ')
    filename=input('please input the filename you want to save: ')
    furl=fopen(url)
    data=fcat(furl)
    fwrite(data,filename)


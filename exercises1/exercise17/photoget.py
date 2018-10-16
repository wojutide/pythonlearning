#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import imghdr
import requests
import re
from bs4 import BeautifulSoup as bs
'''
To get the photos of a website.
'''

def getphoto(urlfig,figname):
    param  = {'ie':'utf-8', 'q':'query'}
    fig=requests.get(urlfig,params=param,allow_redirects = False)
    with open(figname,'wb') as f:
        f.write(fig.content)

def getext(urlfig):
    figformat='bmp,jpg,png,tiff,gif,eps,ai,raw'
    FF=re.split(r',',figformat)
    key_url=re.split(r'\.',urlfig)
    for ext in FF:
        if ext in key_url:
            return ext
    return 'jpg'

def pagefig(url,page):
    r_html=requests.get(url).content
    soup=bs(r_html, 'html.parser')
    i=1
    for val in soup.find_all('img',src=True):
        if val != None:
            for figurl in re.split(r'\"',str(val)):
                if re.match('http',figurl):
                    print('Getting the %dth figure from %s.' % (i,figurl))
                    ext=getext(figurl)
                    getphoto(figurl,'page'+page+'_fig'+str(i)+'.'+ext)
                    i+=1
    if i==1:
        print('No target was found')


def webfig(url):
    r_html=requests.get(url).content
    soup=bs(r_html, 'html.parser')
    i=2
    pagefig(url,str(1))   # the first page
    for val in soup.find_all('a',href=re.compile(".*\d$")):
        if val != None:
            for pageurl in re.split(r'\"',str(val)):
                if re.match('http',pageurl):
                    print('Getting the %dth page from %s.' % (i,pageurl)) 
                    pagefig(pageurl,str(i)) 
                    i+=1


if __name__=='__main__':
    work=input('what kind of target do you want to obtain(f:fig,c:cartoon)? ')
    if work=='f': 
        url=input('Please input the website:\n') 
        webfig(url)
    elif work=='c':
        url=input('Please input the website:\n') 
        webcartoon(url)

#!/usr/bin/env python
# coding: utf-8

# In[118]:


import requests,webbrowser

from bs4 import BeautifulSoup

a = requests.get('https://www.mysmartprice.com/mobile/apple-iphone-xir-msp15688')
        
parse = BeautifulSoup(a.content,'html.parser')

get_price = parse.find('span',class_="prdct-dtl__prc-val").text

cur_price = ''.join([i for i in get_price if i.isdigit()])

running = True

while running:
    
    a1 = requests.get('https://www.mysmartprice.com/mobile/apple-iphone-xir-msp15688')
    
    parse1 = BeautifulSoup(a1.content,'html.parser')
    
    print('Getting the price of Iphone 11')
    
    get_price1 = parse1.find('span',class_="prdct-dtl__prc-val").text
    
    cur_price1 = ''.join([i for i in get_price1 if i.isdigit()])
    
    print('Checking if lesser than current price')
    
    if int(cur_price1)<int(cur_price):
        
        print('There seems to be a drop in price.')
        
        webbrowser.open('https://www.mysmartprice.com/mobile/apple-iphone-xir-msp15688')
        
        running = False
        
    else:
        print('Price hasnt changed.')
        
        running = False
    
    
    


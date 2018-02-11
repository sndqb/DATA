# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:55:33 2017

@author: asd
"""

import requests     
r = requests.get('https://book.douban.com/subject/1084336/comments/').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)

import pandas
comments = []
for item in pattern:
    comments.append(item.string)    
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
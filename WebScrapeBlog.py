# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 01:14:27 2018
Web scraping from the blog to get truth values to the different topics
@author: nEW u
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import bs4
import re

rawFile = open('blog.html','r',encoding='utf-8') 
soup = bs4.BeautifulSoup(rawFile, "lxml")

# Getting the essay categories
categories = soup.select('strong')
categories = [category.getText() for category in categories]
categories = categories[4:25]

#Getting the essay topics
post = soup.select('.post-entry')
post = post[0].getText()

post = post.split('\n')

post = [p for p in post if len(p) is not 0]
post = post[4:164]

# category: topics
dic = {}
#nsoup = bs4.BeautifulSoup("<div><p>Fuck</p></div>", "html-parser")
#cat = nsoup.select('p')
#print(post)

index = 0
count_cat={}
#count_cat['Topic']=categories
for line in post:
    
    try:
        if line == categories[index] :
            current = index
            index = index + 1
            continue
        cat_array = []
        for i in range(len(categories)):
            if i is current:
                cat_array.append(1)
            else:
                cat_array.append(0)
        
    except:
        #print('here')
        cat_array = []
        for i in range(len(categories)-1):
            cat_array.append(0)
        cat_array.append(1)
        count_cat[line]=cat_array
        continue
    count_cat[line]=cat_array
    
#categories.insert(0,'Topic')    
df = pd.DataFrame.from_dict(count_cat,orient='index',columns=categories)
#(count_cat,)
#df = df.transpose()
df.to_csv('blog_preprocessed.csv')

rawFile.close()

    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:00:20 2018

@author: nEW u
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
dataset1 = pd.read_csv('preprocessed.csv')
categories1=list(dataset1)[2:]

dataset2 = pd.read_csv('blog_preprocessed.csv')
dataset2.rename( columns={'Unnamed: 0':'Topics'}, inplace=True )
categories2=list(dataset2)[1:]


category_mapping={}
#Education
new_categories = [categories2[17],categories2[4]]
category_mapping[categories1[0]]=new_categories

#Technology and Society
new_categories = [categories2[0],categories2[2],categories2[8],
                  categories2[12],categories2[18],categories2[19]]
category_mapping[categories1[1]]=new_categories

#Cities
new_categories = [categories2[2],categories2[3]]
category_mapping[categories1[2]]=new_categories

#Arts
new_categories = [categories2[11],categories2[9]]
category_mapping[categories1[3]]=new_categories

#Goverenmnt and Power       
new_categories = [categories2[3],categories2[5],categories2[7],
                  categories2[15],categories2[18],categories2[19]]
category_mapping[categories1[4]]=new_categories

#Intellectual Endeavors
new_categories = [categories2[13],categories2[14],categories2[20],
                  categories2[15],categories2[16],categories2[6]]
category_mapping[categories1[5]]=new_categories
#Philosophical
new_categories = [categories2[9],categories2[10],categories2[11],
                  categories2[12],categories2[1]]
category_mapping[categories1[6]]=new_categories

topics2=dataset2['Topics'].tolist()
topics1=dataset1['Topics'].tolist()

common = set(topics2).intersection(topics1)
#v=dataset2.loc[dataset2['Topics'] == list(common)[23]]
categories = ['Topic']
for t in categories1:
    categories.append(t)
df=pd.DataFrame(columns=categories)
for topic in common:
    #the_row = dataset2.loc[dataset2['Topics'] == topic]
    temp_row=[topic,0,0,0,0,0,0,0]
    for key in list(category_mapping):      
        the_state = 0
        index = 1
        for cat in category_mapping[key]:
            the_state = list(dataset2.loc[dataset2['Topics'] == topic][cat])[0]
            temp_row[index]=temp_row[index] or the_state
            #print(temp_row[index])
            index=index+1
        
            
    #if key == 'Philosophical':        
        #print(temp_row)
    df = df.append([pd.DataFrame([temp_row],columns=categories)],ignore_index=True)
        


uncommon = list(set(topics1)^set(topics2))


df1 = pd.DataFrame(columns=categories)

df1 = pd.concat([pd.DataFrame([[topic,0,0,0,0,0,0,0]],columns=categories) for topic in uncommon],ignore_index=True)

# df = pd.concat([df,df1],ignore_index=True)

df.to_csv('training_set.csv', sep=',',columns=categories)
df1.to_csv('test_set.csv', sep=',',columns=categories)






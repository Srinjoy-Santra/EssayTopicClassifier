# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 01:43:31 2018
@author: Srinjoy Santra
The IssueEssayTopics file was downloaded using requests from
https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool

Demo:
https://greessays.wordpress.com/2012/07/12/consolidated-pool-of-issue-topics/

Resource:
https://cloud.google.com/blog/products/gcp/problem-solving-with-ml-automatic-document-classification

"""
# Importing the libraries
import bs4
import pandas as pd

rawFile = open('IssueEssayTopics.txt')
soup = bs4.BeautifulSoup(rawFile.read(), "html.parser")

paras = soup.select('p')
# Glancing through the file it was found that topics begin from index 4
topics = []
x = 4
while x < len(paras):

    content = paras[x].getText().replace('"','')

    check = content.split(' ', 1)[0]
    if check == 'Register':
        break
    print(content)
    if check == "Claim:":
        topics.append(content+paras[x+1].getText().replace('"',''))
        #print()
        x = x+3
    else:
        x = x+2
        topics.append(content)

print(topics)

categories = ['Topics','Education', 'Technology & Society', 'Cities', 'Arts', 'Government & Power',
              'Intellectual Endeavors', 'Philosophical']

df = pd.DataFrame(columns=categories)
df = pd.concat([pd.DataFrame([[topic,0,0,0,0,0,0,0]],columns=categories) for topic in topics],ignore_index=True)
print(df)

df.to_csv('preprocessed.csv', sep=',',columns=categories)

rawFile.close()

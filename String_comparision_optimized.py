# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:20:30 2019

@author: Baalaaji VR
"""

import pandas as pd
from fuzzywuzzy import fuzz
import os
#!pip install fuzzywuzzy
os.chdir("C:/Users/Baalaaji VR/Desktop/Comprehensive_school_database/string_matching_school_connects")

school=pd.read_excel('School_Database_master_2.xlsx',encoding='utf-8')
day=pd.read_excel('Final_fees.xlsx',encoding='utf-8')


def ratio(s1,s2):
    return(fuzz.ratio(s1,s2))


pooled = []
a=school["City"].str.lower()
b=day.City.str.lower()
if school["City"].str.lower().sort_index(inplace=True)==day.City.str.lower().sort_index(inplace=True):
    for i in range(len(school)):
        # n=[]
        match_df=day[day.first_char==school['first_char'][i]][["name-c"]]
        pooled.append([[school["name-c"][i], column, ratio(school["name-c"][i], column)] for column in match_df["name-c"] if ratio(school["name-c"][i], column)> 80 ])
    

flattened=[j for i in pooled for j in i ]
flattened



l1=[]
l2=[]
l3=[]
for items in flattened:
    l1.append(items[0])
    l2.append(items[1])
    l3.append(items[2])
    
l1,l2,l3

final=pd.DataFrame(list(zip(l1,l2,l3)),columns=["school_name","s_connects_name","match_percentage"])

final.to_excel('similar_schools_connects.xlsx')

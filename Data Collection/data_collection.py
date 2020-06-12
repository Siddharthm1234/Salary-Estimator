# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:41:43 2020
@author: siddh
"""
import glassdoor_scraper as gs
import pandas as pd
path='C:/Users/siddh/ML/Project/chromedriver'
df= gs.get_jobs('data scientist', 0,False, path)

'''We obtain 1000 entries from glassdoor with jobs in different companies as datascientist'''

df.to_csv('glassdoor_jobs.csv')
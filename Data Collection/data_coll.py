# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:41:43 2020

@author: siddh
"""
import glassdoor_scraper as gs
import pandas as pd
path='C:/Users/siddh/ML/Project/chromedriver'
df= gs.get_jobs('data scientist', 5,False, path)
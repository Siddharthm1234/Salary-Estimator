# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:41:43 2020
Obtained code from: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiihLT9m_3pAhXKdCsKHYOYCdMQFjAAegQIARAB&url=https%3A%2F%2Ftowardsdatascience.com%2Fselenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905&usg=AOvVaw3JAqE40EY1hbNp8wdaMadi
@author: siddh
"""
import glassdoor_scraper as gs
import pandas as pd
path='C:/Users/siddh/ML/Project/chromedriver'
df= gs.get_jobs('data scientist', 0,False, path)


df=pd.read_csv('glassdoor_jobs.csv')
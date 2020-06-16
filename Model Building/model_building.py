# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:53:15 2020

@author: siddh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('salary_data_cleaned.csv')

#Choose relevant columns
df.columns

df_model=df[['Rating', 'Size', 'Type of ownership','Industry', 'Sector', 'Revenue','State', 'same state', 'age',
       'python_reqd', 'spark_reqd', 'aws_reqd', 'excel_reqd', 'job_simp', 'avg','seniority', 'desc_len']]
#Get Dummy Data
df_dum = pd.get_dummies(df_model)

#Train Test Split
from sklearn.model_selection import train_test_split
X=df_dum.drop('avg', axis=1)
y=df_dum['avg'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Multiple linear regression (Linear model)
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
print(cross_val_score(lr, X, y, cv=3, scoring='neg_mean_absolute_error '))

#Lasso regression (Linear model)

#Random Forest (tree-based)

#Tune modelGridSearchCV

#test
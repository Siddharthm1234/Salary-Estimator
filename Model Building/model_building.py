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
lm=LinearRegression()
lm.fit(X, y)
print(cross_val_score(lm, X_train, y_train, cv=3, scoring='neg_mean_absolute_error').mean())


#Random Forest (tree-based)
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()
rf.fit(X_train, y_train)

print(cross_val_score(rf, X_train, y_train, cv=3, scoring='neg_mean_absolute_error').mean())

#Tune using modelGridSearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10, 300, 10), 'criterion':("mse", "mae"), 'max_features':('auto', 'sqrt', 'log2')}
gs=GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error', cv=3)
gs.fit(X_train, y_train)

gs.best_score_
gs.best_estimator_


#testing the oredicted and actual values for different model
tpred_lm=lm.predict(X_test)
tpred_rf=rf.predict(X_test)
tpred_best_rf=gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
print(f'MEA for Linear Regression Model is: {mean_absolute_error(y_test, tpred_lm)}')
print(f'MEA for a Random Forest is: {mean_absolute_error(y_test, tpred_rf)}')
print(f'MAE for Random Forest with Model Tuning is: {mean_absolute_error(y_test, tpred_best_rf)}')
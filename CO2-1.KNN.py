#!/usr/bin/env python
# coding: utf-8

# In[1]:
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
data=load_iris()
x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2)
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
print(y_pred)
knn.predict_proba(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

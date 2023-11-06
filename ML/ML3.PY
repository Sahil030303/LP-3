#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# In[3]:


from sklearn.neural_network import MLPClassifier
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.metrics import accuracy_score, classification_report


# In[5]:


df = pd.read_csv("D:/Training datasets/Churn_Modelling.csv")
df


# In[6]:


df.columns


# In[7]:


df['Geography'].nunique()


# In[11]:


df = pd.concat([df,pd.get_dummies(df['Gender'])],axis = 1)
df


# In[7]:


df.drop(columns = ['RowNumber','CustomerId'])


# In[14]:


#df = df.drop(columns = ['Gender'])
df


# In[14]:


def num(column):
    for i in range(len(column)):
        if column[i]==True:
            column[i]=1
        else:
            column[i]=0

num(df['Geo_France'])
num(df['Geo_Germany'])
num(df['Geo_Spain'])
num(df['Female'])
num(df['Male'])


# In[15]:


df


# In[16]:


df.columns


# In[17]:


x = df[['CreditScore','Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary','Geo_France','Geo_Germany', 'Geo_Spain', 'Female', 'Male']]


# In[18]:


y = df['Exited']


# In[19]:


sns.countplot(x=y)


# In[20]:


sc = StandardScaler()


# In[21]:


sc_x = sc.fit_transform(x)


# In[22]:


x_train, x_test, y_train, y_test = train_test_split(sc_x, y, test_size=0.2)


# In[23]:


mlp = MLPClassifier()


# In[24]:


mlp.fit(x_train, y_train)


# In[25]:


predict = mlp.predict(x_test)


# In[26]:


print(accuracy_score(predict,y_test))


# In[27]:


ConfusionMatrixDisplay.from_predictions(predict,y_test)


# In[28]:


cm = confusion_matrix(predict,y_test)
cm


# In[29]:


TP = cm[0,[0]]
TN = cm[1,[1]]
FP = cm[0,[1]]
FN = cm[1,[0]]


# In[30]:


TP


# In[31]:


acc = (TP+TN)/(TP+TN+FP+FN)
acc


# In[32]:


cr = classification_report(predict,y_test)
cr


# In[16]:


import requests
print(requests.get("https://raw.githubusercontent.com/Sahil030303/LP-3/main/ML/ML5.py").text)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Import Data-Set

# In[3]:


da=pd.read_csv(r"C:\Users\User\Downloads\adultmanisha.csv")


# # a.)Display Top 10 Rows of The Dataset 
# 

# In[4]:


da.head(10)


# # b.) Check Last 10 Rows of The Dataset

# In[5]:


da.tail(10)


# # Find Shape,Size,Rows,Columns,Info about DataSet

# In[8]:


print(da.shape)
print(da.shape[0])
print(da.shape[1])
print(da.size)
print("\n")
print(da.info())


# # Fetch Random Sample From the Dataset (50%)

# In[9]:


da.sample(frac=0.50)


# # Check Null Values In The Dataset

# In[10]:


da.isna()


# In[11]:


sns.heatmap(da.isnull())


# It shows There is no null values there are ? instead of null values

# # Perform Data Cleaning [ Replace '?' with NaN ]

# In[12]:


da.isin(["?"]).sum()


# In[13]:


da["workclass"]=da["workclass"].replace("?",np.nan)
da["occupation"]=da["occupation"].replace("?",np.nan)
da["native-country"]=da["native-country"].replace("?",np.nan)


# In[14]:


da.isin(["?"]).sum()


# In[16]:


da.isin([np.nan]).sum()


# In[18]:


sns.heatmap(da.isnull())


# # Drop missing values

# In[19]:


da.dropna(how="any",inplace=True)


# In[20]:


da.shape


# Shape is decreased

# # Check for duplicate and drop them

# In[22]:


du=da.duplicated().any()
du


# In[23]:


do=da.drop_duplicates()


# In[24]:


do.shape


# # Statistics

# In[25]:


da.describe()


# # Drop the columns capital-gain,capital-loss

# In[26]:


da.drop(["capital-gain",'capital-loss'],axis=1)


# # Univariate Analysis
# Taking one variable at a time

# # What is the distribution of Age column

# In[27]:


da["age"].describe()


# In[37]:


da["age"].hist()


# # Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method

# In[32]:


t=da[da["age"].between(17,48)]
t["age"].sum()


# # What is The Distribution of Workclass Column?

# In[33]:


da["workclass"].describe()


# In[35]:


da["workclass"].hist()
#overlapping change the figure size


# In[43]:


plt.figure(figsize=(10,10))
da["workclass"].hist()


# # How Many Persons Having Bachelors and Masters Degree?

# In[45]:


f=da["education"]=="Bachelors"
g=da["education"]=="Masters"
y=da[f|g]
y["education"].count()


# # Bivariate Analysis
#     Relationship between two Variables

# # Replace Salary(<=50 k ,>=50k) Values With 0 and 1

# In[46]:


sns.boxplot(x="income",y="age",data=da)


# In[47]:


da["income"].unique()


# In[48]:


da["income"].value_counts()


# In[49]:


sns.countplot("income",data=da)


# In[50]:


da.replace(to_replace=['<=50K', '>50K'],value=[0,1],inplace=True)


# In[51]:


da


# # Which Workclass Getting The Highest Salary?

# In[52]:


da.groupby("workclass")["income"].mean().sort_values(ascending=False)


# # How Has Better Chance To Get Salary greater than 50K Male or Female?

# In[53]:


da.groupby("gender")["income"].mean().sort_values(ascending=False)


# # Covert workclass Columns Datatype To Category Datatype

# In[54]:


da.info()


# In[56]:


da["workclass"]=da["workclass"].astype("category")


# In[57]:


da.info()


# In[59]:


sns.catplot(x="gender",y="hours-per-week",data=da,kind="boxen")


# In[60]:


sns.catplot(x="gender",y="age",data=da,hue="education",kind="boxen")


# In[61]:


sns.catplot(x="gender",y="age",data=da,hue="education",kind="boxen")


# In[62]:



sns.catplot(x="age",y="marital-status",data=da,hue="gender",kind="violin")


# In[ ]:






# coding: utf-8

# In[2]:

import pandas as pd


# In[3]:

#read dataser of Chiptle orders directly from a URL and store the results in a Dataframe
#All data are tab separated
orders = pd.read_table('http://bit.ly/chiporders')


# In[4]:

orders.head()


# In[5]:

pd.read_table('http://bit.ly/movieusers')
#The fields are not separated by tab


# In[6]:


pd.read_table('http://bit.ly/movieusers', sep='|', header=None)


# In[7]:

#It´s necessery to define column names
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)


# In[8]:


#let´s create a dataframe with it.
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)


# In[9]:

users


# In[ ]:




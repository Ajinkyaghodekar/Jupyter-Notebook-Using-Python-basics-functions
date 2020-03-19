#!/usr/bin/env python
# coding: utf-8

# In[ ]:


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


# In[33]:


all_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    all_ratings.append(rating)
    


# In[34]:


avg_rating = sum(all_ratings) / len(all_ratings)
avg_rating


# In[35]:


print('test code')


# In[36]:


welcome_message = 'Hello, Jupyter!'
first_cell = True
if first_cell:
    print(welcome_message)


# In[37]:


result = 1200/5
second_cell = True
if second_cell:
    print(result)
    



# In[2]:


print('First cell')


# In[5]:


print('Third cell')


# In[8]:


print('Second cell')


# In[9]:


print('A true third cell')


# In[27]:


def welcome(a_string):
    print('welcome to'  + a_string + '!')
    
dq = 'Dataquest'
jn = 'Jupyter Notebook'
py = 'Python'


# In[30]:


welcome(dq)
welcome(jn)
welcome(py)




# In[33]:


get_ipython().magic('history -p')


# In[34]:


get_ipython().magic('history -p')


# In[42]:


def welcome(a_string):
    welcome_msg = 'Welcome to ' + a_string + '!'
    return welcome_msg

dq = 'Dataquest'
jq = 'Jupyter Notebook'


# In[43]:


welcome(dq)
welcome(jq)


# In[45]:


get_ipython().magic('history -p')


# In[46]:


welcome(py)


# In[47]:


welcome(dq)


# In[49]:


opened_file  = open('AppleStore.csv')


# In[51]:


from csv import reader


# In[52]:


read_file = reader(opened_file)


# In[53]:


apps_data = list(read_file)


# In[54]:


apps_data[:4]


# In the Above code cell we:
# 
# 1. First open the 'AppleStore.csv' file using the open() function and assign the output to the variable opened_file.
# 2. Then import the reader() function from csv module
# 3. Then created real_file variable using reader() function to read the opened_file.
# 4. Then transform the read file into a list of lists using list() and save it to the variable name apps_data.
# 5. Finally display header rows and first three rows of the dataset.
# 

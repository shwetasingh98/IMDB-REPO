#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


# In[2]:


headers={"Accept-Language":"en-US,en;,q=0.5"}


# In[3]:


movie_name = []
year = []
time=[]
rating=[]
metascore =[]
votes = []
gross = []


# In[4]:


pages=np.arange(1,1000,50)


# In[5]:


print(pages)


# In[6]:


for page in pages:
    page=requests.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=50&start="+str(page)+"&ref_=adv_nxt")
    soup=BeautifulSoup(page.text,'html.parser')   
    movie_data=soup.findAll('div',attrs={'class':'lister-item mode-advanced'})
    sleep(randint(2,8))
    for store in movie_data:
        name=store.h3.a.text
        movie_name.append(name)
        
        year_of_release=store.h3.find('span', class_="lister-item-year text-muted unbold").text
        year.append(year_of_release)
        
        
        runtime=store.p.find("span",class_='runtime').text
        time.append(runtime)
        
        
        rate=store.find('div',class_="inline-block ratings-imdb-rating").text
        rating.append(rate)
        
        meta=store.find('span',class_="metascore").text if store.find('span',class_="metascore") else "0"
        metascore.append(meta)
        
        value=store.find_all('span', attrs={'name':"nv"})
        
        vote=value[0].text
        votes.append(vote)
        
        grosses=value[1].text if len(value)>1 else '0'
        gross.append(grosses)
        
df = pd.DataFrame({ "Movie Name": movie_name, "Year of Release" : year, "Watch Time": time,"Movie Rating": rating, "Meatscore of movie": metascore, "Votes" : votes, "Gross": gross })
        
        


# In[7]:


df


# In[8]:


type(df)


# In[9]:


df.shape


# In[10]:


df.dtypes


# In[11]:


df.isnull().sum()


# In[12]:


df[['Movie Name','Year of Release' ]].value_counts()


# In[13]:


df = df.replace(r'\n',' ', regex=True)


# In[14]:


df = df.replace(r'#',' ', regex=True)


# In[15]:


df


# In[16]:


df.to_csv('C:\\Users\\ADMIN\\Desktop\\sstt.csv')


# In[40]:


top_movies=df['Movie Name'].value_counts().head(5)


# In[41]:


top_movies


# In[44]:


plt.figure(figsize=(8,4))
plt.title('Top movies')
sns.barplot(x=top_movies.index, y=top_movies);


# In[96]:


m_Rat=df[['Movie Name','Movie Rating']]


# In[98]:


m_Rat


# In[99]:


m_Rat.head(10)


# In[116]:


m_Rat=df.groupby(['Movie Rating']).sum()
m_Rat


# In[118]:


rate_info=df.groupby(['Movie Name']).value_counts()
rate_info


# In[ ]:





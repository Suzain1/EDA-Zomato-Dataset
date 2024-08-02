#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv('C:\\Users\\suzai\\Downloads\\Zomatodataset\\zomato.csv', encoding = 'latin')
df.head()


# In[8]:


df.columns


# In[10]:


df.info()


# In[11]:


df.describe() #contains only features containg integer values


# In[12]:


df.isnull().sum() # finds number of missing values


# In[15]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[23]:


sns.heatmap(df.isnull(), yticklabels= False, cbar =False , cmap = 'viridis')  #very less number of null values that is why it is not visible


# In[26]:


df_country = pd.read_excel('C:\\Users\\suzai\\Downloads\\Zomatodataset\\Country-Code.xlsx')
df_country.head()


# In[30]:


final_df = pd.merge(df,df_country, on= 'Country Code',how = 'left')
#on = on which column do we want to merge the tables (common columns) and how = which side you want to focus more on


# In[31]:


final_df.head()


# In[35]:


final_df.dtypes


# In[36]:


final_df.columns


# In[37]:


country_val = final_df.Country.value_counts()


# In[46]:


country_names = final_df.Country.value_counts().index
print(country_names)


# In[47]:


country_val = final_df.Country.value_counts()
print(country_val)


# In[59]:


plt.pie(country_val[:3], labels = country_names[:3], autopct="%1.2f%%")


# In[60]:


final_df.columns


# In[73]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})
print(ratings)


# In[88]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x = "Aggregate rating", y = "Rating Count", hue = "Rating color",  data = ratings )


# In[89]:


sns.countplot(x="Rating color", data = ratings)


# In[108]:


count_rating = final_df.g(['Rating color'== 'White', 'Country']).size().reset_index()
print(count_rating.head(66))


# In[111]:


count_rating = final_df[final_df["Rating color"] == 'White'].groupby('Country').size().reset_index()
print(count_rating)


# In[113]:


count_currency = final_df.groupby(['Currency', 'Country']).size().reset_index()
print(count_currency)


# In[114]:


online_deli = final_df.groupby(['Has Online delivery', 'Country']).size().reset_index()
print(online_deli)


# In[116]:


city = final_df["City"].unique()
print(city)


# In[117]:


city_val = final_df.City.value_counts()
print(city_val)


# In[122]:


city_name = final_df.City.value_counts().index
print(city_name)


# In[ ]:





# In[129]:


plt.pie(city_val[:5], labels = city_name[:5], autopct="%1.2f%%")


# In[131]:


#top 10 cuisines
final_df.columns


# In[133]:


a= final_df["Cuisines"]
print(a)


# In[ ]:





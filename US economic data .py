#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook
output_notebook()


# In[2]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color='firebrick', line_width=4, legend='% GDP change')
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend='% unemployed')
    show(p)


# In[4]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

GDP_data= pd.read_csv(links['GDP'])  #GDP_data is the name of the file
GDP_data                             #dataframe containing the gdp data


# In[6]:


GDP_data= pd.read_csv(links['GDP'])  #GDP_data is the name of the file
GDP_data.head()                           


# In[9]:


unemployment_data= pd.read_csv(links['unemployment'])  #unemployment_data is the name of the file
unemployment_data                                      #dataframe containing the unemployment data


# In[10]:


unemployment_data=pd.read_csv(links['unemployment'])
unemployment_data.head()                               #displaying the first five rows of the unemployment dataframe


# In[30]:


new=unemployment_data[unemployment_data['unemployment']>8.5]
new


# In[31]:


x=GDP_data[['date']]
x


# In[32]:


gdp_change=GDP_data[['change-current']]
gdp_change


# In[33]:


unemployment=unemployment_data[['unemployment']]
unemployment


# In[35]:


title= "unemployment during the given gdp"


# In[36]:


file_name="index.html"


# In[37]:


make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title=title, file_name=file_name)


# In[ ]:





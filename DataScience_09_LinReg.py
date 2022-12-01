#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# # Part I: Simpler Linear Regression. Knowing data

# Data source [0].

# <h1>Table of contents</h1>
# 
# <div class="alert  alert-block alert-info" style="margin-top: 20px">
#     <ol>
#         <li><a href="#unData">Data</a></li>
#          <ol>
#              <li><a href="#reData">Reading</a></li>
#              <li><a href="#exData">Exploration</a></li>
#          </ol>
#         <li><a href="#daExploration">Data Exploration</a></li>
#         <li><a href="#simRegression">Simple Regression Model</a></li>
#     </ol>
# </div>
# <br>
# <hr>

# 
# <h2 id="unData">Data</h2>
# 
# ### `titanic3.csv`:
# 
# This dataset contains a model-specific fuel consumption ratings and estimated carbon dioxide 
# emissions for new light-duty vehicles for retail sale in Canada.
# 
# Some **features** are
# 
# - **survived** e.g. 1 or 0
# 

# In[4]:


df = pd.read_csv("titanic3.csv")


# In[5]:


df.dtypes


# In[6]:


df.shape


# In[7]:


print("Number of rows =", df.shape[0], "\nNumber of features (columns) =",df.shape[1])


# In[8]:


df.columns


# In[9]:


type(df)


# In[10]:


df.head(7)


# In[11]:


df.describe()


# ## Querying
# 
# Note, pandas considers a table (dataframe) as a pasting of many "series" together, horizontally.

# In[12]:


type(df.survived), type(df)


# In[13]:


df.survived == 1


# In[14]:


from statistics import median
from statistics import mean
def statistics(n):
    for i in range(len(n)):
        values =[]
        average = n[i].sum()/n[i].count()
        values.append(average)
        values.append(n[i].mean())
        values.append(n[i].median())
        values.append(n[i].sum())
        values.append(n[i].min())
        values.append(n[i].max())
        values.append(n[i].count())
        print(values)
        print('\n')
statistics([df.age,df.fare,df.body,df.pclass])


# In[16]:


import seaborn as sns
#means of df.age,df.fare,df.body,df.pclass
sns.distplot([29.881137667304014,33.29547928134557,160.8099173553719,2.294881588999236]
).set(title='Means')
plt.show()


# ## You should implement similar NB to DataScience_7_LinReg.ipynb
# ## Exercises should be different.

# ##  Exercises

# 1. Use at least four more features and calculate: average, mean, median, sum, and implement at least three more statistics functions. Check the ```numpy``` documentation. Different to previous implementations.
# 1. Implement a new different Library, such as ```seaborn```
# 1. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# ## Versions

# In[ ]:


from platform import python_version
print("python version: ", python_version())
get_ipython().system('pip3 freeze | grep qiskit')


# # References

# [0] data https://tinyurl.com/2m3vr2xp
# 
# [1] numpy https://numpy.org/
# 
# [2] scipy https://docs.scipy.org/
# 
# [3] matplotlib https://matplotlib.org/
# 
# [4] matplotlib.cm https://matplotlib.org/stable/api/cm_api.html
# 
# [5] matplotlib.pyplot https://matplotlib.org/stable/api/pyplot_summary.html
# 
# [6] pandas https://pandas.pydata.org/docs/
# 
# [7] seaborn https://seaborn.pydata.org/
# 

# In[ ]:





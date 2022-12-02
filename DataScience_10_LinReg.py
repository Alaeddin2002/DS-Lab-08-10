#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# In[2]:


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
#         <li><a href="#unData">AAAA</a></li>
#          <ol>
#              <li><a href="#reData">ZZZZ</a></li>
#              <li><a href="#exData">YYY</a></li>
#          </ol>
#         <li><a href="#daExploration"> XXXX</a></li>   
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
# - **srvived** e.g. 2014

# In[3]:


df = pd.read_csv("titanic3.csv")


# In[4]:


df.dtypes


# In[5]:


print("Number of rows =", df.shape[0], "\nNumber of features (columns) =",df.shape[1])


# In[6]:


df.columns


# We select some features

# In[7]:


Seldf = df[['pclass','survived','sibsp','parch']]


# In[8]:


Seldf.head(5)


# In[9]:


Seldf.dtypes


# # Plotting

# ## Histograms. You should modify this part

# In[10]:


SeldfHistogram = Seldf[['pclass','survived','sibsp','parch']]


# In[11]:


SeldfHistogram.hist(facecolor='g', alpha=0.75)
plt.grid(True)
plt.show()


# ## Scatter plot

# In[60]:


import seaborn as sns

sns.regplot(df.age,df.fare,color='g')


# In[61]:


sns.lineplot(df.age,df.fare)


# In[59]:


plt.scatter(df.age,df.fare)

plt.show()


# # Exercises

# 1. Plot **Atribute A** vs **atribute B**, to see how linear is their relationship.
# 1. Use ```matplotlib``` documentation, and implement different parameters to get a beatiful plot. Different to previous NB
# 1. Create the scatter plot
# 1. Implement a new different Library, such as ```seaborn```
# 1. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# ## Versions

# In[33]:


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





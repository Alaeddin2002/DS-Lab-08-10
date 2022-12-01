#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# In[1]:


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
# ### `FuelConsumption.csv`:
# 
# This dataset contains a model-specific fuel consumption ratings and estimated carbon dioxide 
# emissions for new light-duty vehicles for retail sale in Canada.
# 
# Some **features** are
# 
# - **MODELYEAR** e.g. 2014
# - **MAKE** e.g. Acura
# - **MODEL** e.g. ILX
# - **VEHICLE CLASS** e.g. SUV
# - **ENGINE SIZE** e.g. 4.7
# - **CYLINDERS** e.g 6
# - **TRANSMISSION** e.g. A6
# - **FUEL CONSUMPTION in CITY(L/100 km)** e.g. 9.9
# - **FUEL CONSUMPTION in HWY (L/100 km)** e.g. 8.9
# - **FUEL CONSUMPTION COMB (L/100 km)** e.g. 9.2
# - **CO2 EMISSIONS (g/km)** e.g. 182   --> low --> 0

# In[5]:


df = pd.read_csv("FuelConsumption.csv")


# <h3>Dataframe</h3>
# 
# <div class="alert  alert-block alert-info" style="margin-top: 20px">
#     A dataframe is a two-dimensional of data with columns and rows indexes. 
#     The columns are made up of pandas series objects.
#     
# </div>
# <br>
# <hr>

# In[6]:


df.dtypes


# In[7]:


print("Number of rows =", df.shape[0], "\nNumber of features (columns) =",df.shape[1])


# In[8]:


df.columns


# We select some features

# In[9]:


Seldf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]


# In[10]:


Seldf.head(5)


# In[11]:


Seldf.dtypes


# # Plotting

# ## Histograms

# In[12]:


SeldfHistogram = Seldf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]


# In[13]:


SeldfHistogram.hist(facecolor='g', alpha=0.75)
plt.grid(True)
plt.show()


# ## Scatter plot

# In[14]:


plt.scatter(Seldf.FUELCONSUMPTION_COMB, Seldf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel(r"CO$_2$ Emission")
plt.title(r"CO$_2$ Emission vs. Fuel consumption")
plt.grid(True)
plt.show()


# In[15]:


plt.scatter(Seldf.ENGINESIZE, Seldf.CO2EMISSIONS,  color='red')
plt.xlabel("Engine size")
plt.ylabel(r"CO$_2$ Emission")
plt.title(r"CO$_2$ Emission vs. Engine size")
plt.text(7.5, 350, r'This point', c = 'g')
plt.grid(True)
plt.show()


# In[22]:


plt.scatter(Seldf.CYLINDERS, Seldf.CO2EMISSIONS,  color='red')
plt.xlabel("Engine size")
plt.ylabel(r"CO$_2$ Emission")
plt.title(r"CO$_2$ Emission vs. Engine size")
plt.grid(True)
plt.show()


# # Exercises

# 1. Plot **CYLINDER** vs **Emission**, to see how linear is their relationship.
# 1. Use ```matplotlib``` documentation, and implement different parameters to get a beatiful plot.
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





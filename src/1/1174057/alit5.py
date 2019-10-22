# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:22:08 2019

@author: alitf
"""

import shapefile

w=shapefile.Writer('alit5', shapefile=3)

# In[]: mendeklarasikan table shapefile
w.field("kolom1","C")
w.field("kolom2","C")

# In[]: mengisi table
w.record("yun","satu")

# In[]: membuat garis yang menghubungkan antara titik
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])

# In[]: save
w.close()
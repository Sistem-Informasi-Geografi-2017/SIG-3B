# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:01:41 2019

@author: alitf
"""

import shapefile

w=shapefile.Writer('alit4', shapefile .POINT)

# In[]: mendeklarasikan table shapefile
w.field("kolom1","C")
w.field("kolom2","C")

# In[]: mengisi table
w.record("lit","satu")
w.record("yun","dua")

# In[]: mengisi data vektor poin
w.point(1,1)
w.point(2,2)

# In[]: save
w.close()   
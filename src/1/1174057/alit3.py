# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:56:37 2019

@author: alitf
"""

import shapefile

w=shapefile.Writer('alit3', shapeType=1) 

# In[]: mendeklarasikan table shapefile
w.field("kolom1","C")
w.field("kolom2","C")

# In[]: mengisi table
w.record("wiw","satu") 
w.record("wow","dua")

# In[]: mengisi data vektor poin
w.point(1,1)
w.point(2,1.5)

# In[]: save
w.close()   
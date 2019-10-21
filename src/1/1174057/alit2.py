# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:50:44 2019

@author: alitf
"""

import shapefile

w=shapefile.Writer('alit2',shapeType=1) 

# In[]: mendeklarasikan table shapefile
w.shapeType
w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")

# In[]: mengisi table
w.record("uhuy","satu") 
w.record("ihiy","dua")

# In[]: mengisi data vektor poin
w.point(1,1)
w.point(2,2)

# In[]: save
w.close()   
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:09:56 2019

@author: alitf
"""

import shapefile

w=shapefile.Writer('alit1',shapeType=1) 

# In[]: mendeklarasikan table shapefile
w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")

# In[]: mengisi table
w.record("ngek","satu") 
w.record("ngok","dua")

# In[]: mengisi data vektor poin
w.point(1,1)
w.point(2,2)

# In[]: save
w.close()    

           
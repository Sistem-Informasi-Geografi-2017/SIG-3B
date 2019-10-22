# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:25:33 2019

@author: alitf
"""

import shapefile

# In[]: membuat file dengan nama alit6 dan untuk membua garis menggunakan shapefile=5
w=shapefile.Writer('alit6', shapefile=5)

# In[]: mendeklarasikan table shapefile
w.field("kolom1","C")
w.field("kolom2","C")

# In[]: isi dari tabel yun adalah isi dari kolom1 dan satu kolom2
w.record("yun","satu")

# In[]: membuat garis yang menghubungkan antara titik
w.poly([[[1,3],[5,3]]])

# In[]: save
w.close()
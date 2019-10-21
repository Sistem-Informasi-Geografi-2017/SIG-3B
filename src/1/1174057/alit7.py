# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:13:37 2019

@author: alitf
"""

import shapefile

# In[]: membuat file dengan nama soal 6 dan untuk membua polygon menggunakan shapefile=5
w=shapefile.Writer('alit7', shapefile=5)

# In[]: mendeklarasikan table shapefile
w.field("kolom1","C") 
w.field("kolom2","C") 

# In: isi dari tabel yun adalah isi dari kolom1 dan satu kolom2
w.record("yun","satu")

# In[]: membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[1,3],[5,3],[1,2],[5,2]]])

# In[]: penutup
w.close() 
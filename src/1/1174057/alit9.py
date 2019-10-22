# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:26:30 2019

@author: alitf
"""

import shapefile 

# In[]; membuat file dengan nama soal 9 dan untuk membua polygon menggunakan shapefile=5
w=shapefile.Writer('alit9', shapeType=5) 

# In[]: Membuat tabel dengan kolom pertama dan kedua
w.field("kolom1","C") 
w.field("kolom2","C")

#In[]: isi dari tabel adalah isi dari kolom1 dan satu kolom2
w.record("lit","satu") 
w.record("alit","dua")

# In[]: membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
w.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])

# In[]: Penutup
w.close() #penutup

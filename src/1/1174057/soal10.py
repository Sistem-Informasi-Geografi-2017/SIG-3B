# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:37:32 2019

@author: alitf
"""

import shapefile

# In[]: membuat file dengan nama soal 8 dan untuk membua polygon menggunakan shapefile=5
w=shapefile.Writer('soal10', shapeType=5) 

# In[]: Membuat tabel dengan kolom pertama dan kedua
w.field("klm1","C") 
w.field("klm2","C")

# In[]: isi dari tabel ngek adalah isi dari kolom1 sampai kolom5
w.record("yun","aku")
w.record("lit","kamu")
w.record("tod","dia")
w.record("wew","mereka")
w.record("rok","siapa")

# In[]: membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[-1,1],[0,3],[1,1],[-1,1]]])   
w.poly([[[-1,5],[0,3],[1,5],[-1,5]]])   
w.poly([[[2,2],[0,3],[2,4],[2,2]]])  
w.poly([[[-2,2],[0,3],[-2,4],[-2,2]]])
w.poly([[[-3,1],[-4,3],[-5,1],[-3,1]]])

# In[]: penutup
w.close() 

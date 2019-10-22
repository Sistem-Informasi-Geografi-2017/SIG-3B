# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:39:53 2019

@author: User
"""

import shapefile #Mengambil data dari shapefile
w=shapefile.Writer('soal7', shapeType=5) #membuat file dengan nama soal 7 dan untuk membua polygon menggunakan shapefile=5
w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua
w.record("ken","satu") #isi dari tabel ken adalah isi dari kolom1 dan satu kolom2
w.poly([[[1,3],[5,3],[1,2],[5,2]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.close() #penutup
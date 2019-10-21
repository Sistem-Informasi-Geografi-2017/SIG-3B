# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:26:43 2019

@author: User
"""

import shapefile #Mengambil data dari shapefile
w=shapefile.Writer('soal2', shapeType=1) #Membuat file yang bernama soal2 dan mendefinisikan shapetype=1 untuk point
w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua
w.record("ken","satu") #isi dari tabel ken adalah isi dari kolom1 dan satu kolom2
w.record("tha","dua") #isi dari tabel tha adalah isi dari kolom1 dan dua kolom2
w.point(1,1) # membuat poin dengan menentukan titik x dan y
w.point(2,2) #membuat poin dengan menentukan titik x dan y
w.close() #penutup

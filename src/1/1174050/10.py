# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:01:17 2019

@author: User
"""

import shapefile #Mengambil data dari shapefile
w=shapefile.Writer('soal10', shapeType=5) #membuat file dengan nama soal 10 dan untuk membua polygon menggunakan shapefile=5
w.field("k1","C") #Membuat tabel dengan kolom pertama
w.field("k2","C") #Membuat tabel dengan kolom kedua
w.record("Utara","Sepuluh") #isi dari tabel Utara adalah isi dari kolom1 dan Sepuluh kolom2
w.record("Selatan","Sebelas") #isi dari tabel Selatan adalah isi dari kolom1 dan Sebelas kolom2
w.record("Kamu","Selingkuh") #isi dari tabel Kamu adalah isi dari kolom1 dan Selingkuh kolom2
w.record("Raimu","TakAmplas") #isi dari tabel Raimu adalah isi dari kolom1 dan TakAmplas kolom2
w.record("By","RadhycaLz") #isi dari tabel By adalah isi dari kolom1 dan RadhycaLz kolom2
w.poly([[[2,2],[8,2],[8,8],[2,8],[2,2]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[9,2],[15,2],[15,8],[9,8],[9,2]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[2,0],[8,0],[8,-6],[2,-6],[2,0]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[9,0],[15,0],[15,-6],[9,-6],[9,0]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[20,0],[26,0],[26,-6],[20,-6],[20,0]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.close() #penutup

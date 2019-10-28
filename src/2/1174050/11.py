# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:14:32 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
isidata = sf.records() #Memanggil seluruh record yang terdapat pada file db soal1
print(isidata[0]) #Menampilkan isi baris ke 1 yang telah dipanggil
print(isidata[0][0]) #Menampilkan isi baris ke 1 dan kolom ke 1 yang telah dipanggil pada file db soal1
sf.close() #Menutup reader pyshp
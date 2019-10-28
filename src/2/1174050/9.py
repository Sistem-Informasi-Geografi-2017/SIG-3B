# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:50 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
namakolom = sf.fields #Memanggil field  yang terdapat pada file db soal1
print(namakolom) #Menampilkan hasil pemanggilan field
sf.close() #Menutup reader pyshp
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:51 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
isidata = sf.records() #Memanggil seluruh isi yang terdapat pada file db soal1
print(isidata) #Menampilkan isi yang telah dipanggil pada file db soal1
sf.close() #Menutup reader pyshp
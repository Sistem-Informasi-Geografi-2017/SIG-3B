# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:48 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
print(sf.shapeType) #Menampilkan tipe bentuk dari shapefile yang dibaca yaitu file soal1
sf.close() #Menutup reader pyshp
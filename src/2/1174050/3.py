# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:49 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
print(sf.bbox) #Untuk mengambil koordinat dari bentuk yang dibaca dan mengkonversinya dengan bentuk array
sf.close() #Menutup reader pyshp
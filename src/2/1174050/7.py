# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:50 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
anu = sf.shapes() #Memanggil semua shapes yang telah dibaca dan mengkonversinya dengan bentuk array
print(anu[0].parts) #Mengelompokkan kumpulan point menjadi shapes
sf.close() #Menutup reader pyshp
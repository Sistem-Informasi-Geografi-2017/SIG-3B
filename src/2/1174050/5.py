# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:49 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
anu = sf.shapes() #Memanggil semua shapes yang telah dibaca dan mengkonversinya dengan bentuk array
print(dir(anu)) #Menampilkan fungsi apa saja yang dapat digunakan oleh fungsi shapes pada semua shape
print(dir(anu[0])) #Menampilkan fungsi apa saja yang dapat digunakan oleh fungsi shapes pada shape pertama
sf.close() #Menutup reader pyshp
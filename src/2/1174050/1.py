# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:47 2019

@author: User
"""

import shapefile #Import library shapefile
sf = shapefile.Reader("soal1") #Memanggil fungsi untuk membaca file PYSHP dengan nama soal1
sf.close() #Menutup reader pyshp
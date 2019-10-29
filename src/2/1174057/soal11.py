"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : menggunakan fungsi records
isidata = sf.records()

# In[] : menampilkan isidata pada index 0
print(isidata[0])

# In[] : print isidata dari index 0 pada index 0
print(isidata[0][0])
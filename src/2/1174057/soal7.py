"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit5.shp") 

# In[] : membaca shapes
lit = sf.shapes()

# In[] : menggunakan fungsi parts
isi = lit[0].parts

# In[] : menampilkan isi
print(isi) 
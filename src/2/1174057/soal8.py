"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : membaca shapes
lit = sf.shapes()

# In[] : menggunakan fungsi point
anu = lit[0].points

# In[] : menampilkan anu
print(anu)
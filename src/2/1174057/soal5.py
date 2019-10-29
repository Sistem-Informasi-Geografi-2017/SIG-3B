"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : membaca shapes
lit = sf.shapes()

# In[] : menggunakan fungsi dir
dir(lit)

# In[] : menampilkan fungsi dir
print(dir(lit[0])) 
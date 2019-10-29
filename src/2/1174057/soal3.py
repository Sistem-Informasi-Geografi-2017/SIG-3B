"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : Membaca bbox yang digunakan
lit = sf.bbox

# In[] : Menampilkan fungsi dari lit 
print(lit)
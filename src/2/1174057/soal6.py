"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : membaca shapes
lit = sf.shapes()

# In[] : Menggunakan sebuah fungsi pada shapetype untuk memeriksa sebuah tipe
ngek = lit[0].shapeType

# In[] : menampilkan fungsi isi
print(ngek)
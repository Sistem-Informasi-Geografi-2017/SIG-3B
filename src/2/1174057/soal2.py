"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : Membaca tipe shape yang di pakai
alt = sf.shapeType

# In[] : Menampilkan fungsi dari alt untuk membaca shapeType
print(alt)  
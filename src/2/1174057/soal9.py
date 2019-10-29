"""
@author: alitf
"""

# In[] : menggunakan library
import shapefile

# In[] : menginisialisasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama file
sf = shapefile.Reader("alit1.shp") 

# In[] : menggunakan fungsi fields
namakolom = sf.fields

# In[] ; menampilkan namakolom
print(namakolom)
"""
@author: alitf
"""

# In[] : mengimport library shapefile
import shapefile 

# In[] : membaca file shp dengan nama file alit1.shp
sf = shapefile.Reader("alit1.shp") 

# In[] : membaca shape 
anu = sf.shapes() 

# In[] : Menghitung jumlah shape yang ada pada anu
print(len(anu))     
import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
sf.close() #Menutup reader pyshp
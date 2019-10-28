import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
print(sf.bbox) #Untuk mengambil koordinat dari bentuk yang dibaca dan mengkonversinya dengan bentuk array
sf.close() #Menutup reader pyshp
import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
print(sf.shapeType) #Menampilkan tipe bentuk dari shapefile yang dibaca yaitu file sample
sf.close() #Menutup reader pyshp
import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
namakolom = sf.fields #Memanggil field  yang terdapat pada file db sample
print(namakolom) #Menampilkan hasil pemanggilan field
sf.close() #Menutup reader pyshp
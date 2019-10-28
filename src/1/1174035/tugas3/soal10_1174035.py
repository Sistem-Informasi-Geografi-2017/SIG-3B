import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
isidata = sf.records() #Memanggil seluruh record yang terdapat pada file db sample
print(isidata) #Menampilkan record yang telah dipanggil pada file db sample
sf.close() #Menutup reader pyshp
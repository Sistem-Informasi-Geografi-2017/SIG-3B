import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
isidata = sf.records() #Memanggil seluruh record yang terdapat pada file db sample
print(isidata[0]) #Menampilkan record baris ke 1 yang telah dipanggil
print(isidata[0][0]) #Menampilkan record baris ke 1 dan kolom ke 1 yang telah dipanggil pada file db sample
sf.close() #Menutup reader pyshp
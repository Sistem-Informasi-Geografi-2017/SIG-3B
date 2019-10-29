import shapefile #Import modul shapefile
sf = shapefile.Reader("soal9") #membaca soal9
isidata = sf.records() #isi dari setiap kolom
print(isidata) #menampilkannya

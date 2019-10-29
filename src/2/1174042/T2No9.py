import shapefile #Import modul shapefile
sf = shapefile.Reader("soal9") #membaca soal9
namakolom = sf.fields #menampilkan kolom dan keterangan pada setiap kolom
print(namakolom) #menampilkannya

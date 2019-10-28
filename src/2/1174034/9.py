import shapefile #mengimport shapefile
sf = shapefile.Reader("Soal1") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
namakolom = sf.fields # membaca nama kolom
print(namakolom) #menampilkan isi dari variable namakolom
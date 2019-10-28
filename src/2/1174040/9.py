import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
namakolom = sf.fields # membaca nama kolom
print(namakolom) #menampilkan isi dari variable namakolom
import shapefile #mengimport shapefile
sf = shapefile.Reader("Soal1") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sb = sf.bbox # membaca bbox nya
print(sb) #menampilkan isi dari variable sb
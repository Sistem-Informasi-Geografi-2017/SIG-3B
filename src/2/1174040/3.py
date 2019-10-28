import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sb = sf.bbox # membaca bbox nya
print(sb) #menampilkan isi dari variable sb
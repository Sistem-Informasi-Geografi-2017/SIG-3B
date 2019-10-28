import shapefile #mengimport shapefile
sf = shapefile.Reader("Soal1") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
isidata = sf.records() # membaca record
print(isidata) #menampilkan isi dari variable isidata
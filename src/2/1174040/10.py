import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
isidata = sf.records() # membaca record
print(isidata) #menampilkan isi dari variable isidata
import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
isidata = sf.records() # membaca record
print(isidata[0]) #menampilkan isi dari variable isidata di index 0
print(isidata[0][0]) #menampilkan isi dari variable isidata di index 0 berindex 0
import shapefile #mengimport shapefile
sf = shapefile.Reader("Soal1") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sp = sf.shapes() # membaca shapes
anu = sp[0].points # membaca point 
print(anu) #menampilkan isi dari variable anu
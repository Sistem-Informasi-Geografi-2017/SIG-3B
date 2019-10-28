import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sp = sf.shapes() # membaca shapes
anu = sp[0].points # membaca point 
print(anu) #menampilkan isi dari variable anu
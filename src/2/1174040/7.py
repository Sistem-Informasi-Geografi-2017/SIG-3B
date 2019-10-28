import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal9.shp") #membaca file shp yang bernama Soal9 di dalam folder Tugas4
sp = sf.shapes() # membaca shapes 
anu = sp[1].parts #untuk membaca ada berapa part yg ada..jika hanya ada satu maka dikembalikan nilai 0
print(anu) #menampilkan isi dari variable anu
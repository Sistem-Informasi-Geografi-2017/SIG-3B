import shapefile #mengimport shapefile
sf = shapefile.Reader("Tugas4/Soal1.shp") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sp = sf.shapes() # untuk membaca shapes
print(dir(sp[0])) # untuk menampilkan fungsi - fungsi di dir dari index 0
print(dir(sp)) # untuk menampilkan fungsi - fungsi di dir
import shapefile #mengimport shapefile
sf = shapefile.Reader("Soal1") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
sp = sf.shapes() # untuk membaca shapes 
print(len(sp)) # untuk menghitung ada berapa banyak shapes yang telah dimasukkan dalam variable sp
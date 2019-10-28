import shapefile #mengimport shapefile
sf = shapefile.Reader("Soal1") #membaca file shp yang bernama Soal1 di dalam folder Tugas4
st = sf.shapeType # membaca tipe shape apa yang digunakan
print(st) # menampilkan variable st yaitu shapetype
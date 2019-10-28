import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
hsl = sf.shapeType #menggunakan fungsi shapetype untuk cek tipe
print(hsl) #menampilkan fungsi dari hsl
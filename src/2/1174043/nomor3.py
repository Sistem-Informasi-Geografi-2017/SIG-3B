import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
hsl = sf.bbox #menggunakan fungsi bbox
print(hsl) #menampilkan fungsi dari hsl
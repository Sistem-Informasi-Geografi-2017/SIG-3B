import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
isidata = sf.records() #menggunakan fungsi records
print(isidata) #menampilkan variabel isidata
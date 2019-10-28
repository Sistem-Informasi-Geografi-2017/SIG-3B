import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
isidata = sf.records() #menggunakan fungsi records
print(isidata[0]) #menampilkan isidata index 0
print(isidata[0][0]) #menampilkan isidata index 0 dari index 0
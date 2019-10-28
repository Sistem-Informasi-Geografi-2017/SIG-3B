import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
anu = sf.fields #menggunakan fungsi fields
print(anu) #menampilkan variabel anu
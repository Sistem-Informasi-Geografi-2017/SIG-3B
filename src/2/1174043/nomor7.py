import shapefile #import class shapefile
sf = shapefile.Reader("Nomor9.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor9.shp
anu = sf.shapes() #menggunakan fungsi shapes
isi = anu[0].parts #menggunakan fungsi parts
print(isi) #menampilkan variabel isi
import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
anu = sf.shapes() #menggunakan fungsi shapes
isi = anu[0].shapeType #menggunakan fungsi shapetype untuk cek tipe
print(isi) #menampilkan fungsi dari variabel isi
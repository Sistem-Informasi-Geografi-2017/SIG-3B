import shapefile #import class shapefile
sf = shapefile.Reader("Nomor1.shp") #menggunakan fungsi reader dari shapefile untuk membaca file nomor1.shp
anu = sf.shapes() #menggunakan fungsi shapes
print(len(anu)) #menampilkan fungsi dari hsl
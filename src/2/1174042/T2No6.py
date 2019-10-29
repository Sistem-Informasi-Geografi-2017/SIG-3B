import shapefile #Import modul shapefile
sf = shapefile.Reader("soal9") #membaca soal9
anu=sf.shapes()#untuk mendapatkan daftar geometri shapefile dengan memanggil metode shapes().
print(anu[1].shapeType)#untuk melihat type shapefile pada baris

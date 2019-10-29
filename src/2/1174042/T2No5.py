import shapefile #Import modul shapefile
sf = shapefile.Reader("soal9") #membaca soal9
anu=sf.shapes()#untuk mendapatkan daftar geometri shapefile dengan memanggil metode shapes().
dir(anu) #dir berguna untuk melihat objek
print(dir(anu[0]))#melihat objek ke 1

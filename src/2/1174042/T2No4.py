import shapefile #Import modul shapefile
sf = shapefile.Reader("soal8") #membaca soal8
anu=sf.shapes()#untuk mendapatkan daftar geometri shapefile dengan memanggil metode shapes().
print(len(anu))#lea berguna untuk melihat berapa baris


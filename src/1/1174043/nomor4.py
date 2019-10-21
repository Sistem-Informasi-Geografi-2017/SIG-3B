import shapefile #import class shapefile

tes=shapefile.Writer('nomor4', shapefile.POINT) #buat file nomor4 dan menggunakan shapefile.POINT

tes.field("kolom1","C") #buat tabel pertama
tes.field("kolom2","C") #buat tabel kedua

tes.record("ngek","satu") #isi tabel ngek
tes.record("ngok","dua") #isi tabel ngok

tes.point(1,1) #poin titik x dan y
tes.point(2,2) #poin titik x dan y

tes.close() #tutup

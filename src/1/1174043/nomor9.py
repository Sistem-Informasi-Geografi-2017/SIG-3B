import shapefile #import class shapefile

tes=shapefile.Writer('nomor9', shapeType=5) #buat file nomor9 dan untuk menggunakan shapefile=5

tes.field("kolom1","C") #buat tabel  pertama
tes.field("kolom2","C") #buat tabel  kedua

tes.record("ngek","satu") #isi tabel ngek
tes.record("crot","dua") #isi tabel crot

tes.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]]) #buat garis
tes.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]]) #buat garis

tes.close() #tutup

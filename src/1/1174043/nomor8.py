import shapefile #import class shapefile

tes=shapefile.Writer('nomor8', shapeType=5) #buat file nomor8 dan untuk menggunakan shapefile=5

tes.field("kolom1","C") #buat tabel pertama
tes.field("kolom2","C") #buat tabel kedua

tes.record("ngek","satu") #isi tabel ngek

tes.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]]) #buat garis

tes.close() #tutup

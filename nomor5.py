import shapefile #import class shapefile

tes=shapefile.Writer('nomor5', shapefile=3) #buat file nomor5 dan menggunakan shapefile=3

tes.field("kolom1","C") #buat tabel pertama
tes.field("kolom2","C") #buat tabel kedua

tes.record("ngek","satu") #isi tabel ngek

tes.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #buat garis

tes.close() #tutup

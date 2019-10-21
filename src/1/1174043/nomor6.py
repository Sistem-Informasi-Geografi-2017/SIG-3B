import shapefile #import class shapefile

tes=shapefile.Writer('nomor6', shapefile=5) #buat file nomor6 dan untuk menggunakan shapefile=5

tes.field("kolom1","C") #buat tabel pertama
tes.field("kolom2","C") #buat tabel kolom kedua

tes.record("ngek","satu") #isi tabel ngek

tes.poly([[[1,3],[5,3]]]) #buat garis

tes.close() #tutup

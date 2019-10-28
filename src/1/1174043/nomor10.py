import shapefile #import class shapefile

tes=shapefile.Writer('nomor10', shapeType=5) #buat file nomor10 dan untuk menggunakan shapefile=5

tes.field("kolom1","C") #buat tabel  pertama
tes.field("kolom2","C") #buat tabel  kedua

tes.record("ngek","satu") #isi tabel ngek
tes.record("ngok","dua") #isi tabel ngok
tes.record("ngik","tiga") #isi tabel ngok
tes.record("crot","empat") #isi tabel crot

tes.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]]) #buat garis
tes.poly([[[1,5],[5,5], [5,4],[1,4],[1,5]]]) #buat garis
tes.poly([[[1,7],[5,7], [5,6],[1,6],[1,7]]]) #buat garis
tes.poly([[[1,9],[5,9], [5,8],[1,8],[1,9]]]) #buat gariss

tes.close() #tutup
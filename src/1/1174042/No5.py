import shapefile #Mengambil data dari shapefile
w=shapefile.Writer('soal5', shapefile=3) #membuat file dengan nama soal 5 dan untuk membua garis menggunakan shapefile=3
w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua
w.record("ngek","satu") #isi dari tabel ngek adalah isi dari kolom1 dan satu kolom2
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis dengan menghubungkan titik titik yang dibuat
w.close() #penutup

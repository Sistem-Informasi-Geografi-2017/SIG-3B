import shapefile #Mengambil data dari shapefile
w=shapefile.Writer('soal10', shapeType=5) #membuat file dengan nama soal 10 dan untuk membua polygon menggunakan shapefile=5
w.field("k1","C") #Membuat tabel dengan kolom pertama
w.field("k2","C") #Membuat tabel dengan kolom kedua
w.record("Aku","Kamu") #isi dari tabel Aku adalah isi dari kolom1 dan Kamu kolom2
w.record("Dia","Pacarmu") #isi dari tabel Dia adalah isi dari kolom1 dan Pacarmu kolom2
w.record("Sudah","Chatan") #isi dari tabel Sudah adalah isi dari kolom1 dan Chatan kolom2
w.poly([[[1,1],[6,1],[6,6],[1,6],[1,1]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[7,1],[12,1],[12,6],[7,6],[7,1]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.poly([[[-1,0],[-6,0],[-6,5],[-1,5],[-1,0]]]) #membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan
w.close() #penutup

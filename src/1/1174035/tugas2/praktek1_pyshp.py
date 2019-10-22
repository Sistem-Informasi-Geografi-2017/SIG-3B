import shapefile #Impor pyshp buat bisa dipake

w=shapefile.Writer('soal1.shp') #Inisiasi Parameter untuk menulis file SHP. Parameter 1 menuliskan nama file yang akan di save. File yang ditulis yaitu "soal1".
w.shapeType #Pengecekan tipe dari shapefile
w.field("kolom1", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom1" dan tipe datanya string
w.field("kolom2", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom2" dan tipe datanya string
w.record("ngek", "satu") #Mengisi kolom 1 dan 2 untuk baris pertama, untuk kolom pertama berisi ngek dan kolom kedua berisi satu
w.record("ngok", "dua") #Mengisi kolom 1 dan 2 untuk baris kedua, untuk kolom pertama berisi ngok dan kolom kedua berisi dua
w.point(1,1) #Setting shape pertama dengan koordinat 1,1 dan tipe bentuk yaitu point
w.point(2,2) #Setting shape kedua dengan koordinat 2,2 dan tipe bentuk yaitu point
w.close() #Menutup pembuatan shapefile
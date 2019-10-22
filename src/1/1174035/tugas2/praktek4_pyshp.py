import shapefile #Impor pyshp buat bisa dipake
w = shapefile.Writer("soal4", shapeType=shapefile.POINTM) #Inisiasi Parameter untuk menulis file SHP. Parameter 1 menuliskan nama file yang akan di save. file yang ditulis yaitu "soal4" dan parameter 2 menentukan tipe bentuk yang akan dibuat/dibangun. Bentuk yang dibangun adalah bentuk pointm.
print(w.shapeType) #Menampilkan tipe dari shapefile
w.field("kolom1", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom1" dan tipe datanya string
w.field("kolom2", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom2" dan tipe datanya string
w.record("ngek", "satu") #Mengisi kolom 1 dan 2 untuk baris pertama, untuk kolom pertama berisi ngek dan kolom kedua berisi satu
w.record("ngok", "dua") #Mengisi kolom 1 dan 2 untuk baris kedua, untuk kolom pertama berisi ngok dan kolom kedua berisi dua
w.pointm(1,1) #Setting shape pertama dengan koordinat 1,1 dan tipe bentuk yaitu pointm
w.pointm(2,2) #Setting shape kedua dengan koordinat 2,2 dan tipe bentuk yaitu pointm
w.close() #Menutup pembuatan shapefile
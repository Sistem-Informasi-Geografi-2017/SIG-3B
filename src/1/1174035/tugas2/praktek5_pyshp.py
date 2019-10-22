import shapefile #Impor pyshp buat bisa dipake
w=shapefile.Writer("soal5") #Inisiasi Parameter untuk menulis file SHP. Parameter 1 menuliskan nama file yang akan di save. file yang ditulis yaitu "soal5"
print(w.shapeType) #Menampilkan tipe dari shapefile
w.field("kolom1", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom1" dan tipe datanya string
w.field("kolom2", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom2" dan tipe datanya string
w.record("ngek", "satu") #Mengisi kolom 1 dan 2 untuk baris pertama, untuk kolom pertama berisi ngek dan kolom kedua berisi satu
w.poly([[[1,5], [5,5], [5,1], [3,3], [1,1]]]) #Setting shape pertama untuk mensetting tipe bentuk polygon
w.close() #Menutup pembuatan shapefile
import shapefile #Impor pyshp buat bisa dipake
w=shapefile.Writer('soal_10', shapeType=shapefile.POLYGON) #Inisiasi Parameter untuk menulis file SHP. Parameter 1 menuliskan nama file yang akan di save. file yang ditulis yaitu "soal10". parameter 2 akan menginisiasi tipe bentuk yang akan dibangun. Tipe yang dibentuk yaitu polygon.
print(w.shapeType) #Menampilkan tipe dari shapefile
w.field("kolom1", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom1" dan tipe datanya string
w.field("kolom2", "C") #Setting kolom untuk simpan data di database shape. Judul kolom yang disetting yaitu "kolom2" dan tipe datanya string
w.record("ngek", "satu") #Mengisi kolom 1 dan 2 untuk baris pertama, untuk kolom pertama berisi ngek dan kolom kedua berisi satu
w.record("ngok", "dua") #Mengisi kolom 1 dan 2 untuk baris kedua, untuk kolom pertama berisi ngok dan kolom kedua berisi dua
w.record("ngik", "tiga") #Mengisi kolom 1 dan 2 untuk baris ketiga, untuk kolom pertama berisi ngik dan kolom kedua berisi tiga
w.poly([[[8,3], [10,3], [10,6], [8,6], [8,3]]]) #Setting shape pertama untuk mensetting tipe bentuk polygon
w.poly([[[8+4,3], [10+4,3], [10+4,6], [8+4,6], [8+4,3]]]) #Setting shape kedua untuk mensetting tipe bentuk polygon
w.poly([[[8+8,3], [10+8,3], [10+8,6], [8+8,6], [8+8,3]]]) #Setting shape ketiga untuk mensetting tipe bentuk polygon
w.close() #Menutup pembuatan shapefile
import shapefile # import library shapefile
w = shapefile.Writer('soal10', shapeType=5)  # menggunakan fungsi writer yang digunakan untuk menggambar dan akan dinamakan no10 dalam bentuk shapetype=5 yang merupakan sebuah polygon
  
w.field("kolom1","C")  # Digunakan untuk membuat kolom pertama pada table
w.field("kolom2","C")  # Digunakan untuk membuat kolom dua pada table
 
w.record("HESOYAM ","Cheat darah + uang") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("BAGUVIX ","Cheat kebal") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("CVWKXAM ","Cheat menyelam") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("ANOSEONGLASS ","Cheat Matrix") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("FULLCLIP ","Cheat ammo") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("BUFFMEUP ","Cheat otot") # mengisi kolum yang sudah dibuat dengan ngek dan satu





w.poly([[[1,1],[3,1],[3,3],[1,1]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[5,1],[7,1],[5,3],[5,1]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[9,1],[11,1],[9,3],[9,1]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[13,1],[15,1],[13,3],[13,1]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[1,5],[1,7],[3,5],[1,5]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[1,9],[1,11],[3,9],[1,9]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut 


w.close() # Menutup writer
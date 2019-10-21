import shapefile #mengimpor modul shapefile
w=shapefile.Writer(shapeType=1) #Instansiasi writer method
w.shapeType #menggunakan jenis shape apa
w.shapeType=3 #mengunakan tipe shape 3
w.shapeType #menentukan shape jenis apa yang digunakan

w.field("kolom1","C") #membuat field dengan nama (kolom1 dengan type character)
w.field("kolom2","C") #membuat field dengan nama (kolom1 dengan type character)

w.record("ngek","satu") #membuat record pada kedua kolom yang sudahd dibuat dengan isi "ngek","satu"
w.record("ngok","dua") #membuat record pada kedua kolom yang sudahd dibuat dengan isi "ngok","dua"

w.point(1,1) #membuat ESRI dengan type point
w.point(2,2) #membuat ESRI dengan type point

w.save("soal3") #menyimpan file shape dengan nama soal3

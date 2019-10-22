import shapefile #import kelas shapefile
sibin = shapefile.Writer('soal4', shapefile.POINT) #buat nama file 'soal4' dan menggunakan shapefile.POINT
sibin.shapeType

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak
sibin.record("hiyok","dua") #membuat isi tabel hiyok

sibin.point(1,1) #titik di poin x dan y
sibin.point(2,2) #titik di poin x dan y

sibin.close() #mengakhiri kode
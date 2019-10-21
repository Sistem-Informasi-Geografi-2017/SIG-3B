import shapefile #import kelas shapefile
sibin = shapefile.Writer('soal9', shapeType=5) #buat nama file 'soal9' dan menggunakan shapeType=5

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak
sibin.record("hiyok","dua") #membuat isi tabel hiyok

sibin.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]]) #buat garis
sibin.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]]) #buat garis

sibin.close() #mengakhiri kode
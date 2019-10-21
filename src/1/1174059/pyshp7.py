import shapefile #import kelas shapefile
sibin = shapefile.Writer('soal7', shapeType=5) #buat nama file 'soal7' dan menggunakan shapeType=5

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak

sibin.poly([[[1,3],[5,3],[1,2],[5,2]]]) #buat garis

sibin.close() #mengakhiri kode
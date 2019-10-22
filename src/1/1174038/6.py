import shapefile #import kelas shapefile
sibin = shapefile.Writer('soal6', shapeType=5) #buat nama file 'soal6' dan menggunakan shapeType=5

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak

sibin.poly([[[2,3],[1,3]]]) #buat garis

sibin.close() #mengakhiri kode
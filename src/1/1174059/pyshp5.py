import shapefile #import kelas shapefile
sibin = shapefile.Writer('soal5', shapeType=3) #buat nama file 'ininamafile5' dan menggunakan shapeType=3

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak

sibin.line([[[1,1],[2,2],[1,2],[3,3],[2,3]]]) #buat garis

sibin.close() #mengakhiri kode
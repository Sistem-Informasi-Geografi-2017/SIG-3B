import shapefile #import kelas shapefile
sibin = shapefile.Writer('ininamafile10', shapeType=5) #buat nama file 'ininamafile10' dan menggunakan shapeType=5

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak
sibin.record("hiyok","dua") #membuat isi tabel hiyok
sibin.record("hayuk","tiga") #membuat isi tabel hayuk
sibin.record("hayik","empat") #membuat isi tabel hayik
sibin.record("heyok","lima") #membuat isi tabel heyok

sibin.poly([[[1,1],[4,1],[4,3],[1,3],[1,1]]]) #buat persegipanjang
sibin.poly([[[1,5],[4,5],[4,7],[1,7],[1,5]]]) #buat persegipanjang
sibin.poly([[[6,1],[9,1],[9,3],[6,3],[6,1]]]) #buat persegipanjang
sibin.poly([[[6,5],[9,5],[9,7],[6,7],[6,5]]]) #buat persegipanjang
sibin.poly([[[11,1],[14,1],[14,3],[11,3],[11,1]]]) #buat persegipanjang

sibin.close() #mengakhiri kode
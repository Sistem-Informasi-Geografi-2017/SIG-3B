import shapefile #mengimport shapefile
w=shapefile.Writer('Soal4', shapeType=shapefile.POINTM) #membuat file bernama Soal4 dan mendifinisikan shapetypenya yaitu POINTM
w.shapeType #mendeklarasikan(memanggil) shape type
w.field("kolom1","C") #membuat field pertama 
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu") #membuat record pertama
w.record("ngok","dua") #membuat record kedua
w.pointm(1,1) #membuat point pertama denan titik x dan y
w.pointm(2,2) #membuat point kedua denan titik x dan y
w.close() #menghentikan perintah
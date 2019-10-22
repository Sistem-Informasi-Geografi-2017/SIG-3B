import shapefile  #mengimport shapefile
w=shapefile.Writer('Soal9', shapeType=shapefile.POLYGON) #membuat file bernama Soal9 dan mendifinisikan shapetypenya yaitu POLYGON
w.shapeType #mendeklarasikan(memanggil) shape type
w.field("kolom1","C") #membuat field pertama 
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu") #membuat record pertama
w.record("crot","dua") #membuat record kedua
w.poly([[[1,3],[5,3],[5,2],[1,2],[1,3]]]) #memmbuat polygon pertama
w.poly([[[1,6],[5,6],[5,9],[1,9],[1,6]]]) #memmbuat polygon kedua
w.close() #menghentikan perintah
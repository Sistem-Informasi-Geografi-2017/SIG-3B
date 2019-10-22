import shapefile #mengimport shapefile
w=shapefile.Writer('Soal5', shapeType=shapefile.POLYLINE) #membuat file bernama Soal5 dan mendifinisikan shapetypenya yaitu POLYLINE
w.shapeType  #mendeklarasikan(memanggil) shape type
w.field("kolom1","C") #membuat field pertama
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu") #membuat record pertama
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat line pertama
w.close() #menghentikan perintah
import shapefile #mengimport shapefile
w=shapefile.Writer('SoalMod', shapeType=shapefile.POLYGON) #membuat file bernama SoalMod dan mendifinisikan shapetypenya yaitu POLYGON
w.shapeType #mendeklarasikan(memanggil) shape type
w.field("kolom1","C") #membuat field pertama 
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu") #membuat record pertama
w.record("baaa","dua") #membuat record kedua
w.record("bii","tiga") #membuat record ketiga
w.record("buu","empat") #membuat record keempat
w.poly([[[2,7],[4,7],[3,10],[3,10],[2,7]]]) #memmbuat polygon pertama
w.poly([[[2,3],[4,3],[3,6],[3,6],[2,3]]]) #memmbuat polygon kedua
w.poly([[[5,3],[7,3],[6,6],[6,6],[5,3]]]) #memmbuat polygon ketiga
w.poly([[[5,7],[7,7],[6,10],[6,10],[5,7]]]) #memmbuat polygon keempat
w.close()  #menghentikan perintah
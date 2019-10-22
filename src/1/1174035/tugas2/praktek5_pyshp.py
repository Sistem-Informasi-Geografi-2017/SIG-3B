import shapefile
w=shapefile.Writer("soal5")
print(w.shapeType)
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.poly([[[1,5], [5,5], [5,1], [3,3], [1,1]]])
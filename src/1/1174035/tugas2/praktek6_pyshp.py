import shapefile
w=shapefile.Writer("soal6")
print(w.shapeType)
shapeType=shapefile.POLYGON
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.poly([[[1,3],[5,3]]])
w.close()
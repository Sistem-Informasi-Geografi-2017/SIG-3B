import shapefile
w=shapefile.Writer('SoalMod', shapeType=shapefile.POLYGON)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.poly([[[2,3],[4,3],[3,6],[3,6],[2,3]]])
w.close()
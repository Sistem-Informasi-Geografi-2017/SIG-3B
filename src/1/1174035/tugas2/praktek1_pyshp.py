import shapefile

w=shapefile.Writer('soal1.shp')
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("ngek", "satu")
w.record("ngek", "dua")

w.point(1,1)
w.point(2,2)
w.close()
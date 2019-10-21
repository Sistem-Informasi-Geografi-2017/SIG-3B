import shapefile #mengimpor modul shapefile
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)

#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bangun","bangun ke ") 
w.field("Nama Bangun","bangun ke") 
 
w.record("belah ketupat","satu") #membuat record dengan isi kolom 1 "belah ketupat" dan kolom dua "satu"
w.record("belah ketupat","dua") #membuat record dengan isi kolom 2 "belah ketupat" dan kolom dua "dua"
w.record("belah ketupat","tiga")#membuat record dengan isi kolom 3 "belah ketupat" dan kolom dua "tiga"
w.record("belah ketupat","empat")#membuat record dengan isi kolom 4 "belah ketupat" dan kolom dua "empat"
w.record("belah ketupat","lima")#membuat record dengan isi kolom 5 "belah ketupat" dan kolom dua "lima"
#membuat 5 row karena menggunakan 5 record
w.poly(parts=[[[-6,4],[-4,6], [-2,4],[-4,2],[-6,4]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point yang sesuai, dengan type polygon
w.poly(parts=[[[2,4],[4,6],[6,4],[4,2],[2,4]]],shapeType=shapefile.POLYGON)  #mengisi .shp dengan titik point yang sesuai, dengan type polygon
w.poly(parts=[[[2,-4],[4,-2],[6,-4],[4,-6],[2,-4]]],shapeType=shapefile.POLYGON)  #mengisi .shp dengan titik point yang sesuai, dengan type polygon
w.poly(parts=[[[-6,-4],[-4,-2],[-2,-4],[-4,-6],[-6,-4]]],shapeType=shapefile.POLYGON)  #mengisi .shp dengan titik point yang sesuai, dengan type polygon
w.poly(parts=[[[-6,-13],[-4,-11],[-2,-13],[-4,-15],[-6,-13]]],shapeType=shapefile.POLYGON)  #mengisi .shp dengan titik point yang sesuai, dengan type polygon

w.save("soal10")#melakukan save dengan nama (soal10)
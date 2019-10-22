import shapefile #mengimpor modul shapefile
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)

#mem#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bangun","Smash") 
w.field("Nama Bangun","Smash") 
 
w.record("Segitiga siku-siku","Bisma") #membuat record dengan isi kolom 1 "Segitiga siku-siku" dan kolom dua "satu"
w.record("Segitiga siku-siku","Rafael") #membuat record dengan isi kolom 2 "Segitiga siku-siku" dan kolom dua "dua"
w.record("Segitiga siku-siku","Rangga")#membuat record dengan isi kolom 3 "Segitiga siku-siku" dan kolom dua "tiga"
w.record("Segitiga siku-siku","Reza")#membuat record dengan isi kolom 4 "Segitiga siku-siku" dan kolom dua "empat"
w.record("Segitiga siku-siku","Ilham")#membuat record dengan isi kolom 5 "Segitiga siku-siku" dan kolom dua "lima"
#membuat 5 row karena menggunakan 5 record
w.poly(parts=[[[-6,4],[-4,6], [-2,4],[-4,2],[-6,4]]],shapeType=shapefile.POLYGON) #membuat polygon
w.poly(parts=[[[2,4],[4,6],[6,4],[4,2],[2,4]]],shapeType=shapefile.POLYGON)  #membuat polygon
w.poly(parts=[[[2,-4],[4,-2],[6,-4],[4,-6],[2,-4]]],shapeType=shapefile.POLYGON)  #membuat polygon
w.poly(parts=[[[-6,-4],[-4,-2],[-2,-4],[-4,-6],[-6,-4]]],shapeType=shapefile.POLYGON)  #membuat polygon
w.poly(parts=[[[-6,-13],[-4,-11],[-2,-13],[-4,-15],[-6,-13]]],shapeType=shapefile.POLYGON)  #membuat polygon

w.save("soal10")#melakukan save dengan nama (soal10)
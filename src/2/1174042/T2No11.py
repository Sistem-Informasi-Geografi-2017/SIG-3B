import shapefile #Import modul shapefile
sf = shapefile.Reader("soal9") #membaca soal9
isidata = sf.records()#isi dari setiap kolom
print(isidata[0])#isi dari kolom ke 1 & 2
print(isidata[0][1]) #isi dari kolom ke 1 field ke2

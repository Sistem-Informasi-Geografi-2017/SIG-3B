import shapefile #Import modul shapefile
sf = shapefile.Reader("soal8") #membaca soal8
print(sf.bbox) #berguna untuk melihat titik titik

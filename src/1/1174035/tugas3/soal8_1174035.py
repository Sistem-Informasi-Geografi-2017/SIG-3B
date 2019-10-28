import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
anu = sf.shapes() #Memanggil semua shapes yang telah dibaca dan mengkonversinya dengan bentuk array yang dapat dipanggil oleh index
print(anu[0].points) #Akan menampilkan kumpulan koordinat pada shape pertama / index 0
sf.close() #Menutup reader pyshp
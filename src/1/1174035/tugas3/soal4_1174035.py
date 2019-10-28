import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
anu = sf.shapes() #Memanggil semua shapes yang telah dibaca dan mengkonversinya dengan bentuk array yang dapat dipanggil oleh index
print(len(anu)) #Mengetahui berapa banyak shapes
sf.close() #Menutup reader pyshp
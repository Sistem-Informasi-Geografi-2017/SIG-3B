import shapefile #Mengimport library shapefile
sf = shapefile.Reader("sample") #menginisiasi variable sf, memanggil fungsi untuk membaca file PYSHP dengan nama sample
anu = sf.shapes() #Memanggil semua shapes yang telah dibaca dan mengkonversinya dengan bentuk array yang dapat dipanggil oleh index
print(anu[0].shapeType) #Mengidentifikasi bentuk dari shape ke 1 yang dibuat pada file sample
sf.close() #Menutup reader pyshp
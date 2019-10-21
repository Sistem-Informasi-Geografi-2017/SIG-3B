import shapefile #Berfungsi untuk mengimport library shapefile
w = shapefile.Writer("Nomor10", shapeType=5) #membuat writer dengan nama nomor10 yang dimana bentuknya adalah shapetype =5

w.field("Te","C") # Membuat table kolom pertama
w.field("Dy","C") # Membuat table kolom kedua

w.record("LeeJongSuk","JiChangWook") #Membuat isi table pada kolom pertama
w.record("LeeSeungGi","LeeMinHoo") #Membuat isi table pada kolom kedua
w.record("YooSeungHoo","ParkSooHyun") #Membuat isi table pada kolom ketiga


w.poly([[[-6,2],[3,-2],[5,3],[-4,3],[-6,2]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[2,3],[5,3],[6,1],[1,1],[2,3]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-3,2],[-3,5],[-1,6],[-1,1],[-3,2]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Untuk menutup Writer
# Inputan dari user
# artimatika

# Belajar Inputan
ivan = input("masukan kata : ")
#print ("isi dari ivan :", ivan,bertipe data" :", type ivan)

# Belajar aritmatika dasar
x = 3
y = 4

# penjumlahan +
hasil = x + y
print ("x - y =",hasil )

#pengurangan
hasil = x - y
print ("x - y =", hasil )

#perkalian *
hasil = x * y
print ("x * y =" ,hasil)

#pembagian /
hasil = x / y
print ("x : y =", hasil )

# perperangkatan exponen **
hasil = x ** y
print ("x mod y =",hasil )

# modulus %
hasil = y % x 
print ("x mod y=",hasil )

# floor division (pembulatan kebawah) //
hasil = x // y
print ("x // y =",hasil )

# aritmatika prioritas
# (), exponen, perkalian/pembagian, penjumlahan/pengurangan
x = 3
y = 4
z = 5

hasil = ( x ** y * (z + y) / y - z % x // y )
print(hasil)
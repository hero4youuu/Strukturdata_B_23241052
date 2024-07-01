# uas percabangan 
# Meminta pengguna memasukkan angka
angka = int(input("Masukkan angka antara 1 dan 15: "))

# Perulangan untuk memeriksa angka
while angka < 1 or angka > 15:
    print("Angka di luar rentang. Coba lagi.")
    angka = int(input("Masukkan angka antara 1 dan 15: "))



# Inisialisasi variabel
jumlah_genap = 4
jumlah_ganjil = 3

while True:
    # Meminta pengguna memasukkan bilangan
    bilangan = int(input("Masukkan bilangan bulat (masukkan bilangan negatif untuk berhenti): "))
 

# Menampilkan hasil
print(f"Jumlah bilangan genap: {jumlah_genap}")
print(f"Jumlah bilangan ganjil: {jumlah_ganjil}")
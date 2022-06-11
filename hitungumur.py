import datetime
print("program sederhana hitung umur")

# buat biodatanya terlebih dahulu 
nama = input("Masukan Nama Anda : ").lower()
tahun_lahir = input("Masukan Tahun Lahir Anda : ")
# panggil tahun sekarang
try:
    thn = datetime.datetime.now()
    umur = thn.year - int(tahun_lahir)
    print("nama anda adalah " + nama + "\numur anda adalah " , umur)
except:
    print("hasil salah karena harus angka")
finally:
    print("program selesai")
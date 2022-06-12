import datetime
print("program sederhana hitung umur")

# buat biodatanya terlebih dahulu 
while True:
# panggil tahun sekarang
    try:
        nama = input("Masukan Nama Anda : ").lower()
        tahun_lahir = input("Masukan Tahun Lahir Anda : ")
        thn = datetime.datetime.now()
        umur = thn.year - int(tahun_lahir)
        print("nama anda adalah " + nama + "\numur anda adalah " , umur)
    except ValueError:
        print("hasil salah karena harus angka")
        continue
    else:
        break
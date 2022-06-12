import datetime
print("program sederhana hitung tahun lahir")

while True:
    try:
        # buat biodatanya terlebih dahulu 
        nama = input("Masukan Nama Anda : ").lower()
        umur_anda = input("Masukan Umur Anda : ")
        # panggil tahun sekarang
        thn = datetime.datetime.now()
        umur = thn.year - int(umur_anda)
        print("nama anda adalah " + nama + "\ntahun lahir anda adalah " , umur)
    except:
        print("hasil salah karena harus angka")
        continue
    else:
        break
    # finally:
    #     print("program selesai")
    #     break
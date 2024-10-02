def cek_sisi_segita(sisi1, sisi2, sisi3):
    if sisi1 == sisi2 == sisi3:
        return "3 sisi sama"
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        return "2 sisi sama"
    else:
        return "Tidak ada yang sama"

# Meminta pengguna memasukkan tiga sisi
try:
    sisi1 = float(input("Masukkan sisi 1: "))
    sisi2 = float(input("Masukkan sisi 2: "))
    sisi3 = float(input("Masukkan sisi 3: "))

    # Memanggil fungsi dan menampilkan hasil
    hasil = cek_sisi_segita(sisi1, sisi2, sisi3)
    print(hasil)
except ValueError:
    print("Input harus berupa angka yang valid.")

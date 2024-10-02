def jumlah_hari_bulan (bulan): 
    # Daftar jumlah hari untuk setiap bulan di tahun 2020
    hari_per_bulan = {
            1: 31,  # Januari
            2: 29,  # Februari (tahun kabisat)
            3: 31,  # Maret
            4: 30,  # April
            5: 31,  # Mei
            6: 30,  # Juni
            7: 31,  # Juli
            8: 31,  # Agustus
            9: 30,  # September
            10: 31, # Oktober
            11: 30, # November
            12: 31  # Desember
        }
    
    if bulan < 1 or bulan > 12:
        print("Bulan yang diinputkan tidak valid. Silakan masukkan angka antara 1 hingga 12.")
    else:
        print(f" Jumlah hari: {hari_per_bulan[bulan]} hari")
    
#meminta input dari pengguna
try:
    bulan = int(input("Masukkan bulan (1-12): "))
    jumlah_hari_bulan(bulan)
except ValueError:
    print("Input harus berupa angka.")
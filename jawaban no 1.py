class Hotel:
    JENIS_KAMAR = {
        'M': ('Melati', 650000),
        'S': ('Sakura', 550000),
        'L': ('Lily', 400000),
        'A': ('Anggrek', 350000)
    }

    @staticmethod
    def hitung_total(durasi_sewa, harga_kamar):
        total = durasi_sewa * harga_kamar
        diskon = 0
        jika durasi_sewa > 5:
            diskon = total * 0.10
        elif durasi_sewa > 3:
            diskon = total * 0.05
        kembali total - diskon, diskon

def main():
    petugas = input("Masukkan Nama Petugas: ")
    pelanggan = input("Masukkan Nama Pelanggan: ")
    check_in = input("Masukkan Tanggal Check-in (YYYY-MM-DD): ")
    kode_kamar = input("Pilih Kode Kamar [M/S/L/A]: ").upper()
    durasi_sewa = int(input("Masukkan Lama Sewa: "))
    jumlah_bayar = int(input("Masukkan Uang Bayar: "))

    jika kode_kamar di Hotel.JENIS_KAMAR:
        nama_kamar, harga_kamar = Hotel.JENIS_KAMAR[kode_kamar]
        total_bayar, diskon = Hotel.hitung_total(durasi_sewa, harga_kamar)
        kembalian = jumlah_bayar - total_bayar

        print("\nBukti Pemesanan Kamar")
        print("Hotel SEJUK ASRI")
        print("===================")
        print(f"Nama Petugas: {petugas}")
        print(f"Nama Pelanggan: {pelanggan}")
        print(f"Tanggal Check-in: {check_in}")
        print("===================")
        print(f"Nama Kamar Yang dipesan: {nama_kamar}")
        print(f"Harga sewa permalam: Rp. {harga_kamar}")
        print(f"Lama sewa: {durasi_sewa} malam")
        print(f"Diskon: Rp. {diskon}")
        print(f"Jumlah Bayar: Rp. {durasi_sewa * harga_kamar}")
        print(f"Total Bayar: Rp. {total_bayar}")
        print(f"Uang Bayar: Rp. {jumlah_bayar}")
        print(f"Uang Kembali: Rp. {kembalian}")
    else:
        print("Kode kamar tidak valid")

if __name__ == "__main__":
    main()

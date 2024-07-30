class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Inventori:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self):
        nama = input("Masukkan Nama Barang: ")
        harga = int(input("Masukkan Harga Barang: "))
        stok = int(input("Masukkan Stok Barang: "))
        barang = Barang(nama, harga, stok)
        self.daftar_barang.append(barang)

    def tampilkan_barang(self):
        print("\nData Barang:")
        untuk idx, barang dalam enumerate(self.daftar_barang):
            print(f"{idx+1}. {barang.nama} - Harga: Rp {barang.harga} - Stok: {barang.stok}")

    def hapus_barang(self):
        self.tampilkan_barang()
        idx = int(input("Masukkan nomor barang yang akan dihapus: ")) - 1
        jika 0 <= idx < len(self.daftar_barang):
            del self.daftar_barang[idx]
        else:
            print("Nomor barang tidak valid")

    def cari_barang(self):
        nama = input("Masukkan nama barang yang dicari: ")
        untuk barang dalam self.daftar_barang:
            jika barang.nama.lower() == nama.lower():
                print(f"{barang.nama} - Harga: Rp {barang.harga} - Stok: {barang.stok}")
                kembali
        print("Barang tidak ditemukan")

    def hitung_pembelian(self):
        self.tampilkan_barang()
        idx = int(input("Masukkan nomor barang yang dibeli: ")) - 1
        jika 0 <= idx < len(self.daftar_barang):
            jumlah = int(input("Masukkan jumlah yang dibeli: "))
            jika jumlah <= self.daftar_barang[idx].stok:
                total = jumlah * self.daftar_barang[idx].harga
                self.daftar_barang[idx].stok -= jumlah
                print(f"Total pembelian: Rp {total}")
            else:
                print("Stok tidak mencukupi")
        else:
            print("Nomor barang tidak valid")

def menu_utama():
    inventori = Inventori()
    sementara benar:
        print("\nMenu:")
        print("1. Input Data Barang")
        print("2. Tampil Data Barang")
        print("3. Delete Data Barang")
        print("4. Cari Data Barang")
        print("5. Hitung Jumlah Pembelian")
        print("6. Keluar")
        pilihan = int(input("Pilih menu (1-6): "))
        jika pilihan == 1:
            inventori.tambah_barang()
        elif pilihan == 2:
            inventori.tampilkan_barang()
        elif pilihan == 3:
            inventori.hapus_barang()
        elif pilihan == 4:
            inventori.cari_barang()
        elif pilihan == 5:
            inventori.hitung_pembelian()
        elif pilihan == 6:
            istirahat
        lain:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    menu_utama()

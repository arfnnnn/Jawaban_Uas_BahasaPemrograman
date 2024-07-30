class BangunDatar:
    def luas(self):
        pass
    
    def keliling(self):
        pass

class SegiEmpat(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi, sisi_miring):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi_miring = sisi_miring

    def luas(self):
        return 0.5 * self.alas * self.tinggi

    def keliling(self):
        return self.alas + self.tinggi + self.sisi_miring

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari * self.jari_jari

    def keliling(self):
        return 2 * 3.14 * self.jari_jari

def main():
    print("Menu Perhitungan Bangun Datar")
    print("1. Segi Empat")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    pilihan = int(input("Pilih bangun datar (1-4): "))
    
    jika pilihan == 1:
        sisi = float(input("Masukkan sisi segi empat: "))
        bangun_datar = SegiEmpat(sisi)
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        bangun_datar = PersegiPanjang(panjang, lebar)
    elif pilihan == 3:
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_miring = float(input("Masukkan sisi miring: "))
        bangun_datar = Segitiga(alas, tinggi, sisi_miring)
    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        bangun_datar = Lingkaran(jari_jari)
    else:
        print("Pilihan tidak valid")
        kembali

    print(f"Luas: {bangun_datar.luas()}")
    print(f"Keliling: {bangun_datar.keliling()}")

if __name__ == "__main__":
    main()

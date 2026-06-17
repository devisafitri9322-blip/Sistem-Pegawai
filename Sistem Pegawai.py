class Pegawai:
    def __init__(self, nama, umur, gajiPokok, kinerja):
        self.nama = nama
        self.umur = umur
        self.gajiPokok = gajiPokok
        self.kinerja = kinerja

    def hitungTunjangan(self):
        if self.kinerja == 100:
            return self.gajiPokok * 0.20
        elif self.kinerja == 90:
            return self.gajiPokok * 0.15
        elif self.kinerja == 80:
            return self.gajiPokok * 0.10
        else:
            return 0

    def hitungGaji(self):
        return self.gajiPokok + self.hitungTunjangan()

    def info(self):
        print(f"Nama              : {self.nama}")
        print(f"Umur              : {self.umur} tahun")
        print(f"Gaji Pokok        : Rp {self.gajiPokok:,}")
        print(f"Kinerja           : {self.kinerja}")
        print(f"Tunjangan_bonus   : Rp {self.hitungTunjangan():,}")
        print(f"Total Gaji        : Rp {self.hitungGaji():,}")


class Dosen(Pegawai):
    def __init__(self, nama, umur, gajiPokok, kinerja, mataKuliah):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.mataKuliah = mataKuliah

    def info(self):
        print("=== DATA DOSEN ===")
        super().info()
        print(f"Mata Kuliah : {self.mataKuliah}")
        print("-" * 30)


class Staff(Pegawai):
    def __init__(self, nama, umur, gajiPokok, kinerja, divisi):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.divisi = divisi

    def info(self):
        print("=== DATA STAFF ===")
        super().info()
        print(f"Divisi      : {self.divisi}")
        print("-" * 30)


class Satpam(Pegawai):
    def __init__(self, nama, umur, gajiPokok, kinerja, shift):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.shift = shift

    def info(self):
        print("=== DATA SATPAM ===")
        super().info()
        print(f"Shift       : {self.shift}")
        print("-" * 30)


dosen1 = Dosen("Bayuu", 22, 5000000, 100, "Pemrograman Python")
staff1 = Staff("Budi", 30, 5000000, 90, "IT")
satpam1 = Satpam("Agus", 25, 5000000, 80, "Malam")

dosen1.info()
staff1.info()
satpam1.info()

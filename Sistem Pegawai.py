class Pegawai:
    def __init__(self, nama, umur, gajiPokok):
        self.nama = nama
        self.umur = umur
        self.gajiPokok = gajiPokok

    def hitungGaji(self):
        return self.gajiPokok

    def info(self):
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur} tahun")
        print(f"Gaji Pokok  : Rp {self.gajiPokok:,}")
        print(f"Total Gaji  : Rp {self.hitungGaji():,}")

class Dosen(Pegawai):
    def __init__(self, nama, umur, gajiPokok, mataKuliah):
        super().__init__(nama, umur, gajiPokok)
        self.mataKuliah = mataKuliah

    def hitungGaji(self):
        return self.gajiPokok

    def info(self):
        print("=== DATA DOSEN ===")
        super().info()
        print(f"Mata Kuliah : {self.mataKuliah}")
        print("-" * 30)

class Staff(Pegawai):
    def __init__(self, nama, umur, gajiPokok, divisi):
        super().__init__(nama, umur, gajiPokok)
        self.divisi = divisi

    def hitungGaji(self):
        return self.gajiPokok

    def info(self):
        print("=== DATA STAFF ===")
        super().info()
        print(f"Divisi      : {self.divisi}")
        print("-" * 30)

class Satpam(Pegawai):
    def __init__(self, nama, umur, gajiPokok, shift):
        super().__init__(nama, umur, gajiPokok)
        self.shift = shift

    def hitungGaji(self):
        return self.gajiPokok

    def info(self):
        print("=== DATA SATPAM ===")
        super().info()
        print(f"Shift       : {self.shift}")
        print("-" * 30)

dosen1 = Dosen("Bayuu", 22, 5000000, "Pemrograman Python")
staff1 = Staff("Budi", 30, 5000000, "IT")
satpam1 = Satpam("Bapak Budi Kopling", 25, 5000000, "Malam")

dosen1.info()
staff1.info()
satpam1.info()
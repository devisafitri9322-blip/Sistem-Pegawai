class pegawai:
    def __init__(self, nama, umur, gajiPokok, kinerja):
        self.nama = nama
        self.umur = umur
        self.gajiPokok = gajiPokok
        self.kinerja = kinerja
 
    def hitungGaji(self):
        if self.kinerja == "100%":
            bonus = 0.2 * self.gajiPokok
        elif self.kinerja == "90%":
            bonus = 0.15 * self.gajiPokok
        elif self.kinerja == "80%":
            bonus = 0.1 * self.gajiPokok
        else:
            bonus = 0
        return self.gajiPokok + bonus
 
    def tampilkanInfo(self):
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur} tahun")
        print(f"Kinerja     : {self.kinerja}")
        print(f"Gaji Pokok  : Rp {self.gajiPokok:,}")
        print(f"Total Gaji  : Rp {self.hitungGaji():,.0f}") 
        print("-" * 30)
class Dosen(pegawai):
    def __init__(self, nama, umur, gajiPokok, mataKuliah, kinerja):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.mataKuliah = mataKuliah
 
    def hitungGaji(self):
        return self.gajiPokok * (1 + self.kinerja / 100)
 
    def tampilkanInfo(self):
        print("=== DATA DOSEN ===")
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur} tahun")
        print(f"Kinerja     : {self.kinerja}")
        print(f"Gaji Pokok  : Rp {self.gajiPokok:,}")
        print(f"Mata Kuliah : {self.mataKuliah}")
        print(f"Total Gaji  : Rp {self.hitungGaji():,.0f}")
        print("-" * 30)

class Staff(pegawai):
    def __init__(self, nama, umur, gajiPokok, divisi, kinerja):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.divisi = divisi
 
    def hitungGaji(self):
        return self.gajiPokok * (1 + self.kinerja / 100)
 
    def tampilkanInfo(self):
        print("=== DATA STAFF ===")
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur} tahun")
        print(f"Kinerja     : {self.kinerja}")
        print(f"Gaji Pokok  : Rp {self.gajiPokok:,}")
        print(f"Divisi      : {self.divisi}")
        print(f"Total Gaji  : Rp {self.hitungGaji():,.0f}")
        print("-" * 30)

class Satpam(pegawai):
    def __init__(self, nama, umur, gajiPokok, shift, kinerja):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.shift = shift
 
    def hitungGaji(self):
        return self.gajiPokok * (1 + self.kinerja / 100)
 
    def tampilkanInfo(self):
        print("=== DATA SATPAM ===")
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur} tahun")
        print(f"Kinerja     : {self.kinerja}")
        print(f"Gaji Pokok  : Rp {self.gajiPokok:,}")
        print(f"Shift       : {self.shift}")
        print(f"Total Gaji  : Rp {self.hitungGaji():,.0f}")
        print("-" * 30)

dosen1 = Dosen("Bayuu", 22, 5000000, "Pemrograman Python", 80)
staff1 = Staff("Budi", 30, 5000000, "IT", 90)
satpam1 = Satpam("Agus", 25, 5000000, "Malam", 100)

dosen1.tampilkanInfo()
staff1.tampilkanInfo()
satpam1.tampilkanInfo()

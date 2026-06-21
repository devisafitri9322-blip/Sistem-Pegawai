class Pegawai:
    def __init__(self, nama, umur, gajiPokok, kinerja):

        if gajiPokok < 0:
            raise ValueError("Gaji pokok tidak boleh bernilai negatif!")

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
        print(f"Tunjangan Bonus   : Rp {self.hitungTunjangan():,}")
        print(f"Total Gaji        : Rp {self.hitungGaji():,}")


class Dosen(Pegawai):
    def __init__(self, nama, umur, gajiPokok, kinerja, mataKuliah, jumlahSks):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.mataKuliah = mataKuliah
        self.jumlahSks = jumlahSks

    # Override hitungGaji()
    def hitungGaji(self):
        honorSks = self.jumlahSks * 100000
        return self.gajiPokok + self.hitungTunjangan() + honorSks

    def info(self):
        print("=== DATA DOSEN ===")
        super().info()
        print(f"Mata Kuliah       : {self.mataKuliah}")
        print(f"Jumlah SKS        : {self.jumlahSks} sks")
        print("-" * 40)

class Staff(Pegawai):
    def __init__(self, nama, umur, gajiPokok, kinerja, divisi, jamKerja):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.divisi = divisi
        self.jamKerja = jamKerja

    def hitungGaji(self):
        uangLembur = self.jamKerja * 50000
        return self.gajiPokok + self.hitungTunjangan() + uangLembur

    def info(self):
        print("=== DATA STAFF ===")
        super().info()
        print(f"Divisi            : {self.divisi}")
        print(f"Jam Kerja         : {self.jamKerja} jam")
        print("-" * 40)


class Satpam(Pegawai):
    def __init__(self, nama, umur, gajiPokok, kinerja, shift, harikerja):
        super().__init__(nama, umur, gajiPokok, kinerja)
        self.shift = shift
        self.harikerja = harikerja

    # Override hitungGaji()
    def hitungGaji(self):
        insentif = self.harikerja * 75000
        return self.gajiPokok + self.hitungTunjangan() + insentif

    def info(self):
        print("=== DATA SATPAM ===")
        super().info()
        print(f"Shift             : {self.shift}")
        print(f"Hari Kerja        : {self.harikerja} hari")
        print("-" * 40)

dosen1 = Dosen("Bayuu", 22, 5000000, 100, "Pemrograman Python", 4)
dosen2 = Dosen("Andi", 35, 6000000, 90, "Basis Data", 3)
dosen3 = Dosen("Siti", 40, 7000000, 100, "Algoritma", 5)

staff1 = Staff("Budi", 30, 5000000, 90, "IT", 8)
staff2 = Staff("Dewi", 28, 4500000, 100, "Keuangan", 8)

satpam1 = Satpam("Agus", 25, 5000000, 80, "Malam", 5)
satpam2 = Satpam("Rudi", 29, 5200000, 90, "Pagi", 6)
satpam3 = Satpam("Eko", 21, 4800000, 80, "Pagi", 6)

pegawai_list = [
    dosen1, dosen2, dosen3,
    staff1, staff2,
    satpam1, satpam2, satpam3
]

def tampilkan_semua_pegawai(daftar):
    print("\n=== DAFTAR PEGAWAI ===")
    if not daftar:
        print("Belum ada data pegawai.")
        return

    for pegawai in daftar:
        pegawai.info()

def cari_pegawai(daftar):
    nama_cari = input("\nMasukkan nama pegawai yang dicari: ").lower()

    ditemukan = False

    for pegawai in daftar:
        if pegawai.nama.lower() == nama_cari:
            print("\n=== PEGAWAI DITEMUKAN ===")
            pegawai.info()
            ditemukan = True

    if not ditemukan:
        print("Pegawai tidak ditemukan.")

def urut_gaji_terbesar(daftar):
    if not daftar:
        print("Belum ada data pegawai.")
        return

    daftar_urut = sorted(
        daftar,
        key=lambda p: p.hitungGaji(),
        reverse=True
    )

    print("\n=== URUTAN GAJI PEGAWAI TERBESAR - TERKECIL ===")
    print("-" * 40)

    for i, pegawai in enumerate(daftar_urut, start=1):
        print(f"{i}. {pegawai.nama}")
        print(f"   Jabatan    : {pegawai.__class__.__name__}")
        print(f"   Total Gaji : Rp {pegawai.hitungGaji():,.0f}")
        print("-" * 40)

def tambah_pegawai():
    print("\n=== TAMBAH PEGAWAI ===")
    print("1. Dosen")
    print("2. Staff")
    print("3. Satpam")

    pilihan = input("Pilih jenis pegawai (1-3): ")

    if pilihan not in {"1", "2", "3"}:
        print("Pilihan tidak valid.")
        return None

    nama = input("Nama: ")

    try:
        umur = int(input("Umur: "))
        gajiPokok = int(input("Gaji Pokok: "))
        kinerja = int(input("Kinerja (80/90/100): "))
    except ValueError:
        print("Input harus berupa angka.")
        return None
    
    if gajiPokok < 0:
        print("Gaji pokok tidak boleh bernilai negatif!")
        return None

    if pilihan == "1":
        mataKuliah = input("Mata Kuliah: ")

        try:
            jumlahSks = int(input("Jumlah SKS: "))
        except ValueError:
            print("Input tidak valid.")
            return None

        return Dosen(
            nama, umur, gajiPokok,
            kinerja, mataKuliah, jumlahSks
        )

    elif pilihan == "2":
        divisi = input("Divisi: ")

        try:
            jamKerja = int(input("Jam Kerja per hari: "))
        except ValueError:
            print("Input tidak valid.")
            return None

        return Staff(
            nama, umur, gajiPokok,
            kinerja, divisi, jamKerja
        )

    else:
        shift = input("Shift: ")

        try:
            harikerja = int(input("Hari Kerja: "))
        except ValueError:
            print("Input tidak valid.")
            return None

        return Satpam(
            nama, umur, gajiPokok,
            kinerja, shift, harikerja
        )

while True:
    print("\n=== MENU PEGAWAI ===")
    print("1. Tambah Pegawai")
    print("2. Tampilkan Semua Pegawai")
    print("3. Cari Pegawai")
    print("4. Ranking Gaji Pegawai")
    print("5. Keluar")

    pilihan_menu = input("Pilih menu (1-5): ")

    if pilihan_menu == "1":
        pegawai_baru = tambah_pegawai()

        if pegawai_baru:
            pegawai_list.append(pegawai_baru)
            print(f"\nPegawai {pegawai_baru.nama} berhasil ditambahkan.")

    elif pilihan_menu == "2":
        tampilkan_semua_pegawai(pegawai_list)

    elif pilihan_menu == "3":
        cari_pegawai(pegawai_list)

    elif pilihan_menu == "4":
        urut_gaji_terbesar(pegawai_list)

    elif pilihan_menu == "5":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")

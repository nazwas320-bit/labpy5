# Membuat dictionary daftar kontak
kontak = {
    "Ari": "081267888",
    "Dina": "087677776"
}

# Tampilkan kontaknya Ari
print("Kontak Ari :", kontak["Ari"])

# Tambah kontak baru Riko
kontak["Riko"] = "087654544"

# Ubah kontak Dina
kontak["Dina"] = "088999776"

# Tampilkan semua Nama
print("Semua Nama :", list(kontak.keys()))

# Tampilkan semua Nomor
print("Semua Nomor :", list(kontak.values()))

# Tampilkan daftar Nama dan Nomor
print("Daftar Kontak :")
for nama, nomor in kontak.items():
    print("-", nama, ":", nomor)

# Hapus kontak Dina
del kontak["Dina"]

# Tampilkan kontak setelah Dina dihapus
print("Kontak setelah Dina dihapus :", kontak)
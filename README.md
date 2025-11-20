## Nama : Nazwa Salsabila
## Nim  : 312510155
## Kelas : TI.25.A2
## Pertemuan : 10
## Mata Kuliah : Pengantar Pemograman

## Kode Latihan
<img width="862" height="671" alt="kode latihan" src="https://github.com/user-attachments/assets/a5a72ea7-f0b8-4e4b-b17e-84bb23d2be9f" />

## Output latihan
<img width="996" height="531" alt="output latihan" src="https://github.com/user-attachments/assets/e51d7d7f-fad8-4559-828e-f7c3f63c974e" />

## Kode Praktikum
<img width="1014" height="749" alt="kode praktikum" src="https://github.com/user-attachments/assets/8aa5e1e1-4632-4ced-86f0-91a8ec5e4ba7" />

## Output Praktikum
<img width="1231" height="846" alt="output praktikum" src="https://github.com/user-attachments/assets/dbbd6653-001e-4618-a54a-1353d95bb4d7" />

## flowchart
```
                   ┌────────────────────────┐
                   │     MULAI PROGRAM      │
                   └───────────┬────────────┘
                               │
                               ▼
                   ┌────────────────────────┐
                   │   TAMPILKAN MENU       │
                   └───────────┬────────────┘
                               │
                               ▼
                   ┌────────────────────────┐
                   │   INPUT PILIHAN MENU   │
                   └───────────┬────────────┘
             ┌─────────────────┼──────────────────┐
             ▼                 ▼                  ▼

   ┌────────────────┐   ┌────────────────┐   ┌─────────────────────┐
   │ Pilihan = 1 ?  │   │ Pilihan = 2 ?  │   │ Pilihan = 3 ?       │
   └───────┬────────┘   └───────┬────────┘   └──────────┬──────────┘
           │                    │                       │
           ▼                    ▼                       ▼

┌─────────────────────┐  ┌──────────────────────┐  ┌───────────────────────┐
│ INPUT nama, nim,    │  │ INPUT nama yang akan │  │ INPUT nama yang akan   │
│ tugas, uts, uas     │  │ diubah               │  │ dihapus                │
│ HITUNG nilai akhir  │  │ Jika ada → ubah data │  │ Jika ada → hapus data  │
│ SIMPAN ke dictionary│  │ Jika tidak → pesan   │  │ Jika tidak → pesan     │
└─────────┬───────────┘  └──────────┬──────────┘   └────────────┬──────────┘
          │                         │                         │
          └──────────────┬──────────┴───────────────┬─────────┘
                         │                          │
                         ▼                          ▼

              ┌──────────────────────┐     ┌───────────────────────┐
              │   Pilihan = 4 ?      │     │    Pilihan = 5 ?      │
              └───────────┬──────────┘     └───────────┬───────────┘
                          │                            │
                          ▼                            ▼
      ┌────────────────────────────┐   ┌─────────────────────────────┐
      │ TAMPILKAN semua data       │   │ INPUT nama yang dicari       │
      │ Jika kosong → pesan        │   │ Jika ada → tampilkan         │
      └──────────┬─────────────────┘   │ Jika tidak → pesan           │
                 │                     └──────────┬──────────────────┘
                 │                                │
                 └───────────────┬────────────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │   Pilihan = 0 ?       │
                     └────────────┬──────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │    KELUAR PROGRAM  │
                        └────────────────────┘
```
## PENJELASAN PROGRAM
1. Dictionary Data Mahasiswa
   
data_mahasiswa = {}

Semua data mahasiswa akan disimpan dalam dictionary dengan format:
```



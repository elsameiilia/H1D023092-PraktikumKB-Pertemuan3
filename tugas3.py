from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)
daftar_tugas=[]

def tambah_tugas ():
    nama_tugas = input("Nama Tugas : ")
    deadline = input("Deadline (dd-mm-yyyy): ")
    deskripsi = input("Deskripsi: ")

    try:
        deadline = datetime.strptime(deadline, "%d-%m-%Y")
    except ValueError:
        print(Fore.RED + "Format tanggal tidak valid.")
        return

    tugas = {
        "judul" : nama_tugas,
        "dl" : deadline,
        "desc" : deskripsi,
        "selesai" : False
    }
    daftar_tugas.append(tugas)
    print(Fore.BLUE + "Berhasil ditambahkan ke daftar!")

def lihat_tugas():
    if not daftar_tugas:
        print(Fore.RED + "Belum ada tugas.")
        return

    print("Daftar Tugas:")
    for idx, tugas in enumerate(daftar_tugas, start=1):
        if tugas["selesai"]:
            status = Fore.GREEN + "Selesai"
        else: 
            status = Fore.RED + "Belum Selesai"
        print(f"{idx}. {tugas['judul']} (Deadline: {tugas['dl'].strftime('%d-%m-%Y')}) - {tugas['desc']} - {status}" )

def selesai_tugas():
    lihat_tugas()
    try:
        nomor_tugas = int(input("Nomor tugas yang sudah selesai : ")) -1
        if 0<=nomor_tugas < len(daftar_tugas):
            daftar_tugas[nomor_tugas]["selesai"] = True
            print(Fore.GREEN + "Tugas berhasil diselesaikan.")
        else:
            print(Fore.RED + "Nomor tugas salah.")
    except ValueError:
        print(Fore.RED + "Input tidak valid.")

def hapus_tugas():
    lihat_tugas()
    try: 
        nomor_tugas = int(input("Nomor tugas yang ingin dihapus : ")) -1
        if 0<=nomor_tugas < len(daftar_tugas):
            tugas_terhapus = daftar_tugas.pop(nomor_tugas)
            print(Fore.GREEN + "Tugas berhasil dihapus.")
        else:
            print(Fore.RED + "Nomor tugas salah.")
    except ValueError:
        print(Fore.RED + "Input tidak valid.")

menu = [
    "1. Tambah Tugas",
    "2. Daftar Tugas",
    "3. Tandai Tugas Selesai",
    "4. Hapus Tugas",
    "5. Keluar"
]

def main():
    while True:
        print("To-do List")
        for i in menu:
            print(i)

        pilih = int(input("Pilih menu (1-5): "))

        if pilih == 1:
            tambah_tugas()
        elif pilih == 2:
            lihat_tugas()
        elif pilih == 3:
            selesai_tugas()
        elif pilih == 4:
            hapus_tugas()
        elif pilih == 5:
            print("Keluar dari program.")
            break
        else: print(Fore.RED + "Pilihan tidak valid.")

if __name__ == "__main__":
    main()        
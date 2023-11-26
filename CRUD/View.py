# INTERAKSI DENGAN VIEW
from . import operasi


def delete_console():
    read_console()
    while (True):
        print("Pilih nomer buku yang akan di delete!")
        no_buku = int(input("Nomor Buku \t= "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3];
            tahun = data_break[4][:-1]

            # DATA YANG INGIN DI HAPUS
            print("\n"+"="*100)
            print("\nData yang akan dihapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:.40}")

            is_Done = input("Apakah Yakin Dihapus? (y/n)")
            if is_Done == "y" or is_Done == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("No tidak ditemukan, masukkan nomer kembali")

    print("Data Berhasil dihapus!")


def update_console():
    read_console()
    while (True):
        print("Pilih nomer buku yang akan di update!")
        no_buku = int(input("Nomor Buku \t= "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("No tidak ditemukan, masukkan nomer kembali")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        # DATA YANG INGIN DI UPDATE
        print("\n"+"="*100)
        print("\nSilahkan pilih data yang akan diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:.40}")

        # MEMILIH MODE UPDATE
        user_option = input("Pilih option (1,2,3) ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t= "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print(
                                "Data tahun harus berupa 4 angka (yyyy), Silahkan ulangi")
                    except:
                        print(
                            "Data tahun harus berupa 4 angka (yyyy), Silahkan ulangi")

            case _: print("Index tidak cocok")

        print("\nData Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun}")
        is_Done = input("Apakah Selesai Update? (y/n)")
        if is_Done == "y" or is_Done == "Y":
            break

    operasi.update(no_buku, pk, date_add, tahun, judul, penulis)
    # print(data_buku)


def create_console():
    print(f"\n{'='*40}")
    print("Silahkan Masukkan Data Anda!")
    judul = input("Judul\t= ")
    penulis = input("Penulis\t= ")
    while True:
        try:
            tahun = int(input("Tahun\t= "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Data tahun harus berupa 4 angka (yyyy), Silahkan ulangi")
        except:
            print("Data tahun harus berupa 4 angka (yyyy), Silahkan ulangi")

    operasi.create(tahun, judul, penulis)
    print("Data berhasil di input!")
    read_console()


def read_console():
    data_file = operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # HEADER
    print("\n"+"="*100)
    print(f"{index:^4} | {judul:40} | {penulis:20} | {tahun:5}")
    print("-"*100)

    # DATA
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:^4} | {judul:.40} | {penulis:.20} | {tahun:4}", end="")

        # FOOTER
    print("="*100+"\n")

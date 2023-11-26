from . import operasi


database_name = "data.txt"
template = {
    "primekey": "xxxxxx",
    "date_add": "yyyy-mm-dd",
    "judul": " "*255,
    "penulis": " "*255,
    "tahun": "xxxx"
}


def init_console():
    try:
        with open(database_name, "r") as file:
            print("Database telah tersedia, init done!")
    except:
        print("Database tidak ditemukan, buat database baru")
        operasi.create_first_data()

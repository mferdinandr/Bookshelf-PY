# INTERAKSI DENGAN DATABASE
from . import Database
import time
from .Utility import random_str
import os


def delete(no_buku):
    print(Database.database_name)
    try:
        with open(Database.database_name, 'r') as file:
            counter = 0

            while (True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database Error!")
    os.replace("data_temp.txt", Database.database_name)


def create_first_data():
    penulis = input("Penulis\t= ")
    judul = input("Judul\t= ")
    while True:
        try:
            tahun = int(input("Tahun\t= "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Data tahun harus berupa 4 angka (yyyy), Silahkan ulangi")
        except:
            print("Data tahun harus berupa 4 angka (yyyy), Silahkan ulangi")

    data = Database.template.copy()

    data["pk"] = random_str(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.template["penulis"][len(penulis):]
    data["judul"] = judul + Database.template["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.database_name, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print('Data ILANG')


def update(no_buku, pk, date_add, tahun, judul, penulis):
    data = Database.template.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.template["penulis"][len(penulis):]
    data["judul"] = judul + Database.template["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with (open(Database.database_name, 'r+', encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("Update Error!")


def create(tahun, judul, penulis):
    data = Database.template.copy()

    data["pk"] = random_str(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.template["penulis"][len(penulis):]
    data["judul"] = judul + Database.template["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    try:
        with open(Database.database_name, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print('Data Gagal Ditambahkan!')


def read(**kwargs):
    try:
        with open(Database.database_name, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            print(jumlah_buku)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]

            else:
                return content
    except:
        print("Database Eror")
        return False

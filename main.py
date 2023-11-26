import os
import CRUD as CRUD

# CLEAR TAMPILAN
if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print(f"{'SELAMAT DATANG DI PROGRAM':^40}")
    print(f"{'DATABASE PERPUSTAKAAN':^40}")
    print("="*40)

# CHECK DATABASE
    CRUD.init_console()

    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(f"{'SELAMAT DATANG DI PROGRAM':^40}")
        print(f"{'DATABASE PERPUSTAKAAN':^40}")
        print("="*40)

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("Masukkan Opsi = ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_Done = input("Apakah Selesai? (y/n)")
        if is_Done == "y" or is_Done == "Y":
            break
    print("SELESAI")

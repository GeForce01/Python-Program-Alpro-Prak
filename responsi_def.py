def clear():
    import os
    os.system('cls')
aktivitas=[]
def show_data():
    print("=============")
    print("To Do List : ")

    if len(aktivitas) <= 0 :
        print("Belum Ada Aktivitas ")
    else:
        for indeks in range(len(aktivitas)):
            print(indeks+1,aktivitas[indeks])

    print("=============")

def add_data():
    aktivitas_baru=str(input("Tulis Aktivitas = "))
    aktivitas.append(aktivitas_baru)

def remove_data():
    if len(aktivitas) <= 0 :
        print("To Do List Masih Kosong")
        input("Tekan ENTER Untuk Melanjukan")
    else: 
        if len(aktivitas) > 0 :
            hapus=int(input("No Aktivitas Yang Ingin Di Hapus = "))
            if (hapus==1):
                aktivitas.pop(0)
            elif (hapus > 1):
                hapus=hapus-1
                aktivitas.pop(hapus) 
            else:
                print("Aktivitas Yang Dipilih Tidak Ada !")
                input("Tekan ENTER Untuk Melanjutkan")
def show_menu():
    print("\n")
    clear()
    show_data()
    input("Ketuk ENTER Untuk Menampilkan Menu")
    print("MENU")
    print("1. Tambah To Do List")
    print("2. Coret Do List")
    print("3. Keluar")
    menu=int(input("Pilih Menu = "))
    print("\n")

    if (menu==1):
        clear()
        show_data()
        add_data()
    elif (menu==2):
        clear()
        show_data()
        remove_data()
    elif (menu==3):
        exit()
    else:
        print("Menu Yang Anda Pilih Tidak Tersedia !")

if (__name__ == "__main__"):
    while(True):
        show_menu()
aktivitas=[]
indeks=1
menu=0
while(menu != 3):
    print("=============")
    print("To Do List : ")

    if len(aktivitas) <= 0 :
        print("Belum Ada Aktivitas ")
    else:
        for indeks in range(len(aktivitas)):
            print(indeks+1,aktivitas[indeks])
    print("=============")
    input("Ketuk ENTER Untuk Menampilkan Menu")
    print("MENU")
    print("1. Tambah To Do List")
    print("2. Coret Do List")
    print("3. Keluar")

    menu=int(input("Pilih Menu = "))

    if(menu==1):
        aktivitas_baru=str(input("Tulis Aktivitas = "))
        aktivitas.append(aktivitas_baru)

    elif(menu==2):
        if len(aktivitas) <= 0 :
            print("To Do List Masih Kosong")
            input("Tekan ENTER Untuk Melanjukan")
        else: 
            if len(aktivitas) >= 1:
                hapus=int(input("No Aktivitas Yang Ingin Di Hapus = "))
                hapus=hapus-1
                if(hapus==indeks):
                    aktivitas.pop(hapus) 
                else:
                    print("Aktivitas Yang Dipilih Tidak Ada !")
                    input("Tekan ENTER Untuk Melanjutkan")
    
    elif(menu==3):
        exit
    
    else:
        print("Menu Yang Anda Pilih Tidak Tersedia")
        input("Tekan Enter Untuk Melanjutkan")




#===================================================#
#Program Kasir untuk mencatat belanja pelanggan    
#Program ini memiliki tiga menu, yakni:            
#   1. Catat transaksi baru                        
#   2. Lihat laporan transaksi                     
#   3. Keluar                                      
#===================================================#
#import library
#---------------------------------------------------#
import os

#---------------------------------------------------#
#sub program (fungsi dan prosedur)
#---------------------------------------------------#
def catat_transaksi():
    #inisialisasi variabel lokal
    lagi = 'Y'
    total_harga = 0

    #perulangan selama user ingin input data transaksi
    while (lagi.upper() != 'T'):
        #bersihkan layar
        os.system('cls')

        #meminta input kode dan jumlah barang yang dibeli
        kode = input("Input kode barang\t: ")
        jumlah = int(input("Jumlah barang\t\t: "))

        #mencari data barang dari dalam list_barang
        for barang in list_barang:
            #cek apakah kode barang sama dengan yang diinput user
            if (barang["kode"] == kode.lower()):
                #update total_harga
                total_harga = total_harga + (jumlah * barang["harga"])

                #tampilkan nama, harga, dan sub total harga barang
                print("Nama barang\t\t:", barang["nama"] )
                print("Harga satuan\t\t: Rp", barang["harga"] )
                print("---------------------------------")
                print("TOTAL TRANSAKSI\t: Rp", total_harga)
                print("---------------------------------")

                #update data 'jumlah_transaksi' dari barang tersebut
                barang["jumlah_transaksi"] = barang["jumlah_transaksi"] + jumlah

        #tanya user apakah mau input data transaksi lagi atau tidak
        lagi = input("Input data belanja lagi (Y/T)? ")

def pilih_menu():
    #tampilkan menu
    print("MENU PROGRAM:")
    print("1. Catat transaksi baru")
    print("2. Lihat laporan transaksi")
    print("3. Keluar")

    #meminta input menu dari user
    pilih = int(input("Pilih menu: "))

    #mengembalikan nilai variabel 'pilih' ke program utama
    return pilih

def tampil_laporan (list_barang):
    #cetak header tabel
    print("-" * 53)
    print("Kode".ljust(8), "Nama Barang".ljust(15), "Harga".ljust(11), "Jumlah Transaksi".ljust(18))
    print("-" * 53)

    #tampilkan isi list_belanja
    for barang in list_barang:
        print(barang["kode"].ljust(8), barang["nama"].ljust(15), str(barang["harga"]).ljust(11), str(barang["jumlah_transaksi"]).ljust(18))

    #cetak garis bawah
    print("-" * 53)


#---------------------------------------------------#
#program utama
#---------------------------------------------------#
#variabel menu
menu = 0

#menyiapkan list yang berisi dictionary untuk menyimpan data SEMUA barang
list_barang = [{"kode" : 'p01', "nama" : 'susu', 'harga' : 3000, 'jumlah_transaksi' : 0},
               {"kode" : 'p02', "nama" : 'roti', 'harga' : 7000, 'jumlah_transaksi' : 0},
               {"kode" : 'p03', "nama" : 'gula', 'harga' : 9000, 'jumlah_transaksi' : 0},
               {"kode" : 'p04', "nama" : 'kopi', 'harga' : 5000, 'jumlah_transaksi' : 0}]        

while (menu != 3):
    #bersihkan layar
    os.system('cls')

    #pilih menu
    menu = pilih_menu()

    #cek menu
    if (menu == 1):
        #catat transaksi belanja
        catat_transaksi()

    elif (menu == 2):
        #tampilkan laporan transaksi belanja
        tampil_laporan(list_barang)
        
        #berhenti hingga user menekan ENTER
        input("Tekan ENTER untuk melanjutkan ")
    
    elif (menu == 3):
        #menampilkan informasi bahwa user telah keluar dari program
        print ("Anda telah keluar dari program.")

    else:
        #menampilkan informasi bahwa menu yang diinputkan tidak tersedia
        print("Menu yang dipilih tidak tersedia.")

        #berhenti hingga user menekan ENTER
        input("Tekan ENTER untuk melanjutkan ")

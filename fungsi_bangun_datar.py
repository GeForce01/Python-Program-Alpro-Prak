#library
import os

#Program Bangun Datar
#Sub Program
def hitungKeliling(panjang, lebar): #parameter formal
    return 2 * (panjang + lebar)

def hitungLuas():
    panjang = int(input("Panjang: "))
    lebar = int(input("Lebar: "))
    luas = panjang * lebar
    return luas

def hitungVolume():
    panjang = int(input("Panjang: "))
    lebar = int(input("Lebar: "))
    tinggi = int(input("Tinggi: "))
    volume = panjang * lebar * tinggi
    print("Volume balok =", volume)

def tampilMenu():
    os.system("cls")    #membersihkan layar
    print("Program Menghitung Keliling dan Luas Persegi Panjang")
    print("1. Keliling Persegi Panjang")
    print("2. Luas Persegi Panjang")
    print("3. Volume Balok")
    print("4. Keluar")

#Program Utama
pilih = 0
while (pilih != 4):
    tampilMenu()
    pilih = int(input("Pilih menu: "))

    if (pilih == 1):
        panjang = int(input("Panjang: "))
        lebar = int(input("Lebar: "))

        keliling = hitungKeliling(panjang, lebar)   #parameter aktual
        print("Keliling persegi panjang =", keliling)
    elif (pilih == 2):
        print("Luas persegi panjang =", hitungLuas())
    elif (pilih == 3):
        hitungVolume()
    elif (pilih == 4):
        print("Anda telah keluar.")
    else:
        print("Menu yang dipilih tidak tersedia.")    

    input()

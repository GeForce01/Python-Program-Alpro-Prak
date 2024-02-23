#program konversi mata uang
#Library
import os

#sub program
def idr_to_usd(idr, kurs=14000):    #nilai default
    usd = idr / kurs
    return round(usd)

def usd_to_idr(usd, kurs=14000):
    idr = usd * kurs
    return round(idr)

#program utama
pilih = 0
while (pilih != 3):
    os.system("cls")    #membersihkan layar
    print("Program Konversi Mata Uang IDR-USD")
    print("1. Konversi IDR ke USD")
    print("2. Konversi USD ke IDR")
    print("3. Keluar")
    pilih = int(input("Pilih menu: "))

    if (pilih == 1):
        nominal = float(input("Nominal IDR: "))
        print("Nominal USD =", idr_to_usd(kurs=15000, idr=nominal))
    elif (pilih == 2):
        nominal = float(input("Nominal USD: "))
        print("Nominal IDR =", usd_to_idr(nominal, 15000))
    elif (pilih == 3):
        print("Anda telah keluar.")
    else:
        print("Menu yang dipilih tidak ada.")
    
    input()
def clear():    #def clear digunakan untuk membuat program yang akan dipanggil
    import os
    os.system('cls')
def data1():
    r=int(input("Masukkan Nominal IDR =Rp."))
    u=0.00007077
    n=r*u
    print("Nilai USD =$.",n)

def data2():
    r=int(input("Masukkan Nominal IDR =Rp."))
    e=0.00005975
    n=r*e
    print("Nilai EURO =€.",n)

def data3():
    u=int(input("Masukkan Nominal USD =$."))
    r=14.130
    n=u*r
    print("Nilai IDR =Rp.",n)

def data4():
    u=int(input("Masukkan Nominal USD =$."))
    e=0.8442
    n=u*e
    print("Nilai EURO =€.",n)

def data5():
    e=int(input("Masukkan Nominal EURO =€."))
    r=16.742
    n=e*r
    print("Nilai IDR =Rp.",n)

def data6():
    e=int(input("Masukkan Nominal EURO =€."))
    u=1.1846
    n=e*u
    print("Nilai USD =$.",n)

def show_menu():
    print("\n")
    print("==========Menu==========")
    print("1. Konversi IDR ke USD")
    print("2. Konversi IDR ke EURO")
    print("3. Konversi USD ke IDR")
    print("4. Konversi USD ke EURO")
    print("5. Konversi EURO ke IDR")
    print("6. Konversi EURO ke USD")
    print("7. Exit")
    print("========================")
    menu=int(input("Pilih Menu = "))
    print("\n")

    if (menu==1):
        clear()     #clear digunakan untuk memanggil program def clear
        data1()
    elif (menu==2):
        clear()
        data2()
    elif (menu==3):
        clear()
        data3()
    elif (menu==4):
        clear()
        data4()
    elif (menu==5):
        clear()
        data5()
    elif (menu==6):
        clear()
        data6()
    elif (menu==7):
        exit()
    else:
        clear()
        print("Menu Yang Anda Pilih Tidak Tersedia !")

if (__name__=="__main__"):
    while(True):
        show_menu()
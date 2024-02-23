print("Menghitung Luas Bangun Datar")
print("============MENU============")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")
print("============================")

pilihan=int(input("Silahkan Pilih Menu = "))

if(pilihan==1):
    print("apa yang akan anda hitung ? ")
    print("1. Keliling Persegi ")
    print("2. Luas Persegi ") 
    pilihan=int(input("Masukkan Pilihan Anda = " ))
    if(pilihan==1):
        print("Maaf Pilihan Anda Tidak Tersedia Untuk Saat Ini")
        print("========Terima Kasih========")

    elif(pilihan==2):
        s=float(input("Masukkan Panjang sisi = "))
        l=s*s
        print("Luas Persegi Adalah = ",l)
        print("========Terima Kasih========")

    else:
        print("Maaf Pilihan Yang Anda Masukkan Salah")
        print("========Terima Kasih========")

elif(pilihan==2):
    print("Apa Yang Akan Anda Hitung ? ")
    print("1. Keliling Persegi Panjang")
    print("2. Luas Persegi Panjang")
    pilihan=int(input("Masukkan Pilihan Anda = "))
    if(pilihan==1):
        print("Maaf Pilihan Anda Tidak Tersedia Untuk Saat Ini")
        print("========Terima Kasih========")

    elif(pilihan==2):
        p=float(input("Masukkan Panjang = "))  
        l=float(input("Masukkan Lebar = " ))
        luas=p*l
        print("Luas Persegi Panjang Adalah = ",luas)
        print("========Terima Kasih========")

    else:
        print("Maaf Pilihan Yang Anda Masukkan Salah") 
        print("========Terima Kasih========")

elif(pilihan==3):
    print("Apa Yang Akan Anda Hitung ? ")
    print("1. Keliling Segitiga")
    print("2. Luas Segitiga")
    pilihan=int(input("Masukkan Pilihan Anda = "))
    
    if(pilihan==1):
        print("Maaf Pilihan Anda Tidak Tersedia Untuk Saat Ini")
        print("========Terima Kasih========")

    elif(pilihan==2):
        a=float(input("Masukkan Panjang Alas = "))
        t=float(input("Masukkan Tinggi = "))
        l=1/2*a*t
        print("Luas Segitiga Adalah = ",l)
        print("========Terima Kasih========")

    else:
        print("Maaf Pilihan Yang Anda Masukkan Salah")
        print("========Terima Kasih========")

elif(pilihan==4):
    print("Apa Yang Akan Anda Hitung ? ")
    print("1. Keliling Lingkaran")
    print("2. Luas Lingkaran")
    pilihan=float(input("Masukkan Pilihan Anda = "))

    if(pilihan==1):
        print("Maaf Pilihan Anda Tidak Tersedia Untuk Saat Ini")
        print("========Terima Kasih========")

    elif(pilihan==2):
        r=float(input("Masukkan Jari-Jari = "))
        v=float(22/7)
        
        l=v*r**2
        print("Luas Lingkaran Adalah = ",l)
        print("========Terima Kasih========")

    else:
        print("Maaf Plilihan Yang Anda Masukkan Salah")
        print("========Terima Kasih========")

else:
    print("Maaf Menu Yang Anda Masukkan Salah")
    print("========Terima Kasih========")